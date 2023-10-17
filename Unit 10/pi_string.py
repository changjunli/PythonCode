"""打开文件并读取文件内的内容，判断用户输入生日月日年是否在圆周率Pi中出现，打印消息"""
file_path = "pi_million_digits.txt" # 绝对路径
with open(file_path) as file_object:
	lines = file_object.readlines() # 创建一个包含文件各行内容的列表

pi_string = ''
for line in lines: # 逐行读取
	pi_string += line.rstrip()

print(pi_string[:52] + "...") # 切片，只打印到小数点后50位，其余以省略号结尾
print(len(pi_string))

birthday = input("Enter your birthday,in the form mmddyy:") # 输入生日，判断生日是否出现在圆周率pi中
if birthday in pi_string:
	print("your birthday appears in the first million digits of pi !")
else:
	print("your birthday does not appears in the first million digits of pi.")