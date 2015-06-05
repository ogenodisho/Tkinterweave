'''
This brushes.py module represents the different
kinds of paint tools and how they draw on the
global PhotoImage. All they need is a coordinate
and they will draw themselves based off that coord.

TODO - make scale and color globals in the global_config
       module rather than parameters.
TODO - exception handling for when the paint method x, y ends up
       painting stuff outside of the canvas' bounding box. Maybe
       just ignore them because they aren't crashing anything.
'''

import global_configs
import tool_names

# generic paint function that will paint using a
# tool based on the current global tool.
def paint(x, y, scale, color, reflected):
    if global_configs.CURRENT_TOOL == tool_names.PENCIL:
        draw_dot(x, y, scale, color)
    elif global_configs.CURRENT_TOOL == tool_names.SPRAY_CAN:
        spray_and_pray(x, y, scale, color)
    elif global_configs.CURRENT_TOOL == tool_names.CALLIGRAPHY_LEFT:
        if reflected:
            draw_backslash(x, y, scale, color)
        else:
            draw_forwardslash(x, y, scale, color)
    elif global_configs.CURRENT_TOOL == tool_names.CALLIGRAPHY_RIGHT:
        if reflected:
            draw_forwardslash(x, y, scale, color)
        else:
            draw_backslash(x, y, scale, color)

# draws a backslash, do not call directly - it will be called
# if the user has selected the calligraphy left tool
def draw_backslash(x, y, scale, color):
    # do something with the scale
    global_configs.IMG.put(color, (x + 5, y - 5))
    global_configs.IMG.put(color, (x + 4, y - 4))
    global_configs.IMG.put(color, (x + 3, y - 3))
    global_configs.IMG.put(color, (x + 2, y - 2))
    global_configs.IMG.put(color, (x + 1, y - 1))
    global_configs.IMG.put(color, (x    , y    ))
    global_configs.IMG.put(color, (x - 1, y + 1))
    global_configs.IMG.put(color, (x - 2, y + 2))
    global_configs.IMG.put(color, (x - 3, y + 3))
    global_configs.IMG.put(color, (x - 4, y + 4))
    global_configs.IMG.put(color, (x - 5, y + 5))

# draws a forwardslash, do not call directly - it will be called
# if the user has selected the calligraphy right tool
def draw_forwardslash(x, y, scale, color):
    # do something with the scale
    global_configs.IMG.put(color, (x - 5, y - 5))
    global_configs.IMG.put(color, (x - 4, y - 4))
    global_configs.IMG.put(color, (x - 3, y - 3))
    global_configs.IMG.put(color, (x - 2, y - 2))
    global_configs.IMG.put(color, (x - 1, y - 1))
    global_configs.IMG.put(color, (x    , y    ))
    global_configs.IMG.put(color, (x + 1, y + 1))
    global_configs.IMG.put(color, (x + 2, y + 2))
    global_configs.IMG.put(color, (x + 3, y + 3))
    global_configs.IMG.put(color, (x + 4, y + 4))
    global_configs.IMG.put(color, (x + 5, y + 5))

# TODO - create a tool that uses this cross
def draw_cross(x, y, scale, color):
    draw_forwardslash(x, y, scale, color)
    draw_backslash(x, y, scale, color)

# draws a dot, do not call directly - it will be called
# if the user has selected the pencil tool
def draw_dot(x, y, scale, color):
    # do something with the scale
    global_configs.IMG.put(color, (x, y))
##    global_configs.IMG.put(color, (x + 1, y    ))
##    global_configs.IMG.put(color, (x - 1, y    ))
##    global_configs.IMG.put(color, (x    , y + 1))
##    global_configs.IMG.put(color, (x    , y - 1))
##    global_configs.IMG.put(color, (x + 1, y - 1))
##    global_configs.IMG.put(color, (x + 1, y + 1))
##    global_configs.IMG.put(color, (x - 1, y - 1))
##    global_configs.IMG.put(color, (x - 1, y + 1))

def spray_and_pray(x, y, scale, color):
    # TODO - implement the spray can. Ideas: every time
    #        function is called, use the scale to draw
    #        like 3 or so dots in a random circular area
    #        centered around x, y.
    pass
