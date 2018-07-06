/*
 * port_uart_if.c
 *
 *  Created on: Jul 2, 2018
 *      Author: kevinweiss
 */
/* Includes ------------------------------------------------------------------*/
#include <string.h>

#include "stm32f1xx_hal.h"

#include "port_uart.h"
#include "app_shell_if.h"

#include "app_access.h"
#include "app_errno.h"
#include "app_typedef.h"
#include "app_common.h"
#include "app.h"
#include "app_debug.h"

/* Defines -------------------------------------------------------------------*/
#define IS_RX_WAITING(x)	(HAL_IS_BIT_SET(x, USART_CR3_DMAR))

/* Private function prototypes -----------------------------------------------*/
static error_t _tx_str(PORT_UART_t *port_uart);
static error_t _rx_str(PORT_UART_t *port_uart);
static error_t _xfer_complete(PORT_UART_t *port_uart);
static inline int32_t _get_rx_amount(PORT_UART_t *port_uart);

/* Private variables ---------------------------------------------------------*/
//make a struct that has access, buf, uart handle

/**
 * @brief Initializes and attaches all the pointers for communication.
 *
 * @retval errno defined error code.
 */
error_t port_uart_init(PORT_UART_t *port_uart) {
	sprintf(port_uart->str, "0, Initialized, Build Date: %s %s\n", __DATE__, __TIME__);
	error_t err = _tx_str(port_uart);
	return err;
}

/**
 * @brief Polls and parses the rx and tx buffers.
 *
 * @retval errno defined error code.
 */
error_t port_uart_poll(PORT_UART_t *port_uart) {
	error_t err = ENOACTION;


	if (IS_RX_WAITING(port_uart->huart->Instance->CR3)) {
		err = _rx_str(port_uart);
	} else if (port_uart->huart->TxXferCount == 0) {
		if (port_uart->str[port_uart->size - 1] != 0) {
			err = EMSGSIZE;
			HAL_UART_AbortTransmit(port_uart->huart);
			HAL_UART_AbortReceive(port_uart->huart);
			memset(port_uart->str, 0, port_uart->size);
			sprintf(port_uart->str, "%d%s", err, TX_END_STR);
			HAL_UART_Transmit_DMA(port_uart->huart,
					(uint8_t*) port_uart->str, strlen(port_uart->str));
		} else {
			err = _xfer_complete(port_uart);
		}
	}
	return err;
}
/**
 * @brief Private function
 *
 * @retval errno defined error code.
 */
static error_t _xfer_complete(PORT_UART_t *port_uart) {
	char *str = port_uart->str;
	UART_HandleTypeDef *huart = port_uart->huart;

	HAL_StatusTypeDef status;
	error_t err = EUNKNOWN;

	memset(port_uart->str, 0, port_uart->size);
	HAL_UART_AbortTransmit(huart);
	HAL_UART_AbortReceive(huart);
	status = HAL_UART_Receive_DMA(huart,
			(uint8_t*) str, port_uart->size);
	if (status == HAL_BUSY) {
		err = EBUSY;
	}
	if (status == HAL_ERROR) {
		err = ENXIO;
	} else if (status == HAL_OK) {
		err = EOK;
	}
	return err;
}

/**
 * @brief Private function
 *
 * @retval errno defined error code.
 */
static error_t _rx_str(PORT_UART_t *port_uart) {
	char *str = port_uart->str;
	UART_HandleTypeDef *huart = port_uart->huart;

	uint16_t rx_amount;
	error_t err = ENOACTION;

	rx_amount = _get_rx_amount(port_uart);
	if (rx_amount >= 1) {
		if (str[rx_amount - 1] == RX_END_CHAR
				&& _get_rx_amount(port_uart) != port_uart->size) {
			HAL_UART_AbortTransmit(huart);
			HAL_UART_AbortReceive(huart);
			err = parse_command(str, port_uart->size, port_uart->access);
			HAL_UART_Transmit_DMA(huart, (uint8_t*) str, strlen(str));
		}
	}
	return err;
}

/**
 * @brief Private function
 *
 * @retval errno defined error code.
 */
static error_t _tx_str(PORT_UART_t *port_uart) {
	char *str = port_uart->str;
	UART_HandleTypeDef *huart = port_uart->huart;
	error_t err = EUNKNOWN;
	HAL_StatusTypeDef status = HAL_UART_Transmit_DMA(huart, (uint8_t*) str,
			strlen(str));

	if (status == HAL_BUSY) {
		HAL_UART_AbortTransmit(huart);
		HAL_UART_AbortReceive(huart);
		status = HAL_UART_Transmit_DMA(huart, (uint8_t*) str, strlen(str));
		if (status == HAL_BUSY) {
			err = EBUSY;
		}
	}
	if (status == HAL_ERROR) {
		err = ENXIO;
	} else if (status == HAL_OK) {
		err = EOK;
	}

	return err;
}

/**
 * @brief Private function
 *
 * @retval errno defined error code.
 */
static inline int32_t _get_rx_amount(PORT_UART_t *port_uart) {
	return (port_uart->size - port_uart->huart->hdmarx->Instance->CNDTR);
}
