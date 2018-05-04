# Grindstone gs_window.py
# Authors: Sam Carnes and Sean Adams

# This file creates the Grindstone window and attaches script functionality to UI elements

import os
import functools
import gs_ScriptList_class as SL
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2 import QtWidgets
import sys
import functools


# extension to reach the gs_scripts directory from the current one
gs_scr = '/gs_scripts'



# **************************************************************************************************
# GrindstoneWindow Class
class GrindstoneWindow(QtWidgets.QMainWindow):
    
    
    #********** DATA **********#

    # an array to hold all of our scripts
    pipelineStages = []
    
    
    
    
    #********** INIT **********#
    
    # constructor that populates the pipelineStages array using the directories in the gs_scripts folder
    def __init__(self, parent, gs_path):
         
        # this is the complete path to the Grindstone scripts
        scriptsPath = gs_path + gs_scr
        
        #add it to the python path so we can import scripts
        sys.path.append(gs_path)
        
        # clean up our data in case any of it is still in memory
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
                


                
            
        # set up the pyside window    
        super(GrindstoneWindow, self).__init__()
        self.resize(900, 600)
        self.setWindowTitle("Grindstone 2.0")
        
        # checks widget 
        self.checks = QtWidgets.QFrame()
        self.checks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        
        # checks layout
        self.checksLayout = QtWidgets.QVBoxLayout(self.checks)
        
        # results widget 
        self.results = QtWidgets.QFrame()
        self.results.setFrameShape(QtWidgets.QFrame.StyledPanel)
        
        # results layout 
        self.resultsLayout = QtWidgets.QVBoxLayout(self.results)
        
        # scrolling widget to contain the results
        #self.resultsScroll = QtWidgets.QScrollArea()
        #self.resultsScroll.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.resultsScroll.setWidget(self.results)
        
        # main widget 
        self.mainWidget = QtWidgets.QWidget()

        # main layout
        self.mainLayout = QtWidgets.QHBoxLayout(self)

        # the tree widget for the categories (goes inside the checks widget)
        self.tree = QtWidgets.QTreeWidget()
        self.tree.setHeaderLabel("Grindstone Checks")

        # makes the tri-state checkboxes for the categories more readable
        self.tree.setStyleSheet("QTreeView {background-color: #444444;} QTreeView::indicator:unchecked {border: 1px solid #444444; background-color: #232629;} QTreeView::indicator:indeterminate {border: 3px solid #232629; background-color: #BBBBBB;}")
    
        # populate the categories of the tree
        for stage in self.pipelineStages:
            parent = QtWidgets.QTreeWidgetItem(self.tree)
            parent.setText(0, stage.name)
            parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            
            # populate the child items of each category
            for script in stage.scripts:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, script.scriptName)
                child.setCheckState(0, Qt.Unchecked)
        

        # add the tree to the checks widget 
        self.checksLayout.addWidget(self.tree)
        
        # create the button that runs the selected scripts
        self.runButton = QtWidgets.QPushButton("Run")
        self.runButton.clicked.connect(self.runScripts)
        
        # add the 'run' button to the checks layout
        self.checksLayout.addWidget(self.runButton)
        
        # A stub for the publish button
        self.pubButton = QtWidgets.QPushButton("Publish")
        self.checksLayout.addWidget(self.pubButton)

        # create a horizontal splitter to display the checks on the left and the results on the right
        self.splitter = QtWidgets.QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.checks)
        self.splitter.addWidget(self.results)
        self.splitter.setStretchFactor(1, 1)
        self.splitter.setStretchFactor(2, 4)
        
        # add the splitter to the main layout
        self.mainLayout.addWidget(self.splitter)
        
        # set the main widgets layout to the main layout
        self.mainWidget.setLayout(self.mainLayout)
        
        # set the main widget as the central widget
        self.setCentralWidget(self.mainWidget)
        
       
   
    # execute all of the scripts that are checked
    def runScripts(self):
        
        # disable the "Run" button
        self.runButton.setEnabled(False)
        
        # remove old entries
        for i in reversed(range(self.resultsLayout.count())): 
            #print i
            child = self.resultsLayout.takeAt(i).widget()
            
            if child != None:
                child.setParent(None)

        #print "Begin Test!"

        root = self.tree.invisibleRootItem()
        catCount = root.childCount()
        for i in range(catCount):
            category = root.child(i)
            if category.checkState(0) != Qt.Unchecked:
                scriptCount = category.childCount()
                for j in range(scriptCount):
                    script = category.child(j)
                    if script.checkState(0) != Qt.Unchecked:
                        #print self.pipelineStages[i].scripts[j].hasFix
                        labelText = str(self.pipelineStages[i].scripts[j].doCheck())
                        
                        # if the check found an error, create a result entry
                        if labelText != '':
                            # create the result entry row
                            resultEntry = QtWidgets.QLabel()
                            resultEntry.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Sunken)
                            resultEntry.setMargin(10)
                            
                            # create a horizontal layout for the result entry
                            resultEntryLayout = QtWidgets.QHBoxLayout()
                            resultEntryLayout.setAlignment(Qt.AlignCenter)
                            
                            # create the text for the result
                            resultLabel = QtWidgets.QLabel()
                            resultLabel.setText(labelText)
                            resultEntryLayout.addWidget(resultLabel)
                            
                            # create an ignore button 
                            ignoreButton = QtWidgets.QPushButton("Ignore")
                            ignoreButton.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
                            ignoreButton.clicked.connect(functools.partial(lambda resultEntry, *args: self.remWidge(resultEntry), resultEntry))
                            resultEntryLayout.addWidget(ignoreButton)
                            
                            # if the script has an autofix, create a button for it 
                            if self.pipelineStages[i].scripts[j].hasFix:
                                fixLabel = self.pipelineStages[i].scripts[j].fixLabel
                                autofixButton = QtWidgets.QPushButton(fixLabel)
                                
                                autofixButton.clicked.connect(functools.partial(lambda i, j, resultEntryLayout, *args: self.runFix(i, j, resultEntryLayout), i, j, resultEntryLayout))
                                
                                resultEntryLayout.addWidget(autofixButton)
                            
                            # otherwise, fill the space with nothing
                            else:
                                blankSpace = QtWidgets.QLabel()
                                resultEntryLayout.addWidget(blankSpace)

                            # set the stretch of the result entry layout
                            resultEntryLayout.setStretch(0, 5)
                            resultEntryLayout.setStretch(1, 1)
                            resultEntryLayout.setStretch(2, 2)
                            
                            # set the result entry's layout
                            resultEntry.setLayout(resultEntryLayout)
                            
                            # add the result entry to the results field
                            self.resultsLayout.addWidget(resultEntry)
        
        # add spacer
        self.resultsLayout.addStretch()
        
        # re-enable the "Run" button
        self.runButton.setEnabled(True)
        

    def remWidge(self, delEnt):
        delEnt.setParent(None)
    

    def runFix(self, catVal, scrVal, entryVal):
        newLabel = entryVal.itemAt(0).widget()
        fixResult = self.pipelineStages[catVal].scripts[scrVal].runFix()
        newLabel.setText(fixResult)
        fixButton = entryVal.itemAt(1).widget()
        fixButton.setText("OK")
        oldButton = entryVal.takeAt(2).widget()
        oldButton.setParent(None)
        blankSpace = QtWidgets.QLabel()
        entryVal.addWidget(blankSpace)
        entryVal.setStretch(2, 2)
        #print catVal
        #print scrVal
    
    # creates the Grindstone window and exposes script functionality to the user
    def run(self):
        
        self.show()
        
# End GrindstoneWindow Class
# **************************************************************************************************
