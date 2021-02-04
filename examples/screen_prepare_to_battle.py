from tkinter import *

class Screen_PrepareToBattle (Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which EW return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        ## initialization
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets on the prepare to battle page.
        '''
        ## shows which stat/image pertains to who
        Label(self, text = "You", font = "Helvetica 20 bold", bg = "gray").grid(row = 0, column = 0, sticky = EW)
        Label(self, text = "Computer", font = "Helvetica 20 bold", bg = "gray").grid(row = 0, column = 1, sticky = EW)

#need picture here-- pat. also, how do EW call the computer's stats again?

        Player1_imageLarge = PhotoImage(file = "images/" + self.player1.large_image)
        w = Label(self, image = Player1_imageLarge)
        w.photo = Player1_imageLarge
        w.grid(row = 1, column = 0, sticky = W)

        Player2_imageLarge = PhotoImage(file = "images/" + self.player2.large_image)
        w = Label(self, image = Player2_imageLarge)
        w.photo = Player2_imageLarge
        w.grid(row = 1, column = 1, sticky = W)

        ## hp of each char
        Label(self, text = "%d HP" % (self.player1.hit_points), font = "Helvetica 20 bold", bg = "gray").grid(row = 2, column = 0, sticky = EW)
        Label(self, text = "%d HP" % (self.player2.hit_points), font = "Helvetica 20 bold", bg = "gray").grid(row = 2, column = 1, sticky = EW)

        ## dex of each char
        Label(self, text = "%d Dexterity" % (self.player1.dexterity), font = "Helvetica 20 bold", bg = "gray").grid(row = 3, column = 0, sticky = EW)
        Label(self, text = "%d Dexterity" % (self.player2.dexterity), font = "Helvetica 20 bold", bg = "gray").grid(row = 3, column = 1, sticky = EW)
        
        ## strength of each char
        Label(self, text = "%d Strength" % (self.player1.strength), font = "Helvetica 20 bold", bg = "gray").grid(row = 4, column = 0, sticky = EW)
        Label(self, text = "%d Strength" % (self.player2.strength), font = "Helvetica 20 bold", bg = "gray").grid(row = 4, column = 1, sticky = EW)

        ## move onto screen_battle
        Button(self, text = "Commence Battle!", bg = "black", fg = "red", font = "Times 20 bold", command = self.commence_battle_clicked).grid(row = 5, column = 2)

        
        
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
    
