from ClassCongregation import ErrorLog


#只支持\xff格式的16进制
def XOR(Value:int, RawShellcode:bytes):
    # #逐字节读取，二进制文件数据，单个字节为16进制
    # f=open("payload.bin","rb")
    # code = f.read(1)
    Shellcode = ''#Value的最大值为0XFF，也就是int值255
    try:
        for SingleByte in RawShellcode:
            #如果是bytes类型的字符串，for循环会读取单个16进制然后转换成10进制
            XORValue = SingleByte ^ Value#进行xor操作
            Code = hex(XORValue)#转换会16进制
            Code = Code.replace('0x','')
            if(len(Code) == 1):
                Code = '0' + Code#位数补全
            Shellcode += '\\x' + Code
        return Shellcode
    except Exception as e:
        ErrorLog().Write("Web_AntiAntiVirus_EncryptionProcessing_XOR(def)", e)


# if __name__ == "__main__":
#     p1=open("/Users/ascotbe/Downloads/payload.bin","rb")
#     XOR(10, p1.read())
