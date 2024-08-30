"""
States Seed #10

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""
from models.postgres.locations.regions import Region
from models.postgres.locations.subregions import Subregion
from models.postgres.locations.countries import Country
from models.postgres.locations.states import State
from models.postgres.locations.cities import City
from app import create_app, db

app = create_app()

with app.app_context():
    try:
        country_list = db.session.query(Country).all()
        list_of_states = []

        list_of_states.append(State(
            name="Kunene Region",
            state_code="KU",
            latitude=-19.4086317,
            longitude=13.914399,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Kungota",
            state_code="055",
            latitude=46.6418793,
            longitude=15.6036288,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kupiškis District Municipality",
            state_code="23",
            latitude=55.8428741,
            longitude=25.0295816,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Kurbin District",
            state_code="KB",
            latitude=41.6412644,
            longitude=19.705595,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Kurdamir District",
            state_code="KUR",
            latitude=40.3698651,
            longitude=48.1644626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Kurdistan",
            state_code="12",
            latitude=35.9553579,
            longitude=47.1362125,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Kurgan Oblast",
            state_code="KGN",
            latitude=55.4481548,
            longitude=65.1180975,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kurigram District",
            state_code="28",
            latitude=25.8072414,
            longitude=89.6294746,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Kursk Oblast",
            state_code="KRS",
            latitude=51.7634026,
            longitude=35.3811812,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kushtia District",
            state_code="30",
            latitude=23.8906995,
            longitude=89.1099368,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Kütahya",
            state_code="43",
            latitude=39.358137,
            longitude=29.6035495,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Kutná Hora",
            state_code="205",
            latitude=49.9492089,
            longitude=15.247044,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Kuyavian-Pomeranian Voivodeship",
            state_code="KP",
            latitude=53.1648363,
            longitude=18.4834224,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Kuzma Municipality",
            state_code="056",
            latitude=46.8351038,
            longitude=16.08071,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kvemo Kartli",
            state_code="KK",
            latitude=41.4791833,
            longitude=44.6560451,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Kwai Tsing",
            state_code="NKT",
            latitude=22.35488,
            longitude=114.08401,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Kwale",
            state_code="19",
            latitude=-4.1816115,
            longitude=39.4605612,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Kwango",
            state_code="KG",
            latitude=-6.4337409,
            longitude=17.668887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Kwara",
            state_code="KW",
            latitude=8.9668961,
            longitude=4.3874051,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="KwaZulu-Natal",
            state_code="KZN",
            latitude=-28.5305539,
            longitude=30.8958242,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Africa")][0]),
        ))
        list_of_states.append(State(
            name="Kween District",
            state_code="228",
            latitude=1.443879,
            longitude=34.597132,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kweneng District",
            state_code="KW",
            latitude=-23.8367249,
            longitude=25.2837585,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Botswana")][0]),
        ))
        list_of_states.append(State(
            name="Kwilu",
            state_code="KL",
            latitude=-5.1188825,
            longitude=18.4276047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Kwun Tong",
            state_code="KKT",
            latitude=22.31326,
            longitude=114.22581,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Kyankwanzi District",
            state_code="123",
            latitude=1.0966037,
            longitude=31.7195459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kyegegwa District",
            state_code="422",
            latitude=0.4818193,
            longitude=31.0550093,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kyenjojo District",
            state_code="415",
            latitude=0.6092923,
            longitude=30.6401231,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kyiv",
            state_code="30",
            latitude=50.4501,
            longitude=30.5234,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Kyivska oblast",
            state_code="32",
            latitude=50.0529506,
            longitude=30.7667134,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Kymenlaakso",
            state_code="09",
            latitude=60.780512,
            longitude=26.8829336,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Kyotera District",
            state_code="125",
            latitude=-0.6358988,
            longitude=31.5455637,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kyōto Prefecture",
            state_code="26",
            latitude=35.1566609,
            longitude=135.5251982,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Kyrenia District (Keryneia)",
            state_code="06",
            latitude=35.299194,
            longitude=33.2363246,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cyprus")][0]),
        ))
        list_of_states.append(State(
            name="Kyustendil Province",
            state_code="10",
            latitude=42.2868799,
            longitude=22.6939635,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Kyzylorda Region",
            state_code="KZY",
            latitude=44.6922613,
            longitude=62.6571885,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="L'Aquila",
            state_code="AQ",
            latitude=42.1256317,
            longitude=13.6362715,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="L'Oriental",
            state_code="02",
            latitude=37.069683,
            longitude=-94.512277,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="La Altagracia Province",
            state_code="11",
            latitude=18.5850236,
            longitude=-68.6201072,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="La Araucanía",
            state_code="AR",
            latitude=-38.948921,
            longitude=-72.331113,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="La Colle",
            state_code="CL",
            latitude=43.7327465,
            longitude=7.4137276,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Monaco")][0]),
        ))
        list_of_states.append(State(
            name="La Condamine",
            state_code="CO",
            latitude=43.7350665,
            longitude=7.419906,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Monaco")][0]),
        ))
        list_of_states.append(State(
            name="La Digue",
            state_code="15",
            latitude=49.7666922,
            longitude=-97.1546629,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="La Guaira",
            state_code="X",
            latitude=29.3052268,
            longitude=-94.7913854,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="La Guajira",
            state_code="LAG",
            latitude=11.3547743,
            longitude=-72.5204827,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="La Libertad",
            state_code="LAL",
            latitude=13.490697,
            longitude=-89.3084607,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="La Libertad Department",
            state_code="LI",
            latitude=13.6817661,
            longitude=-89.3606298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="La Massana",
            state_code="04",
            latitude=42.545625,
            longitude=1.5147392,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Andorra")][0]),
        ))
        list_of_states.append(State(
            name="La Pampa",
            state_code="L",
            latitude=-36.6147573,
            longitude=-64.2839209,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="La Paz Department",
            state_code="L",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bolivia")][0]),
        ))
        list_of_states.append(State(
            name="La Paz Department",
            state_code="PA",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="La Paz Department",
            state_code="LP",
            latitude=-15.0892416,
            longitude=-68.5247149,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="La Réunion",
            state_code="974",
            latitude=-21.115141,
            longitude=55.536384,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="La Rioja",
            state_code="F",
            latitude=-29.4193793,
            longitude=-66.8559932,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="La Rioja",
            state_code="LO",
            latitude=42.2870733,
            longitude=-2.539603,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="La Rivière Anglaise",
            state_code="16",
            latitude=-4.610615,
            longitude=55.4540841,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="La Romana Province",
            state_code="12",
            latitude=18.4310271,
            longitude=-68.9837373,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="La Spezia",
            state_code="SP",
            latitude=44.2447913,
            longitude=9.7678687,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="La Union",
            state_code="LUN",
            latitude=38.8766878,
            longitude=-77.1280912,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="La Unión Department",
            state_code="UN",
            latitude=13.4886443,
            longitude=-87.8942451,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="La Vega Province",
            state_code="13",
            latitude=19.2211554,
            longitude=-70.5288753,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Laamu Atoll",
            state_code="05",
            latitude=1.9430737,
            longitude=73.4180211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Lääne County",
            state_code="57",
            latitude=58.9722742,
            longitude=23.8740834,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Lääne-Viru County",
            state_code="59",
            latitude=59.3018816,
            longitude=26.3280312,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Laâyoune (EH)",
            state_code="LAA",
            latitude=27.1500384,
            longitude=-13.1990758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Laâyoune-Sakia El Hamra (EH-partial)",
            state_code="11",
            latitude=27.8683194,
            longitude=-11.9804613,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Labé Prefecture",
            state_code="LA",
            latitude=11.3541939,
            longitude=-12.3463875,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Labé Region",
            state_code="L",
            latitude=11.3232042,
            longitude=-12.2891314,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Laborie Quarter",
            state_code="07",
            latitude=13.7522783,
            longitude=-60.9932889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Labuan",
            state_code="15",
            latitude=5.2831456,
            longitude=115.230825,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Lac",
            state_code="LC",
            latitude=13.6915377,
            longitude=14.1001326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Lachin District",
            state_code="LAC",
            latitude=39.6383414,
            longitude=46.5460853,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Laconia",
            state_code="16",
            latitude=43.5278546,
            longitude=-71.4703509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Lacs District",
            state_code="LC",
            latitude=48.1980169,
            longitude=-80.4564412,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Lacs Region",
            state_code="07",
            latitude=47.7395866,
            longitude=-70.4186652,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Ladakh",
            state_code="LA",
            latitude=34.2268475,
            longitude=77.5619419,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Laghman",
            state_code="LAG",
            latitude=34.6897687,
            longitude=70.1455805,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Laghouat",
            state_code="03",
            latitude=33.8078341,
            longitude=2.8628294,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Lagos",
            state_code="LA",
            latitude=6.5243793,
            longitude=3.3792057,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Laguna",
            state_code="LAG",
            latitude=33.5427189,
            longitude=-117.7853568,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Lagunes District",
            state_code="LG",
            latitude=5.8827334,
            longitude=-4.2333355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Lagunes region",
            state_code="01",
            latitude=5.8827334,
            longitude=-4.2333355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Lahij",
            state_code="LA",
            latitude=13.1489588,
            longitude=44.8505495,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Lai Châu",
            state_code="01",
            latitude=22.3862227,
            longitude=103.4702631,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Laikipia",
            state_code="20",
            latitude=0.3606063,
            longitude=36.7819505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Lajas",
            state_code="079",
            latitude=18.049962,
            longitude=-67.0593449,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Lakes",
            state_code="LK",
            latitude=37.1628255,
            longitude=-95.6911623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Lakshadweep",
            state_code="LD",
            latitude=10.3280265,
            longitude=72.7846336,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Lakshmipur District",
            state_code="31",
            latitude=22.9446744,
            longitude=90.8281907,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Lalmonirhat District",
            state_code="32",
            latitude=25.9923398,
            longitude=89.2847251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Lâm Đồng",
            state_code="35",
            latitude=11.5752791,
            longitude=108.1428669,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Lambayeque",
            state_code="LAM",
            latitude=-6.7197666,
            longitude=-79.9080757,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Lampang",
            state_code="52",
            latitude=18.2855395,
            longitude=99.5127895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Lamphun",
            state_code="51",
            latitude=18.5744606,
            longitude=99.0087221,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Lampung",
            state_code="LA",
            latitude=-4.5585849,
            longitude=105.4068079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Lamu",
            state_code="21",
            latitude=-2.2355058,
            longitude=40.4720004,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Lamwo District",
            state_code="326",
            latitude=3.5707568,
            longitude=32.5372741,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Lanao del Norte",
            state_code="LAN",
            latitude=7.8721811,
            longitude=123.8857747,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Lanao del Sur",
            state_code="LAS",
            latitude=7.823176,
            longitude=124.4198243,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Lancashire",
            state_code="LAN",
            latitude=53.7632254,
            longitude=-2.7044052,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Landes",
            state_code="40",
            latitude=44.009508,
            longitude=-1.2538579,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Lạng Sơn",
            state_code="09",
            latitude=21.853708,
            longitude=106.761519,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Lankaran",
            state_code="LAN",
            latitude=38.7528669,
            longitude=48.8475015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Lankaran District",
            state_code="LA",
            latitude=38.7528669,
            longitude=48.8475015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Lào Cai",
            state_code="02",
            latitude=22.4809431,
            longitude=103.9754959,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Laois",
            state_code="LS",
            latitude=52.994295,
            longitude=-7.3323007,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Lapland",
            state_code="10",
            latitude=67.9222304,
            longitude=26.5046438,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Lara",
            state_code="K",
            latitude=33.9822165,
            longitude=-118.1322747,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Larache",
            state_code="LAR",
            latitude=35.1744271,
            longitude=-6.1473964,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Lares",
            state_code="081",
            latitude=34.0250802,
            longitude=-118.4594593,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Larissa Prefecture",
            state_code="42",
            latitude=39.6390224,
            longitude=22.4191254,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Larnaca District (Larnaka)",
            state_code="03",
            latitude=34.8507206,
            longitude=33.4831906,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cyprus")][0]),
        ))
        list_of_states.append(State(
            name="Larne Borough Council",
            state_code="LRN",
            latitude=54.8578003,
            longitude=-5.8236224,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Las Marías",
            state_code="083",
            latitude=35.8382238,
            longitude=-78.6103566,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Las Palmas",
            state_code="GC",
            latitude=28.2915637,
            longitude=-16.6291304,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Las Piedras",
            state_code="085",
            latitude=18.1855753,
            longitude=-65.8736245,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Las Tunas Province",
            state_code="10",
            latitude=21.0605162,
            longitude=-76.9182097,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Laško Municipality",
            state_code="057",
            latitude=46.1542236,
            longitude=15.2361491,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Latakia",
            state_code="LA",
            latitude=35.6129791,
            longitude=36.0023225,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Latina",
            state_code="LT",
            latitude=41.4087476,
            longitude=13.0817903,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Lau",
            state_code="05",
            latitude=31.6687015,
            longitude=-106.3955763,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Lautém Municipality",
            state_code="LA",
            latitude=-8.3642307,
            longitude=126.9043845,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Timor-Leste")][0]),
        ))
        list_of_states.append(State(
            name="Lavalleja",
            state_code="LA",
            latitude=-33.9226175,
            longitude=-54.9765794,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Lazdijai District Municipality",
            state_code="24",
            latitude=54.2343267,
            longitude=23.5156505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Lazio",
            state_code="62",
            latitude=41.812241,
            longitude=12.73851,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Lebap Region",
            state_code="L",
            latitude=38.1272462,
            longitude=64.7162415,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkmenistan")][0]),
        ))
        list_of_states.append(State(
            name="Lecce",
            state_code="LE",
            latitude=40.2347393,
            longitude=18.1428669,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Lecco",
            state_code="LC",
            latitude=45.9382941,
            longitude=9.385729,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Leeds",
            state_code="LDS",
            latitude=53.8007554,
            longitude=-1.5490774,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Lefkada Regional Unit",
            state_code="24",
            latitude=38.8333663,
            longitude=20.7069108,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Leicestershire",
            state_code="LEC",
            latitude=52.772571,
            longitude=-1.2052126,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Leinster",
            state_code="L",
            latitude=53.3271538,
            longitude=-7.5140841,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Leiria",
            state_code="10",
            latitude=39.7709532,
            longitude=-8.7921836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Lékoumou Department",
            state_code="2",
            latitude=-3.170382,
            longitude=13.3587288,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Lélouma Prefecture",
            state_code="LE",
            latitude=11.183333,
            longitude=-12.933333,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Lempira Department",
            state_code="LE",
            latitude=14.1887698,
            longitude=-88.556531,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Lenart Municipality",
            state_code="058",
            latitude=46.5834424,
            longitude=15.8262125,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Lendava Municipality",
            state_code="059",
            latitude=46.5513483,
            longitude=16.4419839,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Leningrad Oblast",
            state_code="LEN",
            latitude=60.0793208,
            longitude=31.8926645,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="León",
            state_code="LE",
            latitude=12.5092037,
            longitude=-86.6611083,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="León",
            state_code="LE",
            latitude=42.5987041,
            longitude=-5.5670839,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Léraba Province",
            state_code="LER",
            latitude=10.6648785,
            longitude=-5.3102505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Leribe District",
            state_code="C",
            latitude=-28.8638065,
            longitude=28.0478826,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lesotho")][0]),
        ))
        list_of_states.append(State(
            name="Lerik District",
            state_code="LER",
            latitude=38.7736192,
            longitude=48.4151483,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Les Mamelles",
            state_code="24",
            latitude=38.8250505,
            longitude=-90.4834517,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Lesser Poland Voivodeship",
            state_code="MA",
            latitude=49.7225306,
            longitude=20.2503358,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Leste Province",
            state_code="L",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="Leyte",
            state_code="LEY",
            latitude=10.8624536,
            longitude=124.8811195,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Lezhë County",
            state_code="08",
            latitude=41.7813759,
            longitude=19.8067916,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Lezhë District",
            state_code="LE",
            latitude=41.786073,
            longitude=19.6460758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Lhaviyani Atoll",
            state_code="03",
            latitude=5.3747021,
            longitude=73.5122928,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Lhuntse District",
            state_code="44",
            latitude=27.8264989,
            longitude=91.135302,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Liaoning",
            state_code="LN",
            latitude=41.9436543,
            longitude=122.5290376,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Liberec",
            state_code="513",
            latitude=50.7564101,
            longitude=14.9965041,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Liberecký kraj",
            state_code="51",
            latitude=50.659424,
            longitude=14.7632424,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Libertador General Bernardo O'Higgins",
            state_code="LI",
            latitude=-34.5755374,
            longitude=-71.0022311,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Librazhd District",
            state_code="LB",
            latitude=41.1829232,
            longitude=20.3174769,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Liège",
            state_code="WLG",
            latitude=50.6325574,
            longitude=5.5796662,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="Lielvārde Municipality",
            state_code="053",
            latitude=56.7392976,
            longitude=24.9711618,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Lienchiang",
            state_code="LIE",
            latitude=26.1505556,
            longitude=119.9288889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Liepāja",
            state_code="LPX",
            latitude=56.5046678,
            longitude=21.010806,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Līgatne Municipality",
            state_code="055",
            latitude=57.1944204,
            longitude=25.0940681,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Liguria",
            state_code="42",
            latitude=44.3167917,
            longitude=8.3964938,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Lija",
            state_code="24",
            latitude=49.180076,
            longitude=-123.103317,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Lika-Senj",
            state_code="09",
            latitude=44.6192218,
            longitude=15.4701608,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Likoma District",
            state_code="LK",
            latitude=-12.0584005,
            longitude=34.7354031,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Likouala Department",
            state_code="7",
            latitude=2.043924,
            longitude=17.668887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Lilongwe District",
            state_code="LI",
            latitude=-14.0475228,
            longitude=33.617577,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Lima",
            state_code="LIM",
            latitude=-12.0463731,
            longitude=-77.042754,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Limassol District (Leymasun)",
            state_code="02",
            latitude=34.7071301,
            longitude=33.0226174,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cyprus")][0]),
        ))
        list_of_states.append(State(
            name="Limavady Borough Council",
            state_code="LMV",
            latitude=55.051682,
            longitude=-6.9491944,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Limbaži Municipality",
            state_code="054",
            latitude=57.5403227,
            longitude=24.7134451,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Limburg",
            state_code="VLI",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="Limburg",
            state_code="LI",
            latitude=51.4427238,
            longitude=6.0608726,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Limerick",
            state_code="LK",
            latitude=52.5090517,
            longitude=-8.7474955,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Limón Province",
            state_code="L",
            latitude=9.9896398,
            longitude=-83.0332417,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Costa Rica")][0]),
        ))
        list_of_states.append(State(
            name="Limpopo",
            state_code="LP",
            latitude=-23.4012946,
            longitude=29.4179324,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Africa")][0]),
        ))
        list_of_states.append(State(
            name="Lincolnshire",
            state_code="LIN",
            latitude=52.9451889,
            longitude=-0.1601246,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Lindi",
            state_code="12",
            latitude=-9.2343394,
            longitude=38.3165725,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Line Islands",
            state_code="L",
            latitude=1.7429439,
            longitude=-157.2132826,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kiribati")][0]),
        ))
        list_of_states.append(State(
            name="Lipetsk Oblast",
            state_code="LIP",
            latitude=52.5264702,
            longitude=39.2032269,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Lipkovo Municipality",
            state_code="48",
            latitude=42.2006626,
            longitude=21.6183755,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Liquiçá Municipality",
            state_code="LI",
            latitude=-8.6674095,
            longitude=125.2587964,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Timor-Leste")][0]),
        ))
        list_of_states.append(State(
            name="Lira District",
            state_code="307",
            latitude=2.2316169,
            longitude=32.9437667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Lisbon",
            state_code="11",
            latitude=38.7223263,
            longitude=-9.1392714,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Lisburn and Castlereagh",
            state_code="LBC",
            latitude=54.4981584,
            longitude=-6.1306791,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Lisburn City Council",
            state_code="LSB",
            latitude=54.4981584,
            longitude=-6.1306791,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Litija Municipality",
            state_code="060",
            latitude=46.0573226,
            longitude=14.8309636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Litoměřice",
            state_code="423",
            latitude=50.5384197,
            longitude=14.1305458,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Litoral Province",
            state_code="LI",
            latitude=1.5750244,
            longitude=9.8124935,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Equatorial Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Littoral",
            state_code="LT",
            latitude=48.4622757,
            longitude=-68.5178071,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cameroon")][0]),
        ))
        list_of_states.append(State(
            name="Littoral Department",
            state_code="LI",
            latitude=6.3806973,
            longitude=2.4406387,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Līvāni Municipality",
            state_code="056",
            latitude=56.3550942,
            longitude=26.172519,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Liverpool",
            state_code="LIV",
            latitude=32.6564981,
            longitude=-115.4763241,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Livorno",
            state_code="LI",
            latitude=43.0239848,
            longitude=10.6647101,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Ljubljana City Municipality",
            state_code="061",
            latitude=46.0569465,
            longitude=14.5057515,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Ljubno Municipality",
            state_code="062",
            latitude=46.3443125,
            longitude=14.8335492,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Ljutomer Municipality",
            state_code="063",
            latitude=46.5190848,
            longitude=16.1893216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Lleida",
            state_code="L",
            latitude=41.6183731,
            longitude=0.6024253,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Lobaye Prefecture",
            state_code="LB",
            latitude=4.3525981,
            longitude=17.4795173,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Lodi",
            state_code="LO",
            latitude=45.2405036,
            longitude=9.5292512,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Loei",
            state_code="42",
            latitude=17.4860232,
            longitude=101.7223002,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Lofa County",
            state_code="LO",
            latitude=8.1911184,
            longitude=-9.7232673,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Logar",
            state_code="LOG",
            latitude=34.0145518,
            longitude=69.1923916,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Logatec Municipality",
            state_code="064",
            latitude=45.917611,
            longitude=14.2351451,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Logone Occidental",
            state_code="LO",
            latitude=8.759676,
            longitude=15.876004,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Logone Oriental",
            state_code="LR",
            latitude=8.3149949,
            longitude=16.3463791,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Log–Dragomer Municipality",
            state_code="208",
            latitude=46.0178747,
            longitude=14.3687767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Loir-et-Cher",
            state_code="41",
            latitude=47.659376,
            longitude=0.8537631,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Loire",
            state_code="42",
            latitude=46.3522812,
            longitude=-1.1756339,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Loire-Atlantique",
            state_code="44",
            latitude=47.3475721,
            longitude=-2.3466312,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Loiret",
            state_code="45",
            latitude=47.9135431,
            longitude=1.760099,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Loíza",
            state_code="087",
            latitude=18.4329904,
            longitude=-65.87836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Loja",
            state_code="L",
            latitude=-3.99313,
            longitude=-79.20422,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Lola Prefecture",
            state_code="LO",
            latitude=7.9613818,
            longitude=-8.3964938,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Lomaiviti",
            state_code="06",
            latitude=-17.709,
            longitude=179.091,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Lomami",
            state_code="LO",
            latitude=-6.1453931,
            longitude=24.524264,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Lombardy",
            state_code="25",
            latitude=45.4790671,
            longitude=9.8452433,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Barking and Dagenham",
            state_code="BDG",
            latitude=51.5540666,
            longitude=0.134017,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Barnet",
            state_code="BNE",
            latitude=51.6049673,
            longitude=-0.2076295,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Bexley",
            state_code="BEX",
            latitude=51.4519021,
            longitude=0.1171786,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Brent",
            state_code="BEN",
            latitude=51.5672808,
            longitude=-0.2710568,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Bromley",
            state_code="BRY",
            latitude=51.3679705,
            longitude=0.070062,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Camden",
            state_code="CMD",
            latitude=51.5454736,
            longitude=-0.1627902,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Croydon",
            state_code="CRY",
            latitude=51.3827446,
            longitude=-0.0985163,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Ealing",
            state_code="EAL",
            latitude=51.5250366,
            longitude=-0.3413965,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Enfield",
            state_code="ENF",
            latitude=51.6622909,
            longitude=-0.1180651,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Hackney",
            state_code="HCK",
            latitude=51.573445,
            longitude=-0.0724376,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Hammersmith and Fulham",
            state_code="HMF",
            latitude=51.4990156,
            longitude=-0.22915,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Haringey",
            state_code="HRY",
            latitude=51.5906113,
            longitude=-0.1109709,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Harrow",
            state_code="HRW",
            latitude=51.5881627,
            longitude=-0.3422851,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Havering",
            state_code="HAV",
            latitude=51.577924,
            longitude=0.2120829,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Hillingdon",
            state_code="HIL",
            latitude=51.5351832,
            longitude=-0.4481378,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Hounslow",
            state_code="HNS",
            latitude=51.4828358,
            longitude=-0.3882062,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Islington",
            state_code="ISL",
            latitude=51.5465063,
            longitude=-0.1058058,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Lambeth",
            state_code="LBH",
            latitude=51.4571477,
            longitude=-0.1230681,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Lewisham",
            state_code="LEW",
            latitude=51.4414579,
            longitude=-0.0117006,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Merton",
            state_code="MRT",
            latitude=51.4097742,
            longitude=-0.2108084,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Newham",
            state_code="NWM",
            latitude=51.5255162,
            longitude=0.0352163,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Redbridge",
            state_code="RDB",
            latitude=51.5886121,
            longitude=0.0823982,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Richmond upon Thames",
            state_code="RIC",
            latitude=51.4613054,
            longitude=-0.3037709,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Southwark",
            state_code="SWK",
            latitude=51.4880572,
            longitude=-0.0762838,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Sutton",
            state_code="STN",
            latitude=51.3573762,
            longitude=-0.1752796,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Tower Hamlets",
            state_code="TWH",
            latitude=51.5202607,
            longitude=-0.0293396,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Waltham Forest",
            state_code="WFT",
            latitude=51.5886383,
            longitude=-0.0117625,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="London Borough of Wandsworth",
            state_code="WND",
            latitude=51.4568274,
            longitude=-0.1896638,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Long An",
            state_code="41",
            latitude=10.5607168,
            longitude=106.6497623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Long Island",
            state_code="LI",
            latitude=40.789142,
            longitude=-73.134961,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Longford",
            state_code="LD",
            latitude=53.7274982,
            longitude=-7.7931527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Lop Buri",
            state_code="16",
            latitude=14.7995081,
            longitude=100.6533706,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Lorestan",
            state_code="15",
            latitude=33.5818394,
            longitude=48.3988186,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (10/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
