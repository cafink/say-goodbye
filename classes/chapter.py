from bs4 import BeautifulSoup
from classes.side import Side


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
            side = Side(side_letter)
            side.load_details_from_xml(xml_side)
            self.sides.append(side)

            side_letter = chr(ord(side_letter) + 1)  # increment letter

    def has_sides(self):
        return self.number in range(9)
