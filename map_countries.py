class Country_Object (object):

    def __init__(self, name):
        self.name = name

class Country_roster (object):

    def __init__(self, file_name):

        self.countries_list = []

        country_text_file = open(file_name, "r")

        for line in country_text_file:
            line = line.strip()
            my_fields = line.split(",")
            country = Country_Object (my_fields[0])
            self.countries_list.append(country)
    