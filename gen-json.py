#!/usr/bin/python
import os, argparse, json, time, sys
from datetime import datetime
from collections import OrderedDict

now = datetime.now()

filelist = os.listdir(sys.argv[1])

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.fromtimestamp(t)

files_json = {"data":[]}

for item in filelist:
	num_lines = sum(1 for line in open(item))
	file_size = sizeof_fmt(os.path.getsize(item))
	modification_time = modification_date(item).strftime("%d/%m/%Y %H:%M:%S")
	obj = OrderedDict([("Filename", item), ("Line Count", num_lines), ("File Size", file_size), ("Date", modification_time), ("Download", "<a href='data/automated/{0}'>Download</a>".format(item))])
	files_json["data"].append(obj)

print(json.dumps(files_json,indent=4,ensure_ascii=False))