'''
  时空图仿真函数
'''
import os
from function import cal_test
from function.control_veh import control_veh
# from function.control_veh import init_canshu
import sys
import traci
from function.simlib import setUpSimulation
from function.draw_3D import draw_3D
from function.draw_2D import draw_2D
class sumoSim():
    def sumoSimulation(self,V0):
        '''
        仿真
        :return:
        '''
        sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        setUpSimulation("../maps/intersection/circle.sumocfg")
        step=0
        changeflag = True
        veh_num = []
        huifu_step=0
        mycon = control_veh()
        LB=100
        with open(r'../temporarydata/space_time/time1.csv', 'w') as f:
            pass
        while step <3000:
            traci.simulationStep()
            # veh_num = []
            for i in range(1, 300):
                if i % 102 == 0:
                    # print(i)
                    mycon.addVeh_console(step, i, 'a{}'.format(i), 2)  # 非图形化界面增加车辆
            # mycon.addVeh_console(step, 90, 'z', 2)  # 非图形化界面增加车辆


            if traci.inductionloop.getLastStepVehicleNumber('myloop2' or 'myloop3') and changeflag:
                L2 = mycon.cal_spacing(LB, V0)
                veh_num=mycon.select_controlveh_singlelane(L2)
                mycon.ban_changelane(L2)
                changeflag = False
            if changeflag == False:
                traci.vehicle.setDecel(veh_num[0],2.5)    #AVs车辆减速度
                traci.vehicle.setSpeed(veh_num[0],V0)
                traci.vehicle.setColor(veh_num[0],(125,120,120))
                if traci.lane.getLastStepVehicleNumber('dtoD_0') == 0 and huifu_step==0:
                    huifu_step=step
                if traci.lane.getLastStepVehicleNumber('dtoD_0') == 0:
                    # traci.vehicle.setSpeed(veh_num[0], 20)
                    # traci.vehicle.setDecel(veh_num[0], 7.5)
                    changeflag = True
            if step==int(huifu_step)+50:#恢复换道模型时间
                huifu_step=0
                mycon.huifu_changelane()
                mycon.init_canshu()
            step += 1
        traci.close()


if __name__=='__main__':
    x=[]
    y=[]
    sim_num=1
    with open('../temporarydata/ssm/ssm.csv', 'w') as f:
        pass
    for por in [0.2,0.4,0.6,0.8,1.0]:
        cal_test.write_route(float(por))
        i = 0
        while i < sim_num:
            sumosim = sumoSim()
            sumosim.sumoSimulation(9)
            cal_test.write_ttc_time(por, cal_test.count_ttc(), cal_test.count_duration())
            i += 1
        # draw_3D(por)
    with open('../temporarydata/ssm/ssm.csv', 'r') as f:
        text_all=f.readlines()
        for text in text_all:
            x.append(float(text.split(',')[0]))
            y.append(float(text.split(',')[1]))
    # draw_2D(x,y)

