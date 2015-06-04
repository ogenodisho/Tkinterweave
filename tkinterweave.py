from Tkinter import *
import brushes
import colors
import menu
import controls
import dimensions
import utils
import strings

def canvas_motion_left(event):
    x, y = event.x, event.y

    if x + 5 < 0 or x - 5 < 0 or y + 5 < 0 or y - 5 < 0:
        return
    else:
        brushes.draw_backslash(img, x, y, 1, colors.WHITE)

    # reflect next draw call
    x, y = dimensions.PI_WIDTH - event.x, event.y
    
    if x + 5 < 0 or x - 5 < 0 or y + 5 < 0 or y - 5 < 0:
        return
    else:
        brushes.draw_forwardslash(img, x, y, 1, colors.WHITE)
     

def canvas_motion_right(event):
    x, y = event.x, event.y

    if x + 5 < 0 or x - 5 < 0 or y + 5 < 0 or y - 5 < 0:
        return
    else:
        brushes.draw_forwardslash(img, x, y, 1, colors.WHITE)

    # reflect next draw call
    x, y = dimensions.PI_WIDTH - event.x, event.y
    
    if x + 5 < 0 or x - 5 < 0 or y + 5 < 0 or y - 5 < 0:
        return
    else:
        brushes.draw_backslash(img, x, y, 1, colors.WHITE)

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
    filemenu.add_command(label=strings.NEW, command=lambda: menu.do_new(img))
    filemenu.add_command(label=strings.OPEN, command=lambda: menu.do_open())
    filemenu.add_command(label=strings.SAVE, command=lambda: menu.do_save())
    filemenu.add_separator()
    filemenu.add_command(label=strings.EXIT, command=window.destroy)
    menubar.add_cascade(label=strings.FILE, menu=filemenu)

    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label=strings.CUT, command=lambda: menu.do_cut())
    editmenu.add_command(label=strings.COPY, command=lambda: menu.do_copy())
    editmenu.add_command(label=strings.PASTE, command=lambda: menu.do_paste())
    menubar.add_cascade(label=strings.EDIT, menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label=strings.ABOUT, command=lambda: menu.do_about(window))
    menubar.add_cascade(label=strings.HELP, menu=helpmenu)

    # display the menu
    window.config(menu=menubar)
    
    canvas.bind(controls.LEFT_DRAG, canvas_motion_left)
    canvas.bind(controls.RIGHT_DRAG, canvas_motion_right)

    for i in range(img.height()):
        img.put(colors.GOLDENROD, (img.width() / 2, i))

    window.mainloop()

if __name__ == '__main__':
    main()
