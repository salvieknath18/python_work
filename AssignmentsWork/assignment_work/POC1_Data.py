InfyData = open(r'C:\Python27\NSE-INFY.csv','r')

#content = InfyData.read();
cnt = 1
yrList = list()
for line in InfyData.readlines():
    if line.startswith('Date'):
        continue
    if 
    yrList.append((line.split(',')[0]).split('-')[0])
    
    if cnt == 20:
        break
    cnt += 1
