import json
import requests

f1 = open('data/metal-export-20220511162539.json', 'r', encoding='utf-8')
lines = f1.readlines()
photo_names = []
names2 = []
for line in lines:
    line_str = json.loads(line)
    url = line_str['url']
    name = url.split('/')[-1].split('?')[0]
    name2 = url.split('/')[-2]
    if 'feature.jpg' in url:
        photo_name = name.replace('_feature', '')
        photo_names.append(photo_name)
        photo = requests.get(url)
        with open(f'/Users/smai/Desktop/plate/双层托运板车/已抠图/{name}', 'wb') as f:
            f.write(photo.content)
        print(name)
f1.close()

f1 = open('data/metal-export-20220511162539.json', 'r', encoding='utf-8')
lines = f1.readlines()
for line in lines:
    line_str = json.loads(line)
    url = line_str['url']
    name = url.split('/')[-1].split('?')[0]
    name2 = url.split('/')[-2]
    # 过滤已抠图的
    # if 'feature.jpg' not in url and name not in photo_names and name2 not in names2:
    # 不过滤已经抠图的
    if 'feature.jpg' not in url and 'jpg' in url:
        photo = requests.get(url)
        names2.append(name2)
        with open(f'/Users/smai/Desktop/plate/双层托运板车/未抠图/{name}', 'wb') as f:
            f.write(photo.content)
        print(name)
f1.close()

f1 = open('data/metal-export-20220511162539.json', 'r', encoding='utf-8')
lines = f1.readlines()
for line in lines:
    line_str = json.loads(line)
    url = line_str['url']
    name = url.split('/')[-1].split('?')[0]
    name2 = url.split('/')[-2]
    # 过滤已抠图的
    # if 'feature.jpg' not in url and name not in photo_names and name2 not in names2:
    # 不过滤已经抠图的,过滤截帧的
    if 'feature.jpg' not in url and '.mp4' in url and name2 not in names2:
        video = requests.get(url)
        with open(f'/Users/smai/Desktop/plate/双层托运板车/未抠图视频/{name}', 'wb') as f:
            f.write(video.content)
        print(name)
f1.close()
