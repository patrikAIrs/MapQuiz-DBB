from tkinter import *

class Application (Frame):
    def __init__ (self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        
        self.mapbutton1 = Button(self, text = "American States", fg = "blue", font = "Times 20 bold", command = self.destroy_button)
        self.mapbutton1.grid(row = 2, column = 2)

    def destroy_button(self):
        self.mapbutton1.destroy()



root = Tk()
root.title("Map Quiz")
root.geometry("400x200")

app = Application(root)

root.mainloop()



