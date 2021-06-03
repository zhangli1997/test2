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
def cejuli():
    lanes_d2e=traci.lane.getLastStepVehicleIDs('DtoE_0')+traci.lane.getLastStepVehicleIDs('DtoE_1')+traci.lane.getLastStepVehicleIDs('DtoE_2')
    veh0=lanes_d2e[2]
    veh_zadao='z0'
    for veh in lanes_d2e:
        if traci.vehicle.getPosition(veh)[0]< traci.vehicle.getPosition(veh0)[0] and (traci.vehicle.getTypeID(veh)!='human'):
            veh0=veh
        if traci.vehicle.getPosition(veh)[0] > traci.vehicle.getPosition(veh_zadao)[0] and (traci.vehicle.getTypeID(veh) == 'human'):
            veh_zadao=veh
    juli=traci.vehicle.getDrivingDistance2D(veh_zadao,traci.vehicle.getPosition(veh0)[0],traci.vehicle.getPosition(veh0)[1])
    print(traci.vehicle.getPosition(veh_zadao),traci.vehicle.getPosition(veh0),veh0)
    return juli



class sumoSim():
    def sumoSimulation(self,VO,DCC):
        '''
        仿真
        :return:
        '''
        sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        setUpSimulation("../maps/intersection/circle.sumocfg")
        step=0
        changeflag = True
        veh_num = []
        veh_con=[]
        mycon = control_veh()
        LB=100

        Dcc=DCC   #设置后编队的减速度
        Vo=VO   #车辆最低速

        with open(r'../temporarydata/space_time/time1.csv', 'w') as f:
            pass
        while step <4000:
            traci.simulationStep()
            if step==1000:
                veh_con=mycon.select_controlveh(50)   #50是后编队大概开始减速位置
                for v in veh_con:
                    traci.vehicle.setDecel(v,Dcc) #设置后编队的减速度
            if step>1000 and step<1600:
                mycon.adj_veh(veh_con, Vo) #设置后编队的最低速度
            if step==1600:
                for v in veh_con:
                    traci.vehicle.setSpeed(v, 17)
            if step>=10:
                with open(r'../temporarydata/space_time/time1.csv', 'a') as f1:
                    for veh1 in traci.lane.getLastStepVehicleIDs('BtoC_0')+traci.lane.getLastStepVehicleIDs('CtoD_0')+traci.lane.getLastStepVehicleIDs('DtoE_0'):
                        if traci.vehicle.getDrivingDistance2D(veh1,1481.63,301.13)>=100 and traci.vehicle.getDrivingDistance2D(veh1,1481.63,301.13)<=1482 :
                            f1.write(veh1)
                            f1.write(',')
                            f1.write(str(step / 10))
                            f1.write(',')
                            f1.write(str(round(traci.vehicle.getSpeed(veh1), 2)))
                            f1.write(',')
                            f1.write(str(round(1582.01-traci.vehicle.getDrivingDistance2D(veh1,1481.63,301.13), 2)))
                            f1.write('\n')

            # if len(veh_con)== 0:
            #     print('list is empty')
            # else:
            #     print('步数', step)
            #     for q in veh_con:
            #         print("速度",traci.vehicle.getSpeed(q))
            #         print("加速度",traci.vehicle.getAccel(q))
            #         print("减速度",traci.vehicle.getDecel(q))
            # try:
            #     print('步数', step)
            #     for q in veh_con:
            #         print("速度",traci.vehicle.getSpeed(q))
            #         print("加速度",traci.vehicle.getAccel(q))
            #         print("减速度",traci.vehicle.getDecel(q))
            # except traci.exceptions.TraCIException:
            #     print("0")



            step += 1
        traci.close()
if __name__=='__main__':
    x=[]
    y=[]
    sim_num=1
    # por_list=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    with open('../temporarydata/ssm/ssm.csv', 'w') as f:
        pass
    por=1
    Dcc_list=[0.5,1.0,1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    Vo_list=[2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0,12.5,13.0,13.5,14.0,14.5,15.0,15.5,16.0,16.5]  # 车辆最低速
    for Dcc in Dcc_list:
        for Vo in Vo_list:
            cal_test.write_route(float(por))
            i = 0
            while i<sim_num:
                sumosim = sumoSim()
                sumosim.sumoSimulation(Vo,Dcc)  #速度，减速度
                cal_test.write_ttc(Vo, Dcc, cal_test.count_ttc())
                i+=1
    # Vo=5.0
    # Dcc = 0.5  # 设置后编队的减速度
    # cal_test.write_route(float(por))
    # sumosim = sumoSim()
    # sumosim.sumoSimulation(Vo,Dcc)  #速度，减速度
    # cal_test.write_ttc(Vo, Dcc, cal_test.count_ttc())


    #     draw_3D(por)
    #
    #
    # with open('../temporarydata/ssm/ssm.csv', 'r') as f:
    #     text_all=f.readlines()
    #     for text in text_all:
    #         x.append(float(text.split(',')[0]))
    #         y.append(float(text.split(',')[1]))
    #     draw_2D(x,y)