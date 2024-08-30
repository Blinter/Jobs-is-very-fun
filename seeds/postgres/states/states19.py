"""
States Seed #19

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
            name="Tây Ninh",
            state_code="37",
            latitude=11.3351554,
            longitude=106.1098854,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Taza",
            state_code="TAZ",
            latitude=34.2788953,
            longitude=-3.5812692,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Tbilisi",
            state_code="TB",
            latitude=41.7151377,
            longitude=44.827096,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Tearce Municipality",
            state_code="75",
            latitude=42.0777511,
            longitude=21.0534923,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Tébessa",
            state_code="12",
            latitude=35.1290691,
            longitude=7.9592863,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Tehran",
            state_code="23",
            latitude=35.7248416,
            longitude=51.381653,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Tekirdağ",
            state_code="59",
            latitude=41.1121227,
            longitude=27.2676116,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Tel Aviv District",
            state_code="TA",
            latitude=32.0929075,
            longitude=34.8072165,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Israel")][0]),
        ))
        list_of_states.append(State(
            name="Telangana",
            state_code="TG",
            latitude=18.1124372,
            longitude=79.0192997,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Telenești District",
            state_code="TE",
            latitude=47.4983962,
            longitude=28.3676019,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Teleorman County",
            state_code="TR",
            latitude=44.0160491,
            longitude=25.2986628,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Telford and Wrekin",
            state_code="TFW",
            latitude=52.7409916,
            longitude=-2.4868586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Télimélé Prefecture",
            state_code="TE",
            latitude=10.9089364,
            longitude=-13.0299331,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Telšiai County",
            state_code="TE",
            latitude=56.1026616,
            longitude=22.1113915,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Telšiai District Municipality",
            state_code="51",
            latitude=55.9175215,
            longitude=22.345184,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Temburong District",
            state_code="TE",
            latitude=4.6204128,
            longitude=115.141484,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brunei")][0]),
        ))
        list_of_states.append(State(
            name="Temotu Province",
            state_code="TE",
            latitude=-10.686929,
            longitude=166.0623979,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Solomon Islands")][0]),
        ))
        list_of_states.append(State(
            name="Tennessee",
            state_code="TN",
            latitude=35.5174913,
            longitude=-86.5804473,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Tepelenë District",
            state_code="TE",
            latitude=40.2966632,
            longitude=20.0181673,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Teplice",
            state_code="426",
            latitude=50.6584605,
            longitude=13.7513227,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Teramo",
            state_code="TE",
            latitude=42.5895608,
            longitude=13.6362715,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Terengganu",
            state_code="11",
            latitude=5.3116916,
            longitude=103.1324154,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Terni",
            state_code="TR",
            latitude=42.5634534,
            longitude=12.5298028,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Ternopilska oblast",
            state_code="61",
            latitude=49.553517,
            longitude=25.594767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Territoire de Belfort",
            state_code="90",
            latitude=47.6293072,
            longitude=6.66962,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Teruel",
            state_code="TE",
            latitude=40.345041,
            longitude=-1.1184744,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Tērvete Municipality",
            state_code="098",
            latitude=56.4119201,
            longitude=23.3188332,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Tete Province",
            state_code="T",
            latitude=-15.6596056,
            longitude=32.7181375,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Tétouan",
            state_code="TET",
            latitude=35.5888995,
            longitude=-5.3625516,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Tetovo Municipality",
            state_code="76",
            latitude=42.027486,
            longitude=20.9506636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Texas",
            state_code="TX",
            latitude=31.9685988,
            longitude=-99.9018131,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Thaa Atoll",
            state_code="08",
            latitude=2.4311161,
            longitude=73.1821623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Thaba-Tseka District",
            state_code="K",
            latitude=-29.5238975,
            longitude=28.6089752,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lesotho")][0]),
        ))
        list_of_states.append(State(
            name="Thái Bình",
            state_code="20",
            latitude=20.4463471,
            longitude=106.3365828,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Thái Nguyên",
            state_code="69",
            latitude=21.5671559,
            longitude=105.8252038,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Thakurgaon District",
            state_code="64",
            latitude=26.0418392,
            longitude=88.4282616,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Thanh Hóa",
            state_code="21",
            latitude=19.806692,
            longitude=105.7851816,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Tharaka-Nithi",
            state_code="41",
            latitude=-0.2964851,
            longitude=37.7237678,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Thessaloniki Regional Unit",
            state_code="54",
            latitude=40.6400629,
            longitude=22.9444191,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Thiès Region",
            state_code="TH",
            latitude=14.7910052,
            longitude=-16.9358604,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Thimphu District",
            state_code="15",
            latitude=27.4712216,
            longitude=89.6339041,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Thừa Thiên-Huế",
            state_code="26",
            latitude=16.467397,
            longitude=107.5905326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Thurgau",
            state_code="TG",
            latitude=47.6037856,
            longitude=9.0557371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Thuringia",
            state_code="TH",
            latitude=51.0109892,
            longitude=10.845346,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Thurrock",
            state_code="THR",
            latitude=51.4934557,
            longitude=0.3529197,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Thyolo District",
            state_code="TH",
            latitude=-16.1299177,
            longitude=35.1268781,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Tianjin",
            state_code="TJ",
            latitude=39.1252291,
            longitude=117.0153435,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Tiaret",
            state_code="14",
            latitude=35.3708689,
            longitude=1.3217852,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Tibesti",
            state_code="TI",
            latitude=21.3650031,
            longitude=16.912251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Ticino",
            state_code="TI",
            latitude=46.331734,
            longitude=8.8004529,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Tiền Giang",
            state_code="46",
            latitude=10.4493324,
            longitude=106.3420504,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Tierra del Fuego",
            state_code="V",
            latitude=-54.8053998,
            longitude=-68.3242061,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Tigray Region",
            state_code="TI",
            latitude=14.0323336,
            longitude=38.3165725,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ethiopia")][0]),
        ))
        list_of_states.append(State(
            name="Tillabéri Region",
            state_code="6",
            latitude=14.6489525,
            longitude=2.1450245,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Niger")][0]),
        ))
        list_of_states.append(State(
            name="Timimoun",
            state_code="54",
            latitude=29.678906,
            longitude=0.5004608,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Timiș County",
            state_code="TM",
            latitude=45.8138902,
            longitude=21.3331055,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Tindouf",
            state_code="37",
            latitude=27.8063119,
            longitude=-5.7299821,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Tinghir",
            state_code="TIN",
            latitude=31.4850794,
            longitude=-6.2019298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Tipasa",
            state_code="42",
            latitude=36.546265,
            longitude=2.1843285,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Tipperary",
            state_code="TA",
            latitude=52.4737894,
            longitude=-8.1618514,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Tirana County",
            state_code="11",
            latitude=41.2427598,
            longitude=19.8067916,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Tirana District",
            state_code="TR",
            latitude=41.3275459,
            longitude=19.8186982,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Tiris Zemmour",
            state_code="11",
            latitude=24.5773764,
            longitude=-9.9018131,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Tišina Municipality",
            state_code="010",
            latitude=46.6541884,
            longitude=16.0754781,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Tissemsilt",
            state_code="38",
            latitude=35.6053781,
            longitude=1.813098,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Tivat Municipality",
            state_code="19",
            latitude=42.42348,
            longitude=18.7185184,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Tizi Ouzou",
            state_code="15",
            latitude=36.706911,
            longitude=4.2333355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Tiznit",
            state_code="TIZ",
            latitude=29.693392,
            longitude=-9.732157,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Tlaxcala",
            state_code="TLA",
            latitude=19.318154,
            longitude=-98.2374954,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Tlemcen",
            state_code="13",
            latitude=34.6780284,
            longitude=-1.366216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Toa Alta",
            state_code="135",
            latitude=18.3882823,
            longitude=-66.2482237,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Toa Baja",
            state_code="137",
            latitude=18.4444709,
            longitude=-66.2543293,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Toa Baja",
            state_code="TB",
            latitude=18.443889,
            longitude=-66.259722,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Toamasina Province",
            state_code="A",
            latitude=-18.1442811,
            longitude=49.3957836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Madagascar")][0]),
        ))
        list_of_states.append(State(
            name="Tocantins",
            state_code="TO",
            latitude=-10.17528,
            longitude=-48.2982474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Tochigi Prefecture",
            state_code="09",
            latitude=36.6714739,
            longitude=139.8547266,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Togdheer Region",
            state_code="TO",
            latitude=9.4460587,
            longitude=45.2993862,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Tokat",
            state_code="60",
            latitude=40.3902713,
            longitude=36.6251863,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Tokushima Prefecture",
            state_code="36",
            latitude=33.9419655,
            longitude=134.3236557,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Tokyo",
            state_code="13",
            latitude=35.6761919,
            longitude=139.6503106,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Toledo",
            state_code="TO",
            latitude=39.86232,
            longitude=-4.0694692,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Toledo District",
            state_code="TOL",
            latitude=16.2491923,
            longitude=-88.864698,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belize")][0]),
        ))
        list_of_states.append(State(
            name="Toliara Province",
            state_code="U",
            latitude=-23.3516191,
            longitude=43.6854936,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Madagascar")][0]),
        ))
        list_of_states.append(State(
            name="Tolima",
            state_code="TOL",
            latitude=4.0925168,
            longitude=-75.1545381,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Tolmin Municipality",
            state_code="128",
            latitude=46.1857188,
            longitude=13.7319838,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Tolna County",
            state_code="TO",
            latitude=46.4762754,
            longitude=18.5570627,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Tombali Region",
            state_code="TO",
            latitude=11.3632696,
            longitude=-14.9856176,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="Tombouctou Region",
            state_code="6",
            latitude=21.0526706,
            longitude=-3.743509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Tomsk Oblast",
            state_code="TOM",
            latitude=58.8969882,
            longitude=82.67655,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Tongatapu",
            state_code="04",
            latitude=-21.1465968,
            longitude=-175.2515482,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tonga")][0]),
        ))
        list_of_states.append(State(
            name="Toplica District",
            state_code="21",
            latitude=43.1906592,
            longitude=21.3407762,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Torba",
            state_code="TOB",
            latitude=37.07653,
            longitude=27.456573,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vanuatu")][0]),
        ))
        list_of_states.append(State(
            name="Torbay",
            state_code="TOB",
            latitude=50.4392329,
            longitude=-3.5369899,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Torfaen",
            state_code="TOF",
            latitude=51.7002253,
            longitude=-3.0446015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Tororo District",
            state_code="212",
            latitude=0.6870994,
            longitude=34.0641419,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Totonicapán Department",
            state_code="TO",
            latitude=14.9173402,
            longitude=-91.3613923,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Tottori Prefecture",
            state_code="31",
            latitude=35.3573161,
            longitude=133.4066618,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Touggourt",
            state_code="55",
            latitude=33.1248476,
            longitude=5.7832715,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Tougué Prefecture",
            state_code="TO",
            latitude=11.3841583,
            longitude=-11.6157773,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Töv Province",
            state_code="047",
            latitude=47.2124056,
            longitude=106.41541,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Tovuz District",
            state_code="TOV",
            latitude=40.9954523,
            longitude=45.6165907,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Toyama Prefecture",
            state_code="16",
            latitude=36.6958266,
            longitude=137.2137071,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Tozeur",
            state_code="72",
            latitude=33.9789491,
            longitude=8.0465185,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Trà Vinh",
            state_code="51",
            latitude=9.812741,
            longitude=106.2992912,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Trabzon",
            state_code="61",
            latitude=40.799241,
            longitude=39.5847944,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Trafford",
            state_code="TRF",
            latitude=40.3856246,
            longitude=-79.7589347,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Trakai District Municipality",
            state_code="52",
            latitude=54.6379113,
            longitude=24.9346894,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Trang",
            state_code="92",
            latitude=7.5644833,
            longitude=99.6239334,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Trans Nzoia",
            state_code="42",
            latitude=1.0566667,
            longitude=34.9506625,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Transnistria autonomous territorial unit",
            state_code="SN",
            latitude=47.2152972,
            longitude=29.4638054,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Trapani",
            state_code="TP",
            latitude=38.0183116,
            longitude=12.5148265,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Trarza",
            state_code="06",
            latitude=17.8664964,
            longitude=-14.6587821,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Trashigang District",
            state_code="41",
            latitude=27.2566795,
            longitude=91.7538817,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Trat",
            state_code="23",
            latitude=12.2427563,
            longitude=102.5174734,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Trbovlje Municipality",
            state_code="129",
            latitude=46.1503563,
            longitude=15.0453137,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Třebíč",
            state_code="634",
            latitude=49.2147869,
            longitude=15.8795516,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Trebnje Municipality",
            state_code="130",
            latitude=45.9080163,
            longitude=15.0131905,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Treinta y Tres",
            state_code="TT",
            latitude=-33.0685086,
            longitude=-54.2858627,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Trelawny Parish",
            state_code="07",
            latitude=18.3526143,
            longitude=-77.6077865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Trenčín Region",
            state_code="TC",
            latitude=48.8086758,
            longitude=18.2324026,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovakia")][0]),
        ))
        list_of_states.append(State(
            name="Trentino-South Tyrol",
            state_code="32",
            latitude=46.4336662,
            longitude=11.1693296,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Treviso",
            state_code="TV",
            latitude=45.6668517,
            longitude=12.2430617,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Triesen",
            state_code="09",
            latitude=47.1097988,
            longitude=9.5248296,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Triesenberg",
            state_code="10",
            latitude=47.1224511,
            longitude=9.5701985,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Trieste",
            state_code="TS",
            latitude=45.6894823,
            longitude=13.7833072,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Trincomalee District",
            state_code="53",
            latitude=8.6013069,
            longitude=81.1196075,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Trinity Palmetto Point Parish",
            state_code="15",
            latitude=17.3063519,
            longitude=-62.7617837,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Tripoli District",
            state_code="TB",
            latitude=32.6408021,
            longitude=13.2663479,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Tripura",
            state_code="TR",
            latitude=23.9408482,
            longitude=91.9881527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Trnava Region",
            state_code="TA",
            latitude=48.3943898,
            longitude=17.7216205,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovakia")][0]),
        ))
        list_of_states.append(State(
            name="Trnovska Vas Municipality",
            state_code="185",
            latitude=46.5294035,
            longitude=15.8853118,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Troms og Finnmark",
            state_code="54",
            latitude=69.7789067,
            longitude=18.9940184,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Trongsa District",
            state_code="32",
            latitude=27.5002269,
            longitude=90.5080634,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Tropojë District",
            state_code="TP",
            latitude=42.3982151,
            longitude=20.1625955,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Trujillo",
            state_code="T",
            latitude=36.6734343,
            longitude=-121.6287588,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Trujillo Alto",
            state_code="139",
            latitude=18.3546719,
            longitude=-66.0073876,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Trujillo Alto",
            state_code="TA",
            latitude=18.362778,
            longitude=-66.0175,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Trutnov",
            state_code="525",
            latitude=50.5653838,
            longitude=15.9090923,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Tržič Municipality",
            state_code="131",
            latitude=46.3593514,
            longitude=14.3006623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Trzin Municipality",
            state_code="186",
            latitude=46.1298241,
            longitude=14.5577637,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Trøndelag",
            state_code="50",
            latitude=63.5420125,
            longitude=10.9369267,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Tshopo",
            state_code="TO",
            latitude=0.5455462,
            longitude=24.9042208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Tshuapa",
            state_code="TU",
            latitude=-0.9903023,
            longitude=23.0288844,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Tsirang District",
            state_code="21",
            latitude=27.032207,
            longitude=90.1869644,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Tsuen Wan",
            state_code="NTW",
            latitude=22.36281,
            longitude=114.12907,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Tuamasaga",
            state_code="TU",
            latitude=-13.9163592,
            longitude=-171.8224362,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Samoa")][0]),
        ))
        list_of_states.append(State(
            name="Tubas",
            state_code="TBS",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Tucumán",
            state_code="T",
            latitude=-26.8221127,
            longitude=-65.2192903,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Tuen Mun",
            state_code="NTM",
            latitude=22.39163,
            longitude=113.9770885,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Tukums Municipality",
            state_code="099",
            latitude=56.9672868,
            longitude=23.1524379,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Tula Oblast",
            state_code="TUL",
            latitude=54.163768,
            longitude=37.5649507,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Tulcea County",
            state_code="TL",
            latitude=45.0450565,
            longitude=29.0324912,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Tulkarm",
            state_code="TKM",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Tumbes",
            state_code="TUM",
            latitude=-3.5564921,
            longitude=-80.4270885,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Tunapuna-Piarco Regional Corporation",
            state_code="TUP",
            latitude=10.6859096,
            longitude=-61.3035248,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Tunceli",
            state_code="62",
            latitude=39.3073554,
            longitude=39.4387778,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Tungurahua",
            state_code="T",
            latitude=-1.2635284,
            longitude=-78.5660852,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Tunis",
            state_code="11",
            latitude=36.8374946,
            longitude=10.1927389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Turkana",
            state_code="43",
            latitude=3.3122477,
            longitude=35.5657862,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Turkestan Region",
            state_code="YUZ",
            latitude=43.3666958,
            longitude=68.4094405,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="Turnišče Municipality",
            state_code="132",
            latitude=46.6137504,
            longitude=16.32021,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Tuscany",
            state_code="52",
            latitude=43.7710513,
            longitude=11.2486208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Tutong District",
            state_code="TU",
            latitude=4.7140373,
            longitude=114.6667939,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brunei")][0]),
        ))
        list_of_states.append(State(
            name="Tuva Republic",
            state_code="TY",
            latitude=51.8872669,
            longitude=95.6260172,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Tuy Province",
            state_code="TUI",
            latitude=38.888684,
            longitude=-77.004719,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Tuyên Quang",
            state_code="07",
            latitude=21.7767246,
            longitude=105.2280196,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Tuzla Canton",
            state_code="03",
            latitude=44.5343463,
            longitude=18.6972797,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Tver Oblast",
            state_code="TVE",
            latitude=57.0021654,
            longitude=33.9853142,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Tyrol",
            state_code="7",
            latitude=47.2537414,
            longitude=11.601487,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Austria")][0]),
        ))
        list_of_states.append(State(
            name="Tyumen Oblast",
            state_code="TYU",
            latitude=56.9634387,
            longitude=66.948278,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Uaboe District",
            state_code="13",
            latitude=-0.5202222,
            longitude=166.9311761,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nauru")][0]),
        ))
        list_of_states.append(State(
            name="Uasin Gishu",
            state_code="44",
            latitude=0.5527638,
            longitude=35.3027226,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Ubon Ratchathani",
            state_code="34",
            latitude=15.2448453,
            longitude=104.8472995,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Ucayali",
            state_code="UCA",
            latitude=-9.8251183,
            longitude=-73.087749,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Udine",
            state_code="UD",
            latitude=46.1407972,
            longitude=13.1662896,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Udmurt Republic",
            state_code="UD",
            latitude=57.0670218,
            longitude=53.0277948,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Udon Thani",
            state_code="41",
            latitude=17.3646969,
            longitude=102.8158924,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Uherské Hradiště",
            state_code="722",
            latitude=49.0597969,
            longitude=17.4958501,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Uíge Province",
            state_code="UIG",
            latitude=-7.1736732,
            longitude=15.4068079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Ujar District",
            state_code="UCA",
            latitude=40.5067525,
            longitude=47.6489641,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Ukmergė District Municipality",
            state_code="53",
            latitude=55.245265,
            longitude=24.7760749,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Ulcinj Municipality",
            state_code="20",
            latitude=41.9652795,
            longitude=19.3069432,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Ulsan",
            state_code="31",
            latitude=35.5383773,
            longitude=129.3113596,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Ulster",
            state_code="U",
            latitude=54.7616555,
            longitude=-6.9612273,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Ulyanovsk Oblast",
            state_code="ULY",
            latitude=53.9793357,
            longitude=47.7762425,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Umbria",
            state_code="55",
            latitude=42.938004,
            longitude=12.6216211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Umm al-Quwain",
            state_code="UQ",
            latitude=25.5426324,
            longitude=55.5475348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Arab Emirates")][0]),
        ))
        list_of_states.append(State(
            name="Umm Salal Municipality",
            state_code="US",
            latitude=25.4875242,
            longitude=51.396568,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Qatar")][0]),
        ))
        list_of_states.append(State(
            name="Una-Sana Canton",
            state_code="01",
            latitude=44.6503116,
            longitude=16.3171629,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Ungheni District",
            state_code="UN",
            latitude=47.2305767,
            longitude=27.7892661,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="United Kingdom",
            state_code="UKM",
            latitude=55.378051,
            longitude=-3.435973,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="United States Minor Outlying Islands",
            state_code="UM",
            latitude=19.2823192,
            longitude=166.647047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="United States Virgin Islands",
            state_code="VI",
            latitude=18.335765,
            longitude=-64.896335,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Unity",
            state_code="UY",
            latitude=37.7871276,
            longitude=-122.4034079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Upper Austria",
            state_code="4",
            latitude=48.025854,
            longitude=13.9723665,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Austria")][0]),
        ))
        list_of_states.append(State(
            name="Upper Demerara-Berbice",
            state_code="UD",
            latitude=5.3064879,
            longitude=-58.1892921,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guyana")][0]),
        ))
        list_of_states.append(State(
            name="Upper East",
            state_code="UE",
            latitude=10.7082499,
            longitude=-0.9820668,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Upper Nile",
            state_code="NU",
            latitude=9.8894202,
            longitude=32.7181375,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Upper River Division",
            state_code="U",
            latitude=13.4257366,
            longitude=-14.0072348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gambia The")][0]),
        ))
        list_of_states.append(State(
            name="Upper South Province",
            state_code="US",
            latitude=0.2307,
            longitude=73.2794846,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Upper Takutu-Upper Essequibo",
            state_code="UT",
            latitude=2.9239595,
            longitude=-58.7373634,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guyana")][0]),
        ))
        list_of_states.append(State(
            name="Upper West",
            state_code="UW",
            latitude=10.2529757,
            longitude=-2.1450245,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Uppsala County",
            state_code="C",
            latitude=60.0092262,
            longitude=17.2714588,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Uri",
            state_code="UR",
            latitude=41.4860647,
            longitude=-71.5308537,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Uroševac District (Ferizaj)",
            state_code="XUF",
            latitude=42.3701844,
            longitude=21.1483281,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kosovo")][0]),
        ))
        list_of_states.append(State(
            name="Urozgan",
            state_code="URU",
            latitude=32.9271287,
            longitude=66.1415263,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Uşak",
            state_code="64",
            latitude=38.5431319,
            longitude=29.2320784,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Ústecký kraj",
            state_code="42",
            latitude=50.6119037,
            longitude=13.7870086,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Ústí nad Labem",
            state_code="427",
            latitude=50.6119037,
            longitude=13.7870086,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Ústí nad Orlicí",
            state_code="534",
            latitude=49.9721801,
            longitude=16.3996617,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Usulután Department",
            state_code="US",
            latitude=13.4470634,
            longitude=-88.556531,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="Utah",
            state_code="UT",
            latitude=39.3209801,
            longitude=-111.0937311,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Utena County",
            state_code="UT",
            latitude=55.5318969,
            longitude=25.7904699,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Utena District Municipality",
            state_code="54",
            latitude=55.5084614,
            longitude=25.6832642,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Uthai Thani",
            state_code="61",
            latitude=15.3835001,
            longitude=100.0245527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Utrecht",
            state_code="UT",
            latitude=52.0907374,
            longitude=5.1214201,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Uttar Pradesh",
            state_code="UP",
            latitude=26.8467088,
            longitude=80.9461592,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Uttaradit",
            state_code="53",
            latitude=17.6200886,
            longitude=100.0992942,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Uttarakhand",
            state_code="UK",
            latitude=30.066753,
            longitude=79.0192997,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Utuado",
            state_code="141",
            latitude=18.2655095,
            longitude=-66.7004519,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Uusimaa",
            state_code="18",
            latitude=60.21872,
            longitude=25.271621,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Uva Province",
            state_code="8",
            latitude=6.8427612,
            longitude=81.3399414,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Uvs Province",
            state_code="046",
            latitude=49.6449707,
            longitude=93.2736576,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Va'a-o-Fonoti",
            state_code="VF",
            latitude=-13.9470903,
            longitude=-171.5431872,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Samoa")][0]),
        ))
        list_of_states.append(State(
            name="Vaavu Atoll",
            state_code="04",
            latitude=3.3955438,
            longitude=73.5122928,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Vaduz",
            state_code="11",
            latitude=47.1410303,
            longitude=9.5209277,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Vaiņode Municipality",
            state_code="100",
            latitude=56.4154271,
            longitude=21.8513984,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Vaisigano",
            state_code="VS",
            latitude=-13.5413827,
            longitude=-172.7023383,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Samoa")][0]),
        ))
        list_of_states.append(State(
            name="Vaitupu",
            state_code="VAI",
            latitude=-7.4767327,
            longitude=178.6747675,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tuvalu")][0]),
        ))
        list_of_states.append(State(
            name="Vakaga Prefecture",
            state_code="VK",
            latitude=9.5113296,
            longitude=22.2384017,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Val-d'Oise",
            state_code="95",
            latitude=49.0751818,
            longitude=1.8216914,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Val-de-Marne",
            state_code="94",
            latitude=48.7747004,
            longitude=2.3221039,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Valais",
            state_code="VS",
            latitude=46.1904614,
            longitude=7.5449226,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Valandovo Municipality",
            state_code="10",
            latitude=41.3211909,
            longitude=22.5006693,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Vâlcea County",
            state_code="VL",
            latitude=45.0798051,
            longitude=24.0835283,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Vale of Glamorgan",
            state_code="VGL",
            latitude=51.4095958,
            longitude=-3.4848167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Valencia",
            state_code="V",
            latitude=39.4840108,
            longitude=-0.7532809,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Valga County",
            state_code="82",
            latitude=57.9103441,
            longitude=26.1601819,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Valka Municipality",
            state_code="101",
            latitude=57.77439,
            longitude=26.017005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Valladolid",
            state_code="VA",
            latitude=41.6517375,
            longitude=-4.724495,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Valle del Cauca",
            state_code="VAC",
            latitude=3.8008893,
            longitude=-76.6412712,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Valle Department",
            state_code="VA",
            latitude=13.5782936,
            longitude=-87.5791287,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Vallée du Bandama District",
            state_code="VB",
            latitude=8.278978,
            longitude=-4.8935627,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Vallée du Bandama Region",
            state_code="04",
            latitude=8.278978,
            longitude=-4.8935627,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Valletta",
            state_code="60",
            latitude=35.8989085,
            longitude=14.5145528,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Valmiera",
            state_code="VMR",
            latitude=57.5384659,
            longitude=25.4263618,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Valparaíso",
            state_code="VS",
            latitude=-33.047238,
            longitude=-71.6126885,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Valverde Province",
            state_code="27",
            latitude=19.5881221,
            longitude=-70.980331,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Van",
            state_code="65",
            latitude=38.3679417,
            longitude=43.7182787,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Var",
            state_code="83",
            latitude=43.395073,
            longitude=5.7342417,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (19/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
