import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    # 从文件中获取日期和最高温度
    dates,highs = [],[]
    for row in reader:
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

    # 根据最高温度绘制图形
    plt.style.use('seaborn-v0_8-pastel')
    fig,ax = plt.subplots()
    ax.plot(dates,highs,c='blue')

    # 设置图形的格式
    ax.set_title("2018年7月最高温度",fontsize=24)
    ax.set_xlabel('',fontsize=16)
    ax.set_ylabel("温度(F)",fontsize=16)
    ax.tick_params(axis='both',which='major',labelsize=16)
    # 汉字字体，优先使用楷体，找不到则使用黑体
    plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
    # 正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    plt.show()



