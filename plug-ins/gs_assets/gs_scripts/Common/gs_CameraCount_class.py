# Grindstone gs_CameraCount_class.py
# Authors: Sam Carnes and Sean Adams

# This file defines a script that checks that the number of cameras is not greater than 4


import maya.cmds as cmds

class CameraCount:
    
    
    def __init__(self):
        self.hasFix = True
       
        
    def doCheck(self):
        
        # get the list of cameras
        cameraList = cmds.listCameras()
        
        if len(cameraList) > 4:
            returnString = str(len(cameraList)) + " cameras detected, should have 4."
            return returnString
            
        else:
            return ''
            
            
    def runFix(self):
        return "Camera fix!"
        
        
def getObject():
    return CameraCount()