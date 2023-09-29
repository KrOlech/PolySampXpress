Attribute VB_Name = "MPiErrors"
Option Explicit

' Communication errorcodes.
Public Const COM_NO_ERROR = 0                   ' No error occurred during function call.
Public Const COM_ERROR = -1                     ' Error during com operation (could not be specified).
Public Const SEND_ERROR = -2                    ' Error while sending data.
Public Const REC_ERROR = -3                     ' Error while receiving data.
Public Const NOT_CONNECTED_ERROR = -4           ' Not connected (no port with given ID open).
Public Const COM_BUFFER_OVERFLOW = -5           ' Buffer overflow.
Public Const CONNECTION_FAILED = -6             ' Error while opening port.
Public Const COM_TIMEOUT = -7                   ' Timeout error.
Public Const COM_MULTILINE_RESPONSE = -8        ' There are more lines waiting in buffer.
Public Const COM_INVALID_ID = -9                ' There is no interface open with the given ID.
Public Const COM_NOTIFY_EVENT_ERROR = -10       ' The event for the notification could not be opened.
Public Const COM_NOT_IMPLEMENTED = -11          ' The function was not implemented (e.g. only RS-232 communication provides this feature and it was called for IEEE488).
Public Const COM_ECHO_ERROR = -12               ' Error while sending "echoed" data .
Public Const COM_GPIB_EDVR = -13                ' IEEE488: System error.
Public Const COM_GPIB_ECIC = -14                ' IEEE488: Function requires GPIB board to be CIC.
Public Const COM_GPIB_ENOL = -15                ' IEEE488: Write function detected no Listeners.
Public Const COM_GPIB_EADR = -16                ' IEEE488: Interface board not addressed correctly.
Public Const COM_GPIB_EARG = -17                ' IEEE488: Invalid argument to function call.
Public Const COM_GPIB_ESAC = -18                ' IEEE488: Function requires GPIB board to be SAC.
Public Const COM_GPIB_EABO = -19                ' IEEE488: I/O operation aborted.
Public Const COM_GPIB_ENEB = -20                ' IEEE488: Non-existent interface board.
Public Const COM_GPIB_EDMA = -21                ' IEEE488: Error performing DMA.
Public Const COM_GPIB_EOIP = -22                ' IEEE488: I/O operation started before previous operation completed.
Public Const COM_GPIB_ECAP = -23                ' IEEE488: No capability for intended operation.
Public Const COM_GPIB_EFSO = -24                ' IEEE488: File system operation error.
Public Const COM_GPIB_EBUS = -25                ' IEEE488: Command error during device call.
Public Const COM_GPIB_ESTB = -26                ' IEEE488: Serial poll status byte lost.
Public Const COM_GPIB_ESRQ = -27                ' IEEE488: SRQ remains asserted.
Public Const COM_GPIB_ETAB = -28                ' IEEE488: The return buffer is full.
Public Const COM_GPIB_ELCK = -29                ' IEEE488: Address or board is locked.
Public Const COM_RS_INVALID_DATA_BITS = -30     ' RS-232: The use of 5 data bits with 2 stop bits is an invalid combination, as is 6, 7, or 8 data bits with 1.5 stop bits.
Public Const COM_ERROR_RS_SETTINGS = -31        ' RS-232: Error when configuring the COM port.
Public Const COM_INTERNAL_RESOURCES_ERROR = -32 ' Error when dealing with internal system resources (events, threads, ...).
Public Const COM_DLL_FUNC_ERROR = -33           ' A DLL or one of the required functions could not be loaded.

Public Const COM_MAX_ERROR = -1000


' PI CONTROLLER errors
Public Const PI_UNKNOWN_AXIS_IDENTIFIER = (COM_MAX_ERROR - 1)       ' Unknown axis identifier.
Public Const PI_NR_NAV_OUT_OF_RANGE = (COM_MAX_ERROR - 2)           ' Number for \c NAV out of range - must be in [1,10000].
Public Const PI_INVALID_SGA = (COM_MAX_ERROR - 3)                   ' Invalid value for \c SGA - must be one of {1, 10, 100, 1000}.
Public Const PI_UNEXPECTED_RESPONSE = (COM_MAX_ERROR - 4)           ' Controller has sent unexpected response.
Public Const PI_NO_MANUAL_PAD = (COM_MAX_ERROR - 5)                 ' No manual control pad installed, calls to \c SMA and related commands are not allowed.
Public Const PI_INVALID_MANUAL_PAD_KNOB = (COM_MAX_ERROR - 6)       ' Invalid number for manual control pad knob.
Public Const PI_INVALID_MANUAL_PAD_AXIS = (COM_MAX_ERROR - 7)       ' Axis not currently controlled by a manual control pad.
Public Const PI_CONTROLLER_BUSY = (COM_MAX_ERROR - 8)               ' Controller is busy with some lengthy operation (e.g. reference movement, fast scan algorithm).
Public Const PI_THREAD_ERROR = (COM_MAX_ERROR - 9)                  ' Internal error - could not start thread.
Public Const PI_IN_MACRO_MODE = (COM_MAX_ERROR - 10)                ' Controller is (already) in macro mode - command not valid in macro mode.
Public Const PI_NOT_IN_MACRO_MODE = (COM_MAX_ERROR - 11)            ' Controller not in macro mode - command not valid unless macro mode active.
Public Const PI_MACRO_FILE_ERROR = (COM_MAX_ERROR - 12)             ' Could not open file to write macro or to read macro.
Public Const PI_NO_MACRO_OR_EMPTY = (COM_MAX_ERROR - 13)            ' No macro with given name on controller or macro is empty.
Public Const PI_MACRO_EDITOR_ERROR = (COM_MAX_ERROR - 14)           ' Internal error in macro editor.
Public Const PI_INVALID_ARGUMENT = (COM_MAX_ERROR - 15)             ' One of the arguments given to the function is invalid (empty string, index out of range, ...).
Public Const PI_AXIS_ALREADY_EXISTS = (COM_MAX_ERROR - 16)          ' Axis identifier is already in use for a connected stage.
Public Const PI_INVALID_AXIS_IDENTIFIER = (COM_MAX_ERROR - 17)      ' Invalid axis identifier.
Public Const PI_COM_ARRAY_ERROR = (COM_MAX_ERROR - 18)              ' Could not access array data in COM server.
Public Const PI_COM_ARRAY_RANGE_ERROR = (COM_MAX_ERROR - 19)        ' Range of array does not fit the number of parameters.
Public Const PI_INVALID_SPA_CMD_ID = (COM_MAX_ERROR - 20)           ' Command ID given to \c SPA or \c SPA? is not valid.
Public Const PI_NR_AVG_OUT_OF_RANGE = (COM_MAX_ERROR - 21)          ' Number for \c AVG out of range - must be >0.
Public Const PI_WAV_SAMPLES_OUT_OF_RANGE = (COM_MAX_ERROR - 22)     ' Number of samples given to \c WAV out of range.
Public Const PI_WAV_FAILED = (COM_MAX_ERROR - 23)                   ' Generation of wave failed.
Public Const PI_MOTION_ERROR = (COM_MAX_ERROR - 24)                 ' motion error while stage was moving.
Public Const PI_RUNNING_MACRO = (COM_MAX_ERROR - 25)                ' Controller is (already) running a macro.
Public Const PI_PZT_CONFIG_FAILED = (COM_MAX_ERROR - 26)            ' Configuration of PZT stage or amplifier failed.
Public Const PI_PZT_CONFIG_INVALID_PARAMS = (COM_MAX_ERROR - 27)    ' Current settings are not valid for desired configuration.
Public Const PI_UNKNOWN_CHANNEL_IDENTIFIER = (COM_MAX_ERROR - 28)   ' Unknown channel identifier.
Public Const PI_WAVE_PARAM_FILE_ERROR = (COM_MAX_ERROR - 29)        ' Error while reading/writing to wave generator parameter file.
Public Const PI_UNKNOWN_WAVE_MACRO = (COM_MAX_ERROR - 30)           ' Could not find description of wave form. Maybe WG.INI is missing?
Public Const PI_WAVE_MACRO_FUNC_NOT_LOADED = (COM_MAX_ERROR - 31)   ' The function of WGMacro DLL was not found at startup.
Public Const PI_USER_CANCELLED = (COM_MAX_ERROR - 32)               ' The user cancelled a dialog.
Public Const PI_C844_ERROR = (COM_MAX_ERROR - 33)                   ' Error forn The C844 Controller.
Public Const PI_DLL_NOT_LOADED = (COM_MAX_ERROR - 34)               ' Error forn The C844 Controller.
Public Const PI_PARAMETERFILE_PROTECTED = (COM_MAX_ERROR - 35)      ' Error forn The C844 Controller.
Public Const PI_NO_PARAMETERFILE_OPEND = (COM_MAX_ERROR - 36)       ' Error forn The C844 Controller.
Public Const PI_STAGE_DOSE_NOT_EXIST = (COM_MAX_ERROR - 37)         ' Error forn The C844 Controller.
Public Const PI_PARAMETERFILE_ALLREADY_OPEND = (COM_MAX_ERROR - 38) ' Error forn The C844 Controller.
Public Const PI_PARAMETERFILE__OPEN_ERROR = (COM_MAX_ERROR - 39)    ' DLL neccessary to call function not loaded, or function not found in DLL.
Public Const PI_INVALID_CONTROLLER_VERSION = (COM_MAX_ERROR - 40)   ' The Version of the connected controller is invalid.
Public Const PI_PARAM_SET_ERROR = (COM_MAX_ERROR - 41)              ' parameter could not be set with SPA, parameter on controller undefined!
Public Const PI_NUMBER_OF_POSSIBLE_WAVES_EXCEEDED = (COM_MAX_ERROR - 42)    ' The Number of the possible waves has exceeded.
Public Const PI_NUMBER_OF_POSSIBLE_GENERATORS_EXCEEDED = (COM_MAX_ERROR - 43) ' The Number of the possible waves generators has exceeded.
Public Const PI_NO_WAVE_FOR_AXIS_DEFINED = (COM_MAX_ERROR - 44)     ' There is no wave for the given axis defind.
Public Const PI_CANT_STOP_OR_START_WAV = (COM_MAX_ERROR - 45)       ' You can 't stop a wave of an axis if it's already stopped, or start it if it's already started.
Public Const PI_REFERENCE_ERROR = (COM_MAX_ERROR - 46)              ' Not all axes could be referenced.
Public Const PI_REQUIRED_WAVE_MACRO_NOT_FOUND = (COM_MAX_ERROR - 47) ' Could not find parameter set, required by frequency relation.
Public Const PI_INVALID_SPP_CMD_ID = (COM_MAX_ERROR - 48)           ' Command ID given to \c SPP or \c SPP? is not valid.
Public Const PI_STAGENAME_ISNT_UNIQUE = (COM_MAX_ERROR - 49)        ' A stagename given to \c CST isn't unique.
'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'    Do not forget do update TranslatePIError    !
'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Public Const PI_CONTROLLER_MAX_ERR = (COM_MAX_ERROR - 50)




'////////////////////////////////////////////////////////////////////////////
'//                      Controller error codes                             //
'/////////////////////////////////////////////////////////////////////////////
Public Const PI_CNTR_NO_ERROR = 0                   ' No error.
Public Const PI_CNTR_PARAM_SYNTAX = 1               ' Parameter syntax error.
Public Const PI_CNTR_UNKNOWN_COMMAND = 2            ' Unknown command.
Public Const PI_CNTR_MOVE_WITHOUT_INI = 5           ' Attempt to move before \c INI or when servo is off*/
Public Const PI_CNTR_INVALID_SGA_PARAM = 6          ' Parameter for SGA not valid.
Public Const PI_CNTR_POS_OUT_OF_LIMITS = 7          ' Position out of limits.
Public Const PI_CNTR_VEL_OUT_OF_LIMITS = 8          ' Velocity out of limits.
Public Const PI_CNTR_STOP = 10                      ' Controller was stopped.
Public Const PI_CNTR_SST_OR_SCAN_RANGE = 11         ' Parameter for SST or for one of the embedded scan algorithms out of range.
Public Const PI_CNTR_INVALID_SCAN_AXES = 12         ' Invalid axis combination for fast scan.
Public Const PI_CNTR_INVALID_NAV_PARAM = 13         ' Parameter for NAV out of range.
Public Const PI_CNTR_INVALID_ANALOG_INPUT = 14      ' Invalid analog channel.
Public Const PI_CNTR_INVALID_AXIS_IDENTIFIER = 15   ' Invalid axis identifier.
Public Const PI_CNTR_INVALID_STAGE_NAME = 16        ' Unknown stage name.
Public Const PI_CNTR_PARAM_OUT_OF_RANGE = 17        ' Parameter out of range.
Public Const PI_CNTR_INVALID_MACRO_NAME = 18        ' Invalid macro name.
Public Const PI_CNTR_MACRO_RECORD = 19              ' Error while recording macro.
Public Const PI_CNTR_MACRO_NOT_FOUND = 20           ' Macro not found.
Public Const PI_CNTR_AXIS_HAS_NO_BRAKE = 21         ' Axis has no brake.
Public Const PI_CNTR_DOUBLE_AXIS = 22               ' Axis identifier given more than once.
Public Const PI_CNTR_INVALID_AXIS = 23              ' Invalid axis.
Public Const PI_CNTR_PARAM_NR = 24                  ' Incorrect number of parameters.
Public Const PI_CNTR_INVALID_REAL_NR = 25           ' Invalid floating point number.
Public Const PI_CNTR_MISSING_PARAM = 26             ' Missing parameter.
Public Const PI_CNTR_SOFT_LIMIT_OUT_OF_RANGE = 27   ' Soft limit out of range.
Public Const PI_CNTR_NO_MANUAL_PAD = 28             ' No manual pad connected.
Public Const PI_CNTR_NO_JUMP = 29                   ' PI_CNTR_NO_JUMP.
Public Const PI_CNTR_INVALID_JUMP = 30              ' PI_CNTR_INVALID_JUMP.
Public Const PI_CNTR_RESERVED_31 = 31               ' PI internal error code 31.
Public Const PI_CNTR_RESERVED_32 = 32               ' PI internal error code 32
Public Const PI_CNTR_NO_RELAY_CARD = 33             ' No relay card installed.
Public Const PI_CNTR_RESERVED_34 = 34               ' PI internal error code 34.
Public Const PI_CNTR_NO_DIGITAL_INPUT = 35          ' No digital input installed.
Public Const PI_CNTR_NO_DIGITAL_OUTPUT = 36         ' No digital output installed.
Public Const PI_CNTR_NO_AXIS = 200                  ' No stage connected.
Public Const PI_CNTR_NO_AXIS_PARAM_FILE = 201       ' PI_CNTR_NO_AXIS_PARAM_FILE.
Public Const PI_CNTR_INVALID_AXIS_PARAM_FILE = 202  ' PI_CNTR_INVALID_AXIS_PARAM_FILE.
Public Const PI_CNTR_NO_AXIS_PARAM_BACKUP = 203     ' PI_CNTR_NO_AXIS_PARAM_BACKUP.
Public Const PI_CNTR_SENDING_BUFFER_OVERFLOW = 301  ' PI_CNTR_SENDING_BUFFER_OVERFLOW.
Public Const PI_CNTR_VOLTAGE_OUT_OF_LIMITS = 302    ' Voltage out of limits.
Public Const PI_CNTR_VOLTAGE_SET_WHEN_SERVO_OFF = 303 ' Attempt to set voltage when servo on.
Public Const PI_CNTR_RECEIVING_BUFFER_OVERFLOW = 304 ' PI_CNTR_RECEIVING_BUFFER_OVERFLOW.
Public Const PI_CNTR_EEPROM_ERROR = 305             ' Error while reading/writing EEPROM.
Public Const PI_CNTR_I2C_ERROR = 306                ' Error on I2C bus.
Public Const PI_CNTR_RECEIVING_TIMEOUT = 307        ' Timeout while receiving command.
Public Const PI_CNTR_TOO_MANY_NESTED_MACROS = 1000  'Too many nested macros.
Public Const PI_CNTR_MACRO_ALREADY_DEFINED = 1001   ' Macro already defined.
Public Const PI_CNTR_NO_MACRO_RECORDING = 1002      ' No macro recording.
Public Const PI_CNTR_INVALID_MAC_PARAM = 1003       ' Invalid parameter for \c MAC*/.
Public Const PI_CNTR_RESERVED_1004 = 1004           ' IPI internal error code 31.
Public Const PI_CNTR_ALREDY_HAS_SERIAL_NUMBER = 2000 ' Controller already has a serial number.

