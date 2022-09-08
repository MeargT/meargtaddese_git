#set path for texture files
texPath = hou.ui.selectFile(title = "where is your material folder", file_type = hou.file)
foldername = hou.expandString(texPath)
folderlist = foldername.split('/')
lent = len(folderset)

#create nodes
obj = hou.node('/mat')
dlmat = obj.createNode('dlMaterialBuilder', folderlist[lent-2])
dlmain = dlmat.createNode('dlprincipled', folderlist[lent-2])
dlter = hou.node(dlmat.path() + '/dlTerminal')

#set parameters for nodes
dltex_dif = dlmat.createNode('dlTexture', "Diffuse")
dltex_dif.parm("textureFile").set(texPath + "diffuse_mat.exr")
dltex_rough = dlmat.createNode('dlTexture',"Roughness")
dltex_rough.parm("textureFile").set(texPath + "rough_mat.exr")
dltex_rough.parm("tileRemoval").set(1)

# node connections
dlmain.setInput(0,dltex_dif)
dlmain.setInput(1,dltex_rough)
dlter.setInput(0,dlmain)
dlmat.layoutChildren()
