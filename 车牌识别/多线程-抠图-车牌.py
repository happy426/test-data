# -*- coding:utf-8 -*-
# @Time:2022/1/6 0006 17:27
# @Author:yangjun
# File:多线程-专项头盔抠图.py
import os
import cv2
import json
import numpy as np
import argparse
import requests
import threading
import time

# 车牌图抠出来后打包上传

parser = argparse.ArgumentParser(description='make json file')
parser.add_argument('--bath_dir', default=r"L:", type=str, help='image file or txt of file names')
args = parser.parse_args()
bath_dir = args.bath_dir
picItmes = []
glock = threading.Lock()


def is_Chinease(string):
    for i in string:
        if u'\u4e00' <= i <= u'\u9fff':
            return True
    return False


# 默认从左下、右下、右上、左上排序
def paixu_bbox(list):
    x = [list[0][0], list[1][0], list[2][0], list[3][0]]
    y = [list[0][1], list[1][1], list[2][1], list[3][1]]
    ymin = min(y)
    ymax = max(y)
    xmin = min(x)
    xmax = max(x)
    photo = [ymin, ymax, xmin, xmax]
    return photo


# 得到 未抠图的抠图信息，包括抠图后的存放路径，被扣图的坐标，放到一个字典里面
class GetPicItems(threading.Thread):
    def run(self):
        while (len(lines) > 0):
            glock.acquire()
            line = lines.pop()
            glock.release()
            line_dict = json.loads(line)
            # 过滤无效
            if line_dict['annotation']['classifications'][-1]['value']:
                continue
            url = line_dict['url']
            file = requests.get(url)
            imgBig = cv2.imdecode(np.frombuffer(file.content, np.uint8), 1)
            print('读取{}'.format(url.split('/')[-1]))
            h = imgBig[0]
            w = imgBig[1]
            # 一张图里面，扣多图操作：

            if len(line_dict['annotation']['detections']) == 0:
                continue
            box_list = line_dict['annotation']['detections']
            # 多对象处理，所有抠图的对象都已字典格式存放在box_list中
            glock.acquire()
            for index in range(0, len(box_list)):
                imgname = url.split('/')[-1].split('?')[0]
                imglist = os.listdir('/Users/smai/Desktop/plate/v4plate/')
                if imgname not in imglist:
                    print('存放{}'.format(imgname))
                    # 分别获取抠图图片的存放路径，抠图图片的坐标
                    box_item = box_list[index]
                    dir_name = box_item['key']
                    savepath = os.path.join(saveBasepath, dir_name)
                    if not os.path.exists(savepath):
                        os.mkdir(savepath)
                    imgSavepath = os.path.join(savepath, imgname)
                    bbox = box_item['value']
                    bbox_new = paixu_bbox(bbox)
                    picItmes.append({'img': imgBig, 'imgsavePath': imgSavepath, 'bbox': bbox_new})
            print('都读取完成')
            glock.release()


class kouPic(threading.Thread):
    def run(self):
        while True:
            glock.acquire()
            if len(picItmes) == 0:
                glock.release()
            else:
                picitem = picItmes.pop()
                glock.release()
                img = picitem['img']
                imgsavePath = picitem['imgsavePath']
                bbox = picitem['bbox']
                ymin = bbox[0]
                ymax = bbox[1]
                xmin = bbox[2]
                xmax = bbox[3]
                crop_img = img[int(ymin):int(ymax), int(xmin):int(xmax)]
                if len(crop_img) == 0:
                    continue
                # cv2.imwrite，路径不能带中文的
                cv2.imwrite(imgsavePath, crop_img)
                print('抠图{}'.format(imgsavePath.split('/')[-1]))


if __name__ == '__main__':
    # 文件地址传参
    r_path = r'data04/TASK_测试集_车牌20220105_2850.json'
    # dstpath路径不能带中文的,原因就是cv2.imwrite，入参路径不能带中文的
    r_f = open(r_path, 'r', encoding='utf-8')
    lines = r_f.readlines()
    saveBasepath = '/Users/smai/Desktop/plate/v4plate/'
    for x in range(20):
        g = GetPicItems()
        g.start()
    for x in range(10):
        k = kouPic()
        k.start()
