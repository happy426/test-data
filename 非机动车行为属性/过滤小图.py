import json
import os

w = open('./data06/url01.json', 'w', encoding='utf-8')
photos = []
path = r'/Users/smai/Desktop/plate/non_motor/car/'
dir1s = os.listdir(path)

for dir1 in dir1s:
    if dir1 != '.DS_Store':
        url_dict = 'ks:///personal/QA/test/非机动车行为属性/上海抠图/' + dir1
        photo = path + dir1
        # size = os.path.getsize(photo)
        # size = size / float(1024)
        # if size >= 2:
        url_str = json.dumps(url_dict, ensure_ascii=False)
        w.write(url_str + '\n')



