'''
This module loads images to be used inside tkinterweave
and puts them in a single variable for ease of use.
'''

from Tkinter import *

CALLIGRAPHY_LEFT = None
CALLIGRAPHY_RIGHT = None
PENCIL = None
SPRAY_CAN = None

# call this before the mainloop because
# the photoimages cannot be created instantly
def initialize():
    global CALLIGRAPHY_LEFT, CALLIGRAPHY_RIGHT, PENCIL, SPRAY_CAN 
    CALLIGRAPHY_LEFT = PhotoImage(file="images/calligraphy_left.gif")
    CALLIGRAPHY_RIGHT = PhotoImage(file="images/calligraphy_right.gif")
    PENCIL = PhotoImage(file="images/pencil.gif")
    SPRAY_CAN = PhotoImage(file="images/spray_can.gif")
