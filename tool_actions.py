'''
This module encapsulates the responses to events from tools
such as all of the paint brushes, user input into the canvas etc.
'''
from Tkinter import *
import tool_names
import brushes
import global_configs
import colors
import dimensions

# Dictates what happens when a paint tool is pressed.
# Sink the clicked button and raise all of the other ones.
# Also, change the current_tool which is global in the main
def paint_tool_pressed(button_object, tool_name):
    if button_object.cget("relief") == "raised":
        # raise all the buttons
        for b in global_configs.PAINT_TOOL_BUTTONS:
            b.config(relief="raised")
            
        # sink the selected button
        button_object.config(relief="sunken")
        
        # update the current tool to match the selected one
        global_configs.CURRENT_TOOL = tool_name
    else:
        # don't do anything if the user clicked a pressed button
        pass

# Dictates what happens when the zoom slider is slidden?
def zoom_slider_slid(sample_size):
    global_configs.ZOOM_FACTOR = sample_size
    
    # perform the zoom
    zooming_in = sample_size > 1
    if zooming_in:
        sample_size = int(sample_size) # zoom calls need to be ints
    else:
        sample_size = 1 / sample_size

    if zooming_in:
        # set the size of the canvas to the size of the image - don't know why I have to minus 2...
        global_configs.CANVAS.config(width=global_configs.IMG.width() * sample_size - 2, height=global_configs.IMG.height() * sample_size - 2)
    
        global_configs.IMG = global_configs.IMG.zoom(sample_size, sample_size)
    else:
        # set the size of the canvas to the size of the image - don't know why I have to minus 2...
        global_configs.CANVAS.config(width=global_configs.IMG.width() / sample_size - 2, height=global_configs.IMG.height() / sample_size - 2)

        global_configs.IMG = global_configs.IMG.subsample(int(sample_size), int(sample_size))

    # draw the new image on the canvas
    global_configs.CANVAS.create_image(0, 0,
                        anchor=NW,
                        image=global_configs.IMG,
                        state="normal")
    

def canvas_left_drag(event):
    # unpack coords
    x, y = event.x, event.y

    # paint the non-reflected stuff
    brushes.paint(x, y, 1, colors.WHITE, False)

    # reflect next draw call horizontally
    x, y = global_configs.CANVAS.winfo_width() - event.x, event.y

    # paint the reflected stuff
    brushes.paint(x, y, 1, colors.WHITE, True)
