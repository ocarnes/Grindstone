# Grindstone gs_FileTypeMA_class.py
# Authors: Sam Carnes and Sean Adams

# This file defines a script that checks to see if the file type is .ma


import maya.cmds as cmds

class FileTypeMA:
    
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = False
       
        
        
    #********** DO CHECK **********#
        
    def doCheck(self):
        
        # get a string that contains the file type
        fileType = cmds.file(query=True, type=True)
        
        if "mayaAscii" in fileType:
            return ''
            
        else:
            returnString = "File type is \"" + fileType[0] + ",\" and should be \"mayaAscii.\""
            
            return returnString
        
        
        
#********** RETURN INSTANCE OF SCRIPT CLASS **********#
        
def getObject():
    return FileTypeMA()