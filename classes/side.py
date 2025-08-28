from bs4 import BeautifulSoup
from enum import StrEnum


class SideLetter(StrEnum):
    A = "A"
    B = "B"
    C = "C"


class Side:

    def __init__(self, chapter_number, letter):
        self.chapter_number = chapter_number
        self.letter = SideLetter(letter)

    def load_details_from_xml(self, xml):
        self.strawberry_count = xml.attrs["TotalStrawberries"]
        self.got_heart = xml.attrs["HeartGem"] == 'true'

    def has_strawberries(self):
        return self.chapter_number < 9 and self.letter == SideLetter("A")
