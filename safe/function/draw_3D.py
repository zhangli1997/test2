'''
  时空图函数
'''
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def draw_3D(name):
    plt.figure(figsize=(10, 4))
    with open(r'../temporarydata/space_time/time1.csv', 'r') as f:
        text = f.readlines()
        print(len(text))
    x = []
    y = []
    v = []
    for i in range(len(text)):
        x.append(float(list(text[i].split(','))[1]))
        y.append(float(list(text[i].split(','))[3]))
        v.append(list(text[i].split(','))[2])
    j = 0
    for j in range(23):
        v[j] = int(float(v[j]))
    norm = matplotlib.colors.Normalize(vmin=5, vmax=25)
    ax = plt.scatter(np.array(x), np.array(y), marker='.', s=1, c=v, cmap='jet_r', norm=norm)
    plt.ylim(ymin=0, ymax=1600)
    plt.xlim(xmin=0, xmax=400)
    for y_lim in range(11):
        plt.text(0, y_lim * 100, '{} '.format(y_lim * 100), ha='right')
    for x_lim in range(20):
        plt.text(x_lim * 20, -50, '{} '.format(x_lim * 20), ha='center')
    plt.text(-20, 400, 'position(m)', ha='right', rotation=90, fontsize=12)
    plt.text(200, -120, 'time(s)', ha='center', fontsize=12)
    plt.xticks([])
    plt.yticks([])
    plt.clim(4, 20)
    plt.colorbar()
    plt.savefig('../image/space_time/3D_{}.png'.format(name))
    plt.show()
if __name__=='__main__':
    draw_3D('space')