# Grindstone menu.py

import os

import nuke

import DACLogger

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

# get the common GS components
nuke.pluginAddPath('P:/lib/python/Grindstone')
import gs_window as gs_win

DACLogger.info("Loading %s..." % (__file__,))

# get the main window
def _nuke_main_window():
    """Returns Nuke's main window"""
    for obj in QtWidgets.qApp.topLevelWidgets():
        if (obj.inherits('QMainWindow') and
                obj.metaObject().className() == 'Foundry::UI::DockMainWindow'):
            return obj
    else:
        raise RuntimeError('Could not find DockMainWindow instance')

'''app = QtGui.QGuiApplication.instance()
		
def _nuke_main_window():
    for widget in app.topLevelWidgets():
        DACLogger.info(widget)
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            DACLogger.info("This widget would get returned ^")
            return widget'''
            
            

#_nuke_main_window()
mainWindow = _nuke_main_window()

windowProvider = gs_win.GrindstoneWindow(parent=mainWindow, gs_path='P:/apps/nuke/common/DACTools/Grindstone')

nuke.menu( 'Nuke' ).addCommand( 'Grindstone', windowProvider.run, icon="GS_icon_sm.png")
