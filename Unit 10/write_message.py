"""
调用open()时提供了两个实参。第一个实参也是要打开的文件的名称；
第二个实参（'w'）告诉Python，我们要以写入模式打开这个文件。打开文件时，可指定读取模
式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）。如果
你省略了模式实参，Python将以默认的只读模式打开文件。
"""
# file_name = "programming.txt" # 文件名
# with open(file_name,'w') as file_object:
# 	file_object.write("I like study Python Language.\n")
# 	file_object.write("I like games.\n")


"""向文件中写入"""
file_name = "hello.txt" # 文件名
with open(file_name,'a') as file_object:# 'a'表示以附加模式添加文件内容，不清空原来的文件内容，如果指定的文件不存在，则创建空文件并追加内容
	file_object.write("Hello Python language .\n")
	file_object.write("I want to study Python.\n")