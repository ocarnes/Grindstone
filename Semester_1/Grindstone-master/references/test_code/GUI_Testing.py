import maya.cmds as cmds
import functools

someFruits = ['apple', 'banana', 'orange']
rowArr = []

def addRow(self):
    for fruit in someFruits:    
        tempVar = cmds.rowLayout(parent=stateColumn,  numberOfColumns = 2)
        rowArr.append(tempVar)
        cmds.textField(text=fruit)
        delInd = rowArr[len(rowArr)-1]
        #cmds.button(label='ignore', command="cmds.deleteUI(delInd)")
        cmds.button(label='ignore', command=functools.partial(lambda delInd, *args: cmds.deleteUI(delInd), delInd))

GS_guiWin = cmds.window(title="GUI Thing", backgroundColor=(0.1, 0.1, 0.1))

GS_format = cmds.formLayout(numberOfDivisions=100)

checkColumn = cmds.columnLayout(adj=1, bgc=(0.9, 0.5, 0.2))
cmds.setParent('..')
stateColumn = cmds.columnLayout(adj=1, bgc=(0.4, 0.1, 0.3))

cmds.formLayout(GS_format, edit=True, attachForm=[(checkColumn, 'top', 5), (checkColumn, 'bottom', 5), (checkColumn, 'left', 5), (stateColumn, 'top', 5), (stateColumn, 'bottom', 5), (stateColumn, 'right', 5)], attachPosition=[(checkColumn, 'right', 5, 25), (stateColumn, 'left', 5, 25)])

cmds.setParent(checkColumn)

cmds.button(label = 'dumButton', command = addRow)

cmds.showWindow(GS_guiWin)