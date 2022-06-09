import json

f = open('/Users/smai/Desktop/work/非机动车行为属性/测试集-非机动车行为属性-v4-带场景.json', 'r', encoding='utf-8')
w1 = open('result/测试集-非机动车行为属性v4-再处理-车型.json', 'w', encoding='utf-8')
w2 = open('result/测试集-非机动车行为属性v4-再处理-头盔.json', 'w', encoding='utf-8')
w3 = open('result/测试集-非机动车行为属性v4-再处理-载人.json', 'w', encoding='utf-8')
w4 = open('result/测试集-非机动车行为属性v4-再处理-骑行.json', 'w', encoding='utf-8')
w5 = open('result/测试集-非机动车行为属性v4-再处理-外卖.json', 'w', encoding='utf-8')

r_lines = f.readlines()
for line in r_lines:
    line_str = json.loads(line)
    url = line_str['url']
    type = line_str['label'][0]['data'][0]['class'][0]
    helmet = line_str['label'][0]['data'][0]['class'][1]
    manned = line_str['label'][0]['data'][0]['class'][2]
    ride = line_str['label'][0]['data'][0]['class'][3]
    waimai = line_str['label'][0]['data'][0]['class'][4]
    if type == '':
        l_json = {"url": url, "mime": 0, "meta": {},
                  "annotation": {"detections": [], "classifications": [{'key': 'type', 'value': 'e-bike'}]},
                  "version": "2.0.0"}
        line_str_target = json.dumps(l_json, ensure_ascii=False)
        w1.write(line_str_target+'\n')

    if helmet == '':
        l_json = {"url": url, "mime": 0, "meta": {},
                  "annotation": {"detections": [], "classifications": [{'key': 'helmet', 'value': 'helmet'}]},
                  "version": "2.0.0"}
        line_str_target = json.dumps(l_json, ensure_ascii=False)
        w2.write(line_str_target+'\n')

    if manned == '':
        l_json = {"url": url, "mime": 0, "meta": {},
                  "annotation": {"detections": [], "classifications": [{'key': 'manned', 'value': 'no-manned'}]},
                  "version": "2.0.0"}
        line_str_target = json.dumps(l_json, ensure_ascii=False)
        w3.write(line_str_target+'\n')

    if ride == '':
        l_json = {"url": url, "mime": 0, "meta": {},
                  "annotation": {"detections": [], "classifications": [{'key': 'ride', 'value': 'riding'}]},
                  "version": "2.0.0"}
        line_str_target = json.dumps(l_json, ensure_ascii=False)
        w4.write(line_str_target+'\n')

    if waimai == '':
        l_json = {"url": url, "mime": 0, "meta": {},
                  "annotation": {"detections": [], "classifications": [{'key': 'waimai', 'value': 'other'}]},
                  "version": "2.0.0"}
        line_str_target = json.dumps(l_json, ensure_ascii=False)
        w5.write(line_str_target+'\n')
