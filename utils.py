'''
This module is just for random/helpful utility methods
that many other modules may find useful.
'''

# Returns a tuple of coords that represent
# (in order) the width, height, xPos, yPos of a window.
def get_window_geometry(window):
    l = []
    curr_value = ""
    
    for letter in window.geometry():
        if letter.isdigit():
            curr_value += letter
        else:
            l.append(curr_value)
            curr_value = ""
    l.append(curr_value)
    
    return tuple(map(int, l))

# Returns a geometry string from a tuple of coords that represent
# (in order) the width, height, xPos, yPos of a window.
def get_window_geometry_string(window_geometry):
    return "%dx%d+%d+%d" % (window_geometry[0],
                            window_geometry[1],
                            window_geometry[2],
                            window_geometry[3])
    
