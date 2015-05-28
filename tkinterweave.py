from Tkinter import *
from math import sin

def main():
    global img
    
    WIDTH, HEIGHT = 640, 480
    window = Tk()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

    canvas.bind("<B1-Motion>", canvas_motion_left)
    canvas.bind("<B3-Motion>", canvas_motion_right)

    window.mainloop()


def canvas_motion_right(event):
    img.put("#ffffff", (event.x + 5, event.y - 5))
    img.put("#ffffff", (event.x + 4, event.y - 4))
    img.put("#ffffff", (event.x + 3, event.y - 3))
    img.put("#ffffff", (event.x + 2, event.y - 2))
    img.put("#ffffff", (event.x + 1, event.y - 1))
    img.put("#ffffff", (event.x, event.y))
    img.put("#ffffff", (event.x - 1, event.y + 1))
    img.put("#ffffff", (event.x - 2, event.y + 2))
    img.put("#ffffff", (event.x - 3, event.y + 3))
    img.put("#ffffff", (event.x - 4, event.y + 4))
    img.put("#ffffff", (event.x - 5, event.y + 5))

def canvas_motion_left(event):
    img.put("#ffffff", (event.x - 5, event.y - 5))
    img.put("#ffffff", (event.x - 4, event.y - 4))
    img.put("#ffffff", (event.x - 3, event.y - 3))
    img.put("#ffffff", (event.x - 2, event.y - 2))
    img.put("#ffffff", (event.x - 1, event.y - 1))
    img.put("#ffffff", (event.x, event.y))
    img.put("#ffffff", (event.x + 1, event.y + 1))
    img.put("#ffffff", (event.x + 2, event.y + 2))
    img.put("#ffffff", (event.x + 3, event.y + 3))
    img.put("#ffffff", (event.x + 4, event.y + 4))
    img.put("#ffffff", (event.x + 5, event.y + 5))
        

if __name__ == '__main__':
    main()
