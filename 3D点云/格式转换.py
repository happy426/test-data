import json


f = open('./data/3d.json', 'r', encoding='utf-8')
w = open('./data/new3d.json', 'w', encoding='utf-8')
data = f.readlines()
for line in data:
    line_str = json.loads(line)
    url = line_str['url']
    pcd_url = line_str['pcdUrl']
    j_line = {
        "url": url,
        "pcd": {
            "url": pcd_url,
            "params": {}
        },
        "meta": line_str['meta'],
        "mime": 0
    }
    w.write(json.dumps(j_line, ensure_ascii=False)+'\n')


