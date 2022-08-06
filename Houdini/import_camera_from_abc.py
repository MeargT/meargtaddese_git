import hou

#import camera

cam_path = hou.ui.selectFile(title = 'pick a camera', file_type = hou.fileType.Alembic)

main = hou.node('/obj')
cam_name = 'render_camera'
cam_arc = main.createNode('alembicarchive',cam_name)
cam_arc.parm('fileName').set(cam_path)
cam_xform = cam_arc.createNode('alembicxform',cam_name)
cam_xform.parm('fileName').set(cam_path)
cam_xform.parm('objectPath').set('/camera')
cam_xform.setFirstInput(cam_arc.indirectInputs()[0])
camera = cam_xform.createNode('cam',cam_name)
camera.setFirstInput(cam_xform.indirectInputs()[0])


#import env
cam_path = hou.ui.selectFile(title = 'pick a environment files', file_type = hou.fileType.Alembic)


def build():
    print('hello world!')
    #camabc = hou.parm('/obj/subnet1/camera3').eval()
    cam_path = str(camabc)

    main = hou.node('/obj')
    cam_name = 'render_camera'
    cam_arc = main.createNode('alembicarchive',cam_name)
    cam_arc.parm('fileName').set(cam_path)
    cam_xform = cam_arc.createNode('alembicxform',cam_name)
    cam_xform.parm('fileName').set(cam_path)
    cam_xform.parm('objectPath').set('/camera')
    cam_xform.setFirstInput(cam_arc.indirectInputs()[0])
    camera = cam_xform.createNode('cam',cam_name)
    camera.setFirstInput(cam_xform.indirectInputs()[0])
