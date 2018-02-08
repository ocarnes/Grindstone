# Grindstone gs_NonLocalFilePaths_class.py
# Authors: Sam Carnes and Sean Adams

# This file defines a script that checks for any non-local file paths


import maya.cmds as cmds

class NonLocalFilePaths:
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = False
        
        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = ""
        
        
        # class data
        self.filePaths = []
        self.nonLocals = 0
        
        # if a file path contains this substring, then it is local
        self.LocalFlag = "dacps1"
       
        
        
    #********** DO CHECK **********#
    
    def doCheck(self):
        
        # reset non-local file count
        self.nonLocals = 0
        
        # get the list of all referenced files
        self.filePaths = cmds.file(query=True, reference=True)
        
        # determine how many of the referenced files are non-local
        for referenceFile in self.filePaths:
            if self.LocalFlag not in referenceFile:
                self.nonLocals += 1
        
        if self.nonLocals > 0:
            returnString = str(self.nonLocals) + " non-local file references detected."
            return returnString
            
        else:
            return ''
        
        
        
#********** RETURN INSTANCE OF SCRIPT CLASS **********#
        
def getObject():
    return NonLocalFilePaths()