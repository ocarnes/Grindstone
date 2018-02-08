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
        #app = QtWidgets.QApplication.instance()
        #someWin = QtWidgets.QMainWindow()
        super(windowExample, self).__init__()
        tree = QtWidgets.QTreeWidget()
        headerItem  = QtWidgets.QTreeWidgetItem()
        item = QtWidgets.QTreeWidgetItem()
    
        for i in xrange(3):
            parent = QtWidgets.QTreeWidgetItem(tree)
            parent.setText(0, "Parent {}".format(i))
            parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            for x in xrange(5):
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, "Child {}".format(x))
                child.setCheckState(0, Qt.Unchecked)
        
        self.setCentralWidget(tree)

aTest = windowExample(parent=omui.MQtUtil.mainWindow())
aTest.show()