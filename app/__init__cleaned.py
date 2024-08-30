from extensions_salaries import format_with_commas
from general.general_rest_companies import general_rest_companies_bp
from general.general_rest_jobs import general_rest_jobs_bp
from general.general_rest_stub import general_rest_stub_bp
from secrets_jobs.credentials import (
    flask_secret,
    postgres_information_login_details,
    maria_information_login_details,
    email_server_address,
    email_server_port,
    email_server_username,
    email_server_password,
    email_server_tls,
    email_server_ssl,
    email_server_ssl_verify,
    email_enabled
)

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from extensions_sql import db
from extensions_mail import mail

from email_jobs.email_jobs import email_bp

from sso_github.sso_github import sso_github_bp
from sso_google.sso_google import sso_google_bp

from general.general import general_bp
from general.general_rest import general_rest_bp
from user_jobs.user_profiles_saved_lists import \
    user_profiles_saved_lists_rest_bp

from user_jobs.users_jobs import user_bp

from user_jobs.user_profiles import user_profiles_bp
from user_jobs.user_profiles_rest import user_profiles_rest_bp

from admin.admin import admin_bp
from admin.admin_rest import admin_rest_bp

from admin_query.admin_query import admin_query_bp
from admin_query.admin_query_rest import admin_query_rest_bp


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_host=1)
    app.config['SECRET_KEY'] = flask_secret
    app.config['PREFERRED_URL_SCHEME'] = 'https'

    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True

    # app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_ECHO'] = False
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.jinja_env.filters['commafy'] = format_with_commas

    app.config['SQLALCHEMY_DATABASE_URI'] = postgres_information_login_details
    app.config['SQLALCHEMY_BINDS'] = {
        "mariadb": {
            "url": maria_information_login_details,
            "pool_recycle": 3600,
        },
        "postgres": {
            "url": postgres_information_login_details,
            "pool_recycle": 3600,
        }
    }

    db.app = app
    db.init_app(app)

    app.config['MAIL_SERVER'] = email_server_address
    app.config['MAIL_PORT'] = email_server_port
    app.config['MAIL_USERNAME'] = email_server_username
    app.config['MAIL_PASSWORD'] = email_server_password
    app.config['MAIL_USE_TLS'] = email_server_tls
    app.config['MAIL_USE_SSL'] = email_server_ssl
    app.config['MAIL_SSL_VERIFY'] = email_server_ssl_verify
    app.config['MAIL_BACKEND'] = 'smtp' if email_enabled else 'console'
    app.config['MAIL_USE_LOCALTIME'] = False
    mail.init_app(app)

    app.register_blueprint(general_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(user_profiles_bp)

    app.register_blueprint(email_bp)
    app.register_blueprint(sso_github_bp)
    app.register_blueprint(sso_google_bp)

    app.register_blueprint(general_rest_bp)
    app.register_blueprint(general_rest_stub_bp)
    app.register_blueprint(general_rest_jobs_bp)
    app.register_blueprint(general_rest_companies_bp)
    app.register_blueprint(user_profiles_rest_bp)
    app.register_blueprint(user_profiles_saved_lists_rest_bp)

    app.register_blueprint(admin_bp)
    app.register_blueprint(admin_rest_bp)

    app.register_blueprint(admin_query_bp)
    app.register_blueprint(admin_query_rest_bp)

    return app
