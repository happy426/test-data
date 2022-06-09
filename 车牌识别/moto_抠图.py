import cv2
import json
import os

with open('data04/TASK_测试集-上海摩托车-抠图_3043.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_str = json.loads(line)
        photo = line_str['url'].split('/')[-1]
        # print(photo)
        # if photo != '屏幕快照 2022-04-01 上午10.28.18.png':
        #     continue
        if line_str['annotation'] is None:
            continue
        # 以下是获取抠图坐标
        box_list = line_str['annotation']['detections']
        if box_list is None:
            continue

        read_path = '/Users/smai/Desktop/plate/moto_plate/' + photo
        out_path = '/Users/smai/Desktop/plate/newmoto/' + photo

        img = cv2.imread(read_path)
        bbox = box_list[0]['value']

        w = line_str['meta']['width']
        h = line_str['meta']['height']
        # print(w,h)

        xmin = bbox['x']
        ymin = bbox['y']
        xmax = xmin + bbox['width']
        ymax = ymin + bbox['height']
        if xmin < 0:
            xmin = 0
        if ymin < 0:
            ymin = 0
        if xmax > w:
            xmax = w
        if ymax > h:
            ymax = h
        # print(int(xmax), int(ymax))
        crop_img = img[int(ymin):int(ymax), int(xmin):int(xmax)]
        cv2.imwrite(out_path, crop_img)

