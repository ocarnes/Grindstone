import maya.cmds as cmds

wholeFish = cmds.ls(geometry = True)

#oldHold = [[]]

compLen = len(wholeFish)
oldHold = [[]] * compLen
testHold = [[]] * compLen
typeHold = [] * compLen
#oldHold = [compLen][]
#print oldHold[0]

for i in range(0, compLen):
    #oldHold[i].insert(0, wholeFish[i])
    oldHold[0].append(None)
    oldHold[0].append(None)
    print 'Check'
    #testHold[i].insert(0, wholeFish[i])
    #print wholeFish[i]
    #print oldHold[i][0]
    #oldHold[i].insert(1, 'Blah')
    cmds.select(wholeFish[i])

    if(cmds.selectMode(query = True, object = True)):
        #oldHold[i][1] = 'Object'
        #oldHold[i].insert(1, 'Object')
        oldHold[i][0] = wholeFish[i]
        oldHold[i][1] = 'Object'
        typeHold[i] = 'Object'
        
    elif(cmds.selectType(query = True, polymeshVertex = True)):
        #oldHold[i][1] = 'Vertex'
        #oldHold[i].insert(1, 'Vertex')
        oldHold[i][0] = wholeFish[i]
        oldHold[i][1] = 'Vertex'
        typeHold[i] = 'Vertex'
   
    elif(cmds.selectType(query = True, polymeshEdge = True)):
        #oldHold[i][1] = 'Edge'
        #oldHold[i].insert(1, 'Edge')
        oldHold[i][0] = wholeFish[i]
        oldHold[i][1] = 'Edge'
        typeHold[i] = 'Edge'
        
    elif(cmds.selectType(query = True, polymeshFace = True)):
        #oldHold[i][1] = 'Face'
        #oldHold[i].insert(1, 'Face')
        oldHold[i][0] = wholeFish[i]
        oldHold[i][1] = 'Face'
        typeHold[i] = 'Face'
        
    else:
        #oldHold[i][1] = 'Other'
        #oldHold[i].insert(1, 'Other')
        oldHold[i][0] = wholeFish[i]
        oldHold[i][1] = 'Other'
        typeHold[i] = 'Other'
    
    print oldHold[i]


# print cmds.selectMode(query = True, object = True)
#print oldHold
print oldHold[0]
#print wholeFish