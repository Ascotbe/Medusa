def Result(test):
    if test.find("Active Internet connections") != -1:
        return "Linux"
    elif test.find("Active Connections") != -1:
        return "Windows"
    elif test.find("活动连接") != -1:
        return "Windows"
    elif test.find("LISTEN") != -1:
        return "NoteOS"