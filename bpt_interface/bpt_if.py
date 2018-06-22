import base_if


class BptIf(base_if.BaseIf):

    def __init__(self, port=None, baud=115200):

        if (port is None):
            self.autoconnect(0x42A5, self.get_sys_device_num)
        else:
            self.connect(port, baud)

    def get_sys_sn12(self):
        return self.read_bytes(0, 12)

    def set_sys_sn12(self, data=0):
        return self.write_bytes(0, data, 12)

    def get_sys_fw_rev(self):
        return self.read_bytes(12, 4)

    def set_sys_fw_rev(self, data=0):
        return self.write_bytes(12, data, 4)

    def get_sys_build_time_second(self):
        return self.read_bytes(16, 1)

    def set_sys_build_time_second(self, data=0):
        return self.write_bytes(16, data, 1)

    def get_sys_build_time_minute(self):
        return self.read_bytes(17, 1)

    def set_sys_build_time_minute(self, data=0):
        return self.write_bytes(17, data, 1)

    def get_sys_build_time_hour(self):
        return self.read_bytes(18, 1)

    def set_sys_build_time_hour(self, data=0):
        return self.write_bytes(18, data, 1)

    def get_sys_build_time_day_of_month(self):
        return self.read_bytes(19, 1)

    def set_sys_build_time_day_of_month(self, data=0):
        return self.write_bytes(19, data, 1)

    def get_sys_build_time_day_of_week(self):
        return self.read_bytes(20, 1)

    def set_sys_build_time_day_of_week(self, data=0):
        return self.write_bytes(20, data, 1)

    def get_sys_build_time_month(self):
        return self.read_bytes(21, 1)

    def set_sys_build_time_month(self, data=0):
        return self.write_bytes(21, data, 1)

    def get_sys_build_time_year(self):
        return self.read_bytes(22, 1)

    def set_sys_build_time_year(self, data=0):
        return self.write_bytes(22, data, 1)

    def get_sys_build_time_res1(self):
        return self.read_bytes(23, 1)

    def set_sys_build_time_res1(self, data=0):
        return self.write_bytes(23, data, 1)

    def get_sys_device_num(self):
        return self.read_bytes(24, 4)

    def set_sys_device_num(self, data=0):
        return self.write_bytes(24, data, 4)

    def get_sys_cr(self):
        return self.read_bytes(28, 1)

    def set_sys_cr(self, data=0):
        return self.write_bytes(28, data, 1)

    def get_sys_res3(self):
        return self.read_bytes(29, 3)

    def set_sys_res3(self, data=0):
        return self.write_bytes(29, data, 3)

    def get_i2c_mode(self):
        return self.read_bytes(32, 1)

    def set_i2c_mode(self, data=0):
        return self.write_bytes(32, data, 1)

    def get_i2c_error_code(self):
        return self.read_bytes(33, 2)

    def set_i2c_error_code(self, data=0):
        return self.write_bytes(33, data, 2)

    def get_i2c_clk_stretch_delay(self):
        return self.read_bytes(35, 2)

    def set_i2c_clk_stretch_delay(self, data=0):
        return self.write_bytes(35, data, 2)

    def get_i2c_inject_failure_mode(self):
        return self.read_bytes(37, 1)

    def set_i2c_inject_failure_mode(self, data=0):
        return self.write_bytes(37, data, 1)

    def get_i2c_slave_addr_1(self):
        return self.read_bytes(38, 2)

    def set_i2c_slave_addr_1(self, data=0):
        return self.write_bytes(38, data, 2)

    def get_i2c_slave_addr_2(self):
        return self.read_bytes(40, 2)

    def set_i2c_slave_addr_2(self, data=0):
        return self.write_bytes(40, data, 2)

    def get_i2c_r_count(self):
        return self.read_bytes(42, 1)

    def set_i2c_r_count(self, data=0):
        return self.write_bytes(42, data, 1)

    def get_i2c_w_count(self):
        return self.read_bytes(43, 1)

    def set_i2c_w_count(self, data=0):
        return self.write_bytes(43, data, 1)

    def get_i2c_res4(self):
        return self.read_bytes(44, 4)

    def set_i2c_res4(self, data=0):
        return self.write_bytes(44, data, 4)

    def get_spi_mode(self):
        return self.read_bytes(48, 1)

    def set_spi_mode(self, data=0):
        return self.write_bytes(48, data, 1)

    def get_spi_error_code(self):
        return self.read_bytes(49, 4)

    def set_spi_error_code(self, data=0):
        return self.write_bytes(49, data, 4)

    def get_spi_res11(self):
        return self.read_bytes(53, 11)

    def set_spi_res11(self, data=0):
        return self.write_bytes(53, data, 11)

    def get_uart_mode(self):
        return self.read_bytes(64, 1)

    def set_uart_mode(self, data=0):
        return self.write_bytes(64, data, 1)

    def get_uart_error_code(self):
        return self.read_bytes(65, 2)

    def set_uart_error_code(self, data=0):
        return self.write_bytes(65, data, 2)

    def get_uart_baud(self):
        return self.read_bytes(67, 4)

    def set_uart_baud(self, data=0):
        return self.write_bytes(67, data, 4)

    def get_uart_reg_output(self):
        return self.read_bytes(71, 1)

    def set_uart_reg_output(self, data=0):
        return self.write_bytes(71, data, 1)

    def get_uart_size(self):
        return self.read_bytes(72, 1)

    def set_uart_size(self, data=0):
        return self.write_bytes(72, data, 1)

    def get_uart_res7(self):
        return self.read_bytes(73, 7)

    def set_uart_res7(self, data=0):
        return self.write_bytes(73, data, 7)

    def get_rtc_second(self):
        return self.read_bytes(80, 1)

    def set_rtc_second(self, data=0):
        return self.write_bytes(80, data, 1)

    def get_rtc_minute(self):
        return self.read_bytes(81, 1)

    def set_rtc_minute(self, data=0):
        return self.write_bytes(81, data, 1)

    def get_rtc_hour(self):
        return self.read_bytes(82, 1)

    def set_rtc_hour(self, data=0):
        return self.write_bytes(82, data, 1)

    def get_rtc_day_of_month(self):
        return self.read_bytes(83, 1)

    def set_rtc_day_of_month(self, data=0):
        return self.write_bytes(83, data, 1)

    def get_rtc_day_of_week(self):
        return self.read_bytes(84, 1)

    def set_rtc_day_of_week(self, data=0):
        return self.write_bytes(84, data, 1)

    def get_rtc_month(self):
        return self.read_bytes(85, 1)

    def set_rtc_month(self, data=0):
        return self.write_bytes(85, data, 1)

    def get_rtc_year(self):
        return self.read_bytes(86, 1)

    def set_rtc_year(self, data=0):
        return self.write_bytes(86, data, 1)

    def get_rtc_res1(self):
        return self.read_bytes(87, 1)

    def set_rtc_res1(self, data=0):
        return self.write_bytes(87, data, 1)

    def get_adc0_mode(self):
        return self.read_bytes(88, 1)

    def set_adc0_mode(self, data=0):
        return self.write_bytes(88, data, 1)

    def get_adc0_error_code(self):
        return self.read_bytes(89, 2)

    def set_adc0_error_code(self, data=0):
        return self.write_bytes(89, data, 2)

    def get_adc0_sample_rate(self):
        return self.read_bytes(91, 1)

    def set_adc0_sample_rate(self, data=0):
        return self.write_bytes(91, data, 1)

    def get_adc0_value(self):
        return self.read_bytes(92, 4)

    def set_adc0_value(self, data=0):
        return self.write_bytes(92, data, 4)

    def get_adc0_res8(self):
        return self.read_bytes(96, 8)

    def set_adc0_res8(self, data=0):
        return self.write_bytes(96, data, 8)

    def get_adc1_mode(self):
        return self.read_bytes(104, 1)

    def set_adc1_mode(self, data=0):
        return self.write_bytes(104, data, 1)

    def get_adc1_error_code(self):
        return self.read_bytes(105, 2)

    def set_adc1_error_code(self, data=0):
        return self.write_bytes(105, data, 2)

    def get_adc1_sample_rate(self):
        return self.read_bytes(107, 1)

    def set_adc1_sample_rate(self, data=0):
        return self.write_bytes(107, data, 1)

    def get_adc1_value(self):
        return self.read_bytes(108, 4)

    def set_adc1_value(self, data=0):
        return self.write_bytes(108, data, 4)

    def get_adc1_res8(self):
        return self.read_bytes(112, 8)

    def set_adc1_res8(self, data=0):
        return self.write_bytes(112, data, 8)

    def get_pwm_mode(self):
        return self.read_bytes(120, 1)

    def set_pwm_mode(self, data=0):
        return self.write_bytes(120, data, 1)

    def get_pwm_error_code(self):
        return self.read_bytes(121, 2)

    def set_pwm_error_code(self, data=0):
        return self.write_bytes(121, data, 2)

    def get_pwm_duty(self):
        return self.read_bytes(123, 1)

    def set_pwm_duty(self, data=0):
        return self.write_bytes(123, data, 1)

    def get_pwm_freq(self):
        return self.read_bytes(124, 4)

    def set_pwm_freq(self, data=0):
        return self.write_bytes(124, data, 4)

    def get_pwm_res8(self):
        return self.read_bytes(128, 8)

    def set_pwm_res8(self, data=0):
        return self.write_bytes(128, data, 8)

    def get_tmr_mode(self):
        return self.read_bytes(136, 1)

    def set_tmr_mode(self, data=0):
        return self.write_bytes(136, data, 1)

    def get_tmr_error_code(self):
        return self.read_bytes(137, 2)

    def set_tmr_error_code(self, data=0):
        return self.write_bytes(137, data, 2)

    def get_tmr_duty(self):
        return self.read_bytes(139, 1)

    def set_tmr_duty(self, data=0):
        return self.write_bytes(139, data, 1)

    def get_tmr_freq(self):
        return self.read_bytes(140, 4)

    def set_tmr_freq(self, data=0):
        return self.write_bytes(140, data, 4)

    def get_tmr_hi_us(self):
        return self.read_bytes(144, 4)

    def set_tmr_hi_us(self, data=0):
        return self.write_bytes(144, data, 4)

    def get_tmr_lo_us(self):
        return self.read_bytes(148, 4)

    def set_tmr_lo_us(self, data=0):
        return self.write_bytes(148, data, 4)

    def get_res104(self):
        return self.read_bytes(152, 104)

    def set_res104(self, data=0):
        return self.write_bytes(152, data, 104)

    def get_command_list(self):
        cmds = list()
        cmds.append(self.set_sys_sn12)
        cmds.append(self.get_sys_sn12)
        cmds.append(self.set_sys_fw_rev)
        cmds.append(self.get_sys_fw_rev)
        cmds.append(self.set_sys_build_time_second)
        cmds.append(self.get_sys_build_time_second)
        cmds.append(self.set_sys_build_time_minute)
        cmds.append(self.get_sys_build_time_minute)
        cmds.append(self.set_sys_build_time_hour)
        cmds.append(self.get_sys_build_time_hour)
        cmds.append(self.set_sys_build_time_day_of_month)
        cmds.append(self.get_sys_build_time_day_of_month)
        cmds.append(self.set_sys_build_time_day_of_week)
        cmds.append(self.get_sys_build_time_day_of_week)
        cmds.append(self.set_sys_build_time_month)
        cmds.append(self.get_sys_build_time_month)
        cmds.append(self.set_sys_build_time_year)
        cmds.append(self.get_sys_build_time_year)
        cmds.append(self.set_sys_build_time_res1)
        cmds.append(self.get_sys_build_time_res1)
        cmds.append(self.set_sys_device_num)
        cmds.append(self.get_sys_device_num)
        cmds.append(self.set_sys_cr)
        cmds.append(self.get_sys_cr)
        cmds.append(self.set_sys_res3)
        cmds.append(self.get_sys_res3)
        cmds.append(self.set_i2c_mode)
        cmds.append(self.get_i2c_mode)
        cmds.append(self.set_i2c_error_code)
        cmds.append(self.get_i2c_error_code)
        cmds.append(self.set_i2c_clk_stretch_delay)
        cmds.append(self.get_i2c_clk_stretch_delay)
        cmds.append(self.set_i2c_inject_failure_mode)
        cmds.append(self.get_i2c_inject_failure_mode)
        cmds.append(self.set_i2c_slave_addr_1)
        cmds.append(self.get_i2c_slave_addr_1)
        cmds.append(self.set_i2c_slave_addr_2)
        cmds.append(self.get_i2c_slave_addr_2)
        cmds.append(self.set_i2c_r_count)
        cmds.append(self.get_i2c_r_count)
        cmds.append(self.set_i2c_w_count)
        cmds.append(self.get_i2c_w_count)
        cmds.append(self.set_i2c_res4)
        cmds.append(self.get_i2c_res4)
        cmds.append(self.set_spi_mode)
        cmds.append(self.get_spi_mode)
        cmds.append(self.set_spi_error_code)
        cmds.append(self.get_spi_error_code)
        cmds.append(self.set_spi_res11)
        cmds.append(self.get_spi_res11)
        cmds.append(self.set_uart_mode)
        cmds.append(self.get_uart_mode)
        cmds.append(self.set_uart_error_code)
        cmds.append(self.get_uart_error_code)
        cmds.append(self.set_uart_baud)
        cmds.append(self.get_uart_baud)
        cmds.append(self.set_uart_reg_output)
        cmds.append(self.get_uart_reg_output)
        cmds.append(self.set_uart_size)
        cmds.append(self.get_uart_size)
        cmds.append(self.set_uart_res7)
        cmds.append(self.get_uart_res7)
        cmds.append(self.set_rtc_second)
        cmds.append(self.get_rtc_second)
        cmds.append(self.set_rtc_minute)
        cmds.append(self.get_rtc_minute)
        cmds.append(self.set_rtc_hour)
        cmds.append(self.get_rtc_hour)
        cmds.append(self.set_rtc_day_of_month)
        cmds.append(self.get_rtc_day_of_month)
        cmds.append(self.set_rtc_day_of_week)
        cmds.append(self.get_rtc_day_of_week)
        cmds.append(self.set_rtc_month)
        cmds.append(self.get_rtc_month)
        cmds.append(self.set_rtc_year)
        cmds.append(self.get_rtc_year)
        cmds.append(self.set_rtc_res1)
        cmds.append(self.get_rtc_res1)
        cmds.append(self.set_adc0_mode)
        cmds.append(self.get_adc0_mode)
        cmds.append(self.set_adc0_error_code)
        cmds.append(self.get_adc0_error_code)
        cmds.append(self.set_adc0_sample_rate)
        cmds.append(self.get_adc0_sample_rate)
        cmds.append(self.set_adc0_value)
        cmds.append(self.get_adc0_value)
        cmds.append(self.set_adc0_res8)
        cmds.append(self.get_adc0_res8)
        cmds.append(self.set_adc1_mode)
        cmds.append(self.get_adc1_mode)
        cmds.append(self.set_adc1_error_code)
        cmds.append(self.get_adc1_error_code)
        cmds.append(self.set_adc1_sample_rate)
        cmds.append(self.get_adc1_sample_rate)
        cmds.append(self.set_adc1_value)
        cmds.append(self.get_adc1_value)
        cmds.append(self.set_adc1_res8)
        cmds.append(self.get_adc1_res8)
        cmds.append(self.set_pwm_mode)
        cmds.append(self.get_pwm_mode)
        cmds.append(self.set_pwm_error_code)
        cmds.append(self.get_pwm_error_code)
        cmds.append(self.set_pwm_duty)
        cmds.append(self.get_pwm_duty)
        cmds.append(self.set_pwm_freq)
        cmds.append(self.get_pwm_freq)
        cmds.append(self.set_pwm_res8)
        cmds.append(self.get_pwm_res8)
        cmds.append(self.set_tmr_mode)
        cmds.append(self.get_tmr_mode)
        cmds.append(self.set_tmr_error_code)
        cmds.append(self.get_tmr_error_code)
        cmds.append(self.set_tmr_duty)
        cmds.append(self.get_tmr_duty)
        cmds.append(self.set_tmr_freq)
        cmds.append(self.get_tmr_freq)
        cmds.append(self.set_tmr_hi_us)
        cmds.append(self.get_tmr_hi_us)
        cmds.append(self.set_tmr_lo_us)
        cmds.append(self.get_tmr_lo_us)
        cmds.append(self.set_res104)
        cmds.append(self.get_res104)
        return cmds
