import maya.cmds as cmds

sel = cmds.ls(sl=1)

for node in sel:
    history = cmds.ls(history, long=True)
    deformHistory = set(cmds.ls(history, long=True, type="geometryFilter"))
    nonDeformHistory = [node for node in history if node not in deformHistory]
    print 'nonDeformHistory', nonDeformHistory
    

