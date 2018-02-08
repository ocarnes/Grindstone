def changeTextFld(*args):
    cmds.textField("nameOfTexFld", edit=True, tx="Foo Bar")

window = cmds.window()
cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
cmds.text( label='Name' )
name = cmds.textField("nameOfTexFld", tx="Test", ed=False)
cmds.button( label='Button 1', command=changeTextFld )
cmds.showWindow( window )