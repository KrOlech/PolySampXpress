from ctypes import c_ulonglong, c_void_p, c_int


class DllCallBacks:
    counter = 0
    callbacksresults = []

    @staticmethod
    def Callback_Motion64(Param: c_ulonglong, UserParameter: c_void_p) -> c_int:
        print("Callback_Motion64(): INTERRUPT_PHYSICAL_MOTION_END Callback received. (Parameter: %I64u)\n", Param)
        return c_int(0)

    @staticmethod
    def Callback_Motor64(Param: c_ulonglong, UserParameter: c_void_p) -> c_int:
        print("Callback_Motor64(): INTERRUPT_MOTOR_FAILURE Callback received. (Parameter: %I64u)\n", Param)
        return c_int(0)

    def Callback_ProgramEx64(self, Param: c_ulonglong, UserParameter: c_void_p) -> c_int:
        # Stop the timer
        self.master.preciseTimer.StopTimer()

        # Measure the time
        i64Counter = self.master.preciseTimer.GetTime()
        self.callbacksresults.append(i64Counter)

        Param1 = Param.value >> 32
        Param2 = Param.value & 0x00000000FFFFFFFF

        print(
            "Callback_ProgramEx64(): ACSC_INTR_ACSPL_PROGRAM_EX Callback received (counter = %d). (Parameter 1: 0x%x, Parameter 2: 0x%x), Time = %I64d microseconds\n",
            len(self.callbacksresults), Param1, Param2, i64Counter)

        return c_int(0)

    @staticmethod
    def Callback_SystemError64(Param: c_ulonglong, UserParameter: c_void_p) -> c_int:
        print("Callback_SystemError64(): ACSC_INTR_SYSTEM_ERROR Callback received. (Parameter: %I64u)\n", Param)
        return c_int(0)

    @staticmethod
    def Callback_EtherCATError64(Param: c_ulonglong, UserParameter: c_void_p) -> c_int:
        print("Callback_EtherCATError64(): ACSC_INTR_ETHERCAT_ERROR Callback received. (Parameter: %I64u)\n", Param)
        return c_int(0)

    @staticmethod
    def Callback_Emergency(Param: c_ulonglong, UserParameter: c_void_p) -> c_int:
        print("Callback_Emergency(): ACSC_INTR_EMERGENCY Callback received. (Parameter: %I64u)\n", Param)
        return c_int(0)
