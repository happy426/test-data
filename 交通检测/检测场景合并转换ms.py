"""
场景标和检测标是一样多的
先把两个数据集合并，再去除无效标签，可以节约脚本执行时间。
"""
import json

f1 = open('./data01/TASK_测试集-交通检测v4-高速场景_3003.json', 'r', encoding='utf-8')
f2 = open('./data01/TASK_测试集-交通检测v4-高速_3004.json', 'r', encoding='utf-8')
w = open('./data01/测试集-交通检测v4-高速ms.json', 'w', encoding='utf-8')

lines1 = f1.readlines()
lines2 = f2.readlines()

for i in range(len(lines1)):
    line1_str = json.loads(lines1[i])
    line2_str = json.loads(lines2[i])
    url = line1_str['url']
    url2 = line2_str['url']
    if url2 != url:
        continue
    time = line1_str['annotation']['classifications'][0]['value']
    weather = line1_str['annotation']['classifications'][1]['value']
    dianwei = line1_str['annotation']['classifications'][2]['value']
    difficulty = ''
    if len(line1_str['annotation']['classifications']) == 4:
        difficulty = line1_str['annotation']['classifications'][3]['value']
        if difficulty:
            difficulty = '难例'
        else:
            difficulty = ''
    l_json = {"url": url, "type": "image", "test_tags": [time, weather, dianwei, difficulty],
              "label": [{"name": "general", "type": "detection", "version": "1",
                         "data": []}]}
    for obj in line2_str['annotation']['detections']:
        xmin = obj['value']['x'] if obj['value']['x'] > 0 else 0
        ymin = obj['value']['y'] if obj['value']['y'] > 0 else 0
        xmax = obj['value']['x'] + obj['value']['width']
        xmax = xmax if xmax < line2_str['meta']['width'] else line2_str['meta']['width']
        ymax = obj['value']['y'] + obj['value']['height']
        ymax = ymax if ymax < line2_str['meta']['height'] else line2_str['meta']['height']

        new_obj = {
            # "scores": [1],
            # "class": ['plate'],
            "bbox": [[xmin, ymin], [xmax, ymin], [xmax, ymax], [xmin, ymax]],
            "class": [obj['key']]
        }
        l_json['label'][0]['data'].append(new_obj)
    data = l_json['label'][0]['data']
    # 去除空的
    if len(data) != 0:
        w.write(json.dumps(l_json, ensure_ascii=False) + '\n')
