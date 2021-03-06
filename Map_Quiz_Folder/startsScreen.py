from tkinter import *

class StartingScreen (Frame):
    def __init__ (self, master, map_roster, callback_on_selected):
        super(StartingScreen, self).__init__(master)


        self.map_roster = map_roster
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets() 


    def create_widgets(self):
        
        self.map_index = StringVar()
        self.map_index.set(None)
        self.mode_index = StringVar()
        self.mode_index.set(None)


        row = 1
        for x in range(len(self.map_roster.countries_list)):
            current_map = self.map_roster.countries_list[x]

            Label(self, text = "                       ").grid(row = row, column = 1)
            Label(self, text = "                       ").grid(row = row, column = 2)
            Label(self, 
                  text = """
                
                  
                  
                   """).grid(row = row + 1, column = 0)

            Radiobutton(self, text = current_map.name, 
                        font = "Times 40 bold", variable = self.map_index, 
                        value = current_map.name, fg = "blue", bg = "light yellow").grid(row = row, column = 3)

            row += 1
    
        Radiobutton(self, text = "Press", 
                    font = "Times 30 bold", variable = self.mode_index, 
                    value = " Press", fg = "red", bg = "white").grid(row = 2, column = 4)

        Radiobutton(self, text = "Label", 
                    font = "Times 30 bold", variable = self.mode_index, 
                    value = " Label", fg = "red", bg = "white").grid(row = 2, column = 5)

            

            


        Label(self, text = " ").grid(row = row + 1, column = 6)
        Label(self, text = " ").grid(row = row + 2, column = 6)
        Label(self, text = " ").grid(row = row + 3, column = 6)

        self.country_selected_button = Button(self, text = 'Country Selected!', fg = "Red", bg = "black", font = "Times 50 bold", command = self.selected_clicked)
        self.country_selected_button.grid(row = row + 1, column = 4, sticky = EW)

        self.quit_button = Button(self, text = "Quit", font = "Times 20 bold", command = self.exit_game)
        self.quit_button.grid(row = 0, column = 0)


    def exit_game(self):
        self.map_index.set("None")
        self.mode_index.set(" Exit")
        self.selected_clicked()
    
    def selected_clicked (self):
        self.callback_on_selected(self.map_index.get() + self.mode_index.get())



    







