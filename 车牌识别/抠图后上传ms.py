"""
场景标和检测标是一样多的
先把两个数据集合并，再去除无效标签，可以节约脚本执行时间。
"""
import json

# 场景
f1 = open('../车牌检测/data03/TASK_测试集-车牌检测v4第二期-场景_3038.json', 'r', encoding='utf-8')
# 检测
f2 = open('../车牌检测/data03/TASK_测试集-车牌检测v4第二期-检测_3039.json', 'r', encoding='utf-8')
w = open('./data04/测试集-车牌识别v4第二期-通用.json', 'w', encoding='utf-8')

lines1 = f1.readlines()
lines2 = f2.readlines()


def get_colour(colour):
    if colour == '单层黄色' or colour == '单层黄牌':
        return "s_yellow"
    elif colour == '单层蓝色' or colour == '单层蓝牌':
        return "s_blue"
    elif colour == '单层绿色' or colour == '单层绿牌':
        return "s_green"
    elif colour == '双层黄色' or colour == '双层黄牌':
        return "d_yellow"
    elif colour == '单层白色' or colour == '单层白牌':
        return "s_white"
    elif colour == '双层白色' or colour == '双层白牌':
        return "d_white"
    elif colour == '双层蓝色' or colour == '双层蓝牌':
        return "d_blue"


for i in range(len(lines1)):
    line1_str = json.loads(lines1[i])
    line2_str = json.loads(lines2[i])
    photo1 = line1_str['url'].split('/')[-2] + '_' + line1_str['url'].split('/')[-1]
    photo2 = line2_str['url'].split('/')[-2] + '_' + line2_str['url'].split('/')[-1]
    if photo1 != photo2:
        continue
    url = 'ks:///personal/QA/test/车牌识别/v4/' + photo1
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

    plate = line2_str['annotation']['detections'][0]['classifications'][0]['value']
    if plate is None:
        plate = ''
    attribute = line2_str['annotation']['detections'][0]['classifications'][1]['value']
    attribute = get_colour(attribute)
    if plate != '':
        clarity = 'clear'
    else:
        clarity = 'blur'
    if line2_str['annotation']['classifications'][-1]['value']:
        continue
    l_json = {"url": url,
              "type": "image",
              "label": [{"data": [{"class": [plate, attribute, clarity]}],
                         "name": "general", "type": "ocr"}],
              "test_tags": [type, light, difficulty]}
    w.write(json.dumps(l_json, ensure_ascii=False) + '\n')








