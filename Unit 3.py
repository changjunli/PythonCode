"""
列表

"""


bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

print(bicycles[0]) #打印列表索引为0的第一个元素trek
print(bicycles[1]) #打印列表索引为1的第二个元素cannondale
print(bicycles[2]) #打印列表索引为2的第三个元素redline
print(bicycles[3]) #打印列表索引为3的第四个元素specialized

print(bicycles[0].title()) #打印列表索引为0的第一个元素并以首字母大写显示Trek

print(bicycles[-1]) #打印最后一个列表元素specialized

message = f'My first bicycle was a {bicycles[0].title()}'
print(message)

print('\n===============================') # \n表示换行 \t表示制表符首行缩进
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles) #打印显示，结果为['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati' #修改列表第一个元素值为ducati
print(motorcycles)   #打印显示，结果为['ducati', 'yamaha', 'suzuki']

motorcycles.append('abcd') #附加元素到列表末尾
print(motorcycles) #打印显示，结果为['ducati', 'yamaha', 'suzuki', 'abcd']

print('\n===============================')
names = []
names.append('Lilei')
names.append('Jim')
names.append('Anlice')
names.append('Nike')
print(names)     #打印显示，结果为['Lilei', 'Jim', 'Anlice', 'Nike']
print(len(names)) #打印列表的长度

names.insert(2,'LiNing') #将值插入到索引为2的第三个元素
print(names)             #打印显示，结果为['Lilei', 'Jim', 'LiNing', 'Anlice', 'Nike']

print('\n=============3.2.3从列表中删除元素 ==================')
# 从列表中删除一个元素，且不再以任何方式使用它，就使用del语句
# 在删除元素后还能继续使用它，就使用方法pop()
print(motorcycles)       #打印显示，结果为['ducati', 'yamaha', 'suzuki', 'abcd']

del motorcycles[3]       # 使用del语句删除元素，这里是删除索引为3的第四个元素
print(motorcycles)      #输出语句，这里输出['ducati', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop() #删除列表末尾元素相当于弹出栈顶元素，并赋值给变量
print(motorcycles)                    #打印列表，输出 ['ducati', 'yamaha']
print(popped_motorcycle)              #打印弹出的值，输出 suzuki

motorcycles = ['honda','yamaha','suzuki']

last_owned = motorcycles.pop() #使用pop()来删除列表中任意位置的元素.注意：当使用pop（）时，被弹出的元素就不再列表中了
print(f"我拥有的摩托最后购买的是{last_owned.title()}品牌") # 输出：最后购买我拥有的是Suzuki

first_owned = motorcycles.pop(0) # 使用pop()来删除列表中任意位置的元素，只需要在（）中指定删除元素的索引即可
print(f"我拥有的摩托最先购买的是{first_owned.title()}品牌") # 输出：最先购买我拥有的是honda

print("\n=========================================")
motorcycles = ['honda','yamaha','suzuki','ducati','zongshen','ducati']
print(f"删除之前打印：{motorcycles}")

motorcycles.remove('ducati') # 从列表中删除值'ducati',只删除第一个指定的值
print(f"删除ducati之后打印：{motorcycles}")

print("\n================3.3.1使用方法sort()对列表永久排序=========================")
cars = ['bmw','audi','toyota','subaru']
cars.sort()               # 使用sort()方法永久性地修改列表元素的排列顺序，这里按照字母顺序排列abcdefg.......xyz
print(cars)               #打印结果['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)   # 按与字母顺序相反的顺序排列列表元素，只需向sort()方法传递参数reverse=True即可
print(cars)               #打印结果['toyota', 'subaru', 'bmw', 'audi']

print("\n================3.3.2使用方法sorted()对列表临时排序=========================")
carNames = ['bmw','audi','toyota','subaru']
print(carNames)          #打印输出['bmw', 'audi', 'toyota', 'subaru']，原始列表元素
print(sorted(carNames))  #打印输出['audi', 'bmw', 'subaru', 'toyota']，以特定的顺序显示列表元素，不影响在列表中的原始排列顺序
print(carNames)          #打印输出['bmw', 'audi', 'toyota', 'subaru']，这里原始列表元素没变
carNames.sort(reverse=True) # 按与字母顺序相反的顺序排列列表元素 ????  书中是用sorted()方法传参reverse=True，但实际操作报错
print(carNames)

print("\n================3.3.3倒着打印列表========================")
carNames = ['bmw','audi','toyota','subaru']
print(carNames)          #输出['bmw', 'audi', 'toyota', 'subaru']

carNames.reverse()       #反转列表元素的排列顺序，反转列表元素的排列顺序，永久性地修改列表元素的排列顺序，也可随时恢复原来的排列顺序，只需对列表再次调用reverse()即可
print(carNames)          #输出['subaru', 'toyota', 'audi', 'bmw']

print("\n================3.3.4确定列表的长度=========================")
length = len(carNames)   #使用len（）函数快速获取列表的长度，列表包含4个元素，其长度为4
print(f"carNames length:{length}")
