import matplotlib.pyplot as plt  # 导入模块pyplot并指定别名plt,模块pyplot包含很多用于生成图表的函数

squares = [1,4,9,16,25]  # 创建列表，用来存储制作图表的数据
fig,ax = plt.subplots()  # subplots()可在一张图片中绘制一个或多个图表，变量fig表示整张图片，变量ax表示图片中各个图表
ax.plot(squares,linewidth=3)

ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值的平方",fontsize=24)

ax.tick_params(axis='both',labelsize=14)
# 汉字字体，优先使用楷体，找不到则使用黑体
plt.rcParams['font.sans-serif'] = ['Kaitt','SimHei']
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False

plt.show()  # 根据给定的数据绘制图表并显示
