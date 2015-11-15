from Tkinter import *
import base64


def meh():
    f=open("calligraphy_left.gif","rb")
    print base64.b64encode(f.read()) + "\n\n=============END=============\n"
    
    f=open("calligraphy_right.gif","rb")
    print base64.b64encode(f.read()) + "\n\n=============END=============\n"

    f=open("magnifying_glass.gif","rb")
    print base64.b64encode(f.read()) + "\n\n=============END=============\n"

    f=open("pencil.gif","rb")
    print base64.b64encode(f.read()) + "\n\n=============END=============\n"

    f=open("spray_can.gif","rb")
    print base64.b64encode(f.read()) + "\n\n=============END=============\n"

window = Tk()

meh()
