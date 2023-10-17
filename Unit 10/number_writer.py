import json
"""写入数据到xxx.json文件中"""
numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj) # 将数字列表存储到文件numbers.json中