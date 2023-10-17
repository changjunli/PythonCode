# 定义Dog类，在Python中，首字母大写的名称指的是类,这个类定义中的括号是空的，从空白创建这个类
class Dog(): 
	"""一次模拟小狗的简单尝试"""

	""" __init__()是一个特殊的方法，每当你根据Dog类创建新实例时，Python都会自动运行它。在这个方法的名称中，
	 开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
	Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法
    调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
    我们创建Dog实例时，Python将调用Dog类的方法__init__()。我们将通过实参向Dog()传递名字和
    年龄；self会自动传递，因此我们不需要传递它。每当我们根据Dog类创建实例时，都只需给最
    后两个形参（name和age）提供值。
    """
	def __init__(self,name,age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age

	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + " rolled over!")


my_dog = Dog('whild',8) # 创建实例
print(f"my dog name is {my_dog.name.title()}")  # 获取属性的值
print(f"my dog age is {str(my_dog.age)} years old.") # 获取属性的值
my_dog.sit()           # 实例调用方法
my_dog.roll_over()     # 实例调用方法

your_dog = Dog('lucky',3) # 创建实例
print(f"your_dog name is {your_dog.name.title()}")  # 获取属性的值
print(f"your_dog age is {str(your_dog.age)} years old.") # 获取属性的值
your_dog.sit()           # 实例调用方法
your_dog.roll_over()     # 实例调用方法

class Car():

	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

my_new_car = Car('audi','a4',2016)       # 创建新的实例
print(my_new_car.get_descriptive_name()) # 调用方法