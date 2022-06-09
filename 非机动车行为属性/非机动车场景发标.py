import json

f = open('./data06/url01.json', 'r', encoding='utf-8')
w = open('./data06/测试集-非机动车行为属性-上海-场景.json', 'w', encoding='utf-8')

r_lines = f.readlines()
for line in r_lines:
    line_dict = json.loads(line)
    url = line_dict

    # 检测
    l_json = {"url": url, "mime": 0, "meta": {},
              "annotation": {"detections": [], "classifications": [{'key': 'light', 'value': '白天'},
                                                                   {'key': 'weather', 'value': '晴天'}]},
              "version": "2.0.0"}
    line_str_target = json.dumps(l_json, ensure_ascii=False)
    w.write(line_str_target+'\n')
