import json
import pandas as pd

# 按照attribute统计。plate, attribute, clarity

datas = []
with open('/Users/smai/Desktop/work/车牌识别/测试集-车牌识别v4-通用ms.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_str = json.loads(line)
        plate = line_str['label'][0]['data'][0]['class'][0]
        attribute = line_str['label'][0]['data'][0]['class'][1]
        clarity = line_str['label'][0]['data'][0]['class'][-1]
        datas.append([plate, attribute, clarity])

data = pd.DataFrame(datas, columns=['plate', 'attribute', 'clarity'])
print(data.groupby(['attribute']).size())
print(data.groupby(['attribute']).size().values.sum())
print(data.groupby(['attribute', 'clarity']).size())
print(data.groupby(['clarity']).size())


