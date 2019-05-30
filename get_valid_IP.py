import linecache

f = open(r"initialProcessing",'r')
#g = open("initialProcessing",'w')
#g.close()
#g = open("Local_valid_IP",'a')


def writeValidIP(lineNum):
    print(lineNum)
    validIP_file = open("Local_valid_IP",'a')
    
    #for i in range(lineNum-1):
        #line = g.readline()
    line = linecache.getline('initialProcessing', lineNum-1)
    validIP_file.write(line)
    validIP_file.close()
 

lineNum = 0
while 1:
    lineNum = lineNum + 1
    line = f.readline()
    #print(line[35:37])
    if line[35:37] == '0%':
        #print(lineNum)
        writeValidIP(lineNum)
    if not line:
        break
    pass
f.close()

