import json
"""问候用户"""

def get_stored_username():
	"""获取json文件中存储的用户名"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""提示用户输入用户名"""
	username = input("what is your name?")
	filename = 'username.json'
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	return username



def greet_user():
	"""问候用户"""
	username = get_stored_username()
	if username: # 判断是否存在用户名，是则直接打印问候消息，否则从用户输入后将用户名写入json文件，并打印消息
		print("welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("we'll remember you when you come back," + username + "!")

greet_user() # 调用方法