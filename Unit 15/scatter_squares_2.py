import matplotlib.pyplot as plt
"""
根据绘制一系列点连线，线条渐变颜色映射
"""
x_values = range(1,1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8-ticks')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10) # 绘制一系列点,颜色映射渐变

ax.set_title("平方数",fontsize=24) # 设置图表标题
ax.set_xlabel("值",fontsize=14)   # 设置x轴标题
ax.set_ylabel("值的平方",fontsize=24)  # 设置y轴标题

ax.tick_params(axis='both',which='major',labelsize=14)
ax.axis([0,1100,0,1100000])

# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt','SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False
# plt.show()  显示出来
plt.savefig('squares_plot.png',bbox_inches='tight') # 保存图片