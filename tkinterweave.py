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

def canvas_motion_left(event):
    x, y = event.x, event.y
    
    
    if x + 5 < 0 or x - 5 < 0 or y + 5 < 0 or y - 5 < 0:
        return
    else:
        brushes.paint(img, x, y, 1, colors.WHITE, False)

    # reflect next draw call
    x, y = dimensions.PI_WIDTH - event.x, event.y
    
    if x + 5 < 0 or x - 5 < 0 or y + 5 < 0 or y - 5 < 0:
        return
    else:
        brushes.paint(img, x, y, 1, colors.WHITE, True)

def main():
    global img
    
    window = Tk()
    window.title("Tkinterweave")
    window.geometry(utils.get_window_geometry_string([dimensions.MW_WIDTH,
                                                      dimensions.MW_HEIGHT,
                                                      0,
                                                      0]))
    canvas = Canvas(window,
                    width=dimensions.PI_WIDTH,
                    height=dimensions.PI_HEIGHT,
                    bg=colors.BLACK)
    canvas.place(x=0, y=0,
                 width=dimensions.PI_WIDTH,
                 height=dimensions.PI_HEIGHT)
    img = PhotoImage(width=dimensions.PI_WIDTH,
                     height=dimensions.PI_HEIGHT)
    canvas.create_image((dimensions.PI_WIDTH / 2, dimensions.PI_HEIGHT / 2),
                        image=img,
                        state="normal")

    menubar = Menu(window)

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label=strings.NEW, command=lambda: menu_actions.do_new(img))
    filemenu.add_command(label=strings.OPEN, command=lambda: menu_actions.do_open())
    filemenu.add_command(label=strings.SAVE, command=lambda: menu_actions.do_save())
    filemenu.add_separator()
    filemenu.add_command(label=strings.EXIT, command=window.destroy)
    menubar.add_cascade(label=strings.FILE, menu=filemenu)

    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label=strings.CUT, command=lambda: menu_actions.do_cut())
    editmenu.add_command(label=strings.COPY, command=lambda: menu_actions.do_copy())
    editmenu.add_command(label=strings.PASTE, command=lambda: menu_actions.do_paste())
    menubar.add_cascade(label=strings.EDIT, menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label=strings.ABOUT, command=lambda: menu_actions.do_about(window))
    menubar.add_cascade(label=strings.HELP, menu=helpmenu)

    # display the menu
    window.config(menu=menubar)

    images.initialize()
    
    canvas.bind(user_input.LEFT_DRAG, canvas_motion_left)

    for i in range(img.height()):
        img.put(colors.GOLDENROD, (img.width() / 2, i))

    # create a frame to hold tools
    frame = Frame(window, width=100, height=120, bg=colors.WHITE)
    frame.place(x=dimensions.PI_WIDTH,
                y=0,
                width=dimensions.MW_WIDTH - dimensions.PI_WIDTH,
                height=dimensions.PI_HEIGHT)

    buttons_tuple = ()
    calligraphy_left_button = Button(frame, image=images.CALLIGRAPHY_LEFT, command=lambda: tool_actions.paint_tool_pressed(calligraphy_left_button, tool_names.CALLIGRAPHY_LEFT, buttons_tuple))
    calligraphy_right_button = Button(frame, image=images.CALLIGRAPHY_RIGHT, command=lambda: tool_actions.paint_tool_pressed(calligraphy_right_button, tool_names.CALLIGRAPHY_RIGHT, buttons_tuple))
    pencil_button = Button(frame, image=images.PENCIL, command=lambda: tool_actions.paint_tool_pressed(pencil_button, tool_names.PENCIL, buttons_tuple), relief=SUNKEN)
    spray_can_button = Button(frame, image=images.SPRAY_CAN, command=lambda: tool_actions.paint_tool_pressed(spray_can_button, tool_names.SPRAY_CAN, buttons_tuple))
    buttons_tuple = (calligraphy_left_button, calligraphy_right_button, pencil_button, spray_can_button)

    pencil_button.grid(row=0, column=0)
    spray_can_button.grid(row=0, column=1)
    calligraphy_left_button.grid(row=1, column=0)
    calligraphy_right_button.grid(row=1, column=1)
    
    window.mainloop()

if __name__ == '__main__':
    main()
