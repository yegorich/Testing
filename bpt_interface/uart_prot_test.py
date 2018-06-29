#!/usr/bin/python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import logging
import argparse

import serial

from bpt_if import BptIf


class RiotProtocolTest(object):

    def autoconnect(self, used_com=[]):
        logging.debug("Autoconnecting")
        logging.debug("Set DUT UART to echo mode")
        cmd_info = self.bpt.set_uart_mode()
        if cmd_info.result != 'Success':
            logging.error(
                "Failed to set UART mode: {}".format(cmd_info.result))
            return None

        cmd_info = self.bpt.set_uart_baud(115200)
        if cmd_info.result != 'Success':
            logging.error(
                "Failed to set UART mode: {}".format(cmd_info.result))
            return None

        cmd_info = self.bpt.execute_changes()
        if cmd_info.result != 'Success':
            logging.error(
                "Failed to excute changes: {}".format(cmd_info.result))
            return None

        found_connection = False
        comlist = serial.tools.list_ports.comports()
        connected = []
        for element in comlist:
            if (element.device not in used_com):
                connected.append(element.device)
        for port in connected:
            logging.debug("Port: " + port)
            self.dev = serial.serial_for_url(
                port, baudrate=115200, timeout=0.1)
            expected_val = b'\x30\x30\x0a'
            self.dev.write(expected_val)
            ret = self.dev.readline()
            try:
                logging.debug("ID rx: %s" % ret)
                logging.debug("ID expected: %s" % expected_val)
                if (ret == expected_val):
                    logging.debug("Found connection")
                    found_connection = True
                    break
            except TypeError:
                logging.debug("Cannot connect, type error")
            except ValueError:
                logging.debug("Cannot connect, value error")
            except Exception as e:
                logging.debug(e)
            self.dev.close()

        return found_connection

    def __init__(self, port=None, dut_port=None):
        self.bpt = BptIf(port=port)
        if dut_port is None:
            self.autoconnect(used_com=[self.bpt.get_port()])
        else:
            self.dev = serial.serial_for_url(
                dut_port, baudrate=115200, timeout=1)

    def echo_test(self):
        # set UART mode to echo
        cmd_info = self.bpt.set_uart_mode()
        if cmd_info.result != 'Success':
            logging.error("Failed to set UART mode: {}".format(cmd_info.result))
            return False

        cmd_info = self.bpt.set_uart_baud(115200)
        if cmd_info.result != 'Success':
            logging.error(
                "Failed to set UART mode: {}".format(cmd_info.result))
            return None

        cmd_info = self.bpt.execute_changes()
        if cmd_info.result != 'Success':
            logging.error("Failed to excute changes: {}".format(cmd_info.result))
            return False

        test_str = b'\x30\x30\x0a'
        try:
            self.dev.write(test_str)
            result = self.dev.readline()
        except Exception as err:
            logging.error(err)
            return False

        if len(result) != 3:
            logging.error("Received wrong character number: {} instead of {}".format(len(result), len(test_str)))
            return False

        if result != test_str:
            logging.error("Wrong string received")
            return False

        logging.debug('Received string: {}'.format(result))

        return True

    def echo_test_wrong_baudrate(self):
        # set UART mode to echo
        cmd_info = self.bpt.set_uart_mode()
        if cmd_info.result != 'Success':
            logging.error("Failed to set UART mode: {}".format(cmd_info.result))
            return False

        cmd_info = self.bpt.set_uart_baud(9600)
        if cmd_info.result != 'Success':
            logging.error(
                "Failed to set UART mode: {}".format(cmd_info.result))
            return None

        cmd_info = self.bpt.execute_changes()
        if cmd_info.result != 'Success':
            logging.error("Failed to excute changes: {}".format(cmd_info.result))
            return False

        test_str = b'\x30\x30\x0a'
        try:
            self.dev.write(test_str)
            result = self.dev.readline()
        except Exception as err:
            logging.error(err)
            return False

        if len(result) != 3:
            logging.error("Received wrong character number: {} instead of {}".format(len(result), len(test_str)))
            return True

        if result != test_str:
            logging.error("Wrong string received")
            return True

        logging.debug('Received string: {}'.format(result))

        return False

    def echo_ext_test(self):
        # set UART mode to echo_ext
        cmd_info = self.bpt.set_uart_mode(1)
        if cmd_info.result != 'Success':
            logging.error("Failed to set UART mode: {}".format(cmd_info.result))
            return False

        cmd_info = self.bpt.set_uart_baud(115200)
        if cmd_info.result != 'Success':
            logging.error(
                "Failed to set UART mode: {}".format(cmd_info.result))
            return None

        cmd_info = self.bpt.execute_changes()
        if cmd_info.result != 'Success':
            logging.error("Failed to excute changes: {}".format(cmd_info.result))
            return False

        test_str = b'\x30\x30\x0a'
        try:
            self.dev.write(test_str)
            result = self.dev.readline()
        except Exception as err:
            logging.error(err)
            return False

        if len(result) != 3:
            logging.error("Received wrong character number: {} instead of {}".format(len(result), len(test_str)))
            return False

        if result != b'\x31\x31\x0a':
            logging.error("Wrong string received")
            return False

        logging.debug('Received string: {}'.format(result))

        return True


    def reg_read_test(self):
        # set UART mode to echo_ext
        cmd_info = self.bpt.set_uart_mode(2)
        if cmd_info.result != 'Success':
            logging.error("Failed to set UART mode: {}".format(cmd_info.result))
            return False

        cmd_info = self.bpt.execute_changes()
        if cmd_info.result != 'Success':
            logging.error("Failed to excute changes: {}".format(cmd_info.result))
            return False

        test_str = 'rr 152 10\n'
        try:
            self.dev.write(test_str.encode('utf-8'))
            result = self.dev.readline()
        except Exception as err:
            logging.error(err)
            return False

        if result != b'0,0x09080706050403020100\n':
            logging.error("Wrong string received")
            return False

        logging.debug('Received string: {}'.format(result))

        return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--log", help='Set the logging level (DEBUG, INFO, WARN)')
    parser.add_argument("--port", help='Serial port for BPT communication')
    parser.add_argument("--dutport", help='Serial port for DUT communication')
    args = parser.parse_args()

    if args.log is not None:
        loglevel = args.log
        numeric_level = getattr(logging, loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % loglevel)
        logging.basicConfig(level=loglevel)

    test = RiotProtocolTest(port=args.port, dut_port=args.dutport)
    if test.echo_test():
        logging.info("Echo test: OK")
    else:
        logging.info("Echo test: failed")

    if test.echo_test_wrong_baudrate():
        logging.info("Echo test wrong baudrate: OK")
    else:
        logging.info("Echo test wrong baudrate: failed")

    if test.echo_ext_test():
        logging.info("Echo extended test: OK")
    else:
        logging.info("Echo extended test: failed")

    if test.reg_read_test():
        logging.info("Register read test: OK")
    else:
        logging.info("Register read test: failed")


if __name__ == "__main__":
    main()
