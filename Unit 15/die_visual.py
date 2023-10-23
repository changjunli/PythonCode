from plotly.graph_objs import Bar,Layout
from plotly import offline

from die import Die  # 从die文件中导入Die类

die_1 = Die() # 创建实例
die_2 = Die(10)

# 掷几次骰子并将结果存储在一个列表中
results = [] # 声明一个空列表，用于存储掷骰子的点数
for roll_num in range(50_000): # 掷骰子1000次
    result = die_1.roll() + die_2.roll() # 每次从1-6个面中随机返回一个点数
    results.append(result) # 将掷骰子的结果点数加到列表中

# 分析结果
frequencies = [] # 创建空列表，用于存储每种点数出现的次数
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value) # 统计每个点数在results中出现的次数
    frequencies.append(frequency)  # 将统计出的次数附加到列表的末尾
# print(frequencies)

# 对结果进行可视化
x_value = list(range(2,max_result+1))
data = [Bar(x=x_value,y=frequencies)]

x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='掷一个D6和一个D10 50000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6_d10.html')




