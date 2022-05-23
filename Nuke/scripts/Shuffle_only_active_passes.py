import nuke 
 
# import exr file and get passes 
read_exr = nuke.nodes.Read() 
read_exr.knob('file').setValue('C:/Users/Lili/Desktop/Mearg/RND/test_render.exr') 
all_passes = read_exr.channels() 
 
 
# check if pass is empty 
active = [] 
for per in all_passes: 
    va = nuke.sample(read_exr, per, 5, 5, 1280, 720) 
    if va != 0: 
        print(per) 
        active.append(per) 
    else: 
        print(per) 
 
# get name of the pass, and remove the rgb redundancy   
new_active = [] 
for x in active: 
    cc = x.split('.') 
    ce = cc[0] 
    print(ce) 
    new_active.append(ce) 
 
# create shuffle noe for each node 
new_active = set(new_active) 
i=1 
old=nuke.nodes.Shuffle() 
for y in new_active:    
    shuff = nuke.nodes.Shuffle() 
    shuff.setInput(0,read_exr) 
    shuff.knob('in').setValue(y) 
    shuff.knob('postage_stamp').setValue(1) 
    shuff['name'].setValue('Shuffle_' + y) 
    if i==1: 
        old=shuff 
    elif i==2: 
        merge=nuke.nodes.Merge() 
        merge.setInput(0,old) 
        merge.setInput(1,shuff) 
        old=merge 
     
    else: 
        merge=nuke.nodes.Merge() 
        merge.setInput(0,old) 
        merge.setInput(1,shuff) 
        old=merge 
    i+=1
