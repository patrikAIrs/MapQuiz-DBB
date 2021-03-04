from tkinter import *
from tkinter import ttk
import random

class AmericaScreen (Frame):
    def __init__ (self, master, number_of_attempts):
        super(AmericaScreen, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.number_of_attempts = number_of_attempts


    def create_widgets(self):
        acanvas = Canvas(self, width = 1830, height = 1080, background = 'gray')
        acanvas.pack(expand = YES, fill = BOTH)

        muricamap = PhotoImage(file = "AMERICANSTATES2.png")
        amap = Label(acanvas, image = muricamap)
        amap.photo = muricamap
        amap.grid(row = 0, column = 0)

        self.number_of_tries = 0

        self.country_list = ["New York", "Oregon", "California", "Montana", "Missouri", "Texas", 
                             "Minnesota", "Michigan", "Ohio", "Alabama", "Utah", "Kansas", 
                             "Kentucky", "Florida", "Wyoming", "Virginia", "Iowa", "Illinois", "Oklahoma", 
                             "Nevada", "Arizona", "Idaho", "North Dakota", "Georgia"]
        self.x_coordinates = [1580, 215, 160, 565, 1040, 820, 975, 1250, 1350, 1260, 421, 845, 1285, 1451, 570, 1510, 1005, 1145, 878, 264, 386, 368, 794, 1366]
        self.y_coordinates = [300, 230, 600, 160, 550, 840, 290, 300, 450, 815, 485, 552, 576, 917, 345, 537, 408, 476, 681, 448, 680, 265, 182, 768]
        self.country_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        self.current_country_index = random.choice(self.country_indexes)

        self.country_text = Label(self, text = self.country_list[self.current_country_index], font = "Times 20 bold")
        self.country_text.config(width = 10, height = 3)
        acanvas.create_window(100, 100, window = self.country_text)

        self.right_wrong = Label(self, text = "", font = "Times 20 bold")
        self.right_wrong.config(width = 10, height = 3)
        acanvas.create_window(100, 200, window = self.right_wrong)

        self.try_number = Label(self, text = "%s: %d" % ("Tries", self.number_of_tries), font = "Times 20 bold")
        self.try_number.config(width = 10, height = 3)
        acanvas.create_window(300, 100, window = self.try_number)



        self.country_radiobutton_value = StringVar()
        self.country_radiobutton_value.set(None)

        for x in range(len(self.country_list)):

            country_button = Radiobutton(acanvas, variable = self.country_radiobutton_value, value = x, command = self.right_or_wrong)
            acanvas.create_window(self.x_coordinates[x], self.y_coordinates[x], window = country_button)


        self.exit_button = Button(self, text = "Go Back to Home Screen", command = self.exit,
                                  font = "Times 20 bold", bg = "light blue")
        acanvas.create_window(362, 846, window = self.exit_button)

    def exit(self):
        self.number_of_attempts(69420)

    def right_or_wrong(self):
        selected_index = int(self.country_radiobutton_value.get())
        if selected_index != self.current_country_index:
            self.right_wrong.config(text = "Incorrect")
            self.number_of_tries += 1
            self.try_number.config(text = "%s: %d" % ("Tries", self.number_of_tries))
        else:
            self.right_wrong.config(text = "Correct!")
            self.number_of_tries += 1
            self.try_number.config(text = "%s: %d" % ("Tries", self.number_of_tries))
            self.change_country_text()

    def change_country_text(self):
        if len(self.country_indexes) > 0:
            self.country_indexes.remove(self.current_country_index)

        if len(self.country_indexes) > 0:
            self.current_country_index = random.choice(self.country_indexes)
            self.country_text.config(text = self.country_list[self.current_country_index])
        else:
           self.export_number_of_tries()

    def export_number_of_tries(self):

        self.number_of_attempts(self.number_of_tries)
        



        # muricamap = PhotoImage(file = "AMERICANSTATES2.png")
        # w = Label(self, image = muricamap)
        # w.photo = muricamap
        # w.grid(row = 0, column = 0, sticky = NSEW)
        # https://tkdocs.com/tutorial/canvas.html



# root = Tk()
# root.title("America")
# root.geometry("1830x1080")

# app = Application(root)

# root.mainloop()
