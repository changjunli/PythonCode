"""
@date:2023年10月5日
如何定义字典、如何使用存储在字典中的信息、如何访问和修改字典中元素、如何遍历字典中所有信息、遍历字典中的键值对、所有的键和所有的值
如何在列表中嵌套字典、在字典中嵌套列表、在字典中嵌套字典
"""
people = {}   #定义一个空的字典
people['Name'] = 'Tom'
people['Age'] = 18
people['Weight'] = 80
people['Address'] = '重庆市渝中区青年路153号负7号'
people['Phone'] = '15313267892'
people['ZipCode'] = '重庆市渝中区青年路153号负7号'
print(f"空字典中添加键值后为：{people}")

# 遍历所有键值对
for key,value in people.items():
	print(f"\n键:{key}")
	print(f"值:{value}")

# 遍历字典中的所有键
for key in people.keys():
	print(f"键:{key}")

# 遍历字典中的所有值
for value in people.values():
	print(f"遍历所有值:{value}")

# 按特定顺序遍历字典中的所有键
for item in sorted(people.keys()):    #这里对所有字典的键在遍历前进行排序
	print(f"这里是遍历键：{item}")

# 剔除重复项使用set集合，保证每个元素是独一无二的
for val in set(people.values()):
	print(f"使用集合set剔除重复元素后遍历值:{val}")

#集合和字典很容易混淆，都是用花括号定义的，当花括号内没有键值对时定义的可能是集合，不同于列表和字典，集合不会以特定的顺序存储元素
languages = {'python','ruby','python','c'} #使用花括号直接创建集合，并在其中用逗号分隔元素
print(languages)                           #输出 {'c', 'python', 'ruby'}

# 定义简单的字典
person = {'first_name':'Li','last_name':'Lei','age':37,'city':'重庆'}

print(f"打印键'first_name'对应的值:{person['first_name']}")     # 打印键'first_name'对应的值，输出Li
print(f"打印键'last_name'对应的值:{person['last_name']}")       # 打印键'last_name'对应的值，输出Lei
print(f"打印键'age'对应的值:{person['age']}")                   # 打印键'age'对应的值，输出37
print(f"打印键'city'对应的值:{person['city']}")                 # 打印键'city'对应的值，输出重庆

# 定义一个字典，键值对应
persons_Like_Count = {
	'Jim':'22',
	'LiLei':'88',
	'Smith':'66',
     '李云龙':'100',
}

print(persons_Like_Count)          # 输出字典 {'Jim': '22', 'LiLei': '88', 'Smith': '66', '李云龙': '100'}

persons_Like_Count['Jim'] = '11'   # 修改字典中Jim键对应的值
print(persons_Like_Count)          # 输出字典 {'Jim': '11', 'LiLei': '88', 'Smith': '66', '李云龙': '100'}

persons_Like_Count['特朗普'] = '12' # 添加键值对
persons_Like_Count['John'] = '28'  # 添加键值对
print(persons_Like_Count)          # 输出字典 {'Jim': '11', 'LiLei': '88', 'Smith': '66', '李云龙': '100', '特朗普': '12', 'John': '28'}

del persons_Like_Count['特朗普']   # 删除键值对
print(persons_Like_Count)         # 输出字典  {'Jim': '11', 'LiLei': '88', 'Smith': '66', '李云龙': '100', 'John': '28'}

# 这里没有定义phone就调用打印phone键对应值会报错KeyError: 'phone'
# print(persons_Like_Count['phone'])  可以用get()指定键不存在时返回一个默认值
phone_Value = persons_Like_Count.get('phone','没有指定值')   # get(第一个参数为指定键必不可少，第二个参数为可选)
print(phone_Value)                #输出  get()没有指定第二个参数，返回默认None,如果指定了第二个参数，则返回第二个参数

# 嵌套字典：将一系列字典存储在列表中或将列表作为值存储在字典中
cat = {'name':'aa','color':'yellow','主人':'bruceLi'}
dog = {'name':'bb','color':'red','主人':'tomas'}
hourse = {'name':'cc','color':'green','主人':'jieXi'}
pets = [cat,dog,hourse]
for pet in pets:
	print(pet)

print("\n-----------------------------------------------------------------------------------------")
#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
	new_alien = {'color':'green','point':5,'speed':'slow'}
	aliens.append(new_alien)


for alien in aliens[:3]:         # 遍历前三个，如果外星人为绿色，则修改color、speed、point的值
	if alien['color'] == 'green':# 判断
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['point'] = 10

#显示前5个外星人
for alien in aliens[:5]:
	print(alien)
print("...")

print(f"外星人总数是:{len(aliens)}") #输出30
print("--------------------------------------------")

# 定义字典，在字典中存储列表
pizza = {
	'crust':'厚实的',
	'toppings':['火腿','奶酪'],
}

print(f"你点了一个{pizza['crust']}披萨，加有以下配料：")
for topping in pizza['toppings']:
	print("\t" + topping)


love_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
}

for name,languages in love_languages.items(): #遍历字典中的键值对
	print(f"\n {name.title()}最喜欢的语言是:")
	for language in languages:
		print(f"\t{language.title()}")

print("--------------------------------------------------------------")

# 在字典中存储字典
users = {
	'aeinstein':{
	   'first':'albert',
	   'last':'einstein',
	   'location':'princeton',
	},
	'mcurie':{
       'first':'marie',
	   'last':'curie',
	   'location':'paris',
	 },
}

for username,user_Info in users.items():
	print(f"用户名:{username}")
	fullName = f"{user_Info['first']}  {user_Info['last']}"
	location = user_Info['location']

	print(f"\t 全名:{fullName.title()}")
	print(f"\t 位置:{location.title()}")