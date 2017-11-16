# Grindstone gs_UnusedNodes_class.py
# Authors: Sam Carnes and Sean Adams

# This file defines a script that checks for unknown nodes and deletes them
# Here are the lines of MEL that it replicates:
# select `ls -type unknown`;
# lockNode -lock false;
# delete;


import maya.cmds as cmds

class UnusedNodes:
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = True
        
        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = "Delete unknown nodes"
        
        
        # class data
        self.unknownNodes = []
        self.numberOfUnknownNodes = 0
       
        
        
    #********** DO CHECK **********#
    
    def doCheck(self):
        
        # get the list of all unknown nodes
        self.unknownNodes = cmds.ls(type='unknown')
        
        # determine how many cameras there are
        self.numberOfUnknownNodes = len(self.unknownNodes)
        
        if self.numberOfUnknownNodes > 0:
            returnString = str(self.numberOfUnknownNodes) + " unknown nodes detected."
            return returnString
            
        else:
            return ''
            
    
    
    #********** RUN FIX **********#
    
    # deletes any unknown nodes
    def runFix(self):
        
        # counts the number of unknown nodes that get deleted
        deletedNodes = 0
        
        # try the fix
        try:
            
            # for all the unknown nodes, unlock and delete them
            for node in unknownNodes:
                cmds.lockNode( node, lock=False )
                cmds.delete( node )
                deletedNodes++
            
            
            # determine if there "was an unknown node" or "were unknown nodes"
            if deletedNodes > 1:
                pluralOrSingular = "nodes"
            else:
                pluralOrSingular = "node"
                
            # return the result
            return str(deletedNodes) + " unknown " + pluralOrSingular + " deleted."
            
        # if the fix doesn't work, return an error message
        except:
            
            return "There was a problem deleteing the unknown nodes."
        
        
        
#********** RETURN INSTANCE OF SCRIPT CLASS **********#
        
def getObject():
    return UnusedNodes()