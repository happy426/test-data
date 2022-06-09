import json
import pandas as pd


datas = []
f_r = open('../data/v1.3.5推理结果.json', 'r', encoding='utf-8')
f = open('../data/测试集-车辆属性-场景-v3.5-无运输车.json', 'r', encoding='utf-8')

# f_r = open('/Users/smai/Downloads/危化品and大车.json', 'r', encoding='utf-8')
# f = open('/Users/smai/PycharmProjects/test_data/车辆属性/data05/测试集-车辆属性-危化品and其他货车.json', 'r', encoding='utf-8')

lines_r = f_r.readlines()
lines = f.readlines()
for i in range(len(lines_r)):
    line_r_str = json.loads(lines_r[i])
    line_str = json.loads((lines[i]))
    photo = line_str['url'].split('/')[-1]
    direction = line_str['label'][0]['data'][0]['class'][1]
    direction_r = line_r_str['label'][0]['data'][0]['class'][1]
    score = line_r_str['label'][0]['data'][0]['scores'][1]
    if direction == "":
        continue
    if score >= 0.7:
        datas.append([photo, direction, direction_r, 'yes'])
    else:
        datas.append([photo, direction, direction_r, 'no'])

data = pd.DataFrame(datas, columns=['photo', '人工标注', '机器识别', 'score'])
data_tj = data.groupby(by=['人工标注', '机器识别', 'score']).size()
# print(data_tj.to_string())
data_tj.to_csv('./data/v1.3.5统计-8分类.csv')


