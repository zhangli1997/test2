'''
  路由文件编辑函数
'''
import numpy as np
def create_rou(vNum,times):
    with open('../maps/intersection/circle.rou.xml', 'w') as routes:
        routes.write("""<routes>""" + '\n')
        routes.write('\n')
        routes.write(
            """    <vTypeDistribution id="typedist1">""" + '\n')
        routes.write(
            """        <vType id="type_h"  accel="2.9" decel="7.5"  maxSpeed="22.22" minGap="2.5"  carFollowModel="IDM" tau="1.5" lcSpeedGain="3.1" lcAssertive="3.4" speedFactor="normc(1,0.1,0.2,2)" speedDev="0.5" color="255,0,0" probability="0.5">""" + '\n')
        routes.write(
            """            <param key="initialAwareness" value="1.1"/>""" + '\n')
        routes.write(
            """            <param key="errorTimeScaleCoefficient" value="100"/>""" + '\n')
        routes.write(
            """            <param key="errorNoiseIntensityCoefficient" value="0.5"/>""" + '\n')
        routes.write(
            """            <param key="speedDifferenceErrorCoefficient" value="1"/>""" + '\n')
        routes.write(
            """            <param key="headwayErrorCoefficient" value="4"/>""" + '\n')
        routes.write(
            """            <param key="speedDifferenceChangePerceptionThreshold" value="1"/>""" + '\n')
        routes.write(
            """            <param key="headwayChangePerceptionThreshold " value="1"/>""" + '\n')
        routes.write(
            """        </vType>""" + '\n')
        routes.write(
            """       <vType id="type_a" accel="2.9" decel="7.5"  maxSpeed="22.22" minGap="2.5"  carFollowModel="IDM" tau="1.5" lcSpeedGain="3.1" lcAssertive="3.4" speedFactor="normc(1,0.1,0.2,2)" speedDev="0.1" color="0,0,255" probability="0.5"/>""" + '\n')
        routes.write(
            """    </vTypeDistribution>""" + '\n')
        routes.write(
            """    <route id="route_0" edges="dtoD DtoE" color="yellow" />""" + '\n')
        routes.write(
            """    <vType id="human" vClass="passenger" accel="2.5" decel="7.5" sigma="0.5" tau="1.2" minGap="2.5" lcCooperative="0.5" lcSpeedGainLookahead="0.5" />""" + '\n')
        routes.write('\n')
        routes.write("""    <route id='1' edges="BtoC CtoD DtoE">""" + '\n')
        routes.write("""        <param key="has.ssm.device" value="true"/>""" + '\n')
        routes.write("""        <param key="device.ssm.measures" value="TTC DRAC"/>""" + '\n')
        routes.write("""        <param key="device.ssm.thresholds" value="3.0 3.0"/>""" + '\n')
        routes.write("""        <param key="device.ssm.range" value="50.0" />""" + '\n')
        routes.write("""        <param key="device.ssm.extratime" value="5.0" />""" + '\n')
        routes.write("""        <param key="device.ssm.file" value="../../output/ssm_v0.xml" />""" + '\n')
        routes.write("""        <param key="device.ssm.trajectories" value="true" />""" + '\n')
        routes.write("""        <param key="device.ssm.geo" value="false" />""" + '\n')
        routes.write("""        <param key="device.ssm.filter-edges.input-file" value="input_list.txt" />""" + '\n')
        routes.write("""    </route>""" + '\n')
        dtime = np.random.uniform(0, times, size=(int(vNum),))
        dtime.sort()
        for veh in range(int(vNum)):
            routes.write("""    <vehicle id=\"""" + str(veh) + """\" depart=\"""" + str(round(dtime[veh], 2)) + """\" type=\"""" + "typedist1" + """\" route=\"""" + "1" + """\" departLane=\""""'random'"""\""""+""" departPos=\""""'base'"""\"""" +""" departSpeed=\""""'random'"""\">"""+ '\n')
            routes.write("""        <param key="has.ssm.device" value="true"/>""" + '\n')
            routes.write("""        <param key="device.ssm.measures" value="TTC DRAC"/>""" + '\n')
            routes.write("""        <param key="device.ssm.thresholds" value="3.0 3.0"/>""" + '\n')
            routes.write("""        <param key="device.ssm.range" value="50.0" />""" + '\n')
            routes.write("""        <param key="device.ssm.extratime" value="5.0" />""" + '\n')
            routes.write("""        <param key="device.ssm.file" value="../../output/ssm_v0.xml" />""" + '\n')
            routes.write("""        <param key="device.ssm.trajectories" value="true" />""" + '\n')
            routes.write("""        <param key="device.ssm.geo" value="false" />""" + '\n')
            routes.write("""        <param key="device.ssm.filter-edges.input-file" value="input_list.txt" />""" + '\n')
            routes.write("""    </vehicle>""" + '\n')
            routes.write('\n')
        routes.write("""</routes>""")
if __name__=='__main__':
    create_rou(60000,3600) #(vNum,times)