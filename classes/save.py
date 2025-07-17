from bs4 import BeautifulSoup
from classes.chapter import Chapter


class Save:

    save_info = {
        "Version": "Celeste version",
        "Name": "Name",
        "TotalStrawberries": "Strawberry count"
    }

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

    def load_from_file(self, filename):

        f = open(filename, "r")
        soup = BeautifulSoup(f.read(), "xml")

        for prop, display_name in self.save_info.items():
            print(
                display_name +
                ": " + eval("soup.SaveData." + prop + ".string")
            )

        stage_count = 1
        for internal_name, display_name in self.chapter_names.items():

            xml_chapter = soup.SaveData.Areas.find(
                "AreaStats",
                SID="Celeste/" + internal_name
            )

            chapter = Chapter(stage_count, display_name, internal_name)
            chapter.load_details_from_xml(xml_chapter)
            chapter.print_details()

            stage_count += 1
