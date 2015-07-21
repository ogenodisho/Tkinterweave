'''
This is the main file which takes care of creating
the windows, initializing the global variables to
be used by the other modules, attaching listeners,
and more.
'''

from Tkinter import *
import brushes
import colors
import menu_actions
import user_input
import dimensions
import utils
import strings
import images
import tool_actions
import tool_names
import global_configs

def main():
    window = Tk()
    window.title("Tkinterweave")
    # set the geometry of the window (width, height, xSpawnPos, ySpawnPos)
    window.geometry(utils.get_window_geometry_string([dimensions.MW_WIDTH,
                                                      dimensions.MW_HEIGHT,
                                                      0,
                                                      0]))
    # create the canvas
    global_configs.CANVAS = Canvas(window,
                    width=dimensions.PI_WIDTH,
                    height=dimensions.PI_HEIGHT,
                    bg=colors.BLACK)
    
    # place the canvas in the top left of the parent window
    global_configs.CANVAS.place(x=0, y=0,
                 width=dimensions.PI_WIDTH,
                 height=dimensions.PI_HEIGHT)
    
    # populate IMG global variable which is a PhotoImage that will be drawn on
    global_configs.IMG = PhotoImage(width=dimensions.PI_WIDTH,
                     height=dimensions.PI_HEIGHT)
    
    # put the image on the canvas
    global_configs.CANVAS.create_image(0, 0,
                        anchor=NW,
                        image=global_configs.IMG,
                        state="normal")
    
    # add left mouse moved listener to the canvas
    global_configs.CANVAS.bind(user_input.LEFT_DRAG, tool_actions.canvas_left_drag)

    # create an empty menu bar to populate
    menubar = Menu(window)
    
    # create and populate a pulldown menu called file
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label=strings.NEW, command=lambda: menu_actions.do_new())
    filemenu.add_command(label=strings.OPEN, command=lambda: menu_actions.do_open())
    filemenu.add_command(label=strings.SAVE, command=lambda: menu_actions.do_save())
    filemenu.add_separator()
    filemenu.add_command(label=strings.EXIT, command=window.destroy)
    menubar.add_cascade(label=strings.FILE, menu=filemenu)

    # create and populate a pulldown menu called edit
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label=strings.COPY, command=lambda: menu_actions.do_copy())
    editmenu.add_command(label=strings.PASTE, command=lambda: menu_actions.do_paste())
    menubar.add_cascade(label=strings.EDIT, menu=editmenu)

    # create and populate a pulldown menu called help
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label=strings.ABOUT, command=lambda: menu_actions.do_about(window))
    menubar.add_cascade(label=strings.HELP, menu=helpmenu)

    # display the menu
    window.config(menu=menubar)

    # initialize the MSPaint images
    images.initialize()

    # draw the separator
    for i in range(global_configs.IMG.height()):
        global_configs.IMG.put(colors.GOLDENROD, (global_configs.IMG.width() / 2, i))

    # create a frame to hold the paint tools
    # place the frame to the right of the canvas and
    # make it go until the end of the window in the x and y
    frame = Frame(window, bg=colors.WHITE)
    frame.place(x=window.winfo_width() - 78,
                y=0,
                width=78,
                height=78 * 2)

    # pack the canvas and paint tool frames
    frame.pack(fill=Y, expand=NO, side=RIGHT)
    global_configs.CANVAS.pack(fill=NONE, expand=YES, side=TOP)
    
    # create the buttons with images and on click listeners
    calligraphy_left_button = Button(frame, image=images.CALLIGRAPHY_LEFT, command=lambda: tool_actions.paint_tool_pressed(calligraphy_left_button, tool_names.CALLIGRAPHY_LEFT))
    calligraphy_right_button = Button(frame, image=images.CALLIGRAPHY_RIGHT, command=lambda: tool_actions.paint_tool_pressed(calligraphy_right_button, tool_names.CALLIGRAPHY_RIGHT))
    pencil_button = Button(frame, image=images.PENCIL, command=lambda: tool_actions.paint_tool_pressed(pencil_button, tool_names.PENCIL), relief=SUNKEN)
    spray_can_button = Button(frame, image=images.SPRAY_CAN, command=lambda: tool_actions.paint_tool_pressed(spray_can_button, tool_names.SPRAY_CAN))
    global_configs.PAINT_TOOL_BUTTONS = (calligraphy_left_button, calligraphy_right_button, pencil_button, spray_can_button)

    # create the zoom slider, label, and button and set it's default value to 1 for x1 zoom
    zoomSliderLabel = Label(frame, text=strings.ZOOM)
    zoomSliderLabel.grid(row=2, column=0, columnspan=2)
    global_configs.ZOOMSLIDER = Scale(frame, from_=4, to=0.5, resolution=0.5, command=tool_actions.on_zoom_level_changed)
    global_configs.ZOOMSLIDER.set(global_configs.ZOOM_FACTOR)
    global_configs.ZOOMSLIDER.grid(row=3, column=0, rowspan=2, columnspan=2)
    zoomButton = Button(frame, image=images.MAGNIFYING_GLASS, command=lambda: tool_actions.perform_zoom(float(global_configs.ZOOMSLIDER.get())))
    zoomButton.grid(row=5, column=0, rowspan=2, columnspan=2)
    
    # arrange the buttons in a grid formation inside the frame
    pencil_button.grid(row=0, column=0)
    spray_can_button.grid(row=0, column=1)
    calligraphy_left_button.grid(row=1, column=0)
    calligraphy_right_button.grid(row=1, column=1)

    # for some reason if we don't call this is doesnt save right the first time round
    menu_actions.do_new()
    
    window.mainloop()

# executable
if __name__ == '__main__':
    main()
