from tkinter import *

from startsScreen import StartingScreen
from map_countries import Country_roster, Country_Object
from europe import EuropeScreen
from america import AmericaScreen
from asia import AsiaScreen
from EndScreen import EndingScreen
from europelabel import EuropeLabelScreen
from asialabel import AsiaLabelScreen

class MapQuizManager (object):

    def __init__ (self):

        self.root = Tk()
        self.current_screen = None  
        self.countries_roster = None
        

    def setup_startScreen (self):

        # self.root.attributes ('-alpha', 0.5)

        self.root.title ("Selecting Map: ")
        self.root.geometry("1830x1080")
        self.countries_roster = Country_roster ("map_characteristics.txt")

        self.current_screen = StartingScreen(master = self.root, 
                                            map_roster = self.countries_roster,
                                            callback_on_selected = self.country_screen
                                            )


    def country_screen (self, selected_country_index):
        
        # self.root.attributes ('-alpha', 0.5)

        self.selected_country_index = selected_country_index

        selected_country_index = int (selected_country_index)

        self.current_screen.destroy()


        if self.selected_country_index == "0":
            self.root.title("America")
            self.current_screen = AmericaScreen (master = self.root
                                                ,number_of_attempts = self.end_screen)

        elif self.selected_country_index == "1":

            self.root.title("Europe")
            self.current_screen = EuropeScreen (master = self.root
                                                ,number_of_attempts = self.end_screen)

        else: 
            self.root.title("Asia")
            self.current_screen = AsiaLabelScreen (master = self.root
                                              ,number_of_attempts = self.end_screen)

    def end_screen(self, number_of_attempts):

        self.number_of_attempts = number_of_attempts

        self.current_screen.destroy()
        self.root.title("You Won!")

        self.current_screen = EndingScreen (master = self.root, number_of_guesses = self.number_of_attempts, callback_on_selected = self.play_again_or_quit)

    def play_again_or_quit(self, play_again_or_not):
        self.play_again_or_not = play_again_or_not

        if play_again_or_not == "0":
            self.current_screen.destroy()
            self.setup_startScreen()

        elif play_again_or_not == "1":
            self.current_screen.quit()

        



def main():
    map_game = MapQuizManager()

    map_game.setup_startScreen()

    map_game.root.mainloop()

main()


    

    