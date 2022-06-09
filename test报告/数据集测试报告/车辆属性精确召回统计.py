import json
import pandas as pd
import os


def tong_ji(result_path, data_path, classify, threshold, csv_name):
    f_r = open(result_path, 'r', encoding='utf-8')
    f = open(data_path, 'r', encoding='utf-8')

    lines_r = f_r.readlines()
    lines = f.readlines()
    datas = []
    for i in range(len(lines_r)):
        line_r_str = json.loads(lines_r[i])
        line_str = json.loads((lines[i]))
        photo = line_str['url'].split('/')[-1]
        classify_data = line_str['label'][0]['data'][0]['class'][classify]
        classify_r = line_r_str['label'][0]['data'][0]['class'][classify]
        score = line_r_str['label'][0]['data'][0]['scores'][classify]
        if classify_data == "":
            continue
        if score >= threshold:
            datas.append([photo, classify_data, classify_r, 'yes'])
        else:
            datas.append([photo, classify_data, classify_r, 'no'])
    data = pd.DataFrame(datas, columns=['photo', '人工标注', '机器识别', 'score'])
    data_tj = data.groupby(by=['人工标注', '机器识别', 'score']).size()

    columns_names = data_tj.index.names
    result = [1 for n in range(len(columns_names)+1)]
    for i in range(len(columns_names)):
        result[i] = data_tj.index.get_level_values(columns_names[i]).values
    result[-1] = data_tj.values
    result_pd = pd.DataFrame(result)
    result_T = pd.DataFrame(result_pd.values.T, index=result_pd.columns, columns=['人工标注', '机器识别', 'score', 'sum'])
    # print(result_T)

    pd_data = result_T
    # names = pd_data['人工标注'].unique().tolist()
    # print(names)
    if classify == 0:
        # 方向
        names = ['front', 'rear', 'no_direction']
    elif classify == 1:
        # 8分类
        names = ['car', 'pick-up', 'light-bus', 'bus', 'light-truck', 'mid-truck', 'heavy-truck', 'van-truck']
    elif classify == 2:
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
    # data_T.to_csv(f'./result/{csv_name}+{zhonglei}.csv')


if __name__ == '__main__':
    """
    车辆属性统计pre和recall阈值
    输入ms推理结果路径、数据集路径、分类、阈值
    种类0代表方向；1代表车型分类；2代表特种车辆分类
    """
    tuilijieguo_path = './data/v1.5.0推理结果.json'
    shujuji_path = './data/测试集-车辆属性-场景-v3.5-有运输车.json'
    zhonglei = int(input('请输入0,1,2:'))
    if zhonglei not in (0, 1, 2):
        print('请输入0到2的整数！')
        os.kill()
    yuzhi = 0.7
    # input('将上面的结果放到result文件夹下，起个名字吧（输入版本号）：')
    csv = 'v1.5.0'
    tong_ji(tuilijieguo_path, shujuji_path, zhonglei, yuzhi, csv)
