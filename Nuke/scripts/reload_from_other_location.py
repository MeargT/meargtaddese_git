# ==================================================
# this will convert all read nodes and
# update their paths to another drive location
# and put all that to a menu
# ==================================================

import nuke
import os 

def load_from_amd():
    node_type = "Read"
    oldD = "D:/"
    oldF = "F:/"
    newD = "Z:/"
    newF = "Y:/"

    for read in nuke.allNodes("Read"):
        path = read.knob('file').value()
        path = path.replace(oldD, newD)
        read.knob('file').setValue(path)
        read.knob('colorspace').setValue('ACES - ACEScg')
        path_dir = os.path.dirname(path)
        if os.path.exists(path_dir):
            for read in nuke.allNodes("Read"):
                path = read.knob('file').value()
                path = path.replace(oldF, newF)
                read.knob('file').setValue(path)
                read.knob('colorspace').setValue('ACES - ACEScg')
    nuke.root()["workingSpaceLUT"].setValue('ACES - ACEScg')


nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')


toolbar = nuke.menu('Nodes')
myMenu = toolbar.findItem('meargMenu')
if myMenu:
    myMenu.clearMenu()
else:
    myMenu = toolbar.addMenu('markMenu', icon='mark_logo.png')
    myMenu.addCommand('load from AMD', lambda: load_from_amd())
