"""
States Seed #2

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
            name="Arges",
            state_code="AG",
            latitude=45.0722527,
            longitude=24.8142726,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Argolis Regional Unit",
            state_code="11",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Argyll and Bute",
            state_code="AGB",
            latitude=56.4006214,
            longitude=-5.480748,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ariana",
            state_code="12",
            latitude=36.9922751,
            longitude=10.1255164,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Arica y Parinacota",
            state_code="AP",
            latitude=-18.5940485,
            longitude=-69.4784541,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Ariège",
            state_code="09",
            latitude=42.9434783,
            longitude=0.9404864,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Arima",
            state_code="ARI",
            latitude=46.7931604,
            longitude=-71.2584311,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Arizona",
            state_code="AZ",
            latitude=34.0489281,
            longitude=-111.0937311,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Arkansas",
            state_code="AR",
            latitude=35.20105,
            longitude=-91.8318334,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Arkhangai Province",
            state_code="073",
            latitude=47.8971101,
            longitude=100.7240165,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Arkhangelsk",
            state_code="ARK",
            latitude=64.5458549,
            longitude=40.5505769,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Armagh City and District Council",
            state_code="ARM",
            latitude=54.3932592,
            longitude=-6.4563401,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Armagh, Banbridge and Craigavon",
            state_code="ABC",
            latitude=54.3932592,
            longitude=-6.4563401,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Armavir Region",
            state_code="AV",
            latitude=40.1554631,
            longitude=44.0372446,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Armenia")][0]),
        ))
        list_of_states.append(State(
            name="Arroyo",
            state_code="015",
            latitude=17.996422,
            longitude=-66.0924879,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Arta Region",
            state_code="AR",
            latitude=11.5255528,
            longitude=42.8479474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Djibouti")][0]),
        ))
        list_of_states.append(State(
            name="Artemisa Province",
            state_code="15",
            latitude=22.7522903,
            longitude=-82.9931607,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Artibonite",
            state_code="AR",
            latitude=19.362902,
            longitude=-72.4258145,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Haiti")][0]),
        ))
        list_of_states.append(State(
            name="Artigas",
            state_code="AR",
            latitude=-30.6175112,
            longitude=-56.9594559,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Artvin",
            state_code="08",
            latitude=41.078664,
            longitude=41.7628223,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Arua District",
            state_code="303",
            latitude=2.9959846,
            longitude=31.1710389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Arunachal Pradesh",
            state_code="AR",
            latitude=28.2179994,
            longitude=94.7277528,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Arusha",
            state_code="01",
            latitude=-3.3869254,
            longitude=36.6829927,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="As-Suwayda",
            state_code="SU",
            latitude=32.7989156,
            longitude=36.7819505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Ascension Island",
            state_code="SH-AC",
            latitude=-7.9467166,
            longitude=-14.3559158,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ascoli Piceno",
            state_code="AP",
            latitude=42.8638933,
            longitude=13.5899733,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Ash Sharqiyah North",
            state_code="SS",
            latitude=22.7141196,
            longitude=58.5308064,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Oman")][0]),
        ))
        list_of_states.append(State(
            name="Ash Sharqiyah Region",
            state_code="SH",
            latitude=22.7141196,
            longitude=58.5308064,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Oman")][0]),
        ))
        list_of_states.append(State(
            name="Ash Sharqiyah South",
            state_code="SJ",
            latitude=22.0158249,
            longitude=59.3251922,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Oman")][0]),
        ))
        list_of_states.append(State(
            name="Ashanti",
            state_code="AH",
            latitude=6.7470436,
            longitude=-1.5208624,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Ashgabat",
            state_code="S",
            latitude=37.9600766,
            longitude=58.3260629,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkmenistan")][0]),
        ))
        list_of_states.append(State(
            name="Assa-Zag (EH-partial)",
            state_code="ASZ",
            latitude=28.1402395,
            longitude=-9.7232673,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Assaba",
            state_code="03",
            latitude=16.7759558,
            longitude=-11.5248055,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Assam",
            state_code="AS",
            latitude=26.2006043,
            longitude=92.9375739,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Astara District",
            state_code="AST",
            latitude=38.4937845,
            longitude=48.6944365,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Asti",
            state_code="AT",
            latitude=44.9007652,
            longitude=8.2064315,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Astrakhan Oblast",
            state_code="AST",
            latitude=46.1321166,
            longitude=48.0610115,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Asturias",
            state_code="O",
            latitude=43.3613953,
            longitude=-5.8593267,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Asuncion",
            state_code="ASU",
            latitude=-25.2968297,
            longitude=-57.6806623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Aswan",
            state_code="ASN",
            latitude=23.6966498,
            longitude=32.7181375,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Asyut",
            state_code="AST",
            latitude=27.2133831,
            longitude=31.4456179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Atacama",
            state_code="AT",
            latitude=-27.5660558,
            longitude=-70.050314,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Atakora Department",
            state_code="AK",
            latitude=10.7954931,
            longitude=1.6760691,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Atlántico",
            state_code="ATL",
            latitude=10.6966159,
            longitude=-74.8741045,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Atlántida Department",
            state_code="AT",
            latitude=15.6696283,
            longitude=-87.1422895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Atlantique Department",
            state_code="AQ",
            latitude=6.6588391,
            longitude=2.2236667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Attapeu Province",
            state_code="AT",
            latitude=14.93634,
            longitude=107.1011931,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Attard",
            state_code="01",
            latitude=35.8904967,
            longitude=14.4199322,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Attica Region",
            state_code="I",
            latitude=38.0457568,
            longitude=23.8584737,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Atua",
            state_code="AT",
            latitude=-13.9787053,
            longitude=-171.6254283,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Samoa")][0]),
        ))
        list_of_states.append(State(
            name="Atyrau Region",
            state_code="ATY",
            latitude=47.1076188,
            longitude=51.914133,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="Au Cap",
            state_code="04",
            latitude=-4.7059723,
            longitude=55.5081012,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Aube",
            state_code="10",
            latitude=48.3197547,
            longitude=3.5637104,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Auce Municipality",
            state_code="010",
            latitude=56.460168,
            longitude=22.9054781,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Auckland Region",
            state_code="AUK",
            latitude=-36.6675328,
            longitude=174.7733325,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Aude",
            state_code="11",
            latitude=43.054114,
            longitude=1.9038476,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Aurora",
            state_code="AUR",
            latitude=36.970891,
            longitude=-93.717979,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Australian Capital Territory",
            state_code="ACT",
            latitude=-35.4734679,
            longitude=149.0123679,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Australia")][0]),
        ))
        list_of_states.append(State(
            name="Autonomous Region in Muslim Mindanao",
            state_code="14",
            latitude=6.9568313,
            longitude=124.2421597,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Autonomous Republic of Crimea",
            state_code="43",
            latitude=44.952117,
            longitude=34.102417,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Auvergne-Rhône-Alpes",
            state_code="ARA",
            latitude=45.4471431,
            longitude=4.3852507,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Aveiro",
            state_code="01",
            latitude=40.7209023,
            longitude=-8.5721016,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Avellino",
            state_code="AV",
            latitude=40.996451,
            longitude=15.1258955,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Aveyron",
            state_code="12",
            latitude=44.3156362,
            longitude=2.0852379,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Ávila",
            state_code="AV",
            latitude=40.6934511,
            longitude=-4.8935627,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Awdal Region",
            state_code="AW",
            latitude=10.6334285,
            longitude=43.329466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Ayacucho",
            state_code="AYA",
            latitude=-13.1638737,
            longitude=-74.2235641,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Aydın",
            state_code="09",
            latitude=37.8117033,
            longitude=28.4863963,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Ayeyarwady Region",
            state_code="07",
            latitude=17.0342125,
            longitude=95.2266675,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Azad Kashmir",
            state_code="JK",
            latitude=33.9259055,
            longitude=73.7810334,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Pakistan")][0]),
        ))
        list_of_states.append(State(
            name="Azilal",
            state_code="AZI",
            latitude=32.004262,
            longitude=-6.5783387,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Azua Province",
            state_code="02",
            latitude=18.4552709,
            longitude=-70.7380928,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Azuay",
            state_code="A",
            latitude=-2.8943068,
            longitude=-78.9968344,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Ba",
            state_code="01",
            latitude=36.0613893,
            longitude=-95.8005872,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Bà Rịa-Vũng Tàu",
            state_code="43",
            latitude=10.5417397,
            longitude=107.2429976,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Baalbek-Hermel",
            state_code="BH",
            latitude=34.2658556,
            longitude=36.3498097,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lebanon")][0]),
        ))
        list_of_states.append(State(
            name="Babek District",
            state_code="BAB",
            latitude=39.1507613,
            longitude=45.4485368,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Babīte Municipality",
            state_code="012",
            latitude=56.954155,
            longitude=23.945399,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Babylon",
            state_code="BB",
            latitude=32.468191,
            longitude=44.5501935,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Bắc Giang",
            state_code="54",
            latitude=21.2819921,
            longitude=106.1974769,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Bắc Kạn",
            state_code="53",
            latitude=22.3032923,
            longitude=105.876004,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Bạc Liêu",
            state_code="55",
            latitude=9.2940027,
            longitude=105.7215663,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Bắc Ninh",
            state_code="56",
            latitude=21.121444,
            longitude=106.1110501,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Bacău County",
            state_code="BC",
            latitude=46.3258184,
            longitude=26.662378,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Bács-Kiskun",
            state_code="BK",
            latitude=46.5661437,
            longitude=19.4272464,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Badajoz",
            state_code="BA",
            latitude=38.8793748,
            longitude=-7.0226983,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Badakhshan",
            state_code="BDS",
            latitude=36.7347725,
            longitude=70.8119953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Baden-Württemberg",
            state_code="BW",
            latitude=48.6616037,
            longitude=9.3501336,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Badghis",
            state_code="BDG",
            latitude=35.1671339,
            longitude=63.7695384,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Badulla District",
            state_code="81",
            latitude=6.9934009,
            longitude=81.0549815,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Bafatá",
            state_code="BA",
            latitude=12.1735243,
            longitude=-14.652952,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="Bafing Region",
            state_code="17",
            latitude=8.3252047,
            longitude=-7.5247243,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Bagerhat District",
            state_code="05",
            latitude=22.6602436,
            longitude=89.7895478,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Baghdad",
            state_code="BG",
            latitude=33.3152618,
            longitude=44.3660653,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Baghlan",
            state_code="BGL",
            latitude=36.1789026,
            longitude=68.7453064,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Bagmati Zone",
            state_code="BA",
            latitude=28.0367577,
            longitude=85.4375574,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Bago",
            state_code="02",
            latitude=17.3220711,
            longitude=96.4663286,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Bahadia",
            state_code="33",
            latitude=23.7898712,
            longitude=90.1671483,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Bahia",
            state_code="BA",
            latitude=-11.409874,
            longitude=-41.280857,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Bahr el Gazel",
            state_code="BG",
            latitude=14.7702266,
            longitude=16.912251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Baie Lazare",
            state_code="06",
            latitude=-4.7482525,
            longitude=55.4859363,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Baie Sainte Anne",
            state_code="07",
            latitude=47.05259,
            longitude=-64.9524579,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Baikonur",
            state_code="BAY",
            latitude=45.9645851,
            longitude=63.3052428,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="Baiti District",
            state_code="05",
            latitude=-0.510431,
            longitude=166.9275744,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nauru")][0]),
        ))
        list_of_states.append(State(
            name="Baja California",
            state_code="BCN",
            latitude=30.8406338,
            longitude=-115.2837585,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Baja California Sur",
            state_code="BCS",
            latitude=26.0444446,
            longitude=-111.6660725,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Baja Verapaz Department",
            state_code="BV",
            latitude=15.1255867,
            longitude=-90.3748354,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Baker Island",
            state_code="UM-81",
            latitude=0.1936266,
            longitude=-176.476908,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Baker Island",
            state_code="81",
            latitude=0.1936266,
            longitude=-176.476908,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States Minor Outlying Islands")][0]),
        ))
        list_of_states.append(State(
            name="Bakool",
            state_code="BK",
            latitude=4.3657221,
            longitude=44.0960311,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Baku",
            state_code="BA",
            latitude=40.4092617,
            longitude=49.8670924,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Balaka District",
            state_code="BA",
            latitude=-15.0506595,
            longitude=35.0828588,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Balakan District",
            state_code="BAL",
            latitude=41.7037509,
            longitude=46.4044213,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Baldone Municipality",
            state_code="013",
            latitude=56.74246,
            longitude=24.3911544,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Balé Province",
            state_code="BAL",
            latitude=11.7820602,
            longitude=-3.0175712,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Bali",
            state_code="BA",
            latitude=-8.3405389,
            longitude=115.0919509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Balıkesir",
            state_code="10",
            latitude=39.7616782,
            longitude=28.1122679,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Balkan Region",
            state_code="B",
            latitude=41.8101472,
            longitude=21.0937311,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkmenistan")][0]),
        ))
        list_of_states.append(State(
            name="Balkh",
            state_code="BAL",
            latitude=36.7550603,
            longitude=66.8975372,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Ballymena Borough",
            state_code="BLA",
            latitude=54.86426,
            longitude=-6.2791074,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ballymoney",
            state_code="BLY",
            latitude=55.0704888,
            longitude=-6.5173708,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Balochistan",
            state_code="BA",
            latitude=28.4907332,
            longitude=65.0957792,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Pakistan")][0]),
        ))
        list_of_states.append(State(
            name="Balqa",
            state_code="BA",
            latitude=32.0366806,
            longitude=35.728848,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jordan")][0]),
        ))
        list_of_states.append(State(
            name="Bălți Municipality",
            state_code="BA",
            latitude=47.7539947,
            longitude=27.9184148,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Baltinava Municipality",
            state_code="014",
            latitude=56.9458468,
            longitude=27.6441066,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Balvi Municipality",
            state_code="015",
            latitude=57.132624,
            longitude=27.2646685,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Balzan",
            state_code="02",
            latitude=35.8957414,
            longitude=14.4534065,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Balzers",
            state_code="01",
            latitude=42.0528357,
            longitude=-88.0366848,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Bam Province",
            state_code="BAM",
            latitude=13.446133,
            longitude=-1.5983959,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Bamako",
            state_code="BKO",
            latitude=12.6392316,
            longitude=-8.0028892,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Bamingui-Bangoran Prefecture",
            state_code="BB",
            latitude=8.2733455,
            longitude=20.7122465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Bamyan",
            state_code="BAM",
            latitude=34.8100067,
            longitude=67.8212104,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Banaadir",
            state_code="BN",
            latitude=2.1187375,
            longitude=45.3369459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Banbridge",
            state_code="BNB",
            latitude=54.348729,
            longitude=-6.2704803,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Bandarban District",
            state_code="01",
            latitude=21.8311002,
            longitude=92.3686321,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Bangkok",
            state_code="10",
            latitude=13.7563309,
            longitude=100.5017651,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Bangui",
            state_code="BGF",
            latitude=4.3946735,
            longitude=18.5581899,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Banjul",
            state_code="B",
            latitude=13.4548761,
            longitude=-16.5790323,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gambia The")][0]),
        ))
        list_of_states.append(State(
            name="Banská Bystrica Region",
            state_code="BC",
            latitude=48.5312499,
            longitude=19.382874,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovakia")][0]),
        ))
        list_of_states.append(State(
            name="Banteay Meanchey",
            state_code="1",
            latitude=13.7531914,
            longitude=102.989615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Banten",
            state_code="BT",
            latitude=-6.4058172,
            longitude=106.0640179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Banwa Province",
            state_code="BAN",
            latitude=12.1323053,
            longitude=-4.1513764,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Baoruco Province",
            state_code="03",
            latitude=18.4879898,
            longitude=-71.4182249,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Bar Municipality",
            state_code="02",
            latitude=42.1278119,
            longitude=19.140438,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Barahona Province",
            state_code="04",
            latitude=18.2139066,
            longitude=-71.1043759,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Baranya",
            state_code="BA",
            latitude=46.0484585,
            longitude=18.2719173,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Barbuda",
            state_code="10",
            latitude=17.6266242,
            longitude=-61.7713028,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Antigua and Barbuda")][0]),
        ))
        list_of_states.append(State(
            name="Barcelona",
            state_code="B",
            latitude=41.3926679,
            longitude=2.1401891,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Barceloneta",
            state_code="017",
            latitude=41.3801061,
            longitude=2.1896957,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Barda District",
            state_code="BAR",
            latitude=40.3706555,
            longitude=47.1378909,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Barguna District",
            state_code="02",
            latitude=22.0952915,
            longitude=90.1120696,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Bari",
            state_code="BR",
            latitude=41.1171432,
            longitude=16.8718715,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Barima-Waini",
            state_code="BA",
            latitude=7.4882419,
            longitude=-59.6564494,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guyana")][0]),
        ))
        list_of_states.append(State(
            name="Barinas",
            state_code="E",
            latitude=8.6231498,
            longitude=-70.2371045,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Baringo",
            state_code="01",
            latitude=0.8554988,
            longitude=36.0893406,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Barisal District",
            state_code="06",
            latitude=22.7022098,
            longitude=90.3696316,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Barisal Division",
            state_code="A",
            latitude=22.3811131,
            longitude=90.3371889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Barlavento Islands",
            state_code="B",
            latitude=16.8236845,
            longitude=-23.9934881,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Barletta-Andria-Trani",
            state_code="BT",
            latitude=41.2004543,
            longitude=16.2051484,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Barnsley",
            state_code="BNS",
            latitude=34.2994956,
            longitude=-84.9845809,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Barranquitas",
            state_code="019",
            latitude=18.1866242,
            longitude=-66.3062802,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Bartın",
            state_code="74",
            latitude=41.5810509,
            longitude=32.4609794,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Bas-Rhin",
            state_code="67",
            latitude=48.5986444,
            longitude=7.0266676,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Bas-Sassandra District",
            state_code="BS",
            latitude=5.2798356,
            longitude=-6.1526985,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Bas-Sassandra Region",
            state_code="09",
            latitude=5.3567916,
            longitude=-6.7493993,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Bas-Uélé",
            state_code="BU",
            latitude=3.9901009,
            longitude=24.9042208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Basarabeasca District",
            state_code="BS",
            latitude=46.423706,
            longitude=28.8935492,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Basel-Land",
            state_code="BL",
            latitude=47.4418122,
            longitude=7.7644002,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Basel-Stadt",
            state_code="BS",
            latitude=47.566667,
            longitude=7.6,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Basilan",
            state_code="BAS",
            latitude=6.4296349,
            longitude=121.9870165,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Basilicata",
            state_code="77",
            latitude=40.6430766,
            longitude=15.9699878,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Basra",
            state_code="BA",
            latitude=30.5114252,
            longitude=47.8296253,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Basse-Kotto Prefecture",
            state_code="BK",
            latitude=4.8719319,
            longitude=21.2845025,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Bataan",
            state_code="BAN",
            latitude=14.6416842,
            longitude=120.4818446,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Batanes",
            state_code="BTN",
            latitude=20.4485074,
            longitude=121.9708129,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Batangas",
            state_code="BTG",
            latitude=13.7564651,
            longitude=121.0583076,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Bath and North East Somerset",
            state_code="BAS",
            latitude=51.3250102,
            longitude=-2.4766241,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Batha",
            state_code="BA",
            latitude=13.9371775,
            longitude=18.4276047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Batken Region",
            state_code="B",
            latitude=39.9721425,
            longitude=69.8597406,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kyrgyzstan")][0]),
        ))
        list_of_states.append(State(
            name="Batman",
            state_code="72",
            latitude=37.8362496,
            longitude=41.3605739,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Batna",
            state_code="05",
            latitude=35.5965954,
            longitude=5.8987139,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Battambang",
            state_code="2",
            latitude=13.0286971,
            longitude=102.989615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Batticaloa District",
            state_code="51",
            latitude=7.8292781,
            longitude=81.4718387,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Baucau Municipality",
            state_code="BA",
            latitude=-8.4714308,
            longitude=126.4575991,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Timor-Leste")][0]),
        ))
        list_of_states.append(State(
            name="Bauchi",
            state_code="BA",
            latitude=10.7760624,
            longitude=9.9991943,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Bauska Municipality",
            state_code="016",
            latitude=56.4101868,
            longitude=24.2000689,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Bavaria",
            state_code="BY",
            latitude=48.7904472,
            longitude=11.4978895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Bay",
            state_code="BY",
            latitude=37.0365534,
            longitude=-95.6174767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Bay Islands Department",
            state_code="IB",
            latitude=16.4826614,
            longitude=-85.8793252,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Bay of Plenty Region",
            state_code="BOP",
            latitude=-37.4233917,
            longitude=176.7416374,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Bayamón",
            state_code="021",
            latitude=18.389396,
            longitude=-66.1653224,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Bayamon",
            state_code="BY",
            latitude=18.17777778,
            longitude=-66.11333333,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Bayan-Ölgii Province",
            state_code="071",
            latitude=48.3983254,
            longitude=89.6625915,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Bayankhongor Province",
            state_code="069",
            latitude=45.1526707,
            longitude=100.1073667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Bayburt",
            state_code="69",
            latitude=40.26032,
            longitude=40.228048,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Bayelsa",
            state_code="BY",
            latitude=4.7719071,
            longitude=6.0698526,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Bazèga Province",
            state_code="BAZ",
            latitude=11.9767692,
            longitude=-1.443469,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Beau Vallon",
            state_code="08",
            latitude=-4.6210967,
            longitude=55.4277802,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Béchar",
            state_code="08",
            latitude=31.6238098,
            longitude=-2.2162443,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Bedford",
            state_code="BDF",
            latitude=32.844017,
            longitude=-97.1430671,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Beheira",
            state_code="BH",
            latitude=30.8480986,
            longitude=30.3435506,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Beijing",
            state_code="BJ",
            latitude=39.9041999,
            longitude=116.4073963,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Beirut",
            state_code="BA",
            latitude=33.8886106,
            longitude=35.4954772,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lebanon")][0]),
        ))
        list_of_states.append(State(
            name="Beja",
            state_code="02",
            latitude=37.9687786,
            longitude=-7.87216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Béja",
            state_code="31",
            latitude=35.1722716,
            longitude=8.8307626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Béjaïa",
            state_code="06",
            latitude=36.7515258,
            longitude=5.0556837,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Békés",
            state_code="BE",
            latitude=46.6704899,
            longitude=21.0434996,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Békéscsaba",
            state_code="BC",
            latitude=46.6735939,
            longitude=21.0877309,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Bel Air",
            state_code="09",
            latitude=34.1002455,
            longitude=-118.459463,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Bel Ombre",
            state_code="10",
            latitude=-20.5010095,
            longitude=57.4259624,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Belait District",
            state_code="BE",
            latitude=4.3750749,
            longitude=114.6192899,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brunei")][0]),
        ))
        list_of_states.append(State(
            name="Belfast district",
            state_code="BFS",
            latitude=54.6170366,
            longitude=-5.9531861,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Belgorod Oblast",
            state_code="BEL",
            latitude=50.7106926,
            longitude=37.7533377,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Belgrade",
            state_code="00",
            latitude=44.786568,
            longitude=20.4489216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Belize District",
            state_code="BZ",
            latitude=17.5677679,
            longitude=-88.4016041,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belize")][0]),
        ))
        list_of_states.append(State(
            name="Belluno",
            state_code="BL",
            latitude=46.2497659,
            longitude=12.1969565,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Beltinci Municipality",
            state_code="002",
            latitude=46.6079153,
            longitude=16.2365127,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Ben Arous",
            state_code="13",
            latitude=36.6435606,
            longitude=10.2151578,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Bến Tre",
            state_code="50",
            latitude=10.2433556,
            longitude=106.375551,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Bender Municipality",
            state_code="BD",
            latitude=46.8227551,
            longitude=29.4620101,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Benedikt Municipality",
            state_code="148",
            latitude=46.6155841,
            longitude=15.8957281,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Benešov",
            state_code="201",
            latitude=49.6900828,
            longitude=14.7764399,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Benevento",
            state_code="BN",
            latitude=41.2035093,
            longitude=14.7520939,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Benghazi",
            state_code="BA",
            latitude=32.1194242,
            longitude=20.0867909,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Bengkulu",
            state_code="BE",
            latitude=-3.7928451,
            longitude=102.2607641,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Bengo Province",
            state_code="BGO",
            latitude=-9.1042257,
            longitude=13.7289167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Benguela Province",
            state_code="BGU",
            latitude=-12.8003744,
            longitude=13.914399,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Benguet",
            state_code="BEN",
            latitude=16.5577257,
            longitude=120.8039474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Béni Abbès",
            state_code="53",
            latitude=30.0831042,
            longitude=-2.8345052,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Beni Department",
            state_code="B",
            latitude=-14.3782747,
            longitude=-65.0957792,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bolivia")][0]),
        ))
        list_of_states.append(State(
            name="Béni Mellal",
            state_code="BEM",
            latitude=32.342443,
            longitude=-6.375799,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Béni Mellal-Khénifra",
            state_code="05",
            latitude=32.5719184,
            longitude=-6.0679194,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Beni Suef",
            state_code="BNS",
            latitude=28.8938837,
            longitude=31.4456179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Benishangul-Gumuz Region",
            state_code="BE",
            latitude=10.7802889,
            longitude=35.5657862,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ethiopia")][0]),
        ))
        list_of_states.append(State(
            name="Benslimane",
            state_code="BES",
            latitude=33.6189698,
            longitude=-7.1305536,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Benue",
            state_code="BE",
            latitude=7.3369024,
            longitude=8.7403687,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Beqaa",
            state_code="BI",
            latitude=33.8462662,
            longitude=35.9019489,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lebanon")][0]),
        ))
        list_of_states.append(State(
            name="Berane Municipality",
            state_code="03",
            latitude=42.8257289,
            longitude=19.9020509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Berat County",
            state_code="01",
            latitude=40.6953012,
            longitude=20.0449662,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Berat District",
            state_code="BR",
            latitude=40.7086377,
            longitude=19.9437314,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Berea District",
            state_code="D",
            latitude=41.3661614,
            longitude=-81.8543026,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lesotho")][0]),
        ))
        list_of_states.append(State(
            name="Bergamo",
            state_code="BG",
            latitude=45.6982642,
            longitude=9.6772698,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Berkane",
            state_code="BER",
            latitude=34.8840876,
            longitude=-2.341887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Berlin",
            state_code="BE",
            latitude=52.5200066,
            longitude=13.404954,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Bern",
            state_code="BE",
            latitude=46.7988621,
            longitude=7.7080701,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Beroun",
            state_code="202",
            latitude=49.9573428,
            longitude=13.9840715,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Berovo Municipality",
            state_code="03",
            latitude=41.6661929,
            longitude=22.762883,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Berrechid",
            state_code="BRR",
            latitude=33.2602523,
            longitude=-7.5984837,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Berry Islands",
            state_code="BY",
            latitude=25.6250042,
            longitude=-77.8252203,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Bethlehem",
            state_code="BTH",
            latitude=31.7053996,
            longitude=35.1936877,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (2/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
