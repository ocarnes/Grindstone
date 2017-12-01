# Grindstone
## *Sharpening your 3D Production with the touch of a button*


### Contents
- [Overview](https://github.com/sadams115/Grindstone/blob/master/README.md#overview)
- [Using Grindstone](https://github.com/sadams115/Grindstone/blob/master/README.md#using-grindstone)
  - [How to Access Grindstone In Maya](https://github.com/sadams115/Grindstone/blob/master/README.md#how-to-access-grindstone-in-maya)
  - [The Grindstone Interface](https://github.com/sadams115/Grindstone/blob/master/README.md#the-grindstone-interface)
    - Running Checks
    - Responding to Errors
  - [The Categories](https://github.com/sadams115/Grindstone/blob/master/README.md#the-categories)
    - Common
    - Dynamics
    - Modeling
- [Expanding Grindstone](https://github.com/sadams115/Grindstone/blob/master/README.md#expanding-grindstone)
  - [Grindstone Location](https://github.com/sadams115/Grindstone/blob/master/README.md#grindstone-location)
  - [Adding Scripts](https://github.com/sadams115/Grindstone/blob/master/README.md#adding-scripts)
  - [Adding Categories](https://github.com/sadams115/Grindstone/blob/master/README.md#adding-categories)
  - [Naming Conventions](https://github.com/sadams115/Grindstone/blob/master/README.md#naming-conventions)

## Overview
&nbsp;&nbsp;&nbsp;&nbsp;Grindstone is a plug-in for the Maya 3D modeling software that will help streamline a team- based 
computer animation production workflow. The workflow of most 3D animation productions is the 
pipeline – essentially an assembly line in which a complete product is assembled as it passes 
through multiple stages of work. The problem that arises in such a process is that occasionally 
objects arrive at a stage either incomplete or with defects that should have been corrected in the 
previous stage. Grindstone aims to solve that problem by sitting between stages of the pipeline and 
ensuring that any object passing from one stage to another is complete and error-free.

&nbsp;&nbsp;&nbsp;&nbsp;Targeting an initial set of errors provided by the UC Denver Digital Animation Center (DAC), 
Grindstone was constructed using the Maya Python API to expose a selection of error-checking and 
error-correcting functionality with the touch of a button. At its core, Grindstone is a script 
deployment platform that allows developers to register their own error-checks/fixes and present 
them to users simply by dropping their scripts in the Grindstone scripts directory. Any groups of 
scripts that apply to the same pipeline stage or technology can be grouped together in a 
subdirectory and presented as a single sequence of scripts through the Grindstone interface.
Although the primary component of this project is the script platform itself, Grindstone currently
contains several scripts that address most of the initial set of errors identified by the DAC.



## Using Grindstone

### How to Access Grindstone In Maya
The production version of Grindstone is automatically loaded into Maya on startup. You can summon the Grindstone interface through a [button](plug-ins/gs_assets/GS_icon.png) on the Custom shelf.


### The Grindstone Interface

#### Running Checks
To the left of the Grindstone interface are several checkboxes and a "Run" button. These checkboxes represent different categories of scripts. Each category is a bundle of scripts that are related to each other in some way (by pipeline stage, technology, etc.). After you make a selection of categories to execute, simply press the "Run" button. A list of errors detected by the scripts you ran will populate to the right of the screen. A detailed list of what scripts are included in each category can be found [here](https://github.com/sadams115/Grindstone/blob/master/README.md#the-categories).

#### Responding to Errors
Each entry in the error list will be accomanied by up to two response options. The first is to ignore the error in the event that there is no auto-fix available or you want to address the issue manually. Errors with an available auto-fix will include a second option to execute that auto-fix. The text on the auto-fix button itself briefly describes what the auto-fix will do. A detailed list of available auto-fixes and exactly what they do can be found [here](https://github.com/sadams115/Grindstone/blob/master/README.md#the-categories).


### The Categories

#### Common

##### File Type MA
This script checks to see if your file is a Maya Ascii file. There is no auto-fix for this check.

##### Non-Deformer History
This script checks to see if your file has any non-deformer history. The auto-fix for this script simply deletes any non-deformer history.

##### Non-Local File Paths
This script checks for any non-local file paths in your file. There is no auto-fix for this check.

#### Dynamics

#### Modeling




## Expanding Grindstone

### Grindstone Location


### Adding Scripts


### Adding Categories


### Naming Conventions
A full guide to Grindstone conventions can be found [here](references/Grindstone_Naming_Conventions.txt).
