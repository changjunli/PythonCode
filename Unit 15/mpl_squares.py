import matplotlib.pyplot as plt  # 导入模块pyplot并指定别名plt,模块pyplot包含很多用于生成图表的函数

input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]  # 创建列表，用来存储制作图表的数据

"""
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic',
 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 
 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette',
  'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 
  'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 
  'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
"""

plt.style.use('seaborn-v0_8-darkgrid') # 使用内置样式
fig,ax = plt.subplots()  # subplots()可在一张图片中绘制一个或多个图表，变量fig表示整张图片，变量ax表示图片中各个图表
ax.plot(input_value,squares,linewidth=3) # 校正图形，提供输入值和输出值，linewidth表示线条粗细

ax.set_title("平方数",fontsize=24) # 设置图表标题
ax.set_xlabel("值",fontsize=14)   # 设置x轴标题
ax.set_ylabel("值的平方",fontsize=24)  # 设置y轴标题

ax.tick_params(axis='both',labelsize=14)
# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt','SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

plt.show()  # 根据给定的数据绘制图表并显示
