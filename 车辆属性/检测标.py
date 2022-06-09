import json

f = open('/Users/smai/Desktop/work/车辆属性/测试集-车辆属性-场景-v3.5补标.json', 'r', encoding='utf-8')
w = open('./result/测试集-车辆属性v3.5-场景.json', 'w', encoding='utf-8')

r_lines = f.readlines()
for line in r_lines:
    line_dict = json.loads(line)
    url = line_dict['url']
    # 分类   transport_truck 运输车
    l_json = {"url": url, "mime": 0, "meta": {},
              "annotation": {"detections": [], "classifications": [{"key": "light", "value": "白天"}]},
              "version": "2.0.0"}
    # # 检测
    # l_json = {"url": url, "mime": 0, "meta": {},
    #           "annotation": {"detections": [], "classifications": []},
    #           "version": "2.0.0"}
    line_str_target = json.dumps(l_json, ensure_ascii=False)
    w.write(line_str_target+'\n')

