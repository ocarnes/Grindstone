class ScriptList:
    
    def __init__(self, name):
        self.name = name
        self.isChecked = 0
        self.scripts = []
        
        
    def append(self, object):
        self.scripts.append(object)
        
        
    def check(self):
        if self.isChecked:
            self.isChecked = 0
            
        else:
            self.isChecked = 1
            
            
    def doChecks(self):
        for s in self.scripts:
            s.doCheck()