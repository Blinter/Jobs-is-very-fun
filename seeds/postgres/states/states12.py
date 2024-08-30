"""
States Seed #12

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
            name="Mehedinți County",
            state_code="MH",
            latitude=44.5515053,
            longitude=22.9044157,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Meherpur District",
            state_code="39",
            latitude=23.8051991,
            longitude=88.6723578,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Meknès",
            state_code="MEK",
            latitude=33.881,
            longitude=-5.5730397,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Melekeok",
            state_code="212",
            latitude=7.5150286,
            longitude=134.5972518,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palau")][0]),
        ))
        list_of_states.append(State(
            name="Melilla",
            state_code="ML",
            latitude=35.2937,
            longitude=-2.9383,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Mellieħa",
            state_code="30",
            latitude=35.9523529,
            longitude=14.3500975,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Mělník",
            state_code="206",
            latitude=50.3104415,
            longitude=14.5179223,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Ménaka Region",
            state_code="9",
            latitude=15.9156421,
            longitude=2.396174,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Mendoza",
            state_code="M",
            latitude=-32.8894587,
            longitude=-68.8458386,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Meneng District",
            state_code="11",
            latitude=-0.546724,
            longitude=166.938379,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nauru")][0]),
        ))
        list_of_states.append(State(
            name="Mengeš Municipality",
            state_code="072",
            latitude=46.1659122,
            longitude=14.5719694,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Mérida",
            state_code="L",
            latitude=20.9673702,
            longitude=-89.5925857,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Mersin",
            state_code="33",
            latitude=36.8120858,
            longitude=34.641475,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Mērsrags Municipality",
            state_code="063",
            latitude=57.3306881,
            longitude=23.1023707,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Merthyr Tydfil County Borough",
            state_code="MTY",
            latitude=51.7467474,
            longitude=-3.3813275,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Meru",
            state_code="26",
            latitude=0.3557174,
            longitude=37.8087693,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Meta",
            state_code="MET",
            latitude=39.7673258,
            longitude=-104.9753595,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Colombia")][0]),
        ))
        list_of_states.append(State(
            name="Metlika Municipality",
            state_code="073",
            latitude=45.6480715,
            longitude=15.3177838,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Metro Manila",
            state_code="NCR",
            latitude=14.6090537,
            longitude=121.0222565,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Métropole de Lyon",
            state_code="69M",
            latitude=45.7482629,
            longitude=4.5958404,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Metropolitan Borough of Wigan",
            state_code="WGN",
            latitude=53.5134812,
            longitude=-2.6106999,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Meurthe-et-Moselle",
            state_code="54",
            latitude=48.9556615,
            longitude=5.714235,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Meuse",
            state_code="55",
            latitude=49.012462,
            longitude=4.8108734,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Mežica Municipality",
            state_code="074",
            latitude=46.5215027,
            longitude=14.852134,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Međimurje",
            state_code="20",
            latitude=46.3766644,
            longitude=16.4213298,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Mġarr",
            state_code="31",
            latitude=35.9189327,
            longitude=14.3617343,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Miaoli",
            state_code="MIA",
            latitude=24.560159,
            longitude=120.8214265,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Michigan",
            state_code="MI",
            latitude=44.3148443,
            longitude=-85.6023643,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Michoacán de Ocampo",
            state_code="MIC",
            latitude=19.5665192,
            longitude=-101.7068294,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Micoud Quarter",
            state_code="08",
            latitude=13.8211871,
            longitude=-60.9001934,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saint Lucia")][0]),
        ))
        list_of_states.append(State(
            name="Mid and East Antrim",
            state_code="MEA",
            latitude=54.9399341,
            longitude=-6.1137423,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Mid Ulster",
            state_code="MUL",
            latitude=54.6411301,
            longitude=-6.7522549,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Mid-Western Region",
            state_code="2",
            latitude=38.4111841,
            longitude=-90.3832098,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nepal")][0]),
        ))
        list_of_states.append(State(
            name="Middle Juba",
            state_code="JD",
            latitude=2.0780488,
            longitude=41.6011814,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Middle Shebelle",
            state_code="SD",
            latitude=2.9250247,
            longitude=45.9039689,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Middlesbrough",
            state_code="MDB",
            latitude=54.574227,
            longitude=-1.234956,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Midelt",
            state_code="MID",
            latitude=32.6855079,
            longitude=-4.7501709,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Midlands Province",
            state_code="MI",
            latitude=-19.0552009,
            longitude=29.6035495,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zimbabwe")][0]),
        ))
        list_of_states.append(State(
            name="Midlothian",
            state_code="MLN",
            latitude=32.475335,
            longitude=-97.0103181,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Midway Atoll",
            state_code="UM-71",
            latitude=28.2072168,
            longitude=-177.3734926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Midway Islands",
            state_code="71",
            latitude=28.2072168,
            longitude=-177.3734926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States Minor Outlying Islands")][0]),
        ))
        list_of_states.append(State(
            name="Mie Prefecture",
            state_code="24",
            latitude=33.8143901,
            longitude=136.0487047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Migori",
            state_code="27",
            latitude=-0.9365702,
            longitude=34.4198243,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Miklavž na Dravskem Polju Municipality",
            state_code="169",
            latitude=46.5082628,
            longitude=15.6952065,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Mila",
            state_code="43",
            latitude=36.3647957,
            longitude=6.1526985,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Milne Bay Province",
            state_code="MBA",
            latitude=-9.5221451,
            longitude=150.6749653,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Milton Keynes",
            state_code="MIK",
            latitude=52.0852038,
            longitude=-0.7333133,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Mimaropa",
            state_code="41",
            latitude=9.8432065,
            longitude=118.7364783,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Minas Gerais",
            state_code="MG",
            latitude=-18.512178,
            longitude=-44.5550308,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Brazil")][0]),
        ))
        list_of_states.append(State(
            name="Mingachevir",
            state_code="MI",
            latitude=40.7702563,
            longitude=47.0496015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Minnesota",
            state_code="MN",
            latitude=46.729553,
            longitude=-94.6858998,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Minsk",
            state_code="HM",
            latitude=53.9006011,
            longitude=27.558972,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belarus")][0]),
        ))
        list_of_states.append(State(
            name="Minsk Region",
            state_code="MI",
            latitude=54.1067889,
            longitude=27.4129245,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belarus")][0]),
        ))
        list_of_states.append(State(
            name="Minya",
            state_code="MN",
            latitude=28.284729,
            longitude=30.5279096,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Miranda",
            state_code="M",
            latitude=42.3519383,
            longitude=-71.5290766,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Mirditë District",
            state_code="MR",
            latitude=41.764286,
            longitude=19.9020509,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Albania")][0]),
        ))
        list_of_states.append(State(
            name="Miren–Kostanjevica Municipality",
            state_code="075",
            latitude=45.8436029,
            longitude=13.6276647,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Mirna Municipality",
            state_code="212",
            latitude=45.9515647,
            longitude=15.0620977,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Mirna Peč Municipality",
            state_code="170",
            latitude=45.8481574,
            longitude=15.087945,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Misamis Occidental",
            state_code="MSC",
            latitude=8.3374903,
            longitude=123.7070619,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Misamis Oriental",
            state_code="MSR",
            latitude=8.5045558,
            longitude=124.6219592,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Misiones",
            state_code="N",
            latitude=-27.4269255,
            longitude=-55.9467076,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Argentina")][0]),
        ))
        list_of_states.append(State(
            name="Misiones Department",
            state_code="8",
            latitude=-26.8433512,
            longitude=-57.1013188,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Paraguay")][0]),
        ))
        list_of_states.append(State(
            name="Miskolc",
            state_code="MI",
            latitude=48.1034775,
            longitude=20.7784384,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Mislinja Municipality",
            state_code="076",
            latitude=46.4429403,
            longitude=15.1987678,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Misrata District",
            state_code="MI",
            latitude=32.3255884,
            longitude=15.0992556,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Mississippi",
            state_code="MS",
            latitude=32.3546679,
            longitude=-89.3985283,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Missouri",
            state_code="MO",
            latitude=37.9642529,
            longitude=-91.8318334,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Mitooma District",
            state_code="423",
            latitude=-0.6193276,
            longitude=30.0202964,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Mityana District",
            state_code="115",
            latitude=0.4454845,
            longitude=32.0837445,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Miyagi Prefecture",
            state_code="04",
            latitude=38.630612,
            longitude=141.1193048,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Miyazaki Prefecture",
            state_code="45",
            latitude=32.6036022,
            longitude=131.441251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Mizoram",
            state_code="MZ",
            latitude=23.164543,
            longitude=92.9375739,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Mladá Boleslav",
            state_code="207",
            latitude=50.4252317,
            longitude=14.9362477,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Moca",
            state_code="099",
            latitude=18.3967929,
            longitude=-67.1479035,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Modena",
            state_code="MO",
            latitude=44.5513799,
            longitude=10.918048,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Mogila Municipality",
            state_code="53",
            latitude=41.1479645,
            longitude=21.4514369,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Mogilev Region",
            state_code="MA",
            latitude=53.5101791,
            longitude=30.4006444,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belarus")][0]),
        ))
        list_of_states.append(State(
            name="Mohale's Hoek District",
            state_code="F",
            latitude=-30.1425917,
            longitude=27.4673845,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lesotho")][0]),
        ))
        list_of_states.append(State(
            name="Mohammadia",
            state_code="MOH",
            latitude=33.6873749,
            longitude=-7.4239142,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Mohéli",
            state_code="M",
            latitude=-12.3377376,
            longitude=43.7334089,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Comoros")][0]),
        ))
        list_of_states.append(State(
            name="Mojkovac Municipality",
            state_code="11",
            latitude=42.9688018,
            longitude=19.5211063,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Montenegro")][0]),
        ))
        list_of_states.append(State(
            name="Moka",
            state_code="MO",
            latitude=-20.2399782,
            longitude=57.575926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mauritius")][0]),
        ))
        list_of_states.append(State(
            name="Mokhotlong District",
            state_code="J",
            latitude=-29.2573193,
            longitude=28.9528645,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lesotho")][0]),
        ))
        list_of_states.append(State(
            name="Mokronog–Trebelno Municipality",
            state_code="199",
            latitude=45.9088529,
            longitude=15.1596736,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Molėtai District Municipality",
            state_code="27",
            latitude=55.2265309,
            longitude=25.4180011,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Molise",
            state_code="67",
            latitude=41.6738865,
            longitude=14.7520939,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Mombasa",
            state_code="28",
            latitude=-3.9768291,
            longitude=39.7137181,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Mon State",
            state_code="15",
            latitude=16.3003133,
            longitude=97.6982272,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Myanmar")][0]),
        ))
        list_of_states.append(State(
            name="Monagas",
            state_code="N",
            latitude=9.3241652,
            longitude=-63.0147578,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Monaghan",
            state_code="MN",
            latitude=54.2492046,
            longitude=-6.9683132,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Monaragala District",
            state_code="82",
            latitude=6.8727781,
            longitude=81.3506832,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Monastir",
            state_code="52",
            latitude=35.7642515,
            longitude=10.8112885,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Mondulkiri",
            state_code="11",
            latitude=12.7879427,
            longitude=107.1011931,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cambodia")][0]),
        ))
        list_of_states.append(State(
            name="Moneghetti",
            state_code="MG",
            latitude=43.7364927,
            longitude=7.4153383,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Monaco")][0]),
        ))
        list_of_states.append(State(
            name="Mongala",
            state_code="MO",
            latitude=1.9962324,
            longitude=21.4752851,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Democratic Republic of the Congo")][0]),
        ))
        list_of_states.append(State(
            name="Mongar District",
            state_code="42",
            latitude=27.2617059,
            longitude=91.2891036,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Monmouthshire",
            state_code="MON",
            latitude=51.81161,
            longitude=-2.7163417,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Mono Department",
            state_code="MO",
            latitude=37.9218608,
            longitude=-118.9528645,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Monseñor Nouel Province",
            state_code="28",
            latitude=18.9215234,
            longitude=-70.3836815,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Mont Buxton",
            state_code="17",
            latitude=-4.6166667,
            longitude=55.4457768,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Mont Fleuri",
            state_code="18",
            latitude=-4.6356543,
            longitude=55.4554688,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Seychelles")][0]),
        ))
        list_of_states.append(State(
            name="Montagnes District",
            state_code="MG",
            latitude=7.3762373,
            longitude=-7.4381355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Montana",
            state_code="MT",
            latitude=46.8796822,
            longitude=-110.3625658,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United States")][0]),
        ))
        list_of_states.append(State(
            name="Montana Province",
            state_code="12",
            latitude=43.4085148,
            longitude=23.2257589,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bulgaria")][0]),
        ))
        list_of_states.append(State(
            name="Monte Cristi Province",
            state_code="15",
            latitude=19.7396899,
            longitude=-71.4433984,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Monte Plata Province",
            state_code="29",
            latitude=18.8080878,
            longitude=-69.7869146,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Dominican Republic")][0]),
        ))
        list_of_states.append(State(
            name="Montegiardino",
            state_code="08",
            latitude=43.9052999,
            longitude=12.4810542,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "San Marino")][0]),
        ))
        list_of_states.append(State(
            name="Montevideo",
            state_code="MO",
            latitude=-34.8181587,
            longitude=-56.2138256,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uruguay")][0]),
        ))
        list_of_states.append(State(
            name="Montserrado County",
            state_code="MO",
            latitude=6.5525815,
            longitude=-10.5296115,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Liberia")][0]),
        ))
        list_of_states.append(State(
            name="Monufia",
            state_code="MNF",
            latitude=30.5972455,
            longitude=30.9876321,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Egypt")][0]),
        ))
        list_of_states.append(State(
            name="Monza and Brianza",
            state_code="MB",
            latitude=45.623599,
            longitude=9.2588015,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Italy")][0]),
        ))
        list_of_states.append(State(
            name="Mopti Region",
            state_code="5",
            latitude=14.6338039,
            longitude=-3.4195527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mali")][0]),
        ))
        list_of_states.append(State(
            name="Moquegua",
            state_code="MOQ",
            latitude=-17.1927361,
            longitude=-70.9328138,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Peru")][0]),
        ))
        list_of_states.append(State(
            name="Moravče Municipality",
            state_code="077",
            latitude=46.1362781,
            longitude=14.746001,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Moravica District",
            state_code="17",
            latitude=43.84147,
            longitude=20.2904987,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Moravske Toplice Municipality",
            state_code="078",
            latitude=46.6856932,
            longitude=16.2224582,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Moravskoslezský kraj",
            state_code="80",
            latitude=49.7305327,
            longitude=18.2332637,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Moray",
            state_code="MRY",
            latitude=57.6498476,
            longitude=-3.3168039,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Morazán Department",
            state_code="MO",
            latitude=13.7682,
            longitude=-88.1291387,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "El Salvador")][0]),
        ))
        list_of_states.append(State(
            name="Morbihan",
            state_code="56",
            latitude=47.7439518,
            longitude=-3.4455524,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Morelos",
            state_code="MOR",
            latitude=18.6813049,
            longitude=-99.1013498,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mexico")][0]),
        ))
        list_of_states.append(State(
            name="Morobe Province",
            state_code="MPL",
            latitude=-6.8013737,
            longitude=146.561647,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Papua New Guinea")][0]),
        ))
        list_of_states.append(State(
            name="Morogoro",
            state_code="16",
            latitude=-8.8137173,
            longitude=36.954107,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Morona-Santiago",
            state_code="S",
            latitude=-2.3051062,
            longitude=-78.1146866,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Moroto District",
            state_code="308",
            latitude=2.6168545,
            longitude=34.597132,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Morovis",
            state_code="101",
            latitude=18.325785,
            longitude=-66.4065592,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Moscow",
            state_code="MOW",
            latitude=55.755826,
            longitude=37.6172999,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Moscow Oblast",
            state_code="MOS",
            latitude=55.340396,
            longitude=38.2917651,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Moselle",
            state_code="57",
            latitude=49.0204566,
            longitude=6.2055322,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "France")][0]),
        ))
        list_of_states.append(State(
            name="Most",
            state_code="425",
            latitude=37.1554083,
            longitude=-94.2948884,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Mosta",
            state_code="32",
            latitude=35.9141504,
            longitude=14.4228427,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Mostaganem",
            state_code="27",
            latitude=35.9583054,
            longitude=0.3371889,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Mosteiros",
            state_code="MO",
            latitude=37.8904348,
            longitude=-25.8207556,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cape Verde")][0]),
        ))
        list_of_states.append(State(
            name="Mouhoun",
            state_code="MOU",
            latitude=12.1432381,
            longitude=-3.3388917,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Moulay Yacoub",
            state_code="MOU",
            latitude=34.0874479,
            longitude=-5.1784019,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Moulvibazar District",
            state_code="38",
            latitude=24.3095344,
            longitude=91.7314903,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Mount Lebanon",
            state_code="JL",
            latitude=33.8100858,
            longitude=35.5973139,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lebanon")][0]),
        ))
        list_of_states.append(State(
            name="Mountain Province",
            state_code="MOU",
            latitude=40.7075437,
            longitude=-73.9501033,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Moxico Province",
            state_code="MOX",
            latitude=-13.4293579,
            longitude=20.3308814,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Moyen-Cavally",
            state_code="19",
            latitude=6.5208793,
            longitude=-7.6114217,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Moyen-Chari",
            state_code="MC",
            latitude=9.0639998,
            longitude=18.4276047,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="Moyen-Comoé",
            state_code="05",
            latitude=6.6514917,
            longitude=-3.5003454,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Moyen-Ogooué Province",
            state_code="3",
            latitude=-0.442784,
            longitude=10.439656,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Gabon")][0]),
        ))
        list_of_states.append(State(
            name="Moyle District Council",
            state_code="MYL",
            latitude=55.2047327,
            longitude=-6.253174,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "United Kingdom")][0]),
        ))
        list_of_states.append(State(
            name="Moyo District",
            state_code="309",
            latitude=3.5696464,
            longitude=31.6739371,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Mozirje Municipality",
            state_code="079",
            latitude=46.339435,
            longitude=14.9602413,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Mpigi District",
            state_code="106",
            latitude=0.2273528,
            longitude=32.3249236,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Mpumalanga",
            state_code="MP",
            latitude=-25.565336,
            longitude=30.5279096,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "South Africa")][0]),
        ))
        list_of_states.append(State(
            name="Mqabba",
            state_code="33",
            latitude=35.8444143,
            longitude=14.4694186,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Msida",
            state_code="34",
            latitude=35.8956388,
            longitude=14.4868883,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Mtarfa",
            state_code="35",
            latitude=35.8895125,
            longitude=14.3951953,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Mtskheta-Mtianeti",
            state_code="MM",
            latitude=42.1682185,
            longitude=44.6506058,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Georgia")][0]),
        ))
        list_of_states.append(State(
            name="Mtwara",
            state_code="17",
            latitude=-10.3398455,
            longitude=40.1657466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Mubarak Al-Kabeer",
            state_code="MU",
            latitude=29.21224,
            longitude=48.0605108,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kuwait")][0]),
        ))
        list_of_states.append(State(
            name="Mubende District",
            state_code="107",
            latitude=0.5772758,
            longitude=31.5370003,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Muchinga Province",
            state_code="10",
            latitude=-15.382193,
            longitude=28.26158,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Zambia")][0]),
        ))
        list_of_states.append(State(
            name="Mudug",
            state_code="MU",
            latitude=6.5656726,
            longitude=47.7637565,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Somalia")][0]),
        ))
        list_of_states.append(State(
            name="Muğla",
            state_code="48",
            latitude=37.1835819,
            longitude=28.4863963,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Muharraq",
            state_code="15",
            latitude=26.2685653,
            longitude=50.6482517,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bahrain")][0]),
        ))
        list_of_states.append(State(
            name="Mukdahan",
            state_code="49",
            latitude=16.5435914,
            longitude=104.7024121,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Mukono District",
            state_code="108",
            latitude=0.2835476,
            longitude=32.7633036,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Mulanje District",
            state_code="MU",
            latitude=-15.9346434,
            longitude=35.5220012,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Mullaitivu District",
            state_code="45",
            latitude=9.2675388,
            longitude=80.8128254,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Sri Lanka")][0]),
        ))
        list_of_states.append(State(
            name="Municipality of Apače",
            state_code="195",
            latitude=46.6974679,
            longitude=15.9102534,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Municipality of Cirkulane",
            state_code="196",
            latitude=46.3298322,
            longitude=15.9980666,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Municipality of Ilirska Bistrica",
            state_code="038",
            latitude=45.5791323,
            longitude=14.2809729,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Municipality of Krško",
            state_code="054",
            latitude=45.9589609,
            longitude=15.4923555,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Municipality of Škofljica",
            state_code="123",
            latitude=45.9840962,
            longitude=14.5746626,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Munshiganj District",
            state_code="35",
            latitude=23.4980931,
            longitude=90.4126621,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Munster",
            state_code="M",
            latitude=51.9471197,
            longitude=7.584532,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ireland")][0]),
        ))
        list_of_states.append(State(
            name="Munxar",
            state_code="36",
            latitude=36.0288058,
            longitude=14.2250605,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Muramvya Province",
            state_code="MU",
            latitude=-3.2898398,
            longitude=29.6499162,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Murang'a",
            state_code="29",
            latitude=-0.7839281,
            longitude=37.0400339,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Murcia",
            state_code="MU",
            latitude=38.1398141,
            longitude=-1.366216,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Mureș County",
            state_code="MS",
            latitude=46.5569904,
            longitude=24.6723215,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Romania")][0]),
        ))
        list_of_states.append(State(
            name="Murmansk Oblast",
            state_code="MUR",
            latitude=67.8442674,
            longitude=35.0884102,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Russia")][0]),
        ))
        list_of_states.append(State(
            name="Murqub",
            state_code="MB",
            latitude=32.4599677,
            longitude=14.1001326,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Murska Sobota City Municipality",
            state_code="080",
            latitude=46.6432147,
            longitude=16.1515754,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Murzuq District",
            state_code="MQ",
            latitude=25.9182262,
            longitude=13.9260001,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Muş",
            state_code="49",
            latitude=38.9461888,
            longitude=41.7538931,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Musandam",
            state_code="MU",
            latitude=26.1986144,
            longitude=56.2460949,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Oman")][0]),
        ))
        list_of_states.append(State(
            name="Muscat",
            state_code="MA",
            latitude=23.5880307,
            longitude=58.3828717,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Oman")][0]),
        ))
        list_of_states.append(State(
            name="Muta Municipality",
            state_code="081",
            latitude=46.6097366,
            longitude=15.1629995,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Muyinga Province",
            state_code="MY",
            latitude=-2.7793511,
            longitude=30.2974199,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Mwanza",
            state_code="18",
            latitude=-2.4671197,
            longitude=32.8986812,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Mwanza District",
            state_code="MW",
            latitude=-2.4671197,
            longitude=32.8986812,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Mwaro Province",
            state_code="MW",
            latitude=-3.5025918,
            longitude=29.6499162,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burundi")][0]),
        ))
        list_of_states.append(State(
            name="Mykolaivska oblast",
            state_code="48",
            latitude=46.975033,
            longitude=31.9945829,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Mymensingh District",
            state_code="34",
            latitude=24.7538575,
            longitude=90.4072919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Mymensingh Division",
            state_code="H",
            latitude=24.71362,
            longitude=90.4502368,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Mzimba District",
            state_code="MZ",
            latitude=-11.7475452,
            longitude=33.5280072,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Møre og Romsdal",
            state_code="15",
            latitude=62.8406833,
            longitude=7.007143,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Norway")][0]),
        ))
        list_of_states.append(State(
            name="M’diq-Fnideq",
            state_code="MDF",
            latitude=35.7733019,
            longitude=-5.51433,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="N'Djamena",
            state_code="ND",
            latitude=12.1348457,
            longitude=15.0557415,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Chad")][0]),
        ))
        list_of_states.append(State(
            name="N'zi-Comoé",
            state_code="11",
            latitude=7.2456749,
            longitude=-4.2333355,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Naama",
            state_code="45",
            latitude=33.2667317,
            longitude=-0.3128659,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Algeria")][0]),
        ))
        list_of_states.append(State(
            name="Nabatieh",
            state_code="NA",
            latitude=33.3771693,
            longitude=35.4838293,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lebanon")][0]),
        ))
        list_of_states.append(State(
            name="Nabeul",
            state_code="21",
            latitude=36.4524591,
            longitude=10.6803222,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Nablus",
            state_code="NBS",
            latitude=None,
            longitude=None,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Palestinian Territory Occupied")][0]),
        ))
        list_of_states.append(State(
            name="Náchod",
            state_code="523",
            latitude=50.4145722,
            longitude=16.1656347,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Nador",
            state_code="NAD",
            latitude=34.9171926,
            longitude=-2.8577105,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Nadroga-Navosa",
            state_code="08",
            latitude=-17.9865278,
            longitude=177.658113,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Nadur",
            state_code="37",
            latitude=36.0447019,
            longitude=14.2919273,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Nagaland",
            state_code="NL",
            latitude=26.1584354,
            longitude=94.5624426,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "India")][0]),
        ))
        list_of_states.append(State(
            name="Nagano Prefecture",
            state_code="20",
            latitude=36.1543941,
            longitude=137.9218204,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Nagasaki Prefecture",
            state_code="42",
            latitude=33.2488525,
            longitude=129.6930912,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Naguabo",
            state_code="103",
            latitude=18.2116247,
            longitude=-65.7348841,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        list_of_states.append(State(
            name="Nagykanizsa",
            state_code="NK",
            latitude=46.4590218,
            longitude=16.9896796,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Nahouri Province",
            state_code="NAO",
            latitude=11.2502267,
            longitude=-1.135302,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Nairobi City",
            state_code="30",
            latitude=-1.2920659,
            longitude=36.8219462,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Naitasiri",
            state_code="09",
            latitude=-17.8975754,
            longitude=178.2071598,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Najaf",
            state_code="NA",
            latitude=31.3517486,
            longitude=44.0960311,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iraq")][0]),
        ))
        list_of_states.append(State(
            name="Najran",
            state_code="10",
            latitude=18.3514664,
            longitude=45.6007108,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Saudi Arabia")][0]),
        ))
        list_of_states.append(State(
            name="Nakapiripirit District",
            state_code="311",
            latitude=1.9606173,
            longitude=34.597132,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Nakaseke District",
            state_code="116",
            latitude=1.2230848,
            longitude=32.0837445,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Nakasongola District",
            state_code="109",
            latitude=1.3489721,
            longitude=32.4467238,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Nakhchivan Autonomous Republic",
            state_code="NX",
            latitude=39.3256814,
            longitude=45.4912648,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Nakhon Nayok",
            state_code="26",
            latitude=14.2069466,
            longitude=101.2130511,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Nakhon Pathom",
            state_code="73",
            latitude=13.8140293,
            longitude=100.0372929,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Nakhon Phanom",
            state_code="48",
            latitude=17.392039,
            longitude=104.7695508,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Nakhon Ratchasima",
            state_code="30",
            latitude=14.9738493,
            longitude=102.083652,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Nakhon Sawan",
            state_code="60",
            latitude=15.6987382,
            longitude=100.11996,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Nakhon Si Thammarat",
            state_code="80",
            latitude=8.4324831,
            longitude=99.9599033,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Naklo Municipality",
            state_code="082",
            latitude=46.2718663,
            longitude=14.3156932,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Nakuru",
            state_code="31",
            latitude=-0.3030988,
            longitude=36.080026,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Nalut District",
            state_code="NL",
            latitude=31.8742348,
            longitude=10.9750484,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Nam Định",
            state_code="67",
            latitude=20.4388225,
            longitude=106.1621053,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Namangan Region",
            state_code="NG",
            latitude=41.0510037,
            longitude=71.097317,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uzbekistan")][0]),
        ))
        list_of_states.append(State(
            name="Namayingo District",
            state_code="230",
            latitude=-0.2803575,
            longitude=33.7517723,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Namentenga Province",
            state_code="NAM",
            latitude=13.0812584,
            longitude=-0.5257823,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Namisindwa District",
            state_code="234",
            latitude=0.907101,
            longitude=34.3574037,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Namosi",
            state_code="10",
            latitude=-18.0864176,
            longitude=178.1291387,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Fiji Islands")][0]),
        ))
        list_of_states.append(State(
            name="Nampula Province",
            state_code="N",
            latitude=-14.7604931,
            longitude=39.3206241,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Namur",
            state_code="WNA",
            latitude=50.4673883,
            longitude=4.8719854,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Belgium")][0]),
        ))
        list_of_states.append(State(
            name="Namutumba District",
            state_code="224",
            latitude=0.849261,
            longitude=33.6623301,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Nan",
            state_code="55",
            latitude=45.522208,
            longitude=-122.9863281,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Thailand")][0]),
        ))
        list_of_states.append(State(
            name="Nana-Grébizi Economic Prefecture",
            state_code="KB",
            latitude=7.1848607,
            longitude=19.3783206,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Nana-Mambéré Prefecture",
            state_code="NM",
            latitude=5.6932135,
            longitude=15.2194808,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Central African Republic")][0]),
        ))
        list_of_states.append(State(
            name="Nandi",
            state_code="32",
            latitude=0.1835867,
            longitude=35.1268781,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kenya")][0]),
        ))
        list_of_states.append(State(
            name="Nangarhar",
            state_code="NAN",
            latitude=34.1718313,
            longitude=70.6216794,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Afghanistan")][0]),
        ))
        list_of_states.append(State(
            name="Nantou",
            state_code="NAN",
            latitude=23.9609981,
            longitude=120.9718638,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Taiwan")][0]),
        ))
        list_of_states.append(State(
            name="Nanumanga",
            state_code="NMG",
            latitude=-6.2858019,
            longitude=176.319928,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tuvalu")][0]),
        ))
        list_of_states.append(State(
            name="Nanumea",
            state_code="NMA",
            latitude=-5.6881617,
            longitude=176.1370148,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tuvalu")][0]),
        ))
        list_of_states.append(State(
            name="Naogaon District",
            state_code="48",
            latitude=24.9131597,
            longitude=88.7530952,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Napak District",
            state_code="327",
            latitude=2.3629945,
            longitude=34.2421597,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Napo",
            state_code="N",
            latitude=-0.9955964,
            longitude=-77.8129684,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Nara Prefecture",
            state_code="29",
            latitude=34.2975528,
            longitude=135.8279734,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Japan")][0]),
        ))
        list_of_states.append(State(
            name="Narail District",
            state_code="43",
            latitude=23.1162929,
            longitude=89.5840404,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bangladesh")][0]),
        ))
        list_of_states.append(State(
            name="Naranjito",
            state_code="105",
            latitude=18.3007861,
            longitude=-66.2448904,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Puerto Rico")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (12/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
