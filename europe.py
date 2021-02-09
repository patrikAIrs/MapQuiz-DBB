from tkinter import *

class EuropeSketchpad (Frame):
    def __init__ (self, master):
        super(EuropeSketchpad, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):


        ecanvas = Canvas(self, width = 1280, height = 1024)
        ecanvas.pack(expand = YES, fill = BOTH)

        countryname = Entry(ecanvas)
        ecanvas.create_window(10, 10, window = countryname)

        europemap = PhotoImage(file = "EUROPEMAP3.png")
        europe_map_image = Label(ecanvas, image = europemap)
        europe_map_image.photo = europemap
        europe_map_image.grid(row = 0, column = 0)

        # muricamap = PhotoImage(file = "AMERICANSTATES2.png")
        # w = Label(self, image = muricamap)
        # w.photo = muricamap
        # w.grid(row = 0, column = 0, sticky = NSEW)
        # https://tkdocs.com/tutorial/canvas.html


