'''
  潜在冲突图
'''
import matplotlib.pyplot as plt
import time

def draw_2D(x,y):
    plt.figure(figsize=(10, 4))
    plt.ylim(ymin=0,ymax=1000)
    plt.xlim(xmin=0,xmax=1)
    plt.plot(x,y,'*-')
    plt.text(-0.04, 6, 'nums of conflict', ha='right', rotation=90)
    plt.text(0.5, -1, 'porprotion', ha='center')
    plt.savefig('../image/conflict/conflict_{}.png'.format(time.strftime("%m-%d_%H-%M-%S",time.localtime())))
    plt.show()

if __name__=='__main__':
    x=[]
    y=[]
    with open('../output/ssm.csv', 'r') as f:
        text_all=f.readlines()
        for text in text_all:
            x.append(float(text.split(',')[0]))
            y.append(float(text.split(',')[1]))
        print(x)
        print(y)
    draw_2D(x,y)