import math

from flask import (
    render_template,
    Blueprint,
    url_for,
    redirect,
    flash,
    session,
    Response,
    send_file,
    make_response,
    request,
)

from extensions_companies import get_company_by_id
from extensions_html_parsing import (
    parse_webpage_html2text,
    parse_webpage_bs4,
    parse_webpage_bs4_html5lib
)
from extensions_jobs import get_listed_job_by_id
from extensions_mongo import get_mongo_scrape_from_url
from extensions_saved_jobs import (
    check_saved_job_status
)
from extensions_saved_companies import (
    check_saved_company_status
)

from extensions_saved_companies import check_saved_company_status
from extensions_user import get_authenticated_user_name
from models.postgres.company import Company
from models.postgres.listed_job import ListedJob
from user_jobs.user_limits import (
    max_jobs_authenticated,
    max_jobs_unauthenticated
)

general_bp = Blueprint(
    'general',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/general'
)


@general_bp.route('/robots.txt')
def robots_txt():
    """
    Prevents robots from accessing these routes
    """
    content = """\
User-agent: *
Disallow: /admin/
Disallow: /login/
Disallow: /signup/
Disallow: /api/
Disallow: /private/
Disallow: /tmp/

User-agent: Googlebot
Disallow:

User-agent: Bingbot
Disallow:

Disallow: /*?\
"""
    return Response(content, mimetype='text/plain')


@general_bp.route('/favicon.ico')
def favicon():
    """
    Serves the favicon with the correct MIME type
    """
    return Response(
        url_for('general.static',
                filename='assets/fav/favicon.ico'),
        mimetype='image/x-icon')


@general_bp.route(
    "/"
)
def home():
    """
    Homepage
    """

    return render_template(
        "general/welcome.html",
        user=get_authenticated_user_name()
    )


@general_bp.route(
    "/get_started"
)
def get_started():
    """
    Get Started Link
    """

    # Send the user to the Get Started Page, don't display login buttons if
    # the user is already logged in.
    return render_template(
        "general/get_started.html",
        user=get_authenticated_user_name()
    )


@general_bp.route(
    "/updates"
)
def updates():
    return "TODO"


@general_bp.route(
    "/companies"
)
def companies():
    return render_template(
        "general/companies_board.html",
        user=get_authenticated_user_name()
    )


@general_bp.route(
    "/jobs"
)
def jobs():
    return render_template(
        "general/jobs_board.html",
        user=get_authenticated_user_name()
    )


@general_bp.route(
    "/view_job/<int:job_id>"
)
def view_job(job_id: int):
    """
    View a job based on Job ID
    """

    if (not isinstance(job_id, int) or
            job_id < 0):
        flash(
            'Could not locate Job',
            'danger'
        )

        return redirect(url_for('general.jobs'))

    listed_job: ListedJob = get_listed_job_by_id(job_id)

    if not isinstance(listed_job, ListedJob):
        flash(
            'Could not locate Job',
            'danger'
        )

        return redirect(url_for('general.jobs'))

    # SQLAlchemy session scope switches from Postgres to MariaDB.

    scraped_page: None = None

    if (listed_job.apply_link is not None or
            listed_job.apply_link != ''):
        scraped_page: str = get_mongo_scrape_from_url(
            str(listed_job.apply_link)
        )

    location = None
    if (listed_job.listed_job_location is not None and
            len(listed_job.listed_job_location) >= 1):
        location = (listed_job.listed_job_location[0]
                    .listed_job_location.to_jobs_rest())

    return render_template(
        "general/view_job.html",
        job=listed_job,
        location=location,
        job_scraped=parse_webpage_html2text(scraped_page)
        if scraped_page else (
            'We are currently queued to scrape this page. '
            'You may still visit the link to look at the job listing.'),

        user=get_authenticated_user_name(),
        profile=session.get('profile_id') is not None,

        saved_job=check_saved_job_status(listed_job.id)
        if session.get('profile_id') is not None else False,

        saved_company=check_saved_company_status(listed_job.company_id)
        if session.get('profile_id') is not None else False,
    )


@general_bp.route(
    "/view_company/<int:company_id>"
)
def company_details(company_id: int):
    """
    View a company based on Company ID
    """

    if (not isinstance(company_id, int) or
            company_id < 0):
        flash(
            'Could not locate Company',
            'danger'
        )

        return redirect(url_for('general.companies'))

    company: Company = get_company_by_id(company_id)

    if not isinstance(company, Company):
        flash(
            'Could not locate Company',
            'danger'
        )

        return redirect(url_for('general.companies'))

    found_user = get_authenticated_user_name()

    if found_user:
        max_pages: int = (
            math.ceil(company.current_job_count/max_jobs_authenticated)
        )
        page_limit_max: int = max_jobs_authenticated
    else:
        max_pages: int = (
            math.ceil(company.current_job_count/max_jobs_unauthenticated)
        )
        page_limit_max: int = max_jobs_unauthenticated

    return render_template(
        "general/view_company.html",
        company=company,
        page_limit_max=page_limit_max,
        max_pages=max_pages,
        user=found_user,
        profile=session.get('profile_id') is not None,

        saved_company=check_saved_company_status(company.id)
        if session.get('profile_id') is not None else False,
    )


@general_bp.app_errorhandler(404)
def default_404_error_page(e):
    return make_response("""\
<video src='""" + url_for(
        'general.static',
        filename='assets/gated/sample/jobs_intro_cache.mp4'
    ) + """' autoplay loop muted playsinline preload="metadata"></video>
<br/>
You've attempted to access """ + str(request.path) + """ but it does not exist.
<div style='display:none'>""" + str(request.path) + """/div>""", 404)
