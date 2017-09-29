import sys
import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds
# ... additional imports here ...



##########################################################
# Global Functions
##########################################################

# Function that queries the textField and prints it to the
# History pane in the script editor
def printTxtField ( fieldID ):
    print cmds.textField( fieldID, query=True, text=True)


##########################################################
# Plug-in 
##########################################################
class MyCommandClass( OpenMaya.MPxCommand ):
    kPluginCmdName = 'mimic'
    
    def __init__(self):
        ''' Constructor. '''
        OpenMaya.MPxCommand.__init__(self)
    
    @staticmethod 
    def cmdCreator():
        ''' Create an instance of our command. '''
        return MyCommandClass() 
    
    def doIt(self, args):

        # Define an id string for the window first
        winID = 'kevsUI'

        # Test to make sure that the UI isn't already active
        if cmds.window(winID, exists=True):
            cmds.deleteUI(winID)
    
        # Now create a fresh UI window
        cmds.window(winID)

        # Add a Layout - a columnLayout stacks controls vertically
        cmds.columnLayout()

        # Add controls into this Layout
        message = cmds.textField()
        cmds.button(label='click me', command='print cmds.textField( message, query=True, text=True)')

        # Display the window
        cmds.showWindow()
    
    
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
