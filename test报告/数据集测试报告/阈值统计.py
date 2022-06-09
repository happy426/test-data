import json
import pandas as pd

datas = []

# f = open('/Users/smai/Downloads/危化品and大车.json', 'r', encoding='utf-8')

f = open('/Users/smai/Downloads/运输车.json', 'r', encoding='utf-8')

lines = f.readlines()
for line in lines:
    line_str = json.loads(line)
    photo = line_str['url'].split('/')[-1]
    type_car = line_str['label'][0]['data'][0]['class'][-1]
    score = line_str['label'][0]['data'][0]['scores'][-1]
    if score > 0.7:
        # w.write(json.dumps(line_str, ensure_ascii=False) + '\n')
        datas.append([photo, type_car, score])

data = pd.DataFrame(datas, columns=['type_car', 'score'])
print(data.groupby('type_car').size())
# print(data.to_string())
# data.to_csv('罐车and运输车.csv')


