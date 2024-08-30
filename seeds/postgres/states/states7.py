"""
States Seed #7

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
            name="Goranboy District",
            state_code="GOR",
            latitude=40.5380506,
            longitude=46.5990891,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Gorenja Vas–Poljane Municipality",
            state_code="027",
            latitude=46.1116582,
            longitude=14.1149348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Gorgol",
            state_code="04",
            latitude=15.9717357,
            longitude=-12.6216211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Gorišnica Municipality",
            state_code="028",
            latitude=46.4120271,
            longitude=16.0133089,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Gorizia",
            state_code="GO",
            latitude=45.9053899,
            longitude=13.5163725,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Gorj County",
            state_code="GJ",
            latitude=44.9485595,
            longitude=23.2427079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Gorje Municipality",
            state_code="207",
            latitude=46.3802458,
            longitude=14.0685339,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Gornja Radgona Municipality",
            state_code="029",
            latitude=46.6767099,
            longitude=15.9910847,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Gornji Grad Municipality",
            state_code="030",
            latitude=46.2961712,
            longitude=14.8062347,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Gornji Petrovci Municipality",
            state_code="031",
            latitude=46.8037128,
            longitude=16.2191379,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Gorno-Badakhshan Autonomous Province",
            state_code="GB",
            latitude=38.412732,
            longitude=73.087749,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tajikistan")][0]),
        ))
        list_of_states.append(State(
            name="Gorontalo",
            state_code="GO",
            latitude=0.5435442,
            longitude=123.0567693,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Gostivar Municipality",
            state_code="19",
            latitude=41.8025541,
            longitude=20.9089378,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Gotland County",
            state_code="I",
            latitude=57.4684121,
            longitude=18.4867447,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Gourma Province",
            state_code="GOU",
            latitude=12.1624473,
            longitude=0.6773046,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Governor's Harbour",
            state_code="GH",
            latitude=25.1948096,
            longitude=-76.2439622,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Govi-Altai Province",
            state_code="065",
            latitude=45.4511227,
            longitude=95.8505766,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Govisümber Province",
            state_code="064",
            latitude=46.4762754,
            longitude=108.5570627,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Goychay",
            state_code="GOY",
            latitude=40.6236168,
            longitude=47.7403034,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Goygol District",
            state_code="GYG",
            latitude=40.5595378,
            longitude=46.3314953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Gracias a Dios Department",
            state_code="GD",
            latitude=15.341806,
            longitude=-84.6060449,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Grad Municipality",
            state_code="158",
            latitude=46.808732,
            longitude=16.109206,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Gradsko Municipality",
            state_code="20",
            latitude=41.5991608,
            longitude=21.8807064,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Gramsh District",
            state_code="GR",
            latitude=40.8669873,
            longitude=20.1849323,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Granada",
            state_code="GR",
            latitude=11.9344073,
            longitude=-85.9560005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Granada",
            state_code="GR",
            latitude=37.1809411,
            longitude=-3.626291,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Grand Bassa County",
            state_code="GB",
            latitude=6.2308452,
            longitude=-9.8124935,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Grand Cape Mount County",
            state_code="CM",
            latitude=7.0467758,
            longitude=-11.0711758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Grand Cay",
            state_code="GC",
            latitude=27.2162615,
            longitude=-78.3230559,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Grand Gedeh County",
            state_code="GG",
            latitude=5.9222078,
            longitude=-8.2212979,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Grand Kru County",
            state_code="GK",
            latitude=4.7613862,
            longitude=-8.2212979,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Grand Port",
            state_code="GP",
            latitude=-20.3851546,
            longitude=57.6665742,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Grand'Anse",
            state_code="GA",
            latitude=12.0166667,
            longitude=-61.7666667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Haiti")][0]),
        ))
        list_of_states.append(State(
            name="Grand'Anse Mahé",
            state_code="13",
            latitude=-4.677392,
            longitude=55.463777,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Grand'Anse Praslin",
            state_code="14",
            latitude=-4.3176219,
            longitude=55.7078363,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Grand-Est",
            state_code="GES",
            latitude=48.699803,
            longitude=6.1878074,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Grande Comore",
            state_code="G",
            latitude=-11.7167338,
            longitude=43.3680788,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Comoros")][0]),
        ))
        list_of_states.append(State(
            name="Granma Province",
            state_code="12",
            latitude=20.3844902,
            longitude=-76.6412712,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Graubünden",
            state_code="GR",
            latitude=46.6569871,
            longitude=9.5780257,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Greater Accra",
            state_code="AA",
            latitude=5.8142836,
            longitude=0.0746767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Greater Poland Voivodeship",
            state_code="WP",
            latitude=52.279986,
            longitude=17.3522939,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Greater Skopje",
            state_code="85",
            latitude=41.9981294,
            longitude=21.4254355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Green Turtle Cay",
            state_code="GT",
            latitude=26.7747107,
            longitude=-77.3295708,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Grenadines Parish",
            state_code="06",
            latitude=13.0122965,
            longitude=-61.2277301,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Vincent and the Grenadines")][0]),
        ))
        list_of_states.append(State(
            name="Grevena Prefecture",
            state_code="51",
            latitude=40.0837626,
            longitude=21.4273299,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Grevenmacher District",
            state_code="G",
            latitude=49.680851,
            longitude=6.4407524,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Grobiņa Municipality",
            state_code="032",
            latitude=56.539632,
            longitude=21.166892,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Grodno Region",
            state_code="HR",
            latitude=53.6599945,
            longitude=25.3448571,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belarus")][0]),
        ))
        list_of_states.append(State(
            name="Groningen",
            state_code="GR",
            latitude=53.2193835,
            longitude=6.5665017,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Gros Islet Quarter",
            state_code="06",
            latitude=14.0843578,
            longitude=-60.9452794,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Grosseto",
            state_code="GR",
            latitude=42.8518007,
            longitude=11.2523792,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Grosuplje Municipality",
            state_code="032",
            latitude=45.9557645,
            longitude=14.658899,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Guadalajara",
            state_code="GU",
            latitude=40.6322214,
            longitude=-3.190682,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Guadalcanal Province",
            state_code="GU",
            latitude=-9.5773284,
            longitude=160.1455805,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Solomon Islands")][0]),
        ))
        list_of_states.append(State(
            name="Guadeloupe",
            state_code="971",
            latitude=16.265,
            longitude=-61.551,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Guainía",
            state_code="GUA",
            latitude=2.585393,
            longitude=-68.5247149,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Guairá Department",
            state_code="4",
            latitude=-25.8810932,
            longitude=-56.2929381,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Guam",
            state_code="GU",
            latitude=13.444304,
            longitude=144.793731,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Guanacaste Province",
            state_code="G",
            latitude=10.6267399,
            longitude=-85.4436706,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Costa Rica")][0]),
        ))
        list_of_states.append(State(
            name="Guanajuato",
            state_code="GUA",
            latitude=21.0190145,
            longitude=-101.2573586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Guangdong",
            state_code="GD",
            latitude=23.3790333,
            longitude=113.7632828,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Guangxi Zhuang",
            state_code="GX",
            latitude=23.7247599,
            longitude=108.8076195,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Guánica",
            state_code="055",
            latitude=17.9725145,
            longitude=-66.9086264,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Guantánamo Province",
            state_code="14",
            latitude=20.1455917,
            longitude=-74.8741045,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Guarda",
            state_code="09",
            latitude=40.5385972,
            longitude=-7.2675772,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Guárico",
            state_code="J",
            latitude=8.7489309,
            longitude=-66.2367172,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Guatemala Department",
            state_code="GU",
            latitude=14.5649401,
            longitude=-90.5257823,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Guaviare",
            state_code="GUV",
            latitude=2.043924,
            longitude=-72.331113,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Guayama",
            state_code="057",
            latitude=17.9841328,
            longitude=-66.1137767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Guayanilla",
            state_code="059",
            latitude=18.0191314,
            longitude=-66.791842,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Guayas",
            state_code="G",
            latitude=-1.9574839,
            longitude=-79.9192702,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Guaynabo",
            state_code="061",
            latitude=18.3612954,
            longitude=-66.1102957,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Guaynabo",
            state_code="GN",
            latitude=18.36666667,
            longitude=-66.1,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Gudja",
            state_code="11",
            latitude=35.8469803,
            longitude=14.502904,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Guéckédou Prefecture",
            state_code="GU",
            latitude=8.5649688,
            longitude=-10.1311163,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Guelma",
            state_code="24",
            latitude=36.4627444,
            longitude=7.4330833,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Guelmim",
            state_code="GUE",
            latitude=28.9883659,
            longitude=-10.0527498,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Guelmim-Oued Noun (EH-partial)",
            state_code="10",
            latitude=28.4844281,
            longitude=-10.0807298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Guéra",
            state_code="GR",
            latitude=11.1219015,
            longitude=18.4276047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Guercif",
            state_code="GUF",
            latitude=34.2345036,
            longitude=-3.3813005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Guerrero",
            state_code="GRO",
            latitude=17.4391926,
            longitude=-99.5450974,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Guidimaka",
            state_code="10",
            latitude=15.2557331,
            longitude=-12.2547919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Guimaras",
            state_code="GUI",
            latitude=10.5928661,
            longitude=122.6325081,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Guizhou",
            state_code="GZ",
            latitude=26.8429645,
            longitude=107.2902839,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Gujarat",
            state_code="GJ",
            latitude=22.258652,
            longitude=71.1923805,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Gulbene Municipality",
            state_code="033",
            latitude=57.2155645,
            longitude=26.6452955,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Gulf",
            state_code="GPK",
            latitude=37.0548315,
            longitude=-94.4370419,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Gulu District",
            state_code="304",
            latitude=2.8185776,
            longitude=32.4467238,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Gümüşhane",
            state_code="29",
            latitude=40.2803673,
            longitude=39.3143253,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Guna Yala",
            state_code="KY",
            latitude=9.2344395,
            longitude=-78.192625,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Gunma Prefecture",
            state_code="10",
            latitude=36.5605388,
            longitude=138.8799972,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Gurabo",
            state_code="063",
            latitude=18.2543987,
            longitude=-65.9729421,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Guria",
            state_code="GU",
            latitude=41.9442736,
            longitude=42.0458091,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Gusinje Municipality",
            state_code="22",
            latitude=42.5563455,
            longitude=19.8306051,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Gwangju",
            state_code="29",
            latitude=35.1595454,
            longitude=126.8526012,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Gwynedd",
            state_code="GWN",
            latitude=52.9277266,
            longitude=-4.1334836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Gyeonggi Province",
            state_code="41",
            latitude=37.4138,
            longitude=127.5183,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Győr",
            state_code="GY",
            latitude=47.6874569,
            longitude=17.6503974,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Győr-Moson-Sopron County",
            state_code="GS",
            latitude=47.6509285,
            longitude=17.2505883,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Gżira",
            state_code="12",
            latitude=35.905897,
            longitude=14.4953338,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Għajnsielem",
            state_code="13",
            latitude=36.0247966,
            longitude=14.2802961,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Għarb",
            state_code="14",
            latitude=36.068909,
            longitude=14.2018098,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Għargħur",
            state_code="15",
            latitude=35.9220569,
            longitude=14.4563176,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Għasri",
            state_code="16",
            latitude=36.0668075,
            longitude=14.2192475,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Għaxaq",
            state_code="17",
            latitude=35.8440359,
            longitude=14.516009,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Gədəbəy",
            state_code="GAD",
            latitude=40.5699639,
            longitude=45.8106883,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Hà Giang",
            state_code="03",
            latitude=22.8025588,
            longitude=104.9784494,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Hà Nam",
            state_code="63",
            latitude=20.5835196,
            longitude=105.92299,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Hà Nội",
            state_code="HN",
            latitude=21.0277644,
            longitude=105.8341598,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Hà Tĩnh",
            state_code="23",
            latitude=18.3559537,
            longitude=105.8877494,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Ha'il",
            state_code="06",
            latitude=27.7076143,
            longitude=41.9196471,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Haa Alif Atoll",
            state_code="07",
            latitude=6.9903488,
            longitude=72.9460566,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Haa Dhaalu Atoll",
            state_code="23",
            latitude=6.5782717,
            longitude=72.9460566,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Haa District",
            state_code="13",
            latitude=27.2651669,
            longitude=89.1705998,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Habiganj District",
            state_code="20",
            latitude=24.4771236,
            longitude=91.4506565,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Hadhramaut",
            state_code="HD",
            latitude=16.9304135,
            longitude=49.3653149,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Hadjer-Lamis",
            state_code="HL",
            latitude=12.4577273,
            longitude=16.7234639,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Hải Dương",
            state_code="61",
            latitude=20.9373413,
            longitude=106.3145542,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Hải Phòng",
            state_code="HP",
            latitude=20.8449115,
            longitude=106.6880841,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Haifa District",
            state_code="HA",
            latitude=32.4814111,
            longitude=34.994751,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Israel")][0]),
        ))
        list_of_states.append(State(
            name="Hainan",
            state_code="HI",
            latitude=19.5663947,
            longitude=109.949686,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Hainaut",
            state_code="WHT",
            latitude=50.5257076,
            longitude=4.0621017,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="Hajdina Municipality",
            state_code="159",
            latitude=46.4185014,
            longitude=15.8244722,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Hajdú-Bihar County",
            state_code="HB",
            latitude=47.4688355,
            longitude=21.5453227,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Hajigabul District",
            state_code="HAC",
            latitude=40.039377,
            longitude=48.9202533,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Hajjah",
            state_code="HJ",
            latitude=16.1180631,
            longitude=43.329466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Hakkâri",
            state_code="30",
            latitude=37.4459319,
            longitude=43.7449841,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Halland County",
            state_code="N",
            latitude=56.8966805,
            longitude=12.8033993,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Halton",
            state_code="HAL",
            latitude=43.5325372,
            longitude=-79.8744836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Hama",
            state_code="HM",
            latitude=35.1887865,
            longitude=37.2115829,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Hamadan",
            state_code="13",
            latitude=34.9193607,
            longitude=47.4832925,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Hambantota District",
            state_code="33",
            latitude=6.1535816,
            longitude=81.127149,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Hamburg",
            state_code="HH",
            latitude=53.5510846,
            longitude=9.9936819,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Hamilton",
            state_code="HA",
            latitude=32.3449432,
            longitude=-64.72365,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bermuda")][0]),
        ))
        list_of_states.append(State(
            name="Hampshire",
            state_code="HAM",
            latitude=51.0576948,
            longitude=-1.3080629,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Hanover Parish",
            state_code="09",
            latitude=18.4097707,
            longitude=-78.133638,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Harare Province",
            state_code="HA",
            latitude=-17.8216288,
            longitude=31.0492259,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zimbabwe")][0]),
        ))
        list_of_states.append(State(
            name="Harari Region",
            state_code="HA",
            latitude=9.314866,
            longitude=42.1967716,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ethiopia")][0]),
        ))
        list_of_states.append(State(
            name="Harbour Island",
            state_code="HI",
            latitude=25.50011,
            longitude=-76.6340511,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Hardap Region",
            state_code="HA",
            latitude=-24.2310134,
            longitude=17.668887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Harghita County",
            state_code="HR",
            latitude=46.4928507,
            longitude=25.6456696,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Harju County",
            state_code="37",
            latitude=59.3334239,
            longitude=25.2466974,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Hartlepool",
            state_code="HPL",
            latitude=54.691745,
            longitude=-1.212926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Haryana",
            state_code="HR",
            latitude=29.0587757,
            longitude=76.085601,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Has District",
            state_code="HA",
            latitude=42.7901336,
            longitude=-83.6122012,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Haskovo Province",
            state_code="26",
            latitude=41.9344178,
            longitude=25.5554672,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Hatay",
            state_code="31",
            latitude=36.4018488,
            longitude=36.3498097,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Hatillo",
            state_code="065",
            latitude=18.4284642,
            longitude=-66.7875321,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Hato Mayor Province",
            state_code="30",
            latitude=18.7635799,
            longitude=-69.2557637,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Hatohobei",
            state_code="050",
            latitude=3.0070658,
            longitude=131.1237781,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Hậu Giang",
            state_code="73",
            latitude=9.757898,
            longitude=105.6412527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Haut-Katanga",
            state_code="HK",
            latitude=-10.4102075,
            longitude=27.5495846,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Haut-Lomami",
            state_code="HL",
            latitude=-7.7052752,
            longitude=24.9042208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Haut-Mbomou Prefecture",
            state_code="HM",
            latitude=6.2537134,
            longitude=25.4733554,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Haut-Ogooué Province",
            state_code="2",
            latitude=-1.4762544,
            longitude=13.914399,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gabon")][0]),
        ))
        list_of_states.append(State(
            name="Haut-Rhin",
            state_code="68",
            latitude=47.8653774,
            longitude=6.6711381,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Haut-Sassandra",
            state_code="02",
            latitude=6.8757848,
            longitude=-6.5783387,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Haut-Uélé",
            state_code="HU",
            latitude=3.5845154,
            longitude=28.299435,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Haute-Corse",
            state_code="2B",
            latitude=42.4295866,
            longitude=8.5062561,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Haute-Garonne",
            state_code="31",
            latitude=43.3050555,
            longitude=0.6845515,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Haute-Kotto Prefecture",
            state_code="HK",
            latitude=7.7964379,
            longitude=23.3823545,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Haute-Loire",
            state_code="43",
            latitude=45.0853806,
            longitude=3.2260707,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Haute-Marne",
            state_code="52",
            latitude=48.1324821,
            longitude=4.6983499,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Haute-Saône",
            state_code="70",
            latitude=47.6378996,
            longitude=5.5355055,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Haute-Savoie",
            state_code="74",
            latitude=46.0445277,
            longitude=5.864138,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Haute-Vienne",
            state_code="87",
            latitude=45.9186878,
            longitude=0.7097206,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Hautes-Alpes",
            state_code="05",
            latitude=44.6562682,
            longitude=5.6873211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Hautes-Pyrénées",
            state_code="65",
            latitude=43.1429462,
            longitude=-0.4009736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Hauts-Bassins Region",
            state_code="09",
            latitude=11.4942003,
            longitude=-4.2333355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Hauts-de-France",
            state_code="HDF",
            latitude=50.4801153,
            longitude=2.7937265,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Hauts-de-Seine",
            state_code="92",
            latitude=48.8403008,
            longitude=2.1012559,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Havana Province",
            state_code="03",
            latitude=23.0540698,
            longitude=-82.345189,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Havlíčkův Brod",
            state_code="631",
            latitude=49.6043364,
            longitude=15.5796552,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Hawaii",
            state_code="HI",
            latitude=19.8967662,
            longitude=-155.5827818,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Hawalli",
            state_code="HA",
            latitude=29.3056716,
            longitude=48.0307613,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kuwait")][0]),
        ))
        list_of_states.append(State(
            name="Hawke's Bay Region",
            state_code="HKB",
            latitude=-39.6016597,
            longitude=176.5804473,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Haʻapai",
            state_code="02",
            latitude=-19.75,
            longitude=-174.366667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tonga")][0]),
        ))
        list_of_states.append(State(
            name="Hebei",
            state_code="HE",
            latitude=37.8956594,
            longitude=114.9042208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Hebron",
            state_code="HBN",
            latitude=31.5326001,
            longitude=35.0639475,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Heilongjiang",
            state_code="HL",
            latitude=47.1216472,
            longitude=128.738231,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Hela",
            state_code="HLA",
            latitude=42.3329516,
            longitude=-83.0482618,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Helmand",
            state_code="HEL",
            latitude=39.2989361,
            longitude=-76.6160472,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Henan",
            state_code="HA",
            latitude=34.2904302,
            longitude=113.3823545,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Herat",
            state_code="HER",
            latitude=34.352865,
            longitude=62.2040287,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Hérault",
            state_code="34",
            latitude=43.591112,
            longitude=2.8066108,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Heredia Province",
            state_code="H",
            latitude=10.473523,
            longitude=-84.0167423,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Costa Rica")][0]),
        ))
        list_of_states.append(State(
            name="Herefordshire",
            state_code="HEF",
            latitude=52.0765164,
            longitude=-2.6544182,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Hermanas Mirabal Province",
            state_code="19",
            latitude=19.3747559,
            longitude=-70.3513235,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Herrera Province",
            state_code="6",
            latitude=7.7704282,
            longitude=-80.7214417,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Hertfordshire",
            state_code="HRT",
            latitude=51.8097823,
            longitude=-0.2376744,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Herzegovina-Neretva Canton",
            state_code="07",
            latitude=43.5265159,
            longitude=17.763621,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Hesse",
            state_code="HE",
            latitude=50.6520515,
            longitude=9.1624376,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Heves County",
            state_code="HE",
            latitude=47.8057617,
            longitude=20.2038559,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Hhohho District",
            state_code="HH",
            latitude=-26.1365662,
            longitude=31.3541631,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Eswatini")][0]),
        ))
        list_of_states.append(State(
            name="Hidalgo",
            state_code="HID",
            latitude=26.1003547,
            longitude=-98.2630684,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="High Rock",
            state_code="HR",
            latitude=46.6843415,
            longitude=-121.9017461,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Highland",
            state_code="HLD",
            latitude=36.2967508,
            longitude=-95.8380366,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Hiiu County",
            state_code="39",
            latitude=58.9239553,
            longitude=22.5919468,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Himachal Pradesh",
            state_code="HP",
            latitude=31.1048294,
            longitude=77.1733901,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Hîncești District",
            state_code="HI",
            latitude=46.8281147,
            longitude=28.5850889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Hiran",
            state_code="HI",
            latitude=4.321015,
            longitude=45.2993862,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Hiroshima Prefecture",
            state_code="34",
            latitude=34.8823408,
            longitude=133.0194897,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Hồ Chí Minh",
            state_code="SG",
            latitude=10.8230989,
            longitude=106.6296638,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Hòa Bình",
            state_code="14",
            latitude=20.6861265,
            longitude=105.3131185,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Hoče–Slivnica Municipality",
            state_code="160",
            latitude=46.477858,
            longitude=15.6476005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Hodh Ech Chargui",
            state_code="01",
            latitude=18.6737026,
            longitude=-7.092877,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Hodh El Gharbi",
            state_code="02",
            latitude=16.6912149,
            longitude=-9.5450974,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Hódmezővásárhely",
            state_code="HV",
            latitude=46.4181262,
            longitude=20.3300315,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Hodonín",
            state_code="645",
            latitude=48.8529391,
            longitude=17.1260025,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Hodoš Municipality",
            state_code="161",
            latitude=46.8314134,
            longitude=16.321068,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Hokkaidō Prefecture",
            state_code="01",
            latitude=43.2203266,
            longitude=142.8634737,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Holguín Province",
            state_code="11",
            latitude=20.7837893,
            longitude=-75.8069082,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Homa Bay",
            state_code="08",
            latitude=-0.6220655,
            longitude=34.3310364,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Homs",
            state_code="HI",
            latitude=34.2567123,
            longitude=38.3165725,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Hong Kong SAR",
            state_code="HK",
            latitude=22.3193039,
            longitude=114.1693611,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Honiara",
            state_code="CT",
            latitude=-9.4456381,
            longitude=159.9728999,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Solomon Islands")][0]),
        ))
        list_of_states.append(State(
            name="Hope Town",
            state_code="HT",
            latitude=26.5009504,
            longitude=-76.9959872,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Horjul Municipality",
            state_code="162",
            latitude=46.0225378,
            longitude=14.2986269,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Hormigueros",
            state_code="067",
            latitude=18.1334638,
            longitude=-67.1128123,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Hormozgan",
            state_code="22",
            latitude=27.138723,
            longitude=55.1375834,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Houaphanh Province",
            state_code="HO",
            latitude=20.3254175,
            longitude=104.1001326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Houet Province",
            state_code="HOU",
            latitude=11.1320447,
            longitude=-4.2333355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Howland Island",
            state_code="UM-84",
            latitude=0.8113219,
            longitude=-176.6182736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Howland Island",
            state_code="84",
            latitude=0.8113219,
            longitude=-176.6182736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States Minor Outlying Islands")][0]),
        ))
        list_of_states.append(State(
            name="Hradec Králové",
            state_code="521",
            latitude=50.2414805,
            longitude=15.6743,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Hrastnik Municipality",
            state_code="034",
            latitude=46.1417288,
            longitude=15.0844894,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Hrpelje–Kozina Municipality",
            state_code="035",
            latitude=45.6091192,
            longitude=13.9379148,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Hsinchu",
            state_code="HSZ",
            latitude=24.8138287,
            longitude=120.9674798,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Hsinchu",
            state_code="HSQ",
            latitude=24.8387226,
            longitude=121.0177246,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Hualien",
            state_code="HUA",
            latitude=23.9871589,
            longitude=121.6015714,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Huambo Province",
            state_code="HUA",
            latitude=-12.5268221,
            longitude=15.5943388,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Huancavelica",
            state_code="HUV",
            latitude=-12.7861978,
            longitude=-74.9764024,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Huanuco",
            state_code="HUC",
            latitude=-9.9207648,
            longitude=-76.2410843,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Hubei",
            state_code="HB",
            latitude=30.7378118,
            longitude=112.2384017,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Huehuetenango Department",
            state_code="HU",
            latitude=15.5879914,
            longitude=-91.6760691,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Huelva",
            state_code="H",
            latitude=37.2708666,
            longitude=-6.9571999,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Huesca",
            state_code="HU",
            latitude=41.5976275,
            longitude=-0.9056623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Huila",
            state_code="HUI",
            latitude=2.5359349,
            longitude=-75.5276699,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Huíla Province",
            state_code="HUI",
            latitude=-14.9280553,
            longitude=14.6587821,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Humacao",
            state_code="069",
            latitude=18.1515736,
            longitude=-65.8248529,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Hunan",
            state_code="HN",
            latitude=27.3683009,
            longitude=109.2819347,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Hunedoara County",
            state_code="HD",
            latitude=45.793638,
            longitude=22.9975993,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Hưng Yên",
            state_code="66",
            latitude=20.8525711,
            longitude=106.0169971,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Hyōgo Prefecture",
            state_code="28",
            latitude=34.8579518,
            longitude=134.5453787,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Ialomița County",
            state_code="IL",
            latitude=44.603133,
            longitude=27.3789914,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Ialoveni District",
            state_code="IA",
            latitude=46.863086,
            longitude=28.8234218,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Iași County",
            state_code="IS",
            latitude=47.2679653,
            longitude=27.2185662,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Ibanda District",
            state_code="417",
            latitude=-0.096489,
            longitude=30.5739579,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Ibaraki Prefecture",
            state_code="08",
            latitude=36.2193571,
            longitude=140.1832516,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Ibb",
            state_code="IB",
            latitude=14.1415717,
            longitude=44.2479015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (7/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
