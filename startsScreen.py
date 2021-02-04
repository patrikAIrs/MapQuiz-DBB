from tkinter import *

class StartingScreen (Frame):
    def __init__ (self, master, callback_on_selected):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.american_map.name = "America"
        self.american_map.places = 50
        self.european_map.name = "Europe"
        self.european_map.places = 30
        self.asian_map.name = "Asia"
        self.asian_map.places = 40

        map_roster = [self.american_map, self.european_map, self.asian_map]

    def create_widgets(self):
        
        for x in range(3):
            current_map = map_roster[x]

            Radiobutton(self, text = current_map.name, 
                        font = "Helvetica 20 bold", variable = self.character_index, 
                        value = x).grid(row = row, column = 0, sticky = W)
            
            imageSmall = PhotoImage(file = "images/" + current_character.small_image)
            w = Label(self, image = imageSmall)
            w.photo = imageSmall
            w.grid(row = row, column = 1, sticky = W)
            ## calling character stats
            Label(self, text = current_character.hit_points).grid(row = row, column = 2, sticky = W)

            Label(self, text = current_character.dexterity).grid(row = row, column = 3, sticky = W)

            Label(self, text = current_character.strength).grid(row = row, column = 4, sticky = W)
            ## moving onto next row
            row += 1
        
        self.character_selected_button = Button(self, text = 'Character Selected!', fg = "Red", bg = "black", command = self.selected_clicked)
        self.character_selected_button.grid(row = row + 1, column = 4)
    
    def selected_clicked (self):
        pass



    







