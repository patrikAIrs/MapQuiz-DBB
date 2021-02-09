from tkinter import *

class EuropeSketchpad (Frame):
    def __init__ (self, master):
        super(EuropeSketchpad, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        # acanvas = Canvas(self, width = 1830, height = 1080, background = 'red')
        # acanvas.pack()

        # acanvas.create_image(10,10, image = map, anchor = NW)

        # statename = Entry(acanvas)
        # acanvas.create_window(1000,500, window =statename)


        europemap = PhotoImage(file = "EUROPEMAP3.png")
        europe_map_image = Label(self, image = europemap)
        europe_map_image.photo = europemap
        europe_map_image.grid(row = 0, column = 0)

        # muricamap = PhotoImage(file = "AMERICANSTATES2.png")
        # w = Label(self, image = muricamap)
        # w.photo = muricamap
        # w.grid(row = 0, column = 0, sticky = NSEW)
        # https://tkdocs.com/tutorial/canvas.html


