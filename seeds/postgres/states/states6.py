"""
States Seed #6

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
            name="East Sussex",
            state_code="ESX",
            latitude=50.9085955,
            longitude=0.2494166,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Eastern",
            state_code="EP",
            latitude=6.5,
            longitude=-0.5,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Eastern",
            state_code="HEA",
            latitude=22.28411,
            longitude=114.22414,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Cape",
            state_code="EC",
            latitude=-32.2968402,
            longitude=26.419389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Africa")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Development Region",
            state_code="4",
            latitude=27.3309072,
            longitude=87.0624261,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Division",
            state_code="E",
            latitude=32.8094305,
            longitude=-117.1289937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Equatoria",
            state_code="EE",
            latitude=5.0692995,
            longitude=33.438353,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Highlands Province",
            state_code="EHG",
            latitude=-6.5861674,
            longitude=145.6689636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Province",
            state_code="02",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Rwanda")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Province",
            state_code="04",
            latitude=24.0439932,
            longitude=45.6589225,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Province",
            state_code="E",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sierra Leone")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Province",
            state_code="5",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Province",
            state_code="03",
            latitude=23.1669688,
            longitude=49.3653149,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zambia")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Region",
            state_code="7",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iceland")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Region",
            state_code="E",
            latitude=6.2374036,
            longitude=-0.4502368,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Samar",
            state_code="EAS",
            latitude=11.5000731,
            longitude=125.4999908,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Tobago",
            state_code="ETO",
            latitude=11.2979348,
            longitude=-60.5588524,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Eastern Visayas",
            state_code="08",
            latitude=12.2445533,
            longitude=125.0388164,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Ebonyi",
            state_code="EB",
            latitude=6.2649232,
            longitude=8.0137302,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Edinburgh",
            state_code="EDH",
            latitude=55.953252,
            longitude=-3.188267,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Edineț District",
            state_code="ED",
            latitude=48.1678991,
            longitude=27.2936143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Edirne",
            state_code="22",
            latitude=41.1517222,
            longitude=26.5137964,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Edo",
            state_code="ED",
            latitude=6.6341831,
            longitude=5.9304056,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Eger",
            state_code="EG",
            latitude=47.9025348,
            longitude=20.3772284,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Ehime Prefecture",
            state_code="38",
            latitude=33.6025306,
            longitude=132.7857583,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Ekiti",
            state_code="EK",
            latitude=7.7189862,
            longitude=5.3109505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="El Bayadh",
            state_code="32",
            latitude=32.7148824,
            longitude=0.9056623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="El Hajeb",
            state_code="HAJ",
            latitude=33.685735,
            longitude=-5.3677844,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="El Jadida",
            state_code="JDI",
            latitude=33.2316326,
            longitude=-8.5007116,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="El Kelâa des Sraghna",
            state_code="KES",
            latitude=32.0522767,
            longitude=-7.3516558,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="El M'ghair",
            state_code="49",
            latitude=33.9540561,
            longitude=5.1346418,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="El Menia",
            state_code="50",
            latitude=31.364225,
            longitude=2.5784495,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="El Oro",
            state_code="O",
            latitude=-3.2592413,
            longitude=-79.9583541,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="El Oued",
            state_code="39",
            latitude=33.367811,
            longitude=6.8516511,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="El Paraíso Department",
            state_code="EP",
            latitude=13.9821294,
            longitude=-86.4996546,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="El Progreso Department",
            state_code="PR",
            latitude=14.9388732,
            longitude=-90.0746767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="El Seibo Province",
            state_code="08",
            latitude=18.7658496,
            longitude=-69.040668,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="El Tarf",
            state_code="36",
            latitude=36.7576678,
            longitude=8.3076343,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Elazığ",
            state_code="23",
            latitude=38.4964804,
            longitude=39.2199029,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Elbasan County",
            state_code="03",
            latitude=41.1266672,
            longitude=20.2355647,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Elektrėnai municipality",
            state_code="08",
            latitude=54.7653934,
            longitude=24.7740583,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Elgeyo-Marakwet",
            state_code="05",
            latitude=1.0498237,
            longitude=35.4781926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Emberá-Wounaan Comarca",
            state_code="EM",
            latitude=8.3766983,
            longitude=-77.6536125,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Embu",
            state_code="06",
            latitude=-0.6560477,
            longitude=37.7237678,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Emilia-Romagna",
            state_code="45",
            latitude=44.5967607,
            longitude=11.2186396,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Encamp",
            state_code="03",
            latitude=42.5359764,
            longitude=1.5836773,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Andorra")][0]),
        ))
        list_of_states.append(State(
            name="Enga Province",
            state_code="EPW",
            latitude=-5.3005849,
            longitude=143.5635637,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="England",
            state_code="ENG",
            latitude=52.3555177,
            longitude=-1.1743197,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Engure Municipality",
            state_code="029",
            latitude=57.16235,
            longitude=23.2196634,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Enna",
            state_code="EN",
            latitude=37.5676216,
            longitude=14.2795349,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Ennedi-Est",
            state_code="EE",
            latitude=16.3420496,
            longitude=23.0011989,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Ennedi-Ouest",
            state_code="EO",
            latitude=18.977563,
            longitude=21.8568586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Entre Ríos",
            state_code="E",
            latitude=-31.7746654,
            longitude=-60.4956461,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Enugu",
            state_code="EN",
            latitude=6.536353,
            longitude=7.4356194,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Epirus Region",
            state_code="D",
            latitude=39.5706413,
            longitude=20.7642843,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Équateur",
            state_code="EQ",
            latitude=-1.831239,
            longitude=-78.183406,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Erbil",
            state_code="AR",
            latitude=36.5570628,
            longitude=44.3851263,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Érd",
            state_code="ER",
            latitude=47.3919718,
            longitude=18.904544,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Ērgļi Municipality",
            state_code="030",
            latitude=56.9237065,
            longitude=25.6753852,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Ermera District",
            state_code="ER",
            latitude=-8.7524802,
            longitude=125.3987294,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Timor-Leste")][0]),
        ))
        list_of_states.append(State(
            name="Erongo Region",
            state_code="ER",
            latitude=-22.2565682,
            longitude=15.4068079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Errachidia",
            state_code="ERR",
            latitude=31.9051275,
            longitude=-4.7277528,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Erzincan",
            state_code="24",
            latitude=39.7681914,
            longitude=39.0501306,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Erzurum",
            state_code="25",
            latitude=40.0746799,
            longitude=41.6694562,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Es-Semara (EH-partial)",
            state_code="ESM",
            latitude=26.741856,
            longitude=-11.6783671,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Escaldes-Engordany",
            state_code="08",
            latitude=42.4909379,
            longitude=1.5886966,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Andorra")][0]),
        ))
        list_of_states.append(State(
            name="Eschen",
            state_code="02",
            latitude=40.7669574,
            longitude=-73.9522821,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Escuintla Department",
            state_code="ES",
            latitude=14.1910912,
            longitude=-90.9820668,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Eskişehir",
            state_code="26",
            latitude=39.6329657,
            longitude=31.2626366,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Esmeraldas",
            state_code="E",
            latitude=0.9681789,
            longitude=-79.6517202,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Espaillat Province",
            state_code="09",
            latitude=19.6277658,
            longitude=-70.2786775,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Espírito Santo",
            state_code="ES",
            latitude=-19.1834229,
            longitude=-40.3088626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Essaouira",
            state_code="ESI",
            latitude=31.5084926,
            longitude=-9.7595041,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Essequibo Islands-West Demerara",
            state_code="ES",
            latitude=6.5720132,
            longitude=-58.4629997,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guyana")][0]),
        ))
        list_of_states.append(State(
            name="Essex",
            state_code="ESS",
            latitude=51.5742447,
            longitude=0.4856781,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Essonne",
            state_code="91",
            latitude=48.5304615,
            longitude=1.9699056,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Est Region",
            state_code="08",
            latitude=12.4365526,
            longitude=0.9056623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Estado de México",
            state_code="MEX",
            latitude=23.634501,
            longitude=-102.552784,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Estelí",
            state_code="ES",
            latitude=13.0851139,
            longitude=-86.3630197,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Estuaire Province",
            state_code="1",
            latitude=0.4432864,
            longitude=10.0807298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gabon")][0]),
        ))
        list_of_states.append(State(
            name="Euboea",
            state_code="04",
            latitude=38.5236036,
            longitude=23.8584737,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Eure",
            state_code="27",
            latitude=49.0754035,
            longitude=0.4893732,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Eure-et-Loir",
            state_code="28",
            latitude=48.4469784,
            longitude=0.8147025,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Évora",
            state_code="07",
            latitude=38.5744468,
            longitude=-7.9076553,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Ewa District",
            state_code="09",
            latitude=-0.5087241,
            longitude=166.9369384,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nauru")][0]),
        ))
        list_of_states.append(State(
            name="Exuma",
            state_code="EX",
            latitude=23.6192598,
            longitude=-75.9695465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Fa'asaleleaga",
            state_code="FA",
            latitude=-13.6307638,
            longitude=-172.2365981,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Samoa")][0]),
        ))
        list_of_states.append(State(
            name="Faafu Atoll",
            state_code="14",
            latitude=3.2309409,
            longitude=72.9460566,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Faetano",
            state_code="04",
            latitude=43.9348967,
            longitude=12.4896554,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "San Marino")][0]),
        ))
        list_of_states.append(State(
            name="Fahs-Anjra",
            state_code="FAH",
            latitude=35.7601992,
            longitude=-5.6668306,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Faiyum",
            state_code="FYM",
            latitude=29.3084021,
            longitude=30.8428497,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Fajardo",
            state_code="053",
            latitude=18.3252148,
            longitude=-65.6539356,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Falcón",
            state_code="I",
            latitude=11.1810674,
            longitude=-69.8597406,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Fălești District",
            state_code="FA",
            latitude=47.5647725,
            longitude=27.7265593,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Falkirk",
            state_code="FAL",
            latitude=56.0018775,
            longitude=-3.7839131,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Famagusta District (Mağusa)",
            state_code="04",
            latitude=35.2857023,
            longitude=33.8411288,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cyprus")][0]),
        ))
        list_of_states.append(State(
            name="Far North",
            state_code="EN",
            latitude=66.7613451,
            longitude=124.123753,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cameroon")][0]),
        ))
        list_of_states.append(State(
            name="Far-Western Development Region",
            state_code="5",
            latitude=29.2987871,
            longitude=80.9871074,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Farah",
            state_code="FRA",
            latitude=32.495328,
            longitude=62.2626627,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Faranah Prefecture",
            state_code="FA",
            latitude=9.9057399,
            longitude=-10.8000051,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Faridpur District",
            state_code="15",
            latitude=23.5423919,
            longitude=89.6308921,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Faro",
            state_code="08",
            latitude=37.0193548,
            longitude=-7.9304397,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Fars",
            state_code="07",
            latitude=29.1043813,
            longitude=53.045893,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Faryab",
            state_code="FYB",
            latitude=36.0795613,
            longitude=64.905955,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Fatick",
            state_code="FK",
            latitude=14.3390167,
            longitude=-16.4111425,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Federal Dependencies of Venezuela",
            state_code="W",
            latitude=10.9377053,
            longitude=-65.3569573,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Federally Administered Tribal Areas",
            state_code="TA",
            latitude=32.667476,
            longitude=69.8597406,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Pakistan")][0]),
        ))
        list_of_states.append(State(
            name="Federation of Bosnia and Herzegovina",
            state_code="BIH",
            latitude=43.8874897,
            longitude=17.842793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Fejér County",
            state_code="FE",
            latitude=47.1217932,
            longitude=18.5294815,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Feni District",
            state_code="16",
            latitude=22.9408784,
            longitude=91.4066646,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Fergana Region",
            state_code="FA",
            latitude=40.4568081,
            longitude=71.2874209,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Fermanagh and Omagh",
            state_code="FMO",
            latitude=54.4513524,
            longitude=-7.7125018,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Fermanagh District Council",
            state_code="FER",
            latitude=54.3447978,
            longitude=-7.6384218,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Fermo",
            state_code="FM",
            latitude=43.0931367,
            longitude=13.5899733,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Ferrara",
            state_code="FE",
            latitude=44.766368,
            longitude=11.7644068,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Fès",
            state_code="FES",
            latitude=34.0239579,
            longitude=-5.0367599,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Fès-Meknès",
            state_code="03",
            latitude=34.062529,
            longitude=-4.7277528,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Fgura",
            state_code="08",
            latitude=35.8738269,
            longitude=14.5232901,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Fianarantsoa Province",
            state_code="F",
            latitude=-22.353624,
            longitude=46.8252838,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Madagascar")][0]),
        ))
        list_of_states.append(State(
            name="Fier County",
            state_code="04",
            latitude=40.9191392,
            longitude=19.6639309,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Fier District",
            state_code="FR",
            latitude=40.727504,
            longitude=19.5627596,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Fife",
            state_code="FIF",
            latitude=56.2082078,
            longitude=-3.1495175,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Figuig",
            state_code="FIG",
            latitude=32.1092613,
            longitude=-1.229806,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Finistère",
            state_code="29",
            latitude=48.226961,
            longitude=-4.8243733,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Finland Proper",
            state_code="19",
            latitude=60.3627914,
            longitude=22.4439369,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Fiorentino",
            state_code="05",
            latitude=43.9078337,
            longitude=12.4581209,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "San Marino")][0]),
        ))
        list_of_states.append(State(
            name="Fizuli District",
            state_code="FUZ",
            latitude=39.5378605,
            longitude=47.3033877,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Flacq",
            state_code="FL",
            latitude=-20.2257836,
            longitude=57.7119274,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Flanders",
            state_code="VLG",
            latitude=51.0108706,
            longitude=3.7264613,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="Flemish Brabant",
            state_code="VBR",
            latitude=50.8815434,
            longitude=4.564597,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="Flevoland",
            state_code="FL",
            latitude=52.5279781,
            longitude=5.5953508,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Flintshire",
            state_code="FLN",
            latitude=53.1668658,
            longitude=-3.1418908,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Flores",
            state_code="FS",
            latitude=-33.5733753,
            longitude=-56.8945028,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Florești District",
            state_code="FL",
            latitude=47.8667849,
            longitude=28.3391864,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Floriana",
            state_code="09",
            latitude=45.4952185,
            longitude=-73.7139576,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Florida",
            state_code="054",
            latitude=27.6648274,
            longitude=-81.5157535,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Florida",
            state_code="FL",
            latitude=27.6648274,
            longitude=-81.5157535,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Florida",
            state_code="FD",
            latitude=28.0359495,
            longitude=-82.4579289,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Foggia",
            state_code="FG",
            latitude=41.638448,
            longitude=15.5943388,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Fontana",
            state_code="10",
            latitude=34.0922335,
            longitude=-117.435048,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Forécariah Prefecture",
            state_code="FO",
            latitude=9.3886187,
            longitude=-13.0817903,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Forlì-Cesena",
            state_code="FC",
            latitude=43.9947681,
            longitude=11.9804613,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Formosa",
            state_code="P",
            latitude=-26.1894804,
            longitude=-58.2242806,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Fquih Ben Salah",
            state_code="FQH",
            latitude=32.500168,
            longitude=-6.7100717,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Francisco Morazán Department",
            state_code="FM",
            latitude=14.45411,
            longitude=-87.0624261,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Free State",
            state_code="FS",
            latitude=37.6858525,
            longitude=-97.2811256,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Africa")][0]),
        ))
        list_of_states.append(State(
            name="Freeport",
            state_code="FP",
            latitude=42.2966861,
            longitude=-89.6212271,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="French Guiana",
            state_code="973",
            latitude=3.933889,
            longitude=-53.125782,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="French Polynesia",
            state_code="PF",
            latitude=-17.679742,
            longitude=-149.406843,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="French Southern and Antarctic Lands",
            state_code="TF",
            latitude=-47.5446604,
            longitude=51.2837542,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Fresh Creek",
            state_code="FC",
            latitude=40.6543756,
            longitude=-73.8947939,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Fria Prefecture",
            state_code="FR",
            latitude=10.3674543,
            longitude=-13.5841871,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Fribourg",
            state_code="FR",
            latitude=46.6816748,
            longitude=7.1172635,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Friesland",
            state_code="FR",
            latitude=53.1641642,
            longitude=5.7817542,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Friuli–Venezia Giulia",
            state_code="36",
            latitude=46.2259177,
            longitude=13.1033646,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Fromager",
            state_code="18",
            latitude=45.5450213,
            longitude=-73.6046223,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Frosinone",
            state_code="FR",
            latitude=41.6576528,
            longitude=13.6362715,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Frýdek-Místek",
            state_code="802",
            latitude=49.6819305,
            longitude=18.3673216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Fujairah",
            state_code="FU",
            latitude=25.1288099,
            longitude=56.3264849,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Arab Emirates")][0]),
        ))
        list_of_states.append(State(
            name="Fujian",
            state_code="FJ",
            latitude=26.4836842,
            longitude=117.9249002,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Fukui Prefecture",
            state_code="18",
            latitude=35.896227,
            longitude=136.2111579,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Fukuoka Prefecture",
            state_code="40",
            latitude=33.5662559,
            longitude=130.715857,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Fukushima Prefecture",
            state_code="07",
            latitude=37.3834373,
            longitude=140.1832516,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Funafuti",
            state_code="FUN",
            latitude=-8.5211471,
            longitude=179.1961926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tuvalu")][0]),
        ))
        list_of_states.append(State(
            name="Gaafu Alif Atoll",
            state_code="27",
            latitude=0.6124813,
            longitude=73.323708,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Gaafu Dhaalu Atoll",
            state_code="28",
            latitude=0.358804,
            longitude=73.1821623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Gabès",
            state_code="81",
            latitude=33.9459648,
            longitude=9.7232673,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Gabrovo Province",
            state_code="07",
            latitude=42.86847,
            longitude=25.316889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Gabú Region",
            state_code="GA",
            latitude=11.8962488,
            longitude=-14.1001326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="Gafsa",
            state_code="71",
            latitude=34.3788505,
            longitude=8.6600586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Gaga'emauga",
            state_code="GE",
            latitude=-13.5428666,
            longitude=-172.366887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Samoa")][0]),
        ))
        list_of_states.append(State(
            name="Gaga'ifomauga",
            state_code="GI",
            latitude=-13.5468007,
            longitude=-172.4969331,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Samoa")][0]),
        ))
        list_of_states.append(State(
            name="Gagauzia",
            state_code="GA",
            latitude=46.0979435,
            longitude=28.6384645,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Gaibandha District",
            state_code="19",
            latitude=25.3296928,
            longitude=89.5429652,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Galápagos",
            state_code="W",
            latitude=-0.9537691,
            longitude=-90.9656019,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Galați County",
            state_code="GL",
            latitude=45.7800569,
            longitude=27.8251576,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Galguduud",
            state_code="GA",
            latitude=5.1850128,
            longitude=46.8252838,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Galle District",
            state_code="31",
            latitude=6.057749,
            longitude=80.2175572,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Galway",
            state_code="G",
            latitude=53.3564509,
            longitude=-8.8534113,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Gambela Region",
            state_code="GA",
            latitude=7.9219687,
            longitude=34.1531947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ethiopia")][0]),
        ))
        list_of_states.append(State(
            name="Gampaha District",
            state_code="12",
            latitude=7.0712619,
            longitude=80.0087746,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Gamprin",
            state_code="03",
            latitude=47.213249,
            longitude=9.5025195,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Gandaki Zone",
            state_code="GA",
            latitude=28.3732037,
            longitude=84.4382721,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Gangwon Province",
            state_code="42",
            latitude=37.8228,
            longitude=128.1555,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Ganja",
            state_code="GA",
            latitude=36.3687338,
            longitude=-95.9985767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Gansu",
            state_code="GS",
            latitude=35.7518326,
            longitude=104.2861116,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Ganzourgou Province",
            state_code="GAN",
            latitude=12.2537648,
            longitude=-0.7532809,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Gao Region",
            state_code="7",
            latitude=16.9066332,
            longitude=1.5208624,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Gaoual Prefecture",
            state_code="GA",
            latitude=11.5762804,
            longitude=-13.3587288,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Gard",
            state_code="30",
            latitude=43.9595276,
            longitude=3.4935681,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Garissa",
            state_code="07",
            latitude=-0.4532293,
            longitude=39.6460988,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Garkalne Municipality",
            state_code="031",
            latitude=57.0190387,
            longitude=24.3826181,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Gasa District",
            state_code="GA",
            latitude=28.0185886,
            longitude=89.9253233,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Gash-Barka Region",
            state_code="GB",
            latitude=15.4068825,
            longitude=37.6386622,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Eritrea")][0]),
        ))
        list_of_states.append(State(
            name="Gateshead",
            state_code="GAT",
            latitude=54.95268,
            longitude=-1.603411,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Gauteng",
            state_code="GP",
            latitude=-26.2707593,
            longitude=28.1122679,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Africa")][0]),
        ))
        list_of_states.append(State(
            name="Gävleborg County",
            state_code="X",
            latitude=61.3011993,
            longitude=16.1534214,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Gaza",
            state_code="GZA",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Gaza Province",
            state_code="G",
            latitude=-23.0221928,
            longitude=32.7181375,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Gazi Baba Municipality",
            state_code="17",
            latitude=42.0162961,
            longitude=21.4991334,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Gaziantep",
            state_code="27",
            latitude=37.0763882,
            longitude=37.3827234,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Gazipur District",
            state_code="18",
            latitude=24.0958171,
            longitude=90.4125181,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Gbarpolu County",
            state_code="GP",
            latitude=7.4952637,
            longitude=-10.0807298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Gedo",
            state_code="GE",
            latitude=3.5039227,
            longitude=42.2362435,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Gegharkunik Province",
            state_code="GR",
            latitude=40.3526426,
            longitude=45.1260414,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Armenia")][0]),
        ))
        list_of_states.append(State(
            name="Geita",
            state_code="27",
            latitude=-2.8242257,
            longitude=32.2653887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Gelderland",
            state_code="GE",
            latitude=52.045155,
            longitude=5.8718235,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Geneva",
            state_code="GE",
            latitude=46.2180073,
            longitude=6.1216925,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Georgia",
            state_code="GA",
            latitude=32.1656221,
            longitude=-82.9000751,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Gers",
            state_code="32",
            latitude=43.6950534,
            longitude=-0.0999728,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Gevgelija Municipality",
            state_code="18",
            latitude=41.2118606,
            longitude=22.3814624,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Ghanzi District",
            state_code="GH",
            latitude=-21.8652314,
            longitude=21.8568586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Botswana")][0]),
        ))
        list_of_states.append(State(
            name="Gharbia",
            state_code="GH",
            latitude=30.8753556,
            longitude=31.03351,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Ghardaïa",
            state_code="47",
            latitude=32.4943741,
            longitude=3.64446,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Ghat District",
            state_code="GT",
            latitude=24.9640371,
            longitude=10.1759285,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Ghazni",
            state_code="GHA",
            latitude=33.5450587,
            longitude=68.4173972,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Ghōr",
            state_code="GHO",
            latitude=34.0995776,
            longitude=64.905955,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Gia Lai",
            state_code="30",
            latitude=13.8078943,
            longitude=108.109375,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Gifu Prefecture",
            state_code="21",
            latitude=35.7437491,
            longitude=136.9805103,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Gilan",
            state_code="01",
            latitude=37.2809455,
            longitude=49.5924134,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Gilbert Islands",
            state_code="G",
            latitude=0.3524262,
            longitude=174.7552634,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kiribati")][0]),
        ))
        list_of_states.append(State(
            name="Gilgit-Baltistan",
            state_code="GB",
            latitude=35.8025667,
            longitude=74.9831808,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Pakistan")][0]),
        ))
        list_of_states.append(State(
            name="Gipuzkoa",
            state_code="SS",
            latitude=43.145236,
            longitude=-2.4461825,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Giresun",
            state_code="28",
            latitude=40.6461672,
            longitude=38.5935511,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Girona",
            state_code="GI",
            latitude=41.9803445,
            longitude=2.8011577,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Gironde",
            state_code="33",
            latitude=44.8958469,
            longitude=-1.5940532,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Gisborne District",
            state_code="GIS",
            latitude=-38.1358174,
            longitude=178.3239309,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Gitega Province",
            state_code="GI",
            latitude=-3.4929051,
            longitude=29.9277947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Giurgiu County",
            state_code="GR",
            latitude=43.9037076,
            longitude=25.9699265,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Giza",
            state_code="GZ",
            latitude=28.7666216,
            longitude=29.2320784,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Gjilan District",
            state_code="XGJ",
            latitude=42.4635206,
            longitude=21.4694011,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kosovo")][0]),
        ))
        list_of_states.append(State(
            name="Gjirokastër County",
            state_code="05",
            latitude=40.0672874,
            longitude=20.1045229,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Gjirokastër District",
            state_code="GJ",
            latitude=40.0672874,
            longitude=20.1045229,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Gjorče Petrov Municipality",
            state_code="29",
            latitude=42.0606374,
            longitude=21.3202736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Glacis",
            state_code="12",
            latitude=47.1157303,
            longitude=-70.3028183,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Glarus",
            state_code="GL",
            latitude=47.0411232,
            longitude=9.0679,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Glasgow",
            state_code="GLG",
            latitude=55.864237,
            longitude=-4.251806,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Glodeni District",
            state_code="GL",
            latitude=47.7790156,
            longitude=27.516801,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Gloucestershire",
            state_code="GLS",
            latitude=51.8642112,
            longitude=-2.2380335,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Gnagna Province",
            state_code="GNA",
            latitude=12.8974992,
            longitude=0.0746767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Gnaviyani Atoll",
            state_code="29",
            latitude=-0.3006425,
            longitude=73.4239143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Goa",
            state_code="GA",
            latitude=15.2993265,
            longitude=74.123996,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Gobustan District",
            state_code="QOB",
            latitude=40.5326104,
            longitude=48.927375,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Gôh-Djiboua District",
            state_code="GD",
            latitude=5.8711393,
            longitude=-5.5617279,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Goiás",
            state_code="GO",
            latitude=-15.8270369,
            longitude=-49.8362237,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Golestan",
            state_code="27",
            latitude=37.2898123,
            longitude=55.1375834,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Gomba District",
            state_code="121",
            latitude=0.2229791,
            longitude=31.6739371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Gombe",
            state_code="GO",
            latitude=10.3637795,
            longitude=11.1927587,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Gomel Region",
            state_code="HO",
            latitude=52.1648754,
            longitude=29.1333251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belarus")][0]),
        ))
        list_of_states.append(State(
            name="Gopalganj District",
            state_code="17",
            latitude=26.4831584,
            longitude=84.43655,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (6/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
