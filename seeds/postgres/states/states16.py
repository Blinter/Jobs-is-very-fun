"""
States Seed #16

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
            name="Río Muni",
            state_code="C",
            latitude=1.4610606,
            longitude=9.6786894,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Equatorial Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Río Negro",
            state_code="R",
            latitude=-40.8261434,
            longitude=-63.0266339,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Río Negro",
            state_code="RN",
            latitude=-32.7676356,
            longitude=-57.4295207,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Río San Juan",
            state_code="SJ",
            latitude=11.478161,
            longitude=-84.7733325,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Risaralda",
            state_code="RIS",
            latitude=5.3158475,
            longitude=-75.9927652,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Rîșcani District",
            state_code="RI",
            latitude=47.9070153,
            longitude=27.5374996,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Moldova")][0]),
        ))
        list_of_states.append(State(
            name="Rivas",
            state_code="RI",
            latitude=11.402349,
            longitude=-85.684578,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="River Cess County",
            state_code="RI",
            latitude=5.9025328,
            longitude=-9.456155,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="River Gee County",
            state_code="RG",
            latitude=5.2604894,
            longitude=-7.87216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="River Nile",
            state_code="NR",
            latitude=23.9727595,
            longitude=32.8749206,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sudan")][0]),
        ))
        list_of_states.append(State(
            name="Rivera",
            state_code="RV",
            latitude=-31.4817421,
            longitude=-55.2435759,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Rivers",
            state_code="RI",
            latitude=5.021342,
            longitude=6.4376022,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Rivière du Rempart",
            state_code="RR",
            latitude=-20.0560983,
            longitude=57.6552389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Rivnenska oblast",
            state_code="56",
            latitude=50.6199,
            longitude=26.251617,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Riyadh",
            state_code="01",
            latitude=22.7554385,
            longitude=46.2091547,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Rizal",
            state_code="RIZ",
            latitude=14.6037446,
            longitude=121.3084088,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Rize",
            state_code="53",
            latitude=40.9581497,
            longitude=40.9226985,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Rocha",
            state_code="RO",
            latitude=-33.9690081,
            longitude=-54.021485,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Rochdale",
            state_code="RCH",
            latitude=53.6097136,
            longitude=-2.1561,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Roche Caiman",
            state_code="25",
            latitude=-4.6396028,
            longitude=55.4679315,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Rock Sound",
            state_code="RS",
            latitude=39.0142443,
            longitude=-95.6708989,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Rodrigues Island",
            state_code="RO",
            latitude=-19.7245385,
            longitude=63.4272185,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Rogaland",
            state_code="11",
            latitude=59.1489544,
            longitude=6.0143432,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="Rogaška Slatina Municipality",
            state_code="106",
            latitude=46.2453973,
            longitude=15.6265014,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Rogašovci Municipality",
            state_code="105",
            latitude=46.8055785,
            longitude=16.0345237,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Rogatec Municipality",
            state_code="107",
            latitude=46.2286626,
            longitude=15.6991338,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Roi Et",
            state_code="45",
            latitude=16.0538196,
            longitude=103.6520036,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Roja Municipality",
            state_code="079",
            latitude=57.5046713,
            longitude=22.8012164,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Rokiškis District Municipality",
            state_code="40",
            latitude=55.9555039,
            longitude=25.5859249,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Rokycany",
            state_code="326",
            latitude=49.8262827,
            longitude=13.6874943,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Romblon",
            state_code="ROM",
            latitude=12.5778016,
            longitude=122.269146,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Rondônia",
            state_code="RO",
            latitude=-11.5057341,
            longitude=-63.580611,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Ropaži Municipality",
            state_code="080",
            latitude=56.9615786,
            longitude=24.6010476,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Roraima",
            state_code="RR",
            latitude=2.7375971,
            longitude=-62.0750998,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Roscommon",
            state_code="RN",
            latitude=53.7592604,
            longitude=-8.2681621,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Rosoman Municipality",
            state_code="67",
            latitude=41.4848006,
            longitude=21.8807064,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Rostov Oblast",
            state_code="ROS",
            latitude=47.6853247,
            longitude=41.8258952,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Rotherham",
            state_code="ROT",
            latitude=53.4326035,
            longitude=-1.3635009,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Rotuma",
            state_code="R",
            latitude=-12.5025069,
            longitude=177.0724164,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Rovigo",
            state_code="RO",
            latitude=45.0241818,
            longitude=11.8238162,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Royal Borough of Greenwich",
            state_code="GRE",
            latitude=51.4834627,
            longitude=0.0586202,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Royal Borough of Kensington and Chelsea",
            state_code="KEC",
            latitude=51.4990805,
            longitude=-0.1938253,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Royal Borough of Kingston upon Thames",
            state_code="KTT",
            latitude=51.378117,
            longitude=-0.292709,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Rožaje Municipality",
            state_code="17",
            latitude=42.8408389,
            longitude=20.1670628,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Rubanda District",
            state_code="429",
            latitude=-1.186119,
            longitude=29.8453576,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Rubirizi District",
            state_code="425",
            latitude=-0.264241,
            longitude=30.1084033,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Rucava Municipality",
            state_code="081",
            latitude=56.1593124,
            longitude=21.1618121,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Rugāji Municipality",
            state_code="082",
            latitude=57.0056023,
            longitude=27.1317203,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Ruggell",
            state_code="06",
            latitude=47.2529222,
            longitude=9.5402127,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Rūjiena Municipality",
            state_code="084",
            latitude=57.8937291,
            longitude=25.3391008,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Rukiga District",
            state_code="431",
            latitude=-1.1326337,
            longitude=30.043412,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Rukungiri District",
            state_code="412",
            latitude=-0.751849,
            longitude=29.9277947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Rukwa",
            state_code="20",
            latitude=-8.0109444,
            longitude=31.4456179,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Rum Cay District",
            state_code="RC",
            latitude=23.6854676,
            longitude=-74.8390162,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Rumonge Province",
            state_code="RM",
            latitude=-3.9754049,
            longitude=29.4388014,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Rumphi District",
            state_code="RU",
            latitude=-10.7851537,
            longitude=34.3310364,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Rundāle Municipality",
            state_code="083",
            latitude=56.409721,
            longitude=24.0124139,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Ruše Municipality",
            state_code="108",
            latitude=46.5206265,
            longitude=15.4817869,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Ruse Province",
            state_code="18",
            latitude=43.8355964,
            longitude=25.9656144,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Rutana Province",
            state_code="RT",
            latitude=-3.8791523,
            longitude=30.0665236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Rutland",
            state_code="RUT",
            latitude=43.6106237,
            longitude=-72.9726065,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Ruvuma",
            state_code="21",
            latitude=-10.6878717,
            longitude=36.2630846,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Ruyigi Province",
            state_code="RY",
            latitude=-3.446207,
            longitude=30.2512728,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Ryanggang Province",
            state_code="10",
            latitude=41.2318921,
            longitude=128.5076359,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Korea")][0]),
        ))
        list_of_states.append(State(
            name="Ryazan Oblast",
            state_code="RYA",
            latitude=54.3875964,
            longitude=41.2595661,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Rychnov nad Kněžnou",
            state_code="524",
            latitude=50.1659651,
            longitude=16.2776842,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Sa Kaeo",
            state_code="27",
            latitude=13.824038,
            longitude=102.0645839,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Saada",
            state_code="SD",
            latitude=16.8476528,
            longitude=43.9436788,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Saare County",
            state_code="74",
            latitude=58.4849721,
            longitude=22.6136408,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Estonia")][0]),
        ))
        list_of_states.append(State(
            name="Saarland",
            state_code="SL",
            latitude=49.3964234,
            longitude=7.0229607,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Saatly District",
            state_code="SAT",
            latitude=39.9095503,
            longitude=48.3595122,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Saba",
            state_code="BQ2",
            latitude=17.6354642,
            longitude=-63.2326763,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bonaire, Sint Eustatius and Saba")][0]),
        ))
        list_of_states.append(State(
            name="Saba",
            state_code="BQ2",
            latitude=17.6354642,
            longitude=-63.2326763,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Sabah",
            state_code="12",
            latitude=5.9788398,
            longitude=116.0753199,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Sabana Grande",
            state_code="121",
            latitude=18.0777392,
            longitude=-66.9604549,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Sabaragamuwa Province",
            state_code="9",
            latitude=6.7395941,
            longitude=80.365865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Sabha District",
            state_code="SB",
            latitude=27.0365406,
            longitude=14.4290236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Sabirabad District",
            state_code="SAB",
            latitude=39.9870663,
            longitude=48.4692545,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Sacatepéquez Department",
            state_code="SA",
            latitude=14.5178379,
            longitude=-90.7152749,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="Sadarak District",
            state_code="SAD",
            latitude=39.7105114,
            longitude=44.8864277,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Safi",
            state_code="SAF",
            latitude=32.2989872,
            longitude=-9.1013498,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Saga Prefecture",
            state_code="41",
            latitude=33.3078371,
            longitude=130.2271243,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Sagaing Region",
            state_code="01",
            latitude=24.428381,
            longitude=95.3939551,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Sagarmatha Zone",
            state_code="SA",
            latitude=27.3238263,
            longitude=86.7416374,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Sahel Region",
            state_code="12",
            latitude=14.1000865,
            longitude=-0.1494988,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Sai Kung",
            state_code="NSK",
            latitude=22.38143,
            longitude=114.27052,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hong Kong S.A.R.")][0]),
        ))
        list_of_states.append(State(
            name="Saïda",
            state_code="20",
            latitude=34.8415207,
            longitude=0.1456055,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Saint Andrew",
            state_code="02",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Saint Andrew",
            state_code="02",
            latitude=37.2245103,
            longitude=-95.7021189,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Andrew Parish",
            state_code="02",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Andrew Parish",
            state_code="01",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Grenada")][0]),
        ))
        list_of_states.append(State(
            name="Saint Andrew Parish",
            state_code="02",
            latitude=43.0242999,
            longitude=-81.2025,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Vincent and the Grenadines")][0]),
        ))
        list_of_states.append(State(
            name="Saint Ann Parish",
            state_code="06",
            latitude=37.2871452,
            longitude=-77.4103533,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Anne Sandy Point Parish",
            state_code="02",
            latitude=17.3725333,
            longitude=-62.8441133,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint Brandon Islands",
            state_code="CC",
            latitude=-16.583333,
            longitude=59.616667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Saint Catherine Parish",
            state_code="14",
            latitude=18.0364134,
            longitude=-77.0564464,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Croix",
            state_code="SC",
            latitude=17.729352,
            longitude=-64.7343705,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Virgin Islands (US)")][0]),
        ))
        list_of_states.append(State(
            name="Saint David Parish",
            state_code="03",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominica")][0]),
        ))
        list_of_states.append(State(
            name="Saint David Parish",
            state_code="02",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Grenada")][0]),
        ))
        list_of_states.append(State(
            name="Saint David Parish",
            state_code="03",
            latitude=43.8523095,
            longitude=-79.5236654,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Vincent and the Grenadines")][0]),
        ))
        list_of_states.append(State(
            name="Saint Elizabeth Parish",
            state_code="11",
            latitude=38.9925308,
            longitude=-94.58992,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Saint George",
            state_code="03",
            latitude=37.0965278,
            longitude=-113.5684164,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Saint George Gingerland Parish",
            state_code="04",
            latitude=17.1257759,
            longitude=-62.5619811,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint George Parish",
            state_code="03",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Antigua and Barbuda")][0]),
        ))
        list_of_states.append(State(
            name="Saint George Parish",
            state_code="04",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominica")][0]),
        ))
        list_of_states.append(State(
            name="Saint George Parish",
            state_code="03",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Grenada")][0]),
        ))
        list_of_states.append(State(
            name="Saint George Parish",
            state_code="04",
            latitude=42.957609,
            longitude=-81.326705,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Vincent and the Grenadines")][0]),
        ))
        list_of_states.append(State(
            name="Saint George's",
            state_code="SGE",
            latitude=17.1257759,
            longitude=-62.5619811,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bermuda")][0]),
        ))
        list_of_states.append(State(
            name="Saint Helena",
            state_code="SH-HL",
            latitude=-15.9650104,
            longitude=-5.7089241,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Saint James",
            state_code="04",
            latitude=48.523566,
            longitude=-1.3237885,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Saint James Parish",
            state_code="08",
            latitude=30.0179292,
            longitude=-90.7913227,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Saint James Windward Parish",
            state_code="05",
            latitude=17.1769633,
            longitude=-62.5796026,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint John",
            state_code="05",
            latitude=45.2733153,
            longitude=-66.063308,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Saint John",
            state_code="SJ",
            latitude=18.3356169,
            longitude=-64.80028,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Virgin Islands (US)")][0]),
        ))
        list_of_states.append(State(
            name="Saint John Capisterre Parish",
            state_code="06",
            latitude=17.3810341,
            longitude=-62.7911833,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint John Figtree Parish",
            state_code="07",
            latitude=17.1155748,
            longitude=-62.6031004,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint John Parish",
            state_code="04",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Antigua and Barbuda")][0]),
        ))
        list_of_states.append(State(
            name="Saint John Parish",
            state_code="05",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominica")][0]),
        ))
        list_of_states.append(State(
            name="Saint John Parish",
            state_code="04",
            latitude=30.1118331,
            longitude=-90.4879916,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Grenada")][0]),
        ))
        list_of_states.append(State(
            name="Saint Joseph",
            state_code="06",
            latitude=39.7674578,
            longitude=-94.846681,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Saint Joseph Parish",
            state_code="06",
            latitude=39.0222712,
            longitude=-94.7176504,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Kitts",
            state_code="K",
            latitude=17.3433796,
            longitude=-62.7559043,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint Lawrence",
            state_code="50",
            latitude=38.9578056,
            longitude=-95.2565689,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Saint Louis",
            state_code="22",
            latitude=38.6270025,
            longitude=-90.1994042,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Saint Lucy",
            state_code="07",
            latitude=38.7614625,
            longitude=-77.4491439,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Saint Luke Parish",
            state_code="07",
            latitude=42.1051363,
            longitude=-80.0570722,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Mark Parish",
            state_code="08",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Mark Parish",
            state_code="05",
            latitude=40.5881863,
            longitude=-73.9495701,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Grenada")][0]),
        ))
        list_of_states.append(State(
            name="Saint Mary Cayon Parish",
            state_code="08",
            latitude=17.3462071,
            longitude=-62.7382671,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint Mary Parish",
            state_code="05",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Antigua and Barbuda")][0]),
        ))
        list_of_states.append(State(
            name="Saint Mary Parish",
            state_code="05",
            latitude=36.092522,
            longitude=-95.973844,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Michael",
            state_code="08",
            latitude=36.035977,
            longitude=-95.849052,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Saint Patrick Parish",
            state_code="09",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Patrick Parish",
            state_code="06",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Grenada")][0]),
        ))
        list_of_states.append(State(
            name="Saint Patrick Parish",
            state_code="05",
            latitude=39.7509186,
            longitude=-94.8450556,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Vincent and the Grenadines")][0]),
        ))
        list_of_states.append(State(
            name="Saint Paul Capisterre Parish",
            state_code="09",
            latitude=17.4016683,
            longitude=-62.8257332,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint Paul Charlestown Parish",
            state_code="10",
            latitude=17.1346297,
            longitude=-62.6133816,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint Paul Parish",
            state_code="06",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Antigua and Barbuda")][0]),
        ))
        list_of_states.append(State(
            name="Saint Paul Parish",
            state_code="10",
            latitude=38.86146,
            longitude=-90.7435619,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Peter",
            state_code="09",
            latitude=37.0827119,
            longitude=-94.517125,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Saint Peter Basseterre Parish",
            state_code="11",
            latitude=17.3102911,
            longitude=-62.7147533,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint Peter Parish",
            state_code="07",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Antigua and Barbuda")][0]),
        ))
        list_of_states.append(State(
            name="Saint Peter Parish",
            state_code="11",
            latitude=40.4524194,
            longitude=-80.0085056,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominica")][0]),
        ))
        list_of_states.append(State(
            name="Saint Petersburg",
            state_code="SPE",
            latitude=59.9310584,
            longitude=30.3609096,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Saint Philip",
            state_code="10",
            latitude=35.233114,
            longitude=-89.4364042,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Saint Philip Parish",
            state_code="08",
            latitude=40.4368258,
            longitude=-80.0685532,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Antigua and Barbuda")][0]),
        ))
        list_of_states.append(State(
            name="Saint Pierre and Miquelon",
            state_code="PM",
            latitude=46.8852,
            longitude=-56.3159,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Saint Thomas",
            state_code="11",
            latitude=18.3380965,
            longitude=-64.8940946,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Barbados")][0]),
        ))
        list_of_states.append(State(
            name="Saint Thomas",
            state_code="ST",
            latitude=18.3428459,
            longitude=-65.077018,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Virgin Islands (US)")][0]),
        ))
        list_of_states.append(State(
            name="Saint Thomas Lowland Parish",
            state_code="12",
            latitude=17.1650513,
            longitude=-62.6089753,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint Thomas Middle Island Parish",
            state_code="13",
            latitude=17.3348813,
            longitude=-62.8088251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Kitts and Nevis")][0]),
        ))
        list_of_states.append(State(
            name="Saint Thomas Parish",
            state_code="03",
            latitude=41.4425389,
            longitude=-81.7402218,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Saint-Barthélemy",
            state_code="BL",
            latitude=17.9005134,
            longitude=-62.8205871,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Saint-Louis",
            state_code="SL",
            latitude=38.6270025,
            longitude=-90.1994042,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Saint-Martin",
            state_code="MF",
            latitude=18.0708298,
            longitude=-63.0500809,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Sainyabuli Province",
            state_code="XA",
            latitude=19.3907886,
            longitude=101.5248055,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Saitama Prefecture",
            state_code="11",
            latitude=35.9962513,
            longitude=139.4466005,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Sakarya",
            state_code="54",
            latitude=40.788855,
            longitude=30.405954,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Sakha Republic",
            state_code="SA",
            latitude=66.7613451,
            longitude=124.123753,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Sakhalin",
            state_code="SAK",
            latitude=50.6909848,
            longitude=142.9505689,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Šakiai District Municipality",
            state_code="41",
            latitude=54.952671,
            longitude=23.0480199,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Sakon Nakhon",
            state_code="47",
            latitude=17.1664211,
            longitude=104.1486055,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Sal",
            state_code="SL",
            latitude=26.5958122,
            longitude=-80.2045083,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Sala Municipality",
            state_code="085",
            latitude=59.9679613,
            longitude=16.4978217,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Salacgrīva Municipality",
            state_code="086",
            latitude=57.7580883,
            longitude=24.3543181,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Saladin",
            state_code="SD",
            latitude=34.5337527,
            longitude=43.483738,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Sălaj County",
            state_code="SJ",
            latitude=47.2090813,
            longitude=23.2121901,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Salamanca",
            state_code="SA",
            latitude=40.9515263,
            longitude=-6.2375947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Salamat",
            state_code="SA",
            latitude=10.9691601,
            longitude=20.7122465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Salaspils Municipality",
            state_code="087",
            latitude=56.8608152,
            longitude=24.3497881,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Salavan Province",
            state_code="SL",
            latitude=15.8171073,
            longitude=106.2522143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Šalčininkai District Municipality",
            state_code="42",
            latitude=54.309767,
            longitude=25.387564,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Saldus Municipality",
            state_code="088",
            latitude=56.6665088,
            longitude=22.4935493,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Salé",
            state_code="SAL",
            latitude=34.037757,
            longitude=-6.8427073,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Salerno",
            state_code="SA",
            latitude=40.4287832,
            longitude=15.2194808,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Salfit",
            state_code="SLT",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Salford",
            state_code="SLF",
            latitude=53.4875235,
            longitude=-2.2901264,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Salgótarján",
            state_code="ST",
            latitude=48.0935237,
            longitude=19.7999813,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Salima District",
            state_code="SA",
            latitude=-13.6809586,
            longitude=34.4198243,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Salinas",
            state_code="123",
            latitude=36.6777372,
            longitude=-121.6555013,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Šalovci Municipality",
            state_code="033",
            latitude=46.8533568,
            longitude=16.2591791,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Salta",
            state_code="A",
            latitude=-24.7997688,
            longitude=-65.4150367,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Salto",
            state_code="SA",
            latitude=-31.388028,
            longitude=-57.9612455,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Salyan District",
            state_code="SAL",
            latitude=28.3524811,
            longitude=82.12784,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Salzburg",
            state_code="5",
            latitude=47.80949,
            longitude=13.05501,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Austria")][0]),
        ))
        list_of_states.append(State(
            name="Samaná Province",
            state_code="20",
            latitude=19.2058371,
            longitude=-69.3362949,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Samangan",
            state_code="SAM",
            latitude=36.3155506,
            longitude=67.9642863,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Samara Oblast",
            state_code="SAM",
            latitude=53.4183839,
            longitude=50.4725528,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Samarqand Region",
            state_code="SA",
            latitude=39.627012,
            longitude=66.9749731,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Samburu",
            state_code="37",
            latitude=1.2154506,
            longitude=36.954107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Samdrup Jongkhar District",
            state_code="45",
            latitude=26.8035682,
            longitude=91.5039207,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Samegrelo-Zemo Svaneti",
            state_code="SZ",
            latitude=42.7352247,
            longitude=42.1689362,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Samsun",
            state_code="55",
            latitude=41.1864859,
            longitude=36.1322678,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Samtse District",
            state_code="14",
            latitude=27.0291832,
            longitude=89.0561532,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Samtskhe-Javakheti",
            state_code="SJ",
            latitude=41.5479296,
            longitude=43.27764,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Samukh District",
            state_code="SMX",
            latitude=40.7604631,
            longitude=46.4063181,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Samut Prakan",
            state_code="11",
            latitude=13.5990961,
            longitude=100.5998319,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Samut Sakhon",
            state_code="74",
            latitude=13.5475216,
            longitude=100.2743956,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Samut Songkhram",
            state_code="75",
            latitude=13.4098217,
            longitude=100.0022645,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="San Cristóbal Province",
            state_code="21",
            latitude=18.4180414,
            longitude=-70.1065849,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="San Fernando",
            state_code="SFO",
            latitude=34.2819461,
            longitude=-118.4389719,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="San Germán",
            state_code="125",
            latitude=18.0807082,
            longitude=-67.0411096,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="San Ġwann",
            state_code="49",
            latitude=35.9077365,
            longitude=14.4752416,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="San José",
            state_code="SJ",
            latitude=37.3492968,
            longitude=-121.9056049,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="San José de Ocoa Province",
            state_code="31",
            latitude=18.543858,
            longitude=-70.5041816,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="San José Province",
            state_code="SJ",
            latitude=9.9129727,
            longitude=-84.0768294,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Costa Rica")][0]),
        ))
        list_of_states.append(State(
            name="San Juan",
            state_code="J",
            latitude=-31.5316976,
            longitude=-68.5676962,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="San Juan",
            state_code="127",
            latitude=18.463203,
            longitude=-66.1147571,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="San Juan",
            state_code="SJ",
            latitude=18.45,
            longitude=-66.06666667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="San Juan Province",
            state_code="22",
            latitude=-31.5287127,
            longitude=-68.5360403,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="San Juan-Laventille Regional Corporation",
            state_code="SJL",
            latitude=10.6908578,
            longitude=-61.4552213,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="San Lorenzo",
            state_code="129",
            latitude=18.1886912,
            longitude=-65.9765862,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="San Luis",
            state_code="D",
            latitude=-33.2962042,
            longitude=-66.3294948,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="San Luis Potosí",
            state_code="SLP",
            latitude=22.1564699,
            longitude=-100.9855409,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="San Marcos Department",
            state_code="SM",
            latitude=14.9309569,
            longitude=-91.9099238,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guatemala")][0]),
        ))
        list_of_states.append(State(
            name="San Marino",
            state_code="07",
            latitude=43.94236,
            longitude=12.457777,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "San Marino")][0]),
        ))
        list_of_states.append(State(
            name="San Martín",
            state_code="SAM",
            latitude=37.0849464,
            longitude=-121.6102216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="San Miguel Department",
            state_code="SM",
            latitude=13.4451041,
            longitude=-88.2461183,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="San Pedro de Macorís",
            state_code="23",
            latitude=18.46266,
            longitude=-69.3051234,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="San Pedro Department",
            state_code="2",
            latitude=-24.1948668,
            longitude=-56.561647,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="San Salvador and Rum Cay",
            state_code="SR",
            latitude=23.6854676,
            longitude=-74.8390162,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="San Salvador Department",
            state_code="SS",
            latitude=13.7739997,
            longitude=-89.2086773,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="San Salvador Island",
            state_code="SS",
            latitude=24.0775546,
            longitude=-74.4760088,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="San Sebastián",
            state_code="131",
            latitude=43.318334,
            longitude=-1.9812313,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="San Vicente Department",
            state_code="SV",
            latitude=13.5868561,
            longitude=-88.7493998,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="Sana'a",
            state_code="SN",
            latitude=15.3168913,
            longitude=44.4748018,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Sanaag Region",
            state_code="SA",
            latitude=10.3938218,
            longitude=47.7637565,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Sánchez Ramírez Province",
            state_code="24",
            latitude=19.052706,
            longitude=-70.1492264,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Sancti Spíritus Province",
            state_code="07",
            latitude=21.9938214,
            longitude=-79.4703885,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Sandaun Province",
            state_code="SAN",
            latitude=-3.7126179,
            longitude=141.6834275,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Sandwell",
            state_code="SAW",
            latitude=52.5361674,
            longitude=-2.010793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Sandy Point",
            state_code="SP",
            latitude=39.0145464,
            longitude=-76.3998925,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Sandys",
            state_code="SAN",
            latitude=32.2999528,
            longitude=-64.8674103,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bermuda")][0]),
        ))
        list_of_states.append(State(
            name="Sangha Department",
            state_code="13",
            latitude=1.4662328,
            longitude=15.4068079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Congo")][0]),
        ))
        list_of_states.append(State(
            name="Sangha-Mbaéré",
            state_code="SE",
            latitude=3.4368607,
            longitude=16.3463791,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Sangre Grande Regional Corporation",
            state_code="SGE",
            latitude=10.5852939,
            longitude=-61.1315813,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Trinidad and Tobago")][0]),
        ))
        list_of_states.append(State(
            name="Sanguié Province",
            state_code="SNG",
            latitude=12.1501861,
            longitude=-2.6983868,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Sankuru",
            state_code="SA",
            latitude=-2.8437453,
            longitude=23.3823545,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Şanlıurfa",
            state_code="63",
            latitude=37.3569102,
            longitude=39.1543677,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Sanma",
            state_code="SAM",
            latitude=-15.4840017,
            longitude=166.9182097,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vanuatu")][0]),
        ))
        list_of_states.append(State(
            name="Sanmatenga Province",
            state_code="SMT",
            latitude=13.3565304,
            longitude=-1.0586135,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Sannat",
            state_code="52",
            latitude=36.0192643,
            longitude=14.2599437,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Sant Julià de Lòria",
            state_code="06",
            latitude=42.4529631,
            longitude=1.4918235,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Andorra")][0]),
        ))
        list_of_states.append(State(
            name="Santa Ana Department",
            state_code="SA",
            latitude=14.1461121,
            longitude=-89.5120084,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="Santa Bárbara Department",
            state_code="SB",
            latitude=15.1202795,
            longitude=-88.4016041,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Honduras")][0]),
        ))
        list_of_states.append(State(
            name="Santa Catarina",
            state_code="SC",
            latitude=-27.33,
            longitude=-49.44,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Santa Catarina",
            state_code="CA",
            latitude=-27.2423392,
            longitude=-50.2188556,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Santa Catarina do Fogo",
            state_code="CF",
            latitude=14.9309104,
            longitude=-24.3222577,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Santa Cruz",
            state_code="Z",
            latitude=-51.6352821,
            longitude=-69.2474353,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Santa Cruz",
            state_code="CR",
            latitude=36.9741171,
            longitude=-122.0307963,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (16/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
