# Grindstone gs_ObjEnum_class.py
# Authors: Sam Carnes and Sean Adams

# This file scans assets of a generic Maya scene file and returns the count of
# objects it finds in each asset

# NOTE: Objects with deformers that contain nodes of their original shapes are
# considered additional meshes by the enumerator

import maya.cmds as cmds

class TexEnum:
    
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = False

        # identify what this check is called
        self.scriptName = "Textures"
        
        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = ""
    
    
    
    def doCheck(self):
        
        # Create an empty array for holding each target node found
        sceneScan = []
        # Array for carrying existing results
        countHold = 0
        foundHold = ''
        fndMax = 0
        plural = 's'
        formString = ''
        # String to be returned
        enumReport = "This scene has "
        
        # Array for nodes associated with textures
        sceneScan = cmds.listNodeTypes("texture")
        
        scanRng = len(sceneScan)
        
        for i in range(0, scanRng):
            seenIt = []
            for clue in sceneScan:
                if cmds.ls(type = clue):
                    seenIt.extend(cmds.ls(type=clue))
        
        reduction = set(seenIt)
        
        if reduction:
            countHold = len(reduction)
        
        if countHold == 1:
            plural = ''
            
        formString = str(countHold) + " texture node" + plural + '.'
        enumReport += formString
        
        if countHold == 0:
            enumReport = ''
        
        return enumReport
        
        
        
#********** RETURN INSTANCE OF SCRIPT CLASS **********#
        
def getObject():
    return TexEnum()