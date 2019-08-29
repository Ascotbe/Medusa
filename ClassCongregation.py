class WriteFile:
    def Write(vul,FileName):
        FileNames = FileName + ".txt"
        with open(FileNames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul+ "\n")
