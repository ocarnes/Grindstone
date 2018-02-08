import maya.cmds as cmds

sel = cmds.ls(dag=True)
errorTag = False
i=0
#Set to cmds.ls(shapes=1) if processing time is too much

for node in sel:
    history = cmds.listHistory(node, il=1, pdo=True) or []
    print i
    i+=1
    #if cmds.nodeType(node) != 'geometryFilter':
        #print i
        #i+=1
    #print 'history', history
    print 'The node: ', node
    print 'Node type: ', cmds.nodeType(node)
    print '\n'
    deformHistory = cmds.ls(history, type="geometryFilter", long=True)
    #print 'deformHistory', deformHistory
    
    
    if deformHistory:
        print cmds.nodeType(node)