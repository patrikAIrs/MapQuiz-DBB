from tkinter import *

class Screen_CharacterSelection (Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
       # Save the CharacterRoster  
        self.roster = roster
        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        ########

        Here is some sample code for including an image on a page:   (char is a Character object)
            
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)
        '''

        self.character_index = StringVar()
        self.character_index.set(None)

        ## display of each of the stats
        #health
        Label(self, text = "Hit Points", font = "Helvetica 20 bold").grid(row = 0, column = 2, sticky = W)
        #dexterity
        Label(self, text = "Dexterity", font = "Helvetica 20 bold").grid(row = 0, column = 3, sticky = W)
        #stre
        Label(self, text = "Strength", font = "Helvetica 20 bold").grid(row = 0, column = 4, sticky = W)

        row = 1
        ## calling info from roster
        for x in range(len(self.roster.character_list)):
            current_character = self.roster.character_list[x]

            Radiobutton(self, text = current_character.name, 
                        font = "Helvetica 20 bold", variable = self.character_index, 
                        value = x).grid(row = row, column = 0, sticky = W)
            
            imageSmall = PhotoImage(file = "images/" + current_character.small_image)
            w = Label(self, image = imageSmall)
            w.photo = imageSmall
            w.grid(row = row, column = 1, sticky = W)
            ## calling character stats
            Label(self, text = current_character.hit_points).grid(row = row, column = 2, sticky = W)

            Label(self, text = current_character.dexterity).grid(row = row, column = 3, sticky = W)

            Label(self, text = current_character.strength).grid(row = row, column = 4, sticky = W)
            ## moving onto next row
            row += 1
        
        self.character_selected_button = Button(self, text = 'Character Selected!', fg = "Red", bg = "black", command = self.selected_clicked)
        self.character_selected_button.grid(row = row + 1, column = 4)
 
    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''         
        self.callback_on_selected(self.character_index.get())

