from bs4 import BeautifulSoup
from classes.chapter import Chapter


class Save:

    chapter_names = {
        "1-ForsakenCity": "Forsaken City",
        "2-OldSite": "Old Site",
        "3-CelestialResort": "Celestial Resort",
        "4-GoldenRidge": "Golden Ridge",
        "5-MirrorTemple": "Mirror Temple",
        "6-Reflection": "Reflection",
        "7-Summit": "Summit",
        "9-Core": "Core",
        "LostLevels": "Farewell"
    }

    def __init__(self, filename):

        f = open(filename, "r")
        soup = BeautifulSoup(f.read(), "xml")

        self.load_details_from_xml(soup)

    def load_details_from_xml(self, xml):

        self.version = xml.SaveData.Version.string
        self.name = xml.SaveData.Name.string
        self.strawberry_count = xml.SaveData.TotalStrawberries.string

        self.chapters = []

        stage_count = 1
        for internal_name, display_name in self.chapter_names.items():

            xml_chapter = xml.SaveData.Areas.find(
                "AreaStats",
                SID="Celeste/" + internal_name
            )

            chapter = Chapter(stage_count, display_name, internal_name)
            chapter.load_details_from_xml(xml_chapter)
            self.chapters.append(chapter)
            stage_count += 1
