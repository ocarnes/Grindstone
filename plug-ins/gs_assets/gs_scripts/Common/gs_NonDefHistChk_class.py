# Grindstone gs_NonDefHistChk_class.py
# Authors: Sam Carnes and Sean Adams

# This file scans every DAG object in the scene and checks for any non-deformer history.
# The script returns a true or false depending on the results

import pymel.core as pm

class NonDefHistCheck:
    
    
    def __init__(self):
        self.hasFix = False
    
    
    def doCheck(self):
        
        # Select all DAG objects in the scene and set them to an array
        sceneSel = pm.ls(dagObjects = True)
        
        # Set up elements for iterating through the selection
        objInd = 0
        nonDefTag = ''
        
        for someObj in sceneSel:
            nonDefChk = [n for n in sceneSel[objInd].history(il=1,pdo=True) if not isinstance(n, pm.nodetypes.GeometryFilter)]
            objInd += 1
            
            if nonDefChk:
                nonDefTag = 'Non-Deformer History detected.'
                break
        
        return nonDefTag


def getObject():
    return NonDefHistCheck()