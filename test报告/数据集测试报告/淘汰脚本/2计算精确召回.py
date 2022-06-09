import pandas as pd

pd_data = pd.read_csv('../data/v1.3.5统计结果.csv')
# names = pd_data['人工标注'].unique().tolist()
# print(names)
# 方向
# names = ['front', 'rear', 'no_direction']
# 8分类
# names = ['car', 'pick-up', 'light-bus', 'bus', 'light-truck', 'mid-truck', 'heavy-truck', 'van-truck']
# 17分类：
names = ['taxi', 'police-car', 'engineering-truck', 'emergency-car', 'ambulance', 'fire-truck', 'garbage-truck', 'sweeper-truck', 'watering-truck', 'cementmix-truck', 'cash-truck', 'muck-truck', 'tank-truck', 'bus', 'transport_truck', 'no-sp-car', 'no-sp-truck', 'other']
datas = []
for name in names:
    pre = 0
    recall = 0
    tp = 0
    fp = 0
    fn = 0
    for i in range(len(pd_data)):
        if pd_data.loc[i][0] == name:
            if pd_data.loc[i][0] == pd_data.loc[i][1] and pd_data.loc[i][2] == 'yes':
                tp = pd_data.loc[i][3]
            if pd_data.loc[i][0] != pd_data.loc[i][1] and pd_data.loc[i][2] == 'yes':
                fp = fp + pd_data.loc[i][3]
            if pd_data.loc[i][2] == 'no':
                fn = fn + pd_data.loc[i][3]
    if tp != 0:
        pre = tp / (tp + fp)
        recall = tp / (tp + fp + fn)
    datas.append([name, round(pre, 4), round(recall, 4), tp + fp + fn])
data = pd.DataFrame(datas, columns=['name', 'pre', 'recall', 'num'])
# 转置
data_T = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
print(data_T.to_string())
# data_T.to_csv('./data/v1.3.5精准召回.csv')

