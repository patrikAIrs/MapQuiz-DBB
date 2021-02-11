from tkinter import *
from tkinter import ttk
import random

class AsiaScreen (Frame):
    def __init__ (self, master, number_of_attempts):
        super(AsiaScreen, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.number_of_attempts = number_of_attempts


    def create_widgets(self):
        ascanvas = Canvas(self, width = 990, height = 774, background = 'gray')
        ascanvas.pack(expand = YES, fill = BOTH)

        asiamap = PhotoImage(file = "ASIAMAP4.png")
        asmap = Label(ascanvas, image = asiamap)
        asmap.photo = asiamap
        asmap.grid(row = 0, column = 0)

        self.number_of_tries = 0


        self.country_list = ["China", "India", "Mongolia", "Kazakhstan", "S. Arabia", "Iran", "Pakistan", "Afghanistan", "Turkey", "Myanmar", "Indonesia", "Yemen"]
        self.x_coordinates = [600, 450, 563, 320, 170, 240, 332, 315, 69, 572, 736, 174]
        self.y_coordinates = [360, 480, 265, 257, 460, 400, 428, 378, 331, 483, 686, 541]
        self.country_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        self.current_country_index = random.choice(self.country_indexes)

        self.country_text = Label(self, text = self.country_list[self.current_country_index], font = "Times 20 bold")
        self.country_text.config(width = 10, height = 3)
        ascanvas.create_window(100, 100, window = self.country_text)

        self.right_wrong = Label(self, text = "", font = "Times 20 bold")
        self.right_wrong.config(width = 10, height = 3)
        ascanvas.create_window(100, 200, window = self.right_wrong)

        self.try_number = Label(self, text = "%s: %d" % ("Tries", self.number_of_tries), font = "Times 20 bold")
        self.try_number.config(width = 10, height = 3)
        ascanvas.create_window(300, 100, window = self.try_number)



        self.country_radiobutton_value = StringVar()
        self.country_radiobutton_value.set(None)

        for x in range(len(self.country_list)):

            country_button = Radiobutton(ascanvas, variable = self.country_radiobutton_value, value = x, command = self.right_or_wrong)
            ascanvas.create_window(self.x_coordinates[x], self.y_coordinates[x], window = country_button)



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
            # print("You found all countries in %d guesses" % (self.number_of_tries))
            self.export_number_of_tries()

    def export_number_of_tries(self):

        self.number_of_attempts(self.number_of_tries)
        



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
