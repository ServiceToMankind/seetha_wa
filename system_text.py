import os

def system_text():
    # load text 
    with open("system_text/init.txt") as f:
        init_text = f.read()
    with open("system_text/board_members/president.txt") as f:
        president_text = f.read()
    with open("system_text/board_members/vicepresident.txt") as f:
        vice_president_text = f.read()
    with open("system_text/board_members/secretary.txt") as f:
        secretary_text = f.read()
    with open("system_text/board_members/treasurer.txt") as f:
        treasurer_text = f.read()
    # jointsecretary 
    with open("system_text/board_members/jointsecretary.txt") as f:
        jointsecretary_text = f.read()
    # executives
    with open("system_text/board_members/executives.txt") as f:
        executives_text = f.read()
    # misc
    with open("system_text/board_members/misc.txt") as f:
        misc_text = f.read()
    # add all text in single variable
    system_text = init_text + president_text + vice_president_text + secretary_text + treasurer_text + jointsecretary_text + executives_text + misc_text
    
    return system_text