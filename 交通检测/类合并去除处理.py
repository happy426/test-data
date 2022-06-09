import json

f = open('data01/测试集-交通检测v4-高速收费站广场ms.json', 'r', encoding='utf-8')
w = open('data01/测试集-交通检测v4-高速收费站广场ms-修改.json', 'w', encoding='utf-8')

lines = f.readlines()
for line in lines:
    line_str = json.loads(line)
    data = line_str['label'][0]['data']
    if len(data) == 0:
        continue
    for i in range(len(data)):
        if data[i]['class'] == ['suspect-vehicle']:
            continue
    for j in range(len(data)):
        if data[j]['class'] == ['person-onmotor']:
            line_str['label'][0]['data'][j]['class'] = ['person']
        elif data[j]['class'] == ['motorcycle']:
            line_str['label'][0]['data'][j]['class'] = ['non-motor']
    w.write(json.dumps(line_str, ensure_ascii=False) + '\n')


