import unittest

from sqlalchemy import and_

from app import create_app
from extensions_locations import string_to_location
from extensions_sql import db
from models.postgres.locations.cities import City
from models.postgres.locations.countries import Country
from models.postgres.locations.states import State

app = create_app()

countries_to_test = [
    ["United States", "USA"],
    ["United Kingdom", "GBR"],
    ["Canada", "CAN"],
    ["Poland", "POL"],
    ["Australia", "AUS"],
]

states_to_test = [
    # United States
    ["Colorado, US",
        ["Colorado", "USA"]],
    ["Colorado, USA",
        ["Colorado", "USA"]],
    ["Colorado, United States",
        ["Colorado", "USA"]],
    ["Colorado, United States of America",
        ["Colorado", "USA"]],

    ["New York, US",
        ["New York", "USA"]],
    ["New York, USA",
        ["New York", "USA"]],
    ["New York, United States",
        ["New York", "USA"]],
    ["New York, United States of America",
        ["New York", "USA"]],

    ["New Jersey, US",
        ["New Jersey", "USA"]],
    ["New Jersey, USA",
        ["New Jersey", "USA"]],
    ["New Jersey, United States",
        ["New Jersey", "USA"]],
    ["New Jersey, United States of America",
        ["New Jersey", "USA"]],

    ["California, US",
        ["California", "USA"]],
    ["California, USA",
        ["California", "USA"]],
    ["California, United States",
        ["California", "USA"]],
    ["California, United States of America",
        ["California", "USA"]],

    ["Connecticut, US",
        ["Connecticut", "USA"]],
    ["Connecticut, USA",
        ["Connecticut", "USA"]],
    ["Connecticut, United States",
        ["Connecticut", "USA"]],
    ["Connecticut, United States of America",
        ["Connecticut", "USA"]],

    ["Minnesota, US",
        ["Minnesota", "USA"]],
    ["Minnesota, USA",
        ["Minnesota", "USA"]],
    ["Minnesota, United States",
        ["Minnesota", "USA"]],
    ["Minnesota, United States of America",
        ["Minnesota", "USA"]],

    # United Kingdom
    ["Bedford, GB",
        ["Bedford", "GBR"]],
    ["Bedford, GBR",
        ["Bedford", "GBR"]],
    ["Bedford, United Kingdom",
        ["Bedford", "GBR"]],

    ["Bournemouth, GB",
        ["Bournemouth", "GBR"]],
    ["Bournemouth, GBR",
        ["Bournemouth", "GBR"]],
    ["Bournemouth, United Kingdom",
        ["Bournemouth", "GBR"]],

    ["Bury, GB",
        ["Bury", "GBR"]],
    ["Bury, GBR",
        ["Bury", "GBR"]],
    ["Bury, United Kingdom",
        ["Bury", "GBR"]],

    ["Argyll and Bute, GB",
        ["Argyll and Bute", "GBR"]],
    ["Argyll and Bute, GBR",
        ["Argyll and Bute", "GBR"]],
    ["Argyll and Bute, United Kingdom",
        ["Argyll and Bute", "GBR"]],

    ["London Borough of Lambeth, GB",
        ["London Borough of Lambeth", "GBR"]],
    ["London Borough of Lambeth, GBR",
        ["London Borough of Lambeth", "GBR"]],
    ["London Borough of Lambeth, United Kingdom",
        ["London Borough of Lambeth", "GBR"]],

    ["Neath Port Talbot County Borough, GB",
        ["Neath Port Talbot County Borough", "GBR"]],
    ["Neath Port Talbot County Borough, GBR",
        ["Neath Port Talbot County Borough", "GBR"]],
    ["Neath Port Talbot County Borough, United Kingdom",
        ["Neath Port Talbot County Borough", "GBR"]],

    ["Norfolk, GB",
        ["Norfolk", "GBR"]],
    ["Norfolk, GBR",
        ["Norfolk", "GBR"]],
    ["Norfolk, United Kingdom",
        ["Norfolk", "GBR"]],

    # Canada
    ["Saskatchewan, CA",
        ["Saskatchewan", "CAN"]],
    ["Saskatchewan, CAN",
        ["Saskatchewan", "CAN"]],
    ["Saskatchewan, Canada",
        ["Saskatchewan", "CAN"]],

    ["Nova Scotia, CA",
        ["Nova Scotia", "CAN"]],
    ["Nova Scotia, CAN",
        ["Nova Scotia", "CAN"]],
    ["Nova Scotia, Canada",
        ["Nova Scotia", "CAN"]],

    ["Ontario, CA",
        ["Ontario", "CAN"]],
    ["Ontario, CAN",
        ["Ontario", "CAN"]],
    ["Ontario, Canada",
        ["Ontario", "CAN"]],

    ["Quebec, CA",
        ["Quebec", "CAN"]],
    ["Quebec, CAN",
        ["Quebec", "CAN"]],
    ["Quebec, Canada",
        ["Quebec", "CAN"]],

    ["Alberta, CA",
        ["Alberta", "CAN"]],
    ["Alberta, CAN",
        ["Alberta", "CAN"]],
    ["Alberta, Canada",
        ["Alberta", "CAN"]],

    ["Manitoba, CA",
        ["Manitoba", "CAN"]],
    ["Manitoba, CAN",
        ["Manitoba", "CAN"]],
    ["Manitoba, Canada",
        ["Manitoba", "CAN"]],

    # Poland
    ["Opole Voivodeship, PL",
        ["Opole Voivodeship", "POL"]],
    ["Opole Voivodeship, POL",
        ["Opole Voivodeship", "POL"]],
    ["Opole Voivodeship, Poland",
        ["Opole Voivodeship", "POL"]],

    ["Lublin Voivodeship, PL",
        ["Lublin Voivodeship", "POL"]],
    ["Lublin Voivodeship, POL",
        ["Lublin Voivodeship", "POL"]],
    ["Lublin Voivodeship, Poland",
        ["Lublin Voivodeship", "POL"]],

    # Australia
    ["Victoria, AU",
        ["Victoria", "AUS"]],
    ["Victoria, AUS",
        ["Victoria", "AUS"]],
    ["Victoria, Australia",
        ["Victoria", "AUS"]],

    ["Northern Territory, AU",
        ["Northern Territory", "AUS"]],
    ["Northern Territory, AUS",
        ["Northern Territory", "AUS"]],
    ["Northern Territory, Australia",
        ["Northern Territory", "AUS"]],

    ["Western Australia, AU",
        ["Western Australia", "AUS"]],
    ["Western Australia, AUS",
        ["Western Australia", "AUS"]],
    ["Western Australia, Australia",
        ["Western Australia", "AUS"]],

    ["Queensland, AU",
        ["Queensland", "AUS"]],
    ["Queensland, AUS",
        ["Queensland", "AUS"]],
    ["Queensland, Australia",
        ["Queensland", "AUS"]],
]

cities_to_test = [
    # United States
    ["Applewood, CO, US",
        ["Applewood", "Colorado", "USA"]],
    ["Applewood, Colorado, US",
        ["Applewood", "Colorado", "USA"]],
    ["Applewood, CO, USA",
        ["Applewood", "Colorado", "USA"]],
    ["Applewood, Colorado, USA",
        ["Applewood", "Colorado", "USA"]],
    ["Applewood, CO, United States",
        ["Applewood", "Colorado", "USA"]],
    ["Applewood, Colorado, United States",
        ["Applewood", "Colorado", "USA"]],
    ["Applewood, CO, United States of America",
        ["Applewood", "Colorado", "USA"]],
    ["Applewood, Colorado, United States of America",
        ["Applewood", "Colorado", "USA"]],

    ["Platteville, CO, US",
        ["Platteville", "Colorado", "USA"]],
    ["Platteville, Colorado, US",
        ["Platteville", "Colorado", "USA"]],
    ["Platteville, CO, USA",
        ["Platteville", "Colorado", "USA"]],
    ["Platteville, Colorado, USA",
        ["Platteville", "Colorado", "USA"]],
    ["Platteville, CO, United States",
        ["Platteville", "Colorado", "USA"]],
    ["Platteville, Colorado, United States",
        ["Platteville", "Colorado", "USA"]],
    ["Platteville, CO, United States of America",
        ["Platteville", "Colorado", "USA"]],
    ["Platteville, Colorado, United States of America",
        ["Platteville", "Colorado", "USA"]],

    ["San Juan County, CO, US",
        ["San Juan County", "Colorado", "USA"]],
    ["San Juan County, Colorado, US",
        ["San Juan County", "Colorado", "USA"]],
    ["San Juan County, CO, USA",
        ["San Juan County", "Colorado", "USA"]],
    ["San Juan County, Colorado, USA",
        ["San Juan County", "Colorado", "USA"]],
    ["San Juan County, CO, United States",
        ["San Juan County", "Colorado", "USA"]],
    ["San Juan County, Colorado, United States",
        ["San Juan County", "Colorado", "USA"]],
    ["San Juan County, CO, United States of America",
        ["San Juan County", "Colorado", "USA"]],
    ["San Juan County, Colorado, United States of America",
        ["San Juan County", "Colorado", "USA"]],

    ["Severance, CO, US",
        ["Severance", "Colorado", "USA"]],
    ["Severance, Colorado, US",
        ["Severance", "Colorado", "USA"]],
    ["Severance, CO, USA",
        ["Severance", "Colorado", "USA"]],
    ["Severance, Colorado, USA",
        ["Severance", "Colorado", "USA"]],
    ["Severance, CO, United States",
        ["Severance", "Colorado", "USA"]],
    ["Severance, Colorado, United States",
        ["Severance", "Colorado", "USA"]],
    ["Severance, CO, United States of America",
        ["Severance", "Colorado", "USA"]],
    ["Severance, Colorado, United States of America",
        ["Severance", "Colorado", "USA"]],

    ["West Pleasant View, CO, US",
        ["West Pleasant View", "Colorado", "USA"]],
    ["West Pleasant View, Colorado, US",
        ["West Pleasant View", "Colorado", "USA"]],
    ["West Pleasant View, CO, USA",
        ["West Pleasant View", "Colorado", "USA"]],
    ["West Pleasant View, Colorado, USA",
        ["West Pleasant View", "Colorado", "USA"]],
    ["West Pleasant View, CO, United States",
        ["West Pleasant View", "Colorado", "USA"]],
    ["West Pleasant View, Colorado, United States",
        ["West Pleasant View", "Colorado", "USA"]],
    ["West Pleasant View, CO, United States of America",
        ["West Pleasant View", "Colorado", "USA"]],
    ["West Pleasant View, Colorado, United States of America",
        ["West Pleasant View", "Colorado", "USA"]],

    ["Welby, CO, US",
        ["Welby", "Colorado", "USA"]],
    ["Welby, Colorado, US",
        ["Welby", "Colorado", "USA"]],
    ["Welby, CO, USA",
        ["Welby", "Colorado", "USA"]],
    ["Welby, Colorado, USA",
        ["Welby", "Colorado", "USA"]],
    ["Welby, CO, United States",
        ["Welby", "Colorado", "USA"]],
    ["Welby, Colorado, United States",
        ["Welby", "Colorado", "USA"]],
    ["Welby, CO, United States of America",
        ["Welby", "Colorado", "USA"]],
    ["Welby, Colorado, United States of America",
        ["Welby", "Colorado", "USA"]],

    ["Windsor, MO, US",
        ["Windsor", "Missouri", "USA"]],
    ["Windsor, Missouri, US",
        ["Windsor", "Missouri", "USA"]],
    ["Windsor, MO, USA",
        ["Windsor", "Missouri", "USA"]],
    ["Windsor, Missouri, USA",
        ["Windsor", "Missouri", "USA"]],
    ["Windsor, MO, United States",
        ["Windsor", "Missouri", "USA"]],
    ["Windsor, Missouri, United States",
        ["Windsor", "Missouri", "USA"]],
    ["Windsor, MO, United States of America",
        ["Windsor", "Missouri", "USA"]],
    ["Windsor, Missouri, United States of America",
        ["Windsor", "Missouri", "USA"]],

    ["San Diego, CA, US",
        ["San Diego", "California", "USA"]],
    ["San Diego, California, US",
        ["San Diego", "California", "USA"]],
    ["San Diego, CA, USA",
        ["San Diego", "California", "USA"]],
    ["San Diego, California, USA",
        ["San Diego", "California", "USA"]],
    ["San Diego, CA, United States",
        ["San Diego", "California", "USA"]],
    ["San Diego, California, United States",
        ["San Diego", "California", "USA"]],
    ["San Diego, CA, United States of America",
        ["San Diego", "California", "USA"]],
    ["San Diego, California, United States of America",
        ["San Diego", "California", "USA"]],

    # United Kingdom
    ["Bayston Hill, England, GBR",
        ["Bayston Hill", "England", "GBR"]],
    ["Bayston Hill, England, GB",
        ["Bayston Hill", "England", "GBR"]],
    ["Bayston Hill, England, United Kingdom",
        ["Bayston Hill", "England", "GBR"]],
    ["Bayston Hill, ENG, GBR",
        ["Bayston Hill", "England", "GBR"]],
    ["Bayston Hill, ENG, GB",
        ["Bayston Hill", "England", "GBR"]],
    ["Bayston Hill, ENG, United Kingdom",
        ["Bayston Hill", "England", "GBR"]],

    ["Beaminster, England, GBR",
        ["Beaminster", "England", "GBR"]],
    ["Beaminster, England, GB",
        ["Beaminster", "England", "GBR"]],
    ["Beaminster, England, United Kingdom",
        ["Beaminster", "England", "GBR"]],
    ["Beaminster, ENG, GBR",
        ["Beaminster", "England", "GBR"]],
    ["Beaminster, ENG, GB",
        ["Beaminster", "England", "GBR"]],
    ["Beaminster, ENG, United Kingdom",
        ["Beaminster", "England", "GBR"]],

    ["Cambridge, England, GBR",
        ["Cambridge", "England", "GBR"]],
    ["Cambridge, England, GB",
        ["Cambridge", "England", "GBR"]],
    ["Cambridge, England, United Kingdom",
        ["Cambridge", "England", "GBR"]],
    ["Cambridge, ENG, GBR",
        ["Cambridge", "England", "GBR"]],
    ["Cambridge, ENG, GB",
        ["Cambridge", "England", "GBR"]],
    ["Cambridge, ENG, United Kingdom",
        ["Cambridge", "England", "GBR"]],

    ["Canewdon, England, GBR",
        ["Canewdon", "England", "GBR"]],
    ["Canewdon, England, GB",
        ["Canewdon", "England", "GBR"]],
    ["Canewdon, England, United Kingdom",
        ["Canewdon", "England", "GBR"]],
    ["Canewdon, ENG, GBR",
        ["Canewdon", "England", "GBR"]],
    ["Canewdon, ENG, GB",
        ["Canewdon", "England", "GBR"]],
    ["Canewdon, ENG, United Kingdom",
        ["Canewdon", "England", "GBR"]],

    ["Codsall, England, GBR",
        ["Codsall", "England", "GBR"]],
    ["Codsall, England, GB",
        ["Codsall", "England", "GBR"]],
    ["Codsall, England, United Kingdom",
        ["Codsall", "England", "GBR"]],
    ["Codsall, ENG, GBR",
        ["Codsall", "England", "GBR"]],
    ["Codsall, ENG, GB",
        ["Codsall", "England", "GBR"]],
    ["Codsall, ENG, United Kingdom",
        ["Codsall", "England", "GBR"]],

    ["Shotley Gate, England, GBR",
        ["Shotley Gate", "England", "GBR"]],
    ["Shotley Gate, England, GB",
        ["Shotley Gate", "England", "GBR"]],
    ["Shotley Gate, England, United Kingdom",
        ["Shotley Gate", "England", "GBR"]],
    ["Shotley Gate, ENG, GBR",
        ["Shotley Gate", "England", "GBR"]],
    ["Shotley Gate, ENG, GB",
        ["Shotley Gate", "England", "GBR"]],
    ["Shotley Gate, ENG, United Kingdom",
        ["Shotley Gate", "England", "GBR"]],

    ["Sir Powys, Wales, GBR",
        ["Sir Powys", "Wales", "GBR"]],
    ["Sir Powys, Wales, GB",
        ["Sir Powys", "Wales", "GBR"]],
    ["Sir Powys, Wales, United Kingdom",
        ["Sir Powys", "Wales", "GBR"]],
    ["Sir Powys, WLS, GBR",
        ["Sir Powys", "Wales", "GBR"]],
    ["Sir Powys, WLS, GB",
        ["Sir Powys", "Wales", "GBR"]],
    ["Sir Powys, WLS, United Kingdom",
        ["Sir Powys", "Wales", "GBR"]],

    # Canada
    ["Casselman, Ontario, CAN",
        ["Casselman", "Ontario", "CAN"]],
    ["Casselman, Ontario, CA",
        ["Casselman", "Ontario", "CAN"]],
    ["Casselman, Ontario, Canada",
        ["Casselman", "Ontario", "CAN"]],
    ["Casselman, ON, CAN",
        ["Casselman", "Ontario", "CAN"]],
    ["Casselman, ON, CA",
        ["Casselman", "Ontario", "CAN"]],
    ["Casselman, ON, Canada",
        ["Casselman", "Ontario", "CAN"]],

    ["Chatham-Kent, Ontario, CAN",
        ["Chatham-Kent", "Ontario", "CAN"]],
    ["Chatham-Kent, Ontario, CA",
        ["Chatham-Kent", "Ontario", "CAN"]],
    ["Chatham-Kent, Ontario, Canada",
        ["Chatham-Kent", "Ontario", "CAN"]],
    ["Chatham-Kent, ON, CAN",
        ["Chatham-Kent", "Ontario", "CAN"]],
    ["Chatham-Kent, ON, CA",
        ["Chatham-Kent", "Ontario", "CAN"]],
    ["Chatham-Kent, ON, Canada",
        ["Chatham-Kent", "Ontario", "CAN"]],

    ["New Westminster, British Columbia, CAN",
        ["New Westminster", "British Columbia", "CAN"]],
    ["New Westminster, British Columbia, CA",
        ["New Westminster", "British Columbia", "CAN"]],
    ["New Westminster, British Columbia, Canada",
        ["New Westminster", "British Columbia", "CAN"]],
    ["New Westminster, BC, CAN",
        ["New Westminster", "British Columbia", "CAN"]],
    ["New Westminster, BC, CA",
        ["New Westminster", "British Columbia", "CAN"]],
    ["New Westminster, BC, Canada",
        ["New Westminster", "British Columbia", "CAN"]],

    ["North Bay, Ontario, CAN",
        ["North Bay", "Ontario", "CAN"]],
    ["North Bay, Ontario, CA",
        ["North Bay", "Ontario", "CAN"]],
    ["North Bay, Ontario, Canada",
        ["North Bay", "Ontario", "CAN"]],
    ["North Bay, ON, CAN",
        ["North Bay", "Ontario", "CAN"]],
    ["North Bay, ON, CA",
        ["North Bay", "Ontario", "CAN"]],
    ["North Bay, ON, Canada",
        ["North Bay", "Ontario", "CAN"]],

    ["Shannon, Quebec, CAN",
        ["Shannon", "Quebec", "CAN"]],
    ["Shannon, Quebec, CA",
        ["Shannon", "Quebec", "CAN"]],
    ["Shannon, Quebec, Canada",
        ["Shannon", "Quebec", "CAN"]],
    ["Shannon, QC, CAN",
        ["Shannon", "Quebec", "CAN"]],
    ["Shannon, QC, CA",
        ["Shannon", "Quebec", "CAN"]],
    ["Shannon, QC, Canada",
        ["Shannon", "Quebec", "CAN"]],

    # Poland
    ["Klembów, Masovian Voivodeship, POL",
        ["Klembów", "Masovian Voivodeship", "POL"]],
    ["Klembów, Masovian Voivodeship, PL",
        ["Klembów", "Masovian Voivodeship", "POL"]],
    ["Klembów, Masovian Voivodeship, Poland",
        ["Klembów", "Masovian Voivodeship", "POL"]],
    ["Klembów, MZ, POL",
        ["Klembów", "Masovian Voivodeship", "POL"]],
    ["Klembów, MZ, PL",
        ["Klembów", "Masovian Voivodeship", "POL"]],
    ["Klembów, MZ, Poland",
        ["Klembów", "Masovian Voivodeship", "POL"]],

    ["Klimontów, Świętokrzyskie Voivodeship, POL",
        ["Klimontów", "Świętokrzyskie Voivodeship", "POL"]],
    ["Klimontów, Świętokrzyskie Voivodeship, PL",
        ["Klimontów", "Świętokrzyskie Voivodeship", "POL"]],
    ["Klimontów, Świętokrzyskie Voivodeship, Poland",
        ["Klimontów", "Świętokrzyskie Voivodeship", "POL"]],
    ["Klimontów, SK, POL",
        ["Klimontów", "Świętokrzyskie Voivodeship", "POL"]],
    ["Klimontów, SK, PL",
        ["Klimontów", "Świętokrzyskie Voivodeship", "POL"]],
    ["Klimontów, SK, Poland",
        ["Klimontów", "Świętokrzyskie Voivodeship", "POL"]],

    ["Kowale, Pomeranian Voivodeship, POL",
        ["Kowale", "Pomeranian Voivodeship", "POL"]],
    ["Kowale, Pomeranian Voivodeship, PL",
        ["Kowale", "Pomeranian Voivodeship", "POL"]],
    ["Kowale, Pomeranian Voivodeship, Poland",
        ["Kowale", "Pomeranian Voivodeship", "POL"]],
    ["Kowale, PM, POL",
        ["Kowale", "Pomeranian Voivodeship", "POL"]],
    ["Kowale, PM, PL",
        ["Kowale", "Pomeranian Voivodeship", "POL"]],
    ["Kowale, PM, Poland",
        ["Kowale", "Pomeranian Voivodeship", "POL"]],

    ["Blizanów, Greater Poland Voivodeship, POL",
        ["Blizanów", "Greater Poland Voivodeship", "POL"]],
    ["Blizanów, Greater Poland Voivodeship, PL",
        ["Blizanów", "Greater Poland Voivodeship", "POL"]],
    ["Blizanów, Greater Poland Voivodeship, Poland",
        ["Blizanów", "Greater Poland Voivodeship", "POL"]],
    ["Blizanów, WP, POL",
        ["Blizanów", "Greater Poland Voivodeship", "POL"]],
    ["Blizanów, WP, PL",
        ["Blizanów", "Greater Poland Voivodeship", "POL"]],
    ["Blizanów, WP, Poland",
        ["Blizanów", "Greater Poland Voivodeship", "POL"]],

    ["Radomyśl, Podkarpackie Voivodeship, POL",
        ["Radomyśl", "Podkarpackie Voivodeship", "POL"]],
    ["Radomyśl, Podkarpackie Voivodeship, PL",
        ["Radomyśl", "Podkarpackie Voivodeship", "POL"]],
    ["Radomyśl, Podkarpackie Voivodeship, Poland",
        ["Radomyśl", "Podkarpackie Voivodeship", "POL"]],
    ["Radomyśl, PK, POL",
        ["Radomyśl", "Podkarpackie Voivodeship", "POL"]],
    ["Radomyśl, PK, PL",
        ["Radomyśl", "Podkarpackie Voivodeship", "POL"]],
    ["Radomyśl, PK, Poland",
        ["Radomyśl", "Podkarpackie Voivodeship", "POL"]],

    ["Rajcza, Silesian Voivodeship, POL",
        ["Rajcza", "Silesian Voivodeship", "POL"]],
    ["Rajcza, Silesian Voivodeship, PL",
        ["Rajcza", "Silesian Voivodeship", "POL"]],
    ["Rajcza, Silesian Voivodeship, Poland",
        ["Rajcza", "Silesian Voivodeship", "POL"]],
    ["Rajcza, SL, POL",
        ["Rajcza", "Silesian Voivodeship", "POL"]],
    ["Rajcza, SL, PL",
        ["Rajcza", "Silesian Voivodeship", "POL"]],
    ["Rajcza, SL, Poland",
        ["Rajcza", "Silesian Voivodeship", "POL"]],

    ["Susz, Warmian-Masurian Voivodeship, POL",
        ["Susz", "Warmian-Masurian Voivodeship", "POL"]],
    ["Susz, Warmian-Masurian Voivodeship, PL",
        ["Susz", "Warmian-Masurian Voivodeship", "POL"]],
    ["Susz, Warmian-Masurian Voivodeship, Poland",
        ["Susz", "Warmian-Masurian Voivodeship", "POL"]],
    ["Susz, WN, POL",
        ["Susz", "Warmian-Masurian Voivodeship", "POL"]],
    ["Susz, WN, PL",
        ["Susz", "Warmian-Masurian Voivodeship", "POL"]],
    ["Susz, WN, Poland",
        ["Susz", "Warmian-Masurian Voivodeship", "POL"]],

    # Australia
    ["Bridport, Tasmania, AUS",
        ["Bridport", "Tasmania", "AUS"]],
    ["Bridport, Tasmania, AU",
        ["Bridport", "Tasmania", "AUS"]],
    ["Bridport, Tasmania, Australia",
        ["Bridport", "Tasmania", "AUS"]],
    ["Bridport, TAS, AUS",
        ["Bridport", "Tasmania", "AUS"]],
    ["Bridport, TAS, AU",
        ["Bridport", "Tasmania", "AUS"]],
    ["Bridport, TAS, Australia",
        ["Bridport", "Tasmania", "AUS"]],

    ["Brisbane, Queensland, AUS",
        ["Brisbane", "Queensland", "AUS"]],
    ["Brisbane, Queensland, AU",
        ["Brisbane", "Queensland", "AUS"]],
    ["Brisbane, Queensland, Australia",
        ["Brisbane", "Queensland", "AUS"]],
    ["Brisbane, QLD, AUS",
        ["Brisbane", "Queensland", "AUS"]],
    ["Brisbane, QLD, AU",
        ["Brisbane", "Queensland", "AUS"]],
    ["Brisbane, QLD, Australia",
        ["Brisbane", "Queensland", "AUS"]],

    ["Brookvale, New South Wales, AUS",
        ["Brookvale", "New South Wales", "AUS"]],
    ["Brookvale, New South Wales, AU",
        ["Brookvale", "New South Wales", "AUS"]],
    ["Brookvale, New South Wales, Australia",
        ["Brookvale", "New South Wales", "AUS"]],
    ["Brookvale, NSW, AUS",
        ["Brookvale", "New South Wales", "AUS"]],
    ["Brookvale, NSW, AU",
        ["Brookvale", "New South Wales", "AUS"]],
    ["Brookvale, NSW, Australia",
        ["Brookvale", "New South Wales", "AUS"]],

    ["Gowrie, Australian Capital Territory, AUS",
        ["Gowrie", "Australian Capital Territory", "AUS"]],
    ["Gowrie, Australian Capital Territory, AU",
        ["Gowrie", "Australian Capital Territory", "AUS"]],
    ["Gowrie, Australian Capital Territory, Australia",
        ["Gowrie", "Australian Capital Territory", "AUS"]],
    ["Gowrie, ACT, AUS",
        ["Gowrie", "Australian Capital Territory", "AUS"]],
    ["Gowrie, ACT, AU",
        ["Gowrie", "Australian Capital Territory", "AUS"]],
    ["Gowrie, ACT, Australia",
        ["Gowrie", "Australian Capital Territory", "AUS"]],

    ["Katherine, Northern Territory, AUS",
        ["Katherine", "Northern Territory", "AUS"]],
    ["Katherine, Northern Territory, AU",
        ["Katherine", "Northern Territory", "AUS"]],
    ["Katherine, Northern Territory, Australia",
        ["Katherine", "Northern Territory", "AUS"]],
    ["Katherine, NT, AUS",
        ["Katherine", "Northern Territory", "AUS"]],
    ["Katherine, NT, AU",
        ["Katherine", "Northern Territory", "AUS"]],
    ["Katherine, NT, Australia",
        ["Katherine", "Northern Territory", "AUS"]],

    ["Park Holme, South Australia, AUS",
        ["Park Holme", "South Australia", "AUS"]],
    ["Park Holme, South Australia, AU",
        ["Park Holme", "South Australia", "AUS"]],
    ["Park Holme, South Australia, Australia",
        ["Park Holme", "South Australia", "AUS"]],
    ["Park Holme, SA, AUS",
        ["Park Holme", "South Australia", "AUS"]],
    ["Park Holme, SA, AU",
        ["Park Holme", "South Australia", "AUS"]],
    ["Park Holme, SA, Australia",
        ["Park Holme", "South Australia", "AUS"]],

    ["Potts Point, New South Wales, AUS",
        ["Potts Point", "New South Wales", "AUS"]],
    ["Potts Point, New South Wales, AU",
        ["Potts Point", "New South Wales", "AUS"]],
    ["Potts Point, New South Wales, Australia",
        ["Potts Point", "New South Wales", "AUS"]],
    ["Potts Point, NSW, AUS",
        ["Potts Point", "New South Wales", "AUS"]],
    ["Potts Point, NSW, AU",
        ["Potts Point", "New South Wales", "AUS"]],
    ["Potts Point, NSW, Australia",
        ["Potts Point", "New South Wales", "AUS"]],

    ["West Ballina, New South Wales, AUS",
        ["West Ballina", "New South Wales", "AUS"]],
    ["West Ballina, New South Wales, AU",
        ["West Ballina", "New South Wales", "AUS"]],
    ["West Ballina, New South Wales, Australia",
        ["West Ballina", "New South Wales", "AUS"]],
    ["West Ballina, NSW, AUS",
        ["West Ballina", "New South Wales", "AUS"]],
    ["West Ballina, NSW, AU",
        ["West Ballina", "New South Wales", "AUS"]],
    ["West Ballina, NSW, Australia",
        ["West Ballina", "New South Wales", "AUS"]],
]


class TestLocationParsing(unittest.TestCase):

    def test_countries(self):
        """
        Test that country names can be parsed to their respective ID's in the
        location database.
        Tests the function: string_to_location
        """
        # print(str(countries_to_test))
        with app.app_context():
            countries_ids = []
            for i in range(len(countries_to_test)):
                # print("Checking ISO3 " + str(countries_to_test[i][1]))
                countries_ids.append(
                    int(db.session.query(Country).filter(
                        Country.iso3 == countries_to_test[i][1]
                    ).first().id)
                )
                # print(countries_ids[i])

            for i in range(len(countries_ids)):
                tested_loc = string_to_location(
                    string_to_parse=countries_to_test[i][0]
                )
                self.assertIsNotNone(
                    tested_loc.country_id,
                    "Could not parse any country for " +
                    countries_to_test[i][0]
                )
                self.assertEqual(
                    int(countries_ids[i]),
                    int(tested_loc.country_id),
                    "Error: " +
                    str(countries_to_test[i][0]) +
                    " cannot be parsed. Got " +
                    (str(tested_loc.country_id)
                     if (tested_loc is not None and
                         tested_loc.country_id is not None and
                         isinstance(tested_loc.country_id, int))
                     else "Nothing")
                )

    def test_states(self):
        """
        Test that state names can be parsed to their respective ID's in the
        location database.
        Tests the function: string_to_location
        """
        # print(str(states_to_test))
        with app.app_context():
            countries_ids = []
            states_ids = []
            for i in range(len(states_to_test)):
                # print("Checking ISO3 " + str(states_to_test[i][1][1]))
                countries_ids.append(
                    int(db.session.query(Country).filter(
                        Country.iso3 == states_to_test[i][1][1]
                    ).first().id)
                )
                # print("Checking State " + str(states_to_test[i][1]))
                states_ids.append(
                    int(db.session.query(State).filter(
                        and_(
                            State.name == states_to_test[i][1][0],
                            State.country_id == countries_ids[i]
                        )
                    ).first().id)
                )
                # print(countries_ids[i])
                # print(states_ids[i])

            for i in range(len(states_to_test)):
                tested_loc = string_to_location(
                    string_to_parse=states_to_test[i][0]
                )
                self.assertIsNotNone(
                    tested_loc.country_id,
                    "Could not parse any country for " +
                    states_to_test[i][0]
                )
                self.assertIsNotNone(
                    tested_loc.state_id,
                    "Could not parse any state for " +
                    states_to_test[i][0]
                )
                self.assertEqual(
                    int(countries_ids[i]),
                    int(tested_loc.country_id),
                    "Error: Country " +
                    str(states_to_test[i][0]) +
                    " cannot be parsed. Got " +
                    (str(tested_loc.country_id)
                     if (tested_loc is not None and
                         tested_loc.country_id is not None and
                         isinstance(tested_loc.country_id, int))
                     else "Nothing")
                )
                self.assertEqual(
                    int(states_ids[i]),
                    int(tested_loc.state_id),
                    "Error: State " +
                    str(states_to_test[i][0]) +
                    " cannot be parsed. Got " +
                    (str(tested_loc.country_id)
                     if (tested_loc is not None and
                         tested_loc.state_id is not None and
                         isinstance(tested_loc.state_id, int))
                     else "Nothing")
                )

    def test_cities(self):
        """
        Test that city names can be parsed to their respective ID's in the
        location database.
        Tests the function: string_to_location
        """
        # print(str(cities_to_test))
        with app.app_context():
            countries_ids = []
            states_ids = []
            cities_ids = []
            for i in range(len(cities_to_test)):
                # print("Checking ISO3 " + str(cities_to_test[i][1][2]))
                countries_ids.append(
                    int(db.session.query(Country).filter(
                        Country.iso3 == cities_to_test[i][1][2]
                    ).first().id)
                )
                # print("Checking State " + str(cities_to_test[i][1]))
                states_ids.append(
                    int(db.session.query(State).filter(
                        and_(
                            State.name == cities_to_test[i][1][1],
                            State.country_id == countries_ids[i]
                        )
                    ).first().id)
                )

                # print("Checking City " + str(cities_to_test[i][0]))
                cities_ids.append(
                    int(db.session.query(City).filter(
                        and_(
                            City.name == cities_to_test[i][1][0],
                            City.state_id == states_ids[i],
                            City.country_id == countries_ids[i]
                        )
                    ).first().id)
                )
                # print(countries_ids[i])
                # print(states_ids[i])
                # print(cities_ids[i])

            for i in range(len(cities_to_test)):
                tested_loc = string_to_location(
                    string_to_parse=cities_to_test[i][0]
                )
                self.assertIsNotNone(
                    tested_loc.country_id,
                    "Could not parse any country for " +
                    cities_to_test[i][0]
                )
                self.assertIsNotNone(
                    tested_loc.state_id,
                    "Could not parse any state for " +
                    cities_to_test[i][0]
                )
                self.assertIsNotNone(
                    tested_loc.city_id,
                    "Could not parse any city for " +
                    cities_to_test[i][0]
                )
                self.assertIsNotNone(
                    countries_ids[i],
                    "Could not match database for country " +
                    cities_to_test[i][1][2]
                )
                self.assertIsNotNone(
                    states_ids[i],
                    "Could not match database for state " +
                    cities_to_test[i][1][1]
                )
                self.assertIsNotNone(
                    cities_ids[i],
                    "Could not match database for state " +
                    cities_to_test[i][0][0]
                )

                self.assertEqual(
                    int(countries_ids[i]),
                    int(tested_loc.country_id),
                    "Error: Country " +
                    str(cities_to_test[i][0]) +
                    " cannot be parsed. Got " +
                    (str(tested_loc.country_id)
                     if (tested_loc is not None and
                         tested_loc.country_id is not None and
                         isinstance(tested_loc.country_id, int))
                     else "Nothing")
                )
                self.assertEqual(
                    int(states_ids[i]),
                    int(tested_loc.state_id),
                    "Error: State " +
                    str(cities_to_test[i][0]) +
                    " cannot be parsed. Got " +
                    (str(tested_loc.state_id)
                     if (tested_loc is not None and
                         tested_loc.state_id is not None and
                         isinstance(tested_loc.state_id, int))
                     else "Nothing")
                )
                self.assertEqual(
                    int(cities_ids[i]),
                    int(tested_loc.city_id),
                    "Error: City " +
                    str(cities_to_test[i][0]) +
                    " cannot be parsed. Got " +
                    (str(tested_loc.city_id)
                     if (tested_loc is not None and
                         tested_loc.city_id is not None and
                         isinstance(tested_loc.city_id, int))
                     else "Nothing")
                )


if __name__ == '__main__':
    unittest.main()
