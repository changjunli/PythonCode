import json
"""将用户输入姓名写入json文件，并打印消息"""
username = input("what is your name?")

filename = 'username.json'
with open(filename,'w') as f_obj:
	json.dump(username,f_obj)
	print("We'll remember you when you come back," + username + "!")