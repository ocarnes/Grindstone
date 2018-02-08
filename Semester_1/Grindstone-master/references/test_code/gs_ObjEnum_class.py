# Grindstone gs_ObjEnum_class.py
# Authors: Sam Carnes and Sean Adams

# This file scans assets of a generic Maya scene file and returns the count of
# objects it finds in each asset

# NOTE: Objects with deformers that contain nodes of their original shapes are
# considered additional meshes by the enumerator

import maya.cmds as cmds

class ObjEnum:
    
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = False
        
        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = ""
    
    
    
    def doCheck(self):
        
        # Create an empty array for holding each target node found
        sceneScan = [[0 for x in range(2)] for y in range(10)]
        # Array for carrying existing results
        countHold = []
        foundHold = []
        fndMax = 0
        plural = 's'
        formString = ''
        # String to be returned
        enumReport = "This scene has "
        
        # Array for nodes associated with animation
        sceneScan[0][0] = "animation"
        sceneScan[0][1] = cmds.listNodeTypes("animation")
        
        # Array for nodes associated with cameras
        sceneScan[1][0] = "camera"
        sceneScan[1][1] = cmds.listNodeTypes("camera")
        
        # Array for nodes associated with deformers
        sceneScan[2][0] = "deformer"
        sceneScan[2][1] = cmds.listNodeTypes("deformer")
        
        # Array for nodes associated with dynamics
        sceneScan[3][0] = "dynamic"
        sceneScan[3][1] = cmds.listNodeTypes("dynamics")
        
        # Array for nodes associated with meshes
        sceneScan[4][0] = "geometry"
        sceneScan[4][1] = cmds.listNodeTypes("drawdb/geometry/mesh")
        
        # Array for nodes associated with image planes
        sceneScan[5][0] = "image plane"
        sceneScan[5][1] = cmds.listNodeTypes("imageplane")
        
        # Array for nodes associated with lights
        sceneScan[6][0] = "lighting"
        sceneScan[6][1] = cmds.listNodeTypes("light")
        
        # Array for nodes associated with shaders
        sceneScan[7][0] = "shader"
        sceneScan[7][1] = cmds.listNodeTypes("shader")
        
        # Array for nodes associated with textures
        sceneScan[8][0] = "textures"
        sceneScan[8][1] = cmds.listNodeTypes("texture")
        
        # Array for nodes associated with utilities
        sceneScan[9][0] = "utility"
        sceneScan[9][1] = cmds.listNodeTypes("utility")
        
        
        for i in range(0, 10):
            seenIt = []
            reduction = []
            for clue in sceneScan[i][1]:
                if cmds.ls(type = clue):
                    seenIt.extend(cmds.ls(type=clue))
            reduction = set(seenIt)
            #print len(reduction), sceneScan[i][0]
            if reduction:
                countHold.append(len(reduction))
                foundHold.append(sceneScan[i][0])
        
        fndMax = len(countHold)
        
        for j in range(0, (fndMax - 1)):
            plural = 's'
            formString = ''
            if countHold[j] == 1:
                plural = ''
            formString = str(countHold[j]) + " " + foundHold[j] + " node" + plural + ", "
            enumReport += formString
        
        plural = 's'
        if countHold[fndMax - 1] == 1:
            plural = ''
        
        formString = "and " + str(countHold[fndMax - 1]) + " " + foundHold[fndMax - 1] + " node" + plural + "."
        
        enumReport += formString
        
        return enumReport
        
        
        
#********** RETURN INSTANCE OF SCRIPT CLASS **********#
        
def getObject():
    return ObjEnum()