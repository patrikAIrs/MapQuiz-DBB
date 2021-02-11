from tkinter import *

class EndingScreen (Frame):
    def __init__ (self, master, number_of_tries):
        super(EndingScreen, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        endcanvas = Canvas(self, width = 1434, height = 783, bg = "black")
        endcanvas.pack(expand = YES, fill = BOTH)

        

    def play_again_or_not(self):
        pass




# root = Tk()
# root.title("America")
# root.geometry("1830x1080")

# app = EndingScreen(root)

# root.mainloop()

