import cv2
import os

i = 0
j = 0
filepath = '/Users/smai/Desktop/plate/shipin'
pathDir = os.listdir(filepath)
save_filename = '/Users/smai/Desktop/plate/jiezhen/'
timeF = 48  # 截图时间间隔


def saveImage(frame, SaveAddress, num):
    try:
        address = SaveAddress + str(num) + '.jpg'
        cv2.imencode('.jpg', frame)[1].tofile(address)
        print(num)
    except Exception:
        print(address)


for allDir in pathDir:
    videopath = filepath + '/' + allDir
    name = videopath.split("/")[-1]
    if '.mp4' in name:
        new_name = name.replace('.mp4', '')
        photo_name = save_filename + new_name
        videoCapture = cv2.VideoCapture(videopath)
        if videoCapture.isOpened():  # 判断是否正常打开
            rval, frame = videoCapture.read()
        else:
            rval = False
            print("false")
        while rval:
            rval, frame = videoCapture.read()
            if (i % timeF == 0):
                j += 1
                saveImage(frame, photo_name, j)
                pass
            i += 1
