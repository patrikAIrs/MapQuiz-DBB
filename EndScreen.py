from tkinter import *

class EndingScreen (Frame):
    def __init__ (self, master, number_of_guesses, callback_on_selected):
        super(EndingScreen, self).__init__(master)


        self.callback_on_selected = callback_on_selected
        self.number_of_guesses = number_of_guesses
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        endcanvas = Canvas(self, width = 1434, height = 783)
        endcanvas.pack(expand = YES, fill = BOTH)

        worldmap = PhotoImage(file = "MAPOFTHEWORLD.png")
        wmap = Label(endcanvas, image = worldmap)
        wmap.photo = worldmap
        wmap.grid(row = 0, column = 0)

        self.you_won = Label(self, text = "You guessed all the countries in %d attempts" % (self.number_of_guesses), font = "Times 40 bold")
        self.you_won.config(height = 3, width = 50)
        endcanvas.create_window(717, 350, window = self.you_won)

        self.play_again_button = Button(self, text = "Play Again", font = "Times 40 bold", command = self.play_again)
        self.play_again_button.config(height = 3, width = 11)
        endcanvas.create_window(717, 550, window = self.play_again_button)

        self.quit_button = Button(self, text = "Quit", font = "Times 40 bold", command = self.quit_game)
        self.quit_button.config(height = 3, width = 11)
        endcanvas.create_window(717, 750, window = self.quit_button)


        

    def play_again(self):
        self.callback_on_selected("0")

    def quit_game(self):
        self.callback_on_selected("1")




# root = Tk()
# root.title("America")
# root.geometry("1830x1080")

# app = EndingScreen(root)

# root.mainloop()

