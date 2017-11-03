import maya.cmds as cmds

print cmds.bakePartialHistory('pCube1', q=1, prePostDeformers=True, preDeformers=False, postSmooth=False, preCache=False)