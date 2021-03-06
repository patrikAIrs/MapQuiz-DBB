class Country_Object (object):
    
    def __init__(self, name, place_names, x_coords, y_coords, image_file_name):

        self.name = name
        self.place_names = place_names
        self.x_coords = x_coords
        self.y_coords = y_coords
        self.image_file_name = str(image_file_name)

class Country_Roster (object):

    def __init__(self, file_name):

        self.countries_list = []

        f = open(file_name, "r")

        f.readline()
        f.readline()

        for x in f:
            split_line = x.split(",")

            name = split_line[0]


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

            name = Country_Object(name, place_name_list, x_coord_list, y_coord_list, image_file)
            self.countries_list.append(name)



