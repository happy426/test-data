import cv2
import json
import os


# 默认从左下、右下、右上、左上排序
def paixu_bbox(list):
    x = [list[0][0], list[1][0], list[2][0], list[3][0]]
    y = [list[0][1], list[1][1], list[2][1], list[3][1]]
    ymin = min(y)
    ymax = max(y)
    xmin = min(x)
    xmax = max(x)
    return ymin, ymax, xmin, xmax


with open('../车牌检测/data03/测试集-车牌检测v4第二期-通用.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    num = 1
    for line in lines:
        line_str = json.loads(line)
        photo = line_str['url'].split('/')[-2] + '_' + line_str['url'].split('/')[-1]
        # print(photo)
        # if photo != '屏幕快照 2022-04-01 上午10.28.18.png':
        #     continue
        # 以下是获取抠图坐标
        read_path = '/Users/smai/Desktop/work/smmc上传ks/车辆检测/'\
                    + line_str['url'].split('/')[-2] + '/' + line_str['url'].split('/')[-1]
        out_path = '/Users/smai/Desktop/plate/koutu/' + photo

        img = cv2.imread(read_path)
        bbox = line_str['label'][0]['data'][0]['bbox'][0]
        ymin, ymax, xmin, xmax = paixu_bbox(bbox)
        crop_img = img[int(ymin):int(ymax), int(xmin):int(xmax)]
        cv2.imwrite(out_path, crop_img)
        print(f"第{num}张图" + '抠图完成，名为' + photo)
        num += 1

