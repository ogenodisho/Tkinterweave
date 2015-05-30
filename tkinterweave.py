from Tkinter import *
from math import sin

# Returns a list of coords that represent,
# in order, width, height, xPos, yPos.
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
    
    return list(map(int, l))

def draw_backslash(x, y):
    img.put("#ffffff", (x + 5, y - 5))
    img.put("#ffffff", (x + 4, y - 4))
    img.put("#ffffff", (x + 3, y - 3))
    img.put("#ffffff", (x + 2, y - 2))
    img.put("#ffffff", (x + 1, y - 1))
    img.put("#ffffff", (x    , y    ))
    img.put("#ffffff", (x - 1, y + 1))
    img.put("#ffffff", (x - 2, y + 2))
    img.put("#ffffff", (x - 3, y + 3))
    img.put("#ffffff", (x - 4, y + 4))
    img.put("#ffffff", (x - 5, y + 5))

def draw_forwardslash(x, y):
    img.put("#ffffff", (x - 5, y - 5))
    img.put("#ffffff", (x - 4, y - 4))
    img.put("#ffffff", (x - 3, y - 3))
    img.put("#ffffff", (x - 2, y - 2))
    img.put("#ffffff", (x - 1, y - 1))
    img.put("#ffffff", (x    , y    ))
    img.put("#ffffff", (x + 1, y + 1))
    img.put("#ffffff", (x + 2, y + 2))
    img.put("#ffffff", (x + 3, y + 3))
    img.put("#ffffff", (x + 4, y + 4))
    img.put("#ffffff", (x + 5, y + 5))

def canvas_motion_left(event):
    x, y = event.x, event.y

    if x + 5 < 0 or x - 5 < 0 or y + 5 < 0 or y - 5 < 0:
        return
    else:
        draw_backslash(x, y)

    # reflect next draw call
    x, y = WIDTH - event.x, event.y
    
    if x + 5 < 0 or x - 5 < 0 or y + 5 < 0 or y - 5 < 0:
        return
    else:
        draw_forwardslash(x, y)
     

def canvas_motion_right(event):
    x, y = event.x, event.y

    if x + 5 < 0 or x - 5 < 0 or y + 5 < 0 or y - 5 < 0:
        return
    else:
        draw_forwardslash(x, y)

    # reflect next draw call
    x, y = WIDTH - event.x, event.y
    
    if x + 5 < 0 or x - 5 < 0 or y + 5 < 0 or y - 5 < 0:
        return
    else:
        draw_backslash(x, y)

def do_open():
    print "OPEN"

def do_save():
    print "SAVE"

def do_open():
    print "OPEN"

def do_cut():
    print "CUT"

def do_copy():
    print "COPY"

def do_paste():
    print "PASTE"

def do_about():
    geometry = get_window_geometry(window)
    toplevel = Toplevel()
    toplevel.title("About Tkinterweave")
    toplevel.geometry("%dx%d+%d+%d" % (260, 150, geometry[2] + 30, geometry[3] + 80))
    label1 = Label(toplevel, text="Tkinterweave is a shitty desktop application made to trick CS101 students into thinking that tkinter is useful.\n", wraplength=200, anchor=W, justify=CENTER)
    label1.pack()
    label2 = Label(toplevel, text="Brought to you by:\nOgen Odisho & Krasni Shrivastava\n\nCopyright (c) 2015.", wraplength=200, anchor=W, justify=CENTER)
    label2.pack()

def main():
    global img, HEIGHT, WIDTH, window
    
    WIDTH, HEIGHT = 640, 480
    window = Tk()
    window.title("Tkinterweave")
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

    menubar = Menu(window)

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=do_open)
    filemenu.add_command(label="Save", command=do_save)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=do_cut)
    editmenu.add_command(label="Copy", command=do_copy)
    editmenu.add_command(label="Paste", command=do_paste)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=do_about)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    window.config(menu=menubar)
    
    canvas.bind("<B1-Motion>", canvas_motion_left)
    canvas.bind("<B3-Motion>", canvas_motion_right)

    for i in range(HEIGHT):
        img.put("#800085", (WIDTH / 2, i))

    window.mainloop()

if __name__ == '__main__':
    main()
