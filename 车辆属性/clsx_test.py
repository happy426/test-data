import json


f1 = open('data05/测试集-车辆属性-运输车-检测-排序.json', 'r', encoding='utf-8')
f2 = open('data05/TASK_测试集-车辆属性-运输车-筛选检测_3104.json', 'r', encoding='utf-8')
w = open('data05/测试集-车辆属性-运输车-检测发标.json', 'w', encoding='utf-8')

lines1 = f1.readlines()
lines2 = f2.readlines()

for i in range(len(lines1)):
    line1_str = json.loads(lines1[i])
    line2_str = json.loads(lines2[i])
    url = line1_str['url']
    url2 = line2_str['url']
    if url2 != url:
        continue
    if len(line2_str['annotation']['classifications']) == 0:
        continue
    if line2_str['annotation']['classifications'][0]['value'] == 'yes':
        w.write(json.dumps(line1_str, ensure_ascii=False) + '\n')
