from tkinter import *

class StartingScreen (Frame):
    def __init__ (self, master, map_roster, callback_on_selected):
        super().__init__(master)

        self.map_roster = map_roster
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets() 


    def create_widgets(self):
        
        self.map_index = StringVar()
        self.map_index.set(None)

        row = 0
        for x in range(3):
            current_map = self.map_roster.countries_list[x]

            Radiobutton(self, text = current_map.name, 
                        font = "Helvetica 20 bold", variable = self.map_index, 
                        value = x).grid(row = row, column = 0, sticky = W)

            Label(self, text = current_map.number_of_places, font = "Helvetica 20 bold").grid(row = row, column = 1, sticky = W)

            row +=1
            

        
        self.country_selected_button = Button(self, text = 'Country Selected!', fg = "Red", bg = "black", command = self.selected_clicked)
        self.country_selected_button.grid(row = row + 1, column = 4)
    
    def selected_clicked (self):
        self.callback_on_selected(self.map_index.get())



    







