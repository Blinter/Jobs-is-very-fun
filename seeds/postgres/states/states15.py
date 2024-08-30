"""
States Seed #15

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
            name="Pleven Province",
            state_code="15",
            latitude=43.4170169,
            longitude=24.6066708,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Pljevlja Municipality",
            state_code="14",
            latitude=43.2723383,
            longitude=19.2831531,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Plovdiv Province",
            state_code="16",
            latitude=42.1354079,
            longitude=24.7452904,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Plungė District Municipality",
            state_code="35",
            latitude=55.910784,
            longitude=21.8454069,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Plužine Municipality",
            state_code="15",
            latitude=43.1593384,
            longitude=18.8551484,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Plzeň-jih",
            state_code="324",
            latitude=49.5904885,
            longitude=13.5715861,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Plzeň-město",
            state_code="323",
            latitude=49.7384314,
            longitude=13.3736371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Plzeň-sever",
            state_code="325",
            latitude=49.8774893,
            longitude=13.2537428,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Plzeňský kraj",
            state_code="32",
            latitude=49.4134812,
            longitude=13.3157246,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Podčetrtek Municipality",
            state_code="092",
            latitude=46.1739542,
            longitude=15.6013816,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Podgorica Municipality",
            state_code="16",
            latitude=42.3693834,
            longitude=19.2831531,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Podkarpackie Voivodeship",
            state_code="PK",
            latitude=50.0574749,
            longitude=22.0895691,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Podlaskie Voivodeship",
            state_code="PD",
            latitude=53.0697159,
            longitude=22.9674639,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Podlehnik Municipality",
            state_code="172",
            latitude=46.3310782,
            longitude=15.8785836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Podunavlje District",
            state_code="10",
            latitude=44.4729156,
            longitude=20.9901426,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Podvelka Municipality",
            state_code="093",
            latitude=46.6221952,
            longitude=15.3889922,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Pogradec District",
            state_code="PG",
            latitude=40.9015314,
            longitude=20.6556289,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Pohnpei State",
            state_code="PNI",
            latitude=6.8541254,
            longitude=158.2623822,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Micronesia")][0]),
        ))
        list_of_states.append(State(
            name="Point Fortin",
            state_code="PTF",
            latitude=10.1702737,
            longitude=-61.6713386,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Pointe La Rue",
            state_code="20",
            latitude=-4.680489,
            longitude=55.5191857,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Pointe-Noire",
            state_code="16",
            latitude=-4.7691623,
            longitude=11.866362,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Poljčane Municipality",
            state_code="200",
            latitude=46.3139853,
            longitude=15.5784791,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Polonnaruwa District",
            state_code="72",
            latitude=7.9395567,
            longitude=81.0003403,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Poltavska oblast",
            state_code="53",
            latitude=49.6429196,
            longitude=32.6675339,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Põlva County",
            state_code="65",
            latitude=58.1160622,
            longitude=27.2066394,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Polzela Municipality",
            state_code="173",
            latitude=46.280897,
            longitude=15.0737321,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Pomeranian Voivodeship",
            state_code="PM",
            latitude=54.2944252,
            longitude=18.1531164,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Pomeroon-Supenaam",
            state_code="PM",
            latitude=7.1294166,
            longitude=-58.9206295,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guyana")][0]),
        ))
        list_of_states.append(State(
            name="Pomoravlje District",
            state_code="13",
            latitude=43.9591379,
            longitude=21.271353,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Ponce",
            state_code="113",
            latitude=18.0110768,
            longitude=-66.6140616,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Ponce",
            state_code="PO",
            latitude=18,
            longitude=-66.61666667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Poni Province",
            state_code="PON",
            latitude=10.3325996,
            longitude=-3.3388917,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Pontevedra",
            state_code="PO",
            latitude=42.4338595,
            longitude=-8.6568552,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Pool Department",
            state_code="12",
            latitude=-3.7762628,
            longitude=14.8454619,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Poole",
            state_code="POL",
            latitude=50.71505,
            longitude=-1.987248,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Pordenone",
            state_code="PN",
            latitude=46.0378862,
            longitude=12.710835,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Port Glaud",
            state_code="21",
            latitude=-4.6488523,
            longitude=55.4194753,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Port Louis",
            state_code="PL",
            latitude=-20.1608912,
            longitude=57.5012222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Port Moresby",
            state_code="NCD",
            latitude=-9.4438004,
            longitude=147.1802671,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Port of Spain",
            state_code="POS",
            latitude=10.6603196,
            longitude=-61.5085625,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Port Said",
            state_code="PTS",
            latitude=31.0758606,
            longitude=32.2653887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Portalegre",
            state_code="12",
            latitude=39.2967086,
            longitude=-7.4284755,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Portland Parish",
            state_code="04",
            latitude=18.0844274,
            longitude=-76.4100267,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Porto",
            state_code="13",
            latitude=41.1476629,
            longitude=-8.6078973,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Porto Novo",
            state_code="PN",
            latitude=6.4968574,
            longitude=2.6288523,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Portuguesa",
            state_code="P",
            latitude=9.0943999,
            longitude=-69.097023,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Posavina Canton",
            state_code="02",
            latitude=45.0752094,
            longitude=18.3776304,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Postojna Municipality",
            state_code="094",
            latitude=45.774939,
            longitude=14.2134263,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Potaro-Siparuni",
            state_code="PT",
            latitude=4.7855853,
            longitude=-59.2879977,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guyana")][0]),
        ))
        list_of_states.append(State(
            name="Potenza",
            state_code="PZ",
            latitude=40.4182194,
            longitude=15.876004,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Potosí Department",
            state_code="P",
            latitude=-20.624713,
            longitude=-66.9988011,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bolivia")][0]),
        ))
        list_of_states.append(State(
            name="Powys",
            state_code="POW",
            latitude=52.6464249,
            longitude=-3.3260904,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Požega-Slavonia",
            state_code="11",
            latitude=45.3417868,
            longitude=17.8114359,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Prachatice",
            state_code="315",
            latitude=49.01091,
            longitude=14.0000005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Prachin Buri",
            state_code="25",
            latitude=14.0420699,
            longitude=101.6600874,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Prachuap Khiri Khan",
            state_code="77",
            latitude=11.7938389,
            longitude=99.7957564,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Praha, Hlavní město",
            state_code="10",
            latitude=50.0755381,
            longitude=14.4378005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Praha-východ",
            state_code="209",
            latitude=49.9389307,
            longitude=14.7924472,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Praha-západ",
            state_code="20A",
            latitude=49.8935235,
            longitude=14.3293779,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Prahova County",
            state_code="PH",
            latitude=45.0891906,
            longitude=26.0829313,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Praia",
            state_code="PR",
            latitude=14.93305,
            longitude=-23.5133267,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Praslin Quarter",
            state_code="09",
            latitude=13.8752392,
            longitude=-60.8994663,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Prato",
            state_code="PO",
            latitude=44.04539,
            longitude=11.1164452,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Preah Vihear",
            state_code="13",
            latitude=14.0085797,
            longitude=104.8454619,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Prebold Municipality",
            state_code="174",
            latitude=46.2359136,
            longitude=15.0936912,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Preddvor Municipality",
            state_code="095",
            latitude=46.3017139,
            longitude=14.4218165,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Preiļi Municipality",
            state_code="073",
            latitude=56.1511157,
            longitude=26.7439767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Přerov",
            state_code="714",
            latitude=49.4671356,
            longitude=17.5077332,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Presidente Hayes Department",
            state_code="15",
            latitude=-23.3512605,
            longitude=-58.7373634,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Prešov Region",
            state_code="PV",
            latitude=49.1716773,
            longitude=21.3742001,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovakia")][0]),
        ))
        list_of_states.append(State(
            name="Prevalje Municipality",
            state_code="175",
            latitude=46.5621146,
            longitude=14.8847861,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Preveza Prefecture",
            state_code="34",
            latitude=38.9592649,
            longitude=20.7517155,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Prey Veng",
            state_code="14",
            latitude=11.3802442,
            longitude=105.5005483,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Příbram",
            state_code="20B",
            latitude=49.6947959,
            longitude=14.082381,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Priekule Municipality",
            state_code="074",
            latitude=56.4179413,
            longitude=21.5503336,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Priekuļi Municipality",
            state_code="075",
            latitude=57.3617138,
            longitude=25.4410423,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Prienai District Municipality",
            state_code="36",
            latitude=54.638358,
            longitude=23.9468009,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Prilep Municipality",
            state_code="62",
            latitude=41.2693142,
            longitude=21.7137694,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Primorje-Gorski Kotar",
            state_code="08",
            latitude=45.3173996,
            longitude=14.8167466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Primorsky Krai",
            state_code="PRI",
            latitude=45.0525641,
            longitude=135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Prince Edward Island",
            state_code="PE",
            latitude=46.510712,
            longitude=-63.4168136,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Princes Town Regional Corporation",
            state_code="PRT",
            latitude=10.1786746,
            longitude=-61.2801996,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Príncipe Province",
            state_code="P",
            latitude=1.6139381,
            longitude=7.4056928,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sao Tome and Principe")][0]),
        ))
        list_of_states.append(State(
            name="Pristina (Priştine)",
            state_code="XPI",
            latitude=42.6629138,
            longitude=21.1655028,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kosovo")][0]),
        ))
        list_of_states.append(State(
            name="Prizren District",
            state_code="XPR",
            latitude=42.2152522,
            longitude=20.7414772,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kosovo")][0]),
        ))
        list_of_states.append(State(
            name="Probištip Municipality",
            state_code="63",
            latitude=41.9589146,
            longitude=22.166867,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Prostějov",
            state_code="713",
            latitude=49.4418401,
            longitude=17.1277904,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Provence-Alpes-Côte-d’Azur",
            state_code="PAC",
            latitude=43.9351691,
            longitude=6.0679194,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Provincia de Cartago",
            state_code="C",
            latitude=9.8622311,
            longitude=-83.9214187,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Costa Rica")][0]),
        ))
        list_of_states.append(State(
            name="Pskov Oblast",
            state_code="PSK",
            latitude=56.7708599,
            longitude=29.094009,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Ptuj City Municipality",
            state_code="096",
            latitude=46.4199535,
            longitude=15.8696884,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Puconci Municipality",
            state_code="097",
            latitude=46.7200418,
            longitude=16.0997792,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Puducherry",
            state_code="PY",
            latitude=11.9415915,
            longitude=79.8083133,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Puebla",
            state_code="PUE",
            latitude=19.0414398,
            longitude=-98.2062727,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Puerto Plata Province",
            state_code="18",
            latitude=19.7543225,
            longitude=-70.8332847,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Puerto Rico",
            state_code="PR",
            latitude=18.220833,
            longitude=-66.590149,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Pukë District",
            state_code="PU",
            latitude=42.0469772,
            longitude=19.8960968,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Punakha District",
            state_code="23",
            latitude=27.6903716,
            longitude=89.8879304,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Punjab",
            state_code="PB",
            latitude=31.1471305,
            longitude=75.3412179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Punjab",
            state_code="PB",
            latitude=31.1471305,
            longitude=75.3412179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Pakistan")][0]),
        ))
        list_of_states.append(State(
            name="Puno",
            state_code="PUN",
            latitude=-15.8402218,
            longitude=-70.0218805,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Puntarenas Province",
            state_code="P",
            latitude=9.2169531,
            longitude=-83.336188,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Costa Rica")][0]),
        ))
        list_of_states.append(State(
            name="Pursat",
            state_code="15",
            latitude=12.2720956,
            longitude=103.7289167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Putrajaya",
            state_code="16",
            latitude=2.926361,
            longitude=101.696445,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Puttalam District",
            state_code="62",
            latitude=8.0259915,
            longitude=79.8471272,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Putumayo",
            state_code="PUT",
            latitude=0.4359506,
            longitude=-75.5276699,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Puy-de-Dôme",
            state_code="63",
            latitude=45.7714185,
            longitude=2.6262676,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Pwani",
            state_code="19",
            latitude=-7.3237714,
            longitude=38.8205454,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Pyongyang",
            state_code="01",
            latitude=39.0392193,
            longitude=125.7625241,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="Pyrénées-Atlantiques",
            state_code="64",
            latitude=43.186817,
            longitude=-1.4417071,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Pyrénées-Orientales",
            state_code="66",
            latitude=42.6254179,
            longitude=1.8892958,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Qabala District",
            state_code="QAB",
            latitude=40.9253925,
            longitude=47.8016106,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Qacha's Nek District",
            state_code="H",
            latitude=-30.1114565,
            longitude=28.678979,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lesotho")][0]),
        ))
        list_of_states.append(State(
            name="Qakh District",
            state_code="QAX",
            latitude=41.4206827,
            longitude=46.9320184,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Qala",
            state_code="42",
            latitude=36.0388628,
            longitude=14.318101,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Qalqilya",
            state_code="QQA",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Qalyubia",
            state_code="KB",
            latitude=30.3292368,
            longitude=31.2168466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Qashqadaryo Region",
            state_code="QA",
            latitude=38.8986231,
            longitude=66.0463534,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Qazakh District",
            state_code="QAZ",
            latitude=41.0971074,
            longitude=45.3516331,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Qazvin",
            state_code="26",
            latitude=36.0881317,
            longitude=49.8547266,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Qena",
            state_code="KN",
            latitude=26.2346033,
            longitude=32.9888319,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Qinghai",
            state_code="QH",
            latitude=35.744798,
            longitude=96.4077358,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Qom",
            state_code="25",
            latitude=34.6415764,
            longitude=50.8746035,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Qormi",
            state_code="43",
            latitude=35.8764388,
            longitude=14.4694186,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Qrendi",
            state_code="44",
            latitude=35.8328488,
            longitude=14.4548621,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Quảng Bình",
            state_code="24",
            latitude=17.6102715,
            longitude=106.3487474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Quảng Nam",
            state_code="27",
            latitude=15.5393538,
            longitude=108.019102,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Quảng Ngãi",
            state_code="29",
            latitude=15.1213873,
            longitude=108.8044145,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Quảng Ninh",
            state_code="13",
            latitude=21.006382,
            longitude=107.2925144,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Quảng Trị",
            state_code="25",
            latitude=16.7403074,
            longitude=107.1854679,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Quba District",
            state_code="QBA",
            latitude=41.1564242,
            longitude=48.4135021,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Qubadli District",
            state_code="QBI",
            latitude=39.2713996,
            longitude=46.6354312,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Quebec",
            state_code="QC",
            latitude=52.9399159,
            longitude=-73.5491361,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Quebradillas",
            state_code="115",
            latitude=18.473833,
            longitude=-66.938512,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Queensland",
            state_code="QLD",
            latitude=-20.9175738,
            longitude=142.7027956,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Australia")][0]),
        ))
        list_of_states.append(State(
            name="Querétaro",
            state_code="QUE",
            latitude=20.5887932,
            longitude=-100.3898881,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Quetzaltenango Department",
            state_code="QZ",
            latitude=14.792433,
            longitude=-91.714958,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Quezon",
            state_code="QUE",
            latitude=14.0313906,
            longitude=122.1130909,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Quiché Department",
            state_code="QC",
            latitude=15.4983808,
            longitude=-90.9820668,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Quinara Region",
            state_code="QU",
            latitude=11.795562,
            longitude=-15.1726816,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="Quindío",
            state_code="QUI",
            latitude=4.4610191,
            longitude=-75.667356,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Quintana Roo",
            state_code="ROO",
            latitude=19.1817393,
            longitude=-88.4791376,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Quirino",
            state_code="QUI",
            latitude=16.2700424,
            longitude=121.5370003,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Quneitra",
            state_code="QU",
            latitude=33.0776318,
            longitude=35.8934136,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Qusar District",
            state_code="QUS",
            latitude=41.4266886,
            longitude=48.4345577,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Quthing District",
            state_code="G",
            latitude=-30.4015687,
            longitude=27.7080133,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lesotho")][0]),
        ))
        list_of_states.append(State(
            name="Ra",
            state_code="11",
            latitude=37.1003153,
            longitude=-95.6744246,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Raa Atoll",
            state_code="13",
            latitude=5.6006457,
            longitude=72.9460566,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Rabat",
            state_code="46",
            latitude=33.9715904,
            longitude=-6.8498129,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Rabat",
            state_code="RAB",
            latitude=33.969199,
            longitude=-6.9273029,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Rabat-Salé-Kénitra",
            state_code="04",
            latitude=34.076864,
            longitude=-7.3454476,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Rače–Fram Municipality",
            state_code="098",
            latitude=46.4542083,
            longitude=15.6329467,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Racha-Lechkhumi and Kvemo Svaneti",
            state_code="RL",
            latitude=42.6718873,
            longitude=43.0562836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Radeče Municipality",
            state_code="099",
            latitude=46.0666954,
            longitude=15.1820438,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Radenci Municipality",
            state_code="100",
            latitude=46.6231121,
            longitude=16.0506903,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Radlje ob Dravi Municipality",
            state_code="101",
            latitude=46.6135732,
            longitude=15.2354438,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Radoviš Municipality",
            state_code="64",
            latitude=41.6495531,
            longitude=22.4768287,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Radovljica Municipality",
            state_code="102",
            latitude=46.3355827,
            longitude=14.2094534,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Radviliškis District Municipality",
            state_code="37",
            latitude=55.8108399,
            longitude=23.546487,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Rafah",
            state_code="RFH",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Ragged Island",
            state_code="RI",
            latitude=41.597431,
            longitude=-71.260202,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Ragusa",
            state_code="RG",
            latitude=36.9269273,
            longitude=14.7255129,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Rajasthan",
            state_code="RJ",
            latitude=27.0238036,
            longitude=74.2179326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Rajbari District",
            state_code="53",
            latitude=23.715134,
            longitude=89.5874819,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Rajshahi District",
            state_code="54",
            latitude=24.3733087,
            longitude=88.6048716,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Rajshahi Division",
            state_code="E",
            latitude=24.7105776,
            longitude=88.9413865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Rakai District",
            state_code="110",
            latitude=-0.7069135,
            longitude=31.5370003,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Rakhine State",
            state_code="16",
            latitude=20.1040818,
            longitude=93.5812692,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Rakovník",
            state_code="20C",
            latitude=50.106123,
            longitude=13.7396623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Ralik Chain",
            state_code="L",
            latitude=8.136146,
            longitude=164.8867956,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Marshall Islands")][0]),
        ))
        list_of_states.append(State(
            name="Ramallah",
            state_code="RBH",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Rangamati Hill District",
            state_code="56",
            latitude=22.7324173,
            longitude=92.2985134,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Rangpur District",
            state_code="55",
            latitude=25.7467925,
            longitude=89.2508335,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Rangpur Division",
            state_code="F",
            latitude=25.8483388,
            longitude=88.9413865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Rankovce Municipality",
            state_code="65",
            latitude=42.1808141,
            longitude=22.0953297,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Ranong",
            state_code="85",
            latitude=9.9528702,
            longitude=98.6084641,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Rapla County",
            state_code="70",
            latitude=58.8492625,
            longitude=24.7346569,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Rapti Zone",
            state_code="RA",
            latitude=28.274347,
            longitude=82.3885783,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Ras al-Khaimah",
            state_code="RK",
            latitude=25.6741343,
            longitude=55.9804173,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Arab Emirates")][0]),
        ))
        list_of_states.append(State(
            name="Raseiniai District Municipality",
            state_code="38",
            latitude=55.3819499,
            longitude=23.1156129,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Rasina District",
            state_code="19",
            latitude=43.5263525,
            longitude=21.1588178,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Raška District",
            state_code="18",
            latitude=43.3373461,
            longitude=20.5734005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Rason",
            state_code="13",
            latitude=42.2569063,
            longitude=130.2977186,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="Ratak Chain",
            state_code="T",
            latitude=10.2763276,
            longitude=170.5500937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Marshall Islands")][0]),
        ))
        list_of_states.append(State(
            name="Ratanakiri",
            state_code="16",
            latitude=13.8576607,
            longitude=107.1011931,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Ratchaburi",
            state_code="70",
            latitude=13.5282893,
            longitude=99.8134211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Ratnapura district",
            state_code="91",
            latitude=6.7055168,
            longitude=80.3848389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Rauna Municipality",
            state_code="076",
            latitude=57.331693,
            longitude=25.6100339,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Ravenna",
            state_code="RA",
            latitude=44.4184443,
            longitude=12.2035998,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Ravne na Koroškem Municipality",
            state_code="103",
            latitude=46.5521194,
            longitude=14.9599084,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Raymah",
            state_code="RA",
            latitude=14.6277682,
            longitude=43.7142484,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Rayong",
            state_code="21",
            latitude=12.6813957,
            longitude=101.2816261,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Razavi Khorasan",
            state_code="09",
            latitude=35.1020253,
            longitude=59.1041758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Razgrad Province",
            state_code="17",
            latitude=43.5271705,
            longitude=26.5241228,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Razkrižje Municipality",
            state_code="176",
            latitude=46.5226339,
            longitude=16.2668638,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Reading",
            state_code="RDG",
            latitude=36.1486659,
            longitude=-95.9840012,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Rečica ob Savinji Municipality",
            state_code="209",
            latitude=46.323379,
            longitude=14.922367,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Red Sea",
            state_code="BA",
            latitude=24.6826316,
            longitude=34.1531947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Red Sea",
            state_code="RS",
            latitude=20.280232,
            longitude=38.512573,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Redcar and Cleveland",
            state_code="RCC",
            latitude=54.5971344,
            longitude=-1.0775997,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Redonda",
            state_code="11",
            latitude=16.938416,
            longitude=-62.3455148,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Antigua and Barbuda")][0]),
        ))
        list_of_states.append(State(
            name="Reggio Emilia",
            state_code="RE",
            latitude=44.585658,
            longitude=10.5564736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Región Metropolitana de Santiago",
            state_code="RM",
            latitude=-33.4375545,
            longitude=-70.6504896,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Region of Southern Denmark",
            state_code="83",
            latitude=55.3307714,
            longitude=9.0924903,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Denmark")][0]),
        ))
        list_of_states.append(State(
            name="Region Zealand",
            state_code="85",
            latitude=55.4632518,
            longitude=11.7214979,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Denmark")][0]),
        ))
        list_of_states.append(State(
            name="Rehamna",
            state_code="REH",
            latitude=32.2032905,
            longitude=-8.5689671,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Relizane",
            state_code="48",
            latitude=35.7383405,
            longitude=0.7532809,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Renče–Vogrsko Municipality",
            state_code="201",
            latitude=45.8954617,
            longitude=13.6785673,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Renfrewshire",
            state_code="RFW",
            latitude=55.846654,
            longitude=-4.5331259,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Rennell and Bellona Province",
            state_code="RB",
            latitude=-11.6131435,
            longitude=160.1693949,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Solomon Islands")][0]),
        ))
        list_of_states.append(State(
            name="Republic of Adygea",
            state_code="AD",
            latitude=44.8229155,
            longitude=40.1754463,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republic of Bashkortostan",
            state_code="BA",
            latitude=54.2312172,
            longitude=56.1645257,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republic of Buryatia",
            state_code="BU",
            latitude=54.8331146,
            longitude=112.406053,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republic of Dagestan",
            state_code="DA",
            latitude=42.1431886,
            longitude=47.0949799,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republic of Ingushetia",
            state_code="IN",
            latitude=43.4051698,
            longitude=44.8202999,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republic of Kalmykia",
            state_code="KL",
            latitude=46.1867176,
            longitude=45,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republic of Karelia",
            state_code="KR",
            latitude=63.1558702,
            longitude=32.9905552,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republic of Khakassia",
            state_code="KK",
            latitude=53.0452281,
            longitude=90.3982145,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republic of Mordovia",
            state_code="MO",
            latitude=54.2369441,
            longitude=44.068397,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republic of North Ossetia-Alania",
            state_code="SE",
            latitude=43.0451302,
            longitude=44.2870972,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republic of Tatarstan",
            state_code="TA",
            latitude=55.1802364,
            longitude=50.7263945,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Republika Srpska",
            state_code="SRP",
            latitude=44.7280186,
            longitude=17.3148136,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Resen Municipality",
            state_code="66",
            latitude=40.9368093,
            longitude=21.0460407,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Retalhuleu Department",
            state_code="RE",
            latitude=14.5245485,
            longitude=-91.685788,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Rewa",
            state_code="12",
            latitude=34.7923517,
            longitude=-82.3609264,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Rēzekne",
            state_code="REZ",
            latitude=56.5099223,
            longitude=27.3331357,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Rēzekne Municipality",
            state_code="077",
            latitude=56.3273638,
            longitude=27.3284331,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Rezina District",
            state_code="RE",
            latitude=47.7180447,
            longitude=28.8871024,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Rhineland-Palatinate",
            state_code="RP",
            latitude=50.118346,
            longitude=7.3089527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Rhode Island",
            state_code="RI",
            latitude=41.5800945,
            longitude=-71.4774291,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Rhondda Cynon Taf",
            state_code="RCT",
            latitude=51.6490207,
            longitude=-3.4288692,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Rhône",
            state_code="69",
            latitude=44.93433,
            longitude=4.2409329,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Riau",
            state_code="RI",
            latitude=0.2933469,
            longitude=101.7068294,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Ribeira Brava Municipality",
            state_code="RB",
            latitude=16.6070739,
            longitude=-24.2033843,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Ribeira Grande",
            state_code="RG",
            latitude=37.8210369,
            longitude=-25.5148137,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Ribeira Grande de Santiago",
            state_code="RS",
            latitude=14.9830298,
            longitude=-23.6561725,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Ribnica Municipality",
            state_code="104",
            latitude=45.7400303,
            longitude=14.7265782,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Ribnica na Pohorju Municipality",
            state_code="177",
            latitude=46.5356145,
            longitude=15.2674538,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Riebiņi Municipality",
            state_code="078",
            latitude=56.343619,
            longitude=26.8018138,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Rietavas municipality",
            state_code="39",
            latitude=55.7021719,
            longitude=21.9986564,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Rieti",
            state_code="RI",
            latitude=42.3674405,
            longitude=12.8975098,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Rif Dimashq",
            state_code="RD",
            latitude=33.5167289,
            longitude=36.954107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Riga",
            state_code="RIX",
            latitude=56.9496487,
            longitude=24.1051865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Rimini",
            state_code="RN",
            latitude=44.0678288,
            longitude=12.5695158,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Rincón",
            state_code="117",
            latitude=18.3401514,
            longitude=-67.2499459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Rio Claro-Mayaro Regional Corporation",
            state_code="MRC",
            latitude=10.2412832,
            longitude=-61.0937206,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Rio de Janeiro",
            state_code="RJ",
            latitude=-22.9068467,
            longitude=-43.1728965,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Río Grande",
            state_code="119",
            latitude=28.81063826,
            longitude=-101.8353878,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Rio Grande do Norte",
            state_code="RN",
            latitude=-5.4025803,
            longitude=-36.954107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Rio Grande do Sul",
            state_code="RS",
            latitude=-30.0346316,
            longitude=-51.2176986,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (15/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
