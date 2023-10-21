import matplotlib.pyplot as plt
"""
绘制一系列点
"""
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.style.use('seaborn-v0_8-ticks')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,s=50) # 绘制一系列点

ax.tick_params(axis='both',which='major',labelsize=14)
plt.show()