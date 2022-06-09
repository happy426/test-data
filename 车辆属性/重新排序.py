import json
import time

f = open('data05/测试集-车辆属性-运输车-检测.json', 'r', encoding='utf-8')
w = open('data05/测试集-车辆属性-运输车-检测-排序.json', 'w', encoding='utf-8')

lines = f.readlines()
names = []
for line in lines:
    line_str = json.loads(line)
    photo = line_str['url'].split('/')[-1]
    name = photo[0:-8]
    if name not in names:
        names.append(name)
f.close()

f = open('data05/测试集-车辆属性-运输车-检测.json', 'r', encoding='utf-8')

for i in range(len(names)):
    for line in lines:
        line_str = json.loads(line)
        photo = line_str['url'].split('/')[-1]
        name = photo[0:-8]
        if name == names[i]:
            print(photo)
            w.write(json.dumps(line_str, ensure_ascii=False) + '\n')
f.close()

