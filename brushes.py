'''
All of these functions represent different styles
of painting. Calligraphy pens, brushes, spray can etc.
They each take four parameters.

    img - the photoimage to draw on
    x - the x pos of the click
    y - the y pos of the click
    scale - how big to draw the paint
    color - hex value e.g. #ffffff
'''

import global_configs
import tool_names

def paint(img, x, y, scale, color, reflected):
    if global_configs.CURRENT_TOOL == tool_names.PENCIL:
        draw_dot(img, x, y, scale, color)
    elif global_configs.CURRENT_TOOL == tool_names.SPRAY_CAN:
        draw_dot(img, x, y, scale, color)
    elif global_configs.CURRENT_TOOL == tool_names.CALLIGRAPHY_LEFT:
        if reflected:
            draw_backslash(img, x, y, scale, color)
        else:
            draw_forwardslash(img, x, y, scale, color)
    elif global_configs.CURRENT_TOOL == tool_names.CALLIGRAPHY_RIGHT:
        if reflected:
            draw_forwardslash(img, x, y, scale, color)
        else:
            draw_backslash(img, x, y, scale, color)

def draw_backslash(img, x, y, scale, color):
    # do something with the scale
    img.put(color, (x + 5, y - 5))
    img.put(color, (x + 4, y - 4))
    img.put(color, (x + 3, y - 3))
    img.put(color, (x + 2, y - 2))
    img.put(color, (x + 1, y - 1))
    img.put(color, (x    , y    ))
    img.put(color, (x - 1, y + 1))
    img.put(color, (x - 2, y + 2))
    img.put(color, (x - 3, y + 3))
    img.put(color, (x - 4, y + 4))
    img.put(color, (x - 5, y + 5))

def draw_forwardslash(img, x, y, scale, color):
    # do something with the scale
    img.put(color, (x - 5, y - 5))
    img.put(color, (x - 4, y - 4))
    img.put(color, (x - 3, y - 3))
    img.put(color, (x - 2, y - 2))
    img.put(color, (x - 1, y - 1))
    img.put(color, (x    , y    ))
    img.put(color, (x + 1, y + 1))
    img.put(color, (x + 2, y + 2))
    img.put(color, (x + 3, y + 3))
    img.put(color, (x + 4, y + 4))
    img.put(color, (x + 5, y + 5))


def draw_cross(img, x, y, scale, color):
    draw_forwardslash(img, x, y, scale, color)
    draw_backslash(img, x, y, scale, color)
    
def draw_dot(img, x, y, scale, color):
    # do something with the scale
    img.put(color, (x    , y    ))
    img.put(color, (x + 1, y    ))
    img.put(color, (x - 1, y    ))
    img.put(color, (x    , y + 1))
    img.put(color, (x    , y - 1))
    img.put(color, (x + 1, y - 1))
    img.put(color, (x + 1, y + 1))
    img.put(color, (x - 1, y - 1))
    img.put(color, (x - 1, y + 1))
