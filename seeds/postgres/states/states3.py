"""
States Seed #3

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
            name="Beverīna Municipality",
            state_code="017",
            latitude=57.5197109,
            longitude=25.6073654,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Beyla Prefecture",
            state_code="BE",
            latitude=8.9198178,
            longitude=-8.3088441,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Beylagan District",
            state_code="BEY",
            latitude=39.7723073,
            longitude=47.6154166,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Bheri Zone",
            state_code="BH",
            latitude=28.517456,
            longitude=81.7787021,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Bhola District",
            state_code="07",
            latitude=22.1785315,
            longitude=90.7101023,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Bicol",
            state_code="05",
            latitude=13.4209885,
            longitude=123.4136736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Bié Province",
            state_code="BIE",
            latitude=-12.5727907,
            longitude=17.668887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Biella",
            state_code="BI",
            latitude=45.5628176,
            longitude=8.0582717,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Bihar",
            state_code="BR",
            latitude=25.0960742,
            longitude=85.3131194,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Bihor County",
            state_code="BH",
            latitude=47.0157516,
            longitude=22.172266,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Bijelo Polje Municipality",
            state_code="04",
            latitude=43.0846526,
            longitude=19.7115472,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Bilasuvar District",
            state_code="BIL",
            latitude=39.4598833,
            longitude=48.5509813,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Bilecik",
            state_code="11",
            latitude=40.0566555,
            longitude=30.0665236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Biliran",
            state_code="BIL",
            latitude=11.5833152,
            longitude=124.4641848,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Bimini",
            state_code="BI",
            latitude=24.6415325,
            longitude=-79.8506226,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Bingöl",
            state_code="12",
            latitude=39.0626354,
            longitude=40.7696095,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Bình Dương",
            state_code="57",
            latitude=11.3254024,
            longitude=106.477017,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Bình Phước",
            state_code="58",
            latitude=11.7511894,
            longitude=106.7234639,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Bình Thuận",
            state_code="40",
            latitude=11.0903703,
            longitude=108.0720781,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Bình Định",
            state_code="31",
            latitude=14.1665324,
            longitude=108.902683,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Biobío",
            state_code="BI",
            latitude=-37.4464428,
            longitude=-72.1416132,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Bioko Norte Province",
            state_code="BN",
            latitude=3.6595072,
            longitude=8.7921836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Equatorial Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Bioko Sur Province",
            state_code="BS",
            latitude=3.4209785,
            longitude=8.6160674,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Equatorial Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Biombo Region",
            state_code="BM",
            latitude=11.8529061,
            longitude=-15.7351171,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="Birgu",
            state_code="03",
            latitude=35.8879214,
            longitude=14.522562,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Birkirkara",
            state_code="04",
            latitude=35.8954706,
            longitude=14.4665072,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Birmingham",
            state_code="BIR",
            latitude=33.5185892,
            longitude=-86.8103567,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Birštonas Municipality",
            state_code="05",
            latitude=54.5669664,
            longitude=24.0093098,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Biržai District Municipality",
            state_code="06",
            latitude=56.2017719,
            longitude=24.7560118,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Birżebbuġa",
            state_code="05",
            latitude=35.8135989,
            longitude=14.5247463,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Bishkek",
            state_code="GB",
            latitude=42.8746212,
            longitude=74.5697617,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kyrgyzstan")][0]),
        ))
        list_of_states.append(State(
            name="Biskra",
            state_code="07",
            latitude=34.8449437,
            longitude=5.7248567,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Bistrica ob Sotli Municipality",
            state_code="149",
            latitude=46.0565579,
            longitude=15.6625947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Bistrița-Năsăud County",
            state_code="BN",
            latitude=47.2486107,
            longitude=24.5322814,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Bitlis",
            state_code="13",
            latitude=38.6523133,
            longitude=42.4202028,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Bitola Municipality",
            state_code="04",
            latitude=41.0363302,
            longitude=21.3321974,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Bizerte",
            state_code="23",
            latitude=37.1609397,
            longitude=9.634135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Bizkaia",
            state_code="BI",
            latitude=43.2192199,
            longitude=-3.2111087,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Bjelovar-Bilogora",
            state_code="07",
            latitude=45.8987972,
            longitude=16.8423093,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Black Point",
            state_code="BP",
            latitude=41.3951024,
            longitude=-71.4650556,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Black River",
            state_code="BL",
            latitude=-20.3708492,
            longitude=57.3948649,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Blackburn with Darwen",
            state_code="BBD",
            latitude=53.6957522,
            longitude=-2.4682985,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Blackpool",
            state_code="BPL",
            latitude=53.8175053,
            longitude=-3.0356748,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Blaenau Gwent County Borough",
            state_code="BGW",
            latitude=51.7875779,
            longitude=-3.2043931,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Blagoevgrad Province",
            state_code="01",
            latitude=42.0208614,
            longitude=23.0943356,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Blansko",
            state_code="641",
            latitude=49.3648502,
            longitude=16.6477552,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Blantyre District",
            state_code="BL",
            latitude=-15.6778541,
            longitude=34.9506625,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Bled Municipality",
            state_code="003",
            latitude=46.3683266,
            longitude=14.1145798,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Blekinge County",
            state_code="K",
            latitude=56.28333333,
            longitude=15.11666666,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Blida",
            state_code="09",
            latitude=36.531123,
            longitude=2.8976254,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Bloke Municipality",
            state_code="150",
            latitude=45.7728141,
            longitude=14.5063459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Blue Nile",
            state_code="NB",
            latitude=47.598673,
            longitude=-122.334419,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Boa Vista",
            state_code="BV",
            latitude=38.743466,
            longitude=-120.7304297,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Boaco",
            state_code="BO",
            latitude=12.469284,
            longitude=-85.6614682,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Bobonaro Municipality",
            state_code="BO",
            latitude=-8.9655406,
            longitude=125.2587964,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Timor-Leste")][0]),
        ))
        list_of_states.append(State(
            name="Bocas del Toro Province",
            state_code="1",
            latitude=9.4165521,
            longitude=-82.5207787,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Boe District",
            state_code="06",
            latitude=39.0732776,
            longitude=-94.5710498,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nauru")][0]),
        ))
        list_of_states.append(State(
            name="Boeotia Regional Unit",
            state_code="03",
            latitude=38.3663664,
            longitude=23.0965064,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Boffa Prefecture",
            state_code="BF",
            latitude=10.1808254,
            longitude=-14.0391615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Bogdanci Municipality",
            state_code="05",
            latitude=41.1869616,
            longitude=22.5960268,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Bogotá D.C.",
            state_code="DC",
            latitude=4.2820415,
            longitude=-74.5027042,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Bogovinje Municipality",
            state_code="06",
            latitude=41.9236371,
            longitude=20.9163887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Bogra District",
            state_code="03",
            latitude=24.8510402,
            longitude=89.3697225,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Bohinj Municipality",
            state_code="004",
            latitude=46.3005652,
            longitude=13.9427195,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Bohol",
            state_code="BOH",
            latitude=9.8499911,
            longitude=124.1435427,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Boké Prefecture",
            state_code="BK",
            latitude=11.0847379,
            longitude=-14.3791912,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Boké Region",
            state_code="B",
            latitude=11.1864672,
            longitude=-14.1001326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Bokeo Province",
            state_code="BK",
            latitude=20.2872662,
            longitude=100.7097867,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Bolama Region",
            state_code="BL",
            latitude=11.1480591,
            longitude=-16.1345705,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="Bolikhamsai Province",
            state_code="BL",
            latitude=18.4362924,
            longitude=104.4723301,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Bolívar",
            state_code="BOL",
            latitude=8.6704382,
            longitude=-74.0300122,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Bolívar",
            state_code="B",
            latitude=-1.7095828,
            longitude=-79.0450429,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Bolívar",
            state_code="F",
            latitude=37.6144838,
            longitude=-93.4104749,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Bolton",
            state_code="BOL",
            latitude=44.3726476,
            longitude=-72.8787625,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Bolu",
            state_code="14",
            latitude=40.5759766,
            longitude=31.5788086,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Bomet",
            state_code="02",
            latitude=-0.8015009,
            longitude=35.3027226,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Bomi County",
            state_code="BM",
            latitude=6.7562926,
            longitude=-10.8451467,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Bonaire",
            state_code="BQ1",
            latitude=12.2018902,
            longitude=-68.2623822,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bonaire, Sint Eustatius and Saba")][0]),
        ))
        list_of_states.append(State(
            name="Bonaire",
            state_code="BQ1",
            latitude=12.2018902,
            longitude=-68.2623822,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Bong County",
            state_code="BG",
            latitude=6.8295019,
            longitude=-9.3673084,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Bono",
            state_code="BO",
            latitude=7.65,
            longitude=-2.5,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Bono East",
            state_code="BE",
            latitude=7.75,
            longitude=-1.05,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Boquerón Department",
            state_code="19",
            latitude=-21.7449254,
            longitude=-60.9540073,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Bor District",
            state_code="14",
            latitude=44.0698918,
            longitude=22.0985086,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Bordj Baji Mokhtar",
            state_code="52",
            latitude=22.966335,
            longitude=-3.9472732,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Bordj Bou Arréridj",
            state_code="34",
            latitude=36.0739925,
            longitude=4.7630271,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Borgo Maggiore",
            state_code="06",
            latitude=43.9574882,
            longitude=12.4552546,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "San Marino")][0]),
        ))
        list_of_states.append(State(
            name="Borgou Department",
            state_code="BO",
            latitude=9.5340864,
            longitude=2.7779813,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Borkou",
            state_code="BO",
            latitude=17.8688845,
            longitude=18.8076195,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Borno",
            state_code="BO",
            latitude=11.8846356,
            longitude=13.1519665,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Borovnica Municipality",
            state_code="005",
            latitude=45.9044525,
            longitude=14.3824189,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Borsod-Abaúj-Zemplén",
            state_code="BZ",
            latitude=48.2939401,
            longitude=20.6934112,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Bosilovo Municipality",
            state_code="07",
            latitude=41.4904864,
            longitude=22.7867174,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Bosnian Podrinje Canton",
            state_code="05",
            latitude=43.68749,
            longitude=18.8244394,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Botoșani County",
            state_code="BT",
            latitude=47.8924042,
            longitude=26.7591781,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Bouches-du-Rhône",
            state_code="13",
            latitude=43.5403865,
            longitude=4.4613829,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Boucle du Mouhoun Region",
            state_code="01",
            latitude=12.4166,
            longitude=-3.4195527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Bouenza Department",
            state_code="11",
            latitude=-4.1128079,
            longitude=13.7289167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Bougainville",
            state_code="NSB",
            latitude=-6.3753919,
            longitude=155.3807101,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Bougouriba Province",
            state_code="BGR",
            latitude=10.8722646,
            longitude=-3.3388917,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Bouïra",
            state_code="10",
            latitude=36.3691846,
            longitude=3.9006194,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Boujdour (EH)",
            state_code="BOD",
            latitude=26.1252493,
            longitude=-14.4847347,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Boulemane",
            state_code="BOM",
            latitude=33.3625159,
            longitude=-4.7303397,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Boulgou",
            state_code="BLG",
            latitude=11.4336766,
            longitude=-0.3748354,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Boumerdès",
            state_code="35",
            latitude=36.6839559,
            longitude=3.6217802,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Bourgogne-Franche-Comté",
            state_code="BFC",
            latitude=47.2805127,
            longitude=4.9994372,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Bournemouth",
            state_code="BMH",
            latitude=50.719164,
            longitude=-1.880769,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Bovec Municipality",
            state_code="006",
            latitude=46.3380495,
            longitude=13.5524174,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Boyacá",
            state_code="BOY",
            latitude=5.454511,
            longitude=-73.362003,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Bracknell Forest",
            state_code="BRC",
            latitude=51.4153828,
            longitude=-0.7536495,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Bradford",
            state_code="BRD",
            latitude=53.795984,
            longitude=-1.759398,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Braga",
            state_code="03",
            latitude=41.550388,
            longitude=-8.4261301,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Bragança",
            state_code="04",
            latitude=41.8061652,
            longitude=-6.7567427,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Brahmanbaria District",
            state_code="04",
            latitude=23.9608181,
            longitude=91.1115014,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Braila",
            state_code="BR",
            latitude=45.2652463,
            longitude=27.9594714,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Brakna",
            state_code="05",
            latitude=17.2317561,
            longitude=-13.1740348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Brandenburg",
            state_code="BB",
            latitude=52.4125287,
            longitude=12.5316444,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Braničevo District",
            state_code="11",
            latitude=44.6982246,
            longitude=21.5446775,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Braslovče Municipality",
            state_code="151",
            latitude=46.2836192,
            longitude=15.041832,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Brașov County",
            state_code="BV",
            latitude=45.7781844,
            longitude=25.22258,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Bratislava Region",
            state_code="BL",
            latitude=48.3118304,
            longitude=17.1973299,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovakia")][0]),
        ))
        list_of_states.append(State(
            name="Brava",
            state_code="BR",
            latitude=40.9897778,
            longitude=-73.6835715,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Brazzaville",
            state_code="BZV",
            latitude=-4.2633597,
            longitude=15.2428853,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Brčko District",
            state_code="BRC",
            latitude=44.8405944,
            longitude=18.742153,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Brda Municipality",
            state_code="007",
            latitude=45.9975652,
            longitude=13.5270474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Břeclav",
            state_code="644",
            latitude=48.75314,
            longitude=16.8825169,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Bremen",
            state_code="HB",
            latitude=53.0792962,
            longitude=8.8016936,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Brescia",
            state_code="BS",
            latitude=45.5415526,
            longitude=10.2118019,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Brest Region",
            state_code="BR",
            latitude=52.5296641,
            longitude=25.460648,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belarus")][0]),
        ))
        list_of_states.append(State(
            name="Bretagne",
            state_code="BRE",
            latitude=48.2020471,
            longitude=-2.9326435,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Brežice Municipality",
            state_code="009",
            latitude=45.9041096,
            longitude=15.5943639,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Brezovica Municipality",
            state_code="008",
            latitude=45.9559351,
            longitude=14.4349952,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Briceni District",
            state_code="BR",
            latitude=48.3632022,
            longitude=27.0750398,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Bridgend County Borough",
            state_code="BGE",
            latitude=51.5083199,
            longitude=-3.5812075,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Brighton and Hove",
            state_code="BNH",
            latitude=50.8226288,
            longitude=-0.137047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Brindisi",
            state_code="BR",
            latitude=40.6112663,
            longitude=17.763621,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="British Columbia",
            state_code="BC",
            latitude=53.7266683,
            longitude=-127.6476205,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Brno-město",
            state_code="642",
            latitude=49.1950602,
            longitude=16.6068371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Brno-venkov",
            state_code="643",
            latitude=49.1250138,
            longitude=16.4558824,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Brocēni Municipality",
            state_code="018",
            latitude=56.7347541,
            longitude=22.6357371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Brod-Posavina",
            state_code="12",
            latitude=45.2637951,
            longitude=17.3264562,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Brokopondo District",
            state_code="BR",
            latitude=4.7710247,
            longitude=-55.0493375,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Suriname")][0]),
        ))
        list_of_states.append(State(
            name="Brunei-Muara District",
            state_code="BM",
            latitude=4.9311206,
            longitude=114.9516869,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brunei")][0]),
        ))
        list_of_states.append(State(
            name="Bruntál",
            state_code="801",
            latitude=49.9881767,
            longitude=17.4636941,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Brussels-Capital Region",
            state_code="BRU",
            latitude=50.8503463,
            longitude=4.3517211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="Brvenica Municipality",
            state_code="08",
            latitude=41.9681482,
            longitude=20.9819586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Bryansk Oblast",
            state_code="BRY",
            latitude=53.0408599,
            longitude=33.26909,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Bua",
            state_code="02",
            latitude=43.0964584,
            longitude=-89.50088,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Buada District",
            state_code="07",
            latitude=-0.5328777,
            longitude=166.9268541,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nauru")][0]),
        ))
        list_of_states.append(State(
            name="Bubanza Province",
            state_code="BB",
            latitude=-3.1572403,
            longitude=29.3714909,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Bucharest",
            state_code="B",
            latitude=44.4267674,
            longitude=26.1025384,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Buckinghamshire",
            state_code="BKM",
            latitude=51.8072204,
            longitude=-0.8127664,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Budaka District",
            state_code="217",
            latitude=1.1016277,
            longitude=33.9303991,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Budapest",
            state_code="BU",
            latitude=47.497912,
            longitude=19.040235,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Bududa District",
            state_code="218",
            latitude=1.0029693,
            longitude=34.3338123,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Budva Municipality",
            state_code="05",
            latitude=42.314072,
            longitude=18.8313832,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Bueng Kan",
            state_code="38",
            latitude=18.3609104,
            longitude=103.6464463,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Buenos Aires",
            state_code="B",
            latitude=-37.2017285,
            longitude=-59.8410697,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Bugiri District",
            state_code="201",
            latitude=0.5316127,
            longitude=33.7517723,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Buhweju District",
            state_code="420",
            latitude=-0.2911359,
            longitude=30.2974199,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Buikwe District",
            state_code="117",
            latitude=0.3144046,
            longitude=32.9888319,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Bujumbura Mairie Province",
            state_code="BM",
            latitude=-3.3884141,
            longitude=29.3482646,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Bujumbura Rural Province",
            state_code="BL",
            latitude=-3.5090144,
            longitude=29.464359,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Bukedea District",
            state_code="219",
            latitude=1.3556898,
            longitude=34.1086793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Bukhara Region",
            state_code="BU",
            latitude=40.2504162,
            longitude=63.2032151,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Bukidnon",
            state_code="BUK",
            latitude=8.0515054,
            longitude=124.9229946,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Bukomansimbi District",
            state_code="118",
            latitude=-0.1432752,
            longitude=31.6054893,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Bukwo District",
            state_code="220",
            latitude=1.2818651,
            longitude=34.7298765,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Bulacan",
            state_code="BUL",
            latitude=14.7942735,
            longitude=120.8799008,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Bulambuli District",
            state_code="225",
            latitude=1.4798846,
            longitude=34.3754414,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Bulawayo Province",
            state_code="BU",
            latitude=-20.1489505,
            longitude=28.5331038,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zimbabwe")][0]),
        ))
        list_of_states.append(State(
            name="Bulgan Province",
            state_code="067",
            latitude=48.9690913,
            longitude=102.8831723,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Buliisa District",
            state_code="416",
            latitude=2.0299607,
            longitude=31.5370003,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Bulqizë District",
            state_code="BU",
            latitude=41.4942587,
            longitude=20.2147157,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Bumthang District",
            state_code="33",
            latitude=27.641839,
            longitude=90.6773046,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Bundibugyo District",
            state_code="401",
            latitude=0.6851763,
            longitude=30.0202964,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Bungoma",
            state_code="03",
            latitude=0.5695252,
            longitude=34.5583766,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Bunyangabu District",
            state_code="430",
            latitude=0.4870918,
            longitude=30.2051096,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Burdur",
            state_code="15",
            latitude=37.4612669,
            longitude=30.0665236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Burgas Province",
            state_code="02",
            latitude=42.5048,
            longitude=27.4626079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Burgenland",
            state_code="1",
            latitude=47.1537165,
            longitude=16.2688797,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Austria")][0]),
        ))
        list_of_states.append(State(
            name="Burgos",
            state_code="BU",
            latitude=42.3380758,
            longitude=-3.5812692,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Buri Ram",
            state_code="31",
            latitude=14.9951003,
            longitude=103.1115915,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Bursa",
            state_code="16",
            latitude=40.0655459,
            longitude=29.2320784,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Burtnieki Municipality",
            state_code="019",
            latitude=57.6949004,
            longitude=25.2764777,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Bururi Province",
            state_code="BR",
            latitude=-3.9006851,
            longitude=29.5107708,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Bury",
            state_code="BUR",
            latitude=53.5933498,
            longitude=-2.2966054,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Busan",
            state_code="26",
            latitude=35.1795543,
            longitude=129.0756416,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Bushehr",
            state_code="18",
            latitude=28.7620739,
            longitude=51.5150077,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Bushenyi District",
            state_code="402",
            latitude=-0.4870918,
            longitude=30.2051096,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Busia",
            state_code="04",
            latitude=0.4346506,
            longitude=34.2421597,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Busia District",
            state_code="202",
            latitude=0.4044731,
            longitude=34.0195827,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Butaleja District",
            state_code="221",
            latitude=0.8474922,
            longitude=33.8411288,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Butambala District",
            state_code="119",
            latitude=0.17425,
            longitude=32.1064668,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Butebo District",
            state_code="233",
            latitude=1.2141124,
            longitude=33.9080896,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Butel Municipality",
            state_code="09",
            latitude=42.0895068,
            longitude=21.463361,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Butha-Buthe District",
            state_code="B",
            latitude=-28.7653754,
            longitude=28.2468148,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lesotho")][0]),
        ))
        list_of_states.append(State(
            name="Buvuma District",
            state_code="120",
            latitude=-0.3764912,
            longitude=33.258793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Buyende District",
            state_code="226",
            latitude=1.2413682,
            longitude=33.1239049,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Buzău County",
            state_code="BZ",
            latitude=45.3350912,
            longitude=26.7107578,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Cà Mau",
            state_code="59",
            latitude=9.1526728,
            longitude=105.1960795,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Caaguazú",
            state_code="5",
            latitude=-25.4645818,
            longitude=-56.013851,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Caazapá",
            state_code="6",
            latitude=-26.1827713,
            longitude=-56.3712327,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Cabañas Department",
            state_code="CA",
            latitude=13.8648288,
            longitude=-88.7493998,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="Cabinda Province",
            state_code="CAB",
            latitude=-5.0248749,
            longitude=12.3463875,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Cabo Delgado Province",
            state_code="P",
            latitude=-12.3335474,
            longitude=39.3206241,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Cabo Rojo",
            state_code="023",
            latitude=18.0866265,
            longitude=-67.1457347,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Caceres",
            state_code="CC",
            latitude=39.4716313,
            longitude=-6.4257384,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Cacheu Region",
            state_code="CA",
            latitude=12.0551416,
            longitude=-16.0640179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="Cádiz",
            state_code="CA",
            latitude=36.5163851,
            longitude=-6.2999767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Caerphilly County Borough",
            state_code="CAY",
            latitude=51.6604465,
            longitude=-3.2178724,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Cagayan",
            state_code="CAG",
            latitude=18.2489629,
            longitude=121.8787833,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Cagayan Valley",
            state_code="02",
            latitude=16.9753758,
            longitude=121.8107079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Caguas",
            state_code="025",
            latitude=18.2387995,
            longitude=-66.035249,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Caguas",
            state_code="CG",
            latitude=18.23333333,
            longitude=-66.03333333,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Cahul District",
            state_code="CA",
            latitude=45.8939404,
            longitude=28.1890275,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Čair Municipality",
            state_code="79",
            latitude=41.9930355,
            longitude=21.4365318,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Cairo",
            state_code="C",
            latitude=29.9537564,
            longitude=31.5370003,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Cajamarca",
            state_code="CAJ",
            latitude=-7.1617465,
            longitude=-78.5127855,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Cakaudrove",
            state_code="03",
            latitude=-16.5814105,
            longitude=179.5120084,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Calabarzon",
            state_code="40",
            latitude=14.1007803,
            longitude=121.0793705,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Calabria",
            state_code="78",
            latitude=39.3087714,
            longitude=16.3463791,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Călărași County",
            state_code="CL",
            latitude=44.3658715,
            longitude=26.7548607,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Călărași District",
            state_code="CL",
            latitude=47.286946,
            longitude=28.274531,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Caldas",
            state_code="CAL",
            latitude=5.29826,
            longitude=-75.2479061,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Calderdale",
            state_code="CLD",
            latitude=53.7247845,
            longitude=-1.8658357,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="California",
            state_code="CA",
            latitude=36.778261,
            longitude=-119.4179324,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Callao",
            state_code="CAL",
            latitude=-12.0508491,
            longitude=-77.1259843,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Caltanissetta",
            state_code="CL",
            latitude=37.486013,
            longitude=14.0614982,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Calvados",
            state_code="14",
            latitude=49.0903514,
            longitude=-0.9170648,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Camagüey Province",
            state_code="09",
            latitude=21.2167247,
            longitude=-77.7452081,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Camarines Norte",
            state_code="CAN",
            latitude=14.1390265,
            longitude=122.7633036,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Camarines Sur",
            state_code="CAS",
            latitude=13.5250197,
            longitude=123.3486147,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Cambridgeshire",
            state_code="CAM",
            latitude=52.2052973,
            longitude=0.1218195,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Camiguin",
            state_code="CAM",
            latitude=9.1732164,
            longitude=124.7298765,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Campania",
            state_code="72",
            latitude=40.6670887,
            longitude=15.1068113,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Campeche",
            state_code="CAM",
            latitude=19.8301251,
            longitude=-90.5349087,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Campobasso",
            state_code="CB",
            latitude=41.6738865,
            longitude=14.7520939,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Camuy",
            state_code="027",
            latitude=18.483833,
            longitude=-66.8448994,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Cần Thơ",
            state_code="CT",
            latitude=10.0341851,
            longitude=105.7225507,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Çanakkale",
            state_code="17",
            latitude=40.0510104,
            longitude=26.9852422,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Cañar",
            state_code="F",
            latitude=-2.5589315,
            longitude=-78.9388191,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Canarias",
            state_code="CN",
            latitude=28.2916,
            longitude=16.6291,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Canaries",
            state_code="12",
            latitude=28.2915637,
            longitude=-16.6291304,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Canelones",
            state_code="CA",
            latitude=-34.5408717,
            longitude=-55.93076,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Canillo",
            state_code="02",
            latitude=42.5978249,
            longitude=1.6566377,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Andorra")][0]),
        ))
        list_of_states.append(State(
            name="Canindeyú",
            state_code="14",
            latitude=-24.1378735,
            longitude=-55.6689636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Çankırı",
            state_code="18",
            latitude=40.5369073,
            longitude=33.5883893,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Cankova Municipality",
            state_code="152",
            latitude=46.718237,
            longitude=16.0197222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Cankuzo Province",
            state_code="CA",
            latitude=-3.1527788,
            longitude=30.6199895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (3/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
