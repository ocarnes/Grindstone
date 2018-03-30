# Grindstone gs_CameraCount_class.py
# Authors: Sam Carnes and Sean Adams

# This file defines a script that checks that the number of cameras is not greater than 4



class MakeSphere:
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = True

        # identify what this check is called
        self.scriptName = "Dummy"
        
        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = "Dummy!"
        
       
        
        
    #********** DO CHECK **********#
    
    def doCheck(self):
        
        
        return "I made a SPHERE!!!"
            
    
    
    #********** RUN FIX **********#
    
    # deletes any cameras that are not the default front, persp, side, or top cameras
    def runFix(self):
        
        
        
        return "SPHERE fix!"
        
        
        
#********** RETURN INSTANCE OF SCRIPT CLASS **********#
        
def getObject():
    return MakeSphere()