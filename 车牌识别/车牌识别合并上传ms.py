"""
场景标和检测标是一样多的
先把两个数据集合并，再去除无效标签，可以节约脚本执行时间。
"""
import json

# 场景
f1 = open('./data04/TASK_测试集-车牌识别第二期-场景_3027.json', 'r', encoding='utf-8')
# 检测
f2 = open('./data04/TASK_测试集-车牌识别第二期-检测_3029.json', 'r', encoding='utf-8')
w = open('./data04/测试集-车牌识别-上海.json', 'w', encoding='utf-8')

lines1 = f1.readlines()
lines2 = f2.readlines()

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

    plate = line2_str['annotation']['classifications'][0]['value']
    if plate is None:
        plate = ''
    attribute = line2_str['annotation']['classifications'][1]['value']
    clarity = line2_str['annotation']['classifications'][2]['value']
    if line2_str['annotation']['classifications'][-1]['value']:
        continue
    l_json = {"url": url,
              "type": "image",
              "label": [{"data": [{"class": [plate, attribute, clarity]}],
                         "name": "general", "type": "ocr"}],
              "test_tags": [type, light, difficulty]}
    w.write(json.dumps(l_json, ensure_ascii=False) + '\n')




