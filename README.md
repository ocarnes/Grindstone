# Grindstone
#### *Sharpening your 3D Production with the touch of a button*

******************************************************************************
******************************************************************************


### Contents
- [Overview](https://github.com/sadams115/Grindstone/blob/master/README.md#overview)
- [Using Grindstone](https://github.com/sadams115/Grindstone/blob/master/README.md#using-grindstone)
  - [How to Access Grindstone](https://github.com/sadams115/Grindstone/blob/master/README.md#how-to-access-grindstone-in-maya)
  - [The Grindstone Interface](https://github.com/sadams115/Grindstone/blob/master/README.md#the-grindstone-interface)
    - [Running Checks](https://github.com/sadams115/Grindstone/blob/master/README.md#running-checks)
    - [Responding to Errors](https://github.com/sadams115/Grindstone/blob/master/README.md#responding-to-errors)
- [The Scripts](https://github.com/sadams115/Grindstone/blob/master/README.md#the-scripts)
  - [Common](https://github.com/sadams115/Grindstone/blob/master/README.md#common)
  - [Dynamics](https://github.com/sadams115/Grindstone/blob/master/README.md#dynamics)
  - [Enumeration](https://github.com/sadams115/Grindstone/blob/master/README.md#enumeration)
  - [Modeling](https://github.com/sadams115/Grindstone/blob/master/README.md#modeling)
- [Expanding Grindstone](https://github.com/sadams115/Grindstone/blob/master/README.md#expanding-grindstone)
  - [Grindstone Location](https://github.com/sadams115/Grindstone/blob/master/README.md#grindstone-location)
  - [Enabling/Disabling Grindstone](https://github.com/sadams115/Grindstone/blob/master/README.md#enablingdisabling-grindstone)
  - [Disabling Grindstone for Dev Work](https://github.com/sadams115/Grindstone/blob/master/README.md#disabling-grindstone-on-a-single-computer-for-dev-work)
  - [Adding Scripts](https://github.com/sadams115/Grindstone/blob/master/README.md#adding-scripts)
  - [Adding Categories](https://github.com/sadams115/Grindstone/blob/master/README.md#adding-categories)
  - [Naming Conventions](https://github.com/sadams115/Grindstone/blob/master/README.md#naming-conventions)
  
******************************************************************************
******************************************************************************

## Overview
&nbsp;&nbsp;&nbsp;&nbsp;Grindstone is a universal plug-in for any software suite in the 3D animation production workflow that comes with a distribution of PySide2. It allows users to easily write and deploy scripts that check their assets for errors before they are published.

******************************************************************************
******************************************************************************

## Using Grindstone

### How to Access Grindstone
Grindstone should be automatically loaded into any supported software suite. There is a [button](gs_decentralized/Common/GS_icon.png) in each of those suites that summons the Grindstone interface.

__Maya__ - look on the Custom shelf.

__Nuke__ - look at the top, on the Nuke main menu bar.

__Houdini__ - look on the DACTools shelf.

******************************************************************************

### The Grindstone Interface

#### Running Checks
To the left of the Grindstone interface are several checkboxes and a "Run" button. These checkboxes represent different categories of scripts. Each category is a bundle of scripts that are related to each other in some way (by pipeline stage, technology, etc.). The "+" icon to the left of each category will expand the selection and show you every script inside that category. After you make a selection of scripts to execute, simply press the "Run" button. A list of errors detected by the scripts you ran will populate to the right of the screen. A detailed list of what scripts are included in each category can be found [here](https://github.com/sadams115/Grindstone/blob/master/README.md#the-scripts).

#### Responding to Errors
Each entry in the error list will be accomanied by up to two response options. The first is to ignore the error in the event that there is no auto-fix available or you want to address the issue manually. Errors with an available auto-fix will include a second option to execute that auto-fix. The text on the auto-fix button itself briefly describes what the auto-fix will do. A detailed list of available auto-fixes and exactly what they do can be found [here](https://github.com/sadams115/Grindstone/blob/master/README.md#the-scripts).

******************************************************************************

******************************************************************************

## The Scripts

### Maya

#### **Common**

###### File Type MA
- This script checks to see if your file is a Maya Ascii file. There is no auto-fix for this check.

###### Non-Deformer History
- This script checks to see if your file has any non-deformer history. The auto-fix for this script simply deletes any non-deformer history.

###### Non-Local File Paths
- This script checks for any non-local file paths in your file. There is no auto-fix for this check.

#### **Dynamics**

###### Unused Nodes
- This script checks for any unused/unknown nodes in your file. The auto-fix for this script will unlock and delete all unused nodes in the file.

#### **Enumeration**

###### Animation Node Enumeration
- This script enumerates the animation nodes in your scene. There is no auto-fix for this script.

###### Camera Node Enumeration
- This script enumerates the camera nodes in your scene. There is no auto-fix for this script.

###### Deformer Node Enumeration
- This script enumerates the deformer nodes in your scene. There is no auto-fix for this script.

###### Dynamics Node Enumeration
- This script enumerates the dynamics nodes in your scene. There is no auto-fix for this script.

###### Geometry Node Enumeration
- This script enumerates the geometry nodes in your scene. There is no auto-fix for this script.

###### Image Plane Node Enumeration
- This script enumerates the image plane nodes in your scene. There is no auto-fix for this script.

###### Lighting Node Enumeration
- This script enumerates the lighting nodes in your scene. There is no auto-fix for this script.

###### Shader Node Enumeration
- This script enumerates the shader nodes in your scene. There is no auto-fix for this script.

###### Texture Node Enumeration
- This script enumerates the texture nodes in your scene. There is no auto-fix for this script.

###### Utilities Node Enumeration
- This script enumerates the utilities nodes in your scene. There is no auto-fix for this script.

#### **Modeling**

###### Camera Count
- This script ensures that only the four default cameras are present in your scene. The auto-fix will delete any additional cameras in the scene.

###### Frozen Transforms
- This script will check that the transforms are frozen in the scene. The auto-fix freezes transforms for you.

###### Non-Quads
- This script scans for non-quadrilateral geometry in your scene such as triangles or n-gons. The auto-fix will highlight any non-quads in your scene.

###### UVs
- This script will make sure that all geometry has a UV map. There is no auto-fix for this script.


******************************************************************************


### Nuke

#### Currently, there are no productions scripts for Nuke


******************************************************************************


### Houdini

#### Currently, there are no productions scripts for Houdini

******************************************************************************
******************************************************************************

## Expanding Grindstone

### Grindstone Location
Grindstone's production code can be broken into two categories: common assets and software-specific assets.

__Common__ - Grindstone's common assets are located at `P:/lib/python/Grindstone`. They govern the GS user interface; the piece that every software suite has in common.

__Software-Specific__ - Grindstone's software-specific assets are located at `P:/apps/<software suite>/common/DACTools/Grindstone`. They include the software-specific scripts that Grindstone exposes to users as well as the plug-in component that loads Grindstone into the software suite.

When a software suite starts up, the DAC pipeline infrastructure (__not controlled by Grindstone__) instructs the suite to process Grindstone's plugin-component from the software-specific assets. The plug-in component acquires and instantiates the common Grindstone assets, passing them the location of the scripts so that the GS window can show them to users.

******************************************************************************
### Enabling/Disabling Grindstone
Grindstone loads into software suites automatically because the DAC pipeline infrastructure instructs each supported suite to plug it in on startup. Those instructions depend on the software suite in question.

__Maya__ - Currently, Grindstone is loaded into Maya on lines 10 - 13 of `P:/apps/maya/common/userSetup.py`. Simply commenting out these lines will disable Grindstone in Maya. Un-commenting them will re-enable Grindstone in Maya.

__Nuke__ - Currently, Grindstone is loaded into Nuke on line 23 of `P:/apps/nuke/common/init.py`. Commenting out this line will disable Grindstone in Nuke. Un-commenting it will re-enable Grindstone in Nuke.

__Houdini__ - Currently, Grindstone is not being loaded automatically in Houdini. This is because the DAC pipeline infrastructure for Houdini has yet to be truly built. That said, there is a file in place that should load Grindstone automatically if the rest of the pipeline infrastructure points Houdini to it -- `P:/apps/houdini/common/456.py`. For now, the file serves only to load Grindstone.

******************************************************************************
### Disabling Grindstone on a Single Computer for Dev Work
Sometimes a developer might need to test Grindstone in various suites without disrupting the production versions. In such a case, follow these steps to disable Grindstone for a single computer:

- go to the start menu and type "environment" into the search bar
- select "edit environment variables for your account"
  - NOTE: you probably do not have permission to do it, but __do not__ edit the system environment variables
- at the top of the variables window, select `New...`
- for variable name, put "PYTHONPATH"
- for variable value, put any string; "stub" for example
- click `OK` to create the new environment variable
- click `OK` at the bottom of the variable window to save your changes

At this point, you have overridden the system's "PYTHONPATH" variable, meaning that GS-supported software suites will no longer know where to find the production GS assets. This allows you to set up your own local GS infrastructure and plug it in to each suite manually.

When you want to restore the system "PYTHONPATH" so that Grindstone will auto-load again, simiply re-open the __account__ environment variables window, select your stub "PYTHONPATH" and delete it.

******************************************************************************

### Adding Scripts
Adding scripts to Grindstone is the same process regardless of which software suite you are working with. Simply follow these steps:
- To add a new script to Grindstone, start by downloading the [script template](references/gs_template.py). Save template as a new script class file, keeping in mind the [Grindstone naming conventions](references/Grindstone_Naming_Conventions.txt). The name should reflect the error that the new script checks for, and each script should check for only a single error. 

- Place your new script file in one of the category folders, or [create a new category](https://github.com/sadams115/Grindstone/blob/master/README.md#adding-categories). Category folders are located at `P:/apps/<software suite>/common/DACTools/Grindstone` in a `gs-scripts` folder. Depending on the suite, the `gs_scripts` folder may be at different levels, but never more than a couple levels down.

- Next, go through the template code and follow the instructions in every block comment. When you have completed the tasks outlined in each block comment, your new script will be automatically imported into Grindstone. Your `doCheck()` function will be run when the category is executed, and your `runFix()` function (if you implemented one) will be attached to the auto-fix button that accompanies your script's error report.

- **Don't forget to add a description of your new script to the documentation [here](https://github.com/sadams115/Grindstone/blob/master/README.md#the-scripts).**

******************************************************************************

### Adding Categories
If there is a bundle of scripts that apply to the same general problem set, you may want to construct another category. This may occur if you want to add a new pipeline stage or if you are working with a specific technology that brings its own set of errors. Fear not -- creating a new category is as easy as making a new folder in the `gs_scripts` directory and making or copying a blank `__init__.py` in that new folder (a blank `__init__.py` file tells python that the directory is safe to import from). The name of the folder you created will be exposed in Grindstone as a new checkbox, and any scripts you put into that folder will be available if you expand the new box. **Don't forget to add your new category to the documentation [here](https://github.com/sadams115/Grindstone/blob/master/README.md#the-scripts).**

******************************************************************************

### Naming Conventions
A full guide to Grindstone conventions can be found [here](references/Grindstone_Naming_Conventions.txt).
