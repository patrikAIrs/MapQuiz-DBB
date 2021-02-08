from tkinter import *

from startsScreen import StartingScreen
from map_countries import Country_roster, Country_Object
from europe import EuropeSketchpad

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

        self.root.title ("Quiz")
        selected_country_index = int (selected_country_index)

        self.current_screen.destroy()

        print(self.selected_country_index)

        if self.selected_country_index == 0:
            pass

        elif self.selected_country_index == 1:
            pass

        else: 
            pass

        self.current_screen = EuropeSketchpad(Canvas)

        



def main():
    map_game = MapQuizManager()

    map_game.setup_startScreen()

    map_game.root.mainloop()

main()


    

    