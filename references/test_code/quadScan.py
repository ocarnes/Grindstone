import maya.cmds as cmds

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

oldHold = cmds.ls(selection = True)

cmds.selectMode(co =True)

# Creating lists of all geometry in the scene and then all of its faces
polyHold = cmds.ls(geometry=True)
faceHold= cmds.polyListComponentConversion(polyHold, tf=True)

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

cmds.polySelectConstraint(sz = 0)

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
cmds.selectMode(co = False)
cmds.select(oldHold)

'''cmds.select(nGonHold)
print triHold
print quadHold
print nGonHold'''
print triHold
print triCount

print quadHold
print quadCount

print nGonHold
print nGonCount