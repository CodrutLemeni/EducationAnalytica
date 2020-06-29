import numpy as np
import matplotlib.pyplot as plt
import json
import os

def make_line_graph_js(all_categories, OYName, title, current_export_path, years):
    current_export_path = os.path.join(current_export_path, title)

    meta = {}
    dataDict = {}
    dataDict["series_list"] = []
    
    
    meta["type"] = "LINE_GRAPH"
    meta["title"] = title
    meta["xAxisName"] = "An"
    meta["yAxisName"] = OYName
    dataDict["meta"] = meta
    
    crt_series_with_name = {}
    crt_series = []
    crt_series_with_name["name"] = title

    for j in range(len(all_categories)):
        crt_elem = {}
        crt_elem["key"] = years[j]
        crt_elem["value"] = all_categories[j]
        crt_series.append(crt_elem)

    crt_series_with_name["series"] = crt_series
    dataDict["series_list"].append(crt_series_with_name)

    f = open(current_export_path + ".txt", "w+")
    jsonDict = json.dumps(dataDict)
    f.write(jsonDict)