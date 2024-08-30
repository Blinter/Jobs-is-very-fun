"""
States Seed #11

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
            name="Loreto",
            state_code="LOR",
            latitude=-4.3741643,
            longitude=-76.1304264,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Lori Region",
            state_code="LO",
            latitude=40.9698452,
            longitude=44.4900138,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Armenia")][0]),
        ))
        list_of_states.append(State(
            name="Loroum Province",
            state_code="LOR",
            latitude=13.8129814,
            longitude=-2.0665197,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Los Lagos",
            state_code="LL",
            latitude=-41.9197779,
            longitude=-72.1416132,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Los Ríos",
            state_code="LR",
            latitude=-40.2310217,
            longitude=-72.331113,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Los Ríos",
            state_code="R",
            latitude=-1.0230607,
            longitude=-79.4608897,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Los Santos Province",
            state_code="7",
            latitude=7.5909302,
            longitude=-80.365865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Panama")][0]),
        ))
        list_of_states.append(State(
            name="Loška Dolina Municipality",
            state_code="065",
            latitude=45.6477908,
            longitude=14.4973147,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Loški Potok Municipality",
            state_code="066",
            latitude=45.6909637,
            longitude=14.598597,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Lot",
            state_code="46",
            latitude=44.624607,
            longitude=1.0357631,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Lot-et-Garonne",
            state_code="47",
            latitude=44.3687314,
            longitude=-0.0916169,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Louga",
            state_code="LG",
            latitude=15.6141768,
            longitude=-16.22868,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Louisiana",
            state_code="LA",
            latitude=30.9842977,
            longitude=-91.9623327,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Louny",
            state_code="424",
            latitude=50.3539812,
            longitude=13.8033551,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Louth",
            state_code="LH",
            latitude=53.9252324,
            longitude=-6.4889423,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Lovech Province",
            state_code="11",
            latitude=43.1367798,
            longitude=24.7139335,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Lovrenc na Pohorju Municipality",
            state_code="167",
            latitude=46.5419638,
            longitude=15.4000443,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Lower Austria",
            state_code="3",
            latitude=48.108077,
            longitude=15.8049558,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Austria")][0]),
        ))
        list_of_states.append(State(
            name="Lower Juba",
            state_code="JH",
            latitude=0.224021,
            longitude=41.6011814,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Lower River Division",
            state_code="L",
            latitude=13.3553306,
            longitude=-15.92299,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gambia The")][0]),
        ))
        list_of_states.append(State(
            name="Lower Saxony",
            state_code="NI",
            latitude=52.6367036,
            longitude=9.8450766,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Lower Shebelle",
            state_code="SH",
            latitude=1.8766458,
            longitude=44.2479015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Lower Silesian Voivodeship",
            state_code="DS",
            latitude=51.1339861,
            longitude=16.8841961,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Loyalty Islands Province",
            state_code="03",
            latitude=-20.9667,
            longitude=167.2333,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Caledonia")][0]),
        ))
        list_of_states.append(State(
            name="Lozère",
            state_code="48",
            latitude=44.5422779,
            longitude=2.9293459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Lozovo Municipality",
            state_code="49",
            latitude=41.7818139,
            longitude=21.9000827,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Lualaba",
            state_code="LU",
            latitude=-10.4808698,
            longitude=25.6297816,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Luanda Province",
            state_code="LUA",
            latitude=-9.035088,
            longitude=13.2663479,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Luang Namtha Province",
            state_code="LM",
            latitude=20.9170187,
            longitude=101.1617356,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Luang Prabang Province",
            state_code="LP",
            latitude=20.0656229,
            longitude=102.6216211,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Laos")][0]),
        ))
        list_of_states.append(State(
            name="Luapula Province",
            state_code="04",
            latitude=-11.564831,
            longitude=29.0459927,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zambia")][0]),
        ))
        list_of_states.append(State(
            name="Lubāna Municipality",
            state_code="057",
            latitude=56.8999269,
            longitude=26.7198789,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Lublin Voivodeship",
            state_code="LU",
            latitude=51.2493519,
            longitude=23.1011392,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Lubombo District",
            state_code="LU",
            latitude=-26.7851773,
            longitude=31.8107079,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Eswatini")][0]),
        ))
        list_of_states.append(State(
            name="Lubusz Voivodeship",
            state_code="LB",
            latitude=52.2274612,
            longitude=15.2559103,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Lucca",
            state_code="LU",
            latitude=43.8376736,
            longitude=10.495053,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Luče Municipality",
            state_code="067",
            latitude=46.3544925,
            longitude=14.7471504,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Lucerne",
            state_code="LU",
            latitude=47.0795671,
            longitude=8.1662445,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Ludza Municipality",
            state_code="058",
            latitude=56.545959,
            longitude=27.7143199,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Lugo",
            state_code="LU",
            latitude=43.0123137,
            longitude=-7.5740096,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Luhanska oblast",
            state_code="09",
            latitude=48.574041,
            longitude=39.307815,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Lukovica Municipality",
            state_code="068",
            latitude=46.1696293,
            longitude=14.6907259,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Lumbini Zone",
            state_code="LU",
            latitude=27.45,
            longitude=83.25,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Lunda Norte Province",
            state_code="LNO",
            latitude=-8.3525022,
            longitude=19.1880047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Lunda Sul Province",
            state_code="LSU",
            latitude=-10.2866578,
            longitude=20.7122465,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Luqa",
            state_code="25",
            latitude=35.8582865,
            longitude=14.4868883,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Luquillo",
            state_code="089",
            latitude=18.3724507,
            longitude=-65.7165511,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Lusaka Province",
            state_code="09",
            latitude=-15.3657129,
            longitude=29.2320784,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zambia")][0]),
        ))
        list_of_states.append(State(
            name="Lushnjë District",
            state_code="LU",
            latitude=40.941983,
            longitude=19.6996428,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Luuka District",
            state_code="229",
            latitude=0.7250599,
            longitude=33.3037143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Luwero District",
            state_code="104",
            latitude=0.8271118,
            longitude=32.6277455,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Luxembourg",
            state_code="WLX",
            latitude=49.815273,
            longitude=6.129583,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="Luxembourg District",
            state_code="L",
            latitude=49.5953706,
            longitude=6.1333178,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Luxembourg")][0]),
        ))
        list_of_states.append(State(
            name="Luxor",
            state_code="LX",
            latitude=25.3944444,
            longitude=32.4920088,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Lvivska oblast",
            state_code="46",
            latitude=49.839683,
            longitude=24.029717,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Lwengo District",
            state_code="124",
            latitude=-0.4165288,
            longitude=31.3998995,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Lyantonde District",
            state_code="114",
            latitude=-0.2240696,
            longitude=31.2168466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="M'Sila",
            state_code="28",
            latitude=35.7186646,
            longitude=4.5233423,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Ma'an",
            state_code="MN",
            latitude=30.1926789,
            longitude=35.7249319,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jordan")][0]),
        ))
        list_of_states.append(State(
            name="Ma'rib",
            state_code="MA",
            latitude=15.515888,
            longitude=45.4498065,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Yemen")][0]),
        ))
        list_of_states.append(State(
            name="Macau SAR",
            state_code="MO",
            latitude=22.198745,
            longitude=113.543873,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Macenta Prefecture",
            state_code="MC",
            latitude=8.4615795,
            longitude=-9.2785583,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Macerata",
            state_code="MC",
            latitude=43.2459322,
            longitude=13.2663479,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Machakos",
            state_code="22",
            latitude=-1.5176837,
            longitude=37.2634146,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Machinga District",
            state_code="MH",
            latitude=-14.9407263,
            longitude=35.4781926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Macuata",
            state_code="07",
            latitude=-16.4864922,
            longitude=179.2847251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Mačva District",
            state_code="08",
            latitude=44.5925314,
            longitude=19.5082246,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Madaba",
            state_code="MD",
            latitude=31.7196097,
            longitude=35.7932754,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jordan")][0]),
        ))
        list_of_states.append(State(
            name="Madang Province",
            state_code="MPM",
            latitude=-4.9849733,
            longitude=145.1375834,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Madaripur District",
            state_code="36",
            latitude=23.2393346,
            longitude=90.1869644,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Madeira",
            state_code="30",
            latitude=32.7607074,
            longitude=-16.9594723,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Portugal")][0]),
        ))
        list_of_states.append(State(
            name="Madhya Pradesh",
            state_code="MP",
            latitude=22.9734229,
            longitude=78.6568942,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Madinat ash Shamal",
            state_code="MS",
            latitude=26.1182743,
            longitude=51.2157265,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Qatar")][0]),
        ))
        list_of_states.append(State(
            name="Madona Municipality",
            state_code="059",
            latitude=56.8598923,
            longitude=26.2276201,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Madre de Dios",
            state_code="MDD",
            latitude=-11.7668705,
            longitude=-70.8119953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Madrid",
            state_code="M",
            latitude=40.4167515,
            longitude=-3.7038322,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Madriz",
            state_code="MD",
            latitude=13.4726005,
            longitude=-86.4592091,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Mae Hong Son",
            state_code="58",
            latitude=19.3020296,
            longitude=97.9654368,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Maekel Region",
            state_code="MA",
            latitude=15.3551409,
            longitude=38.8623683,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Eritrea")][0]),
        ))
        list_of_states.append(State(
            name="Mafeteng District",
            state_code="E",
            latitude=-29.8041008,
            longitude=27.5026174,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lesotho")][0]),
        ))
        list_of_states.append(State(
            name="Mafraq",
            state_code="MA",
            latitude=32.3416923,
            longitude=36.2020175,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jordan")][0]),
        ))
        list_of_states.append(State(
            name="Magadan Oblast",
            state_code="MAG",
            latitude=62.6643417,
            longitude=153.914991,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Magallanes y de la Antártica Chilena",
            state_code="MA",
            latitude=-52.2064316,
            longitude=-72.1685001,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Magdalena",
            state_code="MAG",
            latitude=10.4113014,
            longitude=-74.4056612,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Magherafelt District Council",
            state_code="MFT",
            latitude=54.7553279,
            longitude=-6.6077487,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Maguindanao",
            state_code="MAG",
            latitude=6.9422581,
            longitude=124.4198243,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Magway Region",
            state_code="03",
            latitude=19.8871386,
            longitude=94.7277528,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Maha Sarakham",
            state_code="44",
            latitude=16.0132015,
            longitude=103.1615169,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Mahaica-Berbice",
            state_code="MA",
            latitude=6.238496,
            longitude=-57.9162555,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guyana")][0]),
        ))
        list_of_states.append(State(
            name="Mahajanga Province",
            state_code="M",
            latitude=-16.523883,
            longitude=46.516262,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Madagascar")][0]),
        ))
        list_of_states.append(State(
            name="Mahakali Zone",
            state_code="MA",
            latitude=29.3601079,
            longitude=80.543845,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Maharashtra",
            state_code="MH",
            latitude=19.7514798,
            longitude=75.7138884,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Mahdia",
            state_code="53",
            latitude=35.3352558,
            longitude=10.8903099,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Mai-Ndombe",
            state_code="MN",
            latitude=-2.6357434,
            longitude=18.4276047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Maine",
            state_code="ME",
            latitude=45.253783,
            longitude=-69.4454689,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Maine-et-Loire",
            state_code="49",
            latitude=47.3890034,
            longitude=-1.1202527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Maio Municipality",
            state_code="MA",
            latitude=15.2003098,
            longitude=-23.1679793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Majšperk Municipality",
            state_code="069",
            latitude=46.3503019,
            longitude=15.7340595,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Makamba Province",
            state_code="MA",
            latitude=-4.3257062,
            longitude=29.6962677,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Makedonska Kamenica Municipality",
            state_code="51",
            latitude=42.0694604,
            longitude=22.548349,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Makedonski Brod Municipality",
            state_code="52",
            latitude=41.5133088,
            longitude=21.2174329,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Makira-Ulawa Province",
            state_code="MK",
            latitude=-10.5737447,
            longitude=161.8096941,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Solomon Islands")][0]),
        ))
        list_of_states.append(State(
            name="Makkah",
            state_code="02",
            latitude=21.5235584,
            longitude=41.9196471,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Makole Municipality",
            state_code="198",
            latitude=46.3168697,
            longitude=15.6664126,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Makueni",
            state_code="23",
            latitude=-2.2558734,
            longitude=37.8936663,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Malacca",
            state_code="04",
            latitude=2.189594,
            longitude=102.2500868,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malaysia")][0]),
        ))
        list_of_states.append(State(
            name="Málaga",
            state_code="MA",
            latitude=36.7182015,
            longitude=-4.519306,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Malaita Province",
            state_code="ML",
            latitude=-8.9446168,
            longitude=160.9071236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Solomon Islands")][0]),
        ))
        list_of_states.append(State(
            name="Malampa",
            state_code="MAP",
            latitude=-16.4011405,
            longitude=167.6077865,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vanuatu")][0]),
        ))
        list_of_states.append(State(
            name="Malanje Province",
            state_code="MAL",
            latitude=-9.8251183,
            longitude=16.912251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Malatya",
            state_code="44",
            latitude=38.4015057,
            longitude=37.9536298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Maldonado",
            state_code="MA",
            latitude=-34.5597932,
            longitude=-54.8628552,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Malé",
            state_code="MLE",
            latitude=46.3488867,
            longitude=10.9072489,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Malësi e Madhe District",
            state_code="MM",
            latitude=42.4245173,
            longitude=19.6163185,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Mali Prefecture",
            state_code="ML",
            latitude=11.983709,
            longitude=-12.2547919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Mallakastër District",
            state_code="MK",
            latitude=40.5273376,
            longitude=19.7829791,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Mālpils Municipality",
            state_code="061",
            latitude=57.0084119,
            longitude=24.9574278,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Maluku",
            state_code="MA",
            latitude=-3.2384616,
            longitude=130.1452734,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Maluku Utara",
            state_code="MU",
            latitude=1.5709993,
            longitude=127.8087693,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Indonesia")][0]),
        ))
        list_of_states.append(State(
            name="Mambéré-Kadéï",
            state_code="HS",
            latitude=4.7055653,
            longitude=15.9699878,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Mamou Prefecture",
            state_code="MM",
            latitude=10.5736024,
            longitude=-11.8891721,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Mamou Region",
            state_code="M",
            latitude=10.5736024,
            longitude=-11.8891721,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Manabí",
            state_code="M",
            latitude=-1.0543434,
            longitude=-80.452644,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Manafwa District",
            state_code="223",
            latitude=0.9063599,
            longitude=34.2866091,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Managua",
            state_code="MN",
            latitude=12.1391699,
            longitude=-86.3376761,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Manatí",
            state_code="091",
            latitude=18.4181215,
            longitude=-66.5262783,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Manatuto District",
            state_code="MT",
            latitude=-8.5155608,
            longitude=126.0159255,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Timor-Leste")][0]),
        ))
        list_of_states.append(State(
            name="Manawatu-Wanganui Region",
            state_code="MWT",
            latitude=-39.7273356,
            longitude=175.4375574,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Manche",
            state_code="50",
            latitude=49.0881734,
            longitude=-2.4627209,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Manchester",
            state_code="MAN",
            latitude=53.4807593,
            longitude=-2.2426305,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Manchester Parish",
            state_code="12",
            latitude=18.0669654,
            longitude=-77.5160788,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jamaica")][0]),
        ))
        list_of_states.append(State(
            name="Mandalay Region",
            state_code="04",
            latitude=21.5619058,
            longitude=95.8987139,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Mandera",
            state_code="24",
            latitude=3.5737991,
            longitude=40.958688,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Mandiana Prefecture",
            state_code="MD",
            latitude=10.6172827,
            longitude=-8.6985716,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Mandoul",
            state_code="MA",
            latitude=8.603091,
            longitude=17.4795173,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Mangochi District",
            state_code="MG",
            latitude=-14.1388248,
            longitude=35.0388164,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Mangrove Cay",
            state_code="MC",
            latitude=24.1481425,
            longitude=-77.7680952,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Mangystau Region",
            state_code="MAN",
            latitude=44.590802,
            longitude=53.8499508,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kazakhstan")][0]),
        ))
        list_of_states.append(State(
            name="Manica Province",
            state_code="B",
            latitude=-19.5059787,
            longitude=33.438353,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Manicaland",
            state_code="MA",
            latitude=-18.9216386,
            longitude=32.174605,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zimbabwe")][0]),
        ))
        list_of_states.append(State(
            name="Maniema",
            state_code="MA",
            latitude=-3.0730929,
            longitude=26.0413889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Manipur",
            state_code="MN",
            latitude=24.6637173,
            longitude=93.9062688,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Manisa",
            state_code="45",
            latitude=38.8419373,
            longitude=28.1122679,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Manitoba",
            state_code="MB",
            latitude=53.7608608,
            longitude=-98.8138762,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Canada")][0]),
        ))
        list_of_states.append(State(
            name="Mannar District",
            state_code="43",
            latitude=8.9809531,
            longitude=79.9043975,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Manouba",
            state_code="14",
            latitude=36.8446504,
            longitude=9.8571416,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Mantua",
            state_code="MN",
            latitude=45.1667728,
            longitude=10.7753613,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Manufahi Municipality",
            state_code="MF",
            latitude=-9.0145495,
            longitude=125.8279959,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Timor-Leste")][0]),
        ))
        list_of_states.append(State(
            name="Manus Province",
            state_code="MRL",
            latitude=-2.0941169,
            longitude=146.8760951,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Manyara",
            state_code="26",
            latitude=-4.3150058,
            longitude=36.954107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Manzini District",
            state_code="MA",
            latitude=-26.5081999,
            longitude=31.3713164,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Eswatini")][0]),
        ))
        list_of_states.append(State(
            name="Maputo",
            state_code="MPM",
            latitude=-25.969248,
            longitude=32.5731746,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Maputo Province",
            state_code="L",
            latitude=-25.2569876,
            longitude=32.5372741,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Mara",
            state_code="13",
            latitude=-1.7753538,
            longitude=34.1531947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Maracha District",
            state_code="320",
            latitude=3.2873127,
            longitude=30.9403023,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Maradi Region",
            state_code="4",
            latitude=13.8018074,
            longitude=7.4381355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Niger")][0]),
        ))
        list_of_states.append(State(
            name="Marahoué Region",
            state_code="12",
            latitude=6.8846207,
            longitude=-5.8987139,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Maramureș County",
            state_code="MM",
            latitude=46.5569904,
            longitude=24.6723215,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Maranhão",
            state_code="MA",
            latitude=-4.9609498,
            longitude=-45.2744159,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Marche",
            state_code="57",
            latitude=43.304562,
            longitude=13.71947,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Mardin",
            state_code="47",
            latitude=37.3442929,
            longitude=40.6196487,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Margibi County",
            state_code="MG",
            latitude=6.5151875,
            longitude=-10.3048897,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Mari El Republic",
            state_code="ME",
            latitude=56.438457,
            longitude=47.9607758,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="María Trinidad Sánchez Province",
            state_code="14",
            latitude=19.3734597,
            longitude=-69.8514439,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Maribor City Municipality",
            state_code="070",
            latitude=46.5506496,
            longitude=15.6205439,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Maricao",
            state_code="093",
            latitude=18.1807902,
            longitude=-66.9799001,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Marijampolė County",
            state_code="MR",
            latitude=54.7819971,
            longitude=23.1341365,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Marijampolė Municipality",
            state_code="25",
            latitude=54.5711094,
            longitude=23.4859371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Marinduque",
            state_code="MAD",
            latitude=13.4767171,
            longitude=121.9032192,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Maritime",
            state_code="M",
            latitude=41.6551493,
            longitude=-83.5278467,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Togo")][0]),
        ))
        list_of_states.append(State(
            name="Marj District",
            state_code="MJ",
            latitude=32.0550363,
            longitude=21.1891151,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Markazi",
            state_code="00",
            latitude=34.612305,
            longitude=49.8547266,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Markovci Municipality",
            state_code="168",
            latitude=46.3879309,
            longitude=15.9586014,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Marlborough Region",
            state_code="MBH",
            latitude=-41.5916883,
            longitude=173.7624053,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "New Zealand")][0]),
        ))
        list_of_states.append(State(
            name="Marne",
            state_code="51",
            latitude=48.9610745,
            longitude=3.6573767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Marowijne District",
            state_code="MA",
            latitude=5.6268128,
            longitude=-54.2593118,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Suriname")][0]),
        ))
        list_of_states.append(State(
            name="Marrakech",
            state_code="MAR",
            latitude=31.6346023,
            longitude=-8.0778932,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Marrakesh-Safi",
            state_code="07",
            latitude=31.7330833,
            longitude=-8.1338558,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Marsa",
            state_code="26",
            latitude=34.0319587,
            longitude=-118.4455535,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Marsabit",
            state_code="25",
            latitude=2.4426403,
            longitude=37.9784585,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Marsaskala",
            state_code="27",
            latitude=35.860364,
            longitude=14.5567876,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Marsaxlokk",
            state_code="28",
            latitude=35.8411699,
            longitude=14.5393097,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Marsh Harbour",
            state_code="MH",
            latitude=26.5241653,
            longitude=-77.0909809,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Martinique",
            state_code="972",
            latitude=14.641528,
            longitude=-61.024174,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Martuni",
            state_code="XVD",
            latitude=39.7914693,
            longitude=47.1100814,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Mārupe Municipality",
            state_code="062",
            latitude=56.8965717,
            longitude=24.0460049,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Mary Region",
            state_code="M",
            latitude=36.9481623,
            longitude=62.4504154,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkmenistan")][0]),
        ))
        list_of_states.append(State(
            name="Maryland",
            state_code="MD",
            latitude=39.0457549,
            longitude=-76.6412712,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Maryland County",
            state_code="MY",
            latitude=39.0457549,
            longitude=-76.6412712,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Masaka District",
            state_code="105",
            latitude=-0.4463691,
            longitude=31.9017954,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Masally District",
            state_code="MAS",
            latitude=39.0340722,
            longitude=48.6589354,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Masaya",
            state_code="MS",
            latitude=11.9759328,
            longitude=-86.0733498,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Masbate",
            state_code="MAS",
            latitude=12.3574346,
            longitude=123.5504076,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Mascara",
            state_code="29",
            latitude=35.3904125,
            longitude=0.1494988,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Maseru District",
            state_code="A",
            latitude=-29.516565,
            longitude=27.8311428,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lesotho")][0]),
        ))
        list_of_states.append(State(
            name="Mashonaland Central Province",
            state_code="MC",
            latitude=-16.7644295,
            longitude=31.0793705,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zimbabwe")][0]),
        ))
        list_of_states.append(State(
            name="Mashonaland East Province",
            state_code="ME",
            latitude=-18.5871642,
            longitude=31.2626366,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zimbabwe")][0]),
        ))
        list_of_states.append(State(
            name="Mashonaland West Province",
            state_code="MW",
            latitude=-17.4851029,
            longitude=29.7889248,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zimbabwe")][0]),
        ))
        list_of_states.append(State(
            name="Masindi District",
            state_code="409",
            latitude=1.4920363,
            longitude=31.7195459,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Masovian Voivodeship",
            state_code="MZ",
            latitude=51.8927182,
            longitude=21.0021679,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="Massa and Carrara",
            state_code="MS",
            latitude=44.2213998,
            longitude=10.0359661,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Massachusetts",
            state_code="MA",
            latitude=42.4072107,
            longitude=-71.3824374,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Masvingo Province",
            state_code="MV",
            latitude=-20.6241509,
            longitude=31.2626366,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zimbabwe")][0]),
        ))
        list_of_states.append(State(
            name="Mat District",
            state_code="MT",
            latitude=41.5937675,
            longitude=19.9973244,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Matabeleland North Province",
            state_code="MN",
            latitude=-18.5331566,
            longitude=27.5495846,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zimbabwe")][0]),
        ))
        list_of_states.append(State(
            name="Matabeleland South Province",
            state_code="MS",
            latitude=-21.052337,
            longitude=29.0459927,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zimbabwe")][0]),
        ))
        list_of_states.append(State(
            name="Matagalpa",
            state_code="MT",
            latitude=12.9498436,
            longitude=-85.4375574,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nicaragua")][0]),
        ))
        list_of_states.append(State(
            name="Matale District",
            state_code="22",
            latitude=7.4659646,
            longitude=80.6234259,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Matam",
            state_code="MT",
            latitude=15.6600225,
            longitude=-13.2576906,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Matanzas Province",
            state_code="04",
            latitude=22.5767123,
            longitude=-81.3399414,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Matara District",
            state_code="32",
            latitude=5.9449348,
            longitude=80.5487997,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Matera",
            state_code="MT",
            latitude=40.6663496,
            longitude=16.6043636,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Mato Grosso",
            state_code="MT",
            latitude=-12.6818712,
            longitude=-56.921099,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Mato Grosso do Sul",
            state_code="MS",
            latitude=-20.7722295,
            longitude=-54.7851531,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Matrouh",
            state_code="MT",
            latitude=29.569635,
            longitude=26.419389,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Maule",
            state_code="ML",
            latitude=-35.5163603,
            longitude=-71.5723953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chile")][0]),
        ))
        list_of_states.append(State(
            name="Maunabo",
            state_code="095",
            latitude=18.0071885,
            longitude=-65.8993289,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Mauren",
            state_code="04",
            latitude=47.2189285,
            longitude=9.541735,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liechtenstein")][0]),
        ))
        list_of_states.append(State(
            name="Mavrovo and Rostuša Municipality",
            state_code="50",
            latitude=41.6092427,
            longitude=20.6012488,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Mayabeque Province",
            state_code="16",
            latitude=22.8926529,
            longitude=-81.9534815,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cuba")][0]),
        ))
        list_of_states.append(State(
            name="Mayaguana District",
            state_code="MG",
            latitude=22.4017714,
            longitude=-73.0641396,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "The Bahamas")][0]),
        ))
        list_of_states.append(State(
            name="Mayagüez",
            state_code="097",
            latitude=18.2013452,
            longitude=-67.1451549,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Mayagüez",
            state_code="MG",
            latitude=18.20111111,
            longitude=-67.13972222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Mayenne",
            state_code="53",
            latitude=48.3066842,
            longitude=-0.6490182,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Mayo",
            state_code="MO",
            latitude=54.0152604,
            longitude=-9.4289369,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Mayo-Kebbi Est",
            state_code="ME",
            latitude=9.4046039,
            longitude=14.8454619,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Mayo-Kebbi Ouest",
            state_code="MO",
            latitude=10.4113014,
            longitude=15.5943388,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Mayotte",
            state_code="976",
            latitude=-12.8275,
            longitude=45.166244,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Maysan",
            state_code="MA",
            latitude=31.8734002,
            longitude=47.1362125,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Mayuge District",
            state_code="214",
            latitude=-0.2182982,
            longitude=33.5728027,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Mazandaran",
            state_code="02",
            latitude=36.2262393,
            longitude=52.5318604,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Mažeikiai District Municipality",
            state_code="26",
            latitude=56.3092439,
            longitude=22.341468,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Mazsalaca Municipality",
            state_code="060",
            latitude=57.9267749,
            longitude=25.0669895,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Mbale District",
            state_code="209",
            latitude=1.0344274,
            longitude=34.1976882,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Mbarara District",
            state_code="410",
            latitude=-0.6071596,
            longitude=30.6545022,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Mbeya",
            state_code="14",
            latitude=-8.2866112,
            longitude=32.8132537,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Mbomou Prefecture",
            state_code="MB",
            latitude=5.556837,
            longitude=23.7632828,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Mchinji District",
            state_code="MC",
            latitude=-13.7401525,
            longitude=32.9888319,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Mdina",
            state_code="29",
            latitude=35.888093,
            longitude=14.4068357,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Meath",
            state_code="MH",
            latitude=53.605548,
            longitude=-6.6564169,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Mechi Zone",
            state_code="ME",
            latitude=26.8760007,
            longitude=87.9334803,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Mecklenburg-Vorpommern",
            state_code="MV",
            latitude=53.6126505,
            longitude=12.4295953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Germany")][0]),
        ))
        list_of_states.append(State(
            name="Médéa",
            state_code="26",
            latitude=36.2637078,
            longitude=2.7587857,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Medenine",
            state_code="82",
            latitude=33.2280565,
            longitude=10.8903099,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Medio Campidano",
            state_code="VS",
            latitude=39.5317389,
            longitude=8.704075,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Médiouna",
            state_code="MED",
            latitude=33.4540939,
            longitude=-7.516602,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Medvode Municipality",
            state_code="071",
            latitude=46.141908,
            longitude=14.4032596,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Medway",
            state_code="MDW",
            latitude=42.1417641,
            longitude=-71.3967256,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Meemu Atoll",
            state_code="12",
            latitude=3.0090345,
            longitude=73.5122928,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Maldives")][0]),
        ))
        list_of_states.append(State(
            name="Meghalaya",
            state_code="ML",
            latitude=25.4670308,
            longitude=91.366216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (11/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
