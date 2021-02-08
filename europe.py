from tkinter import *

class EuropeSketchpad (Frame):
    def __init__ (self, master):
        super(EuropeSketchpad, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        acanvas = Canvas(self, width = 1830, height = 1080, background = 'gray')
        acanvas.pack()

        map = PhotoImage(file = "AMERICANSTATES2.png")
        acanvas.create_image(10,10, image = map, anchor = NW)

        statename = Entry(acanvas)
        acanvas.create_window(1000,500, window =statename)



        # muricamap = PhotoImage(file = "AMERICANSTATES2.png")
        # w = Label(self, image = muricamap)
        # w.photo = muricamap
        # w.grid(row = 0, column = 0, sticky = NSEW)
        # https://tkdocs.com/tutorial/canvas.html


