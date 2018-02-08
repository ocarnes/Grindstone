import maya.cmds as mc

sel = mc.ls(sl=1)

for node in sel:
    history = mc.listHistory(node) or []

print 'history', history
deformHistory = mc.ls(history, type="geometryFilter", long=True)
print 'deformHistory', deformHistory