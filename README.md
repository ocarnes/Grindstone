# Grindstone
#### *Sharpening your 3D Production with the touch of a button*

******************************************************************************
******************************************************************************


### Contents
- [Overview](https://github.com/sadams115/Grindstone/blob/master/README.md#overview)
- [Using Grindstone](https://github.com/sadams115/Grindstone/blob/master/README.md#using-grindstone)
  - [How to Access Grindstone In Maya](https://github.com/sadams115/Grindstone/blob/master/README.md#how-to-access-grindstone-in-maya)
  - [The Grindstone Interface](https://github.com/sadams115/Grindstone/blob/master/README.md#the-grindstone-interface)
    - [Running Checks](https://github.com/sadams115/Grindstone/blob/master/README.md#running-checks)
    - [Responding to Errors](https://github.com/sadams115/Grindstone/blob/master/README.md#responding-to-errors)
  - [The Categories](https://github.com/sadams115/Grindstone/blob/master/README.md#the-categories)
    - [Common](https://github.com/sadams115/Grindstone/blob/master/README.md#common)
    - [Dynamics](https://github.com/sadams115/Grindstone/blob/master/README.md#dynamics)
    - [Enumeration](https://github.com/sadams115/Grindstone/blob/master/README.md#enumeration)
    - [Modeling](https://github.com/sadams115/Grindstone/blob/master/README.md#modeling)
- [Expanding Grindstone](https://github.com/sadams115/Grindstone/blob/master/README.md#expanding-grindstone)
  - [Grindstone Location](https://github.com/sadams115/Grindstone/blob/master/README.md#grindstone-location)
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

### How to Access Grindstone In Maya
The production version of Grindstone is automatically loaded into Maya on startup. You can summon the Grindstone interface through a [button](plug-ins/gs_assets/GS_icon.png) on the Custom shelf.

******************************************************************************

### The Grindstone Interface

#### Running Checks
To the left of the Grindstone interface are several checkboxes and a "Run" button. These checkboxes represent different categories of scripts. Each category is a bundle of scripts that are related to each other in some way (by pipeline stage, technology, etc.). After you make a selection of categories to execute, simply press the "Run" button. A list of errors detected by the scripts you ran will populate to the right of the screen. A detailed list of what scripts are included in each category can be found [here](https://github.com/sadams115/Grindstone/blob/master/README.md#the-categories).

#### Responding to Errors
Each entry in the error list will be accomanied by up to two response options. The first is to ignore the error in the event that there is no auto-fix available or you want to address the issue manually. Errors with an available auto-fix will include a second option to execute that auto-fix. The text on the auto-fix button itself briefly describes what the auto-fix will do. A detailed list of available auto-fixes and exactly what they do can be found [here](https://github.com/sadams115/Grindstone/blob/master/README.md#the-categories).

******************************************************************************

### The Categories

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
******************************************************************************

## Expanding Grindstone

### Grindstone Location
Grindstone's production code is located at `P:/apps/maya/common/DACTools/Grindstone`. Any production-ready changes to Grindstone can be made here. It is recommended that you develop scripts away from the production version, as any errors in your script will propogate across all computers in the DAC. If you would like to test with Grindstone outside of the production environment, you can simply copy the contents of the `P:/apps/maya/common/DACTools/Grindstone` directory into `Documents/maya/2018/plug-ins`.

******************************************************************************

### Adding Scripts
These steps outline the process of adding scripts to Grindstone:
- To add a new script to Grindstone, start by downloading the [script template](references/gs_template.py). Save template as a new script class file, keeping in mind the [Grindstone naming conventions](references/Grindstone_Naming_Conventions.txt). The name should reflect the error that the new script checks for, and each script should check for only a single error. 

- Place your new script file in one of the category folders, or [create a new category](https://github.com/sadams115/Grindstone/blob/master/README.md#adding-categories). 

- Next, go through the template code and follow the instructions in every block comment. When you have completed the tasks outlined in each block comment, your new script will be automatically imported into Grindstone. Your `doCheck()` function will be run when the category is executed, and your `runFix()` function (if you implemented one) will be attached to the auto-fix button that accompanies your script's error report.

- **Don't forget to add a description of your new script to the documentation [here](https://github.com/sadams115/Grindstone/blob/master/README.md#the-categories).**

******************************************************************************

### Adding Categories
If there is a bundle of scripts that apply to the same general problem set, you may want to construct another category. This may occur if you want to add a new pipeline stage or if you are working with a specific technology that brings its own set of errors. Fear not -- creating a new category is as easy as making a new folder in the `gs_scripts` directory and making or copying a blank `__init__.py` in that new folder (a blank `__init__.py` file tells python that the directory is safe to import from). The name of the folder you created will be exposed in Grindstone as a new checkbox, and any scripts you put into that folder will be executed if you check the new box and press the "Run" button. **Don't forget to add your new category to the documentation [here](https://github.com/sadams115/Grindstone/blob/master/README.md#the-categories).**

******************************************************************************

### Naming Conventions
A full guide to Grindstone conventions can be found [here](references/Grindstone_Naming_Conventions.txt).
