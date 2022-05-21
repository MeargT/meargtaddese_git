import random
import nuke

'''
since different OS has different slash and backslash use
can be useful for later use, currently not.
'''

wd = ':/' #wd is short for windows drive
wp = '/'  #wp is short for windows path

# get info from knobs
mine = nuke.thisNode()
gDrv = mine.knob("Drive").value()
gProj = mine.knob("proj_title").value()
gSeq = mine.knob("seq").value()
gShot = mine.knob("shot").value()
gVer = int(mine.knob("ver").value())
gVer = format(gVer, "03")
gFFrame = mine.knob("FFrame").value()
gLFrame = mine.knob("LFrame").value()

# set folder structure, project setting and project file
path = gDrv + wd + gProj + wp + gSeq + wp + gShot + wp + 'comp/'
name = gShot + '_v' + str(gVer) + '.nk'
nuke.scriptSaveAs(path + name)
nuke.root()['project_directory'].setValue('[python {nuke.script_directory()}]')
nuke.root()['first_frame'].setValue(gFFrame)
nuke.root()['last_frame'].setValue(gLFrame)

# give message for the artist, for motivation
messages = ['All set! Happy compsiting','Good luck with your Nuke','Let\'s get shots done!','This shot is fun']
line = random.choice(messages)
nuke.message(line)
