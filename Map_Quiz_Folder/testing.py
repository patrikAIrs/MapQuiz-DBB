class Country_Object (object):
    
    def __init__(self, name, place_names, x_coords, y_coords, image_file_name, word_bank_x, word_bank_y, home_screen_x, home_screen_y):

        self.name = name
        self.place_names = place_names
        self.x_coords = x_coords
        self.y_coords = y_coords
        self.image_file_name = str(image_file_name)
        self.word_bank_x = word_bank_x
        self.word_bank_y = word_bank_y
        self.home_screen_x = home_screen_x
        self.home_screen_y = home_screen_y


class Country_Roster (object):

    def __init__(self, file_name):

        self.countries_list = []

        file_1 = open(file_name, "r")

        info_list = []
        line_counter = 0
        for x in file_1:
            line_counter += 1
            info_list.append(x.strip())

        line_counter -= 1

        line_counter_2 = int(line_counter / 8)
        info_list_2 = [""] * line_counter_2

        file_2 = open(file_name, "r")

        list_index_value = 0
        for x in file_2:
            if x == "":
                list_index_value += 1
                continue
            else:
                info_list_2[list_index_value] += x.strip()
                info_list_2[list_index_value] += " "
                info_list_2[list_index_value] += ","
                info_list_2[list_index_value] += " "
        

        info_list_2 = info_list_2[0].split(",  ,")
   
        print(info_list_2)
        



        for x in range(len(info_list_2) - 1):
            split_line = info_list_2[x].split(",")

            name = split_line[0]
            a = name.strip()
            b = a.replace("'", "")
            name = b


            place_name_list = []
            individual_names = split_line[1].split("' '")

            a = individual_names[0].replace("'", "")
            individual_names[0] = a

            z = individual_names[-1].replace("'", "")
            individual_names[-1] = z
            
            for x in range(len(individual_names)): 
                a = individual_names[x].strip()
                place_name_list.append(a)
            

            x_coords = split_line[2]
            individual_x_coords = x_coords.split("' '")
            x_coord_list = []

            a = individual_x_coords[0].replace("'", "")
            individual_x_coords[0] = a

            a = individual_x_coords[-1].replace("'", "")
            individual_x_coords[-1] = a
            
            for x in range(len(individual_x_coords)):
                a = individual_x_coords[x].strip()
                x_coord_list.append(int(a))

            y_coords = split_line[3]
            individual_y_coords = y_coords.split("' '")
            y_coord_list = []

            a = individual_y_coords[0].replace("'", "")
            individual_y_coords[0] = a

            a = individual_y_coords[-1].replace("'", "")
            individual_y_coords[-1] = a
            
            for x in range(len(individual_y_coords)):
                a = individual_y_coords[x].strip()
                y_coord_list.append(int(a))

            image_file = split_line[4]
            a = image_file.replace("'", "")
            b = a.strip()
            image_file = b

            words_bank = split_line[5]
            a = words_bank.strip()
            words_bank = a

            a = words_bank.split(" ")
            words_bank = a

            a = words_bank[0].replace("'", "")
            words_bank[0] = int(a)

            a = words_bank[1].replace("'", "")
            words_bank[1] = int(a)

            home_screen = split_line[6]
            a = home_screen.strip()
            home_screen = a

            a = home_screen.split(" ")
            home_screen = a

            a = home_screen[0].replace("'", "")
            home_screen[0] = int(a)

            a = home_screen[1].replace("'", "")
            home_screen[1] = int(a)



            name = Country_Object(name, place_name_list, x_coord_list, y_coord_list, image_file, words_bank[0], words_bank[1], home_screen[0], home_screen[1])
            self.countries_list.append(name)

Country_List = Country_Roster("testing.txt")
print(Country_List.countries_list[0].name)




