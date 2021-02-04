from tkinter import *

class Application (Frame):
    def __init__ (self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        
        Label(self, text = "").grid(row = 0, column = 0)
        Label(self, text = "").grid(row = 1, column = 1)

        muricamap = PhotoImage(file = "AMERICANSTATES2")
        w = Label(self, image = muricamap)
        w.photo = muricamap
        w.grid(row = 4, column = 0, sticky = EW)





root = Tk()
root.title("America")
root.geometry("600x600")

app = Application(root)

root.mainloop()
