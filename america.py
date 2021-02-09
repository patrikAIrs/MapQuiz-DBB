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


        statename1 = Entry(acanvas)
        acanvas.create_window(1040,550, window =statename1) #missouri

        statename2 = Entry(acanvas)
        acanvas.create_window(100,600, window =statename2) #california

        statename3 = Entry(acanvas)
        acanvas.create_window(180,230, window =statename3) #oregon

        statename4 = Entry(acanvas)
        acanvas.create_window(565,160, window =statename4) #montana

        statename5 = Entry(acanvas)
        acanvas.create_window(820,840, window =statename5) #texas

        





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
