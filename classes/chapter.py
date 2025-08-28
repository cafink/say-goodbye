from bs4 import BeautifulSoup
from classes.side import Side

# Doesn't include golden strawberries
MAX_STRAWBERRY_COUNTS = {
    1: 20,
    2: 18,
    3: 25,
    4: 29,
    5: 31,
    7: 47,
    8: 5
}


class Chapter:

    def __init__(self, number, name, internal_name):
        self.number = number
        self.name = name
        self.internal_name = internal_name

    def load_details_from_xml(self, xml):
        self.cassette_collected = xml["Cassette"]

        self.sides = []

        side_letter = "A"
        xml_sides = xml.Modes.find_all("AreaModeStats")
        for xml_side in xml_sides:
            if self.number in MAX_STRAWBERRY_COUNTS:
                max_strawberry_count = MAX_STRAWBERRY_COUNTS[self.number]
            else:
                max_strawberry_count = 0
            side = Side(side_letter, max_strawberry_count)
            side.load_details_from_xml(xml_side)
            self.sides.append(side)

            side_letter = chr(ord(side_letter) + 1)  # increment letter

    def has_sides(self):
        return self.number in range(9)
