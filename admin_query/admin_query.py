"""
Administrator Query

Allows the admin to create a manual request for an API and debug database
routines.
"""
from datetime import datetime

from flask import (
    render_template,
    Blueprint,
    flash,
    redirect,
    url_for,
    session,
    request
)

from admin_query.forms.QueryAPI import QueryAPI
from admin_query.forms.Scrape import Scrape

from extensions_api_endpoints import (
    get_api_endpoint_http_path_and_nice_name_only
)

from extensions_api_keys import get_api_key_only

from extensions_api_list import (
    api_get_list_base,
    get_api_list_url_only
)

from extensions_proxies import (
    proxy_get_proxies_base_last_used,
    proxy_get_proxy_name
)

from extensions_mongo import mongo_storage_add
from extensions_user import get_authenticated_user_name
from models.mariadb.mongo_scrape_storage import MongoScrapeStorage
from models.mariadb.mongo_storage import MongoStorage
from secrets_jobs.credentials import admin_list

admin_query_bp = Blueprint(
    'admin_query',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/admin_query'
)


@admin_query_bp.route(
    "/admin_query",
    methods=["GET", "POST"]
)
def admin_query():
    """
    Administrator Page
    Receives input from a query form allowing the admin to store an API request
    into a table which can then be processed by the server.
    """

    if not session.get('user_id', False):

        flash(
            "Sorry, you cannot access this page since you are not logged in.",
            'danger'
        )

        # Send the unauthenticated user back to the homepage.
        return redirect(url_for('general.home'))

    if get_authenticated_user_name() not in admin_list:

        flash(
            "You are not authorized to access this page.",
            "danger"
        )

        return redirect(url_for('general.home'))

    form = QueryAPI()

    form.proxy.choices = [(str(i.id), str(i.proxy_address))
                          for i in proxy_get_proxies_base_last_used()]

    form.api.choices = [(str(i.id), str(i.nice_name))
                        for i in (api_get_list_base())]

    # Admin will retrieve API key from REST

    # Admin will retrieve Endpoints from REST

    if request.method == "POST":

        # Automatic proxy selection
        selected_proxy = form.proxy.data
        selected_api_key = form.api_key.data
        selected_api_key_auto = form.api_key_auto.data
        selected_api = form.api.data
        selected_endpoint = form.endpoint.data

        unique_suffix = '-prmBdyKey'
        current_active_tab = request.form.get('currentActiveTab')
        new_dict = request.form.to_dict()

        for j in [i for i in new_dict.keys()
                  if len(i) < len(unique_suffix) or
                  i.find(unique_suffix) == -1]:
            new_dict.pop(j, None)

        for j in [i for i in new_dict.keys()]:
            new_dict[j[:-len(unique_suffix)]] = new_dict.pop(j)

        proxy_name = None
        if not selected_api_key_auto:
            # Select the Proxy if API Key Auto is not set
            proxy_name = proxy_get_proxy_name(selected_proxy)

        # Select the APIEndpoint
        api_endpoint = get_api_endpoint_http_path_and_nice_name_only(
            selected_endpoint)

        # Select the APIListURL
        api_list_url = get_api_list_url_only(selected_api)

        api_key = None

        if not selected_api_key_auto:
            # Select the APIKey if API Key Auto is not set
            api_key = get_api_key_only(selected_api_key)

        # Save all settings here in case the CSRF token needs a refresh.
        session['saved_settings'] = {
            'current_active_tab': current_active_tab
            if current_active_tab is not None else None,

            'api_key_auto': selected_api_key_auto,

            'api': form.api.data
            if form.api.data is not None else None,

            'endpoint': form.endpoint.data
            if form.endpoint.data is not None else None,

            'input_json': new_dict
            if new_dict is not None else None,
        }

        if form.validate_on_submit():
            new_mongo_row = MongoStorage(
                time=datetime.now(),
                proxy=proxy_name.proxy_address
                if proxy_name else None,
                api=api_list_url.url,
                api_key=api_key.key
                if api_key else None,
                api_key_auto=selected_api_key_auto
                if selected_api_key_auto else None,
                url=api_endpoint.http_path,
                endpoint_nice_name=api_endpoint.nice_name,
                input_json=new_dict,
            )

            result = mongo_storage_add(new_mongo_row)
            if isinstance(result, str) and len(result) != 0:

                flash(
                    "New Query inserted with ID: " + result,
                    "success"
                )

            else:

                # Clear any saved settings on failure
                if session.get('saved_settings', False):
                    session.pop('saved_settings')

                flash("Error", "danger")
        else:
            flash(
                "Error with form data or CSRF token expired. Try again.",
                "danger"
            )

    return render_template(
        "admin_query/admin_query.html",
        user=get_authenticated_user_name(),
        form=form
    )


@admin_query_bp.route(
    "/admin_query/view_extra/<int:api_endpoint_extra_id>",
    methods=["GET", "POST"]
)
def admin_query_view_extra(api_endpoint_extra_id: int):
    """
    Admin Page
    Loads the template for viewing an extra documentation document.
    """
    if not session.get('user_id', False):
        flash(
            "Sorry, you cannot access this page since you are not logged in.",
            'danger'
        )

        # Send the unauthenticated user back to the homepage.
        return redirect(url_for('general.home'))

    if get_authenticated_user_name() not in admin_list:
        flash(
            "You are not authorized to access this page.",
            "danger"
        )

        return redirect(url_for('general.home'))

    if api_endpoint_extra_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin_query.admin_query'))

    return render_template(
        "admin_query/view_endpoint_extra_doc.html",
        user=get_authenticated_user_name(),
        endpoint_extra_id=api_endpoint_extra_id
    )


@admin_query_bp.route(
    "/admin_scrape",
    methods=["GET", "POST"]
)
def admin_scrape():
    """
    Administrator Page
    Receives input from a query form allowing the admin to store a scrape
    request in a table which can then be processed by the server.
    """

    if not session.get('user_id', False):

        flash(
            "Sorry, you cannot access this page since you are not logged in.",
            'danger'
        )

        # Send the unauthenticated user back to the homepage.
        return redirect(url_for('general.home'))

    if get_authenticated_user_name() not in admin_list:

        flash(
            "You are not authorized to access this page.",
            "danger"
        )

        return redirect(url_for('general.home'))

    form = Scrape()

    # Admin will retrieve API key from REST

    # Admin will retrieve Endpoints from REST

    if request.method == "POST":

        # Automatic proxy selection

        # Save all settings here in case the CSRF token needs a refresh.
        session['saved_scrape_settings'] = {
            'url': form.url.data
            if form.url.data is not None else None,
        }

        if form.validate_on_submit():
            new_mongo_scrape_row = MongoScrapeStorage(
                time=datetime.now(),
                url=form.url.data,
            )

            if mongo_storage_add(new_mongo_scrape_row) is not None:

                flash(
                    "New Scrape Query inserted with ID: " +
                    str(new_mongo_scrape_row.id),
                    "success"
                )

            else:

                # Clear any saved settings on failure
                if session.get('saved_scrape_settings', False):
                    session.pop('saved_scrape_settings')

                flash(
                    "Error",
                    "danger"
                )
        else:
            flash(
                "Error with form data or CSRF token expired. Try again.",
                "danger"
            )

    return render_template(
        "admin_query/admin_scrape.html",
        user=get_authenticated_user_name(),
        form=form
    )


@admin_query_bp.route(
    "/admin_database_routines",
    methods=["GET", "POST"]
)
def admin_database_routines():
    """
    Administrator Page
    Receives input from a query form allowing the admin to store a new database
    routine in a table which can then be processed on a schedule.
    """

    if not session.get('user_id', False):

        flash(
            "Sorry, you cannot access this page since you are not logged in.",
            'danger'
        )

        # Send the unauthenticated user back to the homepage.
        return redirect(url_for('general.home'))

    if get_authenticated_user_name() not in admin_list:

        flash(
            "You are not authorized to access this page.",
            "danger"
        )

        return redirect(url_for('general.home'))

    form = Scrape()

    # Admin will retrieve API key from REST

    # Admin will retrieve Endpoints from REST

    if request.method == "POST":

        # Automatic proxy selection

        # Save all settings here in case the CSRF token needs a refresh.
        session['saved_scrape_settings'] = {
            'url': form.url.data
            if form.url.data is not None else None,
        }

        if form.validate_on_submit():
            new_mongo_scrape_row = MongoScrapeStorage(
                time=datetime.now(),
                url=form.url.data,
            )

            if mongo_storage_add(new_mongo_scrape_row) is not None:

                flash(
                    "New Scrape Query inserted with ID: " +
                    str(new_mongo_scrape_row.id),
                    "success"
                )

            else:

                # Clear any saved settings on failure
                if session.get('saved_scrape_settings', False):
                    session.pop('saved_scrape_settings')

                flash(
                    "Error",
                    "danger"
                )
        else:
            flash(
                "Error with form data or CSRF token expired. Try again.",
                "danger"
            )

    return render_template(
        "admin_query/admin_database_routines.html",
        user=get_authenticated_user_name(),
        form=form
    )
