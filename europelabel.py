from tkinter import *
import random

class EuropeLabelScreen (Frame):
    def __init__ (self, master, number_of_attempts):
        super(EuropeLabelScreen, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.number_of_attempts = number_of_attempts

        

    def create_widgets(self):

        self.country_list = ["Russia", "Ukraine", "Poland", "Germany", "France", "Spain", "Norway", "Sweden", "Finland", "Belarus", "Uk", "Czech Rep.", "Austria", "Italy", "Romania"]
        self.x_coordinates = [1000, 900, 663, 478, 314, 138, 468, 568, 715, 814, 270, 573, 579, 482, 801]
        self.y_coordinates = [250, 545, 495, 527, 658, 763, 248, 282, 189, 432, 475, 571, 640, 722, 677]
        self.country_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

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

        europemap = PhotoImage(file = "EUROPEMAP3.png")
        europe_map_image = Label(ecanvas, image = europemap)
        europe_map_image.photo = europemap
        europe_map_image.grid(row = 0, column = 0)

        self.country_radiobutton_value = StringVar()
        self.country_radiobutton_value.set(self.current_country_index)

        self.country_entry = Entry(self, font = "Times 15", bg = "light yellow")
        ecanvas.create_window(600, 50, window = self.country_entry)

        self.submit_button = Button(self, text = "Submit", font = "Times 15 bold", command = self.right_or_wrong)
        ecanvas.create_window(600, 80, window = self.submit_button)

        for x in range(len(self.country_list)):

            country_button = Radiobutton(ecanvas, variable = self.country_radiobutton_value, value = x, command = self.right_or_wrong)
            ecanvas.create_window(self.x_coordinates[x], self.y_coordinates[x], window = country_button)

        self.exit_button = Button(self, text = "Go Back to Home Screen", command = self.exit,
                                  font = "Times 20 bold", bg = "light blue")
        ecanvas.create_window(362, 846, window = self.exit_button)

    def exit(self):
        self.number_of_attempts(69420)

    def right_or_wrong(self):
        country_submission = self.country_entry.get()

        if country_submission.lower().title() == self.country_list[self.current_country_index]:
            self.right_wrong.config(text = "Correct!")
            self.country_entry.delete(0, 'end')
            self.number_of_tries += 1
            self.try_number.config(text = "%s: %d" % ("Tries", self.number_of_tries))
            self.change_country_text()
        else:
            self.right_wrong.config(text = "Incorrect")
            self.country_entry.delete(0, 'end')
            self.number_of_tries += 1
            self.try_number.config(text = "%s: %d" % ("Tries", self.number_of_tries))




        

    def change_country_text(self):
        if len(self.country_indexes) > 0:
            self.country_indexes.remove(self.current_country_index)

        if len(self.country_indexes) > 0:
            self.current_country_index = random.choice(self.country_indexes)
            self.country_radiobutton_value.set(self.current_country_index)
            self.country_text.config(text = self.country_list[self.current_country_index])
        else:
            # print("You found all countries in %d guesses" % (self.number_of_tries))
            self.export_number_of_tries()

    def export_number_of_tries(self):

        self.number_of_attempts(self.number_of_tries)


    
