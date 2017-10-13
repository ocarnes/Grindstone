import os
import functools
import maya.cmds as cmds


# **************************************************************************************************
# GrindstoneWindow Class
class GrindstoneWindow:
    
    winID = "grindstoneWindow"
    
    scripts = []
    
    
    def sayHello(self):
        print "Hello!"
    
    
    def __init__(self):
        for fn in os.listdir('C:/Users/adamsse/Documents/maya/2018/plug-ins/gs_assets/gs_scripts'):
            if fn[-3:] == ".py" and fn != "__init__.py":
                command = "import gs_scripts." + fn[:-3] + " as temp"
                exec(command)
                self.scripts.append(temp.getObject())
                del temp
                
        for s in self.scripts:
            print s
        print len(self.scripts)
        
        
        
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
        
        for i in range(0, len(self.scripts)):
            print i
            print self.scripts[i]
            #cmds.button(label=i, command=lambda i: self.scripts[i].doCheck())
            cmds.button(label=i, command=functools.partial(lambda i, *args: self.scripts[i].doCheck() , i)
)
        '''for s in self.scripts:
            print s
            print s.doCheck()
            cmds.button(label=s, command=lambda s: s.doCheck())'''

        # Display the window
        cmds.showWindow()
        
# End GrindstoneWindow Class
# **************************************************************************************************
