import json
import pandas as pd

# 按照点位统计time,weather,difficulty

datas = []
with open('/Users/smai/Desktop/work/车牌检测/测试集-车牌检测v4-带场景-已合并.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_str = json.loads(line)
        plate_class = line_str['test_tags'][0]
        light = line_str['test_tags'][1]
        if len(line_str['test_tags']) != 3:
            print(line_str['test_tags'])
            continue
        difficulty = line_str['test_tags'][-1]
        if difficulty == '':
            difficulty = '非难例'
        datas.append([plate_class, light, difficulty])

data = pd.DataFrame(datas, columns=['plate_class', 'light', 'difficulty'])
data_light = data.groupby(by=['plate_class', 'light']).size()
print(data_light)
# data_diff = data.groupby(by=['plate_class', 'light', 'difficulty']).size()
# print(data.groupby(by=['plate_class', 'light', 'difficulty']).size())
# data_diff.to_csv('result/diff.csv')
# data_light.to_csv('result/light.csv')
