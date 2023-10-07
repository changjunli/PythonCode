"""
input()函数使用，主要用于等待用户的输入，再根据用户输入的内容进行判断
while循环是不断运行，直到指定的条件不满足为止
"""
# sublime Text 编辑器不能运行提示用户输入的程序，可以使用sublime Text来编写提示用户输入的程序，但必须从终端运行它们
message = input("告诉我一些事，我将重复它并回给你：") # 等待用户输入 Hello everyone!
print(message)             # 输出 Hello everyone!        

name = input("请输入您的姓名：")
print(f"\n你好,{name}")

prompt = "如果你告诉我们你是谁，我们能把信息单独给你看."
prompt += "\n你的名字是什么？"

_name = input(prompt)
print(f"\nHello,{_name}!")


# 用户输入一个年龄进行判断
age = input("你多大年龄？")
print(age)            
print(type(age)) # 输出类型，这里是<class 'str'>为字符串类型

if int(age)>=18:
    print(f"{age}岁大于或等于18岁，属于有民事行为能力人")
else:
    print(f"{age}岁小于18岁，属于无民事行为能力人")


# 求模运算%,两个数相除返回余数,这里让用户输入一个数，并判断这个数是否是10的整数倍
number = input("请输入一个数：")
number = int(number)

if number % 10 == 0:
    print(f"{number} 是10的整数倍")
else:
    print(f"{number} 不是10的整数倍")

print("\n------------------------------------------------------------------------")
# 利用while循环打印1~5的数
current_number = 1
while current_number <= 5:  # 执行判断5次
    print(current_number)   # 输出 1,2,3,4,5
    current_number += 1     # current_number从第1次开始加1，值分别为 2,3,4,5


# 输入一个字符串，打印出来。当用户输入quit后，退出循环
prom = "\n请输入一个消息，我将打印告知你."
prom += "\n输入'quit'结束该项目:"
message = ""
while message != 'quit':
    message = input(prom)

    if message != 'quit':
        print(message)


# 使用标志
promstr = "\n请输入消息*************"
promstr += "\n如果输入'quit'就结束程序："

active = True
while active:
    message = input(promstr)

    if message == 'quit':
        active = False
    else:
        print(message)

# 使用break退出循环
viewstr ="\n*********请输入你最喜欢的城市名称，"
viewstr += "输入'quit'退出循环："
while True:
    city = input(viewstr)
    if city == 'quit':
        break                # 立即退出循环，不再运行余下的代码

    else:
        print(f"我喜欢{city}")


# 打印100以内的奇数，使用continue 返回循环开头，并根据条件测试结果决定是否继续执行循环
current_value = 0
strs = []
while current_value < 100:
    current_value += 1
    if current_value % 2 == 0:
        continue           #  continue 语句忽略余下的代码，返回循环的开头
    else:
        strs.append(str(current_value))

print(f"100以内的奇数共{len(strs)}个,分别为：{strs}")

# x = 1
# while  x <= 5:
#     print(x)
#     x += 1


# 在列表之间移动元素
unconfirmed_users = ['xxx','yyy','zzz']
confirmed_users = []

while unconfirmed_users:  # 不断运行while循环，直到该列表变成空的
    current_user = unconfirmed_users.pop() # 删除列表中末尾的元素，不再列表中
    print(f"验证用户：{current_user.title()}")
    confirmed_users.append(current_user)

print("\n以下用户已经验证：")
print(confirmed_users)
for confirmed_user in confirmed_users:  # 遍历列表
    print(confirmed_user.title())


# 删除为特定值的所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# 使用用户输入来填充字典
responses = {}
polling_active = True

while polling_active:
    name = input("\n你的姓名是什么？请输入：")
    response = input("你最喜欢爬那座山?请输入:")

    responses[name] = response
    reapeat = input("你愿意让其他人来回答吗?(yes/no)")
    if reapeat == 'no':
        polling_active = False

print("\n-----结果----")
for name,response in responses.items():
    print(f"{name} 喜欢 {response}")