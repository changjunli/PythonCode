"""
函数使用(非常重要)
""" 

from pizza import *   #  这里*表示导入模块中的所有函数
greet_user()
greet_userByName('Jim smith')  # 传参：'Jim smith' 是一个实参

# 传递列表
usernames = ['xy','cd','mn']
greet_users(usernames)

# 在函数中修改列表
unprinted_designs = ['phone','robot','dodeca']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_model(completed_models)


# 函数调用中的每个实参都关联到函数定义中的一个形参。最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。
describe_pet('hamster','harry') # 位置实参，函数调用中的每个实参顺序关联对应到函数中的形参

# 关键字实参是传递给函数的名称—值对,直接在实参中将名称和值关联起来了,不用考虑顺序
# 关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途
describe_pet(animal_type='dog',pet_name='willie') # 关键字实参，等价于describe_pet(pet_name='willie',animal_type='dog')
describe_pet('dog','willie') # 等价于 describe_pet(animal_type='dog',pet_name='willie')结果

# 编写函数时可给每个形参指定默认值。在调用函数中给形参提供了实参时，将使用指定的实参值；
# 否则将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用
describe_petTypeName('TaiDi-Alogha') # 调用传参，使用形参默认值

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_Name('john','hooker','lee')
print(musician)


# 导入整个模块
import pizza  # 这里访问pizza.py 编写一条import语句并在其中指定模块名，就可在程序中使用该模块中的所有函数
pizza.make_pizza(20,'火腿')
pizza.make_pizza(30,'aa','bb','cc')
print("----------------------导入整个模块-分割符号-----------------------")

# 使用as给模块指定别名
import pizza as p
p.make_pizza(20,'火腿')
p.make_pizza(30,'aa','bb','cc')
print("----------------------使用as给模块指定别名-分割符号-----------------------")

# 导入模块中特定的函数
from pizza import add,test  # from 模块名 import 函数名1,函数名2
number = add(2,3)
value = test(3,4)
print(f"number = {number}")
print(f"value = {value}")
print("========================导入模块中特定的函数-分隔符=============================")

# 使用as 给函数指定别名
from pizza import add as a,test as t
number = a(2,3)
value = t(3,4)
print(f"number = {number}")
print(f"value = {value}")
print("***********使用as 给函数指定别名-分隔符**********************")


# 传递任意数量的实参
def make_pizza(*toppings):  # 形参名*toppings中的星号表示创建一个名为toppings的空元组，并将受到的所有的值封装在这个元组中
	print(toppings)

make_pizza('peoperoni')
make_pizza('mushrooms','green peppers','extra cheese')

print("-------------------------------------------------")

def make_pizza(*toppings):  # 形参名*toppings中的星号表示创建一个名为toppings的空元组，并将受到的所有的值封装在这个元组中
	print("\nMaking a pizza with the following toppings: ")
	for topping in toppings: #  遍历
		print(f"-" + topping)

make_pizza('peoperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# 结合使用位置实参和任意数量实参
"""
要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最
后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
"""
def make_pizza(size,*toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("+" + topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

# 使用任意数量的关键字实参
"""
需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种
情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
"""
def build_profile(first,last,**user_info): # 形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所有名称—值对都封装到这个字典中。

	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value

	return profile

user_profile = build_profile('albert','einstein',location = 'princeton',field='physics')
print(user_profile)


# 返回字典
musicianValue = build_person('jack','Henery') # 调用函数，返回表示人的整个字典
print(musicianValue)

musicianVal = build_personInfo('jjj','hhh',27)
print(musicianVal)  # 输出{'first': 'jjj', 'last': 'hhh', 'age': 27}
musicianVal = build_personInfo('aaa','bbb')
print(musicianVal)  # 输出{'first': 'aaa', 'last': 'bbb'}


# 函数和while循环、if条件语句判断使用
#这是一个无限循环,用户输入，再打印消息，如果输入q则退出循环
while True:
	print("\n please tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name:")
	if f_name == 'q':
		break

	l_name = input("Last name:")
	if l_name == 'q':
		break

	full_name = get_formatted_name(f_name,l_name)
	print(f"\nHello,{full_name}")

