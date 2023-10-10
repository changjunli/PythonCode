def make_pizza(size,*toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("+" + topping)

def add(num1,num2):
	return num1 + num2

def  test(a,b):
	return a**b

def greet_user():
	print("Hello!")

def greet_users(names): # 列表
	for name in names:  # 遍历列表
		msg = f"Hello,{name.title()}"
		print(msg)


def greet_userByName(username):   # 变量username是一个形参
	print("Hello," + username.title() + "!")

def describe_pet(animal_type,pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

def describe_petTypeName(pet_name,animal_type='dog'): # 给形参指定默认值
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

def get_formatted_name(first_name,last_name):
	full_name = first_name + ' ' +last_name
	return full_name.title()

def get_formatted_Name(first_name,last_name,middle_name=''):
	if middle_name:          # 检查是否提供了中间名,Python将非空字符串解读为True
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()


def build_person(first_name,last_name):
	person = {'first':first_name,'last':last_name}
	return person

#  新增一个可选形参age,将其默认值设置为特殊值None(表示变量没有值)。可将None视为占位符。在条件测试中，None相当于False
def build_personInfo(first_name,last_name,age=None): 
	person = {'first':first_name,'last':last_name}
	if age:
		person['age'] = age
	return person


def print_models(unprinted_designs,completed_models):
	""" 
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"print model:{current_design}")
		completed_models.append(current_design)

def show_completed_model(completed_models):
	"""显示打印好的所有模型"""
	print("\n The following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

