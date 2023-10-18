def get_formatted_name(first,last,middle=''):
	"""在名和姓之间加上一个空格并将其首字母大写，再返回结果"""
	if middle:
		full_name = f"{first} {middle} {last}" 
	else:
		full_name = f"{first} {last}" 
	return full_name.title()