"""
States Seed #9

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
            name="Karachay-Cherkess Republic",
            state_code="KC",
            latitude=43.8845143,
            longitude=41.7303939,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Karaganda Region",
            state_code="KAR",
            latitude=47.9022182,
            longitude=71.7706807,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="Karak",
            state_code="KA",
            latitude=31.1853527,
            longitude=35.7047682,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jordan")][0]),
        ))
        list_of_states.append(State(
            name="Karakalpakstan",
            state_code="QR",
            latitude=43.8041334,
            longitude=59.4457988,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Karaman",
            state_code="70",
            latitude=37.2436336,
            longitude=33.617577,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Karas Region",
            state_code="KA",
            latitude=-26.8429645,
            longitude=17.2902839,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Karbala",
            state_code="KA",
            latitude=32.4045493,
            longitude=43.8673222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Karbinci",
            state_code="37",
            latitude=41.8180159,
            longitude=22.2324758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Karditsa Regional Unit",
            state_code="41",
            latitude=39.3640258,
            longitude=21.9214049,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Kardzhali Province",
            state_code="09",
            latitude=41.6338416,
            longitude=25.3776687,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Karlovac",
            state_code="04",
            latitude=45.2613352,
            longitude=15.52542016,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Karlovarský kraj",
            state_code="41",
            latitude=50.1435,
            longitude=12.7501899,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Karlovy Vary",
            state_code="412",
            latitude=50.1435,
            longitude=12.7501899,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Karnali Zone",
            state_code="KA",
            latitude=29.3862555,
            longitude=82.3885783,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Karnataka",
            state_code="KA",
            latitude=15.3172775,
            longitude=75.7138884,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Karonga District",
            state_code="KR",
            latitude=-9.9036365,
            longitude=33.9750018,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Karpoš Municipality",
            state_code="38",
            latitude=41.9709661,
            longitude=21.3918168,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Kars",
            state_code="36",
            latitude=40.2807636,
            longitude=42.9919527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Kārsava Municipality",
            state_code="044",
            latitude=56.7645842,
            longitude=27.7358295,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Karuzi Province",
            state_code="KR",
            latitude=-3.1340347,
            longitude=30.112735,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Karviná",
            state_code="803",
            latitude=49.8566524,
            longitude=18.5432186,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Kasaï",
            state_code="KS",
            latitude=-5.0471979,
            longitude=20.7122465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Kasaï Central",
            state_code="KC",
            latitude=-8.4404591,
            longitude=20.4165934,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Kasaï Oriental",
            state_code="KE",
            latitude=-6.033623,
            longitude=23.5728501,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Kasese District",
            state_code="406",
            latitude=0.0646285,
            longitude=30.0665236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kassala",
            state_code="KA",
            latitude=15.4581332,
            longitude=36.4039629,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Kasserine",
            state_code="42",
            latitude=35.0809148,
            longitude=8.6600586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Kastamonu",
            state_code="37",
            latitude=41.4103863,
            longitude=33.6998334,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Kastoria Regional Unit",
            state_code="56",
            latitude=40.5192691,
            longitude=21.2687171,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Kasungu District",
            state_code="KS",
            latitude=-13.1367065,
            longitude=33.258793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Katakwi District",
            state_code="207",
            latitude=1.973103,
            longitude=34.0641419,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Katavi",
            state_code="28",
            latitude=-6.3677125,
            longitude=31.2626366,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Katsina",
            state_code="KT",
            latitude=12.3796707,
            longitude=7.6305748,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Kaunas City Municipality",
            state_code="15",
            latitude=54.9145326,
            longitude=23.9053518,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Kaunas County",
            state_code="KU",
            latitude=54.9872863,
            longitude=23.9525736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Kaunas District Municipality",
            state_code="16",
            latitude=54.9936236,
            longitude=23.6324941,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Kavadarci Municipality",
            state_code="36",
            latitude=41.2890068,
            longitude=21.9999435,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Kavajë District",
            state_code="KA",
            latitude=41.1844529,
            longitude=19.5627596,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Kavango East Region",
            state_code="KE",
            latitude=-18.271048,
            longitude=18.4276047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Kavango West Region",
            state_code="KW",
            latitude=-18.271048,
            longitude=18.4276047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Kayah State",
            state_code="12",
            latitude=19.2342061,
            longitude=97.2652858,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Kayangel",
            state_code="100",
            latitude=8.07,
            longitude=134.702778,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Kayanza Province",
            state_code="KY",
            latitude=-3.0077981,
            longitude=29.6499162,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Kayes Region",
            state_code="1",
            latitude=14.0818308,
            longitude=-9.9018131,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Kayin State",
            state_code="13",
            latitude=16.9459346,
            longitude=97.9592863,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Kayseri",
            state_code="38",
            latitude=38.6256854,
            longitude=35.7406882,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Kayunga District",
            state_code="112",
            latitude=0.9860182,
            longitude=32.8535755,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kazlų Rūda municipality",
            state_code="17",
            latitude=54.7807526,
            longitude=23.4840243,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Kebbi",
            state_code="KE",
            latitude=11.4942003,
            longitude=4.2333355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Kebili",
            state_code="73",
            latitude=33.7071551,
            longitude=8.9714623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Kecskemét",
            state_code="KM",
            latitude=46.8963711,
            longitude=19.6896861,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Kedah",
            state_code="02",
            latitude=6.1183964,
            longitude=100.3684595,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Kėdainiai District Municipality",
            state_code="18",
            latitude=55.3560947,
            longitude=23.9832683,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Kédougou",
            state_code="KE",
            latitude=12.5604607,
            longitude=-12.1747077,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Keelung",
            state_code="KEE",
            latitude=25.1241862,
            longitude=121.6475834,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Kef",
            state_code="33",
            latitude=36.1230512,
            longitude=8.6600586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Kefalonia Prefecture",
            state_code="23",
            latitude=38.1753675,
            longitude=20.5692179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Kegalle District",
            state_code="92",
            latitude=7.1204053,
            longitude=80.3213106,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Ķegums Municipality",
            state_code="051",
            latitude=56.7475357,
            longitude=24.7173645,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Ķekava Municipality",
            state_code="052",
            latitude=56.8064351,
            longitude=24.1939493,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Kelantan",
            state_code="03",
            latitude=6.1253969,
            longitude=102.238071,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Kelmė District Municipality",
            state_code="19",
            latitude=55.6266352,
            longitude=22.878172,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Kemerovo Oblast",
            state_code="KEM",
            latitude=54.7574648,
            longitude=87.4055288,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kémo Prefecture",
            state_code="KG",
            latitude=5.8867794,
            longitude=19.3783206,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Kemps Bay",
            state_code="KB",
            latitude=24.02364,
            longitude=-77.545349,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Kénédougou Province",
            state_code="KEN",
            latitude=11.3919395,
            longitude=-4.976654,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Kénitra",
            state_code="KEN",
            latitude=34.2540503,
            longitude=-6.5890166,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Kent",
            state_code="KEN",
            latitude=41.1536674,
            longitude=-81.3578859,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Kentucky",
            state_code="KY",
            latitude=37.8393332,
            longitude=-84.2700179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Kep",
            state_code="23",
            latitude=10.536089,
            longitude=104.3559158,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Kepulauan Bangka Belitung",
            state_code="BB",
            latitude=-2.7410513,
            longitude=106.4405872,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Kepulauan Riau",
            state_code="KR",
            latitude=3.9456514,
            longitude=108.1428669,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Kerala",
            state_code="KL",
            latitude=10.8505159,
            longitude=76.2710833,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Kerċem",
            state_code="22",
            latitude=36.0447939,
            longitude=14.2250605,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Kericho",
            state_code="12",
            latitude=-0.1827913,
            longitude=35.4781926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Kerman",
            state_code="08",
            latitude=29.4850089,
            longitude=57.6439048,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Kermanshah",
            state_code="05",
            latitude=34.4576233,
            longitude=46.670534,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Kérouané Prefecture",
            state_code="KE",
            latitude=9.2536643,
            longitude=-9.0128926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Kerry",
            state_code="KY",
            latitude=52.1544607,
            longitude=-9.5668633,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Kgalagadi District",
            state_code="KG",
            latitude=-24.7550285,
            longitude=21.8568586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Botswana")][0]),
        ))
        list_of_states.append(State(
            name="Kgatleng District",
            state_code="KL",
            latitude=-24.1970445,
            longitude=26.2304616,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Botswana")][0]),
        ))
        list_of_states.append(State(
            name="Khabarovsk Krai",
            state_code="KHA",
            latitude=50.5888431,
            longitude=135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Khachmaz District",
            state_code="XAC",
            latitude=41.4591168,
            longitude=48.8020626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Khagrachari District",
            state_code="29",
            latitude=23.1321751,
            longitude=91.949021,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Khammouane Province",
            state_code="KH",
            latitude=17.6384066,
            longitude=105.2194808,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Khan Yunis",
            state_code="KYS",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Khánh Hòa",
            state_code="34",
            latitude=12.2585098,
            longitude=109.0526076,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Khanty-Mansi Autonomous Okrug",
            state_code="KHM",
            latitude=62.2287062,
            longitude=70.6410057,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kharkivska oblast",
            state_code="63",
            latitude=49.9935,
            longitude=36.230383,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Khartoum",
            state_code="KH",
            latitude=15.5006544,
            longitude=32.5598994,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Khatlon Province",
            state_code="KT",
            latitude=37.9113562,
            longitude=69.097023,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tajikistan")][0]),
        ))
        list_of_states.append(State(
            name="Khelvachauri Municipality",
            state_code="29",
            latitude=41.5801926,
            longitude=41.6610742,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Khémisset",
            state_code="KHE",
            latitude=33.8153704,
            longitude=-6.0573302,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Khenchela",
            state_code="40",
            latitude=35.4269404,
            longitude=7.1460155,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Khénifra",
            state_code="KHN",
            latitude=32.9340471,
            longitude=-5.661571,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Khentii Province",
            state_code="039",
            latitude=47.6081209,
            longitude=109.9372856,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Khersonska oblast",
            state_code="65",
            latitude=46.635417,
            longitude=32.616867,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Khizi District",
            state_code="XIZ",
            latitude=40.9109489,
            longitude=49.0729264,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Khmelnytska oblast",
            state_code="68",
            latitude=49.422983,
            longitude=26.9871331,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Khojali District",
            state_code="XCI",
            latitude=39.9132553,
            longitude=46.794305,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Khomas Region",
            state_code="KH",
            latitude=-22.6377854,
            longitude=17.1011931,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Khon Kaen",
            state_code="40",
            latitude=16.4321938,
            longitude=102.8236214,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Khost",
            state_code="KHO",
            latitude=33.3338472,
            longitude=69.9371673,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Khouribga",
            state_code="KHO",
            latitude=32.886023,
            longitude=-6.9208655,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Khovd Province",
            state_code="043",
            latitude=47.1129654,
            longitude=92.3110752,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Khövsgöl Province",
            state_code="041",
            latitude=50.2204484,
            longitude=100.3213768,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Khulna District",
            state_code="27",
            latitude=22.6737735,
            longitude=89.3966581,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Khulna Division",
            state_code="D",
            latitude=22.8087816,
            longitude=89.2467191,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Khuzestan",
            state_code="06",
            latitude=31.4360149,
            longitude=49.041312,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Khyber Pakhtunkhwa",
            state_code="KP",
            latitude=34.9526205,
            longitude=72.331113,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Pakistan")][0]),
        ))
        list_of_states.append(State(
            name="Kiambu",
            state_code="13",
            latitude=-1.0313701,
            longitude=36.8680791,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Kibaale District",
            state_code="407",
            latitude=0.9066802,
            longitude=31.0793705,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kiboga District",
            state_code="103",
            latitude=0.965759,
            longitude=31.7195459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kibuku District",
            state_code="227",
            latitude=1.0452874,
            longitude=33.7992536,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kičevo Municipality",
            state_code="40",
            latitude=41.5129112,
            longitude=20.9525065,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Kidal Region",
            state_code="8",
            latitude=18.7986832,
            longitude=1.8318334,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Kidričevo Municipality",
            state_code="045",
            latitude=46.3957572,
            longitude=15.7925906,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kié-Ntem Province",
            state_code="KN",
            latitude=2.028093,
            longitude=11.0711758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Equatorial Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Kiên Giang",
            state_code="47",
            latitude=9.8249587,
            longitude=105.1258955,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Kigali district",
            state_code="01",
            latitude=-1.9440727,
            longitude=30.0618851,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Rwanda")][0]),
        ))
        list_of_states.append(State(
            name="Kigoma",
            state_code="08",
            latitude=-4.8824092,
            longitude=29.6615055,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Kildare",
            state_code="KE",
            latitude=53.2120434,
            longitude=-6.8194708,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Kilifi",
            state_code="14",
            latitude=-3.5106508,
            longitude=39.9093269,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Kilimanjaro",
            state_code="09",
            latitude=-4.1336927,
            longitude=37.8087693,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Kilinochchi District",
            state_code="42",
            latitude=9.3677971,
            longitude=80.3213106,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Kilis",
            state_code="79",
            latitude=36.8204775,
            longitude=37.1687339,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Kilkenny",
            state_code="KK",
            latitude=52.5776957,
            longitude=-7.218002,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Kilkis Regional Unit",
            state_code="57",
            latitude=40.9937071,
            longitude=22.8753674,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Kindia Prefecture",
            state_code="KD",
            latitude=10.1013292,
            longitude=-12.7135121,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Kindia Region",
            state_code="D",
            latitude=10.1781694,
            longitude=-12.989615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Kingman Reef",
            state_code="UM-89",
            latitude=6.383333,
            longitude=-162.416667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Kingman Reef",
            state_code="89",
            latitude=6.383333,
            longitude=-162.416667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States Minor Outlying Islands")][0]),
        ))
        list_of_states.append(State(
            name="Kingston Parish",
            state_code="01",
            latitude=17.9683271,
            longitude=-76.782702,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Kinmen",
            state_code="KIN",
            latitude=24.3487792,
            longitude=118.3285644,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Kinshasa",
            state_code="KN",
            latitude=-4.4419311,
            longitude=15.2662931,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Kırıkkale",
            state_code="71",
            latitude=39.8876878,
            longitude=33.7555248,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Kirinyaga",
            state_code="15",
            latitude=-0.6590565,
            longitude=37.3827234,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Kırklareli",
            state_code="39",
            latitude=41.7259795,
            longitude=27.483839,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Kirklees",
            state_code="KIR",
            latitude=53.5933432,
            longitude=-1.8009509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Kirkop",
            state_code="23",
            latitude=35.8437862,
            longitude=14.4854324,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Kirkuk",
            state_code="KI",
            latitude=35.3292014,
            longitude=43.9436788,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Kirov Oblast",
            state_code="KIR",
            latitude=58.4198529,
            longitude=50.2097248,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kirovohradska oblast",
            state_code="35",
            latitude=48.507933,
            longitude=32.262317,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Kırşehir",
            state_code="40",
            latitude=39.2268905,
            longitude=33.9750018,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Kiruhura District",
            state_code="419",
            latitude=-0.1927998,
            longitude=30.8039474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kirundo Province",
            state_code="KI",
            latitude=-2.5762882,
            longitude=30.112735,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Kiryandongo District",
            state_code="421",
            latitude=2.0179907,
            longitude=32.0837445,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kisela Voda Municipality",
            state_code="39",
            latitude=41.92748,
            longitude=21.4931713,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Kishoreganj District",
            state_code="26",
            latitude=24.4260457,
            longitude=90.9820668,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Kisii",
            state_code="16",
            latitude=-0.677334,
            longitude=34.779603,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Kisoro District",
            state_code="408",
            latitude=-1.220943,
            longitude=29.6499162,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kissidougou Prefecture",
            state_code="KS",
            latitude=9.2252022,
            longitude=-10.0807298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Kisumu",
            state_code="17",
            latitude=-0.0917016,
            longitude=34.7679568,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Kitgum District",
            state_code="305",
            latitude=3.3396829,
            longitude=33.1688883,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kitui",
            state_code="18",
            latitude=-1.6832822,
            longitude=38.3165725,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Kladno",
            state_code="203",
            latitude=50.1940258,
            longitude=14.1043657,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Klaipeda City Municipality",
            state_code="20",
            latitude=55.7032948,
            longitude=21.1442795,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Klaipėda County",
            state_code="KL",
            latitude=55.6519744,
            longitude=21.3743956,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Klaipėda District Municipality",
            state_code="21",
            latitude=55.6841615,
            longitude=21.4416464,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Klatovy",
            state_code="322",
            latitude=49.3955549,
            longitude=13.2950937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Knowsley",
            state_code="KWL",
            latitude=53.454594,
            longitude=-2.852907,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Kobarid Municipality",
            state_code="046",
            latitude=46.2456971,
            longitude=13.5786949,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kobilje Municipality",
            state_code="047",
            latitude=46.68518,
            longitude=16.3936719,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Koboko District",
            state_code="319",
            latitude=3.5237058,
            longitude=31.03351,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kocaeli",
            state_code="41",
            latitude=40.8532704,
            longitude=29.8815203,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Kočani Municipality",
            state_code="42",
            latitude=41.9858374,
            longitude=22.4053046,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Kocēni Municipality",
            state_code="045",
            latitude=57.5226292,
            longitude=25.3349507,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Kočevje Municipality",
            state_code="048",
            latitude=45.6428,
            longitude=14.8615838,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kōchi Prefecture",
            state_code="39",
            latitude=33.2879161,
            longitude=132.2759262,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Kogi",
            state_code="KO",
            latitude=7.7337325,
            longitude=6.6905836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Koh Kong",
            state_code="9",
            latitude=11.5762804,
            longitude=103.3587288,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Kohgiluyeh and Boyer-Ahmad",
            state_code="17",
            latitude=30.724586,
            longitude=50.8456323,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Koknese Municipality",
            state_code="046",
            latitude=56.720556,
            longitude=25.4893909,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Kolašin Municipality",
            state_code="09",
            latitude=42.7601916,
            longitude=19.4259114,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Kolda",
            state_code="KD",
            latitude=12.9107495,
            longitude=-14.9505671,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Kole District",
            state_code="325",
            latitude=2.3701097,
            longitude=32.7633036,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kolín",
            state_code="204",
            latitude=49.9883293,
            longitude=15.0551977,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Kolonjë District",
            state_code="ER",
            latitude=40.3373262,
            longitude=20.6794676,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Kolubara District",
            state_code="09",
            latitude=44.3509811,
            longitude=20.0004305,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Komárom-Esztergom",
            state_code="KE",
            latitude=47.5779786,
            longitude=18.1256855,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Komen Municipality",
            state_code="049",
            latitude=45.8175235,
            longitude=13.7482711,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Komenda Municipality",
            state_code="164",
            latitude=46.206488,
            longitude=14.5382499,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Komi Republic",
            state_code="KO",
            latitude=63.8630539,
            longitude=54.831269,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Komondjari Province",
            state_code="KMD",
            latitude=12.7126527,
            longitude=0.6773046,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Kompienga Province",
            state_code="KMP",
            latitude=11.5238362,
            longitude=0.7532809,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Kon Tum",
            state_code="28",
            latitude=14.3497403,
            longitude=108.0004606,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Konče Municipality",
            state_code="41",
            latitude=41.5171011,
            longitude=22.3814624,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Kongo Central",
            state_code="BC",
            latitude=-5.2365685,
            longitude=13.914399,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Konya",
            state_code="42",
            latitude=37.9838134,
            longitude=32.7181375,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Koper City Municipality",
            state_code="050",
            latitude=45.548059,
            longitude=13.7301877,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Koprivnica-Križevci",
            state_code="06",
            latitude=46.1568919,
            longitude=16.8390826,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Korçë County",
            state_code="06",
            latitude=40.590567,
            longitude=20.6168921,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Korçë District",
            state_code="KO",
            latitude=40.590567,
            longitude=20.6168921,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Koror",
            state_code="150",
            latitude=7.3375646,
            longitude=134.4889469,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Kosi Zone",
            state_code="KO",
            latitude=27.0536524,
            longitude=87.3016132,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Košice Region",
            state_code="KI",
            latitude=48.6375737,
            longitude=21.0834225,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovakia")][0]),
        ))
        list_of_states.append(State(
            name="Kosovska Mitrovica District",
            state_code="XKM",
            latitude=42.8913909,
            longitude=20.8659995,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kosovo")][0]),
        ))
        list_of_states.append(State(
            name="Kosrae State",
            state_code="KSA",
            latitude=5.3095618,
            longitude=162.9814877,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Micronesia")][0]),
        ))
        list_of_states.append(State(
            name="Kossi Province",
            state_code="KOS",
            latitude=12.960458,
            longitude=-3.9062688,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Kostanay Region",
            state_code="KUS",
            latitude=51.5077096,
            longitude=64.0479073,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="Kostanjevica na Krki Municipality",
            state_code="197",
            latitude=45.8316638,
            longitude=15.4411906,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kostel Municipality",
            state_code="165",
            latitude=45.4928255,
            longitude=14.8708235,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kostroma Oblast",
            state_code="KOS",
            latitude=58.5501069,
            longitude=43.9541102,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kotayk Region",
            state_code="KT",
            latitude=40.5410214,
            longitude=44.7690148,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Armenia")][0]),
        ))
        list_of_states.append(State(
            name="Kotido District",
            state_code="306",
            latitude=3.0415679,
            longitude=33.8857747,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kotor Municipality",
            state_code="10",
            latitude=42.5740261,
            longitude=18.6413145,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Koubia Prefecture",
            state_code="KB",
            latitude=11.582354,
            longitude=-11.8920237,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Kouffo Department",
            state_code="KO",
            latitude=7.0035894,
            longitude=1.7538817,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Kouilou Department",
            state_code="5",
            latitude=-4.1428413,
            longitude=11.8891721,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Koulikoro Region",
            state_code="2",
            latitude=13.8018074,
            longitude=-7.4381355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Koulpélogo Province",
            state_code="KOP",
            latitude=11.5247674,
            longitude=0.1494988,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Koundara Prefecture",
            state_code="KN",
            latitude=12.4894021,
            longitude=-13.3067562,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Kouritenga Province",
            state_code="KOT",
            latitude=12.1631813,
            longitude=-0.2244662,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Kouroussa Prefecture",
            state_code="KO",
            latitude=10.6489229,
            longitude=-9.8850586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Kourwéogo Province",
            state_code="KOW",
            latitude=12.7077495,
            longitude=-1.7538817,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Kowloon City",
            state_code="KKC",
            latitude=22.3282,
            longitude=114.19155,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Kozani Prefecture",
            state_code="58",
            latitude=40.3005586,
            longitude=21.7887737,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Kozje Municipality",
            state_code="051",
            latitude=46.0733211,
            longitude=15.5596719,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Krabi",
            state_code="81",
            latitude=8.0862997,
            longitude=98.9062835,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Kraj Vysočina",
            state_code="63",
            latitude=49.4490052,
            longitude=15.6405934,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Královéhradecký kraj",
            state_code="52",
            latitude=50.3512484,
            longitude=15.7976459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Kranj City Municipality",
            state_code="052",
            latitude=46.2585021,
            longitude=14.3543569,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kranjska Gora Municipality",
            state_code="053",
            latitude=46.4845293,
            longitude=13.7857145,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Krapina-Zagorje",
            state_code="02",
            latitude=46.1013393,
            longitude=15.8809693,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Krāslava Municipality",
            state_code="047",
            latitude=55.8951464,
            longitude=27.1814577,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Krasnodar Krai",
            state_code="KDA",
            latitude=45.6415289,
            longitude=39.7055977,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Krasnoyarsk Krai",
            state_code="KYA",
            latitude=64.2479758,
            longitude=95.1104176,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kratie",
            state_code="10",
            latitude=12.5043608,
            longitude=105.9699878,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Kratovo Municipality",
            state_code="43",
            latitude=42.0537141,
            longitude=22.0714835,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Kretinga District Municipality",
            state_code="22",
            latitude=55.883842,
            longitude=21.2350919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Krimulda Municipality",
            state_code="048",
            latitude=57.1791273,
            longitude=24.7140127,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Kriva Palanka Municipality",
            state_code="44",
            latitude=42.2058454,
            longitude=22.3307965,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Krivogaštani Municipality",
            state_code="45",
            latitude=41.3082306,
            longitude=21.3679689,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Križevci Municipality",
            state_code="166",
            latitude=46.5701821,
            longitude=16.1092653,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kroměříž",
            state_code="721",
            latitude=49.2916582,
            longitude=17.39938,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Kronoberg County",
            state_code="G",
            latitude=56.7183403,
            longitude=14.4114673,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Krujë District",
            state_code="KR",
            latitude=41.5094765,
            longitude=19.7710732,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Kruševo Municipality",
            state_code="46",
            latitude=41.3769331,
            longitude=21.2606554,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Krustpils Municipality",
            state_code="049",
            latitude=56.5415578,
            longitude=26.2446397,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Kuala Lumpur",
            state_code="14",
            latitude=3.139003,
            longitude=101.686855,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Kuçovë District",
            state_code="KC",
            latitude=40.7837063,
            longitude=19.8782348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Kufra District",
            state_code="KF",
            latitude=23.3112389,
            longitude=21.8568586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Kukës County",
            state_code="07",
            latitude=42.0807464,
            longitude=20.4142923,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Kukës District",
            state_code="KU",
            latitude=42.0807464,
            longitude=20.4142923,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Kuldīga Municipality",
            state_code="050",
            latitude=56.9687257,
            longitude=21.9613739,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Kumamoto Prefecture",
            state_code="43",
            latitude=32.8594427,
            longitude=130.7969149,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Kumanovo Municipality",
            state_code="47",
            latitude=42.0732613,
            longitude=21.7853143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Kumi District",
            state_code="208",
            latitude=1.4876999,
            longitude=33.9303991,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kunar",
            state_code="KNR",
            latitude=34.8465893,
            longitude=71.097317,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Kunduz Province",
            state_code="KDZ",
            latitude=36.7285511,
            longitude=68.8678982,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (9/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
