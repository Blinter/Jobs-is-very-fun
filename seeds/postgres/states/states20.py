"""
States Seed #20

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
            name="Varakļāni Municipality",
            state_code="102",
            latitude=56.6688006,
            longitude=26.5636414,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Varaždin",
            state_code="05",
            latitude=46.2317473,
            longitude=16.3360559,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Varėna District Municipality",
            state_code="55",
            latitude=54.220333,
            longitude=24.578997,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Varese",
            state_code="VA",
            latitude=45.799026,
            longitude=8.7300945,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Vārkava Municipality",
            state_code="103",
            latitude=56.2465744,
            longitude=26.5664371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Värmland County",
            state_code="S",
            latitude=59.7294065,
            longitude=13.2354024,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Varna Province",
            state_code="03",
            latitude=43.2046477,
            longitude=27.9105488,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Vas County",
            state_code="VA",
            latitude=47.0929111,
            longitude=16.6812183,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Vasilevo Municipality",
            state_code="11",
            latitude=41.4741699,
            longitude=22.6422128,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Vaslui County",
            state_code="VS",
            latitude=46.4631059,
            longitude=27.7398031,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Västerbotten County",
            state_code="AC",
            latitude=65.3337311,
            longitude=16.5161694,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Västernorrland County",
            state_code="Y",
            latitude=63.4276473,
            longitude=17.7292444,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Västmanland County",
            state_code="U",
            latitude=59.6713879,
            longitude=16.2158953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Västra Götaland County",
            state_code="O",
            latitude=58.2527926,
            longitude=13.0596425,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Vaucluse",
            state_code="84",
            latitude=44.04475,
            longitude=4.6427718,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Vaud",
            state_code="VD",
            latitude=46.5613135,
            longitude=6.536765,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Vaupés",
            state_code="VAU",
            latitude=0.8553561,
            longitude=-70.8119953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Vavaʻu",
            state_code="05",
            latitude=-18.622756,
            longitude=-173.9902982,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tonga")][0]),
        ))
        list_of_states.append(State(
            name="Vavuniya District",
            state_code="44",
            latitude=8.7594739,
            longitude=80.5000334,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Vayots Dzor Region",
            state_code="VD",
            latitude=39.7641996,
            longitude=45.3337528,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Armenia")][0]),
        ))
        list_of_states.append(State(
            name="Vecpiebalga Municipality",
            state_code="104",
            latitude=57.0603356,
            longitude=25.8161592,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Vecumnieki Municipality",
            state_code="105",
            latitude=56.6062337,
            longitude=24.5221891,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Vega Alta",
            state_code="143",
            latitude=18.4121703,
            longitude=-66.3312805,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Vega Baja",
            state_code="145",
            latitude=18.4461459,
            longitude=-66.4041967,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Veles Municipality",
            state_code="13",
            latitude=41.7274426,
            longitude=21.7137694,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Velika Polana Municipality",
            state_code="187",
            latitude=46.5731715,
            longitude=16.3444126,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Velike Lašče Municipality",
            state_code="134",
            latitude=45.8336591,
            longitude=14.6362363,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Veliko Tarnovo Province",
            state_code="04",
            latitude=43.0756539,
            longitude=25.61715,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Vendée",
            state_code="85",
            latitude=46.6754103,
            longitude=-2.0298392,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Veneto",
            state_code="34",
            latitude=45.4414662,
            longitude=12.3152595,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Ventspils",
            state_code="VEN",
            latitude=57.3937216,
            longitude=21.5647066,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Ventspils Municipality",
            state_code="106",
            latitude=57.2833682,
            longitude=21.8587558,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Veracruz de Ignacio de la Llave",
            state_code="VER",
            latitude=19.173773,
            longitude=-96.1342241,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Veraguas Province",
            state_code="9",
            latitude=8.1231033,
            longitude=-81.0754657,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Verbano-Cusio-Ossola",
            state_code="VB",
            latitude=46.1399688,
            longitude=8.2724649,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Vercelli",
            state_code="VC",
            latitude=45.3202204,
            longitude=8.418508,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Vermont",
            state_code="VT",
            latitude=44.5588028,
            longitude=-72.5778415,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Verona",
            state_code="VR",
            latitude=45.4418498,
            longitude=11.0735316,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Veržej Municipality",
            state_code="188",
            latitude=46.5841135,
            longitude=16.16208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Vestfold og Telemark",
            state_code="38",
            latitude=59.4117482,
            longitude=7.7647175,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Vestland",
            state_code="46",
            latitude=60.9069442,
            longitude=3.9627081,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Veszprém",
            state_code="VM",
            latitude=47.1028087,
            longitude=17.9093019,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Veszprém County",
            state_code="VE",
            latitude=47.0930974,
            longitude=17.9100763,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Vevčani Municipality",
            state_code="12",
            latitude=41.2407543,
            longitude=20.5915649,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Viana do Castelo",
            state_code="16",
            latitude=41.6918046,
            longitude=-8.834451,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Vibo Valentia",
            state_code="VV",
            latitude=38.6378565,
            longitude=16.2051484,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Vicenza",
            state_code="VI",
            latitude=45.6983995,
            longitude=11.5661465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Vichada",
            state_code="VID",
            latitude=4.4234452,
            longitude=-69.2877535,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Victoria",
            state_code="VIC",
            latitude=-36.4856423,
            longitude=140.9779425,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Australia")][0]),
        ))
        list_of_states.append(State(
            name="Victoria",
            state_code="45",
            latitude=28.8052674,
            longitude=-97.0035982,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Videm Municipality",
            state_code="135",
            latitude=46.363833,
            longitude=15.8781212,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Vidin Province",
            state_code="05",
            latitude=43.9961739,
            longitude=22.8679515,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Vienna",
            state_code="9",
            latitude=48.2081743,
            longitude=16.3738189,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Austria")][0]),
        ))
        list_of_states.append(State(
            name="Vienne",
            state_code="86",
            latitude=45.5221314,
            longitude=4.8453136,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Vientiane Prefecture",
            state_code="VT",
            latitude=18.110541,
            longitude=102.5298028,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Vientiane Province",
            state_code="VI",
            latitude=18.5705063,
            longitude=102.6216211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Vieques",
            state_code="147",
            latitude=18.1262854,
            longitude=-65.4400985,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Viesīte Municipality",
            state_code="107",
            latitude=56.3113085,
            longitude=25.5070464,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Vieux Fort Quarter",
            state_code="11",
            latitude=13.720608,
            longitude=-60.9496433,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Vihiga",
            state_code="45",
            latitude=0.0767553,
            longitude=34.7077665,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Viken",
            state_code="30",
            latitude=59.9653005,
            longitude=7.4505144,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Vila Real",
            state_code="17",
            latitude=41.3003527,
            longitude=-7.7457274,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Viļaka Municipality",
            state_code="108",
            latitude=57.1722263,
            longitude=27.6673188,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Viļāni Municipality",
            state_code="109",
            latitude=56.5456171,
            longitude=26.9167927,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Viljandi County",
            state_code="84",
            latitude=58.2821746,
            longitude=25.5752233,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Vilkaviškis District Municipality",
            state_code="56",
            latitude=54.651945,
            longitude=23.035155,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Villa Clara Province",
            state_code="05",
            latitude=22.4937204,
            longitude=-79.9192702,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Villalba",
            state_code="149",
            latitude=18.1217554,
            longitude=-66.4985787,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Vilnius City Municipality",
            state_code="57",
            latitude=54.6710761,
            longitude=25.2878721,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Vilnius County",
            state_code="VL",
            latitude=54.8086502,
            longitude=25.2182139,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Vilnius District Municipality",
            state_code="58",
            latitude=54.7732578,
            longitude=25.5867113,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Vĩnh Long",
            state_code="49",
            latitude=10.239574,
            longitude=105.9571928,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Vĩnh Phúc",
            state_code="70",
            latitude=21.3608805,
            longitude=105.5474373,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Vinica Municipality",
            state_code="14",
            latitude=41.857102,
            longitude=22.5721881,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Vinnytska oblast",
            state_code="05",
            latitude=49.233083,
            longitude=28.4682169,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Vipava Municipality",
            state_code="136",
            latitude=45.8412674,
            longitude=13.9609613,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Viqueque Municipality",
            state_code="VI",
            latitude=-8.8597918,
            longitude=126.3633516,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Timor-Leste")][0]),
        ))
        list_of_states.append(State(
            name="Virginia",
            state_code="VA",
            latitude=37.4315734,
            longitude=-78.6568942,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Virovitica-Podravina",
            state_code="10",
            latitude=45.6557985,
            longitude=17.7932472,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Visaginas Municipality",
            state_code="59",
            latitude=55.594118,
            longitude=26.4307954,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Viseu",
            state_code="18",
            latitude=40.6588424,
            longitude=-7.914756,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Vitanje Municipality",
            state_code="137",
            latitude=46.3815323,
            longitude=15.2950687,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Vitebsk Region",
            state_code="VI",
            latitude=55.2959833,
            longitude=28.7583627,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belarus")][0]),
        ))
        list_of_states.append(State(
            name="Viterbo",
            state_code="VT",
            latitude=42.400242,
            longitude=11.8891721,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Vladimir Oblast",
            state_code="VLA",
            latitude=56.1553465,
            longitude=40.5926685,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Vlorë County",
            state_code="12",
            latitude=40.150096,
            longitude=19.8067916,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Vlorë District",
            state_code="VL",
            latitude=40.4660668,
            longitude=19.491356,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Vodice Municipality",
            state_code="138",
            latitude=46.1896643,
            longitude=14.4938539,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Vojnik Municipality",
            state_code="139",
            latitude=46.2920581,
            longitude=15.302058,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Vojvodina",
            state_code="VO",
            latitude=45.2608651,
            longitude=19.8319338,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Volgograd Oblast",
            state_code="VGG",
            latitude=49.2587393,
            longitude=39.8154463,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Vologda Oblast",
            state_code="VLG",
            latitude=59.8706711,
            longitude=40.6555411,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Volta",
            state_code="TV",
            latitude=6.5781373,
            longitude=0.4502368,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Volynska oblast",
            state_code="07",
            latitude=50.747233,
            longitude=25.325383,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Vorarlberg",
            state_code="8",
            latitude=47.2497427,
            longitude=9.9797373,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Austria")][0]),
        ))
        list_of_states.append(State(
            name="Voronezh Oblast",
            state_code="VOR",
            latitude=50.8589713,
            longitude=39.8644374,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Võru County",
            state_code="86",
            latitude=57.7377372,
            longitude=27.1398938,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Vosges",
            state_code="88",
            latitude=48.1630173,
            longitude=5.73556,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Vrancea County",
            state_code="VN",
            latitude=45.8134876,
            longitude=27.0657531,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Vraneštica Municipality",
            state_code="15",
            latitude=41.4829087,
            longitude=21.0579632,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Vransko Municipality",
            state_code="189",
            latitude=46.239006,
            longitude=14.9527249,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Vrapčište Municipality",
            state_code="16",
            latitude=41.879116,
            longitude=20.83145,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Vratsa Province",
            state_code="06",
            latitude=43.2101806,
            longitude=23.552921,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Vrhnika Municipality",
            state_code="140",
            latitude=45.9502719,
            longitude=14.3276422,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Vsetín",
            state_code="723",
            latitude=49.379325,
            longitude=18.0618162,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Vukovar-Syrmia",
            state_code="16",
            latitude=45.1773552,
            longitude=18.8053527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Vuzenica Municipality",
            state_code="141",
            latitude=46.5980836,
            longitude=15.1657237,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Vyškov",
            state_code="646",
            latitude=49.2127445,
            longitude=16.9855927,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Wadi al Hayaa District",
            state_code="WD",
            latitude=26.4225926,
            longitude=12.6216211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Wadi al Shatii District",
            state_code="WS",
            latitude=27.7351468,
            longitude=12.4380581,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Wadi Fira",
            state_code="WF",
            latitude=15.0892416,
            longitude=21.4752851,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Waikato Region",
            state_code="WKO",
            latitude=-37.6190862,
            longitude=175.023346,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Wajir",
            state_code="46",
            latitude=1.6360475,
            longitude=40.3088626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Wakayama Prefecture",
            state_code="30",
            latitude=33.9480914,
            longitude=135.3745358,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Wake Island",
            state_code="UM-79",
            latitude=19.279619,
            longitude=166.6499348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Wake Island",
            state_code="79",
            latitude=19.279619,
            longitude=166.6499348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States Minor Outlying Islands")][0]),
        ))
        list_of_states.append(State(
            name="Wakefield",
            state_code="WKF",
            latitude=42.5039395,
            longitude=-71.0723391,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Wakiso District",
            state_code="113",
            latitude=0.063019,
            longitude=32.4467238,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Wales",
            state_code="WLS",
            latitude=52.1306607,
            longitude=-3.7837117,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Wallis and Futuna",
            state_code="WF",
            latitude=-14.2938,
            longitude=-178.1165,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Wallonia",
            state_code="WAL",
            latitude=50.4175637,
            longitude=4.4510066,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="Walloon Brabant",
            state_code="WBR",
            latitude=50.633241,
            longitude=4.524315,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="Walsall",
            state_code="WLL",
            latitude=52.586214,
            longitude=-1.982919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Wan Chai",
            state_code="HWC",
            latitude=22.27968,
            longitude=114.17168,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Wangdue Phodrang District",
            state_code="24",
            latitude=27.4526046,
            longitude=90.0674928,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Wanica District",
            state_code="WA",
            latitude=5.7323762,
            longitude=-55.2701235,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Suriname")][0]),
        ))
        list_of_states.append(State(
            name="Warmian-Masurian Voivodeship",
            state_code="WN",
            latitude=53.8671117,
            longitude=20.7027861,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Warrap",
            state_code="WR",
            latitude=8.0886238,
            longitude=28.6410641,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Warrington",
            state_code="WRT",
            latitude=40.2492741,
            longitude=-75.1340604,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Warwick",
            state_code="WAR",
            latitude=32.2661534,
            longitude=-64.8081198,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bermuda")][0]),
        ))
        list_of_states.append(State(
            name="Warwickshire",
            state_code="WAR",
            latitude=52.2671353,
            longitude=-1.4675216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Washington",
            state_code="WA",
            latitude=47.7510741,
            longitude=-120.7401385,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Wasit",
            state_code="WA",
            latitude=32.6024094,
            longitude=45.7520985,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Waterford",
            state_code="WD",
            latitude=52.1943549,
            longitude=-7.6227512,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Wele-Nzas Province",
            state_code="WN",
            latitude=1.4166162,
            longitude=11.0711758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Equatorial Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Wellington Region",
            state_code="WGN",
            latitude=-41.0299323,
            longitude=175.4375574,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="West",
            state_code="OU",
            latitude=37.0364989,
            longitude=-95.6705987,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cameroon")][0]),
        ))
        list_of_states.append(State(
            name="West Azarbaijan",
            state_code="04",
            latitude=37.4550062,
            longitude=45,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="West Bačka District",
            state_code="05",
            latitude=45.7355385,
            longitude=19.1897364,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="West Bengal",
            state_code="WB",
            latitude=22.9867569,
            longitude=87.8549755,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="West Berkshire",
            state_code="WBK",
            latitude=51.4308255,
            longitude=-1.1444927,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="West Coast Division",
            state_code="W",
            latitude=5.9772798,
            longitude=116.0754288,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gambia The")][0]),
        ))
        list_of_states.append(State(
            name="West Coast Region",
            state_code="WTC",
            latitude=62.4113634,
            longitude=-149.0729714,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="West Darfur",
            state_code="DW",
            latitude=12.8463561,
            longitude=23.0011989,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="West Dunbartonshire",
            state_code="WDU",
            latitude=55.9450925,
            longitude=-4.5646259,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="West Flanders",
            state_code="VWV",
            latitude=51.0404747,
            longitude=2.9994213,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="West Grand Bahama",
            state_code="WG",
            latitude=26.659447,
            longitude=-78.52065,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="West Greece Region",
            state_code="G",
            latitude=38.5115496,
            longitude=21.5706786,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="West Herzegovina Canton",
            state_code="08",
            latitude=43.4369244,
            longitude=17.3848831,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="West Kazakhstan Province",
            state_code="ZAP",
            latitude=49.5679727,
            longitude=50.8066616,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="West Kordofan",
            state_code="GK",
            latitude=11.1990192,
            longitude=29.4179324,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="West Lothian",
            state_code="WLN",
            latitude=55.9070198,
            longitude=-3.5517167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="West Macedonia Region",
            state_code="C",
            latitude=40.3004058,
            longitude=21.7903559,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="West New Britain Province",
            state_code="WBK",
            latitude=-5.7047432,
            longitude=150.0259466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="West Pokot",
            state_code="47",
            latitude=1.6210076,
            longitude=35.3905046,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="West Pomeranian Voivodeship",
            state_code="ZP",
            latitude=53.4657891,
            longitude=15.1822581,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="West Sussex",
            state_code="WSX",
            latitude=50.9280143,
            longitude=-0.4617075,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="West Virginia",
            state_code="WV",
            latitude=38.5976262,
            longitude=-80.4549026,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Western",
            state_code="WP",
            latitude=5.5,
            longitude=-2.5,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Western Area",
            state_code="W",
            latitude=40.2545969,
            longitude=-80.2455444,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sierra Leone")][0]),
        ))
        list_of_states.append(State(
            name="Western Australia",
            state_code="WA",
            latitude=-27.6728168,
            longitude=121.6283098,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Australia")][0]),
        ))
        list_of_states.append(State(
            name="Western Bahr el Ghazal",
            state_code="BW",
            latitude=8.6452399,
            longitude=25.2837585,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Western Cape",
            state_code="WC",
            latitude=-33.2277918,
            longitude=21.8568586,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Africa")][0]),
        ))
        list_of_states.append(State(
            name="Western Division",
            state_code="W",
            latitude=42.9662198,
            longitude=-78.7021134,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Western Equatoria",
            state_code="EW",
            latitude=5.3471799,
            longitude=28.299435,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Western Highlands Province",
            state_code="WHM",
            latitude=-5.6268128,
            longitude=144.2593118,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Western North",
            state_code="WN",
            latitude=6.3,
            longitude=-2.8,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Western Province",
            state_code="WPD",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Western Province",
            state_code="04",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Rwanda")][0]),
        ))
        list_of_states.append(State(
            name="Western Province",
            state_code="WE",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Solomon Islands")][0]),
        ))
        list_of_states.append(State(
            name="Western Province",
            state_code="1",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Western Province",
            state_code="01",
            latitude=6.9016086,
            longitude=80.0087746,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zambia")][0]),
        ))
        list_of_states.append(State(
            name="Western Region",
            state_code="3",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iceland")][0]),
        ))
        list_of_states.append(State(
            name="Western Region",
            state_code="3",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Western Region",
            state_code="W",
            latitude=40.7667215,
            longitude=-111.8877203,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Western Samar",
            state_code="WSA",
            latitude=12.0000206,
            longitude=124.9912452,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Western Tobago",
            state_code="WTO",
            latitude=11.1897072,
            longitude=-60.7795452,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Western Visayas",
            state_code="06",
            latitude=11.0049836,
            longitude=122.5372741,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Westfjords",
            state_code="4",
            latitude=65.919615,
            longitude=-21.8811764,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iceland")][0]),
        ))
        list_of_states.append(State(
            name="Westmeath",
            state_code="WH",
            latitude=53.5345308,
            longitude=-7.4653217,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Westmoreland Parish",
            state_code="10",
            latitude=18.2944378,
            longitude=-78.1564432,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Wexford",
            state_code="WX",
            latitude=52.4793603,
            longitude=-6.5839913,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="White Nile",
            state_code="NW",
            latitude=9.3321516,
            longitude=31.46153,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Wicklow",
            state_code="WW",
            latitude=52.9862313,
            longitude=-6.3672543,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Wiltshire",
            state_code="WIL",
            latitude=51.3491996,
            longitude=-1.9927105,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Windsor and Maidenhead",
            state_code="WNM",
            latitude=51.4799712,
            longitude=-0.6242565,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Wirral",
            state_code="WRL",
            latitude=53.3727181,
            longitude=-3.073754,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Wisconsin",
            state_code="WI",
            latitude=43.7844397,
            longitude=-88.7878678,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Wokingham",
            state_code="WOK",
            latitude=51.410457,
            longitude=-0.833861,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Woleu-Ntem Province",
            state_code="9",
            latitude=2.2989827,
            longitude=11.4466914,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gabon")][0]),
        ))
        list_of_states.append(State(
            name="Wong Tai Sin",
            state_code="KWT",
            latitude=22.33353,
            longitude=114.19686,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Worcestershire",
            state_code="WOR",
            latitude=52.2545225,
            longitude=-2.2668382,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Woroba District",
            state_code="WR",
            latitude=8.2491372,
            longitude=-6.9209135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Worodougou",
            state_code="14",
            latitude=8.2548962,
            longitude=-6.5783387,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Wrexham County Borough",
            state_code="WRX",
            latitude=53.0301378,
            longitude=-3.0261487,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Wyoming",
            state_code="WY",
            latitude=43.0759678,
            longitude=-107.2902839,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Xagħra",
            state_code="61",
            latitude=36.050845,
            longitude=14.267482,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Xaisomboun",
            state_code="XN",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Xaisomboun Province",
            state_code="XS",
            latitude=18.4362924,
            longitude=104.4723301,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Xewkija",
            state_code="62",
            latitude=36.0299236,
            longitude=14.2599437,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Xgħajra",
            state_code="63",
            latitude=35.8868282,
            longitude=14.5472391,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Xiangkhouang Province",
            state_code="XI",
            latitude=19.6093003,
            longitude=103.7289167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Xinjiang",
            state_code="XJ",
            latitude=42.5246357,
            longitude=87.5395855,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Xizang",
            state_code="XZ",
            latitude=30.1533605,
            longitude=88.7878678,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Xorazm Region",
            state_code="XO",
            latitude=41.3565336,
            longitude=60.8566686,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Yabucoa",
            state_code="151",
            latitude=18.0505201,
            longitude=-65.8793288,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Yagha Province",
            state_code="YAG",
            latitude=13.3576157,
            longitude=0.7532809,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Yala",
            state_code="95",
            latitude=44.0579117,
            longitude=-123.1653848,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Yalova",
            state_code="77",
            latitude=40.5775986,
            longitude=29.2088303,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Yamagata Prefecture",
            state_code="06",
            latitude=38.5370564,
            longitude=140.1435198,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Yamaguchi Prefecture",
            state_code="35",
            latitude=34.2796769,
            longitude=131.5212742,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Yamalo-Nenets Autonomous Okrug",
            state_code="YAN",
            latitude=66.0653057,
            longitude=76.9345193,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Yamanashi Prefecture",
            state_code="19",
            latitude=35.6635113,
            longitude=138.6388879,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Yambol Province",
            state_code="28",
            latitude=42.4841494,
            longitude=26.5035296,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Yamoussoukro",
            state_code="YM",
            latitude=6.8276228,
            longitude=-5.2893433,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Yangon Region",
            state_code="06",
            latitude=16.9143488,
            longitude=96.1526985,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Yap State",
            state_code="YAP",
            latitude=8.671649,
            longitude=142.8439335,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Micronesia")][0]),
        ))
        list_of_states.append(State(
            name="Yaracuy",
            state_code="U",
            latitude=10.339389,
            longitude=-68.8108849,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Yardymli District",
            state_code="YAR",
            latitude=38.9058917,
            longitude=48.2496127,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Yaren District",
            state_code="14",
            latitude=-0.5466857,
            longitude=166.9210913,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nauru")][0]),
        ))
        list_of_states.append(State(
            name="Yaroslavl Oblast",
            state_code="YAR",
            latitude=57.8991523,
            longitude=38.8388633,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Yasothon",
            state_code="35",
            latitude=15.792641,
            longitude=104.1452827,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Yatenga Province",
            state_code="YAT",
            latitude=13.6249344,
            longitude=-2.3813621,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Yau Tsim Mong",
            state_code="KYT",
            latitude=22.32138,
            longitude=114.1726,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Yauco",
            state_code="153",
            latitude=18.034964,
            longitude=-66.8498983,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Yazd",
            state_code="21",
            latitude=32.1006387,
            longitude=54.4342138,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Yên Bái",
            state_code="06",
            latitude=21.7167689,
            longitude=104.8985878,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Yerevan",
            state_code="ER",
            latitude=40.1872023,
            longitude=44.515209,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Armenia")][0]),
        ))
        list_of_states.append(State(
            name="Yevlakh",
            state_code="YE",
            latitude=40.6196638,
            longitude=47.1500324,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Yevlakh District",
            state_code="YEV",
            latitude=40.6196638,
            longitude=47.1500324,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Yilan",
            state_code="ILA",
            latitude=24.7021073,
            longitude=121.7377502,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Yobe",
            state_code="YO",
            latitude=12.293876,
            longitude=11.4390411,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Yomou Prefecture",
            state_code="YO",
            latitude=7.5696279,
            longitude=-9.2591571,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Yonne",
            state_code="89",
            latitude=47.8547614,
            longitude=3.0339404,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Yoro Department",
            state_code="YO",
            latitude=15.2949679,
            longitude=-87.1422895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Youssoufia",
            state_code="YUS",
            latitude=32.0200679,
            longitude=-8.8692648,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Yozgat",
            state_code="66",
            latitude=39.7271979,
            longitude=35.1077858,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Yucatán",
            state_code="YUC",
            latitude=20.7098786,
            longitude=-89.0943377,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Yuen Long",
            state_code="NYL",
            latitude=22.44559,
            longitude=114.02218,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Yukon",
            state_code="YT",
            latitude=35.5067215,
            longitude=-97.7625441,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Yumbe District",
            state_code="313",
            latitude=3.4698023,
            longitude=31.2483291,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Yunlin",
            state_code="YUN",
            latitude=23.7092033,
            longitude=120.4313373,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Yunnan",
            state_code="YN",
            latitude=24.4752847,
            longitude=101.3431058,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Yvelines",
            state_code="78",
            latitude=48.7615301,
            longitude=1.2772949,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Zabaykalsky Krai",
            state_code="ZAB",
            latitude=53.0928771,
            longitude=116.9676561,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Żabbar",
            state_code="64",
            latitude=35.8724715,
            longitude=14.5451354,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Žabljak Municipality",
            state_code="21",
            latitude=43.1555152,
            longitude=19.1226018,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Zabul",
            state_code="ZAB",
            latitude=32.1918782,
            longitude=67.1894488,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Zacatecas",
            state_code="ZAC",
            latitude=22.7708555,
            longitude=-102.5832426,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Zadar",
            state_code="13",
            latitude=44.146939,
            longitude=15.6164943,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (20/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
