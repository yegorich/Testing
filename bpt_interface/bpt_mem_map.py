from base_device import Basedevice


class BptMemMap(Basedevice):
    def get_sys_sn_12(self):
        """Unique ID of the device"""
        return self.read_bytes(0, 12)

    def get_sys_fw_rev(self):
        """Firmware revision"""
        return self.read_bytes(12, 4)

    def get_sys_build_time_second(self):
        """The seconds in decimal"""
        return self.read_bytes(16, 1)

    def get_sys_build_time_minute(self):
        """The minutes in decimal"""
        return self.read_bytes(17, 1)

    def get_sys_build_time_hour(self):
        """The hours in decimal"""
        return self.read_bytes(18, 1)

    def get_sys_build_time_day_of_month(self):
        """The months in decimal"""
        return self.read_bytes(19, 1)

    def get_sys_build_time_day_of_week(self):
        """The week in decimal"""
        return self.read_bytes(20, 1)

    def get_sys_build_time_month(self):
        """The month in decimal"""
        return self.read_bytes(21, 1)

    def get_sys_build_time_year(self):
        """The last two digits of the year in decimal (20xx)"""
        return self.read_bytes(22, 1)

    def get_sys_build_time_res_1(self):
        """Reserved bytes"""
        return self.read_bytes(23, 1)

    def get_sys_device_num(self):
        """A constant number that should always be the same"""
        return self.read_bytes(24, 4)

    def set_sys_device_num(self, data=0):
        """A constant number that should always be the same"""
        return self.write_bytes(24, data, 4)

    def get_sys_cr(self):
        """Specific modes for I2C"""
        return self.read_bytes(28, 1)

    def set_sys_cr(self, data=0):
        """Specific modes for I2C"""
        return self.write_bytes(28, data, 1)

    def get_sys_cr_dut_rst(self):
        """resets the DUT"""
        return self.read_bits(28, 1, 1)

    def set_sys_cr_dut_rst(self, data=0):
        """resets the DUT"""
        return self.write_bits(28, 1, 1, data)

    def get_sys_res_3(self):
        """Reserved bytes"""
        return self.read_bytes(29, 3)

    def get_i2c_mode(self):
        """Specific modes for I2C"""
        return self.read_bytes(32, 1)

    def set_i2c_mode(self, data=0):
        """Specific modes for I2C"""
        return self.write_bytes(32, data, 1)

    def get_i2c_mode_addr_10_bit(self):
        """10 bit address enable"""
        return self.read_bits(32, 1, 1)

    def set_i2c_mode_addr_10_bit(self, data=0):
        """10 bit address enable"""
        return self.write_bits(32, 1, 1, data)

    def get_i2c_mode_general_call(self):
        """general call enable"""
        return self.read_bits(32, 2, 1)

    def set_i2c_mode_general_call(self, data=0):
        """general call enable"""
        return self.write_bits(32, 2, 1, data)

    def get_i2c_mode_no_clk_stretch(self):
        """disable for clk stretch"""
        return self.read_bits(32, 3, 1)

    def set_i2c_mode_no_clk_stretch(self, data=0):
        """disable for clk stretch"""
        return self.write_bits(32, 3, 1, data)

    def get_i2c_mode_reg_16_bit(self):
        """16 bit register access mode"""
        return self.read_bits(32, 4, 1)

    def set_i2c_mode_reg_16_bit(self, data=0):
        """16 bit register access mode"""
        return self.write_bits(32, 4, 1, data)

    def get_i2c_mode_nack_data(self):
        """Forces a data nack"""
        return self.read_bits(32, 5, 1)

    def set_i2c_mode_nack_data(self, data=0):
        """Forces a data nack"""
        return self.write_bits(32, 5, 1, data)

    def get_i2c_status(self):
        """Specific modes for I2C"""
        return self.read_bytes(33, 1)

    def set_i2c_status(self, data=0):
        """Specific modes for I2C"""
        return self.write_bytes(33, data, 1)

    def get_i2c_status_OVR(self):
        """Overrun/Underrun: Request for new byte when not ready"""
        return self.read_bits(33, 1, 1)

    def set_i2c_status_OVR(self, data=0):
        """Overrun/Underrun: Request for new byte when not ready"""
        return self.write_bits(33, 1, 1, data)

    def get_i2c_status_AF(self):
        """Acknowledge failure"""
        return self.read_bits(33, 2, 1)

    def set_i2c_status_AF(self, data=0):
        """Acknowledge failure"""
        return self.write_bits(33, 2, 1, data)

    def get_i2c_status_BERR(self):
        """Bus error:  Non-valid position during a byte transfer"""
        return self.read_bits(33, 3, 1)

    def set_i2c_status_BERR(self, data=0):
        """Bus error:  Non-valid position during a byte transfer"""
        return self.write_bits(33, 3, 1, data)

    def get_i2c_status_GENCALL(self):
        """General call address recieved"""
        return self.read_bits(33, 4, 1)

    def set_i2c_status_GENCALL(self, data=0):
        """General call address recieved"""
        return self.write_bits(33, 4, 1, data)

    def get_i2c_status_BUSY(self):
        """Forces a data nack"""
        return self.read_bits(33, 5, 1)

    def set_i2c_status_BUSY(self, data=0):
        """Forces a data nack"""
        return self.write_bits(33, 5, 1, data)

    def get_i2c_status_RSR(self):
        """Repeated start detected"""
        return self.read_bits(33, 6, 1)

    def set_i2c_status_RSR(self, data=0):
        """Repeated start detected"""
        return self.write_bits(33, 6, 1, data)

    def get_i2c_clk_stretch_delay(self):
        """delay in us for clock stretch"""
        return self.read_bytes(34, 2)

    def set_i2c_clk_stretch_delay(self, data=0):
        """delay in us for clock stretch"""
        return self.write_bytes(34, data, 2)

    def get_i2c_slave_addr_1(self):
        """Primary slave address"""
        return self.read_bytes(36, 2)

    def set_i2c_slave_addr_1(self, data=85):
        """Primary slave address"""
        return self.write_bytes(36, data, 2)

    def get_i2c_slave_addr_2(self):
        """Secondary slave address"""
        return self.read_bytes(38, 2)

    def set_i2c_slave_addr_2(self, data=64):
        """Secondary slave address"""
        return self.write_bytes(38, data, 2)

    def get_i2c_r_count(self):
        """last read frame byte count"""
        return self.read_bytes(40, 1)

    def set_i2c_r_count(self, data=0):
        """last read frame byte count"""
        return self.write_bytes(40, data, 1)

    def get_i2c_w_count(self):
        """last write frame byte count"""
        return self.read_bytes(41, 1)

    def set_i2c_w_count(self, data=0):
        """last write frame byte count"""
        return self.write_bytes(41, data, 1)

    def get_i2c_res_6(self):
        """Reserved bytes"""
        return self.read_bytes(42, 6)

    def get_spi_mode(self):
        """"""
        return self.read_bytes(48, 1)

    def set_spi_mode(self, data=0):
        """"""
        return self.write_bytes(48, data, 1)

    def get_spi_error_code(self):
        """"""
        return self.read_bytes(49, 4)

    def set_spi_error_code(self, data=0):
        """"""
        return self.write_bytes(49, data, 4)

    def get_spi_res_11(self):
        """Reserved bytes"""
        return self.read_bytes(53, 11)

    def get_uart_mode(self):
        """Test mode"""
        return self.read_bytes(64, 1)

    def set_uart_mode(self, data=0):
        """Test mode"""
        return self.write_bytes(64, data, 1)

    def get_uart_baud(self):
        """Baudrate"""
        return self.read_bytes(65, 4)

    def set_uart_baud(self, data=0):
        """Baudrate"""
        return self.write_bytes(65, data, 4)

    def get_uart_rx_count(self):
        """Number of received bytes"""
        return self.read_bytes(69, 2)

    def set_uart_rx_count(self, data=0):
        """Number of received bytes"""
        return self.write_bytes(69, data, 2)

    def get_uart_tx_count(self):
        """Number of transmitted bytes"""
        return self.read_bytes(71, 2)

    def set_uart_tx_count(self, data=0):
        """Number of transmitted bytes"""
        return self.write_bytes(71, data, 2)

    def get_uart_ctrl(self):
        """UART control register"""
        return self.read_bytes(73, 1)

    def set_uart_ctrl(self, data=0):
        """UART control register"""
        return self.write_bytes(73, data, 1)

    def get_uart_ctrl_stop_bits(self):
        """Number of stop bits"""
        return self.read_bits(73, 1, 1)

    def set_uart_ctrl_stop_bits(self, data=0):
        """Number of stop bits"""
        return self.write_bits(73, 1, 1, data)

    def get_uart_ctrl_parity(self):
        """Parity"""
        return self.read_bits(73, 3, 2)

    def set_uart_ctrl_parity(self, data=0):
        """Parity"""
        return self.write_bits(73, 3, 2, data)

    def get_uart_ctrl_rts(self):
        """RTS pin state"""
        return self.read_bits(73, 4, 1)

    def set_uart_ctrl_rts(self, data=0):
        """RTS pin state"""
        return self.write_bits(73, 4, 1, data)

    def get_uart_res_6(self):
        """Reserved bytes"""
        return self.read_bytes(74, 6)

    def get_rtc_second(self):
        """The seconds in decimal"""
        return self.read_bytes(80, 1)

    def set_rtc_second(self, data=0):
        """The seconds in decimal"""
        return self.write_bytes(80, data, 1)

    def get_rtc_minute(self):
        """The minutes in decimal"""
        return self.read_bytes(81, 1)

    def set_rtc_minute(self, data=0):
        """The minutes in decimal"""
        return self.write_bytes(81, data, 1)

    def get_rtc_hour(self):
        """The hours in decimal"""
        return self.read_bytes(82, 1)

    def set_rtc_hour(self, data=0):
        """The hours in decimal"""
        return self.write_bytes(82, data, 1)

    def get_rtc_day_of_month(self):
        """The months in decimal"""
        return self.read_bytes(83, 1)

    def set_rtc_day_of_month(self, data=0):
        """The months in decimal"""
        return self.write_bytes(83, data, 1)

    def get_rtc_day_of_week(self):
        """The week in decimal"""
        return self.read_bytes(84, 1)

    def set_rtc_day_of_week(self, data=0):
        """The week in decimal"""
        return self.write_bytes(84, data, 1)

    def get_rtc_month(self):
        """The month in decimal"""
        return self.read_bytes(85, 1)

    def set_rtc_month(self, data=0):
        """The month in decimal"""
        return self.write_bytes(85, data, 1)

    def get_rtc_year(self):
        """The last two digits of the year in decimal (20xx)"""
        return self.read_bytes(86, 1)

    def set_rtc_year(self, data=0):
        """The last two digits of the year in decimal (20xx)"""
        return self.write_bytes(86, data, 1)

    def get_rtc_res_1(self):
        """Reserved bytes"""
        return self.read_bytes(87, 1)

    def get_adc_0_mode(self):
        """"""
        return self.read_bytes(88, 1)

    def set_adc_0_mode(self, data=0):
        """"""
        return self.write_bytes(88, data, 1)

    def get_adc_0_error_code(self):
        """"""
        return self.read_bytes(89, 2)

    def set_adc_0_error_code(self, data=0):
        """"""
        return self.write_bytes(89, data, 2)

    def get_adc_0_sample_rate(self):
        """"""
        return self.read_bytes(91, 1)

    def set_adc_0_sample_rate(self, data=0):
        """"""
        return self.write_bytes(91, data, 1)

    def get_adc_0_value(self):
        """"""
        return self.read_bytes(92, 4)

    def set_adc_0_value(self, data=0):
        """"""
        return self.write_bytes(92, data, 4)

    def get_adc_0_res_8(self):
        """Reserved bytes"""
        return self.read_bytes(96, 8)

    def get_adc_1_mode(self):
        """"""
        return self.read_bytes(104, 1)

    def set_adc_1_mode(self, data=0):
        """"""
        return self.write_bytes(104, data, 1)

    def get_adc_1_error_code(self):
        """"""
        return self.read_bytes(105, 2)

    def set_adc_1_error_code(self, data=0):
        """"""
        return self.write_bytes(105, data, 2)

    def get_adc_1_sample_rate(self):
        """"""
        return self.read_bytes(107, 1)

    def set_adc_1_sample_rate(self, data=0):
        """"""
        return self.write_bytes(107, data, 1)

    def get_adc_1_value(self):
        """"""
        return self.read_bytes(108, 4)

    def set_adc_1_value(self, data=0):
        """"""
        return self.write_bytes(108, data, 4)

    def get_adc_1_res_8(self):
        """Reserved bytes"""
        return self.read_bytes(112, 8)

    def get_pwm_mode(self):
        """"""
        return self.read_bytes(120, 1)

    def set_pwm_mode(self, data=0):
        """"""
        return self.write_bytes(120, data, 1)

    def get_pwm_error_code(self):
        """"""
        return self.read_bytes(121, 2)

    def set_pwm_error_code(self, data=0):
        """"""
        return self.write_bytes(121, data, 2)

    def get_pwm_duty(self):
        """"""
        return self.read_bytes(123, 1)

    def set_pwm_duty(self, data=0):
        """"""
        return self.write_bytes(123, data, 1)

    def get_pwm_freq(self):
        """"""
        return self.read_bytes(124, 4)

    def set_pwm_freq(self, data=0):
        """"""
        return self.write_bytes(124, data, 4)

    def get_pwm_res_8(self):
        """Reserved bytes"""
        return self.read_bytes(128, 8)

    def get_tmr_mode(self):
        """"""
        return self.read_bytes(136, 1)

    def set_tmr_mode(self, data=0):
        """"""
        return self.write_bytes(136, data, 1)

    def get_tmr_error_code(self):
        """"""
        return self.read_bytes(137, 2)

    def set_tmr_error_code(self, data=0):
        """"""
        return self.write_bytes(137, data, 2)

    def get_tmr_duty(self):
        """"""
        return self.read_bytes(139, 1)

    def set_tmr_duty(self, data=0):
        """"""
        return self.write_bytes(139, data, 1)

    def get_tmr_freq(self):
        """"""
        return self.read_bytes(140, 4)

    def set_tmr_freq(self, data=0):
        """"""
        return self.write_bytes(140, data, 4)

    def get_tmr_hi_us(self):
        """"""
        return self.read_bytes(144, 4)

    def set_tmr_hi_us(self, data=0):
        """"""
        return self.write_bytes(144, data, 4)

    def get_tmr_lo_us(self):
        """"""
        return self.read_bytes(148, 4)

    def set_tmr_lo_us(self, data=0):
        """"""
        return self.write_bytes(148, data, 4)

    def get_user_reg_64(self):
        """Writeable registers for user testing"""
        return self.read_bytes(152, 64)

    def set_user_reg_64(self, data=0):
        """Writeable registers for user testing"""
        return self.write_bytes(152, data, 64)

    def get_res_40(self):
        """Reserved bytes"""
        return self.read_bytes(216, 40)

    def get_command_list(self):
        """A list of all possible commands"""
        cmds = list()
        cmds.append(self.get_sys_sn_12)
        cmds.append(self.get_sys_fw_rev)
        cmds.append(self.get_sys_build_time_second)
        cmds.append(self.get_sys_build_time_minute)
        cmds.append(self.get_sys_build_time_hour)
        cmds.append(self.get_sys_build_time_day_of_month)
        cmds.append(self.get_sys_build_time_day_of_week)
        cmds.append(self.get_sys_build_time_month)
        cmds.append(self.get_sys_build_time_year)
        cmds.append(self.get_sys_build_time_res_1)
        cmds.append(self.get_sys_device_num)
        cmds.append(self.set_sys_device_num)
        cmds.append(self.get_sys_cr)
        cmds.append(self.set_sys_cr)
        cmds.append(self.get_sys_cr_dut_rst)
        cmds.append(self.set_sys_cr_dut_rst)
        cmds.append(self.get_sys_res_3)
        cmds.append(self.get_i2c_mode)
        cmds.append(self.set_i2c_mode)
        cmds.append(self.get_i2c_mode_addr_10_bit)
        cmds.append(self.set_i2c_mode_addr_10_bit)
        cmds.append(self.get_i2c_mode_general_call)
        cmds.append(self.set_i2c_mode_general_call)
        cmds.append(self.get_i2c_mode_no_clk_stretch)
        cmds.append(self.set_i2c_mode_no_clk_stretch)
        cmds.append(self.get_i2c_mode_reg_16_bit)
        cmds.append(self.set_i2c_mode_reg_16_bit)
        cmds.append(self.get_i2c_mode_nack_data)
        cmds.append(self.set_i2c_mode_nack_data)
        cmds.append(self.get_i2c_status)
        cmds.append(self.set_i2c_status)
        cmds.append(self.get_i2c_status_OVR)
        cmds.append(self.set_i2c_status_OVR)
        cmds.append(self.get_i2c_status_AF)
        cmds.append(self.set_i2c_status_AF)
        cmds.append(self.get_i2c_status_BERR)
        cmds.append(self.set_i2c_status_BERR)
        cmds.append(self.get_i2c_status_GENCALL)
        cmds.append(self.set_i2c_status_GENCALL)
        cmds.append(self.get_i2c_status_BUSY)
        cmds.append(self.set_i2c_status_BUSY)
        cmds.append(self.get_i2c_status_RSR)
        cmds.append(self.set_i2c_status_RSR)
        cmds.append(self.get_i2c_clk_stretch_delay)
        cmds.append(self.set_i2c_clk_stretch_delay)
        cmds.append(self.get_i2c_slave_addr_1)
        cmds.append(self.set_i2c_slave_addr_1)
        cmds.append(self.get_i2c_slave_addr_2)
        cmds.append(self.set_i2c_slave_addr_2)
        cmds.append(self.get_i2c_r_count)
        cmds.append(self.set_i2c_r_count)
        cmds.append(self.get_i2c_w_count)
        cmds.append(self.set_i2c_w_count)
        cmds.append(self.get_i2c_res_6)
        cmds.append(self.get_spi_mode)
        cmds.append(self.set_spi_mode)
        cmds.append(self.get_spi_error_code)
        cmds.append(self.set_spi_error_code)
        cmds.append(self.get_spi_res_11)
        cmds.append(self.get_uart_mode)
        cmds.append(self.set_uart_mode)
        cmds.append(self.get_uart_baud)
        cmds.append(self.set_uart_baud)
        cmds.append(self.get_uart_rx_count)
        cmds.append(self.set_uart_rx_count)
        cmds.append(self.get_uart_tx_count)
        cmds.append(self.set_uart_tx_count)
        cmds.append(self.get_uart_ctrl)
        cmds.append(self.set_uart_ctrl)
        cmds.append(self.get_uart_ctrl_stop_bits)
        cmds.append(self.set_uart_ctrl_stop_bits)
        cmds.append(self.get_uart_ctrl_parity)
        cmds.append(self.set_uart_ctrl_parity)
        cmds.append(self.get_uart_ctrl_rts)
        cmds.append(self.set_uart_ctrl_rts)
        cmds.append(self.get_uart_res_6)
        cmds.append(self.get_rtc_second)
        cmds.append(self.set_rtc_second)
        cmds.append(self.get_rtc_minute)
        cmds.append(self.set_rtc_minute)
        cmds.append(self.get_rtc_hour)
        cmds.append(self.set_rtc_hour)
        cmds.append(self.get_rtc_day_of_month)
        cmds.append(self.set_rtc_day_of_month)
        cmds.append(self.get_rtc_day_of_week)
        cmds.append(self.set_rtc_day_of_week)
        cmds.append(self.get_rtc_month)
        cmds.append(self.set_rtc_month)
        cmds.append(self.get_rtc_year)
        cmds.append(self.set_rtc_year)
        cmds.append(self.get_rtc_res_1)
        cmds.append(self.get_adc_0_mode)
        cmds.append(self.set_adc_0_mode)
        cmds.append(self.get_adc_0_error_code)
        cmds.append(self.set_adc_0_error_code)
        cmds.append(self.get_adc_0_sample_rate)
        cmds.append(self.set_adc_0_sample_rate)
        cmds.append(self.get_adc_0_value)
        cmds.append(self.set_adc_0_value)
        cmds.append(self.get_adc_0_res_8)
        cmds.append(self.get_adc_1_mode)
        cmds.append(self.set_adc_1_mode)
        cmds.append(self.get_adc_1_error_code)
        cmds.append(self.set_adc_1_error_code)
        cmds.append(self.get_adc_1_sample_rate)
        cmds.append(self.set_adc_1_sample_rate)
        cmds.append(self.get_adc_1_value)
        cmds.append(self.set_adc_1_value)
        cmds.append(self.get_adc_1_res_8)
        cmds.append(self.get_pwm_mode)
        cmds.append(self.set_pwm_mode)
        cmds.append(self.get_pwm_error_code)
        cmds.append(self.set_pwm_error_code)
        cmds.append(self.get_pwm_duty)
        cmds.append(self.set_pwm_duty)
        cmds.append(self.get_pwm_freq)
        cmds.append(self.set_pwm_freq)
        cmds.append(self.get_pwm_res_8)
        cmds.append(self.get_tmr_mode)
        cmds.append(self.set_tmr_mode)
        cmds.append(self.get_tmr_error_code)
        cmds.append(self.set_tmr_error_code)
        cmds.append(self.get_tmr_duty)
        cmds.append(self.set_tmr_duty)
        cmds.append(self.get_tmr_freq)
        cmds.append(self.set_tmr_freq)
        cmds.append(self.get_tmr_hi_us)
        cmds.append(self.set_tmr_hi_us)
        cmds.append(self.get_tmr_lo_us)
        cmds.append(self.set_tmr_lo_us)
        cmds.append(self.get_user_reg_64)
        cmds.append(self.set_user_reg_64)
        cmds.append(self.get_res_40)
        return cmds
