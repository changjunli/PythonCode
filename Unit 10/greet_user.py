import json
"""打开读取json文件并打印读取的数据"""
filename = 'username.json'

with open(filename) as f_obj:
	username = json.load(f_obj)
	print("welcome back, " + username +"!")
