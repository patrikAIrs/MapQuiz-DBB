from tkinter import *
from tkinter import ttk
import random

class AsiaScreen (Frame):
    def __init__ (self, master):
        super(AsiaScreen, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        ascanvas = Canvas(self, width = 990, height = 774, background = 'gray')
        ascanvas.pack(expand = YES, fill = BOTH)

        asiamap = PhotoImage(file = "ASIAMAP4.png")
        asmap = Label(ascanvas, image = asiamap)
        asmap.photo = asiamap
        asmap.grid(row = 0, column = 0)


        self.country_list = ["New York", "Oregon", "California", "Montana", "Missouri", "Texas"]
        self.x_coordinates = [1580, 215, 160, 565, 1040, 820]
        self.y_coordinates = [300, 230, 600, 160, 550, 840]
        self.country_indexes = [0, 1, 2, 3, 4, 5]

        self.current_country_index = random.choice(self.country_indexes)

        self.country_text = Label(self, text = self.country_list[self.current_country_index], font = "Times 20 bold")
        self.country_text.config(width = 10, height = 3)
        ascanvas.create_window(100, 100, window = self.country_text)

        self.right_wrong = Label(self, text = "", font = "Times 20 bold")
        self.right_wrong.config(width = 10, height = 3)
        ascanvas.create_window(100, 200, window = self.right_wrong)



        self.country_radiobutton_value = StringVar()
        self.country_radiobutton_value.set(None)

        for x in range(6):

            country_button = Radiobutton(ascanvas, variable = self.country_radiobutton_value, value = x, command = self.right_or_wrong)
            ascanvas.create_window(self.x_coordinates[x], self.y_coordinates[x], window = country_button)



    def right_or_wrong(self):
        selected_index = int(self.country_radiobutton_value.get())
        if selected_index != self.current_country_index:
            self.right_wrong.config(text = "Incorrect")
        else:
            self.right_wrong.config(text = "Correct!")
            self.change_country_text()

    def change_country_text(self):
        if len(self.country_indexes) > 0:
            self.country_indexes.remove(self.current_country_index)

        if len(self.country_indexes) > 0:
            self.current_country_index = random.choice(self.country_indexes)
            self.country_text.config(text = self.country_list[self.current_country_index])
        else:
           print("You did it!")
           self.quit()
        



        # muricamap = PhotoImage(file = "AMERICANSTATES2.png")
        # w = Label(self, image = muricamap)
        # w.photo = muricamap
        # w.grid(row = 0, column = 0, sticky = NSEW)
        # https://tkdocs.com/tutorial/canvas.html



# root = Tk()
# root.title("Asia")
# root.geometry("1830x1080")

# app = Application(root)

# root.mainloop()
