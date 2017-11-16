# Grindstone gs_QuadScan_class.py
# Authors: Sam Carnes and Sean Adams

# This file scans all objects to identify any triangles or n-gons

import maya.cmds as cmds

class QuadScan:
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = False
        
        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = "Select non-quads"
    
    
    
    #********** DO CHECK **********#
    
    def doCheck(self):
        
        # Setting up vars for tracking and managing the faces found
        triHold = []
        quadHold = []
        nGonHold = []

        triCount = 0
        quadCount = 0
        nGonCount = 0

        triLim = 0
        quadLim = 0
        nGonLim = 0

        oldHold = cmds.ls(selection = True)

        # Creating lists of all geometry in the scene and then all of its faces
        polyHold = cmds.ls(geometry=True)
        faceHold= cmds.polyListComponentConversion(polyHold, tf=True)
        
        # Saving the current selection state and hilite for restoration following execution
        userHil = cmds.ls(hilite = True)
        userSel = cmds.ls(selection = True)

        # Setting the selection type to look for faces and selecting them
        cmds.select(faceHold)

        # Contraining the selection to triangles and storing the results
        cmds.polySelectConstraint(m = 3, t = 8, sz = 1)
        triHold = cmds.ls(sl=1)
        triLim = len(triHold)

        # Quadrilateral constraint
        cmds.polySelectConstraint(m = 3, t = 8, sz = 2)
        quadHold = cmds.ls(sl = 1)
        quadLim = len(quadHold)

        # N_Gon constraint
        cmds.polySelectConstraint(m = 3, t = 8, sz = 3)
        nGonHold = cmds.ls(sl = 1)
        nGonLim = len(nGonHold)

        cmds.polySelectConstraint(disable = True)
        cmds.select(clear = True)

        # Iterating through the results to count the amount of faces found
        for i in range(0, triLim):
            cmds.select(triHold[i])
            triCount += cmds.polyEvaluate(triHold[i], faceComponent = True)

        # Iterating through the results to count the amount of faces found
        for i in range(0, quadLim):
            cmds.select(quadHold[i])
            quadCount += cmds.polyEvaluate(quadHold[i], faceComponent = True)



        # Iterating through the results to count the amount of faces found
        for i in range(0, nGonLim):
            cmds.select(nGonHold[i])
            nGonCount += cmds.polyEvaluate(nGonHold[i], faceComponent = True)


        cmds.selectType(allObjects = True)
        cmds.hilite(userHil)
        cmds.select(userSel)

        print triHold
        print triCount

        print quadHold
        print quadCount

        print nGonHold
        print nGonCount
        
        
        
    #********** RUN FIX **********#
    
    # selects all non-quad faces
    def runFix(self):
        
        try:
            
            # delete non-deformer history
            cmds.bakePartialHistory(allShapes=True, prePostDeformers=True)
            
            return "Non-deformer history deleted."
            
        except:
            
            return "There was a problem deleteing non-deformer history."
            


#********** RETURN INSTANCE OF SCRIPT CLASS **********#

def getObject():
    return QuadScan()