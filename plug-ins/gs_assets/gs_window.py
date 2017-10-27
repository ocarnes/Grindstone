# Grindstone gs_window.py
# Authors: Sam Carnes and Sean Adams

# This file creates the Grindstone window and attaches script functionality to UI elements

import os
import functools
import maya.cmds as cmds
import gs_ScriptList_class as SL

# path to the current directory
gs_path = os.path.dirname(os.path.realpath(SL.__file__))

# extension to reach the gs_scripts directory from the current one
gs_scr = '/gs_scripts'

# **************************************************************************************************
# GrindstoneWindow Class
class GrindstoneWindow:
    
    #********** DATA **********#
    
    # ID for our application window
    winID = "grindstoneWindow"
    
    # an array to hold all of our scripts
    pipelineStages = []
    
    
    
    
    #********** INIT **********#
    
    # constructor that populates the pipelineStages array using the directories in the gs_scripts folder
    def __init__(self):
        
        # this is the complete path to the Grindstone scripts
        scriptsPath = gs_path + gs_scr
        
        # clean up our data in case Maya still has it preserved in memory
        self.pipelineStages = []
        
        # for every folder in the gs_scripts directory
        for fn in os.listdir(scriptsPath):
            
            # create a new ScriptList out of the folder name
            stage = SL.ScriptList(fn)
            
            # if the 'folder' is not the python init script
            if "init" not in fn:
                
                # create a new path that leads into the folder
                newPath = scriptsPath + '/' + fn
            
                # for every file inside the new path
                for f in os.listdir(newPath):

                    # if the file is a .py file and not __init__.py
                    if f[-3:] == ".py" and f != "__init__.py":

                        # create and execute a temporary import command for the file
                        command = "import gs_scripts." + stage.name + "." + f[:-3] + " as temp"
                        exec(command)
                        
                        # retrieve an object representing a script from the file and delete the imported module
                        stage.append(temp.getObject())
                        del temp
                    
                # add the stage information to the pipelineStages array
                self.pipelineStages.append(stage)
        
       
       
       
    #********** RUN SCRIPTS **********#
       
    # run all of the scripts that have been selected by the user
    def runScripts(self):
        
        # for every folder of scripts in the pipelineStages array
        for stage in self.pipelineStages:
            
            # if the folder is checked, execute the checks
            if stage.isChecked:
                stage.doChecks()
                
        
        
        
    #********** RUN **********#
        
    # creates the Grindstone window and exposes script functionality to the user
    def run(self):
        
        # Test to make sure that the UI isn't already active
        if cmds.window(self.winID, exists=True):
            cmds.deleteUI(self.winID)
        
    
        # Now create a fresh UI window
        cmds.window(self.winID)

        # Add a Layout - a columnLayout stacks controls vertically
        cmds.columnLayout()

        # Add controls into this Layout
        
        # create check boxes for every script directory
        for i in range(0, len(self.pipelineStages)):
            cmds.checkBox(label=self.pipelineStages[i].name, value = self.pipelineStages[i].isChecked, align='center', changeCommand=functools.partial(lambda i, *args: self.pipelineStages[i].check() , i))
        
        # create button that will run the checked scripts
        cmds.button(label='RUN', command=lambda *args: self.runScripts())


        # Display the window
        cmds.showWindow()
        
# End GrindstoneWindow Class
# **************************************************************************************************
