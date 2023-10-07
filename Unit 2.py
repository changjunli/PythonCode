"""
字符串（字符串首字母大写、转换为大写、转换为小写、删除字符串空白）
"""


#添加一个名为message的变量，每个变量都指向一个值—与该变量相关联的信息。这里指向的值为文本“Hello Python world!”
message = "Hello Python world!"  
print(message)

#修改变量的值并打印出来
message = "Hello Python Crash Course world!"
print(message)

name = "ada lovelace"
print(name.title()) # 以首字母大写的方式显示每个单词，即将每个单词的首字母改为大写

name = "Ada Lovelace"
print(name.upper()) # 将字符串全部改为大写
print(name.lower()) # 将字符串全部改为小写

first_name = "Cha wang"
last_name = "Zhang"
#  full_name = f"{first_name} {last_name}"   f字符串是python3.6引入的，将花括号内的变量替换为其值来设置字符串的格式
full_name = "{} {}".format(first_name,last_name)  # python3.5或更早版本需要使用format(),与上面f方法一样效果
print(full_name)
message_one = f"Hello,{full_name.title()}!"
print(message_one)

print("\tPython") # 在字符串中添加制表符 
print("Language:\nPython\nC\nJavascript") # 在字符串中添加换行符
print("Language:\n\tPython\n\tC\n\tJavascript") # 在字符串中同时添加换行符和制表符

favorite_language = ' Hello Python '
print(favorite_language)
print(favorite_language.rstrip()) # 删除字符串右边末尾空白
print(favorite_language.lstrip()) # 删除字符串左边开头空白
print(favorite_language.strip()) # 删除字符串左右两边空白

universe_age = 14_000_000_000 # 书写很大的数时，可以使用下划线将其中的数字分组，使其更清晰易读。python不会打印下划线定义的数
print(universe_age)

