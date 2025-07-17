from bs4 import BeautifulSoup

f = open("saves/0.celeste (175 save)", "r")
soup = BeautifulSoup(f.read(), "xml")

save_info = {
    "Version": "Celeste version",
    "Name": "Name",
    "TotalStrawberries": "Strawberry count"
}

levels = {
    "Celeste/1-ForsakenCity": "Forsaken City",
    "Celeste/2-OldSite": "Old Site",
    "Celeste/3-CelestialResort": "Celestial Resort",
    "Celeste/4-GoldenRidge": "Golden Ridge",
    "Celeste/5-MirrorTemple": "Mirror Temple",
    "Celeste/6-Reflection": "Reflection",
    "Celeste/7-Summit": "Summit",
    "Celeste/9-Core": "Core",
    "Celeste/LostLevels": "Farewell"
}

level_info = {
    "Cassette": "Cassette collected"
}

side_info = {
    "TotalStrawberries": "Strawberry count"
}

for prop, display_name in save_info.items():
    print(display_name + ": " + eval("soup.SaveData." + prop + ".string"))

stage_count = 1
for internalname, displayname in levels.items():
    print("Stage " + str(stage_count) + ": " + displayname)

    level = soup.SaveData.Areas.find("AreaStats", SID=internalname)
    for level_prop, level_display_name in level_info.items():
        print("  " + level_display_name + ": " + level[level_prop])

    sides = level.Modes.find_all("AreaModeStats")

    side_letter = "A"
    for side in sides:
        print("  " + side_letter + "-side")

        for side_prop, side_display_name in side_info.items():
            print(
                "    " +
                side_display_name +
                ": " +
                str(side.attrs[side_prop])
            )

        side_letter = chr(ord(side_letter) + 1)  # increment letter

    stage_count += 1
