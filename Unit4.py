# ********************************************************************************************
# 利用for循环遍历整个列表
# 数值列表 range()函数使用
# 处理部分列表元素——切片、遍历切片元素、复制列表
# 元组定义、遍历、修改元组变量
#*********************************************************************************************
"""
多行注释
"""
# 使用for循环来遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 使用for循环来遍历整个列表,打印消息
pics = ['xx', 'yy', 'zz']
for pic in pics:
    print(f"{pic.title()},that was a great trick!")  # 执行三次,一定缩进
    print(f"I can't wait to see your next trick ,{pic.title()}.\n")  # 执行三次,一定缩进
print("Thank you ,everyone.That was a great magic show!")  # 此行没有缩进，只执行一次；缩进需要执行三次

# 创建数值列表，使用range()函数
for value in range(1, 5):
    print(value)  # 只打印1~4，range（）从指定的第一个值开始数，在到达指定的第二个值时停止，在第二个值处停止，输出不包含该值

print("\n")
for key in range(1, 6):
    print(key)  # 打印1~5

# 使用range()函数创建数字列表
numbers = list(range(1, 6))  # 使用list()函数将range()的结果直接转换为列表
print(numbers)  # 输出[1, 2, 3, 4, 5]

even_numbers = list(range(2, 11, 2))  # 第三个参数为步长
print(even_numbers)  # 输出[2, 4, 6, 8, 10]

# 创建一个空列表，包含1~10的平方
squares = []
for val in range(1, 11):
    square = val ** 2  # **表示乘方运算
    squares.append(square)
print(squares)  # 输出[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

conns = []
for val in range(1, 11):
    conns.append(val ** 2)  # 直接将每个计算得到的值附加到列表末尾
print(conns)  # 输出[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"最小值:{min(digits)}")
print(f"最大值：{max(digits)}")
print(f"总和：{sum(digits)}")

# 列表解析
squs = [value ** 2 for value in range(1, 11)]
print(squs)  # 输出[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 打印1~20
for i in range(1, 21):
    print(i)

nums = []
for v in range(1, 1000001):
    nums.append(v)
print(nums)  # 打印1~1000001的列表数字
print(f"在1~1000000中，最小的是：{min(nums)}")
print(f"在1~1000000中，最大的是：{max(nums)}")
print(f"在1~1000000中，总和是：{sum(nums)}")

# 打印1~20内的奇数
m = []
for i in range(1, 20, 2):
    m.append(i)
print(m)  # 输出 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 打印从3~30能被3整除的数
temp = []
for i in range(3, 31):
    if i % 3 == 0:
        temp.append(i)
print(temp)  # 输出[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# 打印1~10的立方
tabs = []
for lam in range(1, 11):
    tab = lam ** 3
    tabs.append(tab)
print(tabs)  # 输出 [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# 使用列表解析生成一个列表，包含前10个整数的立方
digNums = [num ** 3 for num in range(1, 11)]
print(digNums)  # 输出 [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# 处理列表的部分元素，python称为切片，打印列表的一个切片
player = ['charles','martina','michael','florence','eli']
print(player[0:3]) # 打印索引0到索引3，但不包含索引3的值，输出 ['charles', 'martina', 'michael']
print(player[1:4]) # 打印索引1到索引4，但不包含索引4的值，输出['martina', 'michael', 'florence']
print(player[:4]) # 没有指定第一个索引，从列表开头开始，到第四个索引值，但不包括第四个索引的值，输出['charles', 'martina', 'michael', 'florence']
print(player[2:]) # 从第二个索引到列表末尾的所有元素，输出 ['michael', 'florence', 'eli']
print(player[-3:]) # 输出['michael', 'florence', 'eli']，负数索引返回离列表末尾相应距离的元素，从后往前

# 遍历切片,这里是遍历前3名队员并打印他们的名字
print("Here are the first three players on my team:")
for play in player[:3]:
    print(play.title())

# 复制列表
myfoods = ['披萨','咖啡','蛋糕']
friend_foods = myfoods[:] # 提取一个切片作为列表的副本，并赋值给变量

myfoods.append('茉莉蜜茶')
friend_foods.append('奶茶')

print("我最喜爱的食物是：")
print(myfoods)      #  输出 ['披萨', '咖啡', '蛋糕', '茉莉蜜茶']
print(("\n 我朋友最喜爱的食物是："))
print(friend_foods) # 输出['披萨', '咖啡', '蛋糕', '奶茶']

# 元组，不可变,用圆括号来标识
dimensions = (200,50)
print(dimensions[0])  #输出 200
print(dimensions[1])  #输出50

#遍历元组中所有的值
dicals = (211,985,100)
for dical in dicals:
    print(dical)
#修改元组变量
collects = (321,111,777)
print("元组里面元素的值为：")
for collect in collects:
    print(collect)

collects = (222,333,444)
print("\n修改元组变量后的值为：")
for collect in collects:
    print(collect)