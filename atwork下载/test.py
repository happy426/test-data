import json
import requests


f1 = open('data/metal-export-20220511150354的副本.json', 'r', encoding='utf-8')
lines = f1.readlines()
for line in lines:
    line_str = json.loads(line)
    url = line_str['url']
    name = url.split('/')[-1].split('?')[0]
    # 过滤已抠图的
    # if 'feature.jpg' not in url and name not in photo_names and name2 not in names2:
    # 不过滤已经抠图的
    if 'feature.jpg' not in url and '.mp4' in url:
        video = requests.get(url)
        with open(f'/Users/smai/Desktop/plate/双层托运板车/未抠图视频2/{name}', 'wb') as f:
            f.write(video.content)
        print(name)
f1.close()
