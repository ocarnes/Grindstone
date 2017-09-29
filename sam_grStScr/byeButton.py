#File in progress, do not execute

import maya.cmds

string shelfButtons[] = cmds.shelfLayout("Custom",q=1,ca=1)

for ( tarButton in shelfButtons )
{
   string label;

   if(cmds.objectTypeUI(tarButton) == "shelfButton")
   {
      label = cmds.shelfButton(tarButton,q=1,label=1)

      if ( "helloButton" == $label )
         deleteUI $button
   }
}