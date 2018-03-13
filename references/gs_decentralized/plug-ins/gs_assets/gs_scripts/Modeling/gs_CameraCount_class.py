# Grindstone gs_CameraCount_class.py
# Authors: Sam Carnes and Sean Adams

# This file defines a script that checks that the number of cameras is not greater than 4


import maya.cmds as cmds

class CameraCount:
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = True

        # identify what this check is called
        self.scriptName = "Camera count"
        
        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = "Delete extra cameras"
        
        
        # class data
        self.cameraList = []
        self. numberOfCameras = 4
       
        
        
    #********** DO CHECK **********#
    
    def doCheck(self):
        
        # get the list of cameras
        self.cameraList = cmds.listCameras()
        
        # determine how many cameras there are
        self.numberOfCameras = len(self.cameraList)
        
        if self.numberOfCameras > 4:
            returnString = str(self.numberOfCameras) + " cameras detected, should have 4."
            return returnString
            
        else:
            return ''
            
    
    
    #********** RUN FIX **********#
    
    # deletes any cameras that are not the default front, persp, side, or top cameras
    def runFix(self):
        
        # try the fix
        try:
            
            # delete the excess cameras
            for cam in self.cameraList:
                if cam != "front" and cam != "persp" and cam != "side" and cam != "top":
                    cmds.delete(cam)
        
            # determine how many excess cameras there were
            excessCameras = self.numberOfCameras - 4
            
            # determine if there "was an excess camera" or "were excess cameras"
            if excessCameras > 1:
                pluralOrSingular = "cameras"
            else:
                pluralOrSingular = "camera"
                
            # return the result
            return str(self.numberOfCameras - 4) + " excess " + pluralOrSingular + " deleted."
            
        # if the fix doesn't work, return an error message
        except:
            
            return "There was a problem deleteing the excess cameras."
        
        
        
#********** RETURN INSTANCE OF SCRIPT CLASS **********#
        
def getObject():
    return CameraCount()