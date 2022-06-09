import json
import pandas as pd

# 按照点位统计time,weather,difficulty

datas = []
with open('/Users/smai/Desktop/work/车辆属性/测试集-车辆属性-场景-v3.5-有运输车.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_str = json.loads(line)
        direction = line_str['label'][0]['data'][0]['class'][0]
        type = line_str['label'][0]['data'][0]['class'][1]
        type_car = line_str['label'][0]['data'][0]['class'][-1]
        datas.append([direction, type, type_car])

data = pd.DataFrame(datas, columns=['direction', 'type', 'type_car'])
print(data.groupby('type_car').size())


