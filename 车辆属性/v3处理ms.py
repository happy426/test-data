import json

f1 = open('./data05/TASK_测试集-车辆属性-v3再处理-分类_3124.json', 'r', encoding='utf-8')
f2 = open('./data05/测试集-车辆属性-v3再处理-发标.json', 'r', encoding='utf-8')
w = open('./result/测试集-车辆属性-v3再处理ms.json', 'w', encoding='utf-8')

lines1 = f1.readlines()
lines2 = f2.readlines()
for i in range(len(lines1)):
    line1 = json.loads(lines1[i])
    line2 = json.loads(lines2[i])
    url = line1['url']
    tag = line2['test_tags']
    class1 = line1['annotation']['classifications'][0]['key']
    value1 = line1['annotation']['classifications'][0]['value']
    class2 = line1['annotation']['classifications'][1]['key']
    value2 = line1['annotation']['classifications'][1]['value']
    class3 = line1['annotation']['classifications'][2]['key']
    value3 = line1['annotation']['classifications'][2]['value']
    class4 = 0
    value4 = 0
    if len(line1['annotation']['classifications']) == 4:
        class4 = line1['annotation']['classifications'][3]['key']
        value4 = line1['annotation']['classifications'][3]['value']
    if class1 == 'invalid' and value1 == True or class2 == 'invalid' and value2 == True or class3 == 'invalid' and value3 == True or class4 == 'invalid' and value4 == True:
        continue

    if class1 == 'direction':
        direction = value1
    elif class1 == 'type':
        type = value1
    elif class1 == 'type2':
        type2 = value1

    if class2 == 'direction':
        direction = value2
    elif class2 == 'type':
        type = value2
    elif class2 == 'type2':
        type2 = value2

    if class3 == 'direction':
        direction = value3
    elif class3 == 'type':
        type = value3
    elif class3 == 'type2':
        type2 = value3

    if class4 == 'direction':
        direction = value4
    elif class4 == 'type':
        type = value4
    elif class4 == 'type2':
        type2 = value4

    l_json = {"url": url, "type": "image",
              "label": [{"name": "general", "type": "classification", "version": "1",
                         "data": [{"class": [direction, type, type2]}]}],
              "test_tags": tag}
    data = l_json['label'][0]['data']
    # 去除空的
    if len(data) != 0:
        w.write(json.dumps(l_json, ensure_ascii=False) + '\n')