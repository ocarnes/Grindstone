# creates shelf button on plug-in load and destroys shelf button on plug-in un-load

import maya.cmds as cmds
import maya.mel as mel


def hiButton(theShelf, buttonCommand):
    cmds.setParent(theShelf)
    buttonTag = True
    shelfButton=cmds.shelfLayout(theShelf,q=1,ca=1)
    #cmds.shelfButton(annotation="Print \"Hello\".", image1="commandButton.png", command="print \"Hello\\n\"", label="helloButton")
    if shelfButton is None:	    
        cmds.shelfButton(annotation="Print \"Hello\".", image1="commandButton.png", command="mel.eval(\"" + buttonCommand + "\")", label="helloButton")
        buttonTag = False
    else:
        for button in shelfButton:
            label = ""
            if cmds.objectTypeUI(button, isType="shelfButton"):
                label=str(cmds.shelfButton(button, q=1, label=1))
                if "helloButton" == label:
                    buttonTag = False
    if buttonTag:
        cmds.shelfButton(annotation="Print \"Hello\".", image1="commandButton.png", command="mel.eval(\"" + buttonCommand + "\")", label="helloButton")



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