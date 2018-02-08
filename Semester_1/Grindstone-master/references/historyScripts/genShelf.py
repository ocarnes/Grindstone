def createMyShelf():
    shelfName = 'My_Shelf'
    test = cmds.shelfLayout(shelfName, ex=True)
    if test:
        # If the shelf already exists, clear the contents and re-add the buttons.
        newShelf = shelfName
        buttons = cmds.shelfLayout(newShelf, query=True, childArray=True)
        cmds.deleteUI(buttons, control=True)	
    else:
        newShelf = mel.eval('addNewShelfTab %s' % shelfName)	
        cmds.setParent(newShelf)
        # add buttons here 

def removeShelf():
    shelfName = 'My_Shelf'
    test = cmds.shelfLayout(shelfName, ex=True)
    if test:
        mel.eval('deleteShelfTab %s' % shelfName)
        gShelfTopLevel = mel.eval('$tmpVar=$gShelfTopLevel')
        cmds.saveAllShelves(gShelfTopLevel)
    else:
        return