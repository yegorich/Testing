/*
 * Filename: bpt_mem_map.g
 * Author: Kevin Weiss
 * Revision: 1.00.01
 */

#ifndef BPT_MEM_MAP_H_
#define BPT_MEM_MAP_H_

#include <stdint.h>

#pragma pack(1)
/* @brief Time and date */
typedef union timestamp_t_TAG {
	struct {
		/* The seconds in decimal */
		uint8_t second;
		/* The minutes in decimal */
		uint8_t minute;
		/* The hours in decimal */
		uint8_t hour;
		/* The months in decimal */
		uint8_t day_of_month;
		/* The week in decimal */
		uint8_t day_of_week;
		/* The month in decimal */
		uint8_t month;
		/* The last two digits of the year in decimal (20xx) */
		uint8_t year;
		/* Reserved bytes */
		uint8_t res[1];
	};
	uint8_t data8[8];
} timestamp_t;

/* @brief Specific modes for I2C */
typedef struct sys_cr_t_TAG {
	/* resets the DUT */
	uint8_t dut_rst : 1;
} sys_cr_t;

/* @brief System settings for the bpt */
typedef union sys_t_TAG {
	struct {
		/* Unique ID of the device */
		uint8_t sn[12];
		/* Firmware revision */
		uint32_t fw_rev;
		/* time of build */
		timestamp_t build_time;
		/* A constant number that should always be the same */
		uint32_t device_num;
		/* Specific modes for I2C */
		sys_cr_t cr;
		/* Reserved bytes */
		uint8_t res[3];
	};
	uint8_t data8[32];
} sys_t;

/* @brief Specific modes for I2C */
typedef struct i2c_mode_t_TAG {
	/* 10 bit address enable */
	uint8_t addr_10_bit : 1;
	/* general call enable */
	uint8_t general_call : 1;
	/* disable for clk stretch */
	uint8_t no_clk_stretch : 1;
	/* 16 bit register access mode */
	uint8_t reg_16_bit : 1;
	/* disables i2c */
	uint8_t disable : 1;
} i2c_mode_t;

/* @brief System settings for the bpt */
typedef union i2c_t_TAG {
	struct {
		/* Specific modes for I2C */
		i2c_mode_t mode;
		/* Error code for I2C */
		uint16_t error_code;
		/* delay in us for clock stretch */
		uint16_t clk_stretch_delay;
		/* Injects failures for the bus */
		uint8_t inject_failure_mode;
		/* Primary slave address */
		uint16_t slave_addr_1;
		/* Secondary slave address */
		uint16_t slave_addr_2;
		/* last read frame byte count */
		uint8_t r_count;
		/* last write frame byte count */
		uint8_t w_count;
		/* Reserved bytes */
		uint8_t res[4];
	};
	uint8_t data8[16];
} i2c_t;

/* @brief  */
typedef union spi_t_TAG {
	struct {
		/*  */
		uint8_t mode;
		/*  */
		uint32_t error_code;
		/* Reserved bytes */
		uint8_t res[11];
	};
	uint8_t data8[16];
} spi_t;

/* @brief UART control register */
typedef struct uart_ctrl_t_TAG {
	/* Number of stop bits */
	uint8_t stop_bits : 1;
	/* Parity */
	uint8_t parity : 2;
} uart_ctrl_t;

/* @brief  */
typedef union uart_t_TAG {
	struct {
		/* Test mode */
		uint8_t mode;
		/* Baudrate */
		uint32_t baud;
		/* Number of received bytes */
		uint16_t rx_count;
		/* Number of transmitted bytes */
		uint16_t tx_count;
		/* UART control register */
		uart_ctrl_t ctrl;
		/* Reserved bytes */
		uint8_t res[6];
	};
	uint8_t data8[16];
} uart_t;

/* @brief  */
typedef union adc_t_TAG {
	struct {
		/*  */
		uint8_t mode;
		/*  */
		uint16_t error_code;
		/*  */
		uint8_t sample_rate;
		/*  */
		uint32_t value;
		/* Reserved bytes */
		uint8_t res[8];
	};
	uint8_t data8[16];
} adc_t;

/* @brief  */
typedef union pwm_t_TAG {
	struct {
		/*  */
		uint8_t mode;
		/*  */
		uint16_t error_code;
		/*  */
		uint8_t duty;
		/*  */
		uint32_t freq;
		/* Reserved bytes */
		uint8_t res[8];
	};
	uint8_t data8[16];
} pwm_t;

/* @brief  */
typedef union tmr_t_TAG {
	struct {
		/*  */
		uint8_t mode;
		/*  */
		uint16_t error_code;
		/*  */
		uint8_t duty;
		/*  */
		uint32_t freq;
		/*  */
		uint32_t hi_us;
		/*  */
		uint32_t lo_us;
	};
	uint8_t data8[16];
} tmr_t;

/* @brief The memory map */
typedef union map_t_TAG {
	struct {
		/* system configuration (protected) */
		sys_t sys;
		/* I2C configuration */
		i2c_t i2c;
		/*  */
		spi_t spi;
		/*  */
		uart_t uart;
		/*  */
		timestamp_t rtc;
		/*  */
		adc_t adc[2];
		/*  */
		pwm_t pwm;
		/*  */
		tmr_t tmr;
		/* Reserved bytes */
		uint8_t res[104];
	};
	uint8_t data8[256];
} map_t;

#pragma pack()
#endif