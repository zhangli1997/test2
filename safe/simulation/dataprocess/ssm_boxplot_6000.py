
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

fig = plt.figure(figsize=(10, 4))  # 创建画布
ax = plt.subplot()  # 创建作图区域



def list_generator(mean, dis, number):  # 封装一下这个函数，用来后面生成数据
    return np.random.normal(mean, dis * dis, number)  # normal分布，输入的参数是均值、标准差以及生成的数量
a=1
# # 半个小时
# data_case1_00 = [x/a for x in [949, 972, 1001, 896, 935, 905,917, 972, 920, 971]]
# data_case1_02 = [x/a for x in [822, 863, 808, 845, 892, 853, 863, 777, 833, 845]]
# data_case1_04 = [x/a for x in [930, 908, 894, 867, 863, 883, 876, 861, 894, 896]]
# data_case1_06 = [x/a for x in [655, 652, 601, 585, 612, 622, 611, 618, 674, 619]]
# data_case1_08 = [x/a for x in [467, 462, 497, 439, 465, 440, 452, 483, 484, 466]]
# data_case1_10 = [x/a for x in [160, 124, 115, 122, 118, 106,  93,  84, 122, 161]]
#
# data_case2_00 = [x/a for x in [949, 972, 1001, 896, 935, 905,917, 972, 920, 971]]
# data_case2_02 = [x/a for x in [885, 892, 883, 882, 877, 897, 911, 885, 870, 910]]
# data_case2_04 = [x/a for x in [969, 906, 915, 831, 877, 921, 961, 888, 983, 877]]
# data_case2_06 = [x/a for x in [623, 642, 662, 646, 628, 643, 632, 629, 689, 596]]
# data_case2_08 = [x/a for x in [461, 470, 478, 466, 477, 512, 512, 476, 493, 472]]
# data_case2_10 = [x/a for x in [121, 100, 72, 86, 67, 83, 74, 66, 74, 68]]
#
# data_case3_00 = [x/a for x in [1084, 1170, 1196, 1165, 1111, 1137, 1135, 1094, 1107, 1120]]
# data_case3_02 = [x/a for x in [1084, 1170, 1196, 1165, 1111, 1137, 1135, 1094, 1107, 1120]]
# data_case3_04 = [x/a for x in [1084, 1170, 1196, 1165, 1111, 1137, 1135, 1094, 1107, 1120]]
# data_case3_06 = [x/a for x in [1084, 1170, 1196, 1165, 1111, 1137, 1135, 1094, 1107, 1120]]
# data_case3_08 = [x/a for x in [1084, 1170, 1196, 1165, 1111, 1137, 1135, 1094, 1107, 1120]]
# data_case3_10 = [x/a for x in [1084, 1170, 1196, 1165, 1111, 1137, 1135, 1094, 1107, 1120]]

# 5min
data_case1_00 = [x/a for x in [93, 107, 94, 101, 111]]
data_case1_02 = [x/a for x in [75, 61,  111, 71, 89]]
data_case1_04 = [x/a for x in [21, 20, 26, 20, 17]]
data_case1_06 = [x/a for x in [8, 10, 8, 8, 6 ]]
data_case1_08 = [x/a for x in [2,1,2, 2, 2]]
data_case1_10 = [x/a for x in [0,0,0,0,0]]

data_case2_00 = [x/a for x in [93, 107, 94, 101, 111 ]]
data_case2_02 = [x/a for x in [97, 64, 95, 90, 85]]
data_case2_04 = [x/a for x in [32, 33, 43, 33, 44]]
data_case2_06 = [x/a for x in [29,24,32,28,11]]
data_case2_08 = [x/a for x in [16,26,24,10,19]]
data_case2_10 = [x/a for x in [3,2,8,2,0]]

data_case3_00 = [x/a for x in [125, 125,125, 125,125]]
data_case3_02 = [x/a for x in [94,94,94,94,94]]
data_case3_04 = [x/a for x in [61,61,61,61,61]]
data_case3_06 = [x/a for x in [65, 65, 65, 65, 65]]
data_case3_08 = [x/a for x in [44, 44, 44, 44, 44]]
data_case3_10 = [x/a for x in [27, 27, 27, 27, 27]]
125
94
61
65
44
27



bp1 = ax.boxplot([data_case1_00,data_case1_02,data_case1_04,data_case1_06,data_case1_08,data_case1_10], positions=[1,5,9,13,17,21], widths=0.6,
                 patch_artist=True, boxprops={'color':'pink','facecolor':'pink'})
bp2 = ax.boxplot([data_case2_00,data_case2_02,data_case2_04,data_case2_06,data_case2_08,data_case2_10], positions=[2,6,10,14,18,22], widths=0.6,
                 patch_artist=True, boxprops={'color':'lightblue','facecolor':'lightblue'})
bp3 = ax.boxplot([data_case3_00,data_case3_02,data_case3_04,data_case3_06,data_case3_08,data_case3_10], positions=[3,7,11,15,19,23], widths=0.6,
                 patch_artist=True, boxprops={'color':'lightgreen','facecolor':'lightgreen'})

ax.legend([bp1["boxes"][0], bp2["boxes"][0],bp3["boxes"][0]], ['LRMOCS control', 'Traffic signal control', 'Out-control'])#loc='upper middle'


ax.set_xticks([2,6,10,14,18,22]) # 设置刻度
ax.set_xticklabels(["0", "0.2","0.4","0.6", "0.8","1.0"]) # 设置刻度标签

# # Set the y-ticks to a custom scale
# ax.set_yticks([0,200,400,600,800])
# ax.set_yticklabels(["0","200","400","600","800"])
plt.ylim(ymin=0, ymax=140)
plt.xlabel('Penetration rate of AV')
plt.ylabel('Number of potential conflicts')
plt.show()

