"""
Proxy List
"""

from enums.proxies import ProxyType

CurrentProxyList = [
    {
        'proxy_address': "0.0.0.0:1080",
        'proxy_type': ProxyType.PREMIUM_STATIC_RES_SOCKS5,
        'auth_required': False,
    },
    {
        'proxy_address': "0.0.0.0:1080",
        'proxy_type': ProxyType.OWN_DC_SOCKS5,
        'auth_required': True,
        'proxy_username': 'user',
        'proxy_password': 'pass',
    }
]
