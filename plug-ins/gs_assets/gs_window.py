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
    
    # an array to hold the result entries of each script
    rowArr = []
    
    
    
    
    #********** INIT **********#
    
    # constructor that populates the pipelineStages array using the directories in the gs_scripts folder
    def __init__(self):
        
        # this is the complete path to the Grindstone scripts
        scriptsPath = gs_path + gs_scr
        
        # clean up our data in case Maya still has it preserved in memory
        self.pipelineStages = []
        
        for row in self.rowArr:
            cmds.deleteUI(row)
        self.rowArr = []
        
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
    def runScripts(self, destinationLayout):
        
        # clear out previous results
        for row in self.rowArr:
            try:
                cmds.deleteUI(row)
                
            except:
                print "Window closed with stuff in rowArr"
            
        self.rowArr = []
        
        
        # for every folder of scripts in the pipelineStages array
        for stage in self.pipelineStages:
            
            # if the folder is checked, execute the checks
            if stage.isChecked:
                for script in stage.scripts:
                    result = script.doCheck()
                    self.showResult(result, destinationLayout, script)
                    
                    
                                        
          
    #********** SHOW RESULT **********#          
    
    # adds a result entry                
    def showResult(self, result, destinationLayout, script):
        if result != '':
            
            if script.hasFix:
                columnCount = 3
                
            else:
                columnCount = 2
            
            tempVar = cmds.rowLayout(parent=destinationLayout,  numberOfColumns = columnCount)
            self.rowArr.append(tempVar)
            cmds.textField(text=result, editable=False, width=500)
            delInd = self.rowArr[len(self.rowArr)-1]
            cmds.button(label='Ignore', command=functools.partial(lambda delInd, *args: self.removeResult(delInd), delInd))
            
            if script.hasFix:
                cmds.button(label='Auto Fix', command=functools.partial(lambda delInd, script, destinationLayout, *args: self.executeFix(delInd, script, destinationLayout), delInd, script, destinationLayout))
                
                
                
                
    #********** EXECUTE FIX **********#          
    
    # executes an auto fix              
    def executeFix(self, delInd, script, destinationLayout):
        fixResult = script.runFix()
        
        children = cmds.rowLayout(delInd, query=True, childArray=True) 
        
        # change the text field to reflect the fix result
        cmds.textField(children[0], edit=True, text=fixResult)
        
        # change the ignore button to be an acknowledgement of the fix result
        cmds.button(children[1], edit=True, label='Ok')
                
        # delete the auto-fix button
        cmds.deleteUI(children[2])
           
           
           
           
    #********** REMOVE RESULT **********#         
          
    # removes a result entry      
    def removeResult(self, index):
        cmds.deleteUI(index)
        self.rowArr.remove(index)
        
        
        
    #********** RUN **********#
        
    # creates the Grindstone window and exposes script functionality to the user
    def run(self):
        
        # GUI Padding Var defined for quick changes
        # Must be even due to pixel restraints
        gsPad = 6
        
        # Test to make sure that the UI isn't already active
        if cmds.window(self.winID, exists=True):
            cmds.deleteUI(self.winID)
        
    
        # Now create a fresh UI window
        gsWindow = cmds.window(self.winID)
        
        # Start up a form layout for dynamic sized components
        gsFormat = cmds.formLayout(numberOfDivisions=100)
        
        # Add two columns to hold check boxes and the problem states
        checkColumn = cmds.columnLayout(adjustableColumn=1, backgroundColor=(0.2157, 0.2157, 0.2157))
        cmds.setParent('..')
        stateColumn = cmds.columnLayout(adjustableColumn=1, backgroundColor=(0.3157, 0.3157, 0.3157))
        
        # Load columns into form layout
        cmds.formLayout(gsFormat, edit=True, attachForm=[(checkColumn, 'top', gsPad), (checkColumn, 'bottom', gsPad), (checkColumn, 'left', gsPad), (stateColumn, 'top', gsPad), (stateColumn, 'bottom', gsPad), (stateColumn, 'right', gsPad)], attachPosition=[(checkColumn, 'right', gsPad/2, 25), (stateColumn, 'left', gsPad/2, 25)])


        # Set the parent to the check holding column
        cmds.setParent(checkColumn)
        
        # create check boxes for every script directory
        for i in range(0, len(self.pipelineStages)):
            cmds.checkBox(label=self.pipelineStages[i].name, value = self.pipelineStages[i].isChecked, align='center', changeCommand=functools.partial(lambda i, *args: self.pipelineStages[i].check() , i))
        
        # create button that will run the checked scripts
        cmds.button(label='RUN', command=lambda *args: self.runScripts(stateColumn), backgroundColor=(0.3647, 0.3647, 0.3647))


        # Display the window
        cmds.showWindow()
        
# End GrindstoneWindow Class
# **************************************************************************************************
