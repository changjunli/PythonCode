# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("you can't divide by zero!")

"""try...except...else语句使用，判断不能用0作为除数"""
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number:")
	if first_number == 'q':
		break
	second_number = input("Second number:")
	if second_number == 'q':
		break
	try:      # try语句只包含可能导致错误的代码
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:   # except语句表示出现ZeroDivisionError时，打印提示消息
		print("不能被0整除，0不能作为除数")
	else:     # else语句表示除法成功执行后打印结果
		print(answer)