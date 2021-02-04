class Country_Object (object):

    def __init__(self, name, number_of_places):
        self.name = name
        self.number_of_places = number_of_places

class Country_roster (object):

    def __init__(self, file_name):

        self.countries_list = []

        country_text_file = open(file_name, "r")

        for line in country_text_file:
            line = line.strip()
            my_fields = line.split(",")
            country = Country_Object (my_fields[0], int(my_fields[1]))
            self.countries_list.append(country)

    def print_roster(self):
        print(self.countries_list)





def main():
    roster = Country_roster ("map_characteristics.txt")
    roster.print_roster()

main()