import pandas as pd

pd_data = pd.read_csv('../data/v1.3.5统计-方向.csv')
names = pd_data['人工标注'].unique().tolist()
datas = []
for name in names:
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
print(data.to_string())
# data.to_csv('./data/v1.3.5精准召回-方向.csv')

