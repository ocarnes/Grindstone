def initUI(self):        
    #Create combo box (drop-down menu) and add menu items 
    self.combo = QComboBox(self)        
    self.combo.addItem( 'Cone' )        
    self.combo.addItem( 'Cube' )        
    self.combo.addItem( 'Sphere' )        
    self.combo.addItem( 'Torus' )        
    self.combo.setCurrentIndex(0)        
    self.combo.move(20, 20)        
    self.combo.activated[str].connect(self.combo_onActivated)        

    #Create 'Create' button
    self.button = QPushButton('Create', self)        
    self.button.move(20, 50)        
    self.button.clicked.connect(self.button_onClicked)                    

#Change commmand string when combo box changes
def combo_onActivated(self, text):        
    self.cmd = 'poly' + text + '()'            

#Execute MEL command when button is clicked
def button_onClicked(self):        
    mel.eval( self.cmd )   