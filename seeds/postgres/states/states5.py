"""
States Seed #5

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
            name="Como",
            state_code="CO",
            latitude=45.8080416,
            longitude=9.0851793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Comoé District",
            state_code="CM",
            latitude=5.552793,
            longitude=-3.2583626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Comoé Province",
            state_code="COM",
            latitude=10.4072992,
            longitude=-4.5624426,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Compostela Valley",
            state_code="COM",
            latitude=7.512515,
            longitude=126.1762615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Conakry",
            state_code="C",
            latitude=9.6411855,
            longitude=-13.5784012,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Concepción Department",
            state_code="1",
            latitude=-23.4214264,
            longitude=-57.4344451,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Connacht",
            state_code="C",
            latitude=53.8376243,
            longitude=-8.9584481,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Connecticut",
            state_code="CT",
            latitude=41.6032207,
            longitude=-73.087749,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Constanța County",
            state_code="CT",
            latitude=44.212987,
            longitude=28.2550055,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Constantine",
            state_code="25",
            latitude=36.3373911,
            longitude=6.663812,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Conwy County Borough",
            state_code="CWY",
            latitude=53.2935013,
            longitude=-3.7265161,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Cookstown District Council",
            state_code="CKT",
            latitude=54.6418158,
            longitude=-6.7443895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Copán Department",
            state_code="CP",
            latitude=14.9360838,
            longitude=-88.864698,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Copperbelt Province",
            state_code="08",
            latitude=-13.0570073,
            longitude=27.5495846,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zambia")][0]),
        ))
        list_of_states.append(State(
            name="Coquimbo",
            state_code="CO",
            latitude=-30.540181,
            longitude=-70.8119953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Cordillera Administrative",
            state_code="15",
            latitude=17.3512542,
            longitude=121.1718851,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Cordillera Department",
            state_code="3",
            latitude=-25.2289491,
            longitude=-57.0111681,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Córdoba",
            state_code="X",
            latitude=-31.3992876,
            longitude=-64.2643842,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Córdoba",
            state_code="COR",
            latitude=8.049293,
            longitude=-75.57405,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Córdoba",
            state_code="CO",
            latitude=36.5163851,
            longitude=-6.2999767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Corfu Prefecture",
            state_code="22",
            latitude=39.6249838,
            longitude=19.9223461,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Corinthia Regional Unit",
            state_code="15",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Cork",
            state_code="CO",
            latitude=51.8985143,
            longitude=-8.4756035,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Cornwall",
            state_code="CON",
            latitude=50.2660471,
            longitude=-5.0527125,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Coronie District",
            state_code="CR",
            latitude=5.6943271,
            longitude=-56.2929381,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Suriname")][0]),
        ))
        list_of_states.append(State(
            name="Corozal",
            state_code="047",
            latitude=18.4030802,
            longitude=-88.3967536,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Corozal District",
            state_code="CZL",
            latitude=18.1349238,
            longitude=-88.2461183,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belize")][0]),
        ))
        list_of_states.append(State(
            name="Corrèze",
            state_code="19",
            latitude=45.3423707,
            longitude=1.3171733,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Corrientes",
            state_code="W",
            latitude=-27.4692131,
            longitude=-58.8306349,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Corse",
            state_code="20R",
            latitude=42.0396042,
            longitude=9.0128926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Corse-du-Sud",
            state_code="2A",
            latitude=41.8572055,
            longitude=8.4109183,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Cortés Department",
            state_code="CR",
            latitude=15.4923508,
            longitude=-88.0900762,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Çorum",
            state_code="19",
            latitude=40.4998211,
            longitude=34.5986263,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Cosenza",
            state_code="CS",
            latitude=39.5644105,
            longitude=16.2522143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Cospicua",
            state_code="06",
            latitude=35.8806753,
            longitude=14.5218338,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Cotabato",
            state_code="NCO",
            latitude=7.2046668,
            longitude=124.2310439,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Côte-d'Or",
            state_code="21",
            latitude=47.4651302,
            longitude=4.2315495,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Côtes-d'Armor",
            state_code="22",
            latitude=48.4663336,
            longitude=-3.3478961,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Cotopaxi",
            state_code="X",
            latitude=-0.8384206,
            longitude=-78.6662678,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="County Durham",
            state_code="DUR",
            latitude=54.7294099,
            longitude=-1.8811598,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Couva-Tabaquite-Talparo Regional Corporation",
            state_code="CTT",
            latitude=10.4297145,
            longitude=-61.373521,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Cova Lima Municipality",
            state_code="CO",
            latitude=-9.2650375,
            longitude=125.2587964,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Timor-Leste")][0]),
        ))
        list_of_states.append(State(
            name="Covasna County",
            state_code="CV",
            latitude=45.9426347,
            longitude=25.8918984,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Coventry",
            state_code="COV",
            latitude=52.406822,
            longitude=-1.519693,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Cox's Bazar District",
            state_code="11",
            latitude=21.5640626,
            longitude=92.0282129,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Coyah Prefecture",
            state_code="CO",
            latitude=9.7715535,
            longitude=-13.3125299,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Craigavon Borough Council",
            state_code="CGV",
            latitude=54.3932592,
            longitude=-6.4563401,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Cremona",
            state_code="CR",
            latitude=45.2014375,
            longitude=9.9836582,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Črenšovci Municipality",
            state_code="015",
            latitude=46.5720029,
            longitude=16.2877346,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Crete Region",
            state_code="M",
            latitude=35.240117,
            longitude=24.8092691,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Creuse",
            state_code="23",
            latitude=46.0590394,
            longitude=1.431505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Criuleni District",
            state_code="CR",
            latitude=47.2136114,
            longitude=29.1557519,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Črna na Koroškem Municipality",
            state_code="016",
            latitude=46.4704529,
            longitude=14.8499998,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Črnomelj Municipality",
            state_code="017",
            latitude=45.5361225,
            longitude=15.1944143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Crooked Island",
            state_code="CK",
            latitude=22.6390982,
            longitude=-74.006509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Cross River",
            state_code="CR",
            latitude=5.8701724,
            longitude=8.5988014,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Crotone",
            state_code="KR",
            latitude=39.1309856,
            longitude=17.0067031,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Csongrád County",
            state_code="CS",
            latitude=46.416705,
            longitude=20.2566161,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Cuando Cubango Province",
            state_code="CCU",
            latitude=-16.4180824,
            longitude=18.8076195,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Cuanza Norte Province",
            state_code="CNO",
            latitude=-9.2398513,
            longitude=14.6587821,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Cuanza Sul",
            state_code="CUS",
            latitude=-10.595191,
            longitude=15.4068079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Čučer-Sandevo Municipality",
            state_code="82",
            latitude=42.1483946,
            longitude=21.4037407,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Cuenca",
            state_code="CU",
            latitude=40.0620036,
            longitude=-2.1655344,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Culebra",
            state_code="049",
            latitude=18.310394,
            longitude=-65.3030705,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Cumbria",
            state_code="CMA",
            latitude=54.5772323,
            longitude=-2.7974835,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Cundinamarca",
            state_code="CUN",
            latitude=5.026003,
            longitude=-74.0300122,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Cunene Province",
            state_code="CNN",
            latitude=-16.2802221,
            longitude=16.1580937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Cuneo",
            state_code="CN",
            latitude=44.5970314,
            longitude=7.6114217,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Cuscatlán Department",
            state_code="CU",
            latitude=13.8661957,
            longitude=-89.0561532,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="Cusco",
            state_code="CUS",
            latitude=-13.53195,
            longitude=-71.9674626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Cuvette Department",
            state_code="8",
            latitude=-0.2877446,
            longitude=16.1580937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Cuvette-Ouest Department",
            state_code="15",
            latitude=0.144755,
            longitude=14.4723301,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Cuyuni-Mazaruni",
            state_code="CU",
            latitude=6.4642141,
            longitude=-60.2110752,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guyana")][0]),
        ))
        list_of_states.append(State(
            name="Dabola Prefecture",
            state_code="DB",
            latitude=10.7297806,
            longitude=-11.1107854,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Dadra and Nagar Haveli and Daman and Diu",
            state_code="DH",
            latitude=20.3973736,
            longitude=72.8327991,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Daegu",
            state_code="27",
            latitude=35.8714354,
            longitude=128.601445,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Daejeon",
            state_code="30",
            latitude=36.3504119,
            longitude=127.3845475,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Korea")][0]),
        ))
        list_of_states.append(State(
            name="Dagana District",
            state_code="22",
            latitude=27.0322861,
            longitude=89.8879304,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Dagda Municipality",
            state_code="024",
            latitude=56.0956089,
            longitude=27.532459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Dajabón Province",
            state_code="05",
            latitude=19.5499241,
            longitude=-71.7086514,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Dakahlia",
            state_code="DK",
            latitude=31.1656044,
            longitude=31.4913182,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Dakar",
            state_code="DK",
            latitude=14.716677,
            longitude=-17.4676861,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Dakhla-Oued Ed-Dahab (EH)",
            state_code="12",
            latitude=22.7337892,
            longitude=-14.2861116,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Dakhlet Nouadhibou",
            state_code="08",
            latitude=20.5985588,
            longitude=-16.2522143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritania")][0]),
        ))
        list_of_states.append(State(
            name="Dalaba Prefecture",
            state_code="DL",
            latitude=10.6868176,
            longitude=-12.2490697,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Dalarna County",
            state_code="W",
            latitude=61.0917012,
            longitude=14.6663653,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Damascus",
            state_code="DI",
            latitude=33.5151444,
            longitude=36.3931354,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Dâmbovița County",
            state_code="DB",
            latitude=44.9289893,
            longitude=25.425385,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Damietta",
            state_code="DT",
            latitude=31.3625799,
            longitude=31.6739371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Danilovgrad Municipality",
            state_code="07",
            latitude=42.58357,
            longitude=19.140438,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Dar es Salaam",
            state_code="02",
            latitude=-6.792354,
            longitude=39.2083284,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Daraa",
            state_code="DR",
            latitude=32.9248813,
            longitude=36.1762615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Darién Province",
            state_code="5",
            latitude=7.8681713,
            longitude=-77.8367282,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Darkhan-Uul Province",
            state_code="037",
            latitude=49.4648434,
            longitude=105.9745919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Darlington",
            state_code="DAL",
            latitude=34.2998762,
            longitude=-79.8761741,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Dashkasan District",
            state_code="DAS",
            latitude=40.5202257,
            longitude=46.0779304,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Daşoguz Region",
            state_code="D",
            latitude=41.8368737,
            longitude=59.9651904,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkmenistan")][0]),
        ))
        list_of_states.append(State(
            name="Daugavpils",
            state_code="DGV",
            latitude=55.874736,
            longitude=26.536179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Daugavpils Municipality",
            state_code="025",
            latitude=55.8991783,
            longitude=26.6102012,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Dauphin Quarter",
            state_code="04",
            latitude=14.0103396,
            longitude=-60.9190988,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Davao",
            state_code="11",
            latitude=7.3041622,
            longitude=126.0893406,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Davao del Norte",
            state_code="DAV",
            latitude=7.5617699,
            longitude=125.6532848,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Davao del Sur",
            state_code="DAS",
            latitude=6.7662687,
            longitude=125.3284269,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Davao Occidental",
            state_code="DVO",
            latitude=6.0941396,
            longitude=125.6095474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Davao Oriental",
            state_code="DAO",
            latitude=7.3171585,
            longitude=126.5419887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Daykundi",
            state_code="DAY",
            latitude=33.669495,
            longitude=66.0463534,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Debarca Municipality",
            state_code="22",
            latitude=41.3584077,
            longitude=20.8552919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Debrecen",
            state_code="DE",
            latitude=47.5316049,
            longitude=21.6273124,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Debub Region",
            state_code="DU",
            latitude=14.9478692,
            longitude=39.1543677,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Eritrea")][0]),
        ))
        list_of_states.append(State(
            name="Děčín",
            state_code="421",
            latitude=50.7725563,
            longitude=14.2127612,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Dedza District",
            state_code="DE",
            latitude=-14.1894585,
            longitude=34.2421597,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Deir El Balah",
            state_code="DEB",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Deir ez-Zor",
            state_code="DY",
            latitude=35.2879798,
            longitude=40.3088626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Syria")][0]),
        ))
        list_of_states.append(State(
            name="Delaware",
            state_code="DE",
            latitude=38.9108325,
            longitude=-75.5276699,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Delčevo Municipality",
            state_code="23",
            latitude=41.9684387,
            longitude=22.762883,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Delhi",
            state_code="DL",
            latitude=28.7040592,
            longitude=77.1024902,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Delta",
            state_code="DE",
            latitude=33.7453784,
            longitude=-90.7354508,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Delta Amacuro",
            state_code="Y",
            latitude=8.8499307,
            longitude=-61.1403196,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Delvinë District",
            state_code="DL",
            latitude=39.9481364,
            longitude=20.0955891,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Demerara-Mahaica",
            state_code="DE",
            latitude=6.546426,
            longitude=-58.0982046,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guyana")][0]),
        ))
        list_of_states.append(State(
            name="Demir Hisar Municipality",
            state_code="25",
            latitude=41.227083,
            longitude=21.1414226,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Demir Kapija Municipality",
            state_code="24",
            latitude=41.3795538,
            longitude=22.2145571,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Denbighshire",
            state_code="DEN",
            latitude=53.1842288,
            longitude=-3.4224985,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Denguélé District",
            state_code="DN",
            latitude=48.0707763,
            longitude=-68.5609341,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Denguélé Region",
            state_code="10",
            latitude=9.4662372,
            longitude=-7.4381355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Denigomodu District",
            state_code="08",
            latitude=-0.5247964,
            longitude=166.9167689,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nauru")][0]),
        ))
        list_of_states.append(State(
            name="Denizli",
            state_code="20",
            latitude=37.6128395,
            longitude=29.2320784,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Dennery Quarter",
            state_code="05",
            latitude=13.9267393,
            longitude=-60.9190988,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Derbyshire",
            state_code="DBY",
            latitude=53.1046782,
            longitude=-1.5623885,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Derna District",
            state_code="DR",
            latitude=32.755613,
            longitude=22.6377432,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Derry City and Strabane",
            state_code="DRS",
            latitude=55.0047443,
            longitude=-7.3209222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Derry City Council",
            state_code="DRY",
            latitude=54.9690778,
            longitude=-7.1958351,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Destrnik Municipality",
            state_code="018",
            latitude=46.4922368,
            longitude=15.8777956,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Deux-Sèvres",
            state_code="79",
            latitude=46.5386817,
            longitude=-0.9019948,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Devoll District",
            state_code="DV",
            latitude=40.6447347,
            longitude=20.9506636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Devon",
            state_code="DEV",
            latitude=50.7155591,
            longitude=-3.530875,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Devonshire",
            state_code="DEV",
            latitude=32.3038062,
            longitude=-64.7606954,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bermuda")][0]),
        ))
        list_of_states.append(State(
            name="Dhaalu Atoll",
            state_code="17",
            latitude=2.8468502,
            longitude=72.9460566,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Dhaka District",
            state_code="13",
            latitude=23.810514,
            longitude=90.3371889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Dhaka Division",
            state_code="C",
            latitude=23.9535742,
            longitude=90.1494988,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Dhamar",
            state_code="DH",
            latitude=14.7195344,
            longitude=44.2479015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Dhaulagiri Zone",
            state_code="DH",
            latitude=28.611176,
            longitude=83.5070203,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Dhi Qar",
            state_code="DQ",
            latitude=31.1042292,
            longitude=46.3624686,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Dhofar",
            state_code="ZU",
            latitude=17.0322121,
            longitude=54.1425214,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Oman")][0]),
        ))
        list_of_states.append(State(
            name="DI Yogyakarta",
            state_code="YO",
            latitude=-7.8753849,
            longitude=110.4262088,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Dibër County",
            state_code="09",
            latitude=41.5888163,
            longitude=20.2355647,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Dibër District",
            state_code="DI",
            latitude=41.5888163,
            longitude=20.2355647,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Diego Martin Regional Corporation",
            state_code="DMN",
            latitude=10.7362286,
            longitude=-61.5544836,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Diekirch District",
            state_code="D",
            latitude=49.867172,
            longitude=6.1596362,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Diffa Region",
            state_code="2",
            latitude=13.6768647,
            longitude=12.7135121,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Niger")][0]),
        ))
        list_of_states.append(State(
            name="Dikhil Region",
            state_code="DI",
            latitude=11.1054336,
            longitude=42.3704744,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Djibouti")][0]),
        ))
        list_of_states.append(State(
            name="Dili municipality",
            state_code="DI",
            latitude=-8.2449613,
            longitude=125.5876697,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Timor-Leste")][0]),
        ))
        list_of_states.append(State(
            name="Dinagat Islands",
            state_code="DIN",
            latitude=10.1281816,
            longitude=125.6095474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Dinajpur District",
            state_code="14",
            latitude=25.6279123,
            longitude=88.6331758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Dingli",
            state_code="07",
            latitude=35.8627309,
            longitude=14.3850107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Dinguiraye Prefecture",
            state_code="DI",
            latitude=11.6844222,
            longitude=-10.8000051,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Diourbel Region",
            state_code="DB",
            latitude=14.7283085,
            longitude=-16.2522143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Dire Dawa",
            state_code="DD",
            latitude=9.6008747,
            longitude=41.850142,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ethiopia")][0]),
        ))
        list_of_states.append(State(
            name="District of Columbia",
            state_code="DC",
            latitude=38.9071923,
            longitude=-77.0368707,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="districts of Republican Subordination",
            state_code="RA",
            latitude=39.0857902,
            longitude=70.2408325,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tajikistan")][0]),
        ))
        list_of_states.append(State(
            name="Distrito Capital",
            state_code="A",
            latitude=41.2614846,
            longitude=-95.9310807,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Distrito Federal",
            state_code="DF",
            latitude=-15.7997654,
            longitude=-47.8644715,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Distrito Nacional",
            state_code="01",
            latitude=18.4860575,
            longitude=-69.9312117,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Divača Municipality",
            state_code="019",
            latitude=45.6806069,
            longitude=13.9720312,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Dix-Huit Montagnes",
            state_code="06",
            latitude=7.3762373,
            longitude=-7.4381355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Diyala",
            state_code="DI",
            latitude=33.7733487,
            longitude=45.1494505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Diyarbakır",
            state_code="21",
            latitude=38.1066372,
            longitude=40.5426896,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Djanet",
            state_code="56",
            latitude=23.8310872,
            longitude=8.7004672,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Djelfa",
            state_code="17",
            latitude=34.6703956,
            longitude=3.2503761,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Djibouti",
            state_code="DJ",
            latitude=11.825138,
            longitude=42.590275,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Djibouti")][0]),
        ))
        list_of_states.append(State(
            name="DKI Jakarta",
            state_code="JK",
            latitude=-6.2087634,
            longitude=106.845599,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Dnipropetrovska oblast",
            state_code="12",
            latitude=48.464717,
            longitude=35.046183,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Dobele Municipality",
            state_code="026",
            latitude=56.626305,
            longitude=23.2809066,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Dobje Municipality",
            state_code="154",
            latitude=46.1370037,
            longitude=15.394129,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Dobrepolje Municipality",
            state_code="020",
            latitude=45.8524951,
            longitude=14.7083109,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Dobrich Province",
            state_code="08",
            latitude=43.572786,
            longitude=27.8272802,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Dobrna Municipality",
            state_code="155",
            latitude=46.3356141,
            longitude=15.2259732,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Dobrova–Polhov Gradec Municipality",
            state_code="021",
            latitude=46.0648896,
            longitude=14.3168195,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Dobrovnik Municipality",
            state_code="156",
            latitude=46.6538662,
            longitude=16.3506594,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Dodoma",
            state_code="03",
            latitude=-6.5738228,
            longitude=36.2630846,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Doha",
            state_code="DA",
            latitude=25.2854473,
            longitude=51.5310398,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Qatar")][0]),
        ))
        list_of_states.append(State(
            name="Dohuk",
            state_code="DA",
            latitude=36.9077252,
            longitude=43.0631689,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Dojran Municipality",
            state_code="26",
            latitude=41.2436672,
            longitude=22.6913764,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Dokolo District",
            state_code="317",
            latitude=1.9636421,
            longitude=33.0338767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Dol pri Ljubljani Municipality",
            state_code="022",
            latitude=46.0884386,
            longitude=14.6424792,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Dolenjske Toplice Municipality",
            state_code="157",
            latitude=45.7345711,
            longitude=15.0129493,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Dolj County",
            state_code="DJ",
            latitude=44.1623022,
            longitude=23.6325054,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Dolneni Municipality",
            state_code="27",
            latitude=41.4640935,
            longitude=21.4037407,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Domagnano",
            state_code="03",
            latitude=43.9501929,
            longitude=12.4681537,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "San Marino")][0]),
        ))
        list_of_states.append(State(
            name="Domažlice",
            state_code="321",
            latitude=49.4397027,
            longitude=12.9311435,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Domžale Municipality",
            state_code="023",
            latitude=46.1438269,
            longitude=14.6375279,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Doncaster",
            state_code="DNC",
            latitude=53.52282,
            longitude=-1.128462,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Dondușeni District",
            state_code="DO",
            latitude=48.2338305,
            longitude=27.5998087,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Donegal",
            state_code="DL",
            latitude=54.6548993,
            longitude=-8.1040967,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Donetska oblast",
            state_code="14",
            latitude=48.015883,
            longitude=37.80285,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Donga Department",
            state_code="DO",
            latitude=9.7191867,
            longitude=1.6760691,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Dorado",
            state_code="051",
            latitude=43.1480556,
            longitude=-77.5772222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Dordogne",
            state_code="24",
            latitude=45.1423416,
            longitude=0.1427408,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Dornava Municipality",
            state_code="024",
            latitude=46.4443513,
            longitude=15.9889159,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Dornod Province",
            state_code="061",
            latitude=47.4658154,
            longitude=115.392712,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Dornogovi Province",
            state_code="063",
            latitude=43.9653889,
            longitude=109.1773459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Dorset",
            state_code="DOR",
            latitude=50.7487635,
            longitude=-2.3444786,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Dosso Region",
            state_code="3",
            latitude=13.1513947,
            longitude=3.4195527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Niger")][0]),
        ))
        list_of_states.append(State(
            name="Doubs",
            state_code="25",
            latitude=46.9321774,
            longitude=6.3476214,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Dowa District",
            state_code="DO",
            latitude=-13.6041256,
            longitude=33.8857747,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Down District Council",
            state_code="DOW",
            latitude=54.2434287,
            longitude=-5.9577959,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Drâa-Tafilalet",
            state_code="08",
            latitude=31.1499538,
            longitude=-5.3939551,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Drama Regional Unit",
            state_code="52",
            latitude=41.2340023,
            longitude=24.2390498,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Dravograd Municipality",
            state_code="025",
            latitude=46.589219,
            longitude=15.0246021,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Drenthe",
            state_code="DR",
            latitude=52.9476012,
            longitude=6.6230586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Driouch",
            state_code="DRI",
            latitude=34.976032,
            longitude=-3.3964493,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Drochia District",
            state_code="DR",
            latitude=48.0797788,
            longitude=27.8604114,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Drôme",
            state_code="26",
            latitude=44.7293357,
            longitude=4.6782158,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Drugovo Municipality",
            state_code="28",
            latitude=41.4408153,
            longitude=20.9268201,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Druskininkai municipality",
            state_code="07",
            latitude=53.9933685,
            longitude=24.0342438,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Duarte Province",
            state_code="06",
            latitude=19.2090823,
            longitude=-70.0270004,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Dubai",
            state_code="DU",
            latitude=25.2048493,
            longitude=55.2707828,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Arab Emirates")][0]),
        ))
        list_of_states.append(State(
            name="Dubăsari District",
            state_code="DU",
            latitude=47.2643942,
            longitude=29.1550348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Dublin",
            state_code="D",
            latitude=53.3498053,
            longitude=-6.2603097,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Dubréka Prefecture",
            state_code="DU",
            latitude=9.7907348,
            longitude=-13.5147735,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Dubrovnik-Neretva",
            state_code="19",
            latitude=43.0766588,
            longitude=17.5268471,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Dudley",
            state_code="DUD",
            latitude=42.0433661,
            longitude=-71.9276033,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Dumfries and Galloway",
            state_code="DGY",
            latitude=55.0701073,
            longitude=-3.6052581,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Dunaújváros",
            state_code="DU",
            latitude=46.9619059,
            longitude=18.9355227,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Dundaga Municipality",
            state_code="027",
            latitude=57.5049167,
            longitude=22.3505114,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Dundee",
            state_code="DND",
            latitude=56.462018,
            longitude=-2.970721,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Dundgovi Province",
            state_code="059",
            latitude=45.5822786,
            longitude=106.7644209,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Dungannon and South Tyrone Borough Council",
            state_code="DGN",
            latitude=54.5082684,
            longitude=-6.7665891,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Duplek Municipality",
            state_code="026",
            latitude=46.5010016,
            longitude=15.7546307,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Durango",
            state_code="DUR",
            latitude=37.27528,
            longitude=-107.8800667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Durazno",
            state_code="DU",
            latitude=-33.0232454,
            longitude=-56.0284644,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Durbe Municipality",
            state_code="028",
            latitude=56.6279857,
            longitude=21.4916245,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Durrës County",
            state_code="02",
            latitude=41.5080972,
            longitude=19.6163185,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Durrës District",
            state_code="DR",
            latitude=41.3706517,
            longitude=19.5211063,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Düzce",
            state_code="81",
            latitude=40.8770531,
            longitude=31.3192713,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="East",
            state_code="ES",
            latitude=39.0185336,
            longitude=-94.2792411,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cameroon")][0]),
        ))
        list_of_states.append(State(
            name="East Attica Regional Unit",
            state_code="A2",
            latitude=38.2054093,
            longitude=23.8584737,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="East Ayrshire",
            state_code="EAY",
            latitude=55.4518496,
            longitude=-4.2644478,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="East Azerbaijan",
            state_code="03",
            latitude=37.9035733,
            longitude=46.2682109,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="East Berbice-Corentyne",
            state_code="EB",
            latitude=2.7477922,
            longitude=-57.4627259,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guyana")][0]),
        ))
        list_of_states.append(State(
            name="East Darfur",
            state_code="DE",
            latitude=14.3782747,
            longitude=24.9042208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="East Dunbartonshire",
            state_code="EDU",
            latitude=55.9743162,
            longitude=-4.202298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="East Flanders",
            state_code="VOV",
            latitude=51.0362101,
            longitude=3.7373124,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="East Grand Bahama",
            state_code="EG",
            latitude=26.6582823,
            longitude=-78.2248291,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="East Kazakhstan Region",
            state_code="VOS",
            latitude=48.7062687,
            longitude=80.7922534,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="East Lothian",
            state_code="ELN",
            latitude=55.9493383,
            longitude=-2.7704464,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="East Macedonia and Thrace",
            state_code="A",
            latitude=41.1295126,
            longitude=24.8877191,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="East New Britain",
            state_code="EBR",
            latitude=-4.6128943,
            longitude=151.8877321,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="East Renfrewshire",
            state_code="ERW",
            latitude=55.7704735,
            longitude=-4.3359821,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="East Riding of Yorkshire",
            state_code="ERY",
            latitude=53.8416168,
            longitude=-0.4344106,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (5/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
