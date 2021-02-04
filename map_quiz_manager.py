from tkinter import *

from startsScreen import StartingScreen

class MapQuizManager (object):

    def __init__ (self):

        self.root = Tk()
        self.current_screen = None

    def setup_startScreen (self):

        self.root.title ("Selecting Map: ")

        self.current_screen = StartingScreen(master = self.root)
    