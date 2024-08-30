"""
Proxy Types Int Enum
"""
from enum import IntEnum


class ProxyType(IntEnum):
    """
    Enum representing the different types of proxy that can be added.

    Attributes:
        DC_HTTPS (UInt8): General Datacenter Proxy
        DC_HTTP (UInt8): General Datacenter Proxy
        DC_SOCKS4 (UInt8): General Datacenter Proxy
        DC_SOCKS5 (UInt8): General Datacenter Proxy

        FREE_DC_HTTPS (UInt8): Free Datacenter Proxy
        FREE_DC_HTTP (UInt8): Free Datacenter Proxy
        FREE_DC_SOCKS4 (UInt8): Free Datacenter Proxy
        FREE_DC_SOCKS5 (UInt8): Free Datacenter Proxy

        OWN_DC_HTTPS (UInt8): Personal Datacenter Proxy
        OWN_DC_HTTP (UInt8): Personal Datacenter Proxy
        OWN_DC_SOCKS4 (UInt8): Personal Datacenter Proxy
        OWN_DC_SOCKS5 (UInt8): Personal Datacenter Proxy

        PREMIUM_DC_HTTPS (UInt8): Premium Datacenter Proxy
        PREMIUM_DC_HTTP (UInt8): Premium Datacenter Proxy
        PREMIUM_DC_SOCKS4 (UInt8): Premium Datacenter Proxy
        PREMIUM_DC_SOCKS5 (UInt8): Premium Datacenter Proxy

        PRIVATE_DC_HTTPS (UInt8): Private Datacenter Proxy
        PRIVATE_DC_HTTP (UInt8): Private Datacenter Proxy
        PRIVATE_DC_SOCKS4 (UInt8): Private Datacenter Proxy
        PRIVATE_DC_SOCKS5 (UInt8): Private Datacenter Proxy

        ROTATING_DC_HTTPS (UInt8): Rotating Datacenter Proxy
        ROTATING_DC_HTTP (UInt8): Rotating Datacenter Proxy
        ROTATING_DC_SOCKS4 (UInt8): Rotating Datacenter Proxy
        ROTATING_DC_SOCKS5 (UInt8): Rotating Datacenter Proxy

        DEDICATED_DC_HTTPS (UInt8): Dedicated Datacenter Proxy
        DEDICATED_DC_HTTP (UInt8): Dedicated Datacenter Proxy
        DEDICATED_DC_SOCKS4 (UInt8): Dedicated Datacenter Proxy
        DEDICATED_DC_SOCKS5 (UInt8): Dedicated Datacenter Proxy

        PREMIUM_STATIC_RES_HTTPS (UInt8): Premium Static Residential Proxy
        PREMIUM_STATIC_RES_HTTP (UInt8): Premium Static Residential Proxy
        PREMIUM_STATIC_RES_SOCKS4 (UInt8): Premium Static Residential Proxy
        PREMIUM_STATIC_RES_SOCKS5 (UInt8): Premium Static Residential Proxy

        DEDICATED_RES_HTTPS (UInt8): Dedicated Residential Proxy
        DEDICATED_RES_HTTP (UInt8): Dedicated Residential Proxy
        DEDICATED_RES_SOCKS4 (UInt8): Dedicated Residential Proxy
        DEDICATED_RES_SOCKS5 (UInt8): Dedicated Residential Proxy

        ROTATING_RES_HTTPS (UInt8): Rotating Residential Proxy
        ROTATING_RES_HTTP (UInt8): Rotating Residential Proxy
        ROTATING_RES_SOCKS4 (UInt8): Rotating Residential Proxy
        ROTATING_RES_SOCKS5 (UInt8): Rotating Residential Proxy

        PRIVATE_RES_HTTPS (UInt8): Private Residential Proxy
        PRIVATE_RES_HTTP (UInt8): Private Residential Proxy
        PRIVATE_RES_SOCKS4 (UInt8): Private Residential Proxy
        PRIVATE_RES_SOCKS5 (UInt8): Private Residential Proxy

        FREE_RES_HTTPS (UInt8): Free Residential Proxy
        FREE_RES_HTTP (UInt8): Free Residential Proxy
        FREE_RES_SOCKS4 (UInt8): Free Residential Proxy
        FREE_RES_SOCKS5 (UInt8): Free Residential Proxy

        OWN_RES_HTTPS (UInt8): Personal Residential Proxy
        OWN_RES_HTTP (UInt8): Personal Residential Proxy
        OWN_RES_SOCKS4 (UInt8): Personal Residential Proxy
        OWN_RES_SOCKS5 (UInt8): Personal Residential Proxy

        RES_HTTPS (UInt8): General Residential Proxy
        RES_HTTP (UInt8): General Residential Proxy
        RES_SOCKS4 (UInt8): General Residential Proxy
        RES_SOCKS5 (UInt8): General Residential Proxy

        SCRAPED_UNTRUSTED_HTTPS (UInt8): Scraped, Untrusted General Type Proxy
        SCRAPED_UNTRUSTED_HTTP (UInt8): Scraped, Untrusted General Type Proxy
        SCRAPED_UNTRUSTED_SOCKS4 (UInt8): Scraped, Untrusted General Type Proxy
        SCRAPED_UNTRUSTED_SOCKS5 (UInt8): Scraped, Untrusted General Type Proxy

        SCRAPED_UNTRUSTED_TYPE_1_HTTPS (UInt8): Scraped, Untrusted Type 1 Proxy
        SCRAPED_UNTRUSTED_TYPE_1_HTTP (UInt8): Scraped, Untrusted Type 1 Proxy
        SCRAPED_UNTRUSTED_TYPE_1_SOCKS4 (UInt8): Scraped, Untrusted Type 1 Proxy
        SCRAPED_UNTRUSTED_TYPE_1_SOCKS5 (UInt8): Scraped, Untrusted Type 1

        SCRAPED_UNTRUSTED_TYPE_2_HTTPS (UInt8): Scraped, Untrusted Type 2 Proxy
        SCRAPED_UNTRUSTED_TYPE_2_HTTP (UInt8): Scraped, Untrusted Type 2 Proxy
        SCRAPED_UNTRUSTED_TYPE_2_SOCKS4 (UInt8): Scraped, Untrusted Type 2 Proxy
        SCRAPED_UNTRUSTED_TYPE_2_SOCKS5 (UInt8): Scraped, Untrusted Type 2

        SCRAPED_UNTRUSTED_TYPE_3_HTTPS (UInt8): Scraped, Untrusted Type 3 Proxy
        SCRAPED_UNTRUSTED_TYPE_3_HTTP (UInt8): Scraped, Untrusted Type 3 Proxy
        SCRAPED_UNTRUSTED_TYPE_3_SOCKS4 (UInt8): Scraped, Untrusted Type 3 Proxy
        SCRAPED_UNTRUSTED_TYPE_3_SOCKS5 (UInt8): Scraped, Untrusted Type 3 Proxy

        SCRAPED_UNTRUSTED_TYPE_4_HTTPS (UInt8): Scraped, Untrusted Type 4 Proxy
        SCRAPED_UNTRUSTED_TYPE_4_HTTP (UInt8): Scraped, Untrusted Type 4 Proxy
        SCRAPED_UNTRUSTED_TYPE_4_SOCKS4 (UInt8): Scraped, Untrusted Type 4 Proxy
        SCRAPED_UNTRUSTED_TYPE_4_SOCKS5 (UInt8): Scraped, Untrusted Type 4 Proxy
    """

    DC_HTTPS = 1
    DC_HTTP = 2
    DC_SOCKS4 = 3
    DC_SOCKS5 = 4

    FREE_DC_HTTPS = 5
    FREE_DC_HTTP = 6
    FREE_DC_SOCKS4 = 7
    FREE_DC_SOCKS5 = 8

    OWN_DC_HTTPS = 9
    OWN_DC_HTTP = 10
    OWN_DC_SOCKS4 = 11
    OWN_DC_SOCKS5 = 12

    PREMIUM_DC_HTTPS = 13
    PREMIUM_DC_HTTP = 14
    PREMIUM_DC_SOCKS4 = 15
    PREMIUM_DC_SOCKS5 = 16

    PRIVATE_DC_HTTPS = 17
    PRIVATE_DC_HTTP = 18
    PRIVATE_DC_SOCKS4 = 19
    PRIVATE_DC_SOCKS5 = 20

    ROTATING_DC_HTTPS = 21
    ROTATING_DC_HTTP = 22
    ROTATING_DC_SOCKS4 = 23
    ROTATING_DC_SOCKS5 = 24

    DEDICATED_DC_HTTPS = 25
    DEDICATED_DC_HTTP = 26
    DEDICATED_DC_SOCKS4 = 27
    DEDICATED_DC_SOCKS5 = 28

    PREMIUM_STATIC_RES_HTTPS = 29
    PREMIUM_STATIC_RES_HTTP = 30
    PREMIUM_STATIC_RES_SOCKS4 = 31
    PREMIUM_STATIC_RES_SOCKS5 = 32

    DEDICATED_RES_HTTPS = 33
    DEDICATED_RES_HTTP = 34
    DEDICATED_RES_SOCKS4 = 35
    DEDICATED_RES_SOCKS5 = 36

    ROTATING_RES_HTTPS = 37
    ROTATING_RES_HTTP = 38
    ROTATING_RES_SOCKS4 = 39
    ROTATING_RES_SOCKS5 = 40

    PRIVATE_RES_HTTPS = 41
    PRIVATE_RES_HTTP = 42
    PRIVATE_RES_SOCKS4 = 43
    PRIVATE_RES_SOCKS5 = 44

    FREE_RES_HTTPS = 45
    FREE_RES_HTTP = 46
    FREE_RES_SOCKS4 = 47
    FREE_RES_SOCKS5 = 48

    OWN_RES_HTTPS = 49
    OWN_RES_HTTP = 50
    OWN_RES_SOCKS4 = 51
    OWN_RES_SOCKS5 = 52

    RES_HTTPS = 53
    RES_HTTP = 54
    RES_SOCKS4 = 55
    RES_SOCKS5 = 56

    SCRAPED_UNTRUSTED_HTTPS = 57
    SCRAPED_UNTRUSTED_HTTP = 58
    SCRAPED_UNTRUSTED_SOCKS4 = 59
    SCRAPED_UNTRUSTED_SOCKS5 = 60

    SCRAPED_UNTRUSTED_TYPE_1_HTTPS = 61
    SCRAPED_UNTRUSTED_TYPE_1_HTTP = 62
    SCRAPED_UNTRUSTED_TYPE_1_SOCKS4 = 63
    SCRAPED_UNTRUSTED_TYPE_1_SOCKS5 = 64

    SCRAPED_UNTRUSTED_TYPE_2_HTTPS = 65
    SCRAPED_UNTRUSTED_TYPE_2_HTTP = 66
    SCRAPED_UNTRUSTED_TYPE_2_SOCKS4 = 67
    SCRAPED_UNTRUSTED_TYPE_2_SOCKS5 = 68

    SCRAPED_UNTRUSTED_TYPE_3_HTTPS = 69
    SCRAPED_UNTRUSTED_TYPE_3_HTTP = 70
    SCRAPED_UNTRUSTED_TYPE_3_SOCKS4 = 71
    SCRAPED_UNTRUSTED_TYPE_3_SOCKS5 = 72

    SCRAPED_UNTRUSTED_TYPE_4_HTTPS = 73
    SCRAPED_UNTRUSTED_TYPE_4_HTTP = 74
    SCRAPED_UNTRUSTED_TYPE_4_SOCKS4 = 75
    SCRAPED_UNTRUSTED_TYPE_4_SOCKS5 = 76
