"""
States Seed #13

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
            name="Narathiwat",
            state_code="96",
            latitude=6.4254607,
            longitude=101.8253143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Narayanganj District",
            state_code="40",
            latitude=23.7146601,
            longitude=90.563609,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Narayani Zone",
            state_code="NA",
            latitude=27.3611766,
            longitude=84.8567932,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Nariño",
            state_code="NAR",
            latitude=1.289151,
            longitude=-77.35794,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Narok",
            state_code="33",
            latitude=-1.104111,
            longitude=36.0893406,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Naryn Region",
            state_code="N",
            latitude=41.2943227,
            longitude=75.3412179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kyrgyzstan")][0]),
        ))
        list_of_states.append(State(
            name="Nasarawa",
            state_code="NA",
            latitude=8.4997908,
            longitude=8.1996937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Natore District",
            state_code="44",
            latitude=24.410243,
            longitude=89.0076177,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Naukšēni Municipality",
            state_code="064",
            latitude=57.9295361,
            longitude=25.5119266,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Navarra",
            state_code="NA",
            latitude=42.6953909,
            longitude=-1.6760691,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Navassa Island",
            state_code="UM-76",
            latitude=18.4100689,
            longitude=-75.0114612,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Navassa Island",
            state_code="76",
            latitude=18.4100689,
            longitude=-75.0114612,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States Minor Outlying Islands")][0]),
        ))
        list_of_states.append(State(
            name="Navoiy Region",
            state_code="NW",
            latitude=42.6988575,
            longitude=64.6337685,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Naxxar",
            state_code="38",
            latitude=35.9317518,
            longitude=14.4315746,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Nayala Province",
            state_code="NAY",
            latitude=12.6964558,
            longitude=-3.0175712,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Nayarit",
            state_code="NAY",
            latitude=21.7513844,
            longitude=-104.8454619,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Naypyidaw Union Territory",
            state_code="18",
            latitude=19.9386245,
            longitude=96.1526985,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Nazarje Municipality",
            state_code="083",
            latitude=46.2821741,
            longitude=14.9225629,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Neamț County",
            state_code="NT",
            latitude=46.9758685,
            longitude=26.3818764,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Neath Port Talbot County Borough",
            state_code="NTL",
            latitude=51.5978519,
            longitude=-3.7839668,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Nebbi District",
            state_code="310",
            latitude=2.4409392,
            longitude=31.3541631,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Nebraska",
            state_code="NE",
            latitude=41.4925374,
            longitude=-99.9018131,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Ñeembucú Department",
            state_code="12",
            latitude=-27.0299114,
            longitude=-57.825395,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Neftchala District",
            state_code="NEF",
            latitude=39.3881052,
            longitude=49.2413743,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Negeri Sembilan",
            state_code="05",
            latitude=2.7258058,
            longitude=101.9423782,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Negotino Municipality",
            state_code="54",
            latitude=41.4989985,
            longitude=22.0953297,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Negros Occidental",
            state_code="NEC",
            latitude=10.2925609,
            longitude=123.0246518,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Negros Oriental",
            state_code="NER",
            latitude=9.6282083,
            longitude=122.9888319,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Nelson Region",
            state_code="NSN",
            latitude=-41.2985397,
            longitude=173.2441491,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Nenets Autonomous Okrug",
            state_code="NEN",
            latitude=67.6078337,
            longitude=57.6338331,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Nereta Municipality",
            state_code="065",
            latitude=56.1986655,
            longitude=25.3252969,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Neringa Municipality",
            state_code="28",
            latitude=55.4572403,
            longitude=21.0839005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Netrokona District",
            state_code="41",
            latitude=24.8103284,
            longitude=90.8656415,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Neuchâtel",
            state_code="NE",
            latitude=46.9899874,
            longitude=6.9292732,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Neuquén",
            state_code="Q",
            latitude=-38.94587,
            longitude=-68.0730925,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Nevada",
            state_code="NV",
            latitude=38.8026097,
            longitude=-116.419389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Nevis",
            state_code="N",
            latitude=17.1553558,
            longitude=-62.5796026,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Nevşehir",
            state_code="50",
            latitude=38.6939399,
            longitude=34.6856509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="New Brunswick",
            state_code="NB",
            latitude=46.5653163,
            longitude=-66.4619164,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="New Hampshire",
            state_code="NH",
            latitude=43.1938516,
            longitude=-71.5723953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="New Ireland Province",
            state_code="NIK",
            latitude=-4.2853256,
            longitude=152.9205918,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="New Jersey",
            state_code="NJ",
            latitude=40.0583238,
            longitude=-74.4056612,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="New Mexico",
            state_code="NM",
            latitude=34.5199402,
            longitude=-105.8700901,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="New Providence",
            state_code="NP",
            latitude=40.6984348,
            longitude=-74.4015405,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="New South Wales",
            state_code="NSW",
            latitude=-31.2532183,
            longitude=146.921099,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Australia")][0]),
        ))
        list_of_states.append(State(
            name="New Taipei",
            state_code="NWT",
            latitude=24.9875278,
            longitude=121.3645947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="New Valley",
            state_code="WAD",
            latitude=24.5455638,
            longitude=27.1735316,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="New York",
            state_code="NY",
            latitude=40.7127753,
            longitude=-74.0059728,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Newcastle upon Tyne",
            state_code="NET",
            latitude=54.978252,
            longitude=-1.61778,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Newfoundland and Labrador",
            state_code="NL",
            latitude=53.1355091,
            longitude=-57.6604364,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Newport",
            state_code="NWP",
            latitude=37.5278234,
            longitude=-94.1043876,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Newry and Mourne District Council",
            state_code="NYM",
            latitude=54.1742505,
            longitude=-6.3391992,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Newry, Mourne and Down",
            state_code="NMD",
            latitude=54.2434287,
            longitude=-5.9577959,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Newtownabbey Borough Council",
            state_code="NTA",
            latitude=54.6792422,
            longitude=-5.9591102,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ngamiland",
            state_code="NG",
            latitude=-19.1905321,
            longitude=23.0011989,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Botswana")][0]),
        ))
        list_of_states.append(State(
            name="Ngaraard",
            state_code="214",
            latitude=7.60794,
            longitude=134.6348645,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Ngarchelong",
            state_code="218",
            latitude=7.7105469,
            longitude=134.6301646,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Ngardmau",
            state_code="222",
            latitude=7.5850486,
            longitude=134.5596089,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Ngatpang",
            state_code="224",
            latitude=7.4710994,
            longitude=134.5266466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Ngchesar",
            state_code="226",
            latitude=7.452328,
            longitude=134.5784342,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Ngeremlengui",
            state_code="227",
            latitude=7.5198397,
            longitude=134.5596089,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Nghệ An",
            state_code="22",
            latitude=19.2342489,
            longitude=104.9200365,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Ngiwal",
            state_code="228",
            latitude=7.5614764,
            longitude=134.6160619,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Ngöbe-Buglé Comarca",
            state_code="NB",
            latitude=8.6595833,
            longitude=-81.7787021,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Ngora District",
            state_code="231",
            latitude=1.4908115,
            longitude=33.7517723,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Ngounié Province",
            state_code="4",
            latitude=-1.4930303,
            longitude=10.9807003,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gabon")][0]),
        ))
        list_of_states.append(State(
            name="Ngozi Province",
            state_code="NG",
            latitude=-2.8958243,
            longitude=29.8815203,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Niari Department",
            state_code="9",
            latitude=-3.18427,
            longitude=12.2547919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Niassa Province",
            state_code="A",
            latitude=-12.7826202,
            longitude=36.6093926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Nibok District",
            state_code="12",
            latitude=-0.5196208,
            longitude=166.9189301,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nauru")][0]),
        ))
        list_of_states.append(State(
            name="Nīca Municipality",
            state_code="066",
            latitude=56.3464983,
            longitude=21.065493,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Nichollstown and Berry Islands",
            state_code="NB",
            latitude=25.7236234,
            longitude=-77.8310104,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Nickerie District",
            state_code="NI",
            latitude=5.5855469,
            longitude=-56.8311117,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Suriname")][0]),
        ))
        list_of_states.append(State(
            name="Nicosia District (Lefkoşa)",
            state_code="01",
            latitude=35.1855659,
            longitude=33.3822764,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cyprus")][0]),
        ))
        list_of_states.append(State(
            name="Nidwalden",
            state_code="NW",
            latitude=46.9267016,
            longitude=8.3849982,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Nièvre",
            state_code="58",
            latitude=47.1192164,
            longitude=2.9779713,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Niğde",
            state_code="51",
            latitude=38.0993086,
            longitude=34.6856509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Niger",
            state_code="NI",
            latitude=9.9309224,
            longitude=5.598321,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Niigata Prefecture",
            state_code="15",
            latitude=37.5178386,
            longitude=138.9269794,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Nikšić Municipality",
            state_code="12",
            latitude=42.7997184,
            longitude=18.7600963,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Nilphamari District",
            state_code="46",
            latitude=25.8482798,
            longitude=88.9414134,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Nimba",
            state_code="NI",
            latitude=7.6166667,
            longitude=-8.4166667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Nimruz",
            state_code="NIM",
            latitude=31.0261488,
            longitude=62.4504154,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Nineveh",
            state_code="NI",
            latitude=36.229574,
            longitude=42.2362435,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Ningxia Huizu",
            state_code="NX",
            latitude=37.198731,
            longitude=106.1580937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Ninh Bình",
            state_code="18",
            latitude=20.2506149,
            longitude=105.9744536,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Ninh Thuận",
            state_code="36",
            latitude=11.6738767,
            longitude=108.8629572,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Nippes",
            state_code="NI",
            latitude=18.3990735,
            longitude=-73.4180211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Haiti")][0]),
        ))
        list_of_states.append(State(
            name="Nišava District",
            state_code="20",
            latitude=43.3738902,
            longitude=21.9322331,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Nisporeni District",
            state_code="NI",
            latitude=47.0751349,
            longitude=28.1768155,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Nitra Region",
            state_code="NI",
            latitude=48.0143765,
            longitude=18.5416504,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovakia")][0]),
        ))
        list_of_states.append(State(
            name="Niuas",
            state_code="03",
            latitude=-15.9594,
            longitude=-173.783,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tonga")][0]),
        ))
        list_of_states.append(State(
            name="Niutao Island Council",
            state_code="NIT",
            latitude=-6.1064258,
            longitude=177.3438429,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tuvalu")][0]),
        ))
        list_of_states.append(State(
            name="Nizhny Novgorod Oblast",
            state_code="NIZ",
            latitude=55.7995159,
            longitude=44.0296769,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Njombe",
            state_code="29",
            latitude=-9.2422632,
            longitude=35.1268781,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Nkhata Bay District",
            state_code="NB",
            latitude=-11.7185042,
            longitude=34.3310364,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Nkhotakota District",
            state_code="NK",
            latitude=-12.7541961,
            longitude=34.2421597,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Noakhali District",
            state_code="47",
            latitude=22.8723789,
            longitude=91.0973184,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Nógrád County",
            state_code="NO",
            latitude=47.9041031,
            longitude=19.0498504,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Nong Bua Lam Phu",
            state_code="39",
            latitude=17.2218247,
            longitude=102.4260368,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Nong Khai",
            state_code="43",
            latitude=17.8782803,
            longitude=102.7412638,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Nonthaburi",
            state_code="12",
            latitude=13.8591084,
            longitude=100.5216508,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Noonu Atoll",
            state_code="25",
            latitude=5.8551276,
            longitude=73.323708,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Nord",
            state_code="59",
            latitude=50.5285477,
            longitude=2.6000776,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Nord",
            state_code="ND",
            latitude=43.190526,
            longitude=-89.437921,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Haiti")][0]),
        ))
        list_of_states.append(State(
            name="Nord Region, Burkina Faso",
            state_code="10",
            latitude=13.718252,
            longitude=-2.302446,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Nord-Est",
            state_code="NE",
            latitude=19.4889723,
            longitude=-71.8571331,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Haiti")][0]),
        ))
        list_of_states.append(State(
            name="Nord-Kivu",
            state_code="NK",
            latitude=-0.7917729,
            longitude=29.0459927,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Nord-Ouest",
            state_code="NO",
            latitude=19.8374009,
            longitude=-73.0405277,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Haiti")][0]),
        ))
        list_of_states.append(State(
            name="Nord-Ubangi",
            state_code="NU",
            latitude=3.7878726,
            longitude=21.4752851,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Nordland",
            state_code="18",
            latitude=67.693058,
            longitude=12.7073936,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Norfolk",
            state_code="NFK",
            latitude=36.8507689,
            longitude=-76.2858726,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Normandie",
            state_code="NOR",
            latitude=48.8798704,
            longitude=0.1712529,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Norrbotten County",
            state_code="BD",
            latitude=66.8309216,
            longitude=20.3991966,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Norte de Santander",
            state_code="NSA",
            latitude=7.9462831,
            longitude=-72.8988069,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Norte Province",
            state_code="N",
            latitude=7.8721811,
            longitude=123.8857747,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="North",
            state_code="NO",
            latitude=37.09024,
            longitude=-95.712891,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cameroon")][0]),
        ))
        list_of_states.append(State(
            name="North",
            state_code="NNO",
            latitude=22.49471,
            longitude=114.13812,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="North",
            state_code="AS",
            latitude=34.4380625,
            longitude=35.8308233,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lebanon")][0]),
        ))
        list_of_states.append(State(
            name="North Abaco",
            state_code="NO",
            latitude=26.7871697,
            longitude=-77.4357739,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="North Andros",
            state_code="NS",
            latitude=24.7063805,
            longitude=-78.0195387,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="North Ayrshire",
            state_code="NAY",
            latitude=55.6416731,
            longitude=-4.75946,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="North Bačka District",
            state_code="01",
            latitude=45.9803394,
            longitude=19.5907001,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="North Banat District",
            state_code="03",
            latitude=45.906839,
            longitude=19.9993417,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="North Bank Division",
            state_code="N",
            latitude=13.5285436,
            longitude=-16.0169971,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gambia The")][0]),
        ))
        list_of_states.append(State(
            name="North Brabant",
            state_code="NB",
            latitude=51.4826537,
            longitude=5.2321687,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="North Caribbean Coast",
            state_code="AN",
            latitude=13.8394456,
            longitude=-83.9320806,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="North Carolina",
            state_code="NC",
            latitude=35.7595731,
            longitude=-79.0192997,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="North Central Province",
            state_code="NC",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="North Central Province",
            state_code="7",
            latitude=8.1995638,
            longitude=80.6326916,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="North Chungcheong Province",
            state_code="43",
            latitude=36.8,
            longitude=127.7,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="North Dakota",
            state_code="ND",
            latitude=47.5514926,
            longitude=-101.0020119,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="North Darfur",
            state_code="DN",
            latitude=15.7661969,
            longitude=24.9042208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="North Denmark Region",
            state_code="81",
            latitude=56.8307416,
            longitude=9.4930527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Denmark")][0]),
        ))
        list_of_states.append(State(
            name="North Down Borough Council",
            state_code="NDN",
            latitude=54.6536297,
            longitude=-5.6724925,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="North East",
            state_code="NE",
            latitude=10.516667,
            longitude=-0.366667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="North East",
            state_code="02",
            latitude=1.3824,
            longitude=103.8972,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Singapore")][0]),
        ))
        list_of_states.append(State(
            name="North East Lincolnshire",
            state_code="NEL",
            latitude=53.5668201,
            longitude=-0.0815066,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="North Eleuthera",
            state_code="NE",
            latitude=25.4647517,
            longitude=-76.675922,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="North Gaza",
            state_code="NGZ",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="North Gyeongsang Province",
            state_code="47",
            latitude=36.4919,
            longitude=128.8889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="North Hamgyong Province",
            state_code="09",
            latitude=41.8148758,
            longitude=129.4581955,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="North Holland",
            state_code="NH",
            latitude=52.5205869,
            longitude=4.788474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="North Hwanghae Province",
            state_code="06",
            latitude=38.3786085,
            longitude=126.4364363,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="North Jeolla Province",
            state_code="45",
            latitude=35.7175,
            longitude=127.153,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="North Karelia",
            state_code="13",
            latitude=62.8062078,
            longitude=30.1553887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="North Kazakhstan Region",
            state_code="SEV",
            latitude=54.1622066,
            longitude=69.9387071,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="North Khorasan",
            state_code="28",
            latitude=37.4710353,
            longitude=57.1013188,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="North Kordofan",
            state_code="KN",
            latitude=13.8306441,
            longitude=29.4179324,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="North Lanarkshire",
            state_code="NLK",
            latitude=55.8662432,
            longitude=-3.9613144,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="North Lincolnshire",
            state_code="NLN",
            latitude=53.6055592,
            longitude=-0.5596582,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="North Province",
            state_code="NO",
            latitude=8.8855027,
            longitude=80.2767327,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="North Province",
            state_code="02",
            latitude=-22.2758,
            longitude=166.458,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Caledonia")][0]),
        ))
        list_of_states.append(State(
            name="North Pyongan Province",
            state_code="03",
            latitude=39.9255618,
            longitude=125.3928025,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="North Rhine-Westphalia",
            state_code="NW",
            latitude=51.4332367,
            longitude=7.6615938,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="North Sinai",
            state_code="SIN",
            latitude=30.282365,
            longitude=33.617577,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="North Somerset",
            state_code="NSM",
            latitude=51.3879028,
            longitude=-2.7781091,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="North Tyneside",
            state_code="NTY",
            latitude=55.0182399,
            longitude=-1.4858436,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="North West",
            state_code="03",
            latitude=1.418,
            longitude=103.8275,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Singapore")][0]),
        ))
        list_of_states.append(State(
            name="North West",
            state_code="NW",
            latitude=32.758852,
            longitude=-97.328806,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Africa")][0]),
        ))
        list_of_states.append(State(
            name="North Western Province",
            state_code="6",
            latitude=7.7584091,
            longitude=80.1875065,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="North Yorkshire",
            state_code="NYK",
            latitude=53.9915028,
            longitude=-1.5412015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="North-East District",
            state_code="NE",
            latitude=37.5884461,
            longitude=-94.6863782,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Botswana")][0]),
        ))
        list_of_states.append(State(
            name="North-West District",
            state_code="NW",
            latitude=39.3446307,
            longitude=-76.6854283,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Botswana")][0]),
        ))
        list_of_states.append(State(
            name="Northamptonshire",
            state_code="NTH",
            latitude=52.2729944,
            longitude=-0.8755515,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Northeastern Region",
            state_code="6",
            latitude=43.2994285,
            longitude=-74.2179326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iceland")][0]),
        ))
        list_of_states.append(State(
            name="Northern",
            state_code="17",
            latitude=26.1551914,
            longitude=50.4825173,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bahrain")][0]),
        ))
        list_of_states.append(State(
            name="Northern",
            state_code="NP",
            latitude=9.5,
            longitude=-1,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Northern",
            state_code="NO",
            latitude=38.063817,
            longitude=-84.4628648,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Northern Bahr el Ghazal",
            state_code="BN",
            latitude=8.5360449,
            longitude=26.7967849,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Northern Borders",
            state_code="08",
            latitude=30.0799162,
            longitude=42.8637875,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Northern Cape",
            state_code="NC",
            latitude=-29.0466808,
            longitude=21.8568586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Africa")][0]),
        ))
        list_of_states.append(State(
            name="Northern District",
            state_code="Z",
            latitude=36.1511864,
            longitude=-95.9951763,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Israel")][0]),
        ))
        list_of_states.append(State(
            name="Northern Division",
            state_code="N",
            latitude=32.8768766,
            longitude=-117.2156345,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Northern Ireland",
            state_code="NIR",
            latitude=54.7877149,
            longitude=-6.4923145,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Northern Mariana Islands",
            state_code="MP",
            latitude=15.0979,
            longitude=145.6739,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Northern Mindanao",
            state_code="10",
            latitude=8.0201635,
            longitude=124.6856509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Northern Ostrobothnia",
            state_code="14",
            latitude=65.279493,
            longitude=26.2890417,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Northern Province",
            state_code="03",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Rwanda")][0]),
        ))
        list_of_states.append(State(
            name="Northern Province",
            state_code="N",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sierra Leone")][0]),
        ))
        list_of_states.append(State(
            name="Northern Province",
            state_code="4",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Northern Province",
            state_code="05",
            latitude=8.8855027,
            longitude=80.2767327,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zambia")][0]),
        ))
        list_of_states.append(State(
            name="Northern Red Sea Region",
            state_code="SK",
            latitude=16.2583997,
            longitude=38.8205454,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Eritrea")][0]),
        ))
        list_of_states.append(State(
            name="Northern Region",
            state_code="N",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Northern Region",
            state_code="N",
            latitude=9.5439269,
            longitude=-0.9056623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Northern Samar",
            state_code="NSA",
            latitude=12.3613199,
            longitude=124.7740793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Northern Savonia",
            state_code="15",
            latitude=63.08448,
            longitude=27.0253504,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Northern Territory",
            state_code="NT",
            latitude=-19.4914108,
            longitude=132.5509603,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Australia")][0]),
        ))
        list_of_states.append(State(
            name="Northland Region",
            state_code="NTL",
            latitude=-35.4136172,
            longitude=173.9320806,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Northumberland",
            state_code="NBL",
            latitude=55.2082542,
            longitude=-2.0784138,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Northwest",
            state_code="NW",
            latitude=36.3711857,
            longitude=-94.1934606,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cameroon")][0]),
        ))
        list_of_states.append(State(
            name="Northwest Territories",
            state_code="NT",
            latitude=64.8255441,
            longitude=-124.8457334,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Northwestern Province",
            state_code="06",
            latitude=-13.0050258,
            longitude=24.9042208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zambia")][0]),
        ))
        list_of_states.append(State(
            name="Northwestern Region",
            state_code="5",
            latitude=41.9133932,
            longitude=-73.0471688,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iceland")][0]),
        ))
        list_of_states.append(State(
            name="Nottinghamshire",
            state_code="NTT",
            latitude=53.100319,
            longitude=-0.9936306,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Nouaceur",
            state_code="NOU",
            latitude=33.3670393,
            longitude=-7.5732537,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Nouakchott-Nord",
            state_code="14",
            latitude=18.1130205,
            longitude=-15.8994956,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Nouakchott-Ouest",
            state_code="13",
            latitude=18.1511357,
            longitude=-15.993491,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Nouakchott-Sud",
            state_code="15",
            latitude=17.9709288,
            longitude=-15.9464874,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Noumbiel Province",
            state_code="NOU",
            latitude=9.8440946,
            longitude=-2.9775558,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Nouvelle-Aquitaine",
            state_code="NAQ",
            latitude=45.7087182,
            longitude=0.626891,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Nova Gorica City Municipality",
            state_code="084",
            latitude=45.976276,
            longitude=13.7308881,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Nova Scotia",
            state_code="NS",
            latitude=44.6819866,
            longitude=-63.744311,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Novaci Municipality",
            state_code="55",
            latitude=41.0442661,
            longitude=21.4588894,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Novara",
            state_code="NO",
            latitude=45.5485133,
            longitude=8.5150793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Novgorod Oblast",
            state_code="NGR",
            latitude=58.2427552,
            longitude=32.566519,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Novo Selo Municipality",
            state_code="56",
            latitude=41.432558,
            longitude=22.8820489,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Novosibirsk",
            state_code="NVS",
            latitude=54.9832693,
            longitude=82.8963831,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Nový Jičín",
            state_code="804",
            latitude=49.5943251,
            longitude=18.0135356,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Nsanje District",
            state_code="NS",
            latitude=-16.7288202,
            longitude=35.1708741,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Ntcheu District",
            state_code="NU",
            latitude=-14.9037538,
            longitude=34.7740793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Ntchisi District",
            state_code="NI",
            latitude=-13.2841992,
            longitude=33.8857747,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Ntoroko District",
            state_code="424",
            latitude=1.0788178,
            longitude=30.3896651,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Ntungamo District",
            state_code="411",
            latitude=-0.9807341,
            longitude=30.2512728,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Ñuble",
            state_code="NB",
            latitude=-36.7225743,
            longitude=-71.7622481,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Nueva Ecija",
            state_code="NUE",
            latitude=15.578375,
            longitude=121.1112615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Nueva Esparta",
            state_code="O",
            latitude=10.9970723,
            longitude=-63.9113296,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Nueva Segovia",
            state_code="NS",
            latitude=13.7657061,
            longitude=-86.5370039,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Nueva Vizcaya",
            state_code="NUV",
            latitude=16.3301107,
            longitude=121.1710389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Nuevo León",
            state_code="NLE",
            latitude=25.592172,
            longitude=-99.9961947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Nugal",
            state_code="NU",
            latitude=43.2793861,
            longitude=17.0339205,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Nui",
            state_code="NUI",
            latitude=-7.2388768,
            longitude=177.1485232,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tuvalu")][0]),
        ))
        list_of_states.append(State(
            name="Nukufetau",
            state_code="NKF",
            latitude=-8,
            longitude=178.5,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tuvalu")][0]),
        ))
        list_of_states.append(State(
            name="Nukulaelae",
            state_code="NKL",
            latitude=-9.381111,
            longitude=179.852222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tuvalu")][0]),
        ))
        list_of_states.append(State(
            name="Nunavut",
            state_code="NU",
            latitude=70.2997711,
            longitude=-83.107577,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Nuoro",
            state_code="NU",
            latitude=40.3286904,
            longitude=9.456155,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Nuqat al Khams",
            state_code="NQ",
            latitude=32.6914909,
            longitude=11.8891721,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Nur-Sultan",
            state_code="AST",
            latitude=51.1605227,
            longitude=71.4703558,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="Nuristan",
            state_code="NUR",
            latitude=35.3250223,
            longitude=70.9071236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Nusa Tenggara Barat",
            state_code="NB",
            latitude=-8.6529334,
            longitude=117.3616476,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Nusa Tenggara Timur",
            state_code="NT",
            latitude=-8.6573819,
            longitude=121.0793705,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Nuwara Eliya District",
            state_code="23",
            latitude=6.9606532,
            longitude=80.7692758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Nwoya District",
            state_code="328",
            latitude=2.562444,
            longitude=31.9017954,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Nyamira",
            state_code="34",
            latitude=-0.5669405,
            longitude=34.9341234,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Nyandarua",
            state_code="35",
            latitude=-0.1803855,
            longitude=36.5229641,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Nyanga Province",
            state_code="5",
            latitude=-2.8821033,
            longitude=11.1617356,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gabon")][0]),
        ))
        list_of_states.append(State(
            name="Nyeri",
            state_code="36",
            latitude=-0.4196915,
            longitude=37.0400339,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Nyíregyháza",
            state_code="NY",
            latitude=47.9495324,
            longitude=21.7244053,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Nymburk",
            state_code="208",
            latitude=50.1855816,
            longitude=15.0436604,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Nzérékoré Prefecture",
            state_code="NZ",
            latitude=7.7478359,
            longitude=-8.8252502,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Nzérékoré Region",
            state_code="N",
            latitude=8.038587,
            longitude=-8.8362755,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Oaxaca",
            state_code="OAX",
            latitude=17.0731842,
            longitude=-96.7265889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Obock Region",
            state_code="OB",
            latitude=12.3895691,
            longitude=43.0194897,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Djibouti")][0]),
        ))
        list_of_states.append(State(
            name="Obwalden",
            state_code="OW",
            latitude=46.877858,
            longitude=8.251249,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Occidental Mindoro",
            state_code="MDC",
            latitude=13.1024111,
            longitude=120.7651284,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Occitanie",
            state_code="OCC",
            latitude=43.8927232,
            longitude=3.2827625,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Ocnița District",
            state_code="OC",
            latitude=48.4110435,
            longitude=27.4768092,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Ocotepeque Department",
            state_code="OC",
            latitude=14.5170347,
            longitude=-89.0561532,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Oddar Meanchey",
            state_code="22",
            latitude=14.1609738,
            longitude=103.8216261,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Odeska oblast",
            state_code="51",
            latitude=46.484583,
            longitude=30.7326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (13/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
