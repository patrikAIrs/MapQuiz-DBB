from tkinter import *

class StartingScreen (Frame):
    def __init__ (self, master):
        super(StartingScreen, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        
        Label(self, text = "").grid(row = 0, column = 0)
        Label(self, text = "").grid(row = 1, column = 1)

        self.mapbutton1 = Button(self, text = "American States", fg = "blue", font = "Times 20 bold", command = self.selected_clicked)
        self.mapbutton1.grid(row = 2, column = 2)

    def selected_clicked (self):
        pass



    







