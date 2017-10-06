import maya.cmds
shelfButtons=cmds.shelfLayout("Custom", q=1, ca=1)
for button in shelfButtons:
    label = ""
    # Assert that this is a shelfButton 
    if cmds.objectTypeUI(button, isType="shelfButton"):
        label=str(cmds.shelfButton(button, q=1, label=1))
        # If this button has the label we're looking for, 
        # delete the button. 
        if "helloButton" == label:
            cmds.deleteUI(button)
