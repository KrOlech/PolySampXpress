from ctypes import c_double, c_uint, LittleEndianStructure, c_uint32, c_char, c_ulonglong, Structure, c_float, c_ubyte, \
    c_int, c_longlong


class Result:
    Ok = 0
    Error = -1
    NotImplemented = -2
    ValueError = -3
    NoDevice = -4


class calibration_t(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('A', c_double),
        ('MicrostepMode', c_uint)
    ]


class device_enumeration_t(LittleEndianStructure):
    pass


class home_settings_calb_t(Structure):
    _fields_ = [
        ("FastHome", c_float),
        ("SlowHome", c_float),
        ("HomeDelta", c_float),
        ("HomeFlags", c_uint),
    ]


class device_network_information_t(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('ipv4', c_uint32),
        ('nodename', c_char * 16),
        ('axis_state', c_uint),
        ('locker_username', c_char * 16),
        ('locker_nodename', c_char * 16),
        ('locked_time', c_ulonglong),
    ]


class feedback_settings_t(Structure):
    _fields_ = [
        ("IPS", c_uint),
        ("FeedbackType", c_uint),
        ("FeedbackFlags", c_uint),
        ("CountsPerTurn", c_uint),
    ]


class home_settings_t(Structure):
    _fields_ = [
        ("FastHome", c_uint),
        ("uFastHome", c_uint),
        ("SlowHome", c_uint),
        ("uSlowHome", c_uint),
        ("HomeDelta", c_int),
        ("uHomeDelta", c_int),
        ("HomeFlags", c_uint),
    ]


class move_settings_t(Structure):
    _fields_ = [
        ("Speed", c_uint),
        ("uSpeed", c_uint),
        ("Accel", c_uint),
        ("Decel", c_uint),
        ("AntiplaySpeed", c_uint),
        ("uAntiplaySpeed", c_uint),
        ("MoveFlags", c_uint),
    ]


class move_settings_calb_t(Structure):
    _fields_ = [
        ("Speed", c_float),
        ("Accel", c_float),
        ("Decel", c_float),
        ("AntiplaySpeed", c_float),
        ("MoveFlags", c_uint),
    ]


class engine_settings_t(Structure):
    _fields_ = [
        ("NomVoltage", c_uint),
        ("NomCurrent", c_uint),
        ("NomSpeed", c_uint),
        ("uNomSpeed", c_uint),
        ("EngineFlags", c_uint),
        ("Antiplay", c_int),
        ("MicrostepMode", c_uint),
        ("StepsPerRev", c_uint),
    ]


class engine_settings_calb_t(Structure):
    _fields_ = [
        ("NomVoltage", c_uint),
        ("NomCurrent", c_uint),
        ("NomSpeed", c_float),
        ("EngineFlags", c_uint),
        ("Antiplay", c_float),
        ("MicrostepMode", c_uint),
        ("StepsPerRev", c_uint),
    ]


class entype_settings_t(Structure):
    _fields_ = [
        ("EngineType", c_uint),
        ("DriverType", c_uint),
    ]


class power_settings_t(Structure):
    _fields_ = [
        ("HoldCurrent", c_uint),
        ("CurrReductDelay", c_uint),
        ("PowerOffDelay", c_uint),
        ("CurrentSetTime", c_uint),
        ("PowerFlags", c_uint),
    ]


class secure_settings_t(Structure):
    _fields_ = [
        ("LowUpwrOff", c_uint),
        ("CriticalIpwr", c_uint),
        ("CriticalUpwr", c_uint),
        ("CriticalT", c_uint),
        ("CriticalIusb", c_uint),
        ("CriticalUusb", c_uint),
        ("MinimumUusb", c_uint),
        ("Flags", c_uint),
    ]


class edges_settings_t(Structure):
    _fields_ = [
        ("BorderFlags", c_uint),
        ("EnderFlags", c_uint),
        ("LeftBorder", c_int),
        ("uLeftBorder", c_int),
        ("RightBorder", c_int),
        ("uRightBorder", c_int),
    ]


class edges_settings_calb_t(Structure):
    _fields_ = [
        ("BorderFlags", c_uint),
        ("EnderFlags", c_uint),
        ("LeftBorder", c_float),
        ("RightBorder", c_float),
    ]


class pid_settings_t(Structure):
    _fields_ = [
        ("KpU", c_uint),
        ("KiU", c_uint),
        ("KdU", c_uint),
        ("Kpf", c_float),
        ("Kif", c_float),
        ("Kdf", c_float),
    ]


class sync_in_settings_t(Structure):
    _fields_ = [
        ("SyncInFlags", c_uint),
        ("ClutterTime", c_uint),
        ("Position", c_int),
        ("uPosition", c_int),
        ("Speed", c_uint),
        ("uSpeed", c_uint),
    ]


class sync_in_settings_calb_t(Structure):
    _fields_ = [
        ("SyncInFlags", c_uint),
        ("ClutterTime", c_uint),
        ("Position", c_float),
        ("Speed", c_float),
    ]


class sync_out_settings_t(Structure):
    _fields_ = [
        ("SyncOutFlags", c_uint),
        ("SyncOutPulseSteps", c_uint),
        ("SyncOutPeriod", c_uint),
        ("Accuracy", c_uint),
        ("uAccuracy", c_uint),
    ]


class sync_out_settings_calb_t(Structure):
    _fields_ = [
        ("SyncOutFlags", c_uint),
        ("SyncOutPulseSteps", c_uint),
        ("SyncOutPeriod", c_uint),
        ("Accuracy", c_float),
    ]


class extio_settings_t(Structure):
    _fields_ = [
        ("EXTIOSetupFlags", c_uint),
        ("EXTIOModeFlags", c_uint),
    ]


class brake_settings_t(Structure):
    _fields_ = [
        ("t1", c_uint),
        ("t2", c_uint),
        ("t3", c_uint),
        ("t4", c_uint),
        ("BrakeFlags", c_uint),
    ]


class control_settings_t(Structure):
    _fields_ = [
        ("MaxSpeed", c_uint * 10),
        ("uMaxSpeed", c_uint * 10),
        ("Timeout", c_uint * 9),
        ("MaxClickTime", c_uint),
        ("Flags", c_uint),
        ("DeltaPosition", c_int),
        ("uDeltaPosition", c_int),
    ]


class control_settings_calb_t(Structure):
    _fields_ = [
        ("MaxSpeed", c_float * 10),
        ("Timeout", c_uint * 9),
        ("MaxClickTime", c_uint),
        ("Flags", c_uint),
        ("DeltaPosition", c_float),
    ]


class joystick_settings_t(Structure):
    _fields_ = [
        ("JoyLowEnd", c_uint),
        ("JoyCenter", c_uint),
        ("JoyHighEnd", c_uint),
        ("ExpFactor", c_uint),
        ("DeadZone", c_uint),
        ("JoyFlags", c_uint),
    ]


class ctp_settings_t(Structure):
    _fields_ = [
        ("CTPMinError", c_uint),
        ("CTPFlags", c_uint),
    ]


class uart_settings_t(Structure):
    _fields_ = [
        ("Speed", c_uint),
        ("UARTSetupFlags", c_uint),
    ]


class calibration_settings_t(Structure):
    _fields_ = [
        ("CSS1_A", c_float),
        ("CSS1_B", c_float),
        ("CSS2_A", c_float),
        ("CSS2_B", c_float),
        ("FullCurrent_A", c_float),
        ("FullCurrent_B", c_float),
    ]


class controller_name_t(Structure):
    _fields_ = [
        ("ControllerName", c_char * 17),
        ("CtrlFlags", c_uint),
    ]


class nonvolatile_memory_t(Structure):
    _fields_ = [
        ("UserData", c_uint * 7),
    ]


class emf_settings_t(Structure):
    _fields_ = [
        ("L", c_float),
        ("R", c_float),
        ("Km", c_float),
        ("BackEMFFlags", c_uint),
    ]


class engine_advansed_setup_t(Structure):
    _fields_ = [
        ("stepcloseloop_Kw", c_uint),
        ("stepcloseloop_Kp_low", c_uint),
        ("stepcloseloop_Kp_high", c_uint),
    ]


class extended_settings_t(Structure):
    _fields_ = [
        ("Param1", c_uint),
    ]


class get_position_t(Structure):
    _fields_ = [
        ("Position", c_int),
        ("uPosition", c_int),
        ("EncPosition", c_longlong),
    ]


class get_position_calb_t(Structure):
    _fields_ = [
        ("Position", c_float),
        ("EncPosition", c_longlong),
    ]


class set_position_t(Structure):
    _fields_ = [
        ("Position", c_int),
        ("uPosition", c_int),
        ("EncPosition", c_longlong),
        ("PosFlags", c_uint),
    ]


class set_position_calb_t(Structure):
    _fields_ = [
        ("Position", c_float),
        ("EncPosition", c_longlong),
        ("PosFlags", c_uint),
    ]


class status_t(Structure):
    _fields_ = [
        ("MoveSts", c_uint),
        ("MvCmdSts", c_uint),
        ("PWRSts", c_uint),
        ("EncSts", c_uint),
        ("WindSts", c_uint),
        ("CurPosition", c_int),
        ("uCurPosition", c_int),
        ("EncPosition", c_longlong),
        ("CurSpeed", c_int),
        ("uCurSpeed", c_int),
        ("Ipwr", c_int),
        ("Upwr", c_int),
        ("Iusb", c_int),
        ("Uusb", c_int),
        ("CurT", c_int),
        ("Flags", c_uint),
        ("GPIOFlags", c_uint),
        ("CmdBufFreeSpace", c_uint),
    ]


class status_calb_t(Structure):
    _fields_ = [
        ("MoveSts", c_uint),
        ("MvCmdSts", c_uint),
        ("PWRSts", c_uint),
        ("EncSts", c_uint),
        ("WindSts", c_uint),
        ("CurPosition", c_float),
        ("EncPosition", c_longlong),
        ("CurSpeed", c_float),
        ("Ipwr", c_int),
        ("Upwr", c_int),
        ("Iusb", c_int),
        ("Uusb", c_int),
        ("CurT", c_int),
        ("Flags", c_uint),
        ("GPIOFlags", c_uint),
        ("CmdBufFreeSpace", c_uint),
    ]


class measurements_t(Structure):
    _fields_ = [
        ("Speed", c_int * 25),
        ("Error", c_int * 25),
        ("Length", c_uint),
    ]


class chart_data_t(Structure):
    _fields_ = [
        ("WindingVoltageA", c_int),
        ("WindingVoltageB", c_int),
        ("WindingVoltageC", c_int),
        ("WindingCurrentA", c_int),
        ("WindingCurrentB", c_int),
        ("WindingCurrentC", c_int),
        ("Pot", c_uint),
        ("Joy", c_uint),
        ("DutyCycle", c_int),
    ]


class serial_number_t(Structure):
    _fields_ = [
        ("SN", c_uint),
        ("Key", c_ubyte * 32),
        ("Major", c_uint),
        ("Minor", c_uint),
        ("Release", c_uint),
    ]


class analog_data_t(Structure):
    _fields_ = [
        ("A1Voltage_ADC", c_uint),
        ("A2Voltage_ADC", c_uint),
        ("B1Voltage_ADC", c_uint),
        ("B2Voltage_ADC", c_uint),
        ("SupVoltage_ADC", c_uint),
        ("ACurrent_ADC", c_uint),
        ("BCurrent_ADC", c_uint),
        ("FullCurrent_ADC", c_uint),
        ("Temp_ADC", c_uint),
        ("Joy_ADC", c_uint),
        ("Pot_ADC", c_uint),
        ("L5_ADC", c_uint),
        ("H5_ADC", c_uint),
        ("A1Voltage", c_int),
        ("A2Voltage", c_int),
        ("B1Voltage", c_int),
        ("B2Voltage", c_int),
        ("SupVoltage", c_int),
        ("ACurrent", c_int),
        ("BCurrent", c_int),
        ("FullCurrent", c_int),
        ("Temp", c_int),
        ("Joy", c_int),
        ("Pot", c_int),
        ("L5", c_int),
        ("H5", c_int),
        ("deprecated", c_uint),
        ("R", c_int),
        ("L", c_int),
    ]


class debug_read_t(Structure):
    _fields_ = [
        ("DebugData", c_ubyte * 128),
    ]


class debug_write_t(Structure):
    _fields_ = [
        ("DebugData", c_ubyte * 128),
    ]


class stage_name_t(Structure):
    _fields_ = [
        ("PositionerName", c_char * 17),
    ]


class stage_information_t(Structure):
    _fields_ = [
        ("Manufacturer", c_char * 17),
        ("PartNumber", c_char * 25),
    ]


class stage_settings_t(Structure):
    _fields_ = [
        ("LeadScrewPitch", c_float),
        ("Units", c_char * 9),
        ("MaxSpeed", c_float),
        ("TravelRange", c_float),
        ("SupplyVoltageMin", c_float),
        ("SupplyVoltageMax", c_float),
        ("MaxCurrentConsumption", c_float),
        ("HorizontalLoadCapacity", c_float),
        ("VerticalLoadCapacity", c_float),
    ]


class motor_information_t(Structure):
    _fields_ = [
        ("Manufacturer", c_char * 17),
        ("PartNumber", c_char * 25),
    ]


class motor_settings_t(Structure):
    _fields_ = [
        ("MotorType", c_uint),
        ("ReservedField", c_uint),
        ("Poles", c_uint),
        ("Phases", c_uint),
        ("NominalVoltage", c_float),
        ("NominalCurrent", c_float),
        ("NominalSpeed", c_float),
        ("NominalTorque", c_float),
        ("NominalPower", c_float),
        ("WindingResistance", c_float),
        ("WindingInductance", c_float),
        ("RotorInertia", c_float),
        ("StallTorque", c_float),
        ("DetentTorque", c_float),
        ("TorqueConstant", c_float),
        ("SpeedConstant", c_float),
        ("SpeedTorqueGradient", c_float),
        ("MechanicalTimeConstant", c_float),
        ("MaxSpeed", c_float),
        ("MaxCurrent", c_float),
        ("MaxCurrentTime", c_float),
        ("NoLoadCurrent", c_float),
        ("NoLoadSpeed", c_float),
    ]


class encoder_information_t(Structure):
    _fields_ = [
        ("Manufacturer", c_char * 17),
        ("PartNumber", c_char * 25),
    ]


class encoder_settings_t(Structure):
    _fields_ = [
        ("MaxOperatingFrequency", c_float),
        ("SupplyVoltageMin", c_float),
        ("SupplyVoltageMax", c_float),
        ("MaxCurrentConsumption", c_float),
        ("PPR", c_uint),
        ("EncoderSettings", c_uint),
    ]


class hallsensor_information_t(Structure):
    _fields_ = [
        ("Manufacturer", c_char * 17),
        ("PartNumber", c_char * 25),
    ]


class hallsensor_settings_t(Structure):
    _fields_ = [
        ("MaxOperatingFrequency", c_float),
        ("SupplyVoltageMin", c_float),
        ("SupplyVoltageMax", c_float),
        ("MaxCurrentConsumption", c_float),
        ("PPR", c_uint),
    ]


class gear_information_t(Structure):
    _fields_ = [
        ("Manufacturer", c_char * 17),
        ("PartNumber", c_char * 25),
    ]


class gear_settings_t(Structure):
    _fields_ = [
        ("ReductionIn", c_float),
        ("ReductionOut", c_float),
        ("RatedInputTorque", c_float),
        ("RatedInputSpeed", c_float),
        ("MaxOutputBacklash", c_float),
        ("InputInertia", c_float),
        ("Efficiency", c_float),
    ]


class accessories_settings_t(Structure):
    _fields_ = [
        ("MagneticBrakeInfo", c_char * 25),
        ("MBRatedVoltage", c_float),
        ("MBRatedCurrent", c_float),
        ("MBTorque", c_float),
        ("MBSettings", c_uint),
        ("TemperatureSensorInfo", c_char * 25),
        ("TSMin", c_float),
        ("TSMax", c_float),
        ("TSGrad", c_float),
        ("TSSettings", c_uint),
        ("LimitSwitchesSettings", c_uint),
    ]


class init_random_t(Structure):
    _fields_ = [
        ("key", c_ubyte * 16),
    ]


class globally_unique_identifier_t(Structure):
    _fields_ = [
        ("UniqueID0", c_uint),
        ("UniqueID1", c_uint),
        ("UniqueID2", c_uint),
        ("UniqueID3", c_uint),
    ]
