import os
import maya.api.OpenMaya as OpenMaya
import gs_assets.gs_window as gs_win
import gs_assets.gs_shelf_button_gen as sbg

gs_path = os.path.dirname(os.path.realpath(gs_win.__file__))

##########################################################
# Plug-in 
##########################################################
class MyCommandClass( OpenMaya.MPxCommand ):
    
    kPluginCmdName = 'grindstone'
    
    # create an instance of the Grindstone window provider
    windowProvider = gs_win.GrindstoneWindow()
    
    
    def __init__(self):
        # constructor.
        OpenMaya.MPxCommand.__init__(self)
    
    
    @staticmethod 
    def cmdCreator():
        # create an instance of our command.
        return MyCommandClass() 
        
    
    def doIt(self, args):

       # pass control to the window provider
       self.windowProvider.run()
    
    
    
    
##########################################################
# Plug-in initialization.
##########################################################

def maya_useNewAPI():
	####
	# the presence of this function tells Maya that the plugin produces, and
	# expects to be passed, objects created using the Maya Python API 2.0.
	####
	pass

def initializePlugin( mobject ):
    # initialize the plug-in when Maya loads it.
    mplugin = OpenMaya.MFnPlugin( mobject )
    try:
        mplugin.registerCommand( MyCommandClass.kPluginCmdName, 
            MyCommandClass.cmdCreator )

    except:
        sys.stderr.write( 'Failed to register command: ' + MyCommandClass.kPluginCmdName )
        
    sbg.hiButton("Custom", MyCommandClass.kPluginCmdName, gs_path)

def uninitializePlugin( mobject ):
    # uninitialize the plug-in when Maya un-loads it.
    mplugin = OpenMaya.MFnPlugin( mobject )
    try:
        mplugin.deregisterCommand( MyCommandClass.kPluginCmdName )
        
    except:
        sys.stderr.write( 'Failed to unregister command: ' + MyCommandClass.kPluginCmdName )
        
    sbg.byeButton("Custom")