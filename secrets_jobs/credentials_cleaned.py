admin_list = ["Secret Admin Username CHANGE ME"]
rapid_api_keys = [
    {
        'key': "a",
        'preferred_proxy': '0.0.0.0:0',
    }
]

api_jobs_api_keys = [
    {
            'key': '''\
a\
''',
            'preferred_proxy': '0.0.0.0:0',
        },
]
path_to_base = "/home/jobs/jobs/"
path_to_secrets = path_to_base + "secrets_jobs/"
flask_secret = "SECRETFLASKKEYaaaa"
jwt_path_to_public_key = path_to_secrets + """EdDSA_public.pem"""
jwt_path_to_private_key = path_to_secrets + """EdDSA_private.pem"""

maria_information_login_details = """mariadb+pymysql://jobs:NEWPASSWORDyyyy@127.0.0.1:3306/jobs?charset=utf8mb4"""
postgres_information_login_details = """postgresql+psycopg2://jobs:NEWPASSWORDzzzz@127.0.0.1:5432/jobs"""
mongodb_information_login_details = """mongodb://jobs:NEWPASSWORDxxxx@127.0.0.1:27017/?authSource=jobs"""

mongodb_database_name = """jobs"""
mariadb_database_name = """jobs"""
postgres_database_name = """jobs"""

last_updated = "1715843424"
server_address = "0.0.0.0"

proxy_public_ip_address_for_leak_check = "0.0.0.0"
proxy_public_website_check = "https://api.ipify.org"
proxy_server_authentication_token = "xxx"
proxy_list_location_file_path = "proxycheck/proxylist.txt"
cdn_address = "xxx"
cdn_relative_path = "/cdn/"
cdn_cloudflare_enabled = "0"


# Set proper ownership of these binaries, or copy them to a directory
path_to_chromium_exe = "/usr/bin/chromium"
path_to_chrome_driver = "/usr/bin/chromedriver"

pelias_parser_query_url = "http://localhost:3000/parser/parse"

host_public_ip_address = "0.0.0.0"
website_return_url = "xxxx"

mail_server_mail_from = ""
email_server_address = ""
email_server_port = "465"
email_server_username = "xxx"
email_server_password = """xxx"""
email_server_tls = False
email_server_ssl = True
email_server_ssl_verify = True
email_server_use_localtime = True

email_enabled = "0"

sso_github_id = ""
sso_github_secret = ""
sso_github_enabled = True

sso_google_secrets_path = path_to_secrets + "google_secret.json"

sso_google_enabled = False

google_recaptcha_v2_key = ""
google_recaptcha_v2_secret = ""

google_recaptcha_v2_enabled = False
