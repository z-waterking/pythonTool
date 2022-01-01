# -*- coding: utf-8 -*-
# @Time     :2022/1/1 22:22
# @Author   :Z
# @File     :lineChart.py

import matplotlib.pyplot as plt
import numpy as np

def lineChart(x, y, name = "lineChart_tmp"):
    # 初始化图表工具
    plt.figure()

    # 1. 画出简单折线图
    plt.plot(x, y)

    # 2. 更改线条颜色
    plt.plot(x, y, color = 'red')

    # 3. 画出双/多折线图
    y1 = y * 2
    plt.plot(x, y1, color = 'green')

    # 4. 更改坐标轴范围
    plt.xlim((-2, 2))
    plt.ylim((0.5, 5))

    # 5. 更改坐标轴的数字显示
    plt.yticks([0.5, 3, 5], ['are', 'you', 'kidding?'])

    # 保存图片
    plt.savefig(open("./target/{}.png".format(name), 'wb'))

if __name__ == "__main__":
    x = np.linspace(-1, 1, 50)
    y = x * x + 1
    print("x: {}".format(x))
    print("y: {}".format(y))
    lineChart(x, y, "lineChart1")
