from tkinter import *
import random

class AmericaLabelScreen (Frame):
    def __init__ (self, master, roster, number_of_attempts):
        super(AmericaLabelScreen, self).__init__(master)
        self.roster = roster
        self.grid()
        self.create_widgets()
        self.number_of_attempts = number_of_attempts
        


    def create_widgets(self):
        acanvas = Canvas(self, width = 1830, height = 1080, background = 'gray')
        acanvas.pack(expand = YES, fill = BOTH)

        muricamap = PhotoImage(file = self.roster.image_file_name)
        amap = Label(acanvas, image = muricamap)
        amap.photo = muricamap
        amap.grid(row = 0, column = 0)

        self.number_of_tries = 0

        self.country_list = self.roster.place_names
        self.x_coordinates = self.roster.x_coords
        self.y_coordinates = self.roster.y_coords
        self.country_indexes = []
        for x in range(len(self.country_list)):
            self.country_indexes.append(x)
        self.current_country_index = random.choice(self.country_indexes)

        self.country_text = Label(self, text = self.country_list[self.current_country_index], font = "Times 20 bold")
        self.country_text.config(width = 10, height = 3)
        acanvas.create_window(100, 100, window = self.country_text)

        self.right_wrong = Label(self, text = "", font = "Times 20 bold")
        self.right_wrong.config(width = 10, height = 3)
        acanvas.create_window(100, 100, window = self.right_wrong)


        self.try_number = Label(self, text = "%s: %d" % ("Tries", self.number_of_tries), font = "Times 20 bold")
        self.try_number.config(width = 10, height = 3)
        acanvas.create_window(300, 100, window = self.try_number)


        self.country_radiobutton_value = StringVar()
        self.country_radiobutton_value.set(self.current_country_index)

        self.country_entry = Entry(self, font = "Times 15", bg = "light yellow")
        acanvas.create_window(600, 50, window = self.country_entry)

        self.submit_button = Button(self, text = "Submit", font = "Times 15 bold", command = self.right_or_wrong)
        acanvas.create_window(600, 80, window = self.submit_button)

        for x in range(len(self.country_list)):

            country_button = Radiobutton(acanvas, variable = self.country_radiobutton_value, value = x, command = self.right_or_wrong)
            acanvas.create_window(self.x_coordinates[x], self.y_coordinates[x], window = country_button)

        self.exit_button = Button(self, text = "Go Back to Home Screen", command = self.exit,
                                  font = "Times 20 bold", bg = "light blue")
        acanvas.create_window(self.roster.home_screen_x, self.roster.home_screen_y, window = self.exit_button)

        self.list_of_remaining_countries = []
        self.list_of_remaining_countries.clear()

        for x in self.country_indexes:
            self.list_of_remaining_countries.append(self.country_list[x])

        self.country_wordbox = Label(self, text = self.list_of_remaining_countries, font = "Times 11 bold")
        acanvas.create_window(self.roster.word_bank_x, self.roster.word_bank_y, window = self.country_wordbox)

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
            self.list_of_remaining_countries.clear()

            for x in self.country_indexes:
                self.list_of_remaining_countries.append(self.country_list[x])

            self.country_wordbox.config(text = self.list_of_remaining_countries)

        if len(self.country_indexes) > 0:
            self.current_country_index = random.choice(self.country_indexes)
            self.country_radiobutton_value.set(self.current_country_index)
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
# root.title("America")
# root.geometry("1830x1080")

# app = Application(root)

# root.mainloop()
