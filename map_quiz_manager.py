from tkinter import *

from startsScreen import StartingScreen
from map_countries import Country_roster, Country_Object
from europe import EuropeScreen
from america import AmericaScreen
from asia import AsiaScreen
from EndScreen import EndingScreen

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


        if self.selected_country_index == "0":
            self.root.title("America")
            self.current_screen = AmericaScreen (master = self.root)
                                                # ,callback_on_selected = self.end_screen)

        elif self.selected_country_index == "1":
            self.root.title("Europe")
            self.current_screen = EuropeScreen (master = self.root)
                                                # ,callback_on_selected = self.end_screen)

        else: 
            self.root.title("Asia")
            self.current_screen = AsiaScreen (master = self.root
                                             ,number_of_attempts = self.end_screen)

    def end_screen(self, number_of_attempts):

        self.number_of_attempts = number_of_attempts

        self.current_screen.destroy()
        self.root.title("You Won!")

        print("You won in %d tries!" % (self.number_of_attempts))


        



def main():
    map_game = MapQuizManager()

    map_game.setup_startScreen()

    map_game.root.mainloop()

main()


    

    