'''
********************************************

Add the following in comments to the top of the file:

File name -- be sure to check the naming conventions in the Grindstone documentation
Author(s)
Brief description of what this script does

********************************************
'''



'''
********************************************

Add whatever imports your script needs to run.
For example, if this was a script for Maya, you
would probably want to add this line:

import maya.cmds as cmds

********************************************
'''



class YourClass:

    '''
    ********************************************

    Replace "YourClass" with the name of your new script class.
    Name your class according the the conventions in the Grindstone documentation.

    ********************************************
    '''




    # ********** INIT **********#

    def __init__(self):

        # identify whether or not the script has an auto-fix function
        self.hasFix = False

        '''
        ********************************************

        Set hasFix to True if you will be implementing an auto-fix for this script, and False otherwise.
        This is how Grindstone knows whether or not to include an auto-fix button with the error this script generates.

        ********************************************
        '''





        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = "<your fix label>"

        '''
        ********************************************

        fixLabel is the text that will appear on the auto-fix button.
        If you are not implementing an auto-fix, you can just set it to an empty string.

        ********************************************
        '''




        # local data

        '''
        ********************************************

        Include any other local data for your script here.

        You can declare local data inside the doCheck() and runFix() functions, but anything that needs to be visible
        from BOTH functions NEEDS to be declared here.

        ********************************************
        '''

    # ********** DO CHECK **********#

    def doCheck(self):

        '''
        ********************************************

        This is where the main logic of your script should go. At the end, if an error was detected, return a string
        that describes the error. This is the string that will show up on the error list when your script is
        executed. If no error was detected, return an empty string.

        Examples:

        return "my script found an error!"

        or

        return ""

        ********************************************
        '''




    # ********** RUN FIX **********#

    def runFix(self):

        '''
        ********************************************

        This function is optional. If an auto-fix is possible for the error that this script addresses, then you can
        implement it here. At the end of your auto-fix logic, return a string that describes the auto-fix result -- i.e.
        whether or not it succeeded, and if it did, exactly what operation it performed.If you put an auto-fix function
        here, be sure to set the "hasFix" flag to "True" -- see above.

        Example:

        return "my script did these things to fix the error it found"

        ********************************************
        '''




# ********** RETURN INSTANCE OF SCRIPT CLASS **********#

def getObject():
    return YourClass()


'''
********************************************

Once again, replace "YourClass" with the name of your new script class.
This function is how Grindstone instantiates your script functionality.

********************************************
'''
