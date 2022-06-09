import json
import pandas as pd

# 按照点位统计time,weather,difficulty

datas = []
with open('/Users/smai/Desktop/work/交通检测/测试集-交通检测v4-带场景.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_str = json.loads(line)
        fenlei = line_str['label'][0]['data']
        for i in range(len(fenlei)):
            class_4 = fenlei[i]['class']
            datas.append(class_4)

data = pd.DataFrame(datas, columns=['class'])
print(data.groupby('class').size())

