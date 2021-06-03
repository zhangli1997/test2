'''
  d-v-q
'''


from scipy import optimize

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy
import numpy as np
import matplotlib.pylab
'''
拟合曲线图
'''
#拟合的公式
def f_1(x,A,B,C,V):     #速度密度
    return 1/(A+B/(V-x)+C*x)


def draw_dv(por):
    d = [] #密度
    v1 = []  # 速度
    v = [] #速度
    q = [] # 流量

    with open(r'../temporarydata/edgeoutput/d_v.txt') as f:
        texts = f.readlines()
        for text in texts:
            d.append(float(text.split(',')[0]))
            v1.append(float(text.split(',')[1]))


    v = [i * 3.6 for i in v1]
    func2 = lambda d, v: d * v
    q_before = map(func2, d, v)
    q = list(q_before)

    print(d)
    print(q)
    print(v)
  #速度v _密度d 拟合图
    x0 = v
    y0 = d
    # plt.scatter(x0[:],y0[:],10,"red")
    A1, B1, C1, V1 = optimize.curve_fit(f_1, x0, y0,maxfev=1000000000 )[0]
    x1 = np.arange(0, 80, 0.1)
    y1 = 1 / (A1 + B1 / (V1 - x1) + C1 * x1)
    print(x1)
    print(y1)
    plt.title('V-D')
    plt.xlabel("D(veh/km)")
    plt.ylabel("V(km/h)")
    plt.xlim()
    plt.ylim()
    mpl.pylab.plot(y0, x0, 'b.')
    mpl.pylab.plot(y1, x1, 'r-')
    plt.savefig('../image/d-v-q/d_v{}.png'.format(por))
  #

    # 由q=pv可得流量 _速度图
    x2 = v
    y2 = q
    # plt.scatter(x2[:],y2[:],10,"red")
    x3 = np.arange(0, 80, 0.1)
    y3 = x3 / (A1 + B1 / (V1 - x3) + C1 * x3)
    # plt.plot(x3,y3,'b')
    plt.title('Q-V')
    plt.xlim()
    plt.ylim()
    plt.xlabel("V(km/h)")
    plt.ylabel("Q(veh/h)")
    mpl.pylab.plot(x2, y2, 'b.')
    mpl.pylab.plot(x3, y3, 'r-')
    plt.savefig('../image/d-v-q/q_v{}.png'.format(por))

    # 由q=pv得流量密度
    x4 = y1
    y4 = y3
    x5 = d
    y5 = q
    plt.title('Q-D')
    plt.xlim()
    plt.ylim()
    plt.xlabel("D(veh/km)")
    plt.ylabel("Q(veh/h)")
    mpl.pylab.plot(x4, y4, 'r-')
    mpl.pylab.plot(x5, y5, 'b.')
    plt.savefig('../image/d-v-q/d_q{}.png'.format(por))

    # plt.xlim(xmax=400, xmin=0)
    # plt.ylim(ymax=25, ymin=0)
    # plt.xlabel("density(veh/km)")
    # plt.ylabel("velocity(m/s)")
    # plt.plot(d, v, '.')
    # plt.savefig('../image/d-v/{}.png'.format(por))





if __name__=='__main__':
    draw_dv(0.1)