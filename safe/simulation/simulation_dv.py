'''
  时空图仿真函数
'''
import os
from function import cal_test
from function.control_veh import control_veh
import sys
import traci
from function.simlib import setUpSimulation
from function.extract_output import extract_data
from function.draw_dv import draw_dv

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
    def sumoSimulation(self,V0):
        '''
        仿真
        :return:
        '''
        sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        setUpSimulation("../maps/intersection/circle.sumocfg")
        step = 0
        changeflag = True
        veh_num = []
        veh_con = []
        mycon = control_veh()
        LB = 100
        V0 = V0

        while step < 11000:
            traci.simulationStep()
            if step == 2000:
                veh_con = mycon.select_controlveh(50)
            if 2250 < step < 6000:
                mycon.adj_veh(veh_con, 0)
            # if step == 7000:
            #     veh_num = mycon.select_controlveh(20)
            # if 7150< step < 7500:
            #     mycon.adj_veh(veh_num, 0)

            # if step == 6000:
            #     for v in veh_con:
            #         traci.vehicle.setSpeed(v, 22.22)
            step += 1
        traci.close()
if __name__=='__main__':
    x=[]
    y=[]
    sim_num=1

    cal_test.write_route(float(0.5))

    sumosim = sumoSim()
    sumosim.sumoSimulation(5)

    extract_data()
    draw_dv(0.001)
