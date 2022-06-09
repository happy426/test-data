import json
import pandas as pd


# 按照点位统计time,weather,difficulty
def tongji(classify):
    datas = []
    with open('/Users/smai/Desktop/work/交通检测/测试集-交通检测v4-带场景.json', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line_str = json.loads(line)
            dianwei = line_str['test_tags'][-2]
            if dianwei == '隧道点位':
                time = line_str['test_tags'][0]
                weather = 0
                difficulty = line_str['test_tags'][-1]
                if difficulty == '':
                    difficulty = '非难例'
                datas.append([time, weather, dianwei, difficulty])
            else:
                time = line_str['test_tags'][0]
                weather = line_str['test_tags'][1]
                difficulty = line_str['test_tags'][-1]
                if difficulty == '':
                    difficulty = '非难例'
                datas.append([time, weather, dianwei, difficulty])

    data = pd.DataFrame(datas, columns=['time', 'weather', 'dianwei', 'difficulty'])
    # print(data.to_string())

    data_tj = data.groupby(by=['dianwei', classify]).size()

    # print(data.groupby(by=['dianwei', 'weather']).size().to_string())
    # print(data.groupby(by=['dianwei', 'difficulty']).size().to_string())
    columns_names = data_tj.index.names
    result = [1 for n in range(len(columns_names)+1)]
    for i in range(len(columns_names)):
        result[i] = data_tj.index.get_level_values(columns_names[i]).values
    result[-1] = data_tj.values
    result_pd = pd.DataFrame(result)
    result_T = pd.DataFrame(result_pd.values.T, index=result_pd.columns, columns=['dianwei', classify, 'num'])
    # print(result_T.to_string())

    pd_data = result_T
    names = ['高速-普通点位', '高速-龙门架卡口', '高速-收费站卡口', '高速-收费站广场', '高速-枪机（中间绿化）', '高速-枪机（边上）',
             '高速-隧道枪机', '高速-球机', '高速-高点位', '高速-桥上', '城市-普通点位', '城市-十字路口', '城市-T字路口', '城市-市内卡口',
             '城市-X字路口', '城市-单向路口', '城市-市内高架', '城市-市内桥梁', '城市-快速路', '城市-高点位', '城市-鹰眼', '隧道点位', '乡道', '国道', '省道']
    datas = []
    for name in names:
        for i in range(len(pd_data)):
            if pd_data.loc[i][0] == name:
                datas.append([name, pd_data.loc[i][1], pd_data.loc[i][2]])

    data = pd.DataFrame(datas)
    return data
    # 转置
    # data_T = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
    # print(data_T.to_string())


if __name__ == '__main__':
    # 按照点位统计time,weather,difficulty
    tag = 'time'
    data = tongji(tag)
    print(data.to_string())
    # data.to_csv('./result/time.csv')
