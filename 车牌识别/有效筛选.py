import json

f1 = open('/Users/smai/Desktop/work/车牌识别/TASK_测试集-车牌识别v3-筛选_3053.json', 'r', encoding='utf-8')
f2 = open('/Users/smai/Desktop/work/车牌识别/测试集-车牌识别-场景_已拼接.json', 'r', encoding='utf-8')
w = open('/Users/smai/Desktop/work/车牌识别/测试集-车牌识别v3-修正.json', 'w', encoding='utf-8')

lines1 = f1.readlines()
lines2 = f2.readlines()

for i in range(len(lines1)):
    line1_str = json.loads(lines1[i])
    line2_str = json.loads(lines2[i])
    url = line1_str['url']
    url2 = line2_str['url']
    if url != url2:
        continue
    if line1_str['annotation']['classifications'][0]['value'] == '无效':
        continue
    w.write(json.dumps(line2_str, ensure_ascii=False) + '\n')


