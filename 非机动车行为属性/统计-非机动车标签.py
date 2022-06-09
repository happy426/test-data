import json
import pandas as pd

# 按照点位统计time,weather,difficulty

datas = []
with open('/Users/smai/Desktop/work/非机动车行为属性/测试集-非机动车行为属性-v4-带场景.json', 'r', encoding='utf-8') as f2:
    lines2 = f2.readlines()
    for line2 in lines2:
        line2_str = json.loads(line2)
        light = line2_str['test_tags'][0]
        weather = line2_str['test_tags'][1]

        if len(line2_str['test_tags']) != 3:
            print(line2_str['test_tags'])
            continue

        difficulty = line2_str['test_tags'][-1]
        if difficulty == '':
            difficulty = '非难例'
        datas.append([light, weather, difficulty])

data = pd.DataFrame(datas, columns=['light', 'weather', 'difficulty'])
columns = list(data.columns.values)
# print(columns)
for i in columns:
    print(data.groupby(i)[i].count())


