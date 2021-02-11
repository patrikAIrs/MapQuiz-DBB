from tkinter import *

class EndingScreen (Frame):
    def __init__ (self, master, number_of_guesses):
        super(EndingScreen, self).__init__(master)
        
        self.number_of_guesses = number_of_guesses
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        endcanvas = Canvas(self, width = 1434, height = 783)
        endcanvas.pack(expand = YES, fill = BOTH)

        self.you_won = Label(self, text = "You guessed all the countries in %d attempts" % (self.number_of_guesses), font = "Times 40 bold")
        self.you_won.config(height = 3, width = 50)
        endcanvas.create_window(717, 350, window = self.you_won)

        

    def play_again_or_not(self):
        pass




# root = Tk()
# root.title("America")
# root.geometry("1830x1080")

# app = EndingScreen(root)

# root.mainloop()

