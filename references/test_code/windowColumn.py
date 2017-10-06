import maya.cmds as mc

mc.window(title="helloWindow", wh = (640, 480))
mc.columnLayout("testColumn", adjustableColumn = True)
mc.text("testText", label = "Hello World", width = 20, height = 20, backgroundColor = [0.1, 0.1, 0.1], parent = "testColumn")
mc.showWindow()
