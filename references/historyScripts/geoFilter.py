import maya.cmds as mc

typesNames = ["DeformFunc", "DeformerFunc", "geometryFilter"]

for typeName in typesNames:
    print "--"
    try:
        print "Inherited for {0}".format(typeName)
        print mc.nodeType(typeName, isTypeName=True, inherited=True)
        print "Derived for {0}".format(typeName)
        print mc.nodeType(typeName, isTypeName=True, derived=True)
    except RuntimeError, e:
        print "Error with type: {0}. {1}".format(typeName, e)