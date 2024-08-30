"""
States Seed #4

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
            name="Canóvanas",
            state_code="029",
            latitude=18.3748748,
            longitude=-65.8997533,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Cantabria",
            state_code="S",
            latitude=43.1828396,
            longitude=-3.9878427,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Cantal",
            state_code="15",
            latitude=45.0492177,
            longitude=2.1567272,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Cantemir District",
            state_code="CT",
            latitude=46.2771742,
            longitude=28.2009653,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Canterbury Region",
            state_code="CAN",
            latitude=-43.7542275,
            longitude=171.1637245,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Canton 10",
            state_code="10",
            latitude=43.9534155,
            longitude=16.9425187,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Capellen",
            state_code="CA",
            latitude=49.6403931,
            longitude=5.9553846,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Clervaux",
            state_code="CL",
            latitude=50.0546313,
            longitude=6.0285875,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Diekirch",
            state_code="DI",
            latitude=49.8671784,
            longitude=6.1595633,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Echternach",
            state_code="EC",
            latitude=49.8114133,
            longitude=6.4175635,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Esch-sur-Alzette",
            state_code="ES",
            latitude=49.5008805,
            longitude=5.9860925,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Grevenmacher",
            state_code="GR",
            latitude=49.680841,
            longitude=6.4407593,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Luxembourg",
            state_code="LU",
            latitude=49.6301025,
            longitude=6.1520185,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Mersch",
            state_code="ME",
            latitude=49.7542906,
            longitude=6.1292185,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Redange",
            state_code="RD",
            latitude=49.76455,
            longitude=5.88948,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Remich",
            state_code="RM",
            latitude=49.545017,
            longitude=6.3674222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Vianden",
            state_code="VD",
            latitude=49.9341924,
            longitude=6.2019917,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Canton of Wiltz",
            state_code="WI",
            latitude=49.96622,
            longitude=5.9324306,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Cao Bằng",
            state_code="04",
            latitude=22.635689,
            longitude=106.2522143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Capital",
            state_code="13",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bahrain")][0]),
        ))
        list_of_states.append(State(
            name="Capital",
            state_code="KU",
            latitude=26.2285161,
            longitude=50.5860497,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kuwait")][0]),
        ))
        list_of_states.append(State(
            name="Capital Region",
            state_code="1",
            latitude=38.5656957,
            longitude=-92.1816949,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iceland")][0]),
        ))
        list_of_states.append(State(
            name="Capital Region of Denmark",
            state_code="84",
            latitude=55.6751812,
            longitude=12.5493261,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Denmark")][0]),
        ))
        list_of_states.append(State(
            name="Capiz",
            state_code="CAP",
            latitude=11.5528816,
            longitude=122.740723,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Caquetá",
            state_code="CAQ",
            latitude=0.869892,
            longitude=-73.8419063,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Carabobo",
            state_code="G",
            latitude=10.1176433,
            longitude=-68.0477509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Caraga",
            state_code="13",
            latitude=8.8014562,
            longitude=125.7406882,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Caraș-Severin County",
            state_code="CS",
            latitude=45.1139646,
            longitude=22.0740993,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Carazo",
            state_code="CA",
            latitude=11.7274729,
            longitude=-86.2158497,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Carchi",
            state_code="C",
            latitude=0.5026912,
            longitude=-77.9042521,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Carinthia",
            state_code="2",
            latitude=46.722203,
            longitude=14.1805882,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Austria")][0]),
        ))
        list_of_states.append(State(
            name="Carlow",
            state_code="CW",
            latitude=52.7232217,
            longitude=-6.8108295,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Carmarthenshire",
            state_code="CMN",
            latitude=51.8572309,
            longitude=-4.3115959,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Carnikava Municipality",
            state_code="020",
            latitude=57.1024121,
            longitude=24.2108662,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Carolina",
            state_code="031",
            latitude=18.3680877,
            longitude=-66.0424734,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Carolina",
            state_code="CL",
            latitude=18.38888889,
            longitude=-65.96666667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Carriacou and Petite Martinique",
            state_code="10",
            latitude=12.4785888,
            longitude=-61.4493842,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Grenada")][0]),
        ))
        list_of_states.append(State(
            name="Carrickfergus Borough Council",
            state_code="CKF",
            latitude=54.7256843,
            longitude=-5.8093719,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Casablanca",
            state_code="CAS",
            latitude=33.5722678,
            longitude=-7.6570326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Casablanca-Settat",
            state_code="06",
            latitude=33.2160872,
            longitude=-7.4381355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Casanare",
            state_code="CAS",
            latitude=5.7589269,
            longitude=-71.5723953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Cascade",
            state_code="11",
            latitude=44.5162821,
            longitude=-116.0417983,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Cascades Region",
            state_code="02",
            latitude=10.4072992,
            longitude=-4.5624426,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Caserta",
            state_code="CE",
            latitude=41.2078354,
            longitude=14.1001326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Čaška Municipality",
            state_code="80",
            latitude=41.647438,
            longitude=21.6914115,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Castellón",
            state_code="CS",
            latitude=39.9811435,
            longitude=0.0088407,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Castelo Branco",
            state_code="05",
            latitude=39.8631323,
            longitude=-7.4814163,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Castlereagh",
            state_code="CSR",
            latitude=54.575679,
            longitude=-5.8884028,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Castries Quarter",
            state_code="02",
            latitude=14.0101094,
            longitude=-60.9874687,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Cat Island",
            state_code="CI",
            latitude=30.2280136,
            longitude=-89.1014933,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Catamarca",
            state_code="K",
            latitude=-28.4715877,
            longitude=-65.7877209,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Catanduanes",
            state_code="CAT",
            latitude=13.7088684,
            longitude=124.2421597,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Cataño",
            state_code="033",
            latitude=18.4465355,
            longitude=-66.1355775,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Catanzaro",
            state_code="CZ",
            latitude=38.8896348,
            longitude=16.4405872,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Cauca",
            state_code="CAU",
            latitude=2.7049813,
            longitude=-76.8259652,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Căușeni District",
            state_code="CS",
            latitude=46.6554715,
            longitude=29.4091222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Causeway Coast and Glens",
            state_code="CCG",
            latitude=55.043183,
            longitude=-6.6741288,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Cavan",
            state_code="CN",
            latitude=53.9765424,
            longitude=-7.2996623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Cavite",
            state_code="CAV",
            latitude=14.4791297,
            longitude=120.8969634,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Cayey",
            state_code="035",
            latitude=18.1119051,
            longitude=-66.166,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Cayo District",
            state_code="CY",
            latitude=17.0984445,
            longitude=-88.9413865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belize")][0]),
        ))
        list_of_states.append(State(
            name="Ceará",
            state_code="CE",
            latitude=-5.4983977,
            longitude=-39.3206241,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Cebu",
            state_code="CEB",
            latitude=10.3156992,
            longitude=123.8854366,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Ceiba",
            state_code="037",
            latitude=18.2475177,
            longitude=-65.9084953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Centar Municipality",
            state_code="77",
            latitude=41.9698934,
            longitude=21.4216267,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Centar Župa Municipality",
            state_code="78",
            latitude=41.4652259,
            longitude=20.5930548,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Central",
            state_code="16",
            latitude=26.1426093,
            longitude=50.5653294,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bahrain")][0]),
        ))
        list_of_states.append(State(
            name="Central",
            state_code="CP",
            latitude=5.5,
            longitude=-1,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ghana")][0]),
        ))
        list_of_states.append(State(
            name="Central Abaco",
            state_code="CO",
            latitude=26.3555029,
            longitude=-77.1485163,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Central and Western",
            state_code="HCW",
            latitude=22.28666,
            longitude=114.15497,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Central Andros",
            state_code="CS",
            latitude=24.4688482,
            longitude=-77.973865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Central Banat District",
            state_code="02",
            latitude=45.4788485,
            longitude=20.6082522,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Central Bedfordshire",
            state_code="CBF",
            latitude=52.0029744,
            longitude=-0.4651389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Central Bosnia Canton",
            state_code="06",
            latitude=44.1381856,
            longitude=17.6866714,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Central Darfur",
            state_code="DC",
            latitude=14.3782747,
            longitude=24.9042208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Central Denmark Region",
            state_code="82",
            latitude=56.302139,
            longitude=9.302777,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Denmark")][0]),
        ))
        list_of_states.append(State(
            name="Central Department",
            state_code="11",
            latitude=36.1559229,
            longitude=-95.9662075,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Central District",
            state_code="CE",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Botswana")][0]),
        ))
        list_of_states.append(State(
            name="Central District",
            state_code="M",
            latitude=47.6087583,
            longitude=-122.2964235,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Israel")][0]),
        ))
        list_of_states.append(State(
            name="Central Division",
            state_code="C",
            latitude=34.0440066,
            longitude=-118.2472738,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Central Eleuthera",
            state_code="CE",
            latitude=25.1362037,
            longitude=-76.1435915,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Central Equatoria",
            state_code="EC",
            latitude=4.6144063,
            longitude=31.2626366,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Central Finland",
            state_code="08",
            latitude=62.5666743,
            longitude=25.5549445,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Central Greece Region",
            state_code="H",
            latitude=38.6043984,
            longitude=22.7152131,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Central Luzon",
            state_code="03",
            latitude=15.4827722,
            longitude=120.7120023,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Central Macedonia",
            state_code="B",
            latitude=40.621173,
            longitude=23.1918021,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Central Ostrobothnia",
            state_code="07",
            latitude=63.5621735,
            longitude=24.0013631,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Finland")][0]),
        ))
        list_of_states.append(State(
            name="Central Province",
            state_code="CE",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Central Province",
            state_code="CPM",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Central Province",
            state_code="CE",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Solomon Islands")][0]),
        ))
        list_of_states.append(State(
            name="Central Province",
            state_code="2",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Central Province",
            state_code="02",
            latitude=7.2564996,
            longitude=80.7214417,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zambia")][0]),
        ))
        list_of_states.append(State(
            name="Central Region",
            state_code="C",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Central Region",
            state_code="1",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Central Region",
            state_code="C",
            latitude=44.296875,
            longitude=-94.7401733,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Central River Division",
            state_code="M",
            latitude=13.5994469,
            longitude=-14.8921668,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gambia The")][0]),
        ))
        list_of_states.append(State(
            name="Central Singapore",
            state_code="01",
            latitude=1.2884,
            longitude=103.8535,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Singapore")][0]),
        ))
        list_of_states.append(State(
            name="Central Visayas",
            state_code="07",
            latitude=9.816875,
            longitude=124.0641419,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Centrale Region",
            state_code="C",
            latitude=8.6586029,
            longitude=1.0586135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Togo")][0]),
        ))
        list_of_states.append(State(
            name="Centre",
            state_code="03",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Centre",
            state_code="CE",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cameroon")][0]),
        ))
        list_of_states.append(State(
            name="Centre",
            state_code="CE",
            latitude=32.8370251,
            longitude=-96.7773882,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Haiti")][0]),
        ))
        list_of_states.append(State(
            name="Centre-Est Region",
            state_code="04",
            latitude=11.5247674,
            longitude=-0.1494988,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Centre-Nord Region",
            state_code="05",
            latitude=13.1724464,
            longitude=-0.9056623,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Centre-Ouest Region",
            state_code="06",
            latitude=11.8798466,
            longitude=-2.302446,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Centre-Sud Region",
            state_code="07",
            latitude=11.5228911,
            longitude=-1.0586135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Centre-Val de Loire",
            state_code="CVL",
            latitude=47.7515686,
            longitude=1.6750631,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Centro Sur Province",
            state_code="CS",
            latitude=1.3436084,
            longitude=10.439656,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Equatorial Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Ceredigion",
            state_code="CGN",
            latitude=52.2191429,
            longitude=-3.9321256,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Cerklje na Gorenjskem Municipality",
            state_code="012",
            latitude=46.2517054,
            longitude=14.4857979,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Cerknica Municipality",
            state_code="013",
            latitude=45.7966255,
            longitude=14.392177,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Cerkno Municipality",
            state_code="014",
            latitude=46.1288414,
            longitude=13.9894027,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Cerkvenjak Municipality",
            state_code="153",
            latitude=46.5670711,
            longitude=15.9429753,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Cerro Largo",
            state_code="CL",
            latitude=-32.4411032,
            longitude=-54.3521753,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Cesar",
            state_code="CES",
            latitude=9.3372948,
            longitude=-73.6536209,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Češinovo-Obleševo Municipality",
            state_code="81",
            latitude=41.8639316,
            longitude=22.262246,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Cēsis Municipality",
            state_code="022",
            latitude=57.3102897,
            longitude=25.2676125,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Česká Lípa",
            state_code="511",
            latitude=50.6785201,
            longitude=14.5396991,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="České Budějovice",
            state_code="311",
            latitude=48.9775553,
            longitude=14.5150747,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Český Krumlov",
            state_code="312",
            latitude=48.8127354,
            longitude=14.3174657,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Cesvaine Municipality",
            state_code="021",
            latitude=56.9679264,
            longitude=26.3083172,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Ceuta",
            state_code="CE",
            latitude=35.889,
            longitude=-5.3187,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Chachoengsao",
            state_code="24",
            latitude=13.6904194,
            longitude=101.0779596,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Chaco",
            state_code="H",
            latitude=-27.4257175,
            longitude=-59.0243784,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Chagang Province",
            state_code="04",
            latitude=40.7202809,
            longitude=126.5621137,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="Chaguanas",
            state_code="CHA",
            latitude=10.5168387,
            longitude=-61.4114482,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Chaharmahal and Bakhtiari",
            state_code="14",
            latitude=31.9970419,
            longitude=50.6613849,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Chai Nat",
            state_code="18",
            latitude=15.1851971,
            longitude=100.125125,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Chaiyaphum",
            state_code="36",
            latitude=16.0074974,
            longitude=101.6129172,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Chalatenango Department",
            state_code="CH",
            latitude=14.1916648,
            longitude=-89.1705998,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="Champasak Province",
            state_code="CH",
            latitude=14.6578664,
            longitude=105.9699878,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Chandigarh",
            state_code="CH",
            latitude=30.7333148,
            longitude=76.7794179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Chandpur District",
            state_code="09",
            latitude=23.2513148,
            longitude=90.8517846,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Changhua",
            state_code="CHA",
            latitude=24.0517963,
            longitude=120.5161352,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Chania Regional Unit",
            state_code="94",
            latitude=35.5138298,
            longitude=24.0180367,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Greece")][0]),
        ))
        list_of_states.append(State(
            name="Chanthaburi",
            state_code="22",
            latitude=12.6112485,
            longitude=102.1037806,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Chapai Nawabganj District",
            state_code="45",
            latitude=24.7413111,
            longitude=88.2912069,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Charente",
            state_code="16",
            latitude=45.6658479,
            longitude=-0.3184577,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Charente-Maritime",
            state_code="17",
            latitude=45.7296828,
            longitude=-1.3388116,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Chari-Baguirmi",
            state_code="CB",
            latitude=11.4618626,
            longitude=15.2446394,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Charlotte Parish",
            state_code="01",
            latitude=13.2175451,
            longitude=-61.1636244,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Vincent and the Grenadines")][0]),
        ))
        list_of_states.append(State(
            name="Chatham Islands",
            state_code="CIT",
            latitude=-44.0057523,
            longitude=-176.5400674,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Cheb",
            state_code="411",
            latitude=50.0795334,
            longitude=12.3698636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Chechen Republic",
            state_code="CE",
            latitude=43.4023301,
            longitude=45.7187468,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Chefchaouen",
            state_code="CHE",
            latitude=35.018172,
            longitude=-5.1432068,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Chelyabinsk Oblast",
            state_code="CHE",
            latitude=54.4319422,
            longitude=60.8788963,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Cher",
            state_code="18",
            latitude=47.0243628,
            longitude=1.8662732,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Cherkaska oblast",
            state_code="71",
            latitude=49.444433,
            longitude=32.059767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Chernihivska oblast",
            state_code="74",
            latitude=51.4982,
            longitude=31.2893499,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Chernivetska oblast",
            state_code="77",
            latitude=48.291683,
            longitude=25.935217,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Cheshire East",
            state_code="CHE",
            latitude=53.1610446,
            longitude=-2.2185932,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Cheshire West and Chester",
            state_code="CHW",
            latitude=53.2302974,
            longitude=-2.7151117,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Chhattisgarh",
            state_code="CT",
            latitude=21.2786567,
            longitude=81.8661442,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Chiang Mai",
            state_code="50",
            latitude=18.7883439,
            longitude=98.9853008,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Chiang Rai",
            state_code="57",
            latitude=19.9104798,
            longitude=99.840576,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Chiapas",
            state_code="CHP",
            latitude=16.7569318,
            longitude=-93.1292353,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Chiayi",
            state_code="CYI",
            latitude=23.4518428,
            longitude=120.2554615,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Chiayi",
            state_code="CYQ",
            latitude=23.4800751,
            longitude=120.4491113,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Chiba Prefecture",
            state_code="12",
            latitude=35.3354155,
            longitude=140.1832516,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Chichaoua",
            state_code="CHI",
            latitude=31.5383581,
            longitude=-8.7646388,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Chiesanuova",
            state_code="02",
            latitude=45.4226172,
            longitude=7.6503854,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "San Marino")][0]),
        ))
        list_of_states.append(State(
            name="Chieti",
            state_code="CH",
            latitude=42.0334428,
            longitude=14.3791912,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Chihuahua",
            state_code="CHH",
            latitude=28.6329957,
            longitude=-106.0691004,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Chikwawa District",
            state_code="CK",
            latitude=-16.1958446,
            longitude=34.7740793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Chimaltenango Department",
            state_code="CM",
            latitude=14.5634787,
            longitude=-90.9820668,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Chimborazo",
            state_code="H",
            latitude=-1.6647995,
            longitude=-78.6543255,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Chimbu Province",
            state_code="CPK",
            latitude=-6.3087682,
            longitude=144.8731219,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Chin State",
            state_code="14",
            latitude=22.0086978,
            longitude=93.5812692,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Chinandega",
            state_code="CI",
            latitude=12.8820062,
            longitude=-87.1422895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Chiquimula Department",
            state_code="CQ",
            latitude=14.7514999,
            longitude=-89.4742177,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Chiradzulu District",
            state_code="CR",
            latitude=-15.7423151,
            longitude=35.2587964,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Chiriquí Province",
            state_code="4",
            latitude=8.584898,
            longitude=-82.3885783,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Chișinău Municipality",
            state_code="CU",
            latitude=47.0104529,
            longitude=28.8638102,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Chitipa district",
            state_code="CT",
            latitude=-9.7037655,
            longitude=33.2700253,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Chittagong District",
            state_code="10",
            latitude=22.5150105,
            longitude=91.7538817,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Chittagong Division",
            state_code="B",
            latitude=23.1793157,
            longitude=91.9881527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Chlef",
            state_code="02",
            latitude=36.1693515,
            longitude=1.2891036,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Chocó",
            state_code="CHO",
            latitude=5.2528033,
            longitude=-76.8259652,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Choiseul Province",
            state_code="CH",
            latitude=-7.0501494,
            longitude=156.9511459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Solomon Islands")][0]),
        ))
        list_of_states.append(State(
            name="Choiseul Quarter",
            state_code="03",
            latitude=13.7750154,
            longitude=-61.048591,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Choluteca Department",
            state_code="CH",
            latitude=13.2504325,
            longitude=-87.1422895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Chomutov",
            state_code="422",
            latitude=50.4583872,
            longitude=13.301791,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Chon Buri",
            state_code="20",
            latitude=13.3611431,
            longitude=100.9846717,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Chongqing",
            state_code="CQ",
            latitude=29.4315861,
            longitude=106.912251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Chontales",
            state_code="CO",
            latitude=11.9394717,
            longitude=-85.1894045,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Christ Church",
            state_code="01",
            latitude=36.0060407,
            longitude=-95.921121,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Christ Church Nichola Town Parish",
            state_code="01",
            latitude=17.3604812,
            longitude=-62.7617837,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Chrudim",
            state_code="531",
            latitude=49.8830216,
            longitude=15.8290866,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Chtouka-Ait Baha",
            state_code="CHT",
            latitude=30.1072422,
            longitude=-9.2785583,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Chuadanga District",
            state_code="12",
            latitude=23.6160512,
            longitude=88.8263006,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Chubut",
            state_code="U",
            latitude=-43.2934246,
            longitude=-65.1114818,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Chukha District",
            state_code="12",
            latitude=27.0784304,
            longitude=89.4742177,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Chukotka Autonomous Okrug",
            state_code="CHU",
            latitude=65.6298355,
            longitude=171.6952159,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Chumphon",
            state_code="86",
            latitude=10.4930496,
            longitude=99.1800199,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Chuquisaca Department",
            state_code="H",
            latitude=-20.0249144,
            longitude=-64.1478236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bolivia")][0]),
        ))
        list_of_states.append(State(
            name="Chuuk State",
            state_code="TRK",
            latitude=7.1386759,
            longitude=151.5593065,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Micronesia")][0]),
        ))
        list_of_states.append(State(
            name="Chuvash Republic",
            state_code="CU",
            latitude=55.5595992,
            longitude=46.9283535,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Chuy Region",
            state_code="C",
            latitude=42.5655,
            longitude=74.4056612,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kyrgyzstan")][0]),
        ))
        list_of_states.append(State(
            name="Ciales",
            state_code="039",
            latitude=18.3360622,
            longitude=-66.4687823,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Cibitoke Province",
            state_code="CI",
            latitude=-2.8102897,
            longitude=29.1855785,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Cibla Municipality",
            state_code="023",
            latitude=56.6102344,
            longitude=27.8696598,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Cidra",
            state_code="041",
            latitude=18.1757914,
            longitude=-66.1612779,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Ciego de Ávila Province",
            state_code="08",
            latitude=21.9329515,
            longitude=-78.5660852,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Cienfuegos Province",
            state_code="06",
            latitude=22.2379783,
            longitude=-80.365865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Cimișlia District",
            state_code="CM",
            latitude=46.5250851,
            longitude=28.7721835,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="City and County of Cardiff",
            state_code="CRF",
            latitude=51.481581,
            longitude=-3.17909,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City and County of Swansea",
            state_code="SWA",
            latitude=51.62144,
            longitude=-3.943646,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City Municipality of Celje",
            state_code="011",
            latitude=46.2397495,
            longitude=15.2677063,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="City Municipality of Novo Mesto",
            state_code="085",
            latitude=45.8010824,
            longitude=15.1710089,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="City of Bristol",
            state_code="BST",
            latitude=41.673522,
            longitude=-72.9465375,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Derby",
            state_code="DER",
            latitude=37.5483755,
            longitude=-97.2485191,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Kingston upon Hull",
            state_code="KHL",
            latitude=53.7676236,
            longitude=-0.3274198,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Leicester",
            state_code="LCE",
            latitude=52.6368778,
            longitude=-1.1397592,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of London",
            state_code="LND",
            latitude=51.5123443,
            longitude=-0.0909852,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Nottingham",
            state_code="NGM",
            latitude=52.9547832,
            longitude=-1.1581086,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Peterborough",
            state_code="PTE",
            latitude=44.3093636,
            longitude=-78.320153,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Plymouth",
            state_code="PLY",
            latitude=42.3708941,
            longitude=-83.4697141,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Portsmouth",
            state_code="POR",
            latitude=36.832915,
            longitude=-76.2975549,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Southampton",
            state_code="STH",
            latitude=50.9097004,
            longitude=-1.4043509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Stoke-on-Trent",
            state_code="STE",
            latitude=53.002668,
            longitude=-2.179404,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Sunderland",
            state_code="SND",
            latitude=54.8861489,
            longitude=-1.4785797,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Westminster",
            state_code="WSM",
            latitude=39.5765977,
            longitude=-76.9972126,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of Wolverhampton",
            state_code="WLV",
            latitude=52.588912,
            longitude=-2.156463,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="City of York",
            state_code="YOR",
            latitude=53.9599651,
            longitude=-1.0872979,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ciudad Autónoma de Buenos Aires",
            state_code="C",
            latitude=-34.6036844,
            longitude=-58.3815591,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Ciudad de México",
            state_code="CMX",
            latitude=19.4326077,
            longitude=-99.133208,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Ciudad Real",
            state_code="CR",
            latitude=38.9860758,
            longitude=-3.9444975,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Clackmannanshire",
            state_code="CLK",
            latitude=56.1075351,
            longitude=-3.7529409,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Clare",
            state_code="CE",
            latitude=43.04664,
            longitude=-87.899581,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Clarendon Parish",
            state_code="13",
            latitude=17.9557183,
            longitude=-77.2405153,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Clipperton",
            state_code="CP",
            latitude=10.2833541,
            longitude=-109.2254215,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Cluj County",
            state_code="CJ",
            latitude=46.7941797,
            longitude=23.6121492,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Coahuila de Zaragoza",
            state_code="COA",
            latitude=27.058676,
            longitude=-101.7068294,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Coamo",
            state_code="043",
            latitude=18.0799616,
            longitude=-66.3579473,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Cochabamba Department",
            state_code="C",
            latitude=-17.5681675,
            longitude=-65.475736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bolivia")][0]),
        ))
        list_of_states.append(State(
            name="Coclé Province",
            state_code="2",
            latitude=8.6266068,
            longitude=-80.365865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Coimbra",
            state_code="06",
            latitude=40.2057994,
            longitude=-8.41369,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Cojedes",
            state_code="H",
            latitude=9.3816682,
            longitude=-68.3339275,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Coleraine Borough Council",
            state_code="CLR",
            latitude=55.145157,
            longitude=-6.6759814,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Colima",
            state_code="COL",
            latitude=19.2452342,
            longitude=-103.7240868,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Collines Department",
            state_code="CO",
            latitude=8.3022297,
            longitude=2.302446,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Colombo District",
            state_code="11",
            latitude=6.9269557,
            longitude=79.8617306,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Colón Department",
            state_code="CL",
            latitude=15.6425965,
            longitude=-85.520024,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Colón Province",
            state_code="3",
            latitude=9.1851989,
            longitude=-80.0534923,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Colonia",
            state_code="CO",
            latitude=-34.1294678,
            longitude=-57.6605184,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Colorado",
            state_code="CO",
            latitude=39.5500507,
            longitude=-105.7820674,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Comayagua Department",
            state_code="CM",
            latitude=14.5534828,
            longitude=-87.6186379,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Comerío",
            state_code="045",
            latitude=18.2192001,
            longitude=-66.2256022,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Comilla District",
            state_code="08",
            latitude=23.4575667,
            longitude=91.1808996,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Commewijne District",
            state_code="CM",
            latitude=5.740211,
            longitude=-54.8731219,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Suriname")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (4/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
