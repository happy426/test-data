"""
场景标和检测标是一样多的
先把两个数据集合并，再去除无效标签，可以节约脚本执行时间。
"""
import json

f1 = open('./data05/TASK_测试集-车辆属性-油罐车-细分类_3111.json', 'r', encoding='utf-8')
# f2 = open('./data01/TASK_测试集-交通检测v4-高速_3004.json', 'r', encoding='utf-8')
w = open('./data05/测试集-车辆属性-危化品ms.json', 'w', encoding='utf-8')

lines1 = f1.readlines()
# lines2 = f2.readlines()

for i in range(len(lines1)):
    line1_str = json.loads(lines1[i])
    # line2_str = json.loads(lines2[i])
    url = line1_str['url']
    # url2 = line2_str['url']
    # if url2 != url:
    #     continue
    # time = line1_str['annotation']['classifications'][0]['value']
    # weather = line1_str['annotation']['classifications'][1]['value']
    # dianwei = line1_str['annotation']['classifications'][2]['value']
    # difficulty = ''
    if len(line1_str['annotation']['classifications']) == 4:
        invalid = line1_str['annotation']['classifications'][3]['value']
        if invalid:
            continue
    direction = line1_str['annotation']['classifications'][0]['value']
    type1 = line1_str['annotation']['classifications'][1]['value']
    type2 = line1_str['annotation']['classifications'][2]['value']
    l_json = {"url": url, "type": "image",
              "label": [{"name": "general", "type": "classification", "version": "1",
                         "data": [{"class": [direction, type1, type2]}]}]}
    data = l_json['label'][0]['data']
    # 去除空的
    if len(data) != 0:
        w.write(json.dumps(l_json, ensure_ascii=False) + '\n')







