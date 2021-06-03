import re
def extract_data():
    lanes=['BtoC','CtoD','DtoE']
    density=[]
    speed=[]
    with open(r'../output/edgedataOutput.xml','r') as f:
        textall=f.readlines()
        for text in textall:
            text1=text
            text2 = text
            text3 = text
            if re.search('BtoC',text1):
                text1=text1.split(' ')
                for t in text1:
                    if re.search('density',t):
                        #print(re.findall(r"\d+\.?\d*",t))
                        density.append(re.findall(r"\d+\.?\d*",t)[0])
                    if re.search('speed',t):
                        #print(re.findall(r"\d+\.?\d*",t))
                        speed.append(re.findall(r"\d+\.?\d*",t)[0])
            if re.search('CtoD',text2):
                text2=text2.split(' ')
                for t in text2:
                    if re.search('density',t):
                        density.append(re.findall(r"\d+\.?\d*",t)[0])
                    if re.search('speed',t):
                        speed.append(re.findall(r"\d+\.?\d*",t)[0])
            if re.search('DtoE',text3):
                text3=text3.split(' ')
                for t in text3:
                    if re.search('density',t):
                        density.append(re.findall(r"\d+\.?\d*",t)[0])
                    if re.search('speed',t):
                        speed.append(re.findall(r"\d+\.?\d*",t)[0])
    #print(density)
    with open(r'../temporarydata/edgeoutput/d_v.txt','w') as f:
        i=0
        while i<len(density):
            f.write(density[i])
            f.write(',')
            f.write(speed[i])
            f.write('\n')
            i+=1
if __name__=="__main__":
    extract_data()