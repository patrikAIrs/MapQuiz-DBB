f = open("testing.txt")

class Country (object):
    
    def __init__(self, name, place_names, x_coords, y_coords):

        self.name = name
        self.place_names = place_names
        self.x_coords = x_coords
        self.y_coords = y_coords

    def print_name(self):
        print(self.name)

list_of_objects = []

for x in f:
    split_line = x.split(",")

    name = split_line[0]


    place_name_list = []
    individual_names = split_line[1].split("> <")

    a = individual_names[0].replace("<", "")
    individual_names[0] = a

    z = individual_names[-1].replace(">", "")
    individual_names[-1] = z
    
    for x in range(len(individual_names)): 
        a = individual_names[x].strip()
        place_name_list.append(a)
    

    x_coords = split_line[2]
    individual_x_coords = x_coords.split("> <")
    x_coord_list = []

    a = individual_x_coords[0].replace("<", "")
    individual_x_coords[0] = a

    a = individual_x_coords[-1].replace(">", "")
    individual_x_coords[-1] = a
    
    for x in range(len(individual_x_coords)):
        a = individual_x_coords[x].strip()
        x_coord_list.append(int(a))

    y_coords = split_line[3]
    individual_y_coords = y_coords.split("> <")
    y_coord_list = []

    a = individual_y_coords[0].replace("<", "")
    individual_y_coords[0] = a

    a = individual_y_coords[-1].replace(">", "")
    individual_y_coords[-1] = a
    
    for x in range(len(individual_y_coords)):
        a = individual_y_coords[x].strip()
        y_coord_list.append(int(a))

    name = Country(name, place_name_list, x_coord_list, y_coord_list)
    list_of_objects.append(name)

print(list_of_objects[0].x_coords)

