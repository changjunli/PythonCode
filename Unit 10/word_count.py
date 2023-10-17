"""从列表文件名中统计每个文件包含多少个单词"""
def count_words(filename):
	"""计算一个文件大致包含多少个单词"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()

	except FileNotFoundError:
		msg = "sorry,the file " + filename + " does not exist."
		print(msg) # 出现异常时打印消息告诉用户，也可以什么也不做（except模块内部不写任何代码）
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','siddhartha.txt','moby_dict.txt','little_women.txt'] # 文件列表
for filename in filenames: # 遍历文件并计算每个文件包含多少个单词
	count_words(filename) 