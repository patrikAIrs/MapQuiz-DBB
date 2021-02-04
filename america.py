from tkinter import *

class Application (Frame):
    def __init__ (self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):


        muricamap = PhotoImage(file = "AMERICANSTATES2.png")
        w = Label(self, image = muricamap)
        w.photo = muricamap
        w.grid(row = 0, column = 0, sticky = NSEW)





root = Tk()
root.title("America")
root.geometry("1830x1080")

app = Application(root)

root.mainloop()
