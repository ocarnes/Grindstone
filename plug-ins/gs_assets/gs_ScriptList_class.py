# Grindstone gs_ScriptList_class.py
# Authors: Sam Carnes and Sean Adams

# This file defines a class that can represent a directory of scripts

class ScriptList:
    
    #********** INIT **********#
    
    # takes a directory name
    # initializes internal data
    def __init__(self, name):
        self.name = name
        self.isChecked = 0
        self.scripts = []
        
        
        
    #********** APPEND **********#
        
    # takes a script object
    # adds the script to the scripts array
    def append(self, object):
        self.scripts.append(object)
        
        
        
    #********** CHECK **********#
        
    # toggle whether or not this object will run its scripts
    def check(self):
        if self.isChecked:
            self.isChecked = 0
            
        else:
            self.isChecked = 1
            
            
            
    #********** DO CHECKS **********# DEPRECATED
            
    # executes every script in the scripts array
    def doChecks(self):
        for s in self.scripts:
            s.doCheck()