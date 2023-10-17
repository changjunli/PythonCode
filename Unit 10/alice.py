
"""打开文件并读取内容，使用try...except...else语句异常处理"""
filename = 'alice.txt'
try:
	with open(filename) as f_obj:
		contents = f_obj.read()

except FileNotFoundError:
	msg = "sorry,the file " + filename + " does not exist."
	print(msg)
else:
	words = contents.split() # 用空格分隔内容
	num_words = len(words) # 计算单词个数
	print("The file " + filename + " has about " + str(num_words) + " words.")