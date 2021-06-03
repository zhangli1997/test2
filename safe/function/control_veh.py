'''
 车辆控制功能块
'''
import traci
from function import myGui




class control_veh():
    def __init__(self):
        self.control_pathflag = True
        self.adj_vehflag = True
        self.glostep = 0
        self.lanes0 = []
        self.lanes_a=[]#禁止换道车辆列表
        self.lanes_b=[]#需要恢复换道的车辆的列表
        self.lanechange=0
        self.mainjudge = True

    def cal_spacing(self, LB, V0):
        '''
        计算车队间距L2   控制区域
        :param LB:第一个探测点与主道的距离
        :param V0:后编队与匝道的受控车的车速
        :return:
        '''

        veh_list=traci.lane.getLastStepVehicleIDs('dtoD_0')
        # v0=traci.vehicle.getSpeed(veh_list[len(veh_list)-1])
        v_last= traci.vehicle.getSpeed(veh_list[0])
        L0=traci.vehicle.getDrivingDistance2D(veh_list[0],traci.vehicle.getPosition(veh_list[1])[0],traci.vehicle.getPosition(veh_list[1])[1])
        print("车队的长度",L0)
        t2=(LB+L0)/v_last+3
        L2=V0*t2
        return L2

    def control_path(self, V0):
        '''
        控制匝道上的车辆减速，受控车辆变色
        :param V0:受控车速
        :return:
        '''
        if self.control_pathflag:
            lanes1=list(traci.lane.getLastStepVehicleIDs('dtoD_0'))
            traci.vehicle.setSpeed(str(lanes1[len(lanes1) - 1]), V0)
            traci.vehicle.setColor(str(lanes1[len(lanes1) - 1]), (0, 255, 0))
            self.control_pathflag = False
    def select_veh(self,lanes0): # 选中三辆车的在一列上
        '''
        选择受控车辆
        :param lanes0:
        :return:
        '''
        lane_list=['CtoD_0','CtoD_1','CtoD_2']
        veh_name=lanes0[0]+lanes0[1]+lanes0[2]
        n=len(veh_name)
        for i in range(n):
            for j in range(0, n - i - 1):
                if traci.vehicle.getPosition(veh_name[j])[0] > traci.vehicle.getPosition(veh_name[j + 1])[0]:
                    veh_name[j], veh_name[j + 1] = veh_name[j + 1], veh_name[j]
        lane_list.remove(traci.vehicle.getLaneID(veh_name[n - 1]))
        if traci.vehicle.getLaneID(veh_name[n - 2]) in lane_list:
            lane_list.remove(traci.vehicle.getLaneID(veh_name[n - 2]))
        else:
            if lane_list[0]=='CtoD_0':
                lane1=0
            elif lane_list[0]=='CtoD_1':
                lane1 = 1
            elif lane_list[0]=='CtoD_2':
                lane1 = 2
            traci.vehicle.changeLane(veh_name[n-2],lane1,20)
            lane=lane_list[0]
            lane_list.remove(lane)
        if traci.vehicle.getLaneID(veh_name[n - 3]) in lane_list:
            pass
        else:
            if lane_list[0]=='CtoD_0':
                lane2=0
            elif lane_list[0]=='CtoD_1':
                lane2 = 1
            elif lane_list[0]=='CtoD_2':
                lane2 = 2
            traci.vehicle.changeLane(veh_name[n-3],lane2,20)
        vehs=[]
        vehs.append(veh_name[n-1])
        vehs.append(veh_name[n-2])
        vehs.append(veh_name[n-3])
        for veh in vehs:
            traci.vehicle.setColor(veh,(0,255,100))
        return vehs

    def select_controlveh(self, L2): #
        '''
        随机选取主道上的受控车辆，选择范围内的车辆变为蓝色
        :param L2:后编队大概开始减速位置
        :return:
        '''
        print(self.lanes0)
        i = 0
        self.lanes0.append(list(traci.lane.getLastStepVehicleIDs('BtoC_0')+traci.lane.getLastStepVehicleIDs('CtoD_0')+traci.lane.getLastStepVehicleIDs('DtoE_0')))
        self.lanes0.append(list(traci.lane.getLastStepVehicleIDs('BtoC_1')+traci.lane.getLastStepVehicleIDs('CtoD_1')+traci.lane.getLastStepVehicleIDs('DtoE_1')))
        self.lanes0.append(list(traci.lane.getLastStepVehicleIDs('BtoC_2')+traci.lane.getLastStepVehicleIDs('CtoD_2')+traci.lane.getLastStepVehicleIDs('DtoE_2')))
        print('车道选车', self.lanes0)
        lanes1 = []
        while i < 3:
            lanes1.append(self.lanes0[i].copy())
            i += 1
        i = 0
        while i < len(lanes1[0]):
            if traci.vehicle.getDrivingDistance2D(lanes1[0][i],954.88,469.55) > (L2+750) or \
                    traci.vehicle.getDrivingDistance2D(lanes1[0][i], 954.88, 469.55) < (L2+20) :   ##匝道口
                self.lanes0[0].remove(lanes1[0][i])
            i += 1
        i = 0
        while i < len(lanes1[1]):
            if traci.vehicle.getDrivingDistance2D(lanes1[1][i],954.88,469.55) > (L2+750) or \
                    traci.vehicle.getDrivingDistance2D(lanes1[1][i], 954.88, 469.55) < (L2+50):
                self.lanes0[1].remove(lanes1[1][i])
            i += 1
        i = 0
        while i < len(lanes1[2]):
            if traci.vehicle.getDrivingDistance2D(lanes1[2][i],954.88,469.55) > (L2+750) or \
                    traci.vehicle.getDrivingDistance2D(lanes1[2][i],954.88,469.55) < (L2+50):
                self.lanes0[2].remove(lanes1[2][i])
            i += 1
        print('距离筛选', self.lanes0)
        i = 0
        # print(len(lanes0),'---------------------')
        # #检测受控车辆
        lanes2=[]
        while i < 3:
            lanes2.append(self.lanes0[i].copy())
            i += 1
        i = 0
        while i < len(lanes2[0]):
            if traci.vehicle.getTypeID(lanes2[0][i])=="type_h":
                self.lanes0[0].remove(lanes2[0][i])
            i += 1
        i = 0
        while i < len(lanes2[1]):
            if traci.vehicle.getTypeID(lanes2[1][i])=="type_h":
                self.lanes0[1].remove(lanes2[1][i])
            i += 1
        i = 0
        while i < len(lanes2[2]):
            if traci.vehicle.getTypeID(lanes2[2][i])=="type_h":
                self.lanes0[2].remove(lanes2[2][i])
            i += 1
        print('车型筛选', self.lanes0)
        # for veh_blue in lanes0[0] + lanes0[1] + lanes0[2]:
        #     traci.vehicle.setColor(veh_blue, (255, 0, 255))
        # veh_name=self.select_veh(lanes0)
        # lanes0=[]
        veh_name=[]
        veh_name.append(self.lanes0[0][len(self.lanes0[0])-1])
        veh_name.append(self.lanes0[1][len(self.lanes0[1]) - 1])
        print('++++++++++++',self.lanes0[2])
        veh_name.append(self.lanes0[2][len(self.lanes0[2]) - 1])
        return  veh_name

    def select_controlveh_singlelane(self, L2): #
        print(self.lanes0)
        i = 0
        self.lanes0.append(list(traci.lane.getLastStepVehicleIDs('BtoC_0') + traci.lane.getLastStepVehicleIDs(
            'CtoD_0') + traci.lane.getLastStepVehicleIDs('DtoE_0')))
        self.lanes0.append(list(traci.lane.getLastStepVehicleIDs('BtoC_1') + traci.lane.getLastStepVehicleIDs(
            'CtoD_1') + traci.lane.getLastStepVehicleIDs('DtoE_1')))
        self.lanes0.append(list(traci.lane.getLastStepVehicleIDs('BtoC_2') + traci.lane.getLastStepVehicleIDs(
            'CtoD_2') + traci.lane.getLastStepVehicleIDs('DtoE_2')))
        print('车道选车', self.lanes0)
        lanes1 = []
        while i < 3:
            lanes1.append(self.lanes0[i].copy())
            i += 1
        i = 0
        while i < len(lanes1[0]):
            if traci.vehicle.getDrivingDistance2D(lanes1[0][i], 954.88, 469.55) > (L2 + 2050) or \
                    traci.vehicle.getDrivingDistance2D(lanes1[0][i], 954.88, 469.55) < (L2 + 20):  ##匝道口
                self.lanes0[0].remove(lanes1[0][i])
            i += 1
        while i < len(lanes1[1]):
            if traci.vehicle.getDrivingDistance2D(lanes1[1][i], 954.88, 469.55) > (L2 + 2050) or \
                    traci.vehicle.getDrivingDistance2D(lanes1[1][i], 954.88, 469.55) < (L2 + 50):
                self.lanes0[1].remove(lanes1[1][i])
            i += 1
        i = 0
        while i < len(lanes1[2]):
            if traci.vehicle.getDrivingDistance2D(lanes1[2][i], 954.88, 469.55) > (L2 + 2050) or \
                    traci.vehicle.getDrivingDistance2D(lanes1[2][i], 954.88, 469.55) < (L2 + 50):
                self.lanes0[2].remove(lanes1[2][i])
            i += 1
        i = 0
        lanes2 = []
        while i < 3:
            lanes2.append(self.lanes0[i].copy())
            i += 1
        i = 0
        while i < len(lanes2[0]):
            if traci.vehicle.getTypeID(lanes2[0][i]) == "type_h":
                self.lanes0[0].remove(lanes2[0][i])
            i += 1
        i = 0
        while i < len(lanes2[1]):
            if traci.vehicle.getTypeID(lanes2[1][i]) == "type_h":
                self.lanes0[1].remove(lanes2[1][i])
            i += 1
        i = 0
        veh_name = []
        veh_name.append(self.lanes0[0][len(self.lanes0[0]) - 1])
        self.lanechange=traci.vehicle.getLaneChangeMode(self.lanes0[0][len(self.lanes0[0]) - 1])
        traci.vehicle.setLaneChangeMode(self.lanes0[0][len(self.lanes0[0]) - 1],0b000000000000)
        return veh_name

    def ban_changelane(self, L2):
        self.lanes_a.append(list(traci.lane.getLastStepVehicleIDs('BtoC_1') + traci.lane.getLastStepVehicleIDs(
            'CtoD_1') + traci.lane.getLastStepVehicleIDs('DtoE_1')))
        self.lanes_a.append(list(traci.lane.getLastStepVehicleIDs('BtoC_2') + traci.lane.getLastStepVehicleIDs(
            'CtoD_2') + traci.lane.getLastStepVehicleIDs('DtoE_2')))
        for veh in self.lanes_a[0]+self.lanes_a[1]:
            if traci.vehicle.getDrivingDistance2D(veh, 954.88, 469.55) > (L2) and traci.vehicle.getDrivingDistance2D(veh, 954.88, 469.55) < (L2+500):
                traci.vehicle.setLaneChangeMode(veh,0b000000000000)
                self.lanes_b.append(veh)
                traci.vehicle.setColor(veh,(255,0,0))
        return 0
    def huifu_changelane(self):
        lanechange=self.lanechange
        print('lanechange',lanechange)
        for veh_b in self.lanes_b:
            traci.vehicle.setLaneChangeMode(veh_b, lanechange)
            traci.vehicle.setColor(veh_b, (0, 0, 255))

    def init_canshu(self):
        self.control_pathflag = True
        self.adj_vehflag = True
        self.glostep = 0
        self.lanes0 = []
        self.lanes_a = []  # 禁止换道车辆列表
        self.lanes_b = []  # 需要恢复换道的车辆的列表
        self.lanechange = 0
        self.mainjudge = True



    def adj_veh(self,veh_name,V0):
        '''
        调节车速使受控车辆处于一起（调节过程中未绿色，三辆车调节好后变为红色）
        :param veh_name:随机选中的车辆
        :param V0: 设置后编队的低速度
        :return:
        '''
        if self.adj_vehflag:
            n=len(veh_name)
            for i in range(n):
                for j in range(0,n-i-1):
                    if traci.vehicle.getPosition(veh_name[j])[0] > traci.vehicle.getPosition(veh_name[j+1])[0]:
                        veh_name[j],veh_name[j+1]=veh_name[j+1],veh_name[j]
            if traci.vehicle.getPosition(veh_name[2])[0]-traci.vehicle.getPosition(veh_name[0])[0]<10 and traci.vehicle.getPosition(veh_name[2])[0]-traci.vehicle.getPosition(veh_name[1])[0]<10:
                for veh in veh_name:
                    traci.vehicle.setSpeed(veh,V0)
                    traci.vehicle.setColor(veh,(0,150,155))
                    self.adj_vehflag=False
            else:
                traci.vehicle.setSpeed(veh_name[0], V0+5)
                traci.vehicle.setSpeed(veh_name[1], V0+3)
                traci.vehicle.setSpeed(veh_name[2], V0)
                for veh in veh_name:
                    traci.vehicle.setColor(veh,(0,255,0))


    def restore_veh(self,veh_name):
        '''
        恢复车速
        :param veh_name: 随机选中的三辆受控车（每个车道一辆）
        :return:
        '''
        for veh in veh_name:
            traci.vehicle.setSpeed(veh, 30)
            traci.vehicle.setColor(veh, (0, 255, 0))   #选中的车辆恢复速度后变为绿色
            traci.vehicle.setSpeed('z' + '0',30)
    def addVeh(self, step, numbers):
        '''
        利用图形化界面增加车辆
        :param step:
        :param numbers:
        :return:
        '''
        if myGui.guijudge:
            if step == int(myGui.step) * 10:
                for i in range(0, numbers):
                    traci.vehicle.add(myGui.vehname + '{}'.format(i), routeID='route_0', typeID="human",departSpeed='max',
                                      departLane='random')

                myGui.guijudge = False

    def addVeh_console(self,step,addstep,name,numbers):
        '''
        非图形化界面增加车辆
        :param step: 仿真时间
        :param addstep: 增加车辆的时间
        :param name: 车辆的名字（尽量别改）
        :param numbers: 车辆数
        :return:
        '''
        if self.mainjudge:
            if step == int(addstep) * 10:
                for i in range(0, numbers):
                    traci.vehicle.add(name+ '{}'.format(i), routeID='route_0', typeID="human",departSpeed='max',
                                      departLane='random')

                    self.mainjudge = True