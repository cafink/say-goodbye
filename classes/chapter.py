from bs4 import BeautifulSoup


class Chapter:

    def __init__(self, number, name, internal_name):
        self.number = number
        self.name = name
        self.internal_name = internal_name

    def load_details_from_xml(self, xml):
        chapter_details = xml.SaveData.Areas.find(
            "AreaStats",
            SID="Celeste/" + self.internal_name
        )

        self.cassette_collected = chapter_details["Cassette"]

    def print_details(self):
        print("Chapter " + str(self.number) + ": " + self.name)
        print("  Cassette collected: " + self.cassette_collected)
