# Grindstone gs_FileTypeMA_class.py
# Authors: Sam Carnes and Sean Adams

# This file defines a script that checks to see if the file type is .ma


import maya.cmds as cmds

class FileTypeMA:
    
    
    def __init__(self):
        self.hasFix = False
       
        
    def doCheck(self):
        
        # get a string that contains the file type
        fileType = cmds.file(query=True, type=True)
        
        if "mayaAscii" in fileType:
            return ''
            
        else:
            returnString = "File type is \"" + fileType[0] + ",\" and should be \"mayaAscii.\""
            
            return returnString
        
        
def getObject():
    return FileTypeMA()