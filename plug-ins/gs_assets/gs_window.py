import os
import functools # used for dynamically making buttons with scripts -- might take out
import maya.cmds as cmds
import gs_ScriptList_class as SL


# **************************************************************************************************
# GrindstoneWindow Class
class GrindstoneWindow:
    
    winID = "grindstoneWindow"
    
    pipelineStages = []
    
    runTests = 0
    
    
    def sayHello(self):
        print "Hello!"
    
    
    def __init__(self):
        
        scriptsPath = 'C:/Users/adamsse/Documents/maya/2018/plug-ins/gs_assets/gs_scripts'
        
        for fn in os.listdir(scriptsPath):
            stage = SL.ScriptList(fn)
            if "init" not in fn:
                newPath = scriptsPath + '/' + fn
            
                for f in os.listdir(newPath):

                    if f[-3:] == ".py" and f != "__init__.py":

                        command = "import gs_scripts." + stage.name + "." + f[:-3] + " as temp"
                        exec(command)
                        stage.append(temp.getObject())
                        del temp
                    
                # add the stage information to the pipelineStages array
                self.pipelineStages.append(stage)
                

        
    def printTxtField(self, fieldID):
        print cmds.textField(fieldID, query=True, text=True)
        
        
    def runScripts(self):
        for stage in self.pipelineStages:
            if stage.isChecked:
                stage.doChecks()
                
                
    def toggleX(self):
        if self.runTests:
            self.runTests = 0
        else:
            self.runTests = 1
        
        
    def run(self):
        # Test to make sure that the UI isn't already active
        if cmds.window(self.winID, exists=True):
            cmds.deleteUI(self.winID)
            
        
        # reset the runTests flag to 0
        self.runTests = 0
        
    
        # Now create a fresh UI window
        cmds.window(self.winID)

        # Add a Layout - a columnLayout stacks controls vertically
        cmds.columnLayout()

        # Add controls into this Layout
        '''message = cmds.textField()
        cmds.button(label='click me', command=lambda *args: self.printTxtField( message ))
        cmds.button(label='make sphere', command='cmds.polySphere()')
        cmds.button(label='list scene items', command='print cmds.ls(transforms=True)')
        cmds.button(label='list cameras', command='print cmds.listCameras()')
        
        for i in range(0, len(self.scripts)):
            cmds.button(label=i, command=functools.partial(lambda i, *args: self.scripts[i].doCheck() , i))'''

        # check box
        '''cmds.checkBox(label='Run Tests', align='center', onCommand=lambda *args: self.toggleX(), offCommand=lambda *args: self.toggleX())
        cmds.button(label='RUN', command=lambda *args: self.runScripts())'''
        
        
        for i in range(0, len(self.pipelineStages)):
            cmds.checkBox(label=self.pipelineStages[i].name, align='center', changeCommand=functools.partial(lambda i, *args: self.pipelineStages[i].check() , i))
        
        cmds.button(label='RUN', command=lambda *args: self.runScripts())


        # Display the window
        cmds.showWindow()
        
# End GrindstoneWindow Class
# **************************************************************************************************
