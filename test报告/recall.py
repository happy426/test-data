import numpy as np
import matplotlib.pyplot as plt

# 阈值
Threshold = np.linspace(0, 1, 21)
# 模型得分
test_data_score = [[0.8, 0.1, 0.1],
                   [0.1, 0.8, 0.1],
                   [0.1, 0.1, 0.8],
                   [0.41, 0.3, 0.29],
                   [0.29, 0.41, 0.3],
                   [0.29, 0.3, 0.41],
                   [0.34, 0.36, 0.4],
                   [0.4, 0.36, 0.34],
                   [0.36, 0.4, 0.34]]
# 真实值
GT = ['白天车', '晚上车', '负样本', '白天车', '晚上车', '负样本', '白天车', '晚上车', '负样本']
ts = []
pres = []
recalls = []
for t in Threshold:
    t = round(t, 2)
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    ts.append(t)
    for i in range(len(test_data_score)):
        if max(test_data_score[i][0], test_data_score[i][1]) > t and GT[i] in ('白天车', '晚上车'):
            TP += 1
        elif max(test_data_score[i][0], test_data_score[i][1]) > t and GT[i] not in ('白天车', '晚上车'):
            FP += 1
        elif max(test_data_score[i][0], test_data_score[i][1]) < t and GT[i] in ('白天车', '晚上车'):
            FN += 1
        elif max(test_data_score[i][0], test_data_score[i][1]) < t and GT[i] not in ('白天车', '晚上车'):
            TN += 1
        if FP == 0:
            pre = 1
        else:
            pre = TP / (TP + FP)
        if (TP + FN) == 0:
            recall = 0
        else:
            recall = TP / (TP + FN)
    print(f'Threshold = {t}时：TP={TP},FP={FP},FN={FN},TN={TN},pre={pre}, recall = {recall}')

    pres.append(pre)
    recalls.append(recall)

# p_pre = plt.plot(ts, pres, label='pre')
# p_recall = plt.plot(ts, recalls, label='recall')
# plt.legend()
# plt.show()

