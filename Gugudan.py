listMatrix = []
for i in [1,2,3,4,5,6,7,8]:
    line = []
    for j in [1,2,3,4,5,6,7,8,9]:
        line.append(str(i * j).center(5))
    listMatrix.append(line)

for i in [0,1,2,3,4,5,6,7]:
    print(listMatrix[i])