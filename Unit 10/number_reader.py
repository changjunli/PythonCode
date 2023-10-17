import json
"""从xxx.json文件中读取数据并打印"""
filename = 'numbers.json'
with open(filename) as f_obj: # 只需读取这个文件
	numbers = json.load(f_obj) # 使用函数json.load()加载存储在numbers.json中的信息，并将其存储到变量numbers中

print(numbers)