
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fig = plt.figure(figsize=(10, 4))  # 创建画布
ax = plt.subplot()  # 创建作图区域



def list_generator(mean, dis, number):  # 封装一下这个函数，用来后面生成数据
    return np.random.normal(mean, dis * dis, number)  # normal分布，输入的参数是均值、标准差以及生成的数量
a=1
# 半个小时



data_case1_00 = [x/a for x in [145.05,142.6,142.97,144.15,142.29,143.62,143.38,143.83,145.76,143.1]]
data_case1_02 = [x/a for x in [134.32, 134.62, 134.27, 135.68, 134.07, 134.38, 134.38, 133.85, 133.47, 133.94]]
data_case1_04 = [x/a for x in [128.81, 128.49, 128.25, 130.05, 128.53, 128.9, 128.8, 128.52, 129.45, 129]]
data_case1_06 = [x/a for x in [119.73, 120.4, 120.15, 119.23, 118.91, 119.81, 119.89, 119.45, 119.37, 119.68]]
data_case1_08 = [x/a for x in [114, 113.93, 112.8, 113.63, 113.96, 114.33, 113.82, 113.61, 114.19, 113.49]]
data_case1_10 = [x/a for x in [97.37, 97.11, 96.19, 97.06, 96.71, 95.14, 93.68, 93.26, 95.22, 98.55]]


data_case2_00 = [x/a for x in [145.05,142.6,142.97,144.15,142.29,143.62,143.38,143.83,145.76,143.1]]
data_case2_02 = [x/a for x in [134.54,132.95,134.97,134.53,136.47,133.85,132.79,134.21,133.92,133.86]]
data_case2_04 = [x/a for x in [128.04,128.91,128.88,129.29,128.21,128.26,129.34,128.39,127.62,129.37]]
data_case2_06 = [x/a for x in [119.69,119.17,119.48,119.45,119.55,119.13,119.66,120.23,119.23,120.15]]
data_case2_08 = [x/a for x in [114.04,113.65,112.9,113.55,114.6,112.87,114.25,114.08,113.97,112.87]]
data_case2_10 = [x/a for x in [96.8,95.94,94.23,97.5,92.93,93.99,96.77,97.05,94.7,93.19]]

data_case3_00 = [x/a for x in [93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19]]
data_case3_02 = [x/a for x in [93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19]]
data_case3_04 = [x/a for x in [93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19]]
data_case3_06 = [x/a for x in [93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19]]
data_case3_08 = [x/a for x in [93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19]]
data_case3_10 = [x/a for x in [93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19,93.19]]


bp1 = ax.boxplot([data_case1_00,data_case1_02,data_case1_04,data_case1_06,data_case1_08,data_case1_10], positions=[1,5,9,13,17,21], widths=0.6,
                 patch_artist=True, boxprops={'color':'lightgreen','facecolor':'lightgreen'})
bp2 = ax.boxplot([data_case2_00,data_case2_02,data_case2_04,data_case2_06,data_case2_08,data_case2_10], positions=[2,6,10,14,18,22], widths=0.6,
                 patch_artist=True, boxprops={'color':'lightblue','facecolor':'lightblue'})
bp3 = ax.boxplot([data_case3_00,data_case3_02,data_case3_04,data_case3_06,data_case3_08,data_case3_10], positions=[3,7,11,15,19,23], widths=0.6,
                 patch_artist=True, boxprops={'color':'pink','facecolor':'pink'})

ax.legend([bp1["boxes"][0], bp2["boxes"][0],bp3["boxes"][0]], ['LRMOCS control', 'Traffic signal control', 'Out-control'])#loc='upper middle'


ax.set_xticks([2,6,10,14,18,22]) # 设置刻度
ax.set_xticklabels(["0", "0.2","0.4","0.6", "0.8","1.0"]) # 设置刻度标签

# # Set the y-ticks to a custom scale
# ax.set_yticks([0,200,400,600,800])
# ax.set_yticklabels(["0","200","400","600","800"])
plt.ylim(ymin=0, ymax=160)
plt.xlabel('Penetration rate of AV')
plt.ylabel('Average duration time per vehicle')
plt.show()

