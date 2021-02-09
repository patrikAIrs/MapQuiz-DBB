from tkinter import *
from tkinter import ttk


class Application (Frame):
    def __init__ (self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        acanvas = Canvas(self, width = 1830, height = 1080, background = 'gray')
        acanvas.pack(expand = YES, fill = BOTH)

        muricamap = PhotoImage(file = "AMERICANSTATES2.png")
        amap = Label(acanvas, image = muricamap)
        amap.photo = muricamap
        amap.grid(row = 0, column = 0)


        statename = Entry(acanvas)
        acanvas.create_window(1000,500, window =statename)

        





        # muricamap = PhotoImage(file = "AMERICANSTATES2.png")
        # w = Label(self, image = muricamap)
        # w.photo = muricamap
        # w.grid(row = 0, column = 0, sticky = NSEW)
        # https://tkdocs.com/tutorial/canvas.html







root = Tk()
root.title("America")
root.geometry("1830x1080")

app = Application(root)

root.mainloop()
