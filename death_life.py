#!/usr/bin/env python
# Author:Wang Xueming

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中所有性别，男性，女性的平均预期寿命
# 来源 美国开放网站 data.gov
filename = 'files/NCHS_-_Death_rates_and_life_expectancy_at_birth.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, both_sexes, female, male = [], [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y")
            sex_age = float(row[3])

        except ValueError:
            print(current_date, 'missing data')
        else:
            if current_date not in dates:
                dates.append(current_date)

            if row[2] == 'Both Sexes':
                both_sexes.append(row[3])
            elif row[2] == 'Female':
                female.append(row[3])
            elif row[2] == 'Male':
                male.append(row[3])


print(len(dates))
print(len(both_sexes))
print(len(female))
print(len(male))
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 20))

plt.plot(dates, both_sexes, c='red')
plt.plot(dates, female, c='blue')
plt.plot(dates, male, c='green')

# plt.fill_between(dates, female, male, facecolor='blue', alpha=0.1) # 区域着色

# 设置图形的格式
plt.title("NCHS-life_expectancy_at_birth", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Average Life Expectancy (Years)", fontsize=16)
plt.tick_params(axis='y', which='major', labelsize=3)

#plt.axes().get_yaxis().set_visible(False)

plt.show()