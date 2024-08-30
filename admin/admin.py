from flask import (
    render_template,
    Blueprint,
    flash,
    redirect,
    url_for,
    session
)

from extensions_api_endpoints import (
    get_api_endpoints_dashboard_display,
    get_api_endpoints_type_list_existing,
    get_api_endpoint_full
)
from extensions_api_list import (
    api_get_list,
    get_api_list_url_filters_dashboard_display
)

from extensions_mongo import (
    get_mongo_doc_raw,
    get_mongo_db_url_nice_name_and_input,
    check_for_html_output,
    get_mongo_db_url_query_time
)

from extensions_proxies import proxy_get_proxies
from extensions_user import get_authenticated_user_name
from routines.parsing.apply_link import get_apply_link
from routines.parsing.company import get_companies
from routines.parsing.conversions import (
    convert_bytes_to_dict_raw,
    convert_bytes_to_dict
)
from routines.parsing.description import get_descriptions
from routines.parsing.experience_level import get_experience_levels
from routines.parsing.job_title import get_job_titles
from routines.parsing.job_type import get_job_types

from routines.parsing.location import get_locations
from routines.parsing.salary import get_job_salaries
from routines.parsing.times import get_times
from secrets_jobs.credentials import admin_list

admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/admin'
)


@admin_bp.route("/admin")
def admin():
    """
    Administrator Page Menu
    Shows all the links to menus for administrative functions.
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

    return render_template(
        "admin/admin_dashboard.html",
        user=get_authenticated_user_name()
    )


@admin_bp.route(
    "/admin_proxy_list"
)
def admin_proxy_list():
    """
    Administrator Page
    Display the proxy list for the admin.
    Allows the admin to test all proxies, displaying the result.
    Shows the amount of requests and failed requests for each proxy.
    Allows the admin to disable a proxy.
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

    return render_template(
        "admin/admin_proxy_list.html",
        user=get_authenticated_user_name(),
        proxies=proxy_get_proxies()
    )


@admin_bp.route(
    "/admin_api_list"
)
def admin_api_list():
    """
    Administrator Page
    Display the list of API for the admin.
    Allows the admin to disable the API.
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

    return render_template(
        "admin/admin_api_list.html",
        user=get_authenticated_user_name(),
        api_list=api_get_list()
    )


@admin_bp.route(
    "/admin_api_endpoints"
)
def admin_api_endpoints():
    """
    Administrator Page
    Display the list of API Endpoints for the admin.
    Allows the admin to disable the API Endpoint.
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

    return render_template(
        "admin/admin_api_endpoints.html",
        user=get_authenticated_user_name(),
        api_endpoints=get_api_endpoints_dashboard_display(),
        api_endpoints_types=get_api_endpoints_type_list_existing(),
    )


@admin_bp.route(
    "/admin/view_endpoint/<int:api_endpoint_id>"
)
def admin_view_endpoint(api_endpoint_id: int):
    """
    Administrator Page
    Display the details of a specific Endpoint
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

    if api_endpoint_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_api_list'))

    return render_template(
        "admin/admin_api_view_endpoint.html",
        user=get_authenticated_user_name(),
        api_endpoint=get_api_endpoint_full(api_endpoint_id),
    )


@admin_bp.route(
    "/admin_mongo_storage"
)
def admin_mongo_storage():
    """
    Administrator Page
    Shows the current list of cached queries in the database.
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

    return render_template(
        "admin/admin_mongo_storage.html",
        user=get_authenticated_user_name(),
        api_endpoints_types=get_api_endpoints_type_list_existing(),
        api_list_urls=get_api_list_url_filters_dashboard_display(),
    )


@admin_bp.route(
    "/admin_mongo_scrape_storage"
)
def admin_mongo_scrape_storage():
    """
    Administrator Page
    Shows the current list of cached scrapes in the database.
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

    scrape_sort_types = [
        ['Query Time (Desc)', 'query_time_desc'],
        ['Query Time (Asc)', 'query_time_asc'],
        ['ID  (Desc)', 'id_desc'],
        ['ID (Asc)', 'id_asc'],
        ['Time (Desc)', 'time_desc'],
        ['Time (Asc)', 'time_asc'],
        ['Code (Desc)', 'code_desc'],
        ['Code (Asc)', 'code_asc'],
        ['Length (Desc)', 'length_desc'],
        ['Length (Asc)', 'length_asc'],
    ]

    return render_template(
        "admin/admin_mongo_scrape_storage.html",
        user=get_authenticated_user_name(),
        types=scrape_sort_types,
    )


@admin_bp.route(
    "/admin/view_mongo/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_mongo(mongo_storage_id: int):
    """
    Admin Page
    Returns the text of a mongo storage ID without any parsing.
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return render_template(
        "admin/admin_view_mongo.html",
        user=get_authenticated_user_name(),
        mongo_db_id=mongo_storage_id
    )


@admin_bp.route(
    "/admin/view_scrape/<int:mongo_scrape_storage_id>",
    methods=["GET"]
)
def admin_view_mongo_scrape(mongo_scrape_storage_id: int):
    """
    Admin Page
    Returns the text of a mongo storage ID without any parsing.
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

    if mongo_scrape_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return render_template(
        "admin/admin_view_mongo_scrape.html",
        user=get_authenticated_user_name(),
        mongo_db_scrape_id=mongo_scrape_storage_id
    )


@admin_bp.route(
    "/admin/view_raw/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_raw(mongo_storage_id: int):
    """
    Admin Page
    Returns the raw mongo data retrieved by the server.
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    if check_for_html_output(mongo_storage_id):

        flash(
            "Data does not include interpreted data. Defaulting to Text View.",
            "danger"
        )

        return redirect(
            url_for(
                'admin.admin_view_mongo',
                mongo_storage_id=mongo_storage_id
            )
        )

    dict_new = convert_bytes_to_dict(
        get_mongo_doc_raw(mongo_storage_id)
        .decode()
    )

    if dict_new is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))
    return dict_new


@admin_bp.route(
    "/admin/view_raw_locations/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_raw_locations(mongo_storage_id: int):
    """
    Admin Page
    Returns the raw processed location data of the Mongo Storage ID.
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    if check_for_html_output(mongo_storage_id):
        flash(
            "Data does not include interpreted data. Defaulting to Text View.",
            "danger"
        )

        return redirect(
            url_for(
                'admin.admin_view_mongo',
                mongo_storage_id=mongo_storage_id
            )
        )

    stored_mongo_data = get_mongo_db_url_nice_name_and_input(mongo_storage_id)

    if stored_mongo_data is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    dict_new = convert_bytes_to_dict_raw(
        get_mongo_doc_raw(mongo_storage_id)
        .decode()
    )

    if dict_new is None:

        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return get_locations(
        api_url=stored_mongo_data.url,
        nice_name=stored_mongo_data.endpoint_nice_name,
        dict_new=dict_new,
        input_json=stored_mongo_data.input_json
    )


@admin_bp.route(
    "/admin/view_raw_companies/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_raw_companies(mongo_storage_id: int):
    """
    Admin Page
    Returns the raw parsed companies of the provided Mongo Storage ID
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    if check_for_html_output(mongo_storage_id):
        flash(
            "Data does not include interpreted data. Defaulting to Text View.",
            "danger"
        )

        return redirect(
            url_for(
                'admin.admin_view_mongo',
                mongo_storage_id=mongo_storage_id
            )
        )

    stored_mongo_data = get_mongo_db_url_nice_name_and_input(mongo_storage_id)

    if stored_mongo_data is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    dict_new = convert_bytes_to_dict_raw(
        get_mongo_doc_raw(mongo_storage_id)
        .decode()
    )

    if dict_new is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return get_companies(
        api_url=stored_mongo_data.url,
        nice_name=stored_mongo_data.endpoint_nice_name,
        dict_new=dict_new,
        input_json=stored_mongo_data.input_json
    )


@admin_bp.route(
    "/admin/view_raw_descriptions/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_raw_descriptions(mongo_storage_id: int):
    """
    Admin Page
    Returns the raw parsed descriptions of the provided Mongo Storage ID
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    if check_for_html_output(mongo_storage_id):
        flash(
            "Data does not include interpreted data. Defaulting to Text View.",
            "danger"
        )

        return redirect(
            url_for(
                'admin.admin_view_mongo',
                mongo_storage_id=mongo_storage_id
            )
        )

    stored_mongo_data = get_mongo_db_url_nice_name_and_input(mongo_storage_id)

    if stored_mongo_data is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    dict_new = convert_bytes_to_dict_raw(
        get_mongo_doc_raw(mongo_storage_id)
        .decode()
    )

    if dict_new is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return get_descriptions(
        api_url=stored_mongo_data.url,
        nice_name=stored_mongo_data.endpoint_nice_name,
        dict_new=dict_new,
        input_json=stored_mongo_data.input_json
    )


@admin_bp.route(
    "/admin/view_raw_apply_links/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_raw_apply_links(mongo_storage_id: int):
    """
    Admin Page
    Returns the raw parsed Apply Links of the provided Mongo Storage ID
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    if check_for_html_output(mongo_storage_id):
        flash(
            "Data does not include interpreted data. Defaulting to Text View.",
            "danger"
        )

        return redirect(
            url_for(
                'admin.admin_view_mongo',
                mongo_storage_id=mongo_storage_id
            )
        )

    stored_mongo_data = get_mongo_db_url_nice_name_and_input(mongo_storage_id)

    if stored_mongo_data is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    dict_new = convert_bytes_to_dict_raw(
        get_mongo_doc_raw(mongo_storage_id)
        .decode()
    )

    if dict_new is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return get_apply_link(
        api_url=stored_mongo_data.url,
        nice_name=stored_mongo_data.endpoint_nice_name,
        dict_new=dict_new,
        input_json=stored_mongo_data.input_json,
    )


@admin_bp.route(
    "/admin/view_raw_experience_levels/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_raw_experience_levels(mongo_storage_id: int):
    """
    Admin Page
    Returns the raw parsed Experience Levels of the provided Mongo Storage ID
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    if check_for_html_output(mongo_storage_id):
        flash(
            "Data does not include interpreted data. Defaulting to Text View.",
            "danger"
        )

        return redirect(
            url_for(
                'admin.admin_view_mongo',
                mongo_storage_id=mongo_storage_id
            )
        )

    stored_mongo_data = get_mongo_db_url_nice_name_and_input(mongo_storage_id)

    if stored_mongo_data is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    dict_new = convert_bytes_to_dict_raw(
        get_mongo_doc_raw(mongo_storage_id)
        .decode()
    )

    if dict_new is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return get_experience_levels(
        api_url=stored_mongo_data.url,
        nice_name=stored_mongo_data.endpoint_nice_name,
        dict_new=dict_new,
        # input_json=stored_mongo_data.input_json,
    )


@admin_bp.route(
    "/admin/view_raw_job_titles/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_raw_job_titles(mongo_storage_id: int):
    """
    Admin Page
    Returns the raw parsed Job Titles of the provided Mongo Storage ID
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    if check_for_html_output(mongo_storage_id):
        flash(
            "Data does not include interpreted data. Defaulting to Text View.",
            "danger"
        )

        return redirect(
            url_for(
                'admin.admin_view_mongo',
                mongo_storage_id=mongo_storage_id
            )
        )

    stored_mongo_data = get_mongo_db_url_nice_name_and_input(mongo_storage_id)

    if stored_mongo_data is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    dict_new = convert_bytes_to_dict_raw(
        get_mongo_doc_raw(mongo_storage_id)
        .decode()
    )

    if dict_new is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return get_job_titles(
        api_url=stored_mongo_data.url,
        nice_name=stored_mongo_data.endpoint_nice_name,
        dict_new=dict_new,
        input_json=stored_mongo_data.input_json,
    )


@admin_bp.route(
    "/admin/view_raw_job_types/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_raw_job_types(mongo_storage_id: int):
    """
    Admin Page
    Returns the raw parsed Job Types of the provided Mongo Storage ID
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    if check_for_html_output(mongo_storage_id):
        flash(
            "Data does not include interpreted data. Defaulting to Text View.",
            "danger"
        )

        return redirect(
            url_for(
                'admin.admin_view_mongo',
                mongo_storage_id=mongo_storage_id
            )
        )

    stored_mongo_data = get_mongo_db_url_nice_name_and_input(mongo_storage_id)

    if stored_mongo_data is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    dict_new = convert_bytes_to_dict_raw(
        get_mongo_doc_raw(mongo_storage_id)
        .decode()
    )

    if dict_new is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return get_job_types(
        api_url=stored_mongo_data.url,
        nice_name=stored_mongo_data.endpoint_nice_name,
        dict_new=dict_new,
        input_json=stored_mongo_data.input_json,
    )


@admin_bp.route(
    "/admin/view_raw_salaries/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_raw_salaries(mongo_storage_id: int):
    """
    Admin Page
    Returns the raw parsed Job Types of the provided Mongo Storage ID
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    if check_for_html_output(mongo_storage_id):
        flash(
            "Data does not include interpreted data. Defaulting to Text View.",
            "danger"
        )

        return redirect(
            url_for(
                'admin.admin_view_mongo',
                mongo_storage_id=mongo_storage_id
            )
        )

    stored_mongo_data = get_mongo_db_url_nice_name_and_input(mongo_storage_id)

    if stored_mongo_data is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    dict_new = convert_bytes_to_dict_raw(
        get_mongo_doc_raw(mongo_storage_id)
        .decode()
    )

    if dict_new is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return get_job_salaries(
        api_url=stored_mongo_data.url,
        nice_name=stored_mongo_data.endpoint_nice_name,
        dict_new=dict_new,
        input_json=stored_mongo_data.input_json,
    )


@admin_bp.route(
    "/admin/view_raw_times/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_view_raw_times(mongo_storage_id: int):
    """
    Admin Page
    Returns the raw parsed times of the provided Mongo Storage ID
    Posted Time, Expiration Time
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    if check_for_html_output(mongo_storage_id):
        flash(
            "Data does not include interpreted data. Defaulting to Text View.",
            "danger"
        )

        return redirect(
            url_for(
                'admin.admin_view_mongo',
                mongo_storage_id=mongo_storage_id
            )
        )

    stored_mongo_data = get_mongo_db_url_nice_name_and_input(mongo_storage_id)

    if stored_mongo_data is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    dict_new = convert_bytes_to_dict_raw(
        get_mongo_doc_raw(mongo_storage_id)
        .decode()
    )

    if dict_new is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    # retrieve query times from mongo storage
    stored_mongo_data_time = (get_mongo_db_url_query_time(mongo_storage_id)
                              .query_time)

    return get_times(
        api_url=stored_mongo_data.url,
        nice_name=stored_mongo_data.endpoint_nice_name,
        dict_new=dict_new,
        input_json=stored_mongo_data.input_json,
        query_time=stored_mongo_data_time
    )


@admin_bp.route(
    "/admin/confirm_mongo_deletion/<int:mongo_storage_id>",
    methods=["GET"]
)
def admin_confirm_mongo_deletion(mongo_storage_id: int):
    """
    Admin Page
    Displays a confirmation page to delete a
    MongoStorage row and MongoDB Object ID.
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

    if mongo_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return render_template(
        "admin/admin_confirm_mongo_deletion.html",
        user=get_authenticated_user_name(),
        mongo_db_id=mongo_storage_id
    )


@admin_bp.route(
    "/admin/confirm_scrape_deletion/<int:mongo_scrape_storage_id>",
    methods=["GET"]
)
def admin_confirm_mongo_scrape_deletion(mongo_scrape_storage_id: int):
    """
    Admin Page
    Displays a confirmation page to delete a
    MongoScrapeStorage row and MongoDB Object ID.
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

    if mongo_scrape_storage_id is None:
        flash(
            "There was a problem with your request.",
            "danger"
        )

        return redirect(url_for('admin.admin_mongo_storage'))

    return render_template(
        "admin/admin_confirm_mongo_deletion.html",
        user=get_authenticated_user_name(),
        mongo_scrape_db_id=mongo_scrape_storage_id
    )
