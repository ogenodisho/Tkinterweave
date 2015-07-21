'''
This global_configs.py module is an attempt to reduce
parameter passing. It contains all global configurations
such as the currently selected tool, the currently selected
color, the PhotoImage on which to draw on, the paint tool
buttons and more. These can be used by all modules as "god objects"
'''

import tool_names
import colors

CURRENT_TOOL = tool_names.PENCIL # default tool is pencil
CURRENT_COLOR = colors.WHITE # default color is white
IMG = None # initialized in main
CANVAS = None # initialized in main
ZOOMSLIDER = None # initialized in main
ZOOM_FACTOR = 1 # default zoom is 1
ZOOM_LEVELS = [0.5, 1, 2, 4]
PAINT_TOOL_BUTTONS = () # populated in main
