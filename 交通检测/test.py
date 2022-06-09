import json


# with open('/Users/smai/Downloads/TASK_测试集-交通检测v4-高速收费站广场-检测_3024.json', 'r', encoding='utf-8') as f:
f = open('/Users/smai/Downloads/TASK_测试集-交通检测v4-高速收费站广场-检测_3024.json', 'r', encoding='utf-8')
w = open('result/测试集-交通检测v4-高速收费站广场labelx.json', 'w', encoding='utf-8')

lines = f.readlines()
for line in lines:
    line_str = json.loads(line)
    data = line_str['annotation']['detections']
    if len(data) == 0:
        continue
    for i in range(len(data)):
        if data[i]['key'] == ['suspect-vehicle']:
            continue
    for j in range(len(data)):
        if data[j]['key'] == ['person-onmotor']:
            line_str['annotation']['detections'][j]['key'] = ['person']
        elif data[j]['key'] == ['motorcycle']:
            line_str['annotation']['detections'][j]['key'] = ['non-motor']
    w.write(json.dumps(line_str, ensure_ascii=False) + '\n')