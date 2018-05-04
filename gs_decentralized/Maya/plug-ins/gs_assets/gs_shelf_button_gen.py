# Grindstone gs_shelf_button_gen.py
# Authors: Sam Carnes and Sean Adams

# This file creates a shelf button on plug-in load and destroys shelf button on plug-in un-load

import maya.cmds as cmds
import maya.mel as mel

theIcon = '/GS_icon_sm.png'

buttonLabel = 'gsButton'

buttonAnnotation = 'Grindstone'


#********** HI BUTTON **********#

# create shelf button
def hiButton(theShelf, buttonCommand, srDir):
    cmds.setParent(theShelf)
    buttonTag = True
    shelfButton=cmds.shelfLayout(theShelf,q=1,ca=1)

    if shelfButton is None:	    
        cmds.shelfButton(annotation=buttonAnnotation, image1=srDir + theIcon, command="mel.eval(\"" + buttonCommand + "\")", label=buttonLabel, scaleIcon=True)
        buttonTag = False
    else:
        for button in shelfButton:
            label = ""
            if cmds.objectTypeUI(button, isType="shelfButton"):
                label=str(cmds.shelfButton(button, q=1, label=1))
                if buttonLabel == label:
                    buttonTag = False
    if buttonTag:
        cmds.shelfButton(annotation=buttonAnnotation, image1=srDir + theIcon, command="mel.eval(\"" + buttonCommand + "\")", label=buttonLabel, scaleIcon=True)



#********** BYE BUTTON **********#

# destroy shelf button
def byeButton(theShelf):
    shelfButtons=cmds.shelfLayout(theShelf, q=1, ca=1)
    for button in shelfButtons:
        label = ""
        # Assert that this is a shelfButton 
        if cmds.objectTypeUI(button, isType="shelfButton"):
            label=str(cmds.shelfButton(button, q=1, label=1))
            # If this button has the label we're looking for, 
            # delete the button. 
            if buttonLabel == label:
                cmds.deleteUI(button)