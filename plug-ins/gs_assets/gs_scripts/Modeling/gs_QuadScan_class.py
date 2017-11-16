# Grindstone gs_QuadScan_class.py
# Authors: Sam Carnes and Sean Adams

# This file scans all objects to identify any triangles or n-gons

import maya.cmds as cmds

class QuadScan:
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = True
        
        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = "Select non-quads"
        
        # Vars for tracking and referencing the different polygons
        self.triHold = []
        self.quadHold = []
        self.nGonHold = []
    
    
    
    #********** DO CHECK **********#
    
    def doCheck(self):
        
        # Setting up vars for tracking and managing the faces found
        self.triHold = []
        self.quadHold = []
        self.nGonHold = []
        
        triRep = ''
        nGonRep = ''
        dualFind = ''
        perPoint = ''

        triCount = 0
        quadCount = 0
        nGonCount = 0

        triLim = 0
        quadLim = 0
        nGonLim = 0

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
        self.triHold = cmds.ls(sl=1)
        triLim = len(self.triHold)

        # Quadrilateral constraint
        cmds.polySelectConstraint(m = 3, t = 8, sz = 2)
        self.quadHold = cmds.ls(sl = 1)
        quadLim = len(self.quadHold)

        # N_Gon constraint
        cmds.polySelectConstraint(m = 3, t = 8, sz = 3)
        self.nGonHold = cmds.ls(sl = 1)
        nGonLim = len(self.nGonHold)

        cmds.polySelectConstraint(disable = True)
        cmds.select(clear = True)

        # Iterating through the results to count the amount of faces found
        for i in range(0, triLim):
            cmds.select(self.triHold[i])
            triCount += cmds.polyEvaluate(self.triHold[i], faceComponent = True)

        # Iterating through the results to count the amount of faces found
        for i in range(0, quadLim):
            cmds.select(self.quadHold[i])
            quadCount += cmds.polyEvaluate(self.quadHold[i], faceComponent = True)



        # Iterating through the results to count the amount of faces found
        for i in range(0, nGonLim):
            cmds.select(self.nGonHold[i])
            nGonCount += cmds.polyEvaluate(self.nGonHold[i], faceComponent = True)


        cmds.selectType(allObjects = True)
        cmds.hilite(userHil)
        cmds.select(userSel)

        if self.triHold:
            triRep = '%d triangles found'%(triCount)
            perPoint = '.'

        if self.nGonHold:
            nGonRep = '%d n-gons found'%(nGonCount)
            perPoint = '.'
        
        if self.triHold and self.nGonHold:
            dualFind = ' and '
            
        return (triRep + dualFind + nGonRep + perPoint)


    #********** RUN FIX **********#
    
    # selects all non-quad faces
    def runFix(self):
        
        try:
            
            # Highlight the non quadrilateral polygons
            cmds.select(self.triHold + self.nGonHold)
            return "Non-quadrilaterals highlighted."
            
        except:
            
            return "There was a problem selecting the polygons."
            


#********** RETURN INSTANCE OF SCRIPT CLASS **********#

def getObject():
    return QuadScan()