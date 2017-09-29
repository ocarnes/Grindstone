import maya.cmds

cmds.setParent("Custom")
cmds.shelfButton(annotation="Print \"Hello\".", image1="commandButton.png", command="print \"Hello\\n\"", label="helloButton")