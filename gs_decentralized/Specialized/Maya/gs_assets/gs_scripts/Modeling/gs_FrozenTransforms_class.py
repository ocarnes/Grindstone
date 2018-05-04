# Grindstone gs_FrozenTransforms_class.py
# Authors: Sam Carnes and Sean Adams

# This file defines a script that checks for any unfrozen transforms


import maya.cmds as cmds

class FrozenTransforms:
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = True

        # identify what this check is called
        self.scriptName = "Frozen transforms"
        
        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = "Freeze transforms"
        
        
        # class data
        self.transformList = []
        self.cameraList = []
        self.objectsWithUnfrozenTransforms = []
        
       
        
        
    #********** DO CHECK **********#
    
    def doCheck(self):
        
        # get the transform nodes and cameras
        self.transformList = cmds.ls(type = 'transform')
        self.cameraList = cmds.listCameras()
        self.objectsWithUnfrozenTransforms = []

        # for all transform nodes
        for item in self.transformList:
        
            # if the node does not apply to a camera
            if item not in self.cameraList:
        
                # check the translation, rotation, and scale values for the node 
                # and if they are not frozen, add it to the unfrozen list
                
                if cmds.xform(item, query=True, translation=True) != [0, 0, 0]:
                    self.objectsWithUnfrozenTransforms.append(item)
            
                elif cmds.xform(item, query=True, rotation=True) != [0, 0, 0]:
                    self.objectsWithUnfrozenTransforms.append(item)
            
                elif cmds.xform(item, query=True, relative=True, scale=True) != [1, 1, 1]:
                    self.objectsWithUnfrozenTransforms.append(item)
            
            
        #print self.objectsWithUnfrozenTransforms
        
        if len(self.objectsWithUnfrozenTransforms) > 0:
            if len(self.objectsWithUnfrozenTransforms) > 1:
                singularOrPlural = "objects"
                
            else:
                singularOrPlural = "object"
            
            returnString = str(len(self.objectsWithUnfrozenTransforms)) + " " + singularOrPlural + " with unfrozen transforms detected."
            return returnString
            
        else:
            return ''
    
    
    
    
    #********** RUN FIX **********#
    
    # freezes transforms
    def runFix(self):
        
        # try the fix
        try:
            
            # freeze the transforms on the unfrozen nodes
            cmds.makeIdentity(self.objectsWithUnfrozenTransforms, apply=True, t=1, r=1, s=1, n=0, pn=1)
            
            
            # return the result
            return "Transforms frozen."
            
        # if the fix doesn't work, return an error message
        except:
            
            return "There was a problem freezing transforms."
        
        
        
#********** RETURN INSTANCE OF SCRIPT CLASS **********#
        
def getObject():
    return FrozenTransforms()