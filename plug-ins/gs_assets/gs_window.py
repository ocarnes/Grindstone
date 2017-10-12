import os
import maya.cmds as cmds
import gs_scripts.test_1 as t1

# **************************************************************************************************
# GrindstoneWindow Class
class GrindstoneWindow:
    
    winID = "grindstoneWindow"
    
    scripts = []
    
    test = t1.getObject()
    
    
    
    def __init__(self):
        for fn in os.listdir('./scripts'):
            if fn[-3:] == ".py" and fn != "__init__.py":
                command = "import scripts." + fn[:-3] + " as temp"
                exec(command)
                scripts.append(temp.getObject())
                del temp
        
        
        
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
        cmds.button(label='make sphere', command='cmds.polySphere()')
        cmds.button(label='list scene items', command='print cmds.ls(transforms=True)')
        cmds.button(label='list cameras', command='print cmds.listCameras()')
        
        for i in range(0, len(self.scripts) - 1):
            print i
            cmds.button(label=i, command=lambda *args: self.scripts[i].doCheck())
        cmds.button(label='x', command=lambda *args: self.test.doCheck())

        # Display the window
        cmds.showWindow()
        
# End GrindstoneWindow Class
# **************************************************************************************************
