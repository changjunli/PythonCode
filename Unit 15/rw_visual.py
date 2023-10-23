import matplotlib.pyplot as plt

from random_Walk import RandomWalk

while True:
    rw = RandomWalk(50_000)  # 创建一个RandomWalk实例
    rw.fill_walk()

    # 将所有的点都绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,6),dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_value, rw.y_vlaue,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)

    # 突出起点和终点
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_value[-1],rw.y_vlaue[-1],c='red',edgecolors='none',s=100)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)

    plt.show()

    keep_running = input("make another walk?(y/n):")
    if keep_running == 'n':
        break

