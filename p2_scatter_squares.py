#!/usr/bin/env python
# Author:Wang Xueming

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=2)
# plt.scatter(x_values, y_values, edgecolor='none', s=2)  # 删除轮廓
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=2)  # 设置颜色
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=2)  # 设置颜色
# cmap 告诉pyplot 使用哪个颜色映射。这些代码将 y 值较小的点显示为浅蓝色，并将 y 值较大的点显示为深蓝色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=2)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=12)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

# 自动保存
plt.savefig('squares_plot.png', bbox_inches='tight')
# 显示
plt.show()