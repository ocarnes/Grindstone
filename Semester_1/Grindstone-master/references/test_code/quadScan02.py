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
compLen = len(userSel)

faceHold= cmds.polyListComponentConversion(polyHold, toFace=True)
#print oldHold

# Setting the selection type to look for faces and selecting them
#cmds.selectType(polymeshFace = True)
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

cmds.selectType(allObjects = True)


print triHold
print triCount

print quadHold
print quadCount

print nGonHold
print nGonCount

#cmds.select(clear = True)
#cmds.hilite(cmds.ls(), unHilite = True)
cmds.hilite(userHil)
cmds.select(userSel + triHold)