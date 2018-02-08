import maya.cmds as cmds

#print cmds.selectType(query = True, polymeshFace = True)

# Setting up vars for tracking and managing the faces found
triHold = []
quadHold = []
nGonHold = []

triCount = 0
quadCount = 0
nGonCount = 0

triLim = 0
quadLim = 0
nGonLim = 0

#cmds.selectMode(co =True)

# Creating lists of all geometry in the scene and then all of its faces
polyHold = cmds.ls(geometry=True)
userHil = cmds.ls(hilite = True)
userSel = cmds.ls(selection = True)


# Vars for restoring selection states post execution
compLen = len(polyHold)
oldHold = [[0] * 2 for i in range(compLen)]

# Loop to store selection states involved
for i in range(0, compLen):
    oldHold[i][0] = polyHold[i]
    cmds.select(polyHold[i])

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

faceHold= cmds.polyListComponentConversion(polyHold, toFace=True)
print oldHold

# Setting the selection type to look for faces and selecting them
cmds.selectType(polymeshFace = True)
cmds.select(faceHold)

# Contraining the selection to triangles and storing the results
cmds.polySelectConstraint(m = 3, t = 8, sz = 1)
triHold = cmds.ls(sl=1)
triLim = len(triHold)

# Quadrilateral constraint
cmds.polySelectConstraint(m = 3, t = 8, sz = 2)
quadHold = cmds.ls(sl = 1)
quadLim = len(quadHold)

# N_Gon constraint
cmds.polySelectConstraint(m = 3, t = 8, sz = 3)
nGonHold = cmds.ls(sl = 1)
nGonLim = len(nGonHold)

#cmds.select()
#cmds.polySelectConstraint(m = 0, t = 0, sz = 0)
cmds.polySelectConstraint(disable = True)
cmds.select(clear = True)
# Iterating through the results to count the amount of faces found
for i in range(0, triLim):
    cmds.select(triHold[i])
    triCount += cmds.polyEvaluate(triHold[i], faceComponent = True)

# Iterating through the results to count the amount of faces found
for i in range(0, quadLim):
    cmds.select(quadHold[i])
    quadCount += cmds.polyEvaluate(quadHold[i], faceComponent = True)



# Iterating through the results to count the amount of faces found
for i in range(0, nGonLim):
    cmds.select(nGonHold[i])
    nGonCount += cmds.polyEvaluate(nGonHold[i], faceComponent = True)



cmds.select(clear = True)
#cmds.changeSelectMode(object=True)
#cmds.selectMode(co = False)
cmds.selectType(allObjects = True, allComponents = True)
#cmds.selectMode(object = True, component = False)
#cmds.select(polyHold)


#cmds.select(userSel)
# Restoring selection states
for i in range(0, compLen):
    #oldHold[i][0] = polyHold[i]
    #cmds.select(polyHold[i])

    if(oldHold[i][1] == 'Object'):
        #oldHold[i][1] = 'Object'
        #cmds.selectMode(object = True)
        cmds.selectType(objectComponent = True)
        
    elif(oldHold[i][1] == 'Vertex'):
        #cmds.polyListComponentConversion(oldHold[i][0], toVertex=True)
        cmds.selectType(polymeshVertex = True)
   
    elif(oldHold[i][1] == 'Edge'):
        #cmds.polyListComponentConversion(oldHold[i][0], toEdge=True)
        cmds.selectType(polymeshEdge = True)
        
    elif(oldHold[i][1] == 'Face'):
        #cmds.polyListComponentConversion(oldHold[i][0], toFace=True)
        cmds.selectType(polymeshFace = True)
        
    else:
        oldHold[i][1] = 'Other'


print triHold
print triCount

print quadHold
print quadCount

print nGonHold
print nGonCount

#cmds.select(clear = True)
cmds.hilite(userHil)
cmds.select(userSel)
#print cmds.selectType(query = True, polymeshFace = True)