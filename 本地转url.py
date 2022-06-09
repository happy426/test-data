import json
import os

w = open('./车辆属性/data05/url03.json', 'w', encoding='utf-8')
photos = []
path = r'/Users/smai/Desktop/plate/clsx-kt3/car/'
dir1s = os.listdir(path)

# # 两层目录
# for dir1 in dir1s:
#     if dir1 != '.DS_Store':
#         path2 = path + '/' + dir1
#         dir2s = os.listdir(path2)
#         for dir2 in dir2s:
#             if dir2 != '.DS_Store':
#                 path3 = path2 + '/' + dir2
#                 photo = os.listdir(path3)
#                 for i in photo:
#                     if i != '.DS_Store':
#                         url_dict = 'ks:///personal/QA/test/交通检测/v4' + '/' + dir1 + '/' + dir2 + '/' + i
#                         url_str = json.dumps(url_dict, ensure_ascii=False)
#                         w.write(url_str + '\n')

# # 一层目录
# for dir1 in dir1s:
#     if dir1 != '.DS_Store':
#         path2 = path + '/' + dir1
#         photo = os.listdir(path2)
#         for i in photo:
#             if i != '.DS_Store':
#                 url_dict = 'ks:///personal/QA/test/车牌检测/v4/' + dir1 + '/' + i
#                 url_str = json.dumps(url_dict, ensure_ascii=False)
#                 w.write(url_str + '\n')
# 无目录
for dir1 in dir1s:
    if dir1 != '.DS_Store':
        url_dict = 'ks:///personal/QA/test/车辆属性/hyx/v4/' + dir1
        url_str = json.dumps(url_dict, ensure_ascii=False)
        w.write(url_str + '\n')



