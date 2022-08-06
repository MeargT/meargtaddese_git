import nuke

def update_path():
	# set project directory
	nuke.thisRoot().knob("project_directory").setValue("[python {nuke.script_directory()}]")
	# update path for beauty 
	node_type = "Read"
	for read in nuke.allNodes(node_type):
	    old_path = read.knob('file').value()
	    path = read.knob('file').getValue()
	    full_path = path.split('/render/')
	    relative_path = '../FX'
	    updated_path = relative_path + '/render/' + full_path[1]
	    set_path = path.replace(old_path, updated_path)
	    print(set_path)
	    read.knob('file').setValue(set_path)
	# update path for deep 
	node_type = "DeepRead"
	for read in nuke.allNodes(node_type):
	    old_path = read.knob('file').value()
	    path = read.knob('file').getValue()
	    full_path = path.split('/render/')
	    relative_path = '../FX'
	    updated_path = relative_path + '/render/' + full_path[1]
	    set_path = path.replace(old_path, updated_path)
	    print(set_path)
	    read.knob('file').setValue(set_path)

def reload_all():
	#reload all read nodes
	node_type = "Read"
	for read in nuke.allNodes(node_type):
	    read.knob('reload').execute()
	node_type = "DeepRead"
	for read in nuke.allNodes(node_type):
	    read.knob('reload').execute()

toolbar = nuke.menu('Nodes')
myMenu = toolbar.findItem('ElementX')
if myMenu:
    myMenu.clearMenu()
else:
    myMenu = toolbar.addMenu('ElementX', icon='elemx.png')
myMenu.addCommand('relative path', lambda: update_path())
myMenu.addCommand('relaod path', lambda: reload_all())
