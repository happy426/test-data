import json
import pandas as pd


datas = []
f_r = open('/Users/smai/Downloads/运输车.json', 'r', encoding='utf-8')
f = open('/Users/smai/PycharmProjects/test_data/车辆属性/data05/测试集-车辆属性-危化品and其他货车and运输车.json', 'r', encoding='utf-8')

# f_r = open('/Users/smai/Downloads/危化品and大车.json', 'r', encoding='utf-8')
# f = open('/Users/smai/PycharmProjects/test_data/车辆属性/data05/测试集-车辆属性-危化品and其他货车.json', 'r', encoding='utf-8')

lines_r = f_r.readlines()
lines = f.readlines()
for i in range(len(lines_r)):
    line_r_str = json.loads(lines_r[i])
    line_str = json.loads((lines[i]))
    photo = line_str['url'].split('/')[-1]
    type_true = line_str['label'][0]['data'][0]['class'][-1]
    type_r = line_r_str['label'][0]['data'][0]['class'][-1]
    score = line_r_str['label'][0]['data'][0]['scores'][-1]
    if score >= 0.7:
        # w.write(json.dumps(line_str, ensure_ascii=False) + '\n')
        datas.append([photo, type_true, type_r])


data = pd.DataFrame(datas, columns=['photo', '人工标注', '机器识别'])
# print(data.groupby('人工标注').size())
# print(data.groupby('机器识别').size())
# print(data.to_string())
# data.to_csv('v1.4.1危化品and大车and运输车.csv')
data_tj = data.groupby(by=['人工标注', '机器识别']).size()
print(data_tj.to_string())
# data_tj.to_csv('v1.5.0统计.csv')
