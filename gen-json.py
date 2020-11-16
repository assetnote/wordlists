#!/usr/bin/python
import os, argparse, json, time, sys
from datetime import datetime
from collections import OrderedDict

now = datetime.now()
directory = sys.argv[1]
filelist = os.listdir(directory)

def sizeof_fmt(num, suffix='b'):
    for unit in ['','k','m','g','t','p','e','z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def modification_date(filename):
    t = os.path.getmtime(filename)
    return t

files_json = {"data":[]}

for item in filelist:
	full_path = "{}/{}".format(directory, item)
	num_lines = sum(1 for line in open(full_path))
	file_size = sizeof_fmt(os.path.getsize(full_path))
	modification_time = modification_date(full_path)
	obj = OrderedDict([("Filename", item), ("Line Count", num_lines), ("File Size", file_size), ("Date", modification_time), ("Download", "<a href='{0}{1}'>Download</a>".format(directory, item))])
	files_json["data"].append(obj)

print(json.dumps(files_json,indent=4,ensure_ascii=False))