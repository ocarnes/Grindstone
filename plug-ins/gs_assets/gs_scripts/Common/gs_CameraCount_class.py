import maya.cmds as cmds

class CameraCount:
    
    
    def __init__(self):
        pass
       
        
    def doCheck(self):
        
        # get the list of cameras
        cameraList = cmds.listCameras()
        
        if len(cameraList) > 4:
            returnString = str(len(cameraList)) + " cameras detected, should have 4."
            return returnString
            
        else:
            return ''
        
        
def getObject():
    return CameraCount()