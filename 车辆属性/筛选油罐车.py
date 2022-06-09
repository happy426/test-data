import json

w = open('data05/测试集-车辆属性-v3再处理-发标.json', 'w', encoding='utf-8')
with open('data05/测试集-车辆属性-场景-v3.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_str = json.loads(line)
        type_car = line_str['label'][0]['data'][0]['class'][-1]
        url = line_str['url']
        direction = line_str['label'][0]['data'][0]['class'][0]
        type = line_str['label'][0]['data'][0]['class'][1]
        weather = line_str['test_tags'][0]
        difficulty = line_str['test_tags'][1]
        """
        {"key": "direction", "value": direction},
                                                         {"key": "type", "value": type},
                                                         {"key": "type2", "value": type_car}
        """
        # 筛选出有空值的数据
        if direction == "" and type != "" and type_car != "":
            l_json = {"url": url, "mime": 0, "meta": {},
                      "annotation": {"detections": [],
                                     "classifications": [{"key": "type", "value": type},
                                                         {"key": "type2", "value": type_car}]},
                      "test_tags": [weather, difficulty],
                      "version": "2.0.0"}
            line_str_target = json.dumps(l_json, ensure_ascii=False)
            w.write(line_str_target + '\n')

        if direction != "" and type == "" and type_car != "":
            l_json = {"url": url, "mime": 0, "meta": {},
                      "annotation": {"detections": [],
                                     "classifications": [{"key": "direction", "value": direction},
                                                         {"key": "type2", "value": type_car}]},
                      "test_tags": [weather, difficulty],
                      "version": "2.0.0"}
            line_str_target = json.dumps(l_json, ensure_ascii=False)
            w.write(line_str_target + '\n')

        if direction != "" and type != "" and type_car == "":
            l_json = {"url": url, "mime": 0, "meta": {},
                      "annotation": {"detections": [],
                                     "classifications": [{"key": "direction", "value": direction},
                                                         {"key": "type", "value": type}]},
                      "test_tags": [weather, difficulty],
                      "version": "2.0.0"}
            line_str_target = json.dumps(l_json, ensure_ascii=False)
            w.write(line_str_target + '\n')

        if direction == "" and type == "" and type_car != "":
            l_json = {"url": url, "mime": 0, "meta": {},
                      "annotation": {"detections": [],
                                     "classifications": [{"key": "type2", "value": type_car}]},
                      "test_tags": [weather, difficulty],
                      "version": "2.0.0"}
            line_str_target = json.dumps(l_json, ensure_ascii=False)
            w.write(line_str_target + '\n')

        if direction != "" and type == "" and type_car == "":
            l_json = {"url": url, "mime": 0, "meta": {},
                      "annotation": {"detections": [],
                                     "classifications": [{"key": "direction", "value": direction}]},
                      "test_tags": [weather, difficulty],
                      "version": "2.0.0"}
            line_str_target = json.dumps(l_json, ensure_ascii=False)
            w.write(line_str_target + '\n')

        if direction == "" and type != "" and type_car == "":
            l_json = {"url": url, "mime": 0, "meta": {},
                      "annotation": {"detections": [],
                                     "classifications": [{"key": "type", "value": type}]},
                      "test_tags": [weather, difficulty],
                      "version": "2.0.0"}
            line_str_target = json.dumps(l_json, ensure_ascii=False)
            w.write(line_str_target + '\n')

        if direction == "" and type == "" and type_car == "":
            l_json = {"url": url, "mime": 0, "meta": {},
                      "annotation": {"detections": [],
                                     "classifications": []},
                      "test_tags": [weather, difficulty],
                      "version": "2.0.0"}
            line_str_target = json.dumps(l_json, ensure_ascii=False)
            w.write(line_str_target + '\n')
        # # 过滤出有空值的数据
        # if direction == "" or type == "" or type_car == "":
        #     continue
        # line_str_target = json.dumps(line_str, ensure_ascii=False)
        # w.write(line_str_target + '\n')


