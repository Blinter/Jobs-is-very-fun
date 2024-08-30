"""
States Seed #14

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
            name="Odisha",
            state_code="OR",
            latitude=20.9516658,
            longitude=85.0985236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Odranci Municipality",
            state_code="086",
            latitude=46.5901017,
            longitude=16.2788165,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Offaly",
            state_code="OY",
            latitude=53.2356871,
            longitude=-7.7122229,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Oghuz District",
            state_code="OGU",
            latitude=41.0727924,
            longitude=47.4650672,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Ogooué-Ivindo Province",
            state_code="6",
            latitude=0.8818311,
            longitude=13.1740348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gabon")][0]),
        ))
        list_of_states.append(State(
            name="Ogooué-Lolo Province",
            state_code="7",
            latitude=-0.8844093,
            longitude=12.4380581,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gabon")][0]),
        ))
        list_of_states.append(State(
            name="Ogooué-Maritime Province",
            state_code="8",
            latitude=-1.3465975,
            longitude=9.7232673,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gabon")][0]),
        ))
        list_of_states.append(State(
            name="Ogre Municipality",
            state_code="067",
            latitude=56.8147355,
            longitude=24.6044555,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Ogun",
            state_code="OG",
            latitude=6.9979747,
            longitude=3.4737378,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Ohangwena Region",
            state_code="OW",
            latitude=-17.5979291,
            longitude=16.8178377,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Ohio",
            state_code="OH",
            latitude=40.4172871,
            longitude=-82.907123,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Ohrid Municipality",
            state_code="58",
            latitude=41.0682088,
            longitude=20.7599266,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Oio Region",
            state_code="OI",
            latitude=12.2760709,
            longitude=-15.3131185,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea-Bissau")][0]),
        ))
        list_of_states.append(State(
            name="Oise",
            state_code="60",
            latitude=49.4117335,
            longitude=1.8668825,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Ōita Prefecture",
            state_code="44",
            latitude=33.1589299,
            longitude=131.3611121,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Okayama Prefecture",
            state_code="33",
            latitude=34.8963407,
            longitude=133.6375314,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Okinawa Prefecture",
            state_code="47",
            latitude=26.1201911,
            longitude=127.7025012,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Oklahoma",
            state_code="OK",
            latitude=35.4675602,
            longitude=-97.5164276,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Olaine Municipality",
            state_code="068",
            latitude=56.7952353,
            longitude=24.0153589,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Olancho Department",
            state_code="OL",
            latitude=14.8067406,
            longitude=-85.7666645,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Old Royal Capital Cetinje",
            state_code="06",
            latitude=42.3930959,
            longitude=18.9115964,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Oldham",
            state_code="OLD",
            latitude=42.2040598,
            longitude=-71.2048119,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Olomouc",
            state_code="712",
            latitude=49.593778,
            longitude=17.2508787,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Olomoucký kraj",
            state_code="71",
            latitude=49.6586549,
            longitude=17.0811406,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Olt County",
            state_code="OT",
            latitude=44.200797,
            longitude=24.5022981,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Omagh District Council",
            state_code="OMH",
            latitude=54.4513524,
            longitude=-7.7125018,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Omaheke Region",
            state_code="OH",
            latitude=-21.8466651,
            longitude=19.1880047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Ombella-M'Poko Prefecture",
            state_code="MP",
            latitude=5.1188825,
            longitude=18.4276047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Ömnögovi Province",
            state_code="053",
            latitude=43.500024,
            longitude=104.2861116,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Omoro District",
            state_code="331",
            latitude=2.715223,
            longitude=32.4920088,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Omsk Oblast",
            state_code="OMS",
            latitude=55.0554669,
            longitude=73.3167342,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Omusati Region",
            state_code="OS",
            latitude=-18.4070294,
            longitude=14.8454619,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Ondo",
            state_code="ON",
            latitude=6.9148682,
            longitude=5.1478144,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Ontario",
            state_code="ON",
            latitude=51.253775,
            longitude=-85.323214,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Opava",
            state_code="805",
            latitude=49.9083757,
            longitude=17.916338,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Oplotnica",
            state_code="171",
            latitude=46.387163,
            longitude=15.4458131,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Opole Voivodeship",
            state_code="OP",
            latitude=50.8003761,
            longitude=17.937989,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Oran",
            state_code="31",
            latitude=35.6082351,
            longitude=-0.563609,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Orange Walk District",
            state_code="OW",
            latitude=17.760353,
            longitude=-88.864698,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belize")][0]),
        ))
        list_of_states.append(State(
            name="Ordino",
            state_code="05",
            latitude=42.5994433,
            longitude=1.5402327,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Andorra")][0]),
        ))
        list_of_states.append(State(
            name="Ordu",
            state_code="52",
            latitude=40.799058,
            longitude=37.3899005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Ordubad District",
            state_code="ORD",
            latitude=38.9021622,
            longitude=46.0237625,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Örebro County",
            state_code="T",
            latitude=59.535036,
            longitude=15.0065731,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Oregon",
            state_code="OR",
            latitude=43.8041334,
            longitude=-120.5542012,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Orellana",
            state_code="D",
            latitude=-0.4545163,
            longitude=-76.9950286,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Orenburg Oblast",
            state_code="ORE",
            latitude=51.7634026,
            longitude=54.6188188,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Orhei District",
            state_code="OR",
            latitude=47.38604,
            longitude=28.8303082,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Oriental Mindoro",
            state_code="MDR",
            latitude=13.0564598,
            longitude=121.4069417,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Oristano",
            state_code="OR",
            latitude=40.0599068,
            longitude=8.7481167,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Orkhon Province",
            state_code="035",
            latitude=49.004705,
            longitude=104.3016527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Orkney Islands",
            state_code="ORK",
            latitude=58.9809401,
            longitude=-2.9605206,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ormož Municipality",
            state_code="087",
            latitude=46.4353333,
            longitude=16.154374,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Orne",
            state_code="61",
            latitude=48.5757644,
            longitude=-0.5024295,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Oro Province",
            state_code="NPP",
            latitude=-8.8988063,
            longitude=148.1892921,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Orocovis",
            state_code="107",
            latitude=18.2269224,
            longitude=-66.3911686,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Oromia Region",
            state_code="OR",
            latitude=7.5460377,
            longitude=40.6346851,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ethiopia")][0]),
        ))
        list_of_states.append(State(
            name="Oruro Department",
            state_code="O",
            latitude=-18.5711579,
            longitude=-67.7615983,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bolivia")][0]),
        ))
        list_of_states.append(State(
            name="Oryol Oblast",
            state_code="ORL",
            latitude=52.7856414,
            longitude=36.9242344,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Ōsaka Prefecture",
            state_code="27",
            latitude=34.6413315,
            longitude=135.5629394,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Osh",
            state_code="GO",
            latitude=36.0631399,
            longitude=-95.9182895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kyrgyzstan")][0]),
        ))
        list_of_states.append(State(
            name="Osh Region",
            state_code="O",
            latitude=39.8407366,
            longitude=72.8988069,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kyrgyzstan")][0]),
        ))
        list_of_states.append(State(
            name="Oshana Region",
            state_code="ON",
            latitude=-18.4305064,
            longitude=15.6881788,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Oshikoto Region",
            state_code="OT",
            latitude=-18.4152575,
            longitude=16.912251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Osijek-Baranja",
            state_code="14",
            latitude=45.5576428,
            longitude=18.3942141,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Osilnica Municipality",
            state_code="088",
            latitude=45.5418467,
            longitude=14.7156303,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Oslo",
            state_code="03",
            latitude=59.9138688,
            longitude=10.7522454,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Oslomej Municipality",
            state_code="57",
            latitude=41.5758391,
            longitude=21.022196,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Osmaniye",
            state_code="80",
            latitude=37.2130258,
            longitude=36.1762615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Östergötland County",
            state_code="E",
            latitude=58.3453635,
            longitude=15.5197844,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sweden")][0]),
        ))
        list_of_states.append(State(
            name="Ostrava-město",
            state_code="806",
            latitude=49.8209226,
            longitude=18.2625243,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Ostrobothnia",
            state_code="12",
            latitude=63.1181757,
            longitude=21.9061062,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Osun",
            state_code="OS",
            latitude=7.5628964,
            longitude=4.5199593,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Otago Region",
            state_code="OTA",
            latitude=-45.4790671,
            longitude=170.1547567,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Oti",
            state_code="OT",
            latitude=7.9,
            longitude=0.3,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Otjozondjupa Region",
            state_code="OD",
            latitude=-20.5486916,
            longitude=17.668887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Otuke District",
            state_code="329",
            latitude=2.5214059,
            longitude=33.3486147,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Ouaddaï",
            state_code="OD",
            latitude=13.748476,
            longitude=20.7122465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Ouaka Prefecture",
            state_code="UK",
            latitude=6.3168216,
            longitude=20.7122465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Ouargla",
            state_code="30",
            latitude=32.2264863,
            longitude=5.7299821,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Ouarzazate",
            state_code="OUA",
            latitude=30.9335436,
            longitude=-6.937016,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Oubritenga Province",
            state_code="OUB",
            latitude=12.7096087,
            longitude=-1.443469,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Oudalan Province",
            state_code="OUD",
            latitude=14.471902,
            longitude=-0.4502368,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Oudomxay Province",
            state_code="OU",
            latitude=20.4921929,
            longitude=101.8891721,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Oued Ed-Dahab (EH)",
            state_code="OUD",
            latitude=22.7337892,
            longitude=-14.2861116,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Ouémé Department",
            state_code="OU",
            latitude=6.6148152,
            longitude=2.4999918,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Ouest",
            state_code="OU",
            latitude=45.4547249,
            longitude=-73.6502365,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Haiti")][0]),
        ))
        list_of_states.append(State(
            name="Ouezzane",
            state_code="OUZ",
            latitude=34.806345,
            longitude=-5.5914505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Ouham Prefecture",
            state_code="AC",
            latitude=7.090911,
            longitude=17.668887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Ouham-Pendé Prefecture",
            state_code="OP",
            latitude=6.4850984,
            longitude=16.1580937,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Oujda-Angad",
            state_code="OUJ",
            latitude=34.6837504,
            longitude=-2.2993239,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Ouled Djellal",
            state_code="51",
            latitude=34.4178221,
            longitude=4.9685843,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Oum El Bouaghi",
            state_code="04",
            latitude=35.8688789,
            longitude=7.1108266,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Ourense",
            state_code="OR",
            latitude=42.3383613,
            longitude=-7.8811951,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Outer Hebrides",
            state_code="ELS",
            latitude=57.7598918,
            longitude=-7.0194034,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Overijssel",
            state_code="OV",
            latitude=52.4387814,
            longitude=6.5016411,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Övörkhangai Province",
            state_code="055",
            latitude=45.7624392,
            longitude=103.0917032,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Oxfordshire",
            state_code="OXF",
            latitude=51.7612056,
            longitude=-1.2464674,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Oyam District",
            state_code="321",
            latitude=2.2776281,
            longitude=32.4467238,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Oyo",
            state_code="OY",
            latitude=8.1573809,
            longitude=3.6146534,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Ozolnieki Municipality",
            state_code="069",
            latitude=56.6756305,
            longitude=23.8994816,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Pabna District",
            state_code="49",
            latitude=24.158505,
            longitude=89.4480718,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Pader District",
            state_code="312",
            latitude=2.9430682,
            longitude=32.8084496,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Padua",
            state_code="PD",
            latitude=45.3661864,
            longitude=11.8209139,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Pagėgiai municipality",
            state_code="29",
            latitude=55.172132,
            longitude=21.9683614,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Paget",
            state_code="PAG",
            latitude=32.281074,
            longitude=-64.7784787,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bermuda")][0]),
        ))
        list_of_states.append(State(
            name="Pahang",
            state_code="06",
            latitude=3.8126318,
            longitude=103.3256204,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Päijänne Tavastia",
            state_code="16",
            latitude=61.3230041,
            longitude=25.7322496,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Pailin",
            state_code="24",
            latitude=12.9092962,
            longitude=102.6675575,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Pakruojis District Municipality",
            state_code="30",
            latitude=56.0732605,
            longitude=23.9389906,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Paktia",
            state_code="PIA",
            latitude=33.706199,
            longitude=69.3831079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Paktika",
            state_code="PKA",
            latitude=32.2645386,
            longitude=68.5247149,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Pakwach District",
            state_code="332",
            latitude=2.4607141,
            longitude=31.4941738,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Palanga City Municipality",
            state_code="31",
            latitude=55.920198,
            longitude=21.0677614,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Palauli",
            state_code="PA",
            latitude=-13.7294579,
            longitude=-172.4536115,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Samoa")][0]),
        ))
        list_of_states.append(State(
            name="Palawan",
            state_code="PLW",
            latitude=9.8349493,
            longitude=118.7383615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Palencia",
            state_code="P",
            latitude=42.0096832,
            longitude=-4.5287949,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Palermo",
            state_code="PA",
            latitude=38.11569,
            longitude=13.3614868,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Pallisa District",
            state_code="210",
            latitude=1.2324206,
            longitude=33.7517723,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Palmyra Atoll",
            state_code="UM-95",
            latitude=5.8885026,
            longitude=-162.0786656,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Palmyra Atoll",
            state_code="95",
            latitude=5.8885026,
            longitude=-162.0786656,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States Minor Outlying Islands")][0]),
        ))
        list_of_states.append(State(
            name="Pampanga",
            state_code="PAM",
            latitude=15.079409,
            longitude=120.6199895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Pamplemousses",
            state_code="PA",
            latitude=-20.1136008,
            longitude=57.575926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Panamá Oeste Province",
            state_code="10",
            latitude=9.1196751,
            longitude=-79.2902133,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Panamá Province",
            state_code="8",
            latitude=9.1196751,
            longitude=-79.2902133,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Panchagarh District",
            state_code="52",
            latitude=26.2708705,
            longitude=88.5951751,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Pando Department",
            state_code="N",
            latitude=-10.7988901,
            longitude=-66.9988011,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bolivia")][0]),
        ))
        list_of_states.append(State(
            name="Panevėžys City Municipality",
            state_code="32",
            latitude=55.7347915,
            longitude=24.3574774,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Panevėžys County",
            state_code="PN",
            latitude=55.9748049,
            longitude=25.0794767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Panevėžys District Municipality",
            state_code="33",
            latitude=55.6166728,
            longitude=24.3142283,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Pangasinan",
            state_code="PAN",
            latitude=15.8949055,
            longitude=120.2863183,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Panjshir",
            state_code="PAN",
            latitude=38.8802391,
            longitude=-77.1717238,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Paola",
            state_code="39",
            latitude=38.5722353,
            longitude=-94.8791294,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Paphos District (Pafos)",
            state_code="05",
            latitude=34.9164594,
            longitude=32.4920088,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cyprus")][0]),
        ))
        list_of_states.append(State(
            name="Papua",
            state_code="PA",
            latitude=-5.0122202,
            longitude=141.3470159,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Papua Barat",
            state_code="PB",
            latitude=-1.3361154,
            longitude=133.1747162,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Pará",
            state_code="PA",
            latitude=-1.9981271,
            longitude=-54.9306152,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Para District",
            state_code="PR",
            latitude=5.4817318,
            longitude=-55.2259207,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Suriname")][0]),
        ))
        list_of_states.append(State(
            name="Paraguarí Department",
            state_code="9",
            latitude=-25.6262174,
            longitude=-57.1520642,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Paraíba",
            state_code="PB",
            latitude=-7.2399609,
            longitude=-36.7819505,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Paramaribo District",
            state_code="PM",
            latitude=5.8520355,
            longitude=-55.2038278,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Suriname")][0]),
        ))
        list_of_states.append(State(
            name="Paraná",
            state_code="PR",
            latitude=-25.2520888,
            longitude=-52.0215415,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Pardubice",
            state_code="532",
            latitude=49.9444479,
            longitude=16.2856916,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Pardubický kraj",
            state_code="53",
            latitude=49.9444479,
            longitude=16.2856916,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Pārgauja Municipality",
            state_code="070",
            latitude=57.3648122,
            longitude=24.9822045,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Paris",
            state_code="75C",
            latitude=48.856614,
            longitude=2.3522219,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Parma",
            state_code="PR",
            latitude=44.8015322,
            longitude=10.3279354,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Pärnu County",
            state_code="67",
            latitude=58.5261952,
            longitude=24.4020159,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Paro District",
            state_code="11",
            latitude=27.4285949,
            longitude=89.4166516,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Parwan",
            state_code="PAR",
            latitude=34.9630977,
            longitude=68.8108849,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Pas-de-Calais",
            state_code="62",
            latitude=50.5144699,
            longitude=1.811498,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Pasco",
            state_code="PAS",
            latitude=46.2305049,
            longitude=-119.0922316,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Passoré Province",
            state_code="PAS",
            latitude=12.8881221,
            longitude=-2.2236667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Pastaza",
            state_code="Y",
            latitude=-1.4882265,
            longitude=-78.0031057,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Pasvalys District Municipality",
            state_code="34",
            latitude=56.0604619,
            longitude=24.396291,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Pathum Thani",
            state_code="13",
            latitude=14.0208391,
            longitude=100.5250276,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Patillas",
            state_code="109",
            latitude=18.0037381,
            longitude=-66.0134059,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Pattani",
            state_code="94",
            latitude=6.7618308,
            longitude=101.3232549,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Pattaya",
            state_code="S",
            latitude=12.9235557,
            longitude=100.8824551,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Patuakhali District",
            state_code="51",
            latitude=22.2248632,
            longitude=90.4547503,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Paul",
            state_code="PA",
            latitude=37.0625,
            longitude=-95.677068,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Pavia",
            state_code="PV",
            latitude=45.3218166,
            longitude=8.8466236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Pāvilosta Municipality",
            state_code="071",
            latitude=56.8865424,
            longitude=21.1946849,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Pavlodar Region",
            state_code="PAV",
            latitude=52.2878444,
            longitude=76.9733453,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="Pays-de-la-Loire",
            state_code="PDL",
            latitude=47.7632836,
            longitude=-0.3299687,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Paysandú",
            state_code="PA",
            latitude=-32.0667366,
            longitude=-57.3364789,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Pazardzhik Province",
            state_code="13",
            latitude=42.1927567,
            longitude=24.3336226,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Pčinja District",
            state_code="24",
            latitude=42.5836362,
            longitude=22.1430215,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Peć District",
            state_code="XPE",
            latitude=42.6592155,
            longitude=20.2887624,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kosovo")][0]),
        ))
        list_of_states.append(State(
            name="Pécs",
            state_code="PS",
            latitude=46.0727345,
            longitude=18.232266,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Pedernales Province",
            state_code="16",
            latitude=17.8537626,
            longitude=-71.3303209,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Pehčevo Municipality",
            state_code="60",
            latitude=41.7737132,
            longitude=22.8820489,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Peleliu",
            state_code="350",
            latitude=7.0022906,
            longitude=134.2431628,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Pelhřimov",
            state_code="633",
            latitude=49.4306207,
            longitude=15.222983,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Pella Regional Unit",
            state_code="59",
            latitude=40.9148039,
            longitude=22.1430215,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Peloponnese Region",
            state_code="J",
            latitude=37.5079472,
            longitude=22.37349,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Pemagatshel District",
            state_code="43",
            latitude=27.002382,
            longitude=91.3469247,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Pemba North",
            state_code="06",
            latitude=-5.0319352,
            longitude=39.7755571,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Pemba South",
            state_code="10",
            latitude=-5.3146961,
            longitude=39.7549511,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Pembroke",
            state_code="PEM",
            latitude=32.3007672,
            longitude=-64.796263,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bermuda")][0]),
        ))
        list_of_states.append(State(
            name="Pembroke",
            state_code="40",
            latitude=34.6801626,
            longitude=-79.1950373,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Pembrokeshire",
            state_code="PEM",
            latitude=51.674078,
            longitude=-4.9088785,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Penal-Debe Regional Corporation",
            state_code="PED",
            latitude=10.1337402,
            longitude=-61.4435474,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Penama",
            state_code="PAM",
            latitude=-15.3795758,
            longitude=167.9053182,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vanuatu")][0]),
        ))
        list_of_states.append(State(
            name="Penang",
            state_code="07",
            latitude=5.4163935,
            longitude=100.3326786,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Penghu",
            state_code="PEN",
            latitude=23.5711899,
            longitude=119.5793157,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Pennsylvania",
            state_code="PA",
            latitude=41.2033216,
            longitude=-77.1945247,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Peñuelas",
            state_code="111",
            latitude=18.0633577,
            longitude=-66.7273896,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Penza Oblast",
            state_code="PNZ",
            latitude=53.1412105,
            longitude=44.0940048,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Peqin District",
            state_code="PQ",
            latitude=41.0470902,
            longitude=19.7502384,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Perak",
            state_code="08",
            latitude=4.5921126,
            longitude=101.090109,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Peravia Province",
            state_code="17",
            latitude=18.2786594,
            longitude=-70.3335887,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Perlis",
            state_code="09",
            latitude=29.9227094,
            longitude=-90.1228559,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Perm Krai",
            state_code="PER",
            latitude=58.8231929,
            longitude=56.5872481,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Përmet District",
            state_code="PR",
            latitude=40.2361837,
            longitude=20.3517334,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Pernambuco",
            state_code="PE",
            latitude=-8.8137173,
            longitude=-36.954107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Pernik Province",
            state_code="14",
            latitude=42.605199,
            longitude=23.0377916,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Perth and Kinross",
            state_code="PKN",
            latitude=56.3953817,
            longitude=-3.4283547,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Perugia",
            state_code="PG",
            latitude=42.938004,
            longitude=12.6216211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Pesaro and Urbino",
            state_code="PU",
            latitude=43.6130118,
            longitude=12.7135121,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Pescara",
            state_code="PE",
            latitude=42.3570655,
            longitude=13.9608091,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Pesnica Municipality",
            state_code="089",
            latitude=46.6088755,
            longitude=15.6757051,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Pest County",
            state_code="PE",
            latitude=47.4480001,
            longitude=19.4618128,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Petén Department",
            state_code="PE",
            latitude=16.912033,
            longitude=-90.2995785,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Petnjica Municipality",
            state_code="23",
            latitude=42.935348,
            longitude=20.0211449,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Petrovec Municipality",
            state_code="59",
            latitude=41.9029897,
            longitude=21.689921,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Phalombe District",
            state_code="PH",
            latitude=-15.7092038,
            longitude=35.6532848,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Phangnga",
            state_code="82",
            latitude=8.4501414,
            longitude=98.5255317,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Phatthalung",
            state_code="93",
            latitude=7.6166823,
            longitude=100.0740231,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Phayao",
            state_code="56",
            latitude=19.2154367,
            longitude=100.2023692,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Phetchabun",
            state_code="67",
            latitude=16.301669,
            longitude=101.1192804,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Phetchaburi",
            state_code="76",
            latitude=12.9649215,
            longitude=99.6425883,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Phichit",
            state_code="66",
            latitude=16.2740876,
            longitude=100.3346991,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Phitsanulok",
            state_code="65",
            latitude=16.8211238,
            longitude=100.2658516,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Phnom Penh",
            state_code="12",
            latitude=11.5563738,
            longitude=104.9282099,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Phoenix Islands",
            state_code="P",
            latitude=33.3284369,
            longitude=-111.9824774,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kiribati")][0]),
        ))
        list_of_states.append(State(
            name="Phongsaly Province",
            state_code="PH",
            latitude=21.5919377,
            longitude=102.2547919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Phra Nakhon Si Ayutthaya",
            state_code="14",
            latitude=14.3692325,
            longitude=100.5876634,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Phrae",
            state_code="54",
            latitude=18.1445774,
            longitude=100.1402831,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Phthiotis Prefecture",
            state_code="06",
            latitude=38.999785,
            longitude=22.3337769,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Phú Thọ",
            state_code="68",
            latitude=21.268443,
            longitude=105.2045573,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Phú Yên",
            state_code="32",
            latitude=13.0881861,
            longitude=109.0928764,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Phuket",
            state_code="83",
            latitude=7.8804479,
            longitude=98.3922504,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Piacenza",
            state_code="PC",
            latitude=44.8263112,
            longitude=9.5291447,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Piauí",
            state_code="PI",
            latitude=-7.7183401,
            longitude=-42.7289236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Pichincha",
            state_code="P",
            latitude=-0.1464847,
            longitude=-78.4751945,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Piedmont",
            state_code="21",
            latitude=45.0522366,
            longitude=7.5153885,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Pietà",
            state_code="41",
            latitude=42.21862,
            longitude=-83.734647,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Pinar del Río Province",
            state_code="01",
            latitude=22.4076256,
            longitude=-83.8473015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Pingtung",
            state_code="PIF",
            latitude=22.5519759,
            longitude=120.5487597,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Piran Municipality",
            state_code="090",
            latitude=45.5288856,
            longitude=13.5680735,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Pirkanmaa",
            state_code="11",
            latitude=61.6986918,
            longitude=23.7895598,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Pirojpur District",
            state_code="50",
            latitude=22.5790744,
            longitude=89.9759264,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Pirot District",
            state_code="22",
            latitude=43.0874036,
            longitude=22.5983044,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Pisa",
            state_code="PI",
            latitude=43.7228315,
            longitude=10.4017194,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Písek",
            state_code="314",
            latitude=49.3419938,
            longitude=14.246976,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Pistoia",
            state_code="PT",
            latitude=43.9543733,
            longitude=10.8903099,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Pita Prefecture",
            state_code="PI",
            latitude=10.8062086,
            longitude=-12.7135121,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Piura",
            state_code="PIU",
            latitude=-5.1782884,
            longitude=-80.6548882,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Pivka Municipality",
            state_code="091",
            latitude=45.6789296,
            longitude=14.2542689,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Plaines Wilhems",
            state_code="PW",
            latitude=-20.3054872,
            longitude=57.4853561,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Plaisance",
            state_code="19",
            latitude=45.607095,
            longitude=-75.1142745,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Planken",
            state_code="05",
            latitude=40.6650576,
            longitude=-73.504798,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Plasnica Municipality",
            state_code="61",
            latitude=41.4546349,
            longitude=21.1056539,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Plateau",
            state_code="PL",
            latitude=9.2182093,
            longitude=9.5179488,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Plateau Department",
            state_code="PL",
            latitude=7.3445141,
            longitude=2.539603,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Plateau-Central Region",
            state_code="11",
            latitude=12.2537648,
            longitude=-0.7532809,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Plateaux Department",
            state_code="14",
            latitude=-2.0680088,
            longitude=15.4068079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Plateaux Region",
            state_code="P",
            latitude=7.6101378,
            longitude=1.0586135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Togo")][0]),
        ))
        list_of_states.append(State(
            name="Plav Municipality",
            state_code="13",
            latitude=42.6001337,
            longitude=19.9407541,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Pļaviņas Municipality",
            state_code="072",
            latitude=56.6177313,
            longitude=25.7194043,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (14/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
