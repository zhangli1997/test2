'''
  时空图仿真函数
'''
import os
from function import cal_test
from function.control_veh import control_veh
import sys
import traci
from function.simlib import setUpSimulation
from function.draw_3D import draw_3D
from function.draw_2D import draw_2D

class sumoSim():
    def sumoSimulation(self):
        '''
        仿真
        :return:
        '''
        sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        setUpSimulation("../maps/intersection_outcontrol/circle.sumocfg")
        step=0
        mycon = control_veh()
        with open(r'../temporarydata/space_time/time1.csv', 'w') as f:
            pass
        while step <3000:
            traci.simulationStep()

            for i in range(1, 300):
                if i % 100 == 0:
                    # print(i)
                    mycon.addVeh_console(step, i, 'a{}'.format(i), 2)  # 非图形化界面增加车辆

            step += 1
        traci.close()


if __name__=='__main__':
    x=[]
    y=[]
    sim_num=1
    with open('../temporarydata/ssm/ssm.csv', 'w') as f:
        pass
    for por in [0.0,0.2,0.4,0.6,0.8,1.0]:
        cal_test.write_route(float(por))
        i = 0
        while i < sim_num:
            sumosim = sumoSim()
            sumosim.sumoSimulation()
            cal_test.write_ttc_time(por, cal_test.count_ttc(), cal_test.count_duration())
            i += 1
        # draw_3D(por)
    with open('../temporarydata/ssm/ssm.csv', 'r') as f:
        text_all=f.readlines()
        for text in text_all:
            x.append(float(text.split(',')[0]))
            y.append(float(text.split(',')[1]))
    # draw_2D(x,y)

