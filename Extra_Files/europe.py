from tkinter import *
import random

class EuropeScreen (Frame):
    def __init__ (self, master, roster, number_of_attempts):
        super(EuropeScreen, self).__init__(master)
        self.roster = roster
        self.grid()
        self.create_widgets()
        self.number_of_attempts = number_of_attempts

        


    def create_widgets(self):

        self.country_list = self.roster.place_names
        self.x_coordinates = self.roster.x_coords
        self.y_coordinates = self.roster.y_coords
        self.country_indexes = []
        for x in range(len(self.country_list)):
            self.country_indexes.append(x)

        self.number_of_tries = 0

        self.current_country_index = random.choice(self.country_indexes)

        ecanvas = Canvas(self, width = 1280, height = 1024)
        ecanvas.pack(expand = YES, fill = BOTH)

        self.country_text = Label(self, text = self.country_list[self.current_country_index], font = "Times 20 bold")
        self.country_text.config(width = 10, height = 3)
        ecanvas.create_window(100, 100, window = self.country_text)

        self.right_wrong = Label(self, text = "", font = "Times 20 bold")
        self.right_wrong.config(width = 10, height = 3)
        ecanvas.create_window(100, 200, window = self.right_wrong)

        self.try_number = Label(self, text = "%s: %d" % ("Tries", self.number_of_tries), font = "Times 20 bold")
        self.try_number.config(width = 10, height = 3)
        ecanvas.create_window(300, 100, window = self.try_number)

        europemap = PhotoImage(file = self.roster.image_file_name)
        europe_map_image = Label(ecanvas, image = europemap)
        europe_map_image.photo = europemap
        europe_map_image.grid(row = 0, column = 0)

        self.country_radiobutton_value = StringVar()
        self.country_radiobutton_value.set(None)


        for x in range(len(self.country_list)):

            country_button = Radiobutton(ecanvas, variable = self.country_radiobutton_value, value = x, command = self.right_or_wrong)
            ecanvas.create_window(self.x_coordinates[x], self.y_coordinates[x], window = country_button)

        self.exit_button = Button(self, text = "Go Back to Home Screen", command = self.exit,
                                  font = "Times 20 bold", bg = "light blue")
        ecanvas.create_window(362, 846, window = self.exit_button)

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
            # print("You found all countries in %d guesses" % (self.number_of_tries))
            self.export_number_of_tries()


    def export_number_of_tries(self):

        self.number_of_attempts(self.number_of_tries)

    
