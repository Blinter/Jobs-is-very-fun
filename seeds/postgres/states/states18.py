"""
States Seed #18

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
            name="Soria",
            state_code="SO",
            latitude=41.7665464,
            longitude=-2.4790306,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Soriano",
            state_code="SO",
            latitude=-33.5102792,
            longitude=-57.7498103,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Soroca District",
            state_code="SO",
            latitude=48.1549743,
            longitude=28.2870783,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Soroti District",
            state_code="211",
            latitude=1.7229117,
            longitude=33.5280072,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Sorsogon",
            state_code="SOR",
            latitude=12.9927095,
            longitude=124.0147464,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Šoštanj Municipality",
            state_code="126",
            latitude=46.3782836,
            longitude=15.0461378,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Sotavento Islands",
            state_code="S",
            latitude=15,
            longitude=-24,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Soufrière Quarter",
            state_code="10",
            latitude=13.8570986,
            longitude=-61.0573248,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Souk Ahras",
            state_code="41",
            latitude=36.2801062,
            longitude=7.9384033,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Soum Province",
            state_code="SOM",
            latitude=14.0962841,
            longitude=-1.366216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Sourou Province",
            state_code="SOR",
            latitude=13.341803,
            longitude=-2.9375739,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Souss-Massa",
            state_code="09",
            latitude=30.2750611,
            longitude=-8.1338558,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Sousse",
            state_code="51",
            latitude=35.9022267,
            longitude=10.3497895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="South",
            state_code="SU",
            latitude=37.631595,
            longitude=-97.3458409,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cameroon")][0]),
        ))
        list_of_states.append(State(
            name="South",
            state_code="JA",
            latitude=33.2721479,
            longitude=35.2032778,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lebanon")][0]),
        ))
        list_of_states.append(State(
            name="South Abaco",
            state_code="SO",
            latitude=26.0640591,
            longitude=-77.2635038,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="South Aegean",
            state_code="L",
            latitude=37.0855302,
            longitude=25.1489215,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="South Andros",
            state_code="SA",
            latitude=23.9713556,
            longitude=-77.6077865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="South Australia",
            state_code="SA",
            latitude=-30.0002315,
            longitude=136.2091547,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Australia")][0]),
        ))
        list_of_states.append(State(
            name="South Ayrshire",
            state_code="SAY",
            latitude=55.4588988,
            longitude=-4.6291994,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="South Bačka District",
            state_code="06",
            latitude=45.4890344,
            longitude=19.6976187,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="South Banat District",
            state_code="04",
            latitude=45.0027457,
            longitude=21.0542509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="South Caribbean Coast",
            state_code="AS",
            latitude=12.1918502,
            longitude=-84.1012861,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="South Carolina",
            state_code="SC",
            latitude=33.836081,
            longitude=-81.1637245,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="South Central Province",
            state_code="SC",
            latitude=7.2564996,
            longitude=80.7214417,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="South Chungcheong Province",
            state_code="44",
            latitude=36.5184,
            longitude=126.8,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="South Cotabato",
            state_code="SCO",
            latitude=6.3357565,
            longitude=124.7740793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="South Dakota",
            state_code="SD",
            latitude=43.9695148,
            longitude=-99.9018131,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="South Darfur",
            state_code="DS",
            latitude=11.6488639,
            longitude=24.9042208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="South East",
            state_code="04",
            latitude=1.3571,
            longitude=103.7004,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Singapore")][0]),
        ))
        list_of_states.append(State(
            name="South Eleuthera",
            state_code="SE",
            latitude=24.7708562,
            longitude=-76.2131474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="South Gloucestershire",
            state_code="SGC",
            latitude=51.5264361,
            longitude=-2.4728487,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="South Gyeongsang Province",
            state_code="48",
            latitude=35.4606,
            longitude=128.2132,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="South Hamgyong Province",
            state_code="08",
            latitude=40.3725339,
            longitude=128.298884,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="South Holland",
            state_code="ZH",
            latitude=51.9966792,
            longitude=4.5597397,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="South Hwanghae Province",
            state_code="05",
            latitude=38.2007215,
            longitude=125.4781926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="South Jeolla Province",
            state_code="46",
            latitude=34.8679,
            longitude=126.991,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="South Karelia",
            state_code="02",
            latitude=61.1181949,
            longitude=28.1024372,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="South Khorasan",
            state_code="29",
            latitude=32.5175643,
            longitude=59.1041758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="South Kordofan",
            state_code="KS",
            latitude=11.1990192,
            longitude=29.4179324,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="South Lanarkshire",
            state_code="SLK",
            latitude=55.6735909,
            longitude=-3.7819661,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="South Province",
            state_code="SU",
            latitude=-21.7482006,
            longitude=166.1783739,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="South Province",
            state_code="01",
            latitude=-22.2758,
            longitude=166.458,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Caledonia")][0]),
        ))
        list_of_states.append(State(
            name="South Pyongan Province",
            state_code="02",
            latitude=39.3539178,
            longitude=126.168271,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="South Sardinia",
            state_code="SU",
            latitude=39.3893535,
            longitude=8.9397,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="South Sinai",
            state_code="JS",
            latitude=29.3101828,
            longitude=34.1531947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="South Tyneside",
            state_code="STY",
            latitude=54.9636693,
            longitude=-1.4418634,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="South West",
            state_code="05",
            latitude=1.3571,
            longitude=103.9451,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Singapore")][0]),
        ))
        list_of_states.append(State(
            name="South-East District",
            state_code="SE",
            latitude=31.2163798,
            longitude=-82.3527044,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Botswana")][0]),
        ))
        list_of_states.append(State(
            name="Southampton",
            state_code="SOU",
            latitude=32.2540095,
            longitude=-64.8259058,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bermuda")][0]),
        ))
        list_of_states.append(State(
            name="Southend-on-Sea",
            state_code="SOS",
            latitude=51.5459269,
            longitude=0.7077123,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Southern",
            state_code="14",
            latitude=25.9381018,
            longitude=50.5756887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bahrain")][0]),
        ))
        list_of_states.append(State(
            name="Southern",
            state_code="HSO",
            latitude=22.24725,
            longitude=114.15884,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Southern District",
            state_code="SO",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Botswana")][0]),
        ))
        list_of_states.append(State(
            name="Southern District",
            state_code="D",
            latitude=40.7137586,
            longitude=-74.0009059,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Israel")][0]),
        ))
        list_of_states.append(State(
            name="Southern Highlands Province",
            state_code="SHM",
            latitude=-6.4179083,
            longitude=143.5635637,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Southern Leyte",
            state_code="SLE",
            latitude=10.3346206,
            longitude=125.1708741,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Southern Nations, Nationalities, and Peoples' Region",
            state_code="SN",
            latitude=6.5156911,
            longitude=36.954107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ethiopia")][0]),
        ))
        list_of_states.append(State(
            name="Southern Ostrobothnia",
            state_code="03",
            latitude=62.9433099,
            longitude=23.5285267,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Southern Peninsula Region",
            state_code="2",
            latitude=63.9154803,
            longitude=-22.3649667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iceland")][0]),
        ))
        list_of_states.append(State(
            name="Southern Province",
            state_code="05",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Rwanda")][0]),
        ))
        list_of_states.append(State(
            name="Southern Province",
            state_code="S",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sierra Leone")][0]),
        ))
        list_of_states.append(State(
            name="Southern Province",
            state_code="3",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Southern Province",
            state_code="07",
            latitude=6.237375,
            longitude=80.543845,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zambia")][0]),
        ))
        list_of_states.append(State(
            name="Southern Red Sea Region",
            state_code="DK",
            latitude=13.5137103,
            longitude=41.7606472,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Eritrea")][0]),
        ))
        list_of_states.append(State(
            name="Southern Region",
            state_code="8",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iceland")][0]),
        ))
        list_of_states.append(State(
            name="Southern Region",
            state_code="S",
            latitude=32.7504957,
            longitude=-97.3315476,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Southern Savonia",
            state_code="04",
            latitude=61.6945148,
            longitude=27.8005015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Southland Region",
            state_code="STL",
            latitude=-45.8489159,
            longitude=167.6755387,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Southwest",
            state_code="SW",
            latitude=36.1908813,
            longitude=-95.8897448,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cameroon")][0]),
        ))
        list_of_states.append(State(
            name="Spanish Wells",
            state_code="SW",
            latitude=26.3250599,
            longitude=-81.7980328,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Split-Dalmatia",
            state_code="17",
            latitude=43.5240328,
            longitude=16.8178377,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Središče ob Dravi",
            state_code="202",
            latitude=46.3959282,
            longitude=16.2704915,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Srem District",
            state_code="07",
            latitude=45.0029171,
            longitude=19.8013773,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="St Helens",
            state_code="SHN",
            latitude=45.858961,
            longitude=-122.8212356,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="St. Gallen",
            state_code="SG",
            latitude=47.1456254,
            longitude=9.3504332,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="St. Julian's",
            state_code="48",
            latitude=42.2122513,
            longitude=-85.8917127,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="St. Paul's Bay",
            state_code="51",
            latitude=35.936017,
            longitude=14.3966503,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Staffordshire",
            state_code="STS",
            latitude=52.8792745,
            longitude=-2.0571868,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Stann Creek District",
            state_code="SC",
            latitude=16.8116631,
            longitude=-88.4016041,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belize")][0]),
        ))
        list_of_states.append(State(
            name="Stara Zagora Province",
            state_code="24",
            latitude=42.4257709,
            longitude=25.6344855,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Staro Nagoričane Municipality",
            state_code="71",
            latitude=42.2191692,
            longitude=21.9045541,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Starše Municipality",
            state_code="115",
            latitude=46.4674331,
            longitude=15.7640546,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Stavropol Krai",
            state_code="STA",
            latitude=44.6680993,
            longitude=43.520214,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Ștefan Vodă District",
            state_code="SV",
            latitude=46.5540488,
            longitude=29.702242,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Štip Municipality",
            state_code="83",
            latitude=41.7079297,
            longitude=22.1907122,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Stirling",
            state_code="STG",
            latitude=56.1165227,
            longitude=-3.9369029,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Stockholm County",
            state_code="AB",
            latitude=59.6024958,
            longitude=18.1384383,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Stockport",
            state_code="SKP",
            latitude=53.4106316,
            longitude=-2.1575332,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Stockton-on-Tees",
            state_code="STT",
            latitude=54.5704551,
            longitude=-1.3289821,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Stopiņi Municipality",
            state_code="095",
            latitude=56.936449,
            longitude=24.2872949,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Štore Municipality",
            state_code="127",
            latitude=46.2222514,
            longitude=15.3126116,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Strabane District Council",
            state_code="STB",
            latitude=54.8273865,
            longitude=-7.4633103,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Strakonice",
            state_code="316",
            latitude=49.2604043,
            longitude=13.9103085,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Strășeni District",
            state_code="ST",
            latitude=47.1450267,
            longitude=28.6136736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Straža Municipality",
            state_code="203",
            latitude=45.7768428,
            longitude=15.0948694,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Středočeský kraj",
            state_code="20",
            latitude=49.8782223,
            longitude=14.9362955,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Strenči Municipality",
            state_code="096",
            latitude=57.6225471,
            longitude=25.8048086,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Struga Municipality",
            state_code="72",
            latitude=41.3173744,
            longitude=20.6645683,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Strumica Municipality",
            state_code="73",
            latitude=41.4378004,
            longitude=22.6427428,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Studeničani Municipality",
            state_code="74",
            latitude=41.9225639,
            longitude=21.5363965,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Stung Treng",
            state_code="19",
            latitude=13.576473,
            longitude=105.9699878,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Styria",
            state_code="6",
            latitude=47.3593442,
            longitude=14.4699827,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Austria")][0]),
        ))
        list_of_states.append(State(
            name="Suceava County",
            state_code="SV",
            latitude=47.5505548,
            longitude=25.741062,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Suchitepéquez Department",
            state_code="SU",
            latitude=14.4215982,
            longitude=-91.4048249,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Sucre",
            state_code="SUC",
            latitude=8.813977,
            longitude=-74.723283,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Sucre",
            state_code="R",
            latitude=-19.035345,
            longitude=-65.2592128,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Sucumbíos",
            state_code="U",
            latitude=0.0889231,
            longitude=-76.8897557,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Sud",
            state_code="SD",
            latitude=29.9213248,
            longitude=-90.0973772,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Haiti")][0]),
        ))
        list_of_states.append(State(
            name="Sud-Bandama",
            state_code="15",
            latitude=5.5357083,
            longitude=-5.5617279,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Sud-Comoé",
            state_code="13",
            latitude=5.552793,
            longitude=-3.2583626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Sud-Est",
            state_code="SE",
            latitude=18.2783598,
            longitude=-72.3547915,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Haiti")][0]),
        ))
        list_of_states.append(State(
            name="Sud-Kivu",
            state_code="SK",
            latitude=-3.011658,
            longitude=28.299435,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Sud-Ouest Region",
            state_code="13",
            latitude=10.4231493,
            longitude=-3.2583626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Sud-Ubangi",
            state_code="SU",
            latitude=3.2299942,
            longitude=19.1880047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Suez",
            state_code="SUZ",
            latitude=29.3682255,
            longitude=32.174605,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Suffolk",
            state_code="SFK",
            latitude=52.1872472,
            longitude=0.9707801,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Sughd Province",
            state_code="SU",
            latitude=39.5155326,
            longitude=69.097023,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tajikistan")][0]),
        ))
        list_of_states.append(State(
            name="Sükhbaatar Province",
            state_code="051",
            latitude=46.5653163,
            longitude=113.5380836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Sukhothai",
            state_code="64",
            latitude=43.6485556,
            longitude=-79.3746639,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Sul Province",
            state_code="S",
            latitude=-10.2866578,
            longitude=20.7122465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="Sulawesi Barat",
            state_code="SR",
            latitude=-2.8441371,
            longitude=119.2320784,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Sulawesi Selatan",
            state_code="SN",
            latitude=-3.6687994,
            longitude=119.9740534,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Sulawesi Tengah",
            state_code="ST",
            latitude=-1.4300254,
            longitude=121.4456179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Sulawesi Tenggara",
            state_code="SG",
            latitude=-4.14491,
            longitude=122.174605,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Sulawesi Utara",
            state_code="SA",
            latitude=0.6246932,
            longitude=123.9750018,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Sulaymaniyah",
            state_code="SU",
            latitude=35.5466348,
            longitude=45.3003683,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Sultan Kudarat",
            state_code="SUK",
            latitude=6.5069401,
            longitude=124.4198243,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Sulu",
            state_code="SLU",
            latitude=5.9749011,
            longitude=121.03351,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Šumadija District",
            state_code="12",
            latitude=44.2050678,
            longitude=20.7856565,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Sumatera Barat",
            state_code="SB",
            latitude=-0.7399397,
            longitude=100.8000051,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Sumatera Selatan",
            state_code="SS",
            latitude=-3.3194374,
            longitude=103.914399,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Sumatera Utara",
            state_code="SU",
            latitude=2.1153547,
            longitude=99.5450974,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Šumperk",
            state_code="715",
            latitude=49.9778407,
            longitude=16.9717754,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Sumqayit",
            state_code="SM",
            latitude=40.5854765,
            longitude=49.6317411,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Sumska oblast",
            state_code="59",
            latitude=50.9077,
            longitude=34.7981,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Sunamganj District",
            state_code="61",
            latitude=25.0714535,
            longitude=91.3991627,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Suphan Buri",
            state_code="72",
            latitude=14.4744892,
            longitude=100.1177128,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Surat Thani",
            state_code="84",
            latitude=9.1341949,
            longitude=99.3334198,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Surigao del Norte",
            state_code="SUN",
            latitude=9.514828,
            longitude=125.6969984,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Surigao del Sur",
            state_code="SUR",
            latitude=8.5404906,
            longitude=126.1144758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Surin",
            state_code="32",
            latitude=37.0358271,
            longitude=-95.6276367,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Surrey",
            state_code="SRY",
            latitude=51.3147593,
            longitude=-0.5599501,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Surxondaryo Region",
            state_code="SU",
            latitude=37.9409005,
            longitude=67.5708536,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Šuto Orizari Municipality",
            state_code="84",
            latitude=42.0290416,
            longitude=21.4097027,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Svalbard",
            state_code="21",
            latitude=77.8749725,
            longitude=20.9751821,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Svay Rieng",
            state_code="20",
            latitude=11.142722,
            longitude=105.8290298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Švenčionys District Municipality",
            state_code="49",
            latitude=55.1028098,
            longitude=26.0071855,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Sverdlovsk",
            state_code="SVE",
            latitude=56.8430993,
            longitude=60.6454086,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Sveta Ana Municipality",
            state_code="181",
            latitude=46.65,
            longitude=15.845278,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Sveta Trojica v Slovenskih Goricah Municipality",
            state_code="204",
            latitude=46.5680809,
            longitude=15.8823064,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Sveti Andraž v Slovenskih Goricah Municipality",
            state_code="182",
            latitude=46.5189747,
            longitude=15.9498262,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Sveti Jurij ob Ščavnici Municipality",
            state_code="116",
            latitude=46.5687452,
            longitude=16.0222528,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Sveti Jurij v Slovenskih Goricah Municipality",
            state_code="210",
            latitude=46.6170791,
            longitude=15.7804677,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Sveti Nikole Municipality",
            state_code="69",
            latitude=41.8980312,
            longitude=21.9999435,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Sveti Tomaž Municipality",
            state_code="205",
            latitude=46.4835283,
            longitude=16.079442,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Svitavy",
            state_code="533",
            latitude=49.7551629,
            longitude=16.4691861,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Swieqi",
            state_code="57",
            latitude=35.9191182,
            longitude=14.4694186,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Świętokrzyskie Voivodeship",
            state_code="SK",
            latitude=50.6261041,
            longitude=20.9406279,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Swindon",
            state_code="SWD",
            latitude=51.5557739,
            longitude=-1.7797176,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Sylhet District",
            state_code="60",
            latitude=24.8993357,
            longitude=91.8700473,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Sylhet Division",
            state_code="G",
            latitude=24.7049811,
            longitude=91.6760691,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Syunik Province",
            state_code="SU",
            latitude=39.5133112,
            longitude=46.3393234,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Armenia")][0]),
        ))
        list_of_states.append(State(
            name="Szabolcs-Szatmár-Bereg County",
            state_code="SZ",
            latitude=48.0394954,
            longitude=22.00333,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Szeged",
            state_code="SD",
            latitude=46.2530102,
            longitude=20.1414253,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Székesfehérvár",
            state_code="SF",
            latitude=47.1860262,
            longitude=18.4221358,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Szekszárd",
            state_code="SS",
            latitude=46.3474326,
            longitude=18.7062293,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Szolnok",
            state_code="SK",
            latitude=47.1621355,
            longitude=20.1824712,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Szombathely",
            state_code="SH",
            latitude=47.2306851,
            longitude=16.6218441,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Ta' Xbiex",
            state_code="58",
            latitude=35.8991448,
            longitude=14.4963519,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Ta'izz",
            state_code="TA",
            latitude=13.5775886,
            longitude=44.0177989,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Tabasco",
            state_code="TAB",
            latitude=17.8409173,
            longitude=-92.6189273,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Tábor",
            state_code="317",
            latitude=49.3646293,
            longitude=14.7191293,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Tabor Municipality",
            state_code="184",
            latitude=46.2107921,
            longitude=15.0174249,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Tabora",
            state_code="24",
            latitude=-5.0342138,
            longitude=32.8084496,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Tabuk",
            state_code="07",
            latitude=28.2453335,
            longitude=37.6386622,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Táchira",
            state_code="S",
            latitude=7.9137001,
            longitude=-72.1416132,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Tachov",
            state_code="327",
            latitude=49.7987803,
            longitude=12.6361921,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Tacna",
            state_code="TAC",
            latitude=-18.0065679,
            longitude=-70.2462741,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Tacuarembó",
            state_code="TA",
            latitude=-31.7206837,
            longitude=-55.9859887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Tadjourah Region",
            state_code="TA",
            latitude=11.9338885,
            longitude=42.3938375,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Djibouti")][0]),
        ))
        list_of_states.append(State(
            name="Tafea",
            state_code="TAE",
            latitude=-18.7237827,
            longitude=169.0645056,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vanuatu")][0]),
        ))
        list_of_states.append(State(
            name="Tafilah",
            state_code="AT",
            latitude=30.8338063,
            longitude=35.6160513,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jordan")][0]),
        ))
        list_of_states.append(State(
            name="Tagant",
            state_code="09",
            latitude=18.5467527,
            longitude=-9.9018131,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Tahoua Region",
            state_code="5",
            latitude=16.0902543,
            longitude=5.3939551,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Niger")][0]),
        ))
        list_of_states.append(State(
            name="Tai Po",
            state_code="NTP",
            latitude=22.45085,
            longitude=114.16422,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Taichung",
            state_code="TXG",
            latitude=24.1477358,
            longitude=120.6736482,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Tailevu",
            state_code="14",
            latitude=-17.8269111,
            longitude=178.293248,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Tainan",
            state_code="TNN",
            latitude=22.9997281,
            longitude=120.2270277,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Taipei",
            state_code="TPE",
            latitude=25.0329694,
            longitude=121.5654177,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Taita–Taveta",
            state_code="39",
            latitude=-3.3160687,
            longitude=38.4849923,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Taitung",
            state_code="TTT",
            latitude=22.7972447,
            longitude=121.0713702,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Taiwan",
            state_code="TW",
            latitude=23.69781,
            longitude=120.960515,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Tak",
            state_code="63",
            latitude=45.0299646,
            longitude=-93.1049815,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Takamaka",
            state_code="23",
            latitude=37.9645917,
            longitude=-1.2217727,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Takeo",
            state_code="21",
            latitude=10.9321519,
            longitude=104.798771,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Takhar",
            state_code="TAK",
            latitude=36.6698013,
            longitude=69.4784541,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Talas Region",
            state_code="T",
            latitude=42.2867339,
            longitude=72.5204827,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kyrgyzstan")][0]),
        ))
        list_of_states.append(State(
            name="Talsi Municipality",
            state_code="097",
            latitude=57.3415208,
            longitude=22.5713125,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Tamanghasset",
            state_code="11",
            latitude=22.7902972,
            longitude=5.5193268,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Tamaulipas",
            state_code="TAM",
            latitude=24.26694,
            longitude=-98.8362755,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Tambacounda Region",
            state_code="TC",
            latitude=13.5619011,
            longitude=-13.1740348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Tambov Oblast",
            state_code="TAM",
            latitude=52.6416589,
            longitude=41.4216451,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Tameside",
            state_code="TAM",
            latitude=53.4805828,
            longitude=-2.0809891,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Tamil Nadu",
            state_code="TN",
            latitude=11.1271225,
            longitude=78.6568942,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Tan-Tan (EH-partial)",
            state_code="TNT",
            latitude=28.03012,
            longitude=-11.1617356,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Tana River",
            state_code="40",
            latitude=-1.6518468,
            longitude=39.6518165,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Tandjilé",
            state_code="TA",
            latitude=9.6625729,
            longitude=16.7234639,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Tanga",
            state_code="25",
            latitude=-5.3049789,
            longitude=38.3165725,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Tangail District",
            state_code="63",
            latitude=24.3917427,
            longitude=89.9948257,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Tanganyika",
            state_code="TA",
            latitude=-6.2740118,
            longitude=27.9249002,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Tanger-Assilah",
            state_code="TNG",
            latitude=35.7632539,
            longitude=-5.9045098,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Tanger-Tétouan-Al Hoceïma",
            state_code="01",
            latitude=35.2629558,
            longitude=-5.5617279,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Tanintharyi Region",
            state_code="05",
            latitude=12.4706876,
            longitude=99.0128926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Taoudénit Region",
            state_code="10",
            latitude=22.6764132,
            longitude=-3.9789143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Taounate",
            state_code="TAO",
            latitude=34.536917,
            longitude=-4.6398693,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Taourirt",
            state_code="TAI",
            latitude=34.212598,
            longitude=-2.6983868,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Taoyuan",
            state_code="TAO",
            latitude=24.9936281,
            longitude=121.3009798,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Tapoa Province",
            state_code="TAP",
            latitude=12.2497072,
            longitude=1.6760691,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Taraba",
            state_code="TA",
            latitude=7.9993616,
            longitude=10.7739863,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Taraclia District",
            state_code="TA",
            latitude=45.898651,
            longitude=28.6671644,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Taranaki Region",
            state_code="TKI",
            latitude=-39.3538149,
            longitude=174.4382721,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Taranto",
            state_code="TA",
            latitude=40.5740901,
            longitude=17.2429976,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Tarapacá",
            state_code="TA",
            latitude=-20.2028799,
            longitude=-69.2877535,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Tarfaya (EH-partial)",
            state_code="TAF",
            latitude=27.9377701,
            longitude=-12.9294063,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Targovishte Province",
            state_code="25",
            latitude=43.2462349,
            longitude=26.5691251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Tarija Department",
            state_code="T",
            latitude=-21.5831595,
            longitude=-63.9586111,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bolivia")][0]),
        ))
        list_of_states.append(State(
            name="Tarlac",
            state_code="TAR",
            latitude=15.4754786,
            longitude=120.5963492,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Tarn",
            state_code="81",
            latitude=43.7914977,
            longitude=1.6758893,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Tarn-et-Garonne",
            state_code="82",
            latitude=44.080895,
            longitude=1.0891657,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Taroudannt",
            state_code="TAR",
            latitude=30.4727126,
            longitude=-8.8748765,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Tarrafal",
            state_code="TA",
            latitude=15.2760578,
            longitude=-23.7484077,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Tarrafal de São Nicolau",
            state_code="TS",
            latitude=16.5636498,
            longitude=-24.354942,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Tarragona",
            state_code="T",
            latitude=41.1258642,
            longitude=1.2035642,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Tartar District",
            state_code="TAR",
            latitude=40.3443875,
            longitude=46.9376519,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Tartu County",
            state_code="78",
            latitude=58.4057128,
            longitude=26.801576,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Tartus",
            state_code="TA",
            latitude=35.0006652,
            longitude=36.0023225,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Tarxien",
            state_code="59",
            latitude=35.8672552,
            longitude=14.5116405,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Tashkent",
            state_code="TK",
            latitude=41.2994958,
            longitude=69.2400734,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Tashkent Region",
            state_code="TO",
            latitude=41.2213234,
            longitude=69.8597406,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Tasman District",
            state_code="TAS",
            latitude=-41.4571184,
            longitude=172.820974,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Tasmania",
            state_code="TAS",
            latitude=-41.4545196,
            longitude=145.9706647,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Australia")][0]),
        ))
        list_of_states.append(State(
            name="Tata",
            state_code="TAT",
            latitude=29.750877,
            longitude=-7.9756343,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Tatabánya",
            state_code="TB",
            latitude=47.569246,
            longitude=18.404818,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Tataouine",
            state_code="83",
            latitude=32.1344122,
            longitude=10.0807298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Tauragė County",
            state_code="TA",
            latitude=55.3072586,
            longitude=22.3572939,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Tauragė District Municipality",
            state_code="50",
            latitude=55.250366,
            longitude=22.29095,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Tavastia Proper",
            state_code="06",
            latitude=60.907015,
            longitude=24.3005498,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Tavush Region",
            state_code="TV",
            latitude=40.8866296,
            longitude=45.339349,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Armenia")][0]),
        ))
        list_of_states.append(State(
            name="Tawi-Tawi",
            state_code="TAW",
            latitude=5.133811,
            longitude=119.950926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (18/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
