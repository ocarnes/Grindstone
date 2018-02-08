# Grindstone gs_UVDetect_class.py
# Authors: Sam Carnes and Sean Adams

# This file defines a script that makes sure all geometry has UVs


import maya.cmds as cmds

class UVDetect:
    
    #********** INIT **********#
    
    def __init__(self):
        
        # Identify whether or not the script has an auto-fix function
        self.hasFix = True
        
        # Provide a label for the button that executes the auto-fix
        # CANNOT EXCEED 20 CHARACTERS
        
        self.fixLabel = "Find empty UVs"
        
        # Array for holding any empty UVs following the scan
        
        self.emptyUVs = []
        
    
    
    #********** DO CHECK **********#
    
    def doCheck(self):
        
        # Clean out existing vars to start a new detection
        self.emptyUVs = []
        unMapLim = 0
        unMapCount = 0
        unMapRep = ''
        
        # Array for holding polygons and their faces
        polyHold = cmds.ls(geometry = True)
        faceHold = cmds.polyListComponentConversion(polyHold, tf = True)
        
        # Saving the selection and hilite states
        userHil = cmds.ls(hilite = True)
        userSel = cmds.ls(selection = True)
        
        # Selecting the faces for contraint
        cmds.select(faceHold)
        
        # Constraining the selection to any faces that are unmapped
        cmds.polySelectConstraint(mode = 3, type = 8, textured = 2)
        self.emptyUVs = cmds.ls(selection = True)
        unMapLim = len(self.emptyUVs)
        
        # Clearing out the selections
        cmds.polySelectConstraint(disable = True)
        cmds.select(clear = True)
        
        # Counting up the faces found to be unmapped
        for i in range(0, unMapLim):
            cmds.select(self.emptyUVs[i])
            unMapCount += cmds.polyEvaluate(self.emptyUVs[i], faceComponent = True)
        
        # Restoring the original selection state
        cmds.selectType(allObjects = True)
        cmds.hilite(userHil)
        cmds.select(userSel)
        
        # Determining if any unmapped faces have been found and reporting
        if self.emptyUVs:
            unMapRep = '%d unmapped faces detected.'%(unMapCount)
        
        return unMapRep

    
    #********** RUN FIX **********#
    
    # Hilight any unmapped faces found
    def runFix(self):
        
        try:
            
            # Highlight any unmapped faces
            cmds.select(self.emptyUVs)
            return "Unmapped faces highlighted."
            
        except:
            
            return "There was a problem selecting the unmapped faces"
    
    
    
    #********** RETURN INSTANCE OF SCRIPT CLASS **********#
    
def getObject():
    return UVDetect()