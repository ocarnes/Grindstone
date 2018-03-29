# Grindstone gs_plugin.py
# Authors: Sam Carnes and Sean Adams

# This file registers the 'grindstone' command which passes control to a window provider.
# It also creates a button to attach the command to on initialization, and deletes it on un-initialization.

import os
import maya.api.OpenMaya as OpenMaya
#import gs_assets.gs_window as gs_win
import gs_assets.gs_shelf_button_gen as sbg
from maya import OpenMayaUI as omui


# get the common GS components
import sys
sys.path.append('P:/lib/Grindstone')
import gs_window as gs_win

gs_path = os.path.dirname(os.path.realpath(sbg.__file__))

##########################################################
# Plug-in 
##########################################################
class MyCommandClass( OpenMaya.MPxCommand ):
    
    kPluginCmdName = 'grindstone'
    
    # create an instance of the Grindstone window provider
    windowProvider = gs_win.GrindstoneWindow(parent=omui.MQtUtil.mainWindow(), gs_path=gs_path)
    
    
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