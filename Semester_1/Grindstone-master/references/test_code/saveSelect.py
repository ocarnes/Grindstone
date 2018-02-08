import maya.cmds as cmds

wholeFish = cmds.ls(geometry = True)

compLen = len(wholeFish)
oldHold = [[0] * 2 for i in range(compLen)]
testHold = [[]] * compLen
typeHold = [[]] * compLen
print oldHold
print oldHold[0]

for i in range(0, compLen):
    oldHold[i][0] = wholeFish[i]
    typeHold[[i][0]] = i
    cmds.select(wholeFish[i])

    if(cmds.selectMode(query = True, object = True)):
        oldHold[i][1] = 'Object'
        
    elif(cmds.selectType(query = True, polymeshVertex = True)):
        oldHold[i][1] = 'Vertex'
   
    elif(cmds.selectType(query = True, polymeshEdge = True)):
        oldHold[i][1] = 'Edge'
        
    elif(cmds.selectType(query = True, polymeshFace = True)):
        oldHold[i][1] = 'Face'
        
    else:
        oldHold[i][1] = 'Other'

print oldHold