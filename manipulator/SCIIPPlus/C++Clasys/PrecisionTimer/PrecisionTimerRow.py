import time
import ctypes.wintypes


class CPreciseTimer:
    m_i64Start = 0
    m_i64Elapsed = 0

    m_bRunning = False

    m_i64Counts = int()
    m_liCount = int()

    sm_bInit = False

    __freq = None

    @property
    def sm_i64Freq(self):
        return self.__freq

    @sm_i64Freq.setter
    def sm_i64Freq(self, a: int):
        if self.__freq is None:
            self.__freq = a

    __PerformanceCounter = None

    @property
    def sm_bPerformanceCounter(self):
        return self.__PerformanceCounter

    @sm_bPerformanceCounter.setter
    def sm_bPerformanceCounter(self, a: bool):
        if self.__PerformanceCounter in None:
            self.__PerformanceCounter = a

    def __init__(self):

        self.kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        self.sm_i64Freq = self.QueryPerformanceFrequency()
        self.sm_bPerformanceCounter = self.sm_i64Freq

    def SupportsHighResCounter(self):
        return self.sm_bPerformanceCounter

    def StartTimer(self):
        if self.sm_bPerformanceCounter:
            self.m_i64Start = self.QueryPerformanceCounter()
            self.m_i64Start *= 1000000
            self.m_i64Start /= self.sm_i64Freq

        else:
            self.m_i64Start = self.GetTickCount()
        self.m_bRunning = True

    def StopTimer(self):
        self.UpdateElapsed()
        self.m_bRunning = False

    def GetTime(self):
        if self.m_bRunning:
            self.UpdateElapsed()
        return self.m_i64Elapsed

    def UpdateElapsed(self):
        if self.sm_bPerformanceCounter:
            self.m_i64Counts = self.QueryPerformanceCounter()
            self.m_i64Counts *= 1000000
            self.m_i64Counts /= self.sm_i64Freq

        else:
            self.m_i64Counts = self.GetTickCount()

        if self.m_i64Counts > self.m_i64Start:
            self.m_i64Elapsed = self.m_i64Counts - self.m_i64Start
        else:
            self.m_i64Elapsed = (0x7fffffffffffffff - self.m_i64Start) + self.m_i64Counts

    @staticmethod
    def GetTickCount():
        return time.time_ns() // 1000

    def QueryPerformanceCounter(self):
        frequency = ctypes.wintypes.LARGE_INTEGER()
        self.kernel32.QueryPerformanceFrequency(ctypes.byref(frequency))
        return int(frequency.value)

    def QueryPerformanceFrequency(self):
        timePoint = ctypes.wintypes.LARGE_INTEGER()
        self.kernel32.QueryPerformanceCounter(ctypes.byref(timePoint))
        return int(timePoint.value)
