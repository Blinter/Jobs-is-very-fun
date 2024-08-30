"""
States Seed #8

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
            name="Ica",
            state_code="ICA",
            latitude=42.3528832,
            longitude=-71.0430097,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Ida-Viru County",
            state_code="44",
            latitude=59.2592663,
            longitude=27.4136535,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Idaho",
            state_code="ID",
            latitude=44.0682019,
            longitude=-114.7420408,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Idlib",
            state_code="ID",
            latitude=35.8268798,
            longitude=36.6957216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Idrija Municipality",
            state_code="036",
            latitude=46.0040939,
            longitude=13.9775493,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Iecava Municipality",
            state_code="034",
            latitude=56.5986793,
            longitude=24.1996272,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Ifrane",
            state_code="IFR",
            latitude=33.5228062,
            longitude=-5.1109552,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Ifugao",
            state_code="IFU",
            latitude=16.8330792,
            longitude=121.1710389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Ig Municipality",
            state_code="037",
            latitude=45.9588868,
            longitude=14.5270528,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Iganga District",
            state_code="203",
            latitude=0.6600137,
            longitude=33.4831906,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Iğdır",
            state_code="76",
            latitude=39.8879841,
            longitude=44.0048365,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Ignalina District Municipality",
            state_code="09",
            latitude=55.4090342,
            longitude=26.3284893,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Ijuw District",
            state_code="10",
            latitude=-0.5202767,
            longitude=166.9571046,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nauru")][0]),
        ))
        list_of_states.append(State(
            name="Iklin",
            state_code="19",
            latitude=35.9098774,
            longitude=14.4577732,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Ikšķile Municipality",
            state_code="035",
            latitude=56.8373667,
            longitude=24.4974745,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Ilam",
            state_code="16",
            latitude=33.2957618,
            longitude=46.670534,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Île-de-France",
            state_code="IDF",
            latitude=48.8499198,
            longitude=2.6370411,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Ilfov County",
            state_code="IF",
            latitude=44.535548,
            longitude=26.2324886,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Ilinden Municipality",
            state_code="34",
            latitude=41.9957443,
            longitude=21.5676975,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Ille-et-Vilaine",
            state_code="35",
            latitude=48.1762484,
            longitude=-2.2130401,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Illinois",
            state_code="IL",
            latitude=40.6331249,
            longitude=-89.3985283,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Illizi",
            state_code="33",
            latitude=26.1690005,
            longitude=8.4842465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Ilocos",
            state_code="01",
            latitude=16.0832144,
            longitude=120.6199895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Ilocos Norte",
            state_code="ILN",
            latitude=18.1647281,
            longitude=120.7115592,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Ilocos Sur",
            state_code="ILS",
            latitude=17.2278664,
            longitude=120.5739579,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Iloilo",
            state_code="ILI",
            latitude=10.7201501,
            longitude=122.5621063,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Ilūkste Municipality",
            state_code="036",
            latitude=55.9782547,
            longitude=26.2965088,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Imathia Regional Unit",
            state_code="53",
            latitude=40.6060067,
            longitude=22.1430215,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Imbabura",
            state_code="I",
            latitude=0.3499768,
            longitude=-78.1260129,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Imereti",
            state_code="IM",
            latitude=42.230108,
            longitude=42.9008664,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Imishli District",
            state_code="IMI",
            latitude=39.8694686,
            longitude=48.0665218,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Imo",
            state_code="IM",
            latitude=5.5720122,
            longitude=7.0588219,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Imperia",
            state_code="IM",
            latitude=43.941866,
            longitude=7.8286368,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="In Guezzam",
            state_code="58",
            latitude=20.3864323,
            longitude=4.7789394,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="In Salah",
            state_code="57",
            latitude=27.2149229,
            longitude=1.8484396,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Inagua",
            state_code="IN",
            latitude=21.0656066,
            longitude=-73.323708,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Incheon",
            state_code="28",
            latitude=37.4562557,
            longitude=126.7052062,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Inchiri",
            state_code="12",
            latitude=20.0280561,
            longitude=-15.4068079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Inčukalns Municipality",
            state_code="037",
            latitude=57.0994342,
            longitude=24.685557,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Independencia",
            state_code="10",
            latitude=32.6335748,
            longitude=-115.4289294,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Indiana",
            state_code="IN",
            latitude=40.2671941,
            longitude=-86.1349019,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Indre",
            state_code="36",
            latitude=46.811755,
            longitude=0.9755523,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Indre-et-Loire",
            state_code="37",
            latitude=47.2228582,
            longitude=0.1489619,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Inezgane-Ait Melloul",
            state_code="INE",
            latitude=30.3509098,
            longitude=-9.389511,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Inhambane Province",
            state_code="I",
            latitude=-22.8527997,
            longitude=34.5508758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Inner Mongolia",
            state_code="NM",
            latitude=43.37822,
            longitude=115.0594815,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Innlandet",
            state_code="34",
            latitude=61.1935787,
            longitude=5.5083266,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Insular Region",
            state_code="I",
            latitude=37.09024,
            longitude=-95.712891,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Equatorial Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Intibucá Department",
            state_code="IN",
            latitude=14.372734,
            longitude=-88.2461183,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Inverclyde",
            state_code="IVC",
            latitude=55.9316569,
            longitude=-4.6800158,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ioannina Regional Unit",
            state_code="33",
            latitude=39.6650288,
            longitude=20.8537466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Ioba Province",
            state_code="IOB",
            latitude=11.0562034,
            longitude=-3.0175712,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Ionian Islands Region",
            state_code="F",
            latitude=37.9694898,
            longitude=21.3802372,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Iowa",
            state_code="IA",
            latitude=41.8780025,
            longitude=-93.097702,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Irbid",
            state_code="IR",
            latitude=32.5569636,
            longitude=35.8478965,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jordan")][0]),
        ))
        list_of_states.append(State(
            name="Iringa",
            state_code="04",
            latitude=-7.7887442,
            longitude=35.5657862,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Irkutsk",
            state_code="IRK",
            latitude=52.2854834,
            longitude=104.2890222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Isabel Province",
            state_code="IS",
            latitude=-8.0592353,
            longitude=159.1447081,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Solomon Islands")][0]),
        ))
        list_of_states.append(State(
            name="Isabela",
            state_code="ISA",
            latitude=18.5007759,
            longitude=-67.0243462,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Isabela",
            state_code="071",
            latitude=16.9753758,
            longitude=121.8107079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Isère",
            state_code="38",
            latitude=45.2892271,
            longitude=4.9902355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Isernia",
            state_code="IS",
            latitude=41.5891555,
            longitude=14.1930918,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Isfahan",
            state_code="10",
            latitude=33.2771073,
            longitude=52.3613378,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Ishikawa Prefecture",
            state_code="17",
            latitude=36.3260317,
            longitude=136.5289653,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Isingiro District",
            state_code="418",
            latitude=-0.843543,
            longitude=30.8039474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Isiolo",
            state_code="09",
            latitude=0.3524352,
            longitude=38.4849923,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Isla de la Juventud",
            state_code="99",
            latitude=21.7084737,
            longitude=-82.8220232,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Islamabad Capital Territory",
            state_code="IS",
            latitude=33.7204997,
            longitude=73.0405277,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Pakistan")][0]),
        ))
        list_of_states.append(State(
            name="Islands",
            state_code="NIS",
            latitude=22.26114,
            longitude=113.94608,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Islas Baleares",
            state_code="PM",
            latitude=39.3587759,
            longitude=2.7356328,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Isle of Wight",
            state_code="IOW",
            latitude=50.6938479,
            longitude=-1.304734,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Isles of Scilly",
            state_code="IOS",
            latitude=49.9277261,
            longitude=-6.3274966,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ismailia",
            state_code="IS",
            latitude=30.5830934,
            longitude=32.2653887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Ismailli District",
            state_code="ISM",
            latitude=40.7429936,
            longitude=48.2125556,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Isparta",
            state_code="32",
            latitude=38.0211464,
            longitude=31.0793705,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Issyk-Kul Region",
            state_code="Y",
            latitude=42.1859428,
            longitude=77.5619419,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kyrgyzstan")][0]),
        ))
        list_of_states.append(State(
            name="İstanbul",
            state_code="34",
            latitude=41.1634302,
            longitude=28.7664408,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Istria",
            state_code="18",
            latitude=45.1286455,
            longitude=13.901542,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Itapúa",
            state_code="7",
            latitude=-26.7923623,
            longitude=-55.6689636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Ituri",
            state_code="IT",
            latitude=1.5957682,
            longitude=29.4179324,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Ivančna Gorica Municipality",
            state_code="039",
            latitude=45.9395841,
            longitude=14.8047626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Ivano-Frankivska oblast",
            state_code="26",
            latitude=48.922633,
            longitude=24.711117,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Ivanovo Oblast",
            state_code="IVA",
            latitude=57.1056854,
            longitude=41.4830084,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Iwate Prefecture",
            state_code="03",
            latitude=39.5832989,
            longitude=141.2534574,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Izabal Department",
            state_code="IZ",
            latitude=15.4976517,
            longitude=-88.864698,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="İzmir",
            state_code="35",
            latitude=38.3591693,
            longitude=27.2676116,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Izola Municipality",
            state_code="040",
            latitude=45.5313557,
            longitude=13.6664649,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Jabal al Akhdar",
            state_code="JA",
            latitude=23.1856081,
            longitude=57.3713879,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Jabal al Gharbi District",
            state_code="JG",
            latitude=30.2638032,
            longitude=12.8054753,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Jablanica District",
            state_code="23",
            latitude=42.948156,
            longitude=21.8129321,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Jablonec nad Nisou",
            state_code="512",
            latitude=50.7220528,
            longitude=15.1703135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Jabrayil District",
            state_code="CAB",
            latitude=39.2645544,
            longitude=46.9621562,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Jaén",
            state_code="J",
            latitude=37.7800931,
            longitude=-3.8143745,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Jafara",
            state_code="JI",
            latitude=32.4525904,
            longitude=12.9435536,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Jaffna District",
            state_code="41",
            latitude=9.6930468,
            longitude=80.1651854,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Jalal-Abad Region",
            state_code="J",
            latitude=41.106808,
            longitude=72.8988069,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kyrgyzstan")][0]),
        ))
        list_of_states.append(State(
            name="Jalapa Department",
            state_code="JA",
            latitude=14.6121446,
            longitude=-89.9626799,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Jalilabad District",
            state_code="CAL",
            latitude=39.2051632,
            longitude=48.5100604,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Jalisco",
            state_code="JAL",
            latitude=20.6595382,
            longitude=-103.3494376,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Jamalpur District",
            state_code="21",
            latitude=25.0830926,
            longitude=89.7853218,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Jambi",
            state_code="JA",
            latitude=-1.6101229,
            longitude=103.6131203,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Jambyl Region",
            state_code="ZHA",
            latitude=44.2220308,
            longitude=72.3657967,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="Jammu and Kashmir",
            state_code="JK",
            latitude=33.277839,
            longitude=75.3412179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Jämtland County",
            state_code="0",
            latitude=63.283062,
            longitude=14.238281,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Jan Mayen",
            state_code="22",
            latitude=71.031818,
            longitude=-8.2920346,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Janakpur Zone",
            state_code="JA",
            latitude=27.2110899,
            longitude=86.0121573,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Järva County",
            state_code="51",
            latitude=58.8866713,
            longitude=25.5000624,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Jarvis Island",
            state_code="UM-86",
            latitude=-0.3743503,
            longitude=-159.9967206,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Jarvis Island",
            state_code="86",
            latitude=-0.3743503,
            longitude=-159.9967206,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States Minor Outlying Islands")][0]),
        ))
        list_of_states.append(State(
            name="Jász-Nagykun-Szolnok County",
            state_code="JN",
            latitude=47.2555579,
            longitude=20.5232456,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Jaunjelgava Municipality",
            state_code="038",
            latitude=56.5283659,
            longitude=25.3921443,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Jaunpiebalga Municipality",
            state_code="039",
            latitude=57.1433471,
            longitude=25.9951888,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Jaunpils Municipality",
            state_code="040",
            latitude=56.7314194,
            longitude=23.0125616,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Jawa Barat",
            state_code="JB",
            latitude=-7.090911,
            longitude=107.668887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Jawa Tengah",
            state_code="JT",
            latitude=-7.150975,
            longitude=110.1402594,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Jawa Timur",
            state_code="JI",
            latitude=-7.5360639,
            longitude=112.2384017,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Jayuya",
            state_code="073",
            latitude=18.2185674,
            longitude=-66.5915617,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Jegunovce Municipality",
            state_code="35",
            latitude=42.074072,
            longitude=21.1220478,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Jeju",
            state_code="49",
            latitude=33.9568278,
            longitude=-84.13135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Jēkabpils",
            state_code="JKB",
            latitude=56.501455,
            longitude=25.878299,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Jēkabpils Municipality",
            state_code="042",
            latitude=56.291932,
            longitude=25.9812017,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Jelgava",
            state_code="JEL",
            latitude=56.6511091,
            longitude=23.7213541,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Jelgava Municipality",
            state_code="041",
            latitude=56.5895689,
            longitude=23.6610481,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Jendouba",
            state_code="32",
            latitude=36.7181862,
            longitude=8.7481167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Jenin",
            state_code="JEN",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Jerada",
            state_code="JRA",
            latitude=34.3061791,
            longitude=-2.1794136,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Jerash",
            state_code="JA",
            latitude=32.2747237,
            longitude=35.8960954,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jordan")][0]),
        ))
        list_of_states.append(State(
            name="Jericho and Al Aghwar",
            state_code="JRH",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Jerusalem",
            state_code="JEM",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Jerusalem District",
            state_code="JM",
            latitude=31.7648243,
            longitude=34.994751,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Israel")][0]),
        ))
        list_of_states.append(State(
            name="Jesenice Municipality",
            state_code="041",
            latitude=46.4367047,
            longitude=14.0526057,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Jeseník",
            state_code="711",
            latitude=50.2246249,
            longitude=17.1980471,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Jessore District",
            state_code="22",
            latitude=23.1634014,
            longitude=89.2181664,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Jewish Autonomous Oblast",
            state_code="YEV",
            latitude=48.4808147,
            longitude=131.7657367,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Jezersko Municipality",
            state_code="163",
            latitude=46.3942794,
            longitude=14.4985559,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Jhalokati District",
            state_code="25",
            latitude=22.57208,
            longitude=90.1869644,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Jharkhand",
            state_code="JH",
            latitude=23.6101808,
            longitude=85.2799354,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Jhenaidah District",
            state_code="23",
            latitude=23.5449873,
            longitude=89.1726031,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Jiangsu",
            state_code="JS",
            latitude=33.1401715,
            longitude=119.7889248,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Jiangxi",
            state_code="JX",
            latitude=27.0874564,
            longitude=114.9042208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Jičín",
            state_code="522",
            latitude=50.4353325,
            longitude=15.361044,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Jigawa",
            state_code="JI",
            latitude=12.228012,
            longitude=9.5615867,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Jihlava",
            state_code="632",
            latitude=49.3983782,
            longitude=15.5870415,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Jihočeský kraj",
            state_code="31",
            latitude=48.9457789,
            longitude=14.4416055,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Jihomoravský kraj",
            state_code="64",
            latitude=48.9544528,
            longitude=16.7676899,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Jijel",
            state_code="18",
            latitude=36.7179681,
            longitude=5.9832577,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Jilin",
            state_code="JL",
            latitude=43.837883,
            longitude=126.549572,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Jindřichův Hradec",
            state_code="313",
            latitude=49.1444823,
            longitude=15.0061389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Jinja District",
            state_code="204",
            latitude=0.5343743,
            longitude=33.3037143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Jinotega",
            state_code="JI",
            latitude=13.0883907,
            longitude=-85.9993997,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Jiwaka Province",
            state_code="JWK",
            latitude=-5.8691154,
            longitude=144.6972774,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Jizan",
            state_code="09",
            latitude=17.1738176,
            longitude=42.7076107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Jizzakh Region",
            state_code="JI",
            latitude=40.4706415,
            longitude=67.5708536,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Jõgeva County",
            state_code="49",
            latitude=58.7506143,
            longitude=26.3604878,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Johnston Atoll",
            state_code="UM-67",
            latitude=16.7295035,
            longitude=-169.5336477,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Johnston Atoll",
            state_code="67",
            latitude=16.7295035,
            longitude=-169.5336477,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States Minor Outlying Islands")][0]),
        ))
        list_of_states.append(State(
            name="Johor",
            state_code="01",
            latitude=1.4853682,
            longitude=103.7618154,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Jonava District Municipality",
            state_code="10",
            latitude=55.0727242,
            longitude=24.2793337,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Jonglei State",
            state_code="JG",
            latitude=7.1819619,
            longitude=32.3560952,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Joniškis District Municipality",
            state_code="11",
            latitude=56.236073,
            longitude=23.6136579,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Jönköping County",
            state_code="F",
            latitude=57.3708434,
            longitude=14.3439174,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Jowzjan",
            state_code="JOW",
            latitude=36.8969692,
            longitude=65.6658568,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Joypurhat District",
            state_code="24",
            latitude=25.0947349,
            longitude=89.0944937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Juana Díaz",
            state_code="075",
            latitude=18.0534372,
            longitude=-66.5075079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Jufra",
            state_code="JU",
            latitude=27.9835135,
            longitude=16.912251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Jujuy",
            state_code="Y",
            latitude=-24.1843397,
            longitude=-65.302177,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Julfa District",
            state_code="CUL",
            latitude=38.9604983,
            longitude=45.6292939,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Juncos",
            state_code="077",
            latitude=18.2274558,
            longitude=-65.920997,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Junín",
            state_code="JUN",
            latitude=-11.1581925,
            longitude=-75.9926306,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Jura",
            state_code="39",
            latitude=46.7828741,
            longitude=5.1691844,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Jura",
            state_code="JU",
            latitude=47.3444474,
            longitude=7.1430608,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Jurbarkas District Municipality",
            state_code="12",
            latitude=55.077407,
            longitude=22.7419569,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Jūrmala",
            state_code="JUR",
            latitude=56.947079,
            longitude=23.6168485,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Juršinci Municipality",
            state_code="042",
            latitude=46.4898651,
            longitude=15.980923,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Jutiapa Department",
            state_code="JU",
            latitude=14.1930802,
            longitude=-89.9253233,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Kaabong District",
            state_code="318",
            latitude=3.5126215,
            longitude=33.9750018,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kaafu Atoll",
            state_code="26",
            latitude=4.4558979,
            longitude=73.5594128,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Kabale District",
            state_code="404",
            latitude=-1.2493084,
            longitude=30.0665236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kabardino-Balkar Republic",
            state_code="KB",
            latitude=43.3932469,
            longitude=43.5628498,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kabarole District",
            state_code="405",
            latitude=0.5850791,
            longitude=30.2512728,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kaberamaido District",
            state_code="213",
            latitude=1.6963322,
            longitude=33.213851,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kabul",
            state_code="KAB",
            latitude=34.5553494,
            longitude=69.207486,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Kachin State",
            state_code="11",
            latitude=25.850904,
            longitude=97.4381355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Kadavu",
            state_code="04",
            latitude=-19.0127122,
            longitude=178.1876676,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Kadiogo Province",
            state_code="KAD",
            latitude=12.3425897,
            longitude=-1.443469,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Kaduna",
            state_code="KD",
            latitude=10.3764006,
            longitude=7.7094537,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Kaffrine",
            state_code="KA",
            latitude=14.105202,
            longitude=-15.5415755,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Kafr el-Sheikh",
            state_code="KFS",
            latitude=31.3085444,
            longitude=30.8039474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Kagadi District",
            state_code="427",
            latitude=0.9400761,
            longitude=30.8125638,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kagawa Prefecture",
            state_code="37",
            latitude=34.2225915,
            longitude=134.0199152,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Kagera",
            state_code="05",
            latitude=-1.3001115,
            longitude=31.2626366,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Kagoshima Prefecture",
            state_code="46",
            latitude=31.3911958,
            longitude=130.8778586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Kahramanmaraş",
            state_code="46",
            latitude=37.7503036,
            longitude=36.954107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Kainuu",
            state_code="05",
            latitude=64.3736564,
            longitude=28.7437475,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Kairouan",
            state_code="41",
            latitude=35.6711663,
            longitude=10.1005469,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Kaišiadorys District Municipality",
            state_code="13",
            latitude=54.8588669,
            longitude=24.4277929,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Kajiado",
            state_code="10",
            latitude=-2.0980751,
            longitude=36.7819505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Kakamega",
            state_code="11",
            latitude=0.307894,
            longitude=34.7740793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Kakheti",
            state_code="KA",
            latitude=41.6481602,
            longitude=45.6905554,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Kakumiro District",
            state_code="428",
            latitude=0.7808035,
            longitude=31.3241389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kalangala District",
            state_code="101",
            latitude=-0.6350578,
            longitude=32.5372741,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kalasin",
            state_code="46",
            latitude=16.438508,
            longitude=103.5060994,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Kalbajar District",
            state_code="KAL",
            latitude=40.1024329,
            longitude=46.0364872,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Kalimantan Barat",
            state_code="KB",
            latitude=0.4773475,
            longitude=106.6131405,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Kalimantan Selatan",
            state_code="KS",
            latitude=-3.0926415,
            longitude=115.2837585,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Kalimantan Tengah",
            state_code="KT",
            latitude=-1.6814878,
            longitude=113.3823545,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Kalimantan Timur",
            state_code="KI",
            latitude=0.5386586,
            longitude=116.419389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Kalimantan Utara",
            state_code="KU",
            latitude=3.0730929,
            longitude=116.0413889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Kalinga",
            state_code="KAL",
            latitude=17.4740422,
            longitude=121.3541631,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Kaliningrad",
            state_code="KGD",
            latitude=54.7104264,
            longitude=20.4522144,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kaliro District",
            state_code="222",
            latitude=1.0431107,
            longitude=33.4831906,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kalkara",
            state_code="21",
            latitude=35.8914242,
            longitude=14.5320278,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Kalmar County",
            state_code="H",
            latitude=57.2350156,
            longitude=16.1849349,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Kaluga Oblast",
            state_code="KLU",
            latitude=54.3872666,
            longitude=35.1889094,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kalungu District",
            state_code="122",
            latitude=-0.0952831,
            longitude=31.7651362,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kalutara District",
            state_code="13",
            latitude=6.6084686,
            longitude=80.1428584,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Kalvarija municipality",
            state_code="14",
            latitude=54.3761674,
            longitude=23.1920321,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Kamchatka Krai",
            state_code="KAM",
            latitude=61.4343981,
            longitude=166.7884131,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Kamnik Municipality",
            state_code="043",
            latitude=46.2221666,
            longitude=14.6070727,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kampala District",
            state_code="102",
            latitude=0.3475964,
            longitude=32.5825197,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kamphaeng Phet",
            state_code="62",
            latitude=16.4827798,
            longitude=99.5226618,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Kampong Cham",
            state_code="3",
            latitude=12.0982918,
            longitude=105.3131185,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Kampong Chhnang",
            state_code="4",
            latitude=12.1392352,
            longitude=104.5655273,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Kampong Speu",
            state_code="5",
            latitude=11.6155109,
            longitude=104.3791912,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Kampong Thom",
            state_code="6",
            latitude=12.8167485,
            longitude=103.8413104,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Kampot",
            state_code="7",
            latitude=10.7325351,
            longitude=104.3791912,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Kamuli District",
            state_code="205",
            latitude=0.9187107,
            longitude=33.1239049,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kamwenge District",
            state_code="413",
            latitude=0.225793,
            longitude=30.4818446,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kanagawa Prefecture",
            state_code="14",
            latitude=35.4913535,
            longitude=139.284143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Kanal ob Soči Municipality",
            state_code="044",
            latitude=46.067353,
            longitude=13.620335,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Kanchanaburi",
            state_code="71",
            latitude=14.1011393,
            longitude=99.4179431,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Kandahar",
            state_code="KAN",
            latitude=31.628871,
            longitude=65.7371749,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Kandal",
            state_code="8",
            latitude=11.2237383,
            longitude=105.1258955,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Kandava Municipality",
            state_code="043",
            latitude=57.0340673,
            longitude=22.7801813,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Kandy District",
            state_code="21",
            latitude=7.2931588,
            longitude=80.6350107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Kanem",
            state_code="KA",
            latitude=14.8781262,
            longitude=15.4068079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Kangarli District",
            state_code="KAN",
            latitude=39.387194,
            longitude=45.1639852,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Kangwon Province",
            state_code="07",
            latitude=38.8432393,
            longitude=127.5597067,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="Kankan Prefecture",
            state_code="KA",
            latitude=10.3034465,
            longitude=-9.3673084,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Kankan Region",
            state_code="K",
            latitude=10.120923,
            longitude=-9.5450974,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Kano",
            state_code="KN",
            latitude=11.7470698,
            longitude=8.5247107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Kansas",
            state_code="KS",
            latitude=39.011902,
            longitude=-98.4842465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Kanungu District",
            state_code="414",
            latitude=-0.8195253,
            longitude=29.742604,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kaohsiung",
            state_code="KHH",
            latitude=22.6272784,
            longitude=120.3014353,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Kaolack",
            state_code="KL",
            latitude=14.1652083,
            longitude=-16.0757749,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Kapchorwa District",
            state_code="206",
            latitude=1.3350205,
            longitude=34.3976356,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Kapisa",
            state_code="KAP",
            latitude=34.9810572,
            longitude=69.6214562,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Kaposvár",
            state_code="KV",
            latitude=46.3593606,
            longitude=17.7967639,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Kara Region",
            state_code="K",
            latitude=9.7216393,
            longitude=1.0586135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Togo")][0]),
        ))
        list_of_states.append(State(
            name="Karabük",
            state_code="78",
            latitude=41.187489,
            longitude=32.7417419,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (8/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
