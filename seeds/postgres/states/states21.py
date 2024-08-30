"""
States Seed #21

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
            name="Zaghouan",
            state_code="22",
            latitude=36.4091188,
            longitude=10.1423172,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tunisia")][0]),
        ))
        list_of_states.append(State(
            name="Zagora",
            state_code="ZAG",
            latitude=30.5786093,
            longitude=-5.8987139,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Morocco")][0]),
        ))
        list_of_states.append(State(
            name="Zagorje ob Savi Municipality",
            state_code="142",
            latitude=46.1345202,
            longitude=14.9964384,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Zagreb",
            state_code="01",
            latitude=45.8706612,
            longitude=16.395491,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Zagreb",
            state_code="21",
            latitude=45.8150108,
            longitude=15.9819189,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Croatia")][0]),
        ))
        list_of_states.append(State(
            name="Zaire Province",
            state_code="ZAI",
            latitude=-6.5733458,
            longitude=13.1740348,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Angola")][0]),
        ))
        list_of_states.append(State(
            name="Zajas Municipality",
            state_code="31",
            latitude=41.6030328,
            longitude=20.8791343,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Zaječar District",
            state_code="15",
            latitude=43.9015048,
            longitude=22.2738011,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Zakarpatska Oblast",
            state_code="21",
            latitude=48.6208,
            longitude=22.287883,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Zala County",
            state_code="ZA",
            latitude=46.7384404,
            longitude=16.9152252,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Zalaegerszeg",
            state_code="ZE",
            latitude=46.8416936,
            longitude=16.8416322,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Hungary")][0]),
        ))
        list_of_states.append(State(
            name="Žalec Municipality",
            state_code="190",
            latitude=46.2519712,
            longitude=15.1650072,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Zambales",
            state_code="ZMB",
            latitude=15.5081766,
            longitude=119.9697808,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Zambezi Region",
            state_code="CA",
            latitude=-17.8193419,
            longitude=23.9536466,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Namibia")][0]),
        ))
        list_of_states.append(State(
            name="Zambezia Province",
            state_code="Q",
            latitude=-16.5638987,
            longitude=36.6093926,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mozambique")][0]),
        ))
        list_of_states.append(State(
            name="Zamboanga del Norte",
            state_code="ZAN",
            latitude=8.3886282,
            longitude=123.1688883,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Zamboanga del Sur",
            state_code="ZAS",
            latitude=7.8383054,
            longitude=123.2966657,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Zamboanga Peninsula",
            state_code="09",
            latitude=8.154077,
            longitude=123.258793,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Zamboanga Sibugay",
            state_code="ZSI",
            latitude=7.5225247,
            longitude=122.3107517,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Philippines")][0]),
        ))
        list_of_states.append(State(
            name="Zamfara",
            state_code="ZA",
            latitude=12.1221805,
            longitude=6.2235819,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Nigeria")][0]),
        ))
        list_of_states.append(State(
            name="Zamora",
            state_code="ZA",
            latitude=41.6095744,
            longitude=-5.8987139,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Zamora Chinchipe",
            state_code="Z",
            latitude=-4.0655892,
            longitude=-78.9503525,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ecuador")][0]),
        ))
        list_of_states.append(State(
            name="Zangilan District",
            state_code="ZAN",
            latitude=39.0856899,
            longitude=46.6524728,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Zanjan",
            state_code="19",
            latitude=36.5018185,
            longitude=48.3988186,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Iran")][0]),
        ))
        list_of_states.append(State(
            name="Zanzan Region",
            state_code="ZZ",
            latitude=8.8207904,
            longitude=-3.4195527,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Cote D'Ivoire (Ivory Coast)")][0]),
        ))
        list_of_states.append(State(
            name="Zanzibar North",
            state_code="07",
            latitude=-5.9395093,
            longitude=39.2791011,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Zanzibar South",
            state_code="11",
            latitude=-6.2642851,
            longitude=39.4450281,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Zanzibar West",
            state_code="15",
            latitude=-6.2298136,
            longitude=39.2583293,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tanzania")][0]),
        ))
        list_of_states.append(State(
            name="Zaporizka oblast",
            state_code="23",
            latitude=47.8388,
            longitude=35.139567,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Zaqatala District",
            state_code="ZAQ",
            latitude=41.5906889,
            longitude=46.7240373,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Zaragoza",
            state_code="Z",
            latitude=41.6517501,
            longitude=-0.9300002,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Spain")][0]),
        ))
        list_of_states.append(State(
            name="Zarasai District Municipality",
            state_code="60",
            latitude=55.7309609,
            longitude=26.245295,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Lithuania")][0]),
        ))
        list_of_states.append(State(
            name="Zardab District",
            state_code="ZAR",
            latitude=40.2148114,
            longitude=47.714944,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Azerbaijan")][0]),
        ))
        list_of_states.append(State(
            name="Zarqa",
            state_code="AZ",
            latitude=32.0608505,
            longitude=36.0942121,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Jordan")][0]),
        ))
        list_of_states.append(State(
            name="Zavkhan Province",
            state_code="057",
            latitude=48.2388147,
            longitude=96.0703019,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Mongolia")][0]),
        ))
        list_of_states.append(State(
            name="Zavrč Municipality",
            state_code="143",
            latitude=46.35713,
            longitude=16.0477747,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Zawiya District",
            state_code="ZA",
            latitude=32.7630282,
            longitude=12.7364962,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Libya")][0]),
        ))
        list_of_states.append(State(
            name="Žďár nad Sázavou",
            state_code="635",
            latitude=49.5643012,
            longitude=15.939103,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Żebbuġ Gozo",
            state_code="65",
            latitude=36.0716403,
            longitude=14.245408,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Żebbuġ Malta",
            state_code="66",
            latitude=35.8764648,
            longitude=14.439084,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Zeeland",
            state_code="ZE",
            latitude=51.4940309,
            longitude=3.8496815,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Netherlands")][0]),
        ))
        list_of_states.append(State(
            name="Żejtun",
            state_code="67",
            latitude=35.8548714,
            longitude=14.5363969,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Zelenikovo Municipality",
            state_code="32",
            latitude=41.8733812,
            longitude=21.602725,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Železniki Municipality",
            state_code="146",
            latitude=46.2256377,
            longitude=14.1693617,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Želino Municipality",
            state_code="30",
            latitude=41.9006531,
            longitude=21.1175767,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Zenica-Doboj Canton",
            state_code="04",
            latitude=44.2127109,
            longitude=18.1604625,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bosnia and Herzegovina")][0]),
        ))
        list_of_states.append(State(
            name="Žetale Municipality",
            state_code="191",
            latitude=46.2742833,
            longitude=15.7913359,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Zhejiang",
            state_code="ZJ",
            latitude=29.1416432,
            longitude=119.7889248,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "China")][0]),
        ))
        list_of_states.append(State(
            name="Zhemgang District",
            state_code="34",
            latitude=27.076975,
            longitude=90.8294002,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Bhutan")][0]),
        ))
        list_of_states.append(State(
            name="Zhytomyrska oblast",
            state_code="18",
            latitude=50.25465,
            longitude=28.6586669,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Ukraine")][0]),
        ))
        list_of_states.append(State(
            name="Ziguinchor",
            state_code="ZG",
            latitude=12.5641479,
            longitude=-16.2639825,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Senegal")][0]),
        ))
        list_of_states.append(State(
            name="Žilina Region",
            state_code="ZI",
            latitude=49.2031435,
            longitude=19.3645733,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovakia")][0]),
        ))
        list_of_states.append(State(
            name="Zilupe Municipality",
            state_code="110",
            latitude=56.3018985,
            longitude=28.133959,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Latvia")][0]),
        ))
        list_of_states.append(State(
            name="Zinder Region",
            state_code="7",
            latitude=15.1718881,
            longitude=10.2600125,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Niger")][0]),
        ))
        list_of_states.append(State(
            name="Žiri Municipality",
            state_code="147",
            latitude=46.0472499,
            longitude=14.1098451,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Ziro Province",
            state_code="ZIR",
            latitude=11.6094995,
            longitude=-1.9099238,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Žirovnica Municipality",
            state_code="192",
            latitude=46.3954403,
            longitude=14.1539632,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Zlatibor District",
            state_code="16",
            latitude=43.645417,
            longitude=19.7101455,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Serbia")][0]),
        ))
        list_of_states.append(State(
            name="Zlín",
            state_code="724",
            latitude=49.1696052,
            longitude=17.802522,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Zlínský kraj",
            state_code="72",
            latitude=49.2162296,
            longitude=17.7720353,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Znojmo",
            state_code="647",
            latitude=48.9272327,
            longitude=16.1037808,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Czech Republic")][0]),
        ))
        list_of_states.append(State(
            name="Zomba District",
            state_code="ZO",
            latitude=-15.3765857,
            longitude=35.3356518,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malawi")][0]),
        ))
        list_of_states.append(State(
            name="Zombo District",
            state_code="330",
            latitude=2.5544293,
            longitude=30.9417368,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Uganda")][0]),
        ))
        list_of_states.append(State(
            name="Zondoma Province",
            state_code="ZON",
            latitude=13.1165926,
            longitude=-2.4208713,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Zonguldak",
            state_code="67",
            latitude=41.3124917,
            longitude=31.8598251,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Turkey")][0]),
        ))
        list_of_states.append(State(
            name="Zou Department",
            state_code="ZO",
            latitude=7.3469268,
            longitude=2.0665197,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Benin")][0]),
        ))
        list_of_states.append(State(
            name="Zoundwéogo Province",
            state_code="ZOU",
            latitude=11.6141174,
            longitude=-0.9820668,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Burkina Faso")][0]),
        ))
        list_of_states.append(State(
            name="Zreče Municipality",
            state_code="144",
            latitude=46.4177786,
            longitude=15.3709431,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Zrnovci Municipality",
            state_code="33",
            latitude=41.8228221,
            longitude=22.4172256,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "North Macedonia")][0]),
        ))
        list_of_states.append(State(
            name="Zug",
            state_code="ZG",
            latitude=47.1661505,
            longitude=8.5154749,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Zulia",
            state_code="V",
            latitude=10.2910237,
            longitude=-72.1416132,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Venezuela")][0]),
        ))
        list_of_states.append(State(
            name="Zürich",
            state_code="ZH",
            latitude=47.359536,
            longitude=8.6356452,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Switzerland")][0]),
        ))
        list_of_states.append(State(
            name="Żurrieq",
            state_code="68",
            latitude=35.8216306,
            longitude=14.4810648,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Žužemberk Municipality",
            state_code="193",
            latitude=45.820035,
            longitude=14.9535919,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Slovenia")][0]),
        ))
        list_of_states.append(State(
            name="Đà Nẵng",
            state_code="DN",
            latitude=16.0544068,
            longitude=108.2021667,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Đắk Lắk",
            state_code="33",
            latitude=12.7100116,
            longitude=108.2377519,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Đắk Nông",
            state_code="72",
            latitude=12.2646476,
            longitude=107.609806,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Đakovica District (Gjakove)",
            state_code="XDG",
            latitude=42.4375756,
            longitude=20.3785438,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Kosovo")][0]),
        ))
        list_of_states.append(State(
            name="Điện Biên",
            state_code="71",
            latitude=21.8042309,
            longitude=103.1076525,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Đồng Nai",
            state_code="39",
            latitude=11.0686305,
            longitude=107.1675976,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Đồng Tháp",
            state_code="45",
            latitude=10.4937989,
            longitude=105.6881788,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Vietnam")][0]),
        ))
        list_of_states.append(State(
            name="Ħamrun",
            state_code="18",
            latitude=35.8861237,
            longitude=14.4883442,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Malta")][0]),
        ))
        list_of_states.append(State(
            name="Łódź Voivodeship",
            state_code="LD",
            latitude=51.4634771,
            longitude=19.1726974,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Poland")][0]),
        ))
        list_of_states.append(State(
            name="ʻEua",
            state_code="01",
            latitude=37.09024,
            longitude=-95.712891,
            country_id=([i.id for i in country_list
                         if i.name == (
                          "Tonga")][0]),
        ))
        db.session.add_all(list_of_states)
        db.session.commit()
        print(State.__tablename__ + " seeded successfully! (21/21)")
    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
