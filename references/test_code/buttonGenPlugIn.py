import sys, os
import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds
# ... additional imports here ...

def hiButton(theShelf):
    cmds.setParent(theShelf)
    buttonTag = True
    shelfButton=cmds.shelfLayout(theShelf,q=1,ca=1)
    #cmds.shelfButton(annotation="Print \"Hello\".", image1="commandButton.png", command="print \"Hello\\n\"", label="helloButton")
    if shelfButton is None:	    
        cmds.shelfButton(annotation="Print \"Hello\".", image1="commandButton.png", command="print \"Hello\\n\"", label="helloButton")
        buttonTag = False
    else:
        for button in shelfButton:
            label = ""
            if cmds.objectTypeUI(button, isType="shelfButton"):
                label=str(cmds.shelfButton(button, q=1, label=1))
                if "helloButton" == label:
                    buttonTag = False
    if buttonTag:
        cmds.shelfButton(annotation="Print \"Hello\".", image1="commandButton.png", command="print \"Hello\\n\"", label="helloButton")

def byeButton(theShelf):
    shelfButtons=cmds.shelfLayout(theShelf, q=1, ca=1)
    for button in shelfButtons:
        label = ""
        # Assert that this is a shelfButton 
        if cmds.objectTypeUI(button, isType="shelfButton"):
            label=str(cmds.shelfButton(button, q=1, label=1))
            # If this button has the label we're looking for, 
            # delete the button. 
            if "helloButton" == label:
                cmds.deleteUI(button)

##########################################################
# Plug-in 
##########################################################

    
##########################################################
# Plug-in initialization.
##########################################################

def maya_useNewAPI():
	"""
	The presence of this function tells Maya that the plugin produces, and
	expects to be passed, objects created using the Maya Python API 2.0.
	"""
	pass

def initializePlugin(mobject):
    ''' Initialize the plug-in when Maya loads it. '''
    hiButton("Custom")


def uninitializePlugin(mobject):
    ''' Uninitialize the plug-in when Maya un-loads it. '''
    byeButton("Custom")
