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

for prop, displayname in save_info.items():
    print(displayname + ": " + str(soup.find(prop).string))

stage_count = 0
for internalname, displayname in levels.items():
    stage_count += 1
    print("Stage " + str(stage_count) + ": " +  displayname)

    area = soup.find("AreaStats", SID=internalname)
    print("  Cassette collected: " + area["Cassette"])

    sides = area.find_all("AreaModeStats")

    side_letter = "A"
    for side in sides:
        print("  " + side_letter + "-side strawberry count: " + str(side.attrs["TotalStrawberries"]))
        side_letter = chr(ord(side_letter) + 1)