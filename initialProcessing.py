f = open(r"pingLog",'r')
#g = open("initialProcessing",'w')
#g.close()
g = open("initialProcessing",'a')
m = open(r"pingLog",'r')
lineNum = 0
pingLog = m.read()

while 1:
    lineNum = lineNum + 1
    line = f.readline()
    if line[0:4] == '--- ':
        g.write(line)
    if line[2:9] == 'packets':
        g.write(line)
        g.write('\n')
    if not line:
        break
    pass
f.close()
g.close()

