# import this script to a button in hda.

def build():

#   ######## variables ##############  
    self = hou.pwd()
    selfp = hou.pwd().position()
    sp0 = selfp[0]
    sp1 = selfp[1]
    main = hou.node('/obj')  
    cresx = self.parm('camresx').eval()
    cresy = self.parm('camresy').eval()
    
#    ###### scene scale null #########
    main_null = main.createNode('null', 'scene_scale')
    main_null.parm('scale').set(0.01)
    main_null.setPosition([0+sp0,-2+sp1])
    mp = main_null.position()
#    ########## cam null ############$
    cam_null = main.createNode('null', 'cameras')
    cam_null.setFirstInput(main_null)
    cam_null.setPosition([-15+sp0,-5+sp1])
    cmnp = cam_null.position() 
#    ########## env null ############$
    env_null = main.createNode('null', 'environemnts')
    env_null.setFirstInput(main_null)
    env_null.setPosition([-0+sp0,-5+sp1])
    enp = env_null.position()
#    ########## cars null ############$
    car_null = main.createNode('null', 'cars')
    car_null.setFirstInput(main_null)
    car_null.setPosition([15+sp0,-5+sp1])
    cnp = car_null.position()
    ######## import cameras #########    
    cam_count = self.parm('xn__importcamera_yla').eval()
    cc = 0
    while (cam_count > cc):
        cc += 1
        c = ('camera' + str(cc))
        camabc = self.parm(c ).eval()
        cam_path = str(camabc)
        cam_name = cam_path.split ('/')[-1][:-5]
        cam_arc = main.createNode('alembicarchive',cam_name)
        cam_arc.setFirstInput(cam_null)
        cam_arc.setPosition([cmnp[0]-cc,-cc])
        cam_arc.parm('fileName').set(cam_path)
        cam_xform = cam_arc.createNode('alembicxform',cam_name)
        cam_xform.parm('fileName').set(cam_path)
        cam_xform.parm('objectPath').set('/camera')
        cam_xform.setFirstInput(cam_arc.indirectInputs()[0])
        camera = cam_xform.createNode('cam',cam_name)
        camera.setFirstInput(cam_xform.indirectInputs()[0])
        camera.parm('resx').set(cresx)
        camera.parm('resy').set(cresy)

        
        
    ######## import env #########    
    env_count = self.parm('xn__importenv_bja').eval()
    ec = 0
    while (env_count > ec):
        ec += 1
        e = ('env' + str(ec))
        envabc = self.parm(e).eval()
        env_path = str(envabc)
        env_name = 'RENDER_GEO_' + env_path.split ('/')[-1][:-5]        
        env = main.createNode('geo',env_name)
        env.setFirstInput(env_null)
        env.setPosition([enp[0], ec])



    ######## import car #########    
    car_count = self.parm('xn__importcar_bja').eval()
    carc = 0
    while (env_count > carc):
        carc += 1
        c = ('car' + str(carc))
        carabc = self.parm(c).eval()
        car_path = str(carabc)
        car_name = 'RENDER_GEO_CAR_' + car_path.split ('/')[-1][:-5]        
        car = main.createNode('geo',car_name)
        car.setFirstInput(car_null)
        
        
    ######## layour nodes #########   
    #hou.node('/obj/').layoutChildren()
