import maya.cmds as cmds

# Function that queries the textField and prints it to the
# History pane in the script editor
def printTxtField ( fieldID ):
    print cmds.textField( fieldID, query=True, text=True)

# Define an id string for the window first
winID = 'kevsUI'

# Test to make sure that the UI isn't already active
if cmds.window(winID, exists=True):
    cmds.deleteUI(winID)
    
# Now create a fresh UI window
cmds.window(winID)

# Add a Layout - a columnLayout stacks controls vertically
cmds.columnLayout()

# Add controls into this Layout
whatUSay = cmds.textField()
cmds.button(label='click me', command='printTxtField(whatUSay)')

# Display the window
cmds.showWindow()