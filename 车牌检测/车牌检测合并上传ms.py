"""
场景标和检测标是一样多的
先把两个数据集合并，再去除无效标签，可以节约脚本执行时间。
"""
import json

# 场景
f1 = open('./data03/TASK_测试集-车牌检测v4第二期-场景_3038.json', 'r', encoding='utf-8')
# 检测
f2 = open('./data03/TASK_测试集-车牌检测v4第二期-检测_3039.json', 'r', encoding='utf-8')
w = open('./data03/测试集-车牌检测v4第二期-通用.json', 'w', encoding='utf-8')

lines1 = f1.readlines()
lines2 = f2.readlines()


# 默认从左下、右下、右上、左上排序
def paixu_bbox(list):
    for index in range(0, len(list) - 2):
        # 先比纵坐标，小的排前面，大的排后面
        if list[index][1] > list[index + 2][1]:
            temp2 = list[index + 2]
            temp1 = list[index]
            list[index] = temp2
            list[index + 2] = temp1
    # 纵坐标比完了，低的2个在最前面，就是左下和右下的判断了
    # 左下排第一个，右下排第二个
    if (list[0][0] > list[1][0]):
        temp2 = list[1]
        temp1 = list[0]
        list[0] = temp2
        list[1] = temp1

        # 右上排第3个，左上排第4个
    if (list[2][0] < list[3][0]):
        temp2 = list[3]
        temp1 = list[2]
        list[2] = temp2
        list[3] = temp1
    return list


for i in range(len(lines1)):
    line1_str = json.loads(lines1[i])
    line2_str = json.loads(lines2[i])
    url = line1_str['url']
    url2 = line2_str['url']
    if url != url2:
        continue
    type = line1_str['annotation']['classifications'][0]['value']
    light = line1_str['annotation']['classifications'][1]['value']
    difficulty = ''
    if len(line1_str['annotation']['classifications']) == 3:
        difficulty = line1_str['annotation']['classifications'][2]['value']
        if difficulty:
            difficulty = '难例'
        else:
            difficulty = ''

    if len(line1_str['annotation']['classifications']) == 4:
        if line1_str['annotation']['classifications'][3]['value']:
            continue

    new_img_json = {
        "url": url,
        "type": "image",
        "test_tags": [type, light, difficulty],
        "invalid": False,
        "label": [
            {
                "name": "outline",
                "type": "detection",
                "version": "1",
                "data": [

                ]
            }
        ]
    }
    for obj in line2_str['annotation']['detections']:
        value = obj['value']
        new_obj = {
            "class": ['plate'],
            "bbox": paixu_bbox(value)
        }
        new_img_json['label'][0]['data'].append(new_obj)
    w.writelines(json.dumps(new_img_json, ensure_ascii=False) + '\n')
