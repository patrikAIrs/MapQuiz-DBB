from tkinter import *

class Screen_Battle (Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()

        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
                                                                         
        self.attack_button = Button(self, text = "Attack", fg = "Red", bg = "Black", font = "Helvetica 30 bold", command = self.attack_clicked)
        self.attack_button.grid(row = 0, column = 0)

        self.player1_attack_or_miss = Label(self, text = "", font = "Helvetica 30")
        self.player1_attack_or_miss.grid(row = 0, column = 1)
        self.player2_attack_or_miss = Label(self, text = "", font = "Helvetica 30")
        self.player2_attack_or_miss.grid(row = 1, column = 1)

        self.victory = Label(self, text = "", font = "Helvetica 30 bold")
        self.victory.grid(row = 2, column = 1)

        Label(self, text = "You", font = "Helvetica 20 bold").grid(row = 3, column = 0, sticky = EW)
        Label(self, text = "Computer", font = "Helvetica 20 bold").grid(row = 3, column = 1, sticky = EW)

        Player1_imageLarge = PhotoImage(file = "images/" + self.player1.large_image)
        w = Label(self, image = Player1_imageLarge)
        w.photo = Player1_imageLarge
        w.grid(row = 4, column = 0, sticky = EW)

        Player2_imageLarge = PhotoImage(file = "images/" + self.player2.large_image)
        w = Label(self, image = Player2_imageLarge)
        w.photo = Player2_imageLarge
        w.grid(row = 4, column = 1, sticky = EW)

        self.PLAYER1_ORIGINAL_HIT_POINTS = self.player1.hit_points
        self.PLAYER2_ORIGINAL_HIT_POINTS = self.player2.hit_points

        self.player1_hit_points = Label(self, text = "%d/%d" % (self.player1.hit_points, self.PLAYER1_ORIGINAL_HIT_POINTS), font = "Helvetica 30 bold")
        self.player1_hit_points.grid(row = 5, column = 0, sticky = EW)
        self.player2_hit_points = Label(self, text = "%d/%d" % (self.player2.hit_points, self.PLAYER2_ORIGINAL_HIT_POINTS), font = "Helvetica 30 bold")
        self.player2_hit_points.grid(row = 5, column = 1, sticky = EW)

    
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''   

        
        self.player1_attack_or_miss['text'] = self.player1.attack(self.player2)
        

        if self.player2.hit_points > 0:
            self.player2_attack_or_miss["text"] = self.player2.attack(self.player1)

        self.player1_hit_points["text"] = "%d/%d" % (self.player1.hit_points, self.PLAYER1_ORIGINAL_HIT_POINTS)
        self.player2_hit_points["text"] = "%d/%d" % (self.player2.hit_points, self.PLAYER2_ORIGINAL_HIT_POINTS)

        if self.player1.hit_points <= 0:
            self.victory["text"] = "%s is victorious" % (self.player2.name) 
            self.attack_button.destroy()
            Button(self, text = "Exit!", fg = "red", bg = "black", font = "Helvetica 30 bold", command = self.exit_clicked).grid(row = 6, column = 1, sticky = E)
        if self.player2.hit_points <= 0:
            self.victory["text"] = "%s is victorious" % (self.player1.name)
            self.attack_button.destroy()
            Button(self, text = "Exit!", fg = "red", bg = "black", font = "Helvetica 30 bold", command = self.exit_clicked).grid(row = 6, column = 1, sticky = E)


    ## exit the w
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
  
            
            
            
            