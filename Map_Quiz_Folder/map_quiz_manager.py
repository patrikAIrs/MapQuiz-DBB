from tkinter import *

from startsScreen import StartingScreen
from map_countries import Country_Roster, Country_Object
from america import AmericaScreen
from EndScreen import EndingScreen
from americalabel import AmericaLabelScreen

class MapQuizManager (object):

    def __init__ (self):

        self.root = Tk()
        self.current_screen = None  
        self.countries_roster = None
        

    def setup_startScreen (self):

        # self.root.attributes ('-alpha', 0.5)

        self.root.title ("Selecting Map: ")
        self.countries_roster = Country_Roster ("testing.txt")

        self.current_screen = StartingScreen(master = self.root, 
                                            map_roster = self.countries_roster,
                                            callback_on_selected = self.country_screen)


    def country_screen (self, selected_country_index):
        
        # self.root.attributes ('-alpha', 0.5)

        self.selected_country_index = selected_country_index
        self.selected_game_mode = None


        self.current_screen.destroy()

        for x in range(len(self.countries_roster.countries_list)):
            game_type = self.selected_country_index.split(" ")
            self.selected_game_mode = game_type[1]            
            if game_type[0] == self.countries_roster.countries_list[x].name:
                self.selected_country_index = x
                break


        
        if self.selected_game_mode == "Press":
            self.root.title("%s: %s" % (self.countries_roster.countries_list[self.selected_country_index].name, self.selected_game_mode))
            self.current_screen = AmericaScreen (master = self.root, roster = self.countries_roster.countries_list[self.selected_country_index]
                                                ,number_of_attempts = self.end_screen)

        elif self.selected_game_mode == "Label":
            self.root.title("%s: %s" % (self.countries_roster.countries_list[self.selected_country_index].name, self.selected_game_mode))
            self.current_screen = AmericaLabelScreen (master = self.root, roster = self.countries_roster.countries_list[self.selected_country_index]
                                                ,number_of_attempts = self.end_screen)

        else:
            self.current_screen.quit()


    def end_screen(self, number_of_attempts):

        self.number_of_attempts = number_of_attempts

        self.current_screen.destroy()

        if self.number_of_attempts == 69420:
            self.setup_startScreen()
            return None
        
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


    

    