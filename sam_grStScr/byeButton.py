import pymel.core as pm
shelfButtons=pm.shelfLayout("Custom", q=1, childArray=1)
for button in shelfButtons:
	label = ""
	# Assert that this is a shelfButton 
	if pm.objectTypeUI(button, isType="shelfButton"):
		label=str(pm.shelfButton(button, q=1, label=1))
		# If this button has the label we're looking for, 
		# delete the button. 
		if "helloButton" == label:
			pm.deleteUI(button)
