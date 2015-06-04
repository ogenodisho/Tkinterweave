from Tkinter import *
import utils
import colors

# reset the img to one color
def do_new(img):
    utils.fill_img(img, colors.BLACK)

    # reset the horizontal reflector
    for i in range(480):
        img.put(colors.GOLDENROD, (640 / 2, i))

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

# window param - the window to draw the
# about window with respect to.
def do_about(window):
    geometry = utils.get_window_geometry(window)
    toplevel = Toplevel()
    toplevel.title("About Tkinterweave")
    toplevel.geometry("%dx%d+%d+%d" % (260, 150, geometry[2] + 30, geometry[3] + 80))
    label1 = Label(toplevel, text="Tkinterweave is a shitty desktop application made to trick CS101 students into thinking that tkinter is useful.\n", wraplength=200, anchor=W, justify=CENTER)
    label1.pack()
    label2 = Label(toplevel, text="Brought to you by:\nOgen Odisho & Krasni Shrivastava\n\nCopyright (c) 2015.", wraplength=200, anchor=W, justify=CENTER)
    label2.pack()
