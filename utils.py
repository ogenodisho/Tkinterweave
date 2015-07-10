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

# converts "255 255 255" to #ffffff
def rgb_to_hex(rgb):
    rgb = tuple(int(x) for x in rgb.strip().split(" "))
    
    return "#" + '%02x%02x%02x' % rgb

# converts #ffffff to "255 255 255"
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    tuple_rgb = tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))
    return " ".join(str(x) for x in tuple_rgb)
    
