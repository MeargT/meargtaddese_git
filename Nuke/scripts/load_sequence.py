def load_seq():
    read_node = nuke.selectedNode()
    render_path = read_node.knob('file').getValue()
    get_loc = os.path.dirname(render_path)


    for seq in nuke.getFileNameList(get_loc):
        readNode = nuke.createNode('Read')
        readNode.knob('file').fromUserText(get_loc + '//'+ seq)


nuke.menu('Nuke').addCommand( 'load_seq', load_seq, "alt+w")
