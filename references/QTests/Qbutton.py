from PySide2.QtCore import * 
from PySide2.QtGui import * 
#from PySide2 import QtCore
#from PySide2 import QtGui
from PySide2 import QtWidgets
from maya import OpenMayaUI as omui
import maya.cmds as cmds
import sys

class windowExample(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(windowExample, self).__init__()
        self.combo = QComboBox(self)
        self.combo.addItem( 'Cone' )
        self.combo.addItem( 'Cube' )
        self.combo.addItem( 'Sphere' )
        self.combo.addItem( 'Torus' )
        self.combo.setCurrentIndex(0)        
        self.combo.move(20, 20)        
        self.combo.activated[str].connect(self.combo_onActivated)        
    
        #Create 'Create' button
        self.button = QPushButton('Create', self)        
        self.button.move(20, 50)        
        self.button.clicked.connect(self.button_onClicked)
        
        #self.setCentralWidget(tree)
        
    #Change commmand string when combo box changes
    def combo_onActivated(self, text):        
        self.cmd = 'poly' + text + '()'            
    
    #Execute MEL command when button is clicked
    def button_onClicked(self):        
        mel.eval( self.cmd )  

aTest = windowExample(parent=omui.MQtUtil.mainWindow())
aTest.show()