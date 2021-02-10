from tkinter import *

from startsScreen import StartingScreen
from map_countries import Country_roster, Country_Object
from europe import EuropeSketchpad
from america import Application

class MapQuizManager (object):

    def __init__ (self):

        self.root = Tk()
        self.current_screen = None  
        self.countries_roster = None

    def setup_startScreen (self):

        self.root.title ("Selecting Map: ")
        self.countries_roster = Country_roster ("map_characteristics.txt")

        self.current_screen = StartingScreen(master = self.root, 
                                            map_roster = self.countries_roster,
                                            callback_on_selected = self.country_screen
                                            )


    def country_screen (self, selected_country_index):
        
        self.selected_country_index = selected_country_index

        selected_country_index = int (selected_country_index)

        self.current_screen.destroy()

        print(self.selected_country_index)

        if self.selected_country_index == "0":
            self.root.title("America")
            self.current_screen = Application (master = self.root)

        elif self.selected_country_index == "1":
            self.root.title("Europe")
            self.current_screen = EuropeSketchpad (master = self.root)

        else: 
            pass


        



def main():
    map_game = MapQuizManager()

    map_game.setup_startScreen()

    map_game.root.mainloop()

main()


    

    