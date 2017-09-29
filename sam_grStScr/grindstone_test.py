import sys
import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds

#sys.path.append('C:\Users\adamsse\Documents\maya\2018\scripts')
#reload(grindestone_test)
#import grindestone_test as gs



# **************************************************************************************************
# GrindstoneWindow Class
class GrindestoneWindow:
    
    winID = "grindstoneWindow"
    
    
    
    def __init__(self):
        pass
        
        
        
    def printTxtField(self, fieldID):
        print cmds.textField(fieldID, query=True, text=True)
        
        
        
    def run(self):
        # Test to make sure that the UI isn't already active
        if cmds.window(self.winID, exists=True):
            cmds.deleteUI(self.winID)
    
        # Now create a fresh UI window
        cmds.window(self.winID)

        # Add a Layout - a columnLayout stacks controls vertically
        cmds.columnLayout()

        # Add controls into this Layout
        message = cmds.textField()
        cmds.button(label='click me', command=lambda *args: self.printTxtField( message ))
        #cmds.button(lable='make sphere', 

        # Display the window
        cmds.showWindow()
        
# End GrindstoneWindow Class
# **************************************************************************************************




##########################################################
# Plug-in 
##########################################################
class MyCommandClass( OpenMaya.MPxCommand ):
    
    kPluginCmdName = 'mimic'
    
    # create an instance of the Grindstone window provider
    windowProvider = GrindestoneWindow()
    
    
    def __init__(self):
        ''' Constructor. '''
        OpenMaya.MPxCommand.__init__(self)
    
    @staticmethod 
    def cmdCreator():
        ''' Create an instance of our command. '''
        return MyCommandClass() 
        
    
    def doIt(self, args):

       # pass control to the window provider
       self.windowProvider.run()
    
    
    
    
##########################################################
# Plug-in initialization.
##########################################################

def maya_useNewAPI():
	"""
	The presence of this function tells Maya that the plugin produces, and
	expects to be passed, objects created using the Maya Python API 2.0.
	"""
	pass

def initializePlugin( mobject ):
    ''' Initialize the plug-in when Maya loads it. '''
    mplugin = OpenMaya.MFnPlugin( mobject )
    try:
        mplugin.registerCommand( MyCommandClass.kPluginCmdName, 
            MyCommandClass.cmdCreator )

    except:
        sys.stderr.write( 'Failed to register command: ' + MyCommandClass.kPluginCmdName )

def uninitializePlugin( mobject ):
    ''' Uninitialize the plug-in when Maya un-loads it. '''
    mplugin = OpenMaya.MFnPlugin( mobject )
    try:
        mplugin.deregisterCommand( MyCommandClass.kPluginCmdName )
        
    except:
        sys.stderr.write( 'Failed to unregister command: ' + MyCommandClass.kPluginCmdName )
