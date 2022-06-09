# -*- coding:utf-8 -*-
# @Time:2022/1/6 0006 17:27
# @Author:yangjun
# File:多线程-专项头盔抠图.py
import os
import cv2
import json
import argparse
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


# 得到 未抠图的抠图信息，包括抠图后的存放路径，被扣图的坐标，放到一个字典里面
class GetPicItems(threading.Thread):
    def run(self):
        while (len(lines) > 0):
            glock.acquire()
            line = lines.pop()
            glock.release()
            line_dict = json.loads(line)
            # 过滤无效
            if len(line_dict['annotation']['detections']) == 0:
                continue
            url = line_dict['url']
            photo = url.split('/')[-1]
            file = '/Users/smai/Desktop/plate/shfjdc/' + photo
            imgBig = cv2.imread(file)
            print('读取{}'.format(url.split('/')[-1]))
            # 一张图里面，扣多图操作：

            if len(line_dict['annotation']['detections']) == 0:
                continue
            box_list = line_dict['annotation']['detections']
            # 多对象处理，所有抠图的对象都已字典格式存放在box_list中
            glock.acquire()
            for index in range(0, len(box_list)):
                imgname = box_list[index]['id'] + url.split('/')[-1]
                imglist = os.listdir('/Users/smai/Desktop/plate/non_motor/')
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
                    bbox_new = [bbox['x'], bbox['y'], bbox['width'], bbox['height']]
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
                ymin = bbox[1]
                ymax = bbox[1] + bbox[3]
                xmin = bbox[0]
                xmax = bbox[0] + bbox[2]
                crop_img = img[int(ymin):int(ymax), int(xmin):int(xmax)]
                if len(crop_img) == 0:
                    continue
                # cv2.imwrite，路径不能带中文的
                cv2.imwrite(imgsavePath, crop_img)
                print('抠图{}'.format(imgsavePath.split('/')[-1]))


if __name__ == '__main__':
    # 文件地址传参
    r_path = r'data06/TASK_测试集-非机动车行为属性-上海-抠图_3041.json'
    # dstpath路径不能带中文的,原因就是cv2.imwrite，入参路径不能带中文的
    r_f = open(r_path, 'r', encoding='utf-8')
    lines = r_f.readlines()
    saveBasepath = '/Users/smai/Desktop/plate/non_motor/'
    for x in range(20):
        g = GetPicItems()
        g.start()
    for x in range(10):
        k = kouPic()
        k.start()
