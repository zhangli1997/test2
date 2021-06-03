'''
  机动车和受控车比例修改函数
'''
import re

def count_ttc():
    num = 0
    with open('../output/ssm_v0.xml','r') as f:
        r_all=f.readlines()
        for r in r_all:
            pattern='minTTC'
            result=re.search(pattern,str(r))
            if result:
                num+=1
    return num

def write_ttc(bili,nell,num):
    with open('../output/ssm.csv','a') as f:
        f.write(str(bili))
        f.write(',')
        f.write(str(nell))
        f.write(',')
        f.write(str(num))
        f.write('\n')

def write_ttc_time(bili,num,finishtime):
    with open('../output/ssm.csv','a') as f:
        f.write(str(bili))
        f.write(',')
        f.write(str(num))
        f.write(',')
        f.write(str(finishtime))
        f.write('\n')



def count_duration():
    durationtime = []
    with open(r'../maps/intersection/tripinfo.xml','r') as m:
        textall = m.readlines()
        for text in textall:
            text=text.split(' ')
            for t in text:
                if re.search('duration=',t):
                    durationtime.append(re.findall(r"\d+\.?\d*",t)[0])
    length=len(durationtime)
    # print(durationtime)
    sum=0
    for t in durationtime:
        sum+=float(t)
    finishtime=round(sum/length,2)
    print(finishtime)
    return finishtime






def write_route(proportion):
    text_all=[]
    with open('../maps/intersection/circle.rou.xml','r') as f:
        text_all=f.readlines()
    text_all[3] = '<vType id="type_h"  accel="7.9" decel="7.5"  maxSpeed="17.00"  carFollowModel="IDM" tau="1.5" lcSpeedGain="3.1" lcAssertive="3.4" speedFactor="normc(1,0.1,0.2,2)" speedDev="0.4" color="128,128,128" probability="{}">\n'.format(1 - float(proportion))
    text_all[12] = '<vType id="type_a" accel="2.9" decel="3.5"  maxSpeed="17.00" carFollowModel="IDM" tau="1.5" lcSpeedGain="1" lcAssertive="1" speedFactor="normc(1,0.1,0.2,2)" speedDev="0.0" color="0,0,255" probability="{}"/>\n'.format(float(proportion))
    with open('../maps/intersection/circle.rou.xml', 'w') as fw:
        for text in text_all:
            fw.write(text)






if __name__=='__main__':
    print(count_ttc())