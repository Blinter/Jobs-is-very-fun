"""
States Seed #17

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
            name="Santa Cruz de Tenerife",
            state_code="TF",
            latitude=28.4578914,
            longitude=-16.3213539,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Santa Cruz Department",
            state_code="S",
            latitude=-16.7476037,
            longitude=-62.0750998,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bolivia")][0]),
        ))
        list_of_states.append(State(
            name="Santa Elena",
            state_code="SE",
            latitude=-2.2267105,
            longitude=-80.859499,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Santa Fe",
            state_code="S",
            latitude=-31.5855109,
            longitude=-60.7238016,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Santa Isabel",
            state_code="133",
            latitude=17.9660775,
            longitude=-66.404892,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Santa Luċija",
            state_code="53",
            latitude=35.856142,
            longitude=14.50436,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Santa Rosa Department",
            state_code="SR",
            latitude=38.4405759,
            longitude=-122.7037543,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Santa Venera",
            state_code="54",
            latitude=35.8902201,
            longitude=14.4766974,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Santander",
            state_code="SAN",
            latitude=6.6437076,
            longitude=-73.6536209,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Santarém",
            state_code="14",
            latitude=39.2366687,
            longitude=-8.6859944,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Santiago de Cuba Province",
            state_code="13",
            latitude=20.2397682,
            longitude=-75.9927652,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Santiago del Estero",
            state_code="G",
            latitude=-27.7833574,
            longitude=-64.264167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Santiago Province",
            state_code="25",
            latitude=-33.45,
            longitude=-70.6667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Santiago Rodríguez Province",
            state_code="26",
            latitude=19.4713181,
            longitude=-71.3395801,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Santo Domingo de los Tsáchilas",
            state_code="SD",
            latitude=-0.2521882,
            longitude=-79.1879383,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Santo Domingo Province",
            state_code="32",
            latitude=18.5104253,
            longitude=-69.8404054,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="São Domingos",
            state_code="SD",
            latitude=15.0286165,
            longitude=-23.563922,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="São Filipe",
            state_code="SF",
            latitude=14.8951679,
            longitude=-24.4945636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="São Lourenço dos Órgãos",
            state_code="SO",
            latitude=15.0537841,
            longitude=-23.6085612,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="São Miguel",
            state_code="SM",
            latitude=37.780411,
            longitude=-25.4970466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="São Paulo",
            state_code="SP",
            latitude=-23.5505199,
            longitude=-46.6333094,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="São Tomé Province",
            state_code="S",
            latitude=0.3301924,
            longitude=6.733343,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sao Tome and Principe")][0]),
        ))
        list_of_states.append(State(
            name="São Vicente",
            state_code="SV",
            latitude=-23.9607157,
            longitude=-46.3962022,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Saône-et-Loire",
            state_code="71",
            latitude=46.6554883,
            longitude=3.983505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Sar-e Pol",
            state_code="SAR",
            latitude=36.216628,
            longitude=65.93336,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Saraburi",
            state_code="19",
            latitude=14.5289154,
            longitude=100.9101421,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Saraj Municipality",
            state_code="68",
            latitude=41.9869496,
            longitude=21.2606554,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Sarajevo Canton",
            state_code="09",
            latitude=43.8512564,
            longitude=18.2953442,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Saramacca District",
            state_code="SA",
            latitude=5.7240813,
            longitude=-55.6689636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Suriname")][0]),
        ))
        list_of_states.append(State(
            name="Sarandë District",
            state_code="SR",
            latitude=39.8592119,
            longitude=20.0271001,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Sarangani",
            state_code="SAR",
            latitude=5.9267175,
            longitude=124.994751,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Saratov Oblast",
            state_code="SAR",
            latitude=51.8369263,
            longitude=46.7539397,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Sarawak",
            state_code="13",
            latitude=1.5532783,
            longitude=110.3592127,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Sardinia",
            state_code="88",
            latitude=40.1208752,
            longitude=9.0128926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Sarpang District",
            state_code="31",
            latitude=26.9373041,
            longitude=90.4879916,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Sarthe",
            state_code="72",
            latitude=48.0262733,
            longitude=-0.3261317,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Saskatchewan",
            state_code="SK",
            latitude=52.9399159,
            longitude=-106.4508639,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Sassandra-Marahoué District",
            state_code="SM",
            latitude=6.8803348,
            longitude=-6.2375947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Sassari",
            state_code="SS",
            latitude=40.7967907,
            longitude=8.5750407,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Satakunta",
            state_code="17",
            latitude=61.5932758,
            longitude=22.1483081,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Satkhira District",
            state_code="58",
            latitude=22.3154812,
            longitude=89.1114525,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Satu Mare County",
            state_code="SM",
            latitude=47.7668905,
            longitude=22.9241377,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Satun",
            state_code="91",
            latitude=6.6238158,
            longitude=100.0673744,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Satupa'itea",
            state_code="SA",
            latitude=-13.6538214,
            longitude=-172.6159271,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Samoa")][0]),
        ))
        list_of_states.append(State(
            name="Saulkrasti Municipality",
            state_code="089",
            latitude=57.2579418,
            longitude=24.4183146,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Savanes Region",
            state_code="03",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Savanes Region",
            state_code="S",
            latitude=10.5291781,
            longitude=0.5257823,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Togo")][0]),
        ))
        list_of_states.append(State(
            name="Savannah",
            state_code="SV",
            latitude=9.083333,
            longitude=-1.816667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Savannakhet Province",
            state_code="SV",
            latitude=16.5065381,
            longitude=105.5943388,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Savanne",
            state_code="SA",
            latitude=-20.473953,
            longitude=57.4853561,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Šavnik Municipality",
            state_code="18",
            latitude=42.9603756,
            longitude=19.140438,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Savoie",
            state_code="73",
            latitude=45.494699,
            longitude=5.8432984,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Savona",
            state_code="SV",
            latitude=44.2887995,
            longitude=8.265058,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Saxony",
            state_code="SN",
            latitude=51.1045407,
            longitude=13.2017384,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Saxony-Anhalt",
            state_code="ST",
            latitude=51.9502649,
            longitude=11.6922734,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Schaan",
            state_code="07",
            latitude=47.120434,
            longitude=9.5941602,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Schaffhausen",
            state_code="SH",
            latitude=47.7009364,
            longitude=8.568004,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Schellenberg",
            state_code="08",
            latitude=47.230966,
            longitude=9.5467843,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Schleswig-Holstein",
            state_code="SH",
            latitude=54.2193672,
            longitude=9.6961167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Schwyz",
            state_code="SZ",
            latitude=47.0207138,
            longitude=8.6529884,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Scotland",
            state_code="SCT",
            latitude=56.4906712,
            longitude=-4.2026458,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Scottish Borders",
            state_code="SCB",
            latitude=55.5485697,
            longitude=-2.7861388,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Sédhiou",
            state_code="SE",
            latitude=12.704604,
            longitude=-15.5562304,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Sefrou",
            state_code="SEF",
            latitude=33.8305244,
            longitude=-4.8353154,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Sefton",
            state_code="SFT",
            latitude=53.5034449,
            longitude=-2.970359,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ségou Region",
            state_code="4",
            latitude=13.8394456,
            longitude=-6.0679194,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Segovia",
            state_code="SG",
            latitude=40.9429296,
            longitude=-4.1088942,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Seine-et-Marne",
            state_code="77",
            latitude=48.6185394,
            longitude=2.4152561,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Seine-Maritime",
            state_code="76",
            latitude=49.6609681,
            longitude=0.3677561,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Seine-Saint-Denis",
            state_code="93",
            latitude=48.9099318,
            longitude=2.3057379,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Sēja Municipality",
            state_code="090",
            latitude=57.2006995,
            longitude=24.5922821,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Sejong City",
            state_code="50",
            latitude=34.0523323,
            longitude=-118.3084897,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Sekong Province",
            state_code="XE",
            latitude=15.5767446,
            longitude=107.0067031,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Selangor",
            state_code="10",
            latitude=3.0738379,
            longitude=101.5183469,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Selenge Province",
            state_code="049",
            latitude=50.0059273,
            longitude=106.4434108,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Selnica ob Dravi Municipality",
            state_code="178",
            latitude=46.5513918,
            longitude=15.492941,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Sembabule District",
            state_code="111",
            latitude=0.0637715,
            longitude=31.3541631,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Semič Municipality",
            state_code="109",
            latitude=45.6520534,
            longitude=15.1820701,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Semily",
            state_code="514",
            latitude=50.6051576,
            longitude=15.3281409,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Semnan",
            state_code="20",
            latitude=35.2255585,
            longitude=54.4342138,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Šempeter–Vrtojba Municipality",
            state_code="183",
            latitude=45.9290095,
            longitude=13.6415594,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Senaki Municipality",
            state_code="50",
            latitude=42.269636,
            longitude=42.0656896,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Šenčur Municipality",
            state_code="117",
            latitude=46.2433699,
            longitude=14.4192223,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Senglea",
            state_code="20",
            latitude=35.8873041,
            longitude=14.5167371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Sennar",
            state_code="SI",
            latitude=13.567469,
            longitude=33.5672045,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Séno Province",
            state_code="SEN",
            latitude=14.0072234,
            longitude=-0.0746767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Šentilj Municipality",
            state_code="118",
            latitude=46.6862839,
            longitude=15.7103567,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Šentjernej Municipality",
            state_code="119",
            latitude=45.843413,
            longitude=15.3378312,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Šentjur Municipality",
            state_code="120",
            latitude=46.2654339,
            longitude=15.408,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Šentrupert Municipality",
            state_code="211",
            latitude=45.9873142,
            longitude=15.0829783,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Seoul",
            state_code="11",
            latitude=37.566535,
            longitude=126.9779692,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Serere District",
            state_code="232",
            latitude=1.4994033,
            longitude=33.5490078,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Sergipe",
            state_code="SE",
            latitude=-10.5740934,
            longitude=-37.3856581,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Serravalle",
            state_code="09",
            latitude=44.7232084,
            longitude=8.8574005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "San Marino")][0]),
        ))
        list_of_states.append(State(
            name="Serres Prefecture",
            state_code="62",
            latitude=41.0863854,
            longitude=23.5483819,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Serua",
            state_code="13",
            latitude=-18.1804749,
            longitude=178.050979,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Seti Zone",
            state_code="SE",
            latitude=29.6905427,
            longitude=81.3399414,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Sétif",
            state_code="19",
            latitude=36.3073389,
            longitude=5.5617279,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Settat",
            state_code="SET",
            latitude=32.9924242,
            longitude=-7.6222665,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Setúbal",
            state_code="15",
            latitude=38.5240933,
            longitude=-8.8925876,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Sevastopol",
            state_code="40",
            latitude=44.61665,
            longitude=33.5253671,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Sevilla",
            state_code="SE",
            latitude=37.3753501,
            longitude=-6.0250973,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Sevnica Municipality",
            state_code="110",
            latitude=46.0070317,
            longitude=15.3045679,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Sežana Municipality",
            state_code="111",
            latitude=45.7275109,
            longitude=13.8661931,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Sfax",
            state_code="61",
            latitude=34.8606581,
            longitude=10.3497895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Sha Tin",
            state_code="NST",
            latitude=22.38715,
            longitude=114.19534,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Shaanxi",
            state_code="SN",
            latitude=35.3939908,
            longitude=109.1880047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Shabran District",
            state_code="SBN",
            latitude=41.2228376,
            longitude=48.8457304,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Shabwah",
            state_code="SH",
            latitude=14.7546303,
            longitude=46.516262,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Shahbuz District",
            state_code="SAH",
            latitude=39.4452103,
            longitude=45.6568009,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Shaki",
            state_code="SA",
            latitude=41.1974753,
            longitude=47.1571241,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Shaki District",
            state_code="SAK",
            latitude=41.1134662,
            longitude=47.1316927,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Sham Shui Po",
            state_code="KSS",
            latitude=22.33074,
            longitude=114.1622,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Shamakhi District",
            state_code="SMI",
            latitude=40.6318731,
            longitude=48.6363801,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Shamkir District",
            state_code="SKR",
            latitude=40.8288144,
            longitude=46.0166879,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Shan State",
            state_code="17",
            latitude=22.0361985,
            longitude=98.1338558,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Shandong",
            state_code="SD",
            latitude=37.8006064,
            longitude=-122.2699918,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Shanghai",
            state_code="SH",
            latitude=31.230416,
            longitude=121.473701,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Shanxi",
            state_code="SX",
            latitude=37.2425649,
            longitude=111.8568586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Shariatpur District",
            state_code="62",
            latitude=23.2423214,
            longitude=90.4347711,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Sharjah Emirate",
            state_code="SH",
            latitude=25.0753974,
            longitude=55.7578403,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Arab Emirates")][0]),
        ))
        list_of_states.append(State(
            name="Sharqia",
            state_code="SHR",
            latitude=30.6730545,
            longitude=31.1593247,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Sharur District",
            state_code="SAR",
            latitude=39.5536332,
            longitude=44.984568,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Shaviyani Atoll",
            state_code="24",
            latitude=6.17511,
            longitude=73.1349605,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Sheema District",
            state_code="426",
            latitude=-0.5515298,
            longitude=30.3896651,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Shefa",
            state_code="SEE",
            latitude=32.805765,
            longitude=35.169971,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vanuatu")][0]),
        ))
        list_of_states.append(State(
            name="Sheffield",
            state_code="SHF",
            latitude=36.0950743,
            longitude=-80.2788466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Sherpur District",
            state_code="57",
            latitude=25.0746235,
            longitude=90.1494904,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Shetland Islands",
            state_code="ZET",
            latitude=60.5296507,
            longitude=-1.2659409,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Shida Kartli",
            state_code="SK",
            latitude=42.0756944,
            longitude=43.9540462,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Shiga Prefecture",
            state_code="25",
            latitude=35.3292014,
            longitude=136.0563212,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Shimane Prefecture",
            state_code="32",
            latitude=35.1244094,
            longitude=132.6293446,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Shinyanga",
            state_code="22",
            latitude=-3.6809961,
            longitude=33.4271403,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Shirak Region",
            state_code="SH",
            latitude=40.9630814,
            longitude=43.8102461,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Armenia")][0]),
        ))
        list_of_states.append(State(
            name="Shirvan",
            state_code="SR",
            latitude=39.9469707,
            longitude=48.9223919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Shiselweni District",
            state_code="SH",
            latitude=-26.9827577,
            longitude=31.3541631,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Eswatini")][0]),
        ))
        list_of_states.append(State(
            name="Shizuoka Prefecture",
            state_code="22",
            latitude=35.0929397,
            longitude=138.3190276,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Shkodër County",
            state_code="10",
            latitude=42.150371,
            longitude=19.6639309,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Shkodër District",
            state_code="SH",
            latitude=42.0692985,
            longitude=19.5032559,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Shropshire",
            state_code="SHR",
            latitude=52.7063657,
            longitude=-2.7417849,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Shumen",
            state_code="27",
            latitude=43.2712398,
            longitude=26.9361286,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Shusha District",
            state_code="SUS",
            latitude=39.7537438,
            longitude=46.7464755,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Si Sa Ket",
            state_code="33",
            latitude=15.1186009,
            longitude=104.3220095,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Šiauliai City Municipality",
            state_code="43",
            latitude=55.9349085,
            longitude=23.3136823,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Šiauliai County",
            state_code="SA",
            latitude=55.9985751,
            longitude=23.1380051,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Šiauliai District Municipality",
            state_code="44",
            latitude=55.9721456,
            longitude=23.0332371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Siaya",
            state_code="38",
            latitude=-0.0617328,
            longitude=34.2421597,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Siazan District",
            state_code="SIY",
            latitude=41.0783833,
            longitude=49.1118477,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Šibenik-Knin",
            state_code="15",
            latitude=43.9281485,
            longitude=16.1037694,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Sibiu County",
            state_code="SB",
            latitude=45.9269106,
            longitude=24.2254807,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Sichuan",
            state_code="SC",
            latitude=30.2638032,
            longitude=102.8054753,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Sicily",
            state_code="82",
            latitude=37.5999938,
            longitude=14.0153557,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Sidi Bel Abbès",
            state_code="22",
            latitude=34.6806024,
            longitude=-1.0999495,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Sidi Bennour",
            state_code="SIB",
            latitude=32.6492602,
            longitude=-8.4471453,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Sidi Bouzid",
            state_code="43",
            latitude=35.0354386,
            longitude=9.4839392,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Sidi Ifni",
            state_code="SIF",
            latitude=29.3665797,
            longitude=-10.2108485,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Sidi Kacem",
            state_code="SIK",
            latitude=34.2260172,
            longitude=-5.7129164,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Sidi Slimane",
            state_code="SIL",
            latitude=34.2737828,
            longitude=-5.9805972,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Siem Reap",
            state_code="17",
            latitude=13.330266,
            longitude=104.1001326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Siena",
            state_code="SI",
            latitude=43.2937732,
            longitude=11.4339148,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Siġġiewi",
            state_code="55",
            latitude=35.8463742,
            longitude=14.4315746,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Siguiri Prefecture",
            state_code="SI",
            latitude=11.4148113,
            longitude=-9.1788304,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Sigulda Municipality",
            state_code="091",
            latitude=57.1055092,
            longitude=24.8314259,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Sihanoukville",
            state_code="18",
            latitude=10.7581899,
            longitude=103.8216261,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Siirt",
            state_code="56",
            latitude=37.8658862,
            longitude=42.1494523,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Sikasso Region",
            state_code="3",
            latitude=10.8905186,
            longitude=-7.4381355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Sikkim",
            state_code="SK",
            latitude=27.5329718,
            longitude=88.5122178,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Sila",
            state_code="SI",
            latitude=12.13074,
            longitude=21.2845025,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Šilalė District Municipality",
            state_code="45",
            latitude=55.49268,
            longitude=22.1845559,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Silesian Voivodeship",
            state_code="SL",
            latitude=50.5716595,
            longitude=19.3219768,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Siliana",
            state_code="34",
            latitude=36.0887208,
            longitude=9.3645335,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Silistra Province",
            state_code="19",
            latitude=44.1147101,
            longitude=27.2671454,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Šilutė District Municipality",
            state_code="46",
            latitude=55.350414,
            longitude=21.4659859,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Simiyu",
            state_code="30",
            latitude=-2.8308738,
            longitude=34.1531947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Sinaloa",
            state_code="SIN",
            latitude=25.1721091,
            longitude=-107.4795173,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Sindh",
            state_code="SD",
            latitude=25.8943018,
            longitude=68.5247149,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Pakistan")][0]),
        ))
        list_of_states.append(State(
            name="Sing Buri",
            state_code="17",
            latitude=14.8936253,
            longitude=100.3967314,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Sîngerei District",
            state_code="SI",
            latitude=47.6389134,
            longitude=28.1371816,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Singida",
            state_code="23",
            latitude=-6.7453352,
            longitude=34.1531947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Sinoe County",
            state_code="SI",
            latitude=5.49871,
            longitude=-8.6600586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Sinop",
            state_code="57",
            latitude=41.5594749,
            longitude=34.8580532,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Sint Eustatius",
            state_code="BQ3",
            latitude=17.4890306,
            longitude=-62.973555,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bonaire, Sint Eustatius and Saba")][0]),
        ))
        list_of_states.append(State(
            name="Sint Eustatius",
            state_code="BQ3",
            latitude=17.4890306,
            longitude=-62.973555,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Sipaliwini District",
            state_code="SI",
            latitude=3.6567382,
            longitude=-56.2035387,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Suriname")][0]),
        ))
        list_of_states.append(State(
            name="Siparia Regional Corporation",
            state_code="SIP",
            latitude=10.1245626,
            longitude=-61.5603244,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Siquijor",
            state_code="SIG",
            latitude=9.1998779,
            longitude=123.5951925,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Siracusa",
            state_code="SR",
            latitude=37.0656924,
            longitude=15.2857109,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Sirajganj District",
            state_code="59",
            latitude=24.3141115,
            longitude=89.5699615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Sirdaryo Region",
            state_code="SI",
            latitude=40.3863808,
            longitude=68.7154975,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Şırnak",
            state_code="73",
            latitude=37.4187481,
            longitude=42.4918338,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Sironko District",
            state_code="215",
            latitude=1.2302274,
            longitude=34.2491064,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Sirte District",
            state_code="SR",
            latitude=31.189689,
            longitude=16.5701927,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Širvintos District Municipality",
            state_code="47",
            latitude=55.043102,
            longitude=24.956981,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Sisak-Moslavina",
            state_code="03",
            latitude=45.3837926,
            longitude=16.5380994,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Sissili Province",
            state_code="SIS",
            latitude=11.2441219,
            longitude=-2.2236667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Sistan and Baluchestan",
            state_code="11",
            latitude=27.5299906,
            longitude=60.5820676,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Sivas",
            state_code="58",
            latitude=39.4488039,
            longitude=37.1294497,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Skåne County",
            state_code="M",
            latitude=55.9902572,
            longitude=13.5957692,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Skhirate-Témara",
            state_code="SKH",
            latitude=33.7622425,
            longitude=-7.0419052,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Skikda",
            state_code="21",
            latitude=36.6721198,
            longitude=6.8350999,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Škocjan Municipality",
            state_code="121",
            latitude=45.9175454,
            longitude=15.3101736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Škofja Loka Municipality",
            state_code="122",
            latitude=46.1409844,
            longitude=14.2811873,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Skrapar District",
            state_code="SK",
            latitude=40.5349946,
            longitude=20.2832217,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Skrīveri Municipality",
            state_code="092",
            latitude=56.6761391,
            longitude=25.0978849,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Skrunda Municipality",
            state_code="093",
            latitude=56.6643458,
            longitude=22.0045729,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Skuodas District Municipality",
            state_code="48",
            latitude=56.2702169,
            longitude=21.5214331,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Sliema",
            state_code="56",
            latitude=35.9110081,
            longitude=14.502904,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Sligo",
            state_code="SO",
            latitude=54.1553277,
            longitude=-8.6064532,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Sliven Province",
            state_code="20",
            latitude=42.6816702,
            longitude=26.3228569,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Slough",
            state_code="SLG",
            latitude=51.5105384,
            longitude=-0.5950406,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Slovenj Gradec City Municipality",
            state_code="112",
            latitude=46.4877718,
            longitude=15.0729478,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Slovenska Bistrica Municipality",
            state_code="113",
            latitude=46.3919813,
            longitude=15.5727869,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Slovenske Konjice Municipality",
            state_code="114",
            latitude=46.3369191,
            longitude=15.4214708,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Šmarje pri Jelšah Municipality",
            state_code="124",
            latitude=46.2287025,
            longitude=15.5190353,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Šmarješke Toplice Municipality",
            state_code="206",
            latitude=45.8680377,
            longitude=15.2347422,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Šmartno ob Paki Municipality",
            state_code="125",
            latitude=46.3290372,
            longitude=15.0333937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Šmartno pri Litiji Municipality",
            state_code="194",
            latitude=46.0454971,
            longitude=14.8410133,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Smiltene Municipality",
            state_code="094",
            latitude=57.4230332,
            longitude=25.900278,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Smith's",
            state_code="SMI",
            latitude=32.3133966,
            longitude=-64.7310588,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bermuda")][0]),
        ))
        list_of_states.append(State(
            name="Smolensk Oblast",
            state_code="SMO",
            latitude=54.9882994,
            longitude=32.6677378,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Smolyan Province",
            state_code="21",
            latitude=41.5774148,
            longitude=24.7010871,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Sóc Trăng",
            state_code="52",
            latitude=9.602521,
            longitude=105.9739049,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Soccsksargen",
            state_code="12",
            latitude=6.2706918,
            longitude=124.6856509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Socotra",
            state_code="SU",
            latitude=12.4634205,
            longitude=53.8237385,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Södermanland County",
            state_code="D",
            latitude=59.0336349,
            longitude=16.7518899,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Sodražica Municipality",
            state_code="179",
            latitude=45.7616565,
            longitude=14.6352853,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Sofala Province",
            state_code="S",
            latitude=-19.2039073,
            longitude=34.8624166,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Sofia City Province",
            state_code="22",
            latitude=42.7570109,
            longitude=23.4504683,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Sofia Province",
            state_code="23",
            latitude=42.67344,
            longitude=23.8334937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Sohag",
            state_code="SHG",
            latitude=26.693834,
            longitude=32.174605,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Sokolov",
            state_code="413",
            latitude=50.2013434,
            longitude=12.6054636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Sokoto",
            state_code="SO",
            latitude=13.0533143,
            longitude=5.3222722,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Solčava Municipality",
            state_code="180",
            latitude=46.4023526,
            longitude=14.6802304,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Șoldănești District",
            state_code="SD",
            latitude=47.8147389,
            longitude=28.7889586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Solihull",
            state_code="SOL",
            latitude=52.411811,
            longitude=-1.77761,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Sololá Department",
            state_code="SO",
            latitude=14.748523,
            longitude=-91.2891036,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Solothurn",
            state_code="SO",
            latitude=47.3320717,
            longitude=7.6388385,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Somali Region",
            state_code="SO",
            latitude=6.6612293,
            longitude=43.7908453,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ethiopia")][0]),
        ))
        list_of_states.append(State(
            name="Somerset",
            state_code="SOM",
            latitude=51.105097,
            longitude=-2.9262307,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Somme",
            state_code="80",
            latitude=49.9685922,
            longitude=1.7310696,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Somogy County",
            state_code="SO",
            latitude=46.554859,
            longitude=17.5866732,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Sơn La",
            state_code="05",
            latitude=21.1022284,
            longitude=103.7289167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Sondrio",
            state_code="SO",
            latitude=46.1727636,
            longitude=9.7994917,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Songkhla",
            state_code="90",
            latitude=7.1897659,
            longitude=100.5953813,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Songwe",
            state_code="31",
            latitude=-8.272612,
            longitude=31.7113174,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Sonora",
            state_code="SON",
            latitude=37.9829496,
            longitude=-120.3821724,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Sonsonate Department",
            state_code="SO",
            latitude=13.682358,
            longitude=-89.6628111,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="Sonsorol",
            state_code="370",
            latitude=5.3268119,
            longitude=132.2239117,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Sopište Municipality",
            state_code="70",
            latitude=41.8638492,
            longitude=21.3083499,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Sopron",
            state_code="SN",
            latitude=47.6816619,
            longitude=16.5844795,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (17/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
