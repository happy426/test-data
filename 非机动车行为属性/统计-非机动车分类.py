import json
import pandas as pd

# 按照点位统计time,weather,difficulty

datas = []
with open('/Users/smai/Desktop/work/非机动车行为属性/测试集-非机动车行为属性-v4-带场景.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_str = json.loads(line)
        type = line_str['label'][0]['data'][0]['class'][0]
        helmet = line_str['label'][0]['data'][0]['class'][1]
        manned = line_str['label'][0]['data'][0]['class'][2]
        ride = line_str['label'][0]['data'][0]['class'][3]
        waimai = line_str['label'][0]['data'][0]['class'][4]
        datas.append([type, helmet, manned, ride, waimai])

data = pd.DataFrame(datas, columns=['type', 'helmet', 'manned', 'ride', 'waimai'])
columns = list(data.columns.values)
# print(columns)
for i in columns:
    print(data.groupby(i)[i].count())


