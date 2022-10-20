#ifndef __INTERFACE_ERRORS_H__
#define __INTERFACE_ERRORS_H__

#define COM_NO_ERROR					0	/**<\ingroup err
													No error occurred during function call */
#define COM_ERROR						-1	/**< \ingroup err
													Error during com operation (could not be specified) */
#define SEND_ERROR						-2  /**< \ingroup err
													Error while sending data */
#define REC_ERROR						-3  /**< \ingroup err
													Error while receiving data */
#define NOT_CONNECTED_ERROR				-4  /**< \ingroup err
													Not connected (no port with given ID open) */
#define COM_BUFFER_OVERFLOW				-5  /**< \ingroup err
													Buffer overflow */
#define CONNECTION_FAILED				-6	/**< \ingroup err
													Error while opening port */
#define COM_TIMEOUT						-7	/**< \ingroup err
													Timeout error */
#define COM_MULTILINE_RESPONSE			-8	/**< \ingroup err
													There are more lines waiting in buffer */
#define COM_INVALID_ID					-9  /**< \ingroup err
													There is no interface open with the given ID */
#define COM_NOTIFY_EVENT_ERROR			-10 /**< \ingroup err
													The event for the notification could not be opened */
#define COM_NOT_IMPLEMENTED				-11 /**< \ingroup err
													The function was not implemented (e.g. only RS-232 communication provides this feature and it was called for IEEE488) */
#define COM_ECHO_ERROR					-12 /**< \ingroup err
													Error while sending "echoed" data */
#define COM_GPIB_EDVR					-13 /**< \ingroup err
													IEEE488: System error                           */
#define COM_GPIB_ECIC					-14 /**< \ingroup err
													IEEE488: Function requires GPIB board to be CIC */
#define COM_GPIB_ENOL					-15 /**< \ingroup err
													IEEE488: Write function detected no Listeners   */
#define COM_GPIB_EADR					-16 /**< \ingroup err
													IEEE488: Interface board not addressed correctly*/
#define COM_GPIB_EARG					-17 /**< \ingroup err
													IEEE488: Invalid argument to function call      */
#define COM_GPIB_ESAC					-18 /**< \ingroup err
													IEEE488: Function requires GPIB board to be SAC */
#define COM_GPIB_EABO					-19 /**< \ingroup err
													IEEE488: I/O operation aborted                  */
#define COM_GPIB_ENEB					-20 /**< \ingroup err
													IEEE488: Non-existent interface board           */
#define COM_GPIB_EDMA					-21 /**< \ingroup err
													IEEE488: Error performing DMA                   */
#define COM_GPIB_EOIP					-22 /**< \ingroup err
													IEEE488: I/O operation started before previous operation completed                    */
#define COM_GPIB_ECAP					-23 /**< \ingroup err
													IEEE488: No capability for intended operation   */
#define COM_GPIB_EFSO					-24 /**< \ingroup err
													IEEE488: File system operation error            */
#define COM_GPIB_EBUS					-25 /**< \ingroup err
													IEEE488: Command error during device call       */
#define COM_GPIB_ESTB					-26 /**< \ingroup err
													IEEE488: Serial poll status byte lost           */
#define COM_GPIB_ESRQ					-27 /**< \ingroup err
													IEEE488: SRQ remains asserted                   */
#define COM_GPIB_ETAB					-28 /**< \ingroup err
													IEEE488: The return buffer is full.             */
#define COM_GPIB_ELCK					-29 /**< \ingroup err
													IEEE488: Address or board is locked.            */
#define COM_RS_INVALID_DATA_BITS		-30 /**< \ingroup err
													RS-232: The use of 5 data bits with 2 stop bits is an invalid combination, as is 6, 7, or 8 data bits with 1.5 stop bits. */
#define COM_ERROR_RS_SETTINGS			-31 /**< \ingroup err
													RS-232: Error when configuring the COM port */
#define COM_INTERNAL_RESOURCES_ERROR	-32 /**< \ingroup err
													Error when dealing with internal system resources (events, threads, ...) */
#define COM_DLL_FUNC_ERROR				-33 /**< \ingroup err
													A DLL or one of the required functions could not be loaded. */


#define COM_MAX_ERROR			-1000

/**
 * \ingroup err
 * Simple macro to check if an error was caused by basic communication functions.
 */
#define IS_COM_ERROR(err) \
	 ( (err)<0 && (err)>COM_MAX_ERROR )

#endif //__INTERFACE_ERRORS_H__