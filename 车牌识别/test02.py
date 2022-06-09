import json
import os

path = r'/Users/smai/Desktop/plate/v4plate/'
dir1s = os.listdir(path)
photos = []
# 一层目录
for dir1 in dir1s:
    if dir1 != '.DS_Store':
        path2 = path + dir1
        photo = os.listdir(path2)
        for i in photo:
            if i != '.DS_Store':
                photos.append(i)
print(len(photos))
f1 = open('./data04/测试集-车牌识别v4_已拼接-修正.json', 'r', encoding='utf-8')
# w = open('./data04/测试集-车牌识别v4-修正.json', 'w', encoding='utf-8')

lines = f1.readlines()
urls = []
for line in lines:
    line_str = json.loads(line)
    url_photo = line_str['url'].split('/')[-1].split('_0.jpg')[0] + '.jpg'
    # line_str['url'] = 'ks:///personal/QA/test/车牌识别/' + url_photo
    if url_photo in photos:
        urls.append(url_photo)
    else:
        print(line_str)
        # url_str = json.dumps(line_str, ensure_ascii=False)
        # w.write(url_str + '\n')
print(len(urls))
f1.close()

