import cv2
import time
import config
from nonebot import on_command, CommandSession,message,get_bot
# FaceCascadePath="haarcascade_frontalface.xml"
# FaceCascade = cv2.CascadeClassifier(FaceCascadePath)
#传入人脸训练模块
FaceCascade = cv2.CascadeClassifier(config.FaceCascadePath)
# 打开视频捕获设备

bot =get_bot()
video_capture = cv2.VideoCapture(0)
@on_command('开启监控')
async def OpenFace(session: CommandSession):
    if session.ctx['user_id'] ==config.super_administrator:#如果是超级管理员
    #await session.send(message.MessageSegment.at(user_qq_id) + help_list)
        face_time_recording_start = int(time.time())
        face_time_recording_end = 5
        while True:
            if not video_capture.isOpened():  # 检查它是否被初始化
                time.sleep(5)
                pass
            # 读视频帧
            ret, frame = video_capture.read()  # 如果帧被正确读取，则为True
            # 转为灰度图像
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 调用分类器进行检测,如果有人脸返回一个列表
            faces = FaceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            if len(faces) > 0:  # 如果检测到值就写入
                cv2.imwrite(str(int(time.time())) + '.jpg', frame)  # 存储为图像
                await bot.send_private_msg(self_id=session.self_id, user_id=config.super_administrator, message='警戒警戒！[CQ:emoji,id=127917]莎莎检测到有人入侵！数据以保存喵~[CQ:emoji,id=128687]')#对超级用户发送通知
                #await session.send(message.MessageSegment.at(session.ctx['user_id']) + )

            # 画矩形框
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # 显示视频
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


@on_command('关闭监控')
async def CloseFace(session: CommandSession):
    if session.ctx['user_id'] in config.super_administrator:#如果是超级管理员
    #await session.send(message.MessageSegment.at(user_qq_id) + help_list)
        CloseFaceDetection(video_capture)#调用关闭视频函数



def CloseFaceDetection(video_capture):

    # 关闭摄像头设备
    video_capture.release()
    return "关闭成功"
    # 关闭所有窗口
    #cv2.destroyAllWindows()
