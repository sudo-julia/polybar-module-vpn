#!/usr/bin/env python3

from sys import argv

# if a country you use isn't in here, open an issue or pull request
countries = {
    "albania": "al",
    "austrailia": "au",
    "austria": "at",
    "belgium": "be",
    "brazil": "br",
    "bulgaria": "bg",
    "canada": "ca",
    "czech republic": "cz",
    "denmark": "dk",
    "finland": "fi",
    "france": "fr",
    "germany": "de",
    "greece": "gr",
    "hong kong": "hk",
    "hungary": "hu",
    "ireland": "ie",
    "israel": "il",
    "italy": "it",
    "japan": "jp",
    "latvia": "lv",
    "luxembourg": "lu",
    "moldova": "md",
    "netherlands": "nl",
    "new zealand": "nz",
    "norway": "no",
    "poland": "pl",
    "romania": "ro",
    "serbia": "rs",
    "singapore": "sg",
    "spain": "es",
    "sweden": "se",
    "switzerland": "ch",
    "uk": "gb",
    "united arab emirates": "ae",
    "usa": "us",
}

# be sure to quote your arg so countries with spaces don't break the script
# exit code key for integration in main script:
if len(argv) != 2:
    exit(1)
else:
    pass

country = argv[1].lower()

# TODO elif code is given, translate it to country
if country in countries:
    print(countries[country])
else:
    exit(2)
