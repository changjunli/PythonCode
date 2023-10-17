"""
函数open()
返回一个表示文件的对象。在这里，open('pi_digits.txt')返回一个表示文件pi_digits.txt的对
象；Python将这个对象存储在我们将在后面使用的变量中。关键字with在不再需要访问文件后将其关闭
"""
# file_path = "D:\Sublime Text\Code\pi_digits.txt" # 绝对路径
# with open(file_path) as file_object:
# 	contents = file_object.read() # 读取整个文件
# 	print(contents.rstrip()) # 删除字符串多出来的空行


# file_path = "D:\Sublime Text\Code\pi_digits.txt" # 绝对路径
# with open(file_path) as file_object:
# 	for line in file_object: # 逐行读取
# 		print(line.rstrip())


# file_path = "D:\Sublime Text\Code\pi_digits.txt" # 绝对路径
# with open(file_path) as file_object:
# 	lines = file_object.readlines() # 创建一个包含文件各行内容的列表

# for line in lines: # 逐行读取
# 	print(line.rstrip())


"""打开文件并读取，读取文件中的内容和计算内容长度"""
file_path = "D:\Sublime Text\Code\pi_digits.txt" # 绝对路径
with open(file_path) as file_object:
	lines = file_object.readlines() # 创建一个包含文件各行内容的列表

pi_string = ''
for line in lines: # 逐行读取
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))