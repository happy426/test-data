import json
import pandas as pd

# 按照点位统计time,weather,difficulty

datas = []
with open('/Users/smai/Desktop/work/交通检测/测试集-交通检测v4-带场景.json', 'r', encoding='utf-8') as f2:
    lines2 = f2.readlines()
    for line2 in lines2:
        line2_str = json.loads(line2)
        dianwei = line2_str['test_tags'][2]
        time = line2_str['test_tags'][0]
        weather = line2_str['test_tags'][1]
        if len(line2_str['test_tags']) != 4:
            print(line2_str['test_tags'])
            continue
        difficulty = line2_str['test_tags'][3]
        if difficulty == '':
            difficulty = '非难例'
        datas.append([dianwei, time, weather, difficulty])

data = pd.DataFrame(datas, columns=['dianwei', 'time', 'weather', 'difficulty'])
print(data.groupby(by=['dianwei', 'time']).size())


