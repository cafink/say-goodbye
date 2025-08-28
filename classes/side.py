from bs4 import BeautifulSoup
from enum import StrEnum


class SideLetter(StrEnum):
    A = "A"
    B = "B"
    C = "C"


class Side:

    def __init__(self, letter, max_strawberry_count):
        self.letter = SideLetter(letter)

        if self.has_strawberries():
            self.max_strawberry_count = max_strawberry_count

    def load_details_from_xml(self, xml):
        self.strawberry_count = xml.attrs["TotalStrawberries"]
        self.got_heart = xml.attrs["HeartGem"] == 'true'

    def has_strawberries(self):
        return self.letter == SideLetter("A")
