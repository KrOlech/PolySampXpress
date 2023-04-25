// $HeaderUTC:PIControllerErrors.h, 11, 2003-08-18 13:56:46Z, Steffen Rau$
// $LogUTC[5]:
//  11   shared    1.10        2003-08-18 13:56:46Z     Steffen Rau     neue
//       Fehlercodes 51 und 52
//  10   shared    1.9         2003-08-07 13:00:45Z     Steffen Rau     added
//       error codes 46, 47, 48
//  9    shared    1.8         2003-07-23 15:03:19Z     Steffen Rau     new
//       error codes 31, 32, 44, 45, 49, 50
//  8    shared    1.7         2003-07-18 11:28:52Z     Steffen Rau     error 5
//       is now "PI_CNTR_MOVE_WITHOUT_REF_OR_NO_SERVO"
//  7    shared    1.6         2003-07-17 17:18:44Z     Steffen Rau    
//       corrected error code description
//       added max error code
// $


#ifndef __PI_CONTROLLER_ERROS_H__
#define __PI_CONTROLLER_ERROS_H__

#include "../../libs/generic_i/source/InterfaceErrors.h"

// PI CONTROLLER errors
#define PI_UNKNOWN_AXIS_IDENTIFIER					(COM_MAX_ERROR -  1) /**<\ingroup err
																				Unknown axis identifier */
#define PI_NR_NAV_OUT_OF_RANGE						(COM_MAX_ERROR -  2) /**<\ingroup err
																				Number for \c NAV out of range - must be in [1,10000]*/
#define PI_INVALID_SGA								(COM_MAX_ERROR -  3) /**<\ingroup err
																				Invalid value for \c SGA - must be one of {1, 10, 100, 1000}*/
#define PI_UNEXPECTED_RESPONSE						(COM_MAX_ERROR -  4) /**<\ingroup err
																				Controller has sent unexpected response*/
#define PI_NO_MANUAL_PAD							(COM_MAX_ERROR -  5) /**<\ingroup err
																				No manual control pad installed, calls to \c SMA and related commands are not allowed*/
#define PI_INVALID_MANUAL_PAD_KNOB					(COM_MAX_ERROR -  6) /**<\ingroup err
																				Invalid number for manual control pad knob */
#define PI_INVALID_MANUAL_PAD_AXIS					(COM_MAX_ERROR -  7) /**<\ingroup err
																				Axis not currently controlled by a manual control pad*/
#define PI_CONTROLLER_BUSY							(COM_MAX_ERROR -  8) /**<\ingroup err
																				Controller is busy with some lengthy operation (e.g. reference movement, fast scan algorithm)*/
#define PI_THREAD_ERROR								(COM_MAX_ERROR -  9) /**<\ingroup err
																				Internal error - could not start thread*/
#define PI_IN_MACRO_MODE							(COM_MAX_ERROR - 10) /**<\ingroup err
																				Controller is (already) in macro mode - command not valid in macro mode*/
#define PI_NOT_IN_MACRO_MODE						(COM_MAX_ERROR - 11) /**<\ingroup err
																				Controller not in macro mode - command not valid unless macro mode active*/
#define PI_MACRO_FILE_ERROR							(COM_MAX_ERROR - 12) /**<\ingroup err
																				Could not open file to write macro or to read macro*/
#define PI_NO_MACRO_OR_EMPTY						(COM_MAX_ERROR - 13) /**<\ingroup err
																				No macro with given name on controller or macro is empty*/
#define PI_MACRO_EDITOR_ERROR						(COM_MAX_ERROR - 14) /**<\ingroup err
																				Internal error in macro editor*/
#define PI_INVALID_ARGUMENT							(COM_MAX_ERROR - 15) /**<\ingroup err
																				One of the arguments given to the function is invalid (empty string, index out of range, ...) */
#define PI_AXIS_ALREADY_EXISTS						(COM_MAX_ERROR - 16) /**<\ingroup err
																				Axis identifier is already in use for a connected stage*/
#define PI_INVALID_AXIS_IDENTIFIER					(COM_MAX_ERROR - 17) /**<\ingroup err
																				Invalid axis identifier */
#define PI_COM_ARRAY_ERROR							(COM_MAX_ERROR - 18) /**<\ingroup err
																				Could not access array data in COM server */
#define PI_COM_ARRAY_RANGE_ERROR					(COM_MAX_ERROR - 19) /**<\ingroup err
																				Range of array does not fit the number of parameters */
#define PI_INVALID_SPA_CMD_ID						(COM_MAX_ERROR - 20) /**<\ingroup err
																				Command ID given to \c SPA or \c SPA? is not valid */
#define PI_NR_AVG_OUT_OF_RANGE						(COM_MAX_ERROR - 21) /**<\ingroup err
																				Number for \c AVG out of range - must be >0*/
#define PI_WAV_SAMPLES_OUT_OF_RANGE					(COM_MAX_ERROR - 22) /**<\ingroup err
																				Number of samples given to \c WAV out of range*/
#define PI_WAV_FAILED								(COM_MAX_ERROR - 23) /**<\ingroup err
																				Generation of wave failed */
#define PI_MOTION_ERROR								(COM_MAX_ERROR - 24) /**<\ingroup err
																				motion error while axis was moving */
#define PI_RUNNING_MACRO							(COM_MAX_ERROR - 25) /**<\ingroup err
																				Controller is (already) running a macro */
#define PI_PZT_CONFIG_FAILED						(COM_MAX_ERROR - 26) /**<\ingroup err
																				Configuration of PZT stage or amplifier failed. */
#define PI_PZT_CONFIG_INVALID_PARAMS				(COM_MAX_ERROR - 27) /**<\ingroup err
																				Current settings are not valid for desired configuration. */
#define PI_UNKNOWN_CHANNEL_IDENTIFIER				(COM_MAX_ERROR - 28) /**<\ingroup err
																				Unknown channel identifier */
#define PI_WAVE_PARAM_FILE_ERROR					(COM_MAX_ERROR - 29) /**<\ingroup err
																				Error while reading/writing to wave generator parameter file.*/
#define PI_UNKNOWN_WAVE_MACRO						(COM_MAX_ERROR - 30) /**<\ingroup err
																				Could not find description of wave form. Maybe WG.INI is missing?*/
#define PI_WAVE_MACRO_FUNC_NOT_LOADED				(COM_MAX_ERROR - 31) /**<\ingroup err
																				The WGMacro DLL function was not found at startup*/
#define PI_USER_CANCELLED							(COM_MAX_ERROR - 32) /**<\ingroup err
																				The user cancelled a dialog*/
#define PI_C844_ERROR								(COM_MAX_ERROR - 33) /**<\ingroup err
																				Error from the C-844 Controller*/
#define PI_DLL_NOT_LOADED							(COM_MAX_ERROR - 34) /**<\ingroup err
																				DLL neccessary to call function not loaded, or function not found in DLL*/
#define PI_PARAMETER_FILE_PROTECTED					(COM_MAX_ERROR - 35) /**<\ingroup err
																				The opened parameter file is protected and cannot be edited*/
#define PI_NO_PARAMETER_FILE_OPENED					(COM_MAX_ERROR - 36) /**<\ingroup err
																				There is no parameter file opened*/
#define PI_STAGE_DOES_NOT_EXIST						(COM_MAX_ERROR - 37) /**<\ingroup err
																				The selected stages does not exist*/
#define PI_PARAMETER_FILE_ALREADY_OPENED			(COM_MAX_ERROR - 38) /**<\ingroup err
																				There is already a parameter file opened. Please close this file before openig a new file*/
#define PI_PARAMETER_FILE_OPEN_ERROR				(COM_MAX_ERROR - 39) /**<\ingroup err
																				DLL neccessary to call function not loaded, or function not found in DLL*/
#define PI_INVALID_CONTROLLER_VERSION				(COM_MAX_ERROR - 40) /**<\ingroup err
																				The Version of the connected controller is invalid.*/
#define PI_PARAM_SET_ERROR							(COM_MAX_ERROR - 41) /**<\ingroup err
																				parameter could not be set with SPA, parameter on controller undefined! */
#define PI_NUMBER_OF_POSSIBLE_WAVES_EXCEEDED		(COM_MAX_ERROR - 42) /**<\ingroup err
																				The Number of the possible waves has exceeded*/
#define PI_NUMBER_OF_POSSIBLE_GENERATORS_EXCEEDED	(COM_MAX_ERROR - 43) /**<\ingroup err
																				The Number of the possible waves generators has exceeded*/
#define PI_NO_WAVE_FOR_AXIS_DEFINED					(COM_MAX_ERROR - 44) /**<\ingroup err
																				There is no wave for the given axis defind*/
#define PI_CANT_STOP_OR_START_WAV					(COM_MAX_ERROR - 45) /**<\ingroup err
																				You can't stop a wave of an axis if it's already stopped, or start it if it's already started*/
#define PI_REFERENCE_ERROR							(COM_MAX_ERROR - 46) /**<\ingroup err
																				Not all axes could be referenced */
#define PI_REQUIRED_WAVE_MACRO_NOT_FOUND			(COM_MAX_ERROR - 47) /**<\ingroup err
																				Could not find parameter set, required by frequency relation.*/
#define PI_INVALID_SPP_CMD_ID						(COM_MAX_ERROR - 48) /**<\ingroup err
																				Command ID given to \c SPP or \c SPP? is not valid */
#define PI_STAGE_NAME_ISNT_UNIQUE					(COM_MAX_ERROR - 49) /**<\ingroup err
																				 A stagename given to \c CST isn't unique*/
#define PI_FILE_TRANSFER_BEGIN_MISSING				(COM_MAX_ERROR - 50) /**<\ingroup err
																				 A uuencoded file transfered did not start with "begin" and the proprer filename*/
#define PI_FILE_TRANSFER_ERROR_TEMP_FILE			(COM_MAX_ERROR - 51) /**<\ingroup err
																				 Could not create/read file on host PC*/
#define PI_FILE_TRANSFER_CRC_ERROR					(COM_MAX_ERROR - 52) /**<\ingroup err
																				 Checksum error when transfering a file to/from the controller*/

// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// Do not forget do update TranslatePIError !
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#define PI_CONTROLLER_MAX_ERR				(COM_MAX_ERROR - 53)

/////////////////////////////////////////////////////////////////////////////
//                      Controller error codes                             //
/////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////
//  obsolet, provided for backward compatibility

#define PI_CNTR_MOVE_WITHOUT_INI				5			// name "INI" is misleading - we mean "reference"

//
/////////////////////////////////////////////////////////////////////////////


#define PI_CNTR_NO_ERROR						0			/**<\ingroup err
																No error*/											
#define PI_CNTR_PARAM_SYNTAX					1			/**<\ingroup err
																Parameter syntax error*/											
#define PI_CNTR_UNKNOWN_COMMAND					2			/**<\ingroup err
																Unknown command*/
#define PI_CNTR_MOVE_WITHOUT_REF_OR_NO_SERVO	5			/**<\ingroup err
																Unallowable move attempted on unreferenced axis, or move attempted with servo off*/
#define PI_CNTR_INVALID_SGA_PARAM				6			/**<\ingroup err
																Parameter for \c SGA not valid*/
#define PI_CNTR_POS_OUT_OF_LIMITS				7			/**<\ingroup err
																Position out of limits*/
#define PI_CNTR_VEL_OUT_OF_LIMITS				8			/**<\ingroup err
																Velocity out of limits*/
#define PI_CNTR_SET_PIVOT_NOT_POSSIBLE			9			/**<\ingroup err
																Attempt to set pivot point while U,V or W is not equal 0*/
#define PI_CNTR_STOP							10			/**<\ingroup err
																Controller was stopped*/
#define PI_CNTR_SST_OR_SCAN_RANGE				11			/**<\ingroup err
																Parameter for \c SST or for one of the embedded scan algorithms out of range*/	
#define PI_CNTR_INVALID_SCAN_AXES				12			/**<\ingroup err
																Invalid axis combination for fast scan*/
#define PI_CNTR_INVALID_NAV_PARAM				13			/**<\ingroup err
																Parameter for \c NAV out of range*/
#define PI_CNTR_INVALID_ANALOG_INPUT			14			/**<\ingroup err
																Invalid analog channel*/
#define PI_CNTR_INVALID_AXIS_IDENTIFIER			15			/**<\ingroup err
																Invalid axis identifier*/
#define PI_CNTR_INVALID_STAGE_NAME				16			/**<\ingroup err
																Unknown stage name*/
#define PI_CNTR_PARAM_OUT_OF_RANGE				17			/**<\ingroup err
																Parameter out of range*/
#define PI_CNTR_INVALID_MACRO_NAME				18			/**<\ingroup err
																Invalid macro name*/
#define PI_CNTR_MACRO_RECORD					19			/**<\ingroup err
																Error while recording macro*/
#define PI_CNTR_MACRO_NOT_FOUND					20			/**<\ingroup err
																Macro not found*/
#define PI_CNTR_AXIS_HAS_NO_BRAKE				21			/**<\ingroup err
																Axis has no brake*/
#define PI_CNTR_DOUBLE_AXIS						22			/**<\ingroup err
																Axis identifier given more than once*/
#define PI_CNTR_INVALID_AXIS					23			/**<\ingroup err
																Invalid axis*/
#define PI_CNTR_PARAM_NR						24			/**<\ingroup err
																Incorrect number of parameters*/
#define PI_CNTR_INVALID_REAL_NR					25			/**<\ingroup err
																Invalid floating point number*/
#define PI_CNTR_MISSING_PARAM					26			/**<\ingroup err
																Missing parameter*/
#define PI_CNTR_SOFT_LIMIT_OUT_OF_RANGE			27			/**<\ingroup err
																Soft limit out of range*/
#define PI_CNTR_NO_MANUAL_PAD					28			/**<\ingroup err
																No manual pad connected*/
#define PI_CNTR_NO_JUMP							29			/**<\ingroup err
																No more step response values*/
#define PI_CNTR_INVALID_JUMP					30			/**<\ingroup err
																No step response values recorded*/
#define PI_CNTR_AXIS_HAS_NO_REFERENCE			31			/**<\ingroup err
																Axis has no reference sensor*/
#define PI_CNTR_STAGE_HAS_NO_LIM_SWITCH			32			/**<\ingroup err
																Axis has no limit switch*/
#define PI_CNTR_NO_RELAY_CARD					33			/**<\ingroup err
																No relay card installed*/
#define PI_CNTR_CMD_NOT_ALLOWED_FOR_STAGE		34			/**<\ingroup err
																The last command was not allowed for selected stage(s)*/
#define PI_CNTR_NO_DIGITAL_INPUT				35			/**<\ingroup err
																No digital input installed*/
#define PI_CNTR_NO_DIGITAL_OUTPUT				36			/**<\ingroup err
																No digital output installed*/
#define PI_CNTR_INVALID_CNTR_NUMBER				39			/**<\ingroup err
																Controller number invalid*/
#define PI_CNTR_NO_JOYSTICK_CONNECTED			40			/**<\ingroup err
																No joystick connected*/
#define PI_CNTR_INVALID_EGE_AXIS				41			/**<\ingroup err
																Invlaid axis for electronic gearing, axis can not be slave*/
#define PI_CNTR_SLAVE_POSITION_OUT_OF_RANGE		42			/**<\ingroup err
																Position of slave axis is out of range*/
#define PI_CNTR_JOYSTICK_CALIBRATION_FAILED		44			/**<\ingroup err
																Calibration of joystick failed*/
#define PI_CNTR_REFERENCING_FAILED				45			/**<\ingroup err
																Referencing failed*/
#define PI_CNTR_LSM_MISSING						46			/**<\ingroup err
																LSM (Laser Sphere Meter) Missing*/
#define PI_CNTR_LSM_NOT_INITIALIZED				47			/**<\ingroup err
																LSM (Laser Sphere Meter) cannot be initialized/ is not initialized*/
#define PI_CNTR_LSM_COM_ERROR					48			/**<\ingroup err
																LSM (Laser Sphere Meter) Communication Error*/
#define PI_CNTR_MOVE_TO_LIMIT_SWITCH_FAILED		49			/**<\ingroup err
																Move to limit switch failed*/
#define PI_CNTR_REF_WITH_REF_DISABLED			50			/**<\ingroup err
																Reference attempted on an axis with referencing disabled*/
#define PI_CNTR_AXIS_UNDER_JOYSTICK_CONTROL		51			/**<\ingroup err
																Selected axis is controlled by joystick*/
#define PI_CNTR_COMMUNICATION_ERROR				52			/**<\ingroup err
																Controller detected communication error*/
	
#define PI_CNTR_NO_AXIS							200			/**<\ingroup err
																No stage connected*/
#define PI_CNTR_NO_AXIS_PARAM_FILE				201			/**<\ingroup err
																File with axis parameter not found.*/
#define PI_CNTR_INVALID_AXIS_PARAM_FILE			202			/**<\ingroup err
																Invalid axis parameter file*/
#define PI_CNTR_NO_AXIS_PARAM_BACKUP			203			/**<\ingroup err
																Backup file with axis parameter not found.*/
#define PI_CNTR_RESERVED_204					204			/**<\ingroup err
																PI internal error code 204*/
#define PI_CNTR_SMO_WITH_SERVO_ON				205			/**<\ingroup err
																SMO with servo on*/
#define PI_CNTR_UUDECODE_INCOMPLETE_HEADER		206			/**<\ingroup err
																uudecode : incomplete header*/
#define PI_CNTR_UUDECODE_NOTHING_TO_DECODE		207			/**<\ingroup err
																uudecode : nothing to decode*/
#define PI_CNTR_UUDECODE_ILLEGAL_FORMAT			208			/**<\ingroup err
																uudecode : illegal UUE format*/
#define PI_CNTR_CRC32_ERROR						209			/**<\ingroup err
																CRC32 error*/
#define PI_CNTR_ILLEGAL_FILENAME				210			/**<\ingroup err
																Illegal file name*/
	
#define PI_CNTR_SENDING_BUFFER_OVERFLOW			301			/**<\ingroup err
																Sending Buffer Overflow*/
#define PI_CNTR_VOLTAGE_OUT_OF_LIMITS			302			/**<\ingroup err
																Voltage out of limits*/
#define PI_CNTR_VOLTAGE_SET_WHEN_SERVO_ON		303			/**<\ingroup err
																Attempt to set voltage when servo on*/																
#define PI_CNTR_RECEIVING_BUFFER_OVERFLOW		304			/**<\ingroup err
																Received command is too long*/																
#define PI_CNTR_EEPROM_ERROR					305			/**<\ingroup err
																Error while reading/writing EEPROM*/
#define PI_CNTR_I2C_ERROR						306			/**<\ingroup err
																Error on I2C bus*/																
#define PI_CNTR_RECEIVING_TIMEOUT				307			/**<\ingroup err
																Timeout while receiving command*/

#define PI_CNTR_TOO_MANY_NESTED_MACROS			1000		/**<\ingroup err
																Too many nested macros*/
#define PI_CNTR_MACRO_ALREADY_DEFINED			1001		/**<\ingroup err
																Macro already defined*/
#define PI_CNTR_NO_MACRO_RECORDING				1002		/**<\ingroup err
																No macro recording*/
#define PI_CNTR_INVALID_MAC_PARAM				1003		/**<\ingroup err
																Invalid parameter for \c MAC*/
#define PI_CNTR_RESERVED_1004					1004		/**<\ingroup err
																PI internal error code 31*/

#define PI_CNTR_ALREADY_HAS_SERIAL_NUMBER		2000		/**<\ingroup err
																Controller already has a serial number*/

#define PI_CNTR_SECTOR_ERASE_FAILED				4000		/**<\ingroup err
																Sektor Erase failed*/
#define PI_CNTR_FLASH_PROGRAM_FAILED			4001		/**<\ingroup err
																Flash programm failed*/
#define PI_CNTR_FLASH_READ_FAILED				4002		/**<\ingroup err
																Flash read failed*/
#define PI_CNTR_HW_MATCHCODE_ERROR				4003		/**<\ingroup err
																HW Matchcode missing/invalid*/
#define PI_CNTR_FW_MATCHCODE_ERROR				4004		/**<\ingroup err
																FW Matchcode missing/invalid*/
#define PI_CNTR_HW_VERSION_ERROR				4005		/**<\ingroup err
																FW Version missing/invalid*/
#define PI_CNTR_FW_VERSION_ERROR				4006		/**<\ingroup err
																FW Mark missing/invalid*/
	
#define PI_CNTR_MAX_ERROR_NR					4007		// maximum possible error number (at least we know about)*/



#endif //__PI_CONTROLLER_ERROS_H__