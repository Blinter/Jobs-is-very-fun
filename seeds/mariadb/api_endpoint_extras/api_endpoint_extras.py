"""
API Endpoint Extras

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""
from sqlalchemy import inspect, text, MetaData
from sqlalchemy_utils import database_exists, create_database
from secrets_jobs.credentials import (maria_information_login_details,
                                      mariadb_database_name)
from models.mariadb.api_list_url import APIListURL
from models.mariadb.api_headers import APIHeader
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.api_endpoint_params import APIEndpointParam
from models.mariadb.api_endpoint_bodies import APIEndpointBody
from models.mariadb.api_endpoint_headers import APIEndpointHeader
from models.mariadb.api_endpoint_extras import APIEndpointExtra
from app import create_app, db
import sqlalchemy as db2

engine = db2.create_engine(maria_information_login_details)
if not database_exists(engine.url):
    create_database(engine.url, encoding='UTF8')

app = create_app()


# Function to get the names of foreign key constraints
def get_foreign_key_constraint_names(temp_table, temp_connection):
    """
    Inspect table and get foreign key restraints.
    """
    inspector = inspect(temp_connection)
    fks = inspector.get_foreign_keys(temp_table.name, schema=temp_table.schema)
    return [fk['name'] for fk in fks]


def table_exists(temp_db, table_name, schema=mariadb_database_name):
    """
    Query information_schema and check if table exists.
    """
    query = text(f"""\
SELECT COUNT(*) FROM information_schema.TABLES \
WHERE TABLE_SCHEMA = '{schema}' AND TABLE_NAME = '{table_name}'\
""")
    result = temp_db.session.execute(query)
    return result.scalar() > 0


with app.app_context():
    try:
        metadata = MetaData()
        table = db.Table(
            APIEndpointExtra.__tablename__,
            metadata=metadata,
            bind_key="mariadb",
            autoload_with=engine)
        if table_exists(db, table.name):
            fk_names = get_foreign_key_constraint_names(table, engine)
            for fk_name in fk_names:
                if fk_name:
                    sql_text = (f'ALTER TABLE {table.name} DROP FOREIGN KEY '
                                f'{fk_name}')
                    db.session.execute(text(sql_text))

        table.drop(engine, checkfirst=True)
        table.create(engine, checkfirst=True)

        # retrieve API Endpoints in order to reference foreign keys.
        API_Endpoint_List = db.session.query(APIEndpoint).all()

        # Search Jobs
        # APIJobs | Job Searching API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://apijob-job-searching-api.p.rapidapi.com'
                '/v1/job/search') and
            i.nice_name == 'Search jobs')
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
API Overview
Build powerful applications and integrate Apijob | Job searching api into your\
web and mobile applications with the REST API.

APIJobs offers a developer-friendly and enterprise-grade job listing API\
designed for job boards, comprehensive search functionalities, and deep \
insights\
into the job market. It's structured to provide relevant and real-time data,\
empowering developers to build robust job-related applications with ease.

Features

Search Functionality: Tailor your job search by industry, location, or specific\
skills to find exactly what you're looking for.
Real-Time Data: Get access to the latest job listings and insights with data\
that's constantly updated.
Developer-Friendly: Easy to integrate with clear documentation, making it a\
breeze for developers to incorporate into their projects. Enterprise-Grade:\
Robust and reliable API designed to meet the needs of large-scale applications.\
Getting Started

Free Plan: Start without any cost with the free plan, allowing you to make up \
to\
100 API calls per day.
Pro Plan: Need more? Subscribe to our Pro Plan for higher usage limits and\
advanced features.
Use Cases

Job Boards: Integrate real-time job listings into your job board platform.

Career Services: Enhance your career service application with extensive job\
search capabilities.

Market Analysis: Analyze job market trends with detailed insights into various\
industries and locations.

Start integrating APIJobs into your application today and unlock the potential\
of a comprehensive job listing API!
""",
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Search Jobs
        # avadataservices | Job Postings
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://job-postings1.p.rapidapi.com'
                '/') and
            i.nice_name == '/api/v2/Jobs/Latest')
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
https://jobtransparency.experimentsinthedeep99.com/api/v2/Jobs/Latest""",
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get jobs (JSON)
        # Bebity | Linkedin Jobs Scraper API
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://job-postings1.p.rapidapi.com'
                '/') and
            i.nice_name == '/api/v2/Jobs/Latest')
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
[
    {
        "id": "3602163673",
        "publishedAt": "2023-07-16",
        "salary": "",
        "title": "Cloud AI Engineer (English, French)",
        "jobUrl": "https://fr.linkedin.com/jobs/view/cloud-ai-engineer-english-\
french-at-google-3602163673?trk=public_jobs_topcard-title",
        "companyName": "Google",
        "companyUrl": "https://www.linkedin.com/company/google?trk=public_jobs_\
topcard-org-name",
        "location": "Paris, Île-de-France, France",
        "postedTime": "2 weeks ago",
        "applicationsCount": "Over 200 applicants",
        "description": "Google welcomes people with disabilities.\n\nMinimum 
qualifications:\n\n\n * Bachelor's degree in Computer Science, Mathemati\
cs or equivalent practical experience.\n * Experience with Machine Lear\
ning or Artificial Intelligence.\n * Experience with Machine Learning a\
lgorithms and tools (e.g., TensorFlow), artificial intelligence, deep l\
earning or natural language processing.\n * Ability to speak and write \
in English and French fluently.\n   \n   \n\nPreferred qualifications:\
\n\n\n * Experience in delivering complex Artificial Intelligence (\
AI) or data analytics projects.\n * Experience coding in one or more \
languages such as Python, Scala, Java, Go, or with data structures, \
algorithms, and software design.\n * Experience with deep learning \
frameworks such as TensorFlow, PyTorch, XGBoost.\n * Experience in \
customer-facing technical consulting roles.\n * Knowledge of data \
warehousing concepts, including data warehouse technical architectures,\
infrastructure components, Extract, transform, and load (ETL)) and \
reporting/analytic tools and environments such as Apache Beam, Hadoop,\
Spark, Pig, Hive.\n * Ability to translate business problems in AI \
projects.\n   \n   \n\nAbout The Job\n\nThe Google Cloud Platform \
team helps customers transform and build what's next for their \
business — all with technology built in the cloud. Our products are \
engineered for security, reliability and scalability, running the \
full stack from infrastructure to applications to devices and \
hardware. Our teams are dedicated to helping our customers —
developers, small and large businesses, educational institutions and\
government agencies — see the benefits of our technology come to \
life.\
As part of an entrepreneurial team in this rapidly growing business,\
you will play a key role in understanding the needs of our customers\
and help shape the future of businesses of all sizes use technology
to\
connect with customers, employees and partners.\n\nAs a Cloud AI\
Engineer, you will design and implement Machine Learning solutions \
for\
customer use cases, leveraging core Google products including\
TensorFlow, DataFlow, and Vertex AI. You will work with customers to\
identify opportunities to apply machine learning in their business,\
and travel to customer sites to deploy solutions and deliver \
workshops\
to educate and empower customers. Additionally, you will work closely\
with Product Management and Product Engineering to build and\
constantly drive excellence in our products.\n\nIn this role, \
you will\
support customer implementation of Google Cloud products through\
architecture guidance, best practices, data migration, capacity\
planning, implementation, troubleshooting, and monitoring.\n\nGoogle\
Cloud accelerates organizations’ ability to digitally transform their\
business with the best infrastructure, platform, industry solutions\
and expertise. We deliver enterprise-grade solutions that leverage\
Google’s cutting-edge technology – all on the cleanest cloud in the\
industry. Customers in more than 200 countries and territories turn \
to\
Google Cloud as their trusted partner to enable growth and solve 
their\
most critical business problems.\n\nResponsibilities\n\n\n * Be a\
trusted technical advisor to customers and solve complex Machine\
Learning (ML) issues.\n * Create and deliver best practices\
recommendations, tutorials, blog articles, sample code, and technical\
presentations adapting to different levels of key business and\
technical stakeholders.\n * Work with Customers, Partners, and Google\
Product teams to deliver tailored solutions into production.\n * 
Coach\
customers on the practical issues in ML systems feature\
extraction/feature definition, data validation, monitoring, and\
management of features/models.\n * Travel up to 30% of the time as\
needed in-region for meetings, technical reviews, and onsite delivery\
activities.\n   \n   \n\nGoogle is proud to be an equal opportunity\
workplace and is an affirmative action employer. We are committed to\
equal employment opportunity regardless of race, color, ancestry,\
religion, sex, national origin, sexual orientation, age, citizenship,\
marital status, disability, gender identity or Veteran status. We 
also\
consider qualified applicants regardless of criminal histories,\
consistent with legal requirements. See also Google's EEO Policy and\
EEO is the Law. If you have a disability or special need that 
requires\
accommodation, please let us know by completing our Accommodations 
for\
Applicants form .",
        "contractType": "Full-time",
        "experienceLevel": "Not Applicable",
        "workType": "Project Management, Consulting, and Engineering",
        "sector": "Information Services and Technology, Information and \
Internet",
        "companyId": "1441",
        "posterProfileUrl": "",
        "posterFullName": ""
    },
    {
        "id": "3637378044",
        "publishedAt": "2023-07-28",
        "salary": "",
        "title": "AI Research Scientist (Leadership)",
        "jobUrl":
        "https://fr.linkedin.com/jobs/view/ai-research-scientist-leadership-at-\
meta-3637378044?trk=public_jobs_topcard-title",
        "companyName": "Meta",
        "companyUrl": "https://www.linkedin.com/company/meta?trk=public_jobs_to\
pcard-org-name",
        "location": "Paris, Île-de-France, France",
        "postedTime": "4 days ago",
        "applicationsCount": "103 applicants",
        "description": "Meta is seeking exceptional AI Research Scientists to \
join our AI organization. Individuals in this role are expected to be\
recognized experts in areas such as artificial intelligence, machine\
learning, computational statistics, and applied mathematics,\
particularly including areas such as deep learning, graphical models,\
reinforcement learning, computer perception, natural language \
processing\
and data representation. The ideal candidate will have an interest in\
producing new science to understand intelligence and technology to make\
computers more intelligent, and an equal interest in taking new \
research\
findings in this area and implementing it towards production ready\
problems.\n\n\n\n\nAI Research Scientist (Leadership)\
Responsibilities:\n\n\n\n\n * Help Advance the science and technology \
of\
intelligent machines\n * Contribute to research that enables learning\
the semantics of data (images, video, text, audio and other\
modalities)\n * Work on projects, strategies, and problems of moderate\
to high complexity and scope. Can identify and define both short &\
medium term objectives\n * Design policies, processes, procedures,\
methods, tests, and/or components, from the ground up and with the\
understanding of how to put together end-to-end systems\n *\
Independently lead projects and work cross-functionally to bring\
research advancements to production teams and Meta Products\n *\
Influence progress of relevant research communities by producing\
publications\n * Devise better data-driven models of human behavior\n *\
Plan and execute cutting-edge research and development to advance the\
state-of-the-art in machine perception, mapping, reconstruction and\
localization, as well as 3D scene understanding across\
optical/inertial/wireless sensing systems\n * Collaborate with other\
researchers and engineers across machine perception teams at Meta to\
develop experiments, prototypes, and concepts that advance the\
state-of-the-art in AR/VR systems\n * Work with the team to help \
design,\
setup, and run practical experiments and prototype systems related to\
large-scale long-duration sensing and machine \
reasoning\n\n\n\n\nMinimum\
Qualifications:\n\n\n\n\n * PhD in the following fields: Computer\
Vision, Robotics, State Estimation, 3D Reconstruction, Object Tracking,\
Physics based models, or a related field\n * Experience in applying\
research to production problems\n * Experience leading a team in \
solving\
modeling problems using AI/ML approaches\n * Experience communicating\
research for public audiences of peers\n * Publications in machine\
learning experience, AI, computer science, statistics, applied\
mathematics, data science, or related technical fields\n * Experience\
with real world system building and data collection, including design,\
coding (C++) and evaluation (C++/Python)\n * Hands-on experience\
implementing 3D computer vision algorithms, Sensor Fusion,\
Reconstruction, Object Tracking, Mapping, and Image Processing\n *\
Bachelor's degree in Computer Science, Computer Engineering, relevant\
technical field, or equivalent practical experience.\n\n\n\n\nPreferred\
Qualifications:\n\n\n\n\n * Experience holding a faculty, industry, or\
government researcher position in a role with primary emphasis on AI\
research\n * Experience showing first-author publications at\
peer-reviewed AI conferences (e.g., NeurIPS, CVPR, ICML, ICLR, ICCV, \
and\
ACL)\n * Experience in developing and debugging in C/C++, Python, or\
C#\n * Experience in real-time computer graphics or modern GPU\
programming (CUDA, OpenGL, OpenCL)\n * Experience with designing\
(products or open-source) software for inertial/optical/wireless \
sensing\
devices\n * Experience working in a Unix environment",
        "contractType": "Full-time",
        "experienceLevel": "Not Applicable",
        "workType": "Engineering and Information Technology",
        "sector": "Technology, Information and Internet",
        "companyId": "10667",
        "posterProfileUrl": "",
        "posterFullName": ""
    },
    {
        "id": "3675330333",
        "publishedAt": "2023-07-26",
        "salary": "",
        "title": "Cloud Technical Resident, Cloud Academy, Early Career
        (English, French)",
        "jobUrl":
        "https://fr.linkedin.com/jobs/view/cloud-technical-resident-cloud-acade\
my-early-career-english-french-at-google-3675330333?trk=public_jobs_top\
card-title",
        "companyName": "Google",
        "companyUrl":
        "https://www.linkedin.com/company/google?trk=public_jobs_topcard-org-\
name",
        "location": "Paris, Île-de-France, France",
        "postedTime": "6 days ago",
        "applicationsCount": "94 applicants",
        "description": "Google welcomes people with disabilities.\n\nThe Cloud\
Academy is for applicants who can start in November 2023. Candidates \
are\
encouraged to submit their applications as soon as possible.\n\nMinimum\
qualifications:\n\n\n * Bachelor’s Degree in relevant STEM field (e.g.\
Computer Science, Information Systems, Management Information Systems)\
or equivalent practical experience.\n * Experience working with\
Databases, Web Technologies, Machine Learning, AI or Cloud Foundations\
(e.g. cloud computing) through certifications, internships, coursework,\
or relevant practical experience.\n * Experience in customer service,\
communication or leadership.\n * Ability to speak and write English and\
French fluently.\n   \n   \n\nPreferred qualifications:\n\n\n *\
Experience developing programs/scripts in C++, Java, Python, SQL or\
experience in infrastructure/system administration.\n * Experience\
building or troubleshooting websites or web applications using web\
technologies (e.g., HTTP(S), JavaScript, APIs, TCP/IP, DNS).\n *\
Experience in systems software and algorithms, working with Linux/Unix.\
Experience in database design and SQL query construction.\n * \
Experience\
leading entrepreneurial efforts, outreach within organizations, and/or\
in project/product/program management.\n * Ability to adapt your \
message\
to stakeholders and present technical materials. Demonstrate\
organizational, problem-solving, or troubleshooting skills.\n   \n  \
\n\nAbout The Job\n\nCloud Technical Residents provide technical\
expertise across the full Google Cloud portfolio of products to\
demonstrate the value of, deploy, and provide ongoing support of the\
technology to our customers. Google’s Cloud customer teams are on the\
front lines of leading customers through the largest technological \
shift\
in the history of the IT industry. They help customers understand the\
unique value and transformational benefits that result from applying\
these technologies to their business workloads.\n\nAs a part of the \
full\
time Cloud Academy - Cloud Technical Residency, you will have the \
unique\
opportunity to work in different Google Cloud roles under the direct\
mentorship of experienced staff members. Before you start role\
rotations, you will undergo extensive training to prepare you to add\
value on day one of your customer engagements. The role rotations\
include opportunities to provide implementation, advisory, and support\
services to Google customers across a wide variety of industry and\
scale, as well as potential opportunities to develop tools, demos, and\
related assets for customers.\n\nThroughout the program, you will have\
both personal and professional development opportunities. You will \
build\
your business and technical skills by working on a range of projects\
such as automating and scaling business processes, creating custom\
solutions, and providing data driven insights to Google’s internal \
Sales\
and Product teams. You’ll also have the opportunity to develop project\
management, presentation, and customer-facing skills.\n\nGoogle Cloud\
accelerates organizations’ ability to digitally transform their \
business\
with the best infrastructure, platform, industry solutions and\
expertise. We deliver enterprise-grade solutions that leverage Google’s\
cutting-edge technology – all on the cleanest cloud in the industry.\
Customers in more than 200 countries and territories turn to Google\
Cloud as their trusted partner to enable growth and solve their most\
critical business problems.\n\nResponsibilities\n\n\n * Help build\
creative solutions to challenging customer needs using Google Cloud.\
Improve product feature offerings by providing customer feedback to\
internal cross-functional teams including Product Management and\
Engineering.\n * Collaborate with customers and other Googlers to \
manage\
and drive successful adoption of Google Cloud. Help develop\
recommendations for solution architectures and consulting services.\n *\
Guide customers through the entire innovation lifecycle, building\
strategic roadmaps and driving achievement of key milestones.\n * Solve\
customers' operational issues through problem solving and technical\
troubleshooting, while working with internal teams to drive resolution.\
Help customers get answers to product questions.\n   \n   \n\nGoogle is\
proud to be an equal opportunity workplace and is an affirmative action\
employer. We are committed to equal employment opportunity regardless \
of\
race, color, ancestry, religion, sex, national origin, sexual\
orientation, age, citizenship, marital status, disability, gender\
identity or Veteran status. We also consider qualified applicants\
regardless of criminal histories, consistent with legal requirements.\
See also Google's EEO Policy and EEO is the Law. If you have a\
disability or special need that requires accommodation, please let us\
know by completing our Accommodations for Applicants form .",
        "contractType": "Full-time",
        "experienceLevel": "Entry level",
        "workType": "Project Management, Consulting, and Engineering",
        "sector": "Information Services and Technology, Information and \
Internet",
        "companyId": "1441",
        "posterProfileUrl": "",
        "posterFullName": ""
    },
    {
        "id": "3637372533",
        "publishedAt": "2023-07-29",
        "salary": "",
        "title": "Research Scientist, NLP",
        "jobUrl":
        "https://fr.linkedin.com/jobs/view/research-scientist-nlp-at-meta-3637\
372533?trk=public_jobs_topcard-title",
        "companyName": "Meta",
        "companyUrl":
        "https://www.linkedin.com/company/meta?trk=public_jobs_topcard-org-nam\
e",
        "location": "Paris, Île-de-France, France",
        "postedTime": "3 days ago",
        "applicationsCount": "106 applicants",
        "description": "Meta is seeking Research Scientists to join its\
Fundamental AI Research (FAIR) organization, focused on making\
significant advances in AI. We publish groundbreaking papers and \
release\
frameworks/libraries that are widely used in the open-source community.\
Recent examples include the LLaMa family of Large Language Models \
(LLMs)\
and tool-augmented language models. We also collaborate with the Meta\
Generative AI and other organisations to bring the latest research\
findings to production.We are currently seeking talented researchers\
with experience in NLP to join either our London or Paris sites and \
work\
with us on extending the capabilities of large foundation models to\
reason and to use tools. Researchers will drive impact by: (1)\
publishing state-of-the-art research papers, (2) open sourcing high\
quality code and reproducible results for the community, and (3)\
bringing the latest research to Facebook products for connecting\
billions of users. The chosen candidate(s) will work with a diverse and\
highly interdisciplinary team of scientists, engineers, and\
cross-functional partners, and will have access to cutting edge\
technology, resources, and research facilities.\n\n\n\n\nResearch\
Scientist, NLP Responsibilities:\n\n\n\n\n * Lead research that extends\
the capabilities of foundation models through reasoning and the use of\
tools\n * Work towards long-term ambitious research goals, while\
identifying intermediate milestones.\n * Influence progress of relevant\
research communities by producing publications.\n * Contribute research\
that can be applied to Meta product development.\n * Lead and\
collaborate on research projects within a globally based\
team.\n\n\n\n\nMinimum Qualifications:\n\n\n\n\n * PhD degree in\
Computer Science, Mathematics, or similar quantitative field.\n *\
First-author publications at peer-reviewed AI conferences (e.g. *ACL,\
EMNLP, NeurIPS, ICML, ICLR).\n * Experience in training, fine-tuning,\
and/or experimenting with foundation models beyond black-box use.\n *\
Familiarity with one or more deep learning frameworks (e.g. pytorch,\
tensorflow, …)\n * Ability to communicate complex research both in\
writing and orally for public audiences of peers.\n * Knowledge in a\
programming language.\n\n\n\n\nPreferred Qualifications:\n\n\n\n\n *\
High-impact publications at peer-reviewed AI conferences (e.g. *ACL,\
EMNLP, NeurIPS, ICML, ICLR), as witnessed by citations and other signs\
of influencing the research community.\n * Experience in AI research\
beyond completing a PhD.\n * Experience in developing and debugging\
beyond ML experimentation.\n * Experience in working in an industry\
research environment.\n * Experience in coordinating the research of \
PhD\
        students or other researchers.",
        "contractType": "Full-time",
        "experienceLevel": "Not Applicable",
        "workType": "Other",
        "sector": "Technology, Information and Internet",
        "companyId": "10667",
        "posterProfileUrl": "",
        "posterFullName": ""
    },
    {
        "id": "3676161534",
        "publishedAt": "2023-07-26",
        "salary": "",
        "title": "Senior Visiting Scientist - Facebook AI Research (Paris)",
        "jobUrl":
        "https://fr.linkedin.com/jobs/view/senior-visiting-scientist-facebook-\
ai-research-paris-at-meta-3676161534?trk=public_jobs_topcard-title",
        "companyName": "Meta",
        "companyUrl":
        "https://www.linkedin.com/company/meta?trk=public_jobs_topcard-org-name",
        "location": "Paris, Île-de-France, France",
        "postedTime": "6 days ago",
        "applicationsCount": "Be among the first 25 applicants",
        "description": "Facebook is seeking a Senior Visiting Scientist to join\
our Artificial Intelligence Research team. Term length would be\
considered on a case-by-case basis. The role is a research position but\
there is the possibility to develop leadership\
responsibilities.\n\n\n\n\nSenior Visiting Scientist - Facebook AI\
Research (Paris) Responsibilities:\n\n\n\n\n * Conduct research in\
machine learning\n\n\n\n\nMinimum Qualifications:\n\n\n\n\n * Currently\
holding a faculty or government researcher position\n * Ph.D. and\
publications in Machine Learning, AI, computer science, statistics,\
mathematics, data science, or related technical fields\n * Experience \
in\
theoretical and empirical research and for solving problems with\
research\n * Extended experience in managing teams of researchers\n *\
Academic publications in the field of machine\
learning\n\n\n\n\nPreferred Qualifications:\n\n\n\n\n * Knowledge in a\
programming language\n * Presenting skills, both for technical \
audiences\
and the public at large",
        "contractType": "Full-time",
        "experienceLevel": "Not Applicable",
        "workType": "Research, Analyst, and Information Technology",
        "sector": "Technology, Information and Internet",
        "companyId": "10667",
        "posterProfileUrl": "",
        "posterFullName": ""
    }
]
""",
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "description": "The title of the job"
    },
    "location": {
      "type": "string",
      "description": "The location of the job"
    },
    "rows": {
      "type": "number",
      "description": "The number of rows to return"
    },
    "workType": {
      "type": "string",
      "description": "The job type",
      "enum": [
        "OnSite",
        "Remote",
        "Hybrid"
      ]
    },
    "contractType": {
      "type": "string",
      "description": "Type of job contract",
      "enum": [
        "FullTime",
        "PartTime",
        "Contract",
        "Temporary",
        "Internship",
        "Volunteer"
      ]
    },
    "experienceLevel": {
      "type": "string",
      "description": "The experience level",
      "enum": [
        "Internship",
        "EntryLevel",
        "Associate",
        "MidSeniorLevel",
        "Director"
      ]
    },
    "companyNames": {
      "description": "The company name",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "companyIds": {
      "description": "The company id",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "publishedAt": {
      "type": "string",
      "description": "The date the job was published",
      "enum": [
        "AnyTime",
        "Past24Hours",
        "PastWeek",
        "PastMonth"
      ]
    }
  },
  "required": [
    "title",
    "location",
    "rows",
    "workType",
    "contractType",
    "experienceLevel",
    "companyNames",
    "companyIds",
    "publishedAt"
  ]
}
""",
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        # Get Personal Profile
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-linkedin-profile') and
            i.nice_name == 'Get Personal Profile')
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation='''\
API Overview
Build powerful applications and integrate Fresh LinkedIn Profile Data into your
web and mobile applications with the REST API.

Unlock the Power of LinkedIn Data with Our Robust API

Tap into LinkedIn's extensive network through our reliable, advanced scraping\
API. Access real-time profiles, posts, companies, jobs, and insights with\
LinkedIn Sales Navigator, all delivered directly to you. Valued by AI leaders\
globally, our API is your solution for fresh, accurate LinkedIn data, enabling\
targeted marketing, strategic recruitment, and competitive analysis with ease.\
Stay ahead with our streamlined data access, designed for the digital forefront.

What You Can Achieve with Our LinkedIn Scraping API:

Personal Profile Insights: Dive deep into personal profiles with regular or\
Sales Navigator URLs. Extract comprehensive data, activity posts, and gauge\
recent activity levels to understand engagement patterns.

Company Intelligence: Uncover detailed company profiles through URLs or numeric\
IDs. Utilize web domains to find companies and access their latest LinkedIn\
posts for a wealth of corporate insights.

LinkedIn Sales Navigator Automation: Elevate your prospecting capabilities with\
our API's fully automated LinkedIn Sales Navigator searches, requiring no \
direct\
account connection. This breakthrough feature allows you to utilize the\
sophisticated filtering of Sales Navigator to perform detailed searches for\
employees and companies, all automated and integrated seamlessly into your\
workflows. With this advanced functionality, you can execute targeted searches\
without the need for manual input or even accessing a Sales Navigator account\
yourself. Our API's automation unlocks a new level of efficiency and precision\
in identifying high-value prospects, streamlining your lead acquisition process\
like never before.

Job Market Trends: Navigate the job landscape with tailored searches. Obtain\
specific job details directly from LinkedIn to stay ahead in the competitive \
job market.

Your Gateway to Real-Time LinkedIn Data

Our API stands out by providing real-time data scraping capabilities, enabling\
you to make informed decisions swiftly. Whether for market research, lead\
generation, or competitive analysis, our tool empowers you with the data you\
need, when you need it.

Embrace the future of data intelligence with our LinkedIn Scraping API, trusted\
by innovators and leaders worldwide.
''',
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation='''
https://rapidapi.com/freshdata-freshdata-default/api/fresh-linkedin-profile-dat\
a/tutorials/how-to-find-a-geo_code-(geoid)-on-linkedin%3F''',
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="https://rapidapi.com/freshdata"
                                    "-freshdata-default/api/fresh-linkedin-"
                                    "profile-data/tutorials/how-to-find-a-title"
                                    "_id-on-linkedin%3F",
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="https://rapidapi.com/freshdata-freshdata-"
                                    "default/api/fresh-linkedin-profile-data/"
                                    "tutorials/how-to-find-a-function_id-on-"
                                    "linkedin%3F",
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="https://rapidapi.com/freshdata-freshdata-"
                                    "default/api/fresh-linkedin-profile-data/"
                                    "tutorials/how-to-find-a-company_id-on-"
                                    "linkedin%3F",
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="https://rapidapi.com/freshdata-freshdata-"
                                    "default/api/fresh-linkedin-profile-data/"
                                    "tutorials/how-to-find-a-zipcode_id-on-lin"
                                    "kedin%3F",
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="https://rapidapi.com/freshdata-freshdata-"
                                    "default/api/fresh-linkedin-profile-data/"
                                    "tutorials/find-ids-being-used-in-the-endp"
                                    "oint-%22find-custom-headcount%22",
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="https://rapidapi.com/freshdata-freshdata-"
                                    "default/api/fresh-linkedin-profile-data/t"
                                    "utorials/search-posts-payload-references",
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="https://rapidapi.com/freshdata-freshdata-"
                                    "default/api/fresh-linkedin-profile-data/t"
                                    "utorials/search-employees-endpoint-payloa"
                                    "d-references",
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="https://rapidapi.com/freshdata-freshdata-"
                                    "default/api/fresh-linkedin-profile-data/tu"
                                    "torials/sample-python-code-for-search-empl"
                                    "oyees-endpoint-1",
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "about": "I'm CJ, Professor of Real Estate at Schack Institute and a Founder of NOYACK, a financial education company impacting the lives of young investors everywhere through financial education, community and universal access to private markets.\n\nI am the son of Italian immigrants,  my father a highly decorated NYFD Fireman who then built one of the largest municipal building companies in New York City. Nancy Reagan gave him an award for his projects. At 16 my father had a stroke and I gave up my dream of playing in the NHL (yeah, right) to manage the family business which I knew nothing about.\n\nThat started a 40 year journey of educating myself through thousands of hours of reading and painful mistakes. But it also turned out to be my life's mission and I wish everyone finds they're purpose and is able to pusue it . I am doing this as a financial educator of young investors after a pretty successful career as the Chief Investment Officer of a nine family investing syndicate; my track record over 30 years doing this is  23% average annual returns.  We invested in: commercial real estate, media IP,  early stage venture capital, private credit, fine art and consumer packaged goods. \n\nThe COVID pandemic was a wake up call  for me to create a more lasting legacy than just money; helping others by providing so I founded NOYACK to educate and mentor  Millennials & Gen Z as they inherit are inheriting $4.4 trillion by 2025 and $39.4 trillion by 2045 - The Great Wealth Transfer How will they make decisions for their future? NOYACK's mission is all about creating a new kind of next-gen investment culture, bringing people together in a community space for young investors to learn, explore, and invest in private markets. \n\nNOYACK and our Noyack Private Investing Club  is becoming a hub, a home, a safe space to learn, interact and access this valuable world of private markets.\n\nI built this for the 19 year old me, CJ, who had no one to ask for help or any place to learn about private investments or a community of like-minded investors and peers with similar interests at a similar place in their lives. My goal is to teach members to fish for themselves so they can build generational wealth. Whether they’re looking to make a small investment or have just inherited a family nest egg they need to protect - we’re here to transform their lives, their kid’s lives and if all goes as planned, their kid’s kid’s lives.\n\nCome join the wealth revolution to end economic inequality - we don't have to do this, we are lucky enough to get to be able to do this. #AccessGranted",
            "certifications": [
              {
                "authority": "Harvard Business School",
                "issued": "Sep 1993 · Expired Jun 1994",
                "name": "Portfolio Management Professional (PfMP)",
                "url": null
              }
            ],
            "city": "New York",
            "company": "NYU Schack Institute of Real Estate",
            "company_domain": "sps.nyu.edu",
            "company_employee_range": "51 - 200",
            "company_industry": "Higher Education",
            "company_linkedin_url": "https://www.linkedin.com/school/nyuschack/",
            "company_logo_url": "https://media.licdn.com/dms/image/D4E0BAQHmAl7S-DjtKw/company-logo_400_400/0/1689884074014/nyuschack_logo?e=1724284800&v=beta&t=C68jN4Z7pBw4JXr5Syjdx50oLQt4ptcFMEeWqjMEwXU",
            "company_website": "http://www.sps.nyu.edu/schack",
            "company_year_founded": 1967,
            "connections_count": 500,
            "country": "United States",
            "courses": [],
            "current_company_join_month": 4,
            "current_company_join_year": 2024,
            "educations": [
              {
                "activities": "",
                "date_range": "",
                "degree": "Executive Management Program",
                "description": "",
                "eduId": 98366433,
                "end_month": "",
                "end_year": "",
                "field_of_study": "",
                "grade": "",
                "school": "Harvard Business School",
                "school_id": "4867",
                "school_linkedin_url": "https://www.linkedin.com/company/4867/",
                "start_month": "",
                "start_year": ""
              },
              {
                "activities": "",
                "date_range": "",
                "degree": "GC",
                "description": "",
                "eduId": 22899893,
                "end_month": "",
                "end_year": "",
                "field_of_study": "Game Theory And Econometrics",
                "grade": "",
                "school": "London School of Economics and Political Science",
                "school_id": "6544",
                "school_linkedin_url": "https://www.linkedin.com/company/6544/",
                "start_month": "",
                "start_year": ""
              },
              {
                "activities": "",
                "date_range": "",
                "degree": "Bachelor of Science (BS)",
                "description": "",
                "eduId": 112529037,
                "end_month": "",
                "end_year": "",
                "field_of_study": "Mathematical Statistics and Probability",
                "grade": "",
                "school": "Tufts University",
                "school_id": "157341",
                "school_linkedin_url": "https://www.linkedin.com/company/157341/",
                "start_month": "",
                "start_year": ""
              },
              {
                "activities": "",
                "date_range": "",
                "degree": "",
                "description": "",
                "eduId": 165965205,
                "end_month": "",
                "end_year": "",
                "field_of_study": "Classics and Classical Languages, Literatures, and Linguistics",
                "grade": "",
                "school": "Fordham Preparatory",
                "school_id": "",
                "school_linkedin_url": "",
                "start_month": "",
                "start_year": ""
              }
            ],
            "email": "",
            "experiences": [
              {
                "company": "NYU Schack Institute of Real Estate",
                "company_id": "11128202",
                "company_linkedin_url": "https://www.linkedin.com/company/11128202",
                "company_public_url": "https://www.linkedin.com/school/nyuschack/",
                "current_company_join_month": 4,
                "current_company_join_year": 2024,
                "date_range": "Apr 2024 - present",
                "description": "I teach in the NYU Masters Program specifically about Real Estate Investment Trusts, Financing and Investment",
                "duration": "2 mos",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "New York City Metropolitan Area",
                "start_month": 4,
                "start_year": 2024,
                "title": "Professor of Real Estate"
              },
              {
                "company": "Noyack Capital",
                "company_id": "",
                "company_linkedin_url": "",
                "company_public_url": null,
                "date_range": "1988 - present",
                "description": "I am the  Chief Investment Officer of a nine UNHW family alternative investment allocator. NOYACK allocated to  commercial real estate, seed VC, consumer packaged goods, and opportunistic special situations.",
                "duration": "36 yrs 5 mos",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "New York City Metropolitan Area",
                "start_month": "",
                "start_year": 1988,
                "title": "Chief Investment Officer of MultiFamily Office"
              },
              {
                "company": "NOYACK Wealth Club",
                "company_id": "321778",
                "company_linkedin_url": "https://www.linkedin.com/company/321778",
                "company_public_url": "https://www.linkedin.com/company/wearenoyack",
                "date_range": "2022 - present",
                "description": "NOYACK (weareNOYACK.com)is a fast-growing financial education startup that is the only membership club for Millennial, Gen Z, Gen Alpha learn, interact, and invest in private markets.\nNOYACK provides online masterclasses, live events, mentorship, research and private investment offeringssimilar to those reserved for sovereign wealth institutions and billionaires. NOYACK is creating a massive impact through financial literacy educating the future inheritors of The Great Wealth Transfer - $42 trillion by 2040 - the largest wealth transfer in the history of our planet. NOYACK launched only 4 months ago and already built an audience of over 300K strong!   Education, community and access is our product | integrity, innovation, transparency, and inclusivity are our beliefs.\n-that's what we believe in, that's who we are. We are NOYACK...and so are you. #AccessGranted",
                "duration": "2 yrs 5 mos",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "NYC",
                "start_month": "",
                "start_year": 2022,
                "title": "Founder & CEO"
              },
              {
                "company": "Noyack Alternative Investments",
                "company_id": "100329260",
                "company_linkedin_url": "https://www.linkedin.com/company/100329260",
                "company_public_url": null,
                "date_range": "2022 - present",
                "description": "NOYACK is revolutionizing self-directed wealth management  by making world-class private investments accessible to all investors, not just the institutions. At our core is a commitment to financial education and technological innovation, empowering individuals with the knowledge to invest like billionaires. It’s not about quick returns or cashing out. It’s about making smart financial decisions for your future. Our goal is to teach members to fish for themselves so they can build generational wealth. Whether they’re looking to make a small investment or have just inherited a family nest egg they need to protect - we’re here to transform their lives, their kid’s lives and if all goes as planned, their kid’s kid’s lives.\nNOYACK is all about creating a new kind of wealth management culture; one that doesn't lead with transaction but brings people together in a community space for young investors to learn, connect and generate wealth through private investing. Financial literacy AND access as social impact. We want to open up that door and give access to the powerful world of Private Investments.\n\nCome with us, to the room where it all happens. \n\nWe are Noyack.\nAnd so are you.  \nAccessGranted.™",
                "duration": "2 yrs 5 mos",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "New York City Metropolitan Area",
                "start_month": "",
                "start_year": 2022,
                "title": "Managing Partner & Chief Investment Officer"
              },
              {
                "company": "SpaceX",
                "company_id": "30846",
                "company_linkedin_url": "https://www.linkedin.com/company/30846",
                "company_public_url": "https://www.linkedin.com/company/spacex",
                "date_range": "2020 - present",
                "description": "",
                "duration": "4 yrs 5 mos",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "Hawthorne, California, United States",
                "start_month": "",
                "start_year": 2020,
                "title": "Seed Investor"
              },
              {
                "company": "Nalu Bio ",
                "company_id": "37248677",
                "company_linkedin_url": "https://www.linkedin.com/company/37248677",
                "company_public_url": "https://www.linkedin.com/company/nalu-bio",
                "date_range": "Jan 2021 - present",
                "description": "",
                "duration": "3 yrs 5 mos",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "New York City Metropolitan Area",
                "start_month": 1,
                "start_year": 2021,
                "title": "Pre-Seed Investor"
              },
              {
                "company": "Golden Seeds",
                "company_id": "313031",
                "company_linkedin_url": "https://www.linkedin.com/company/313031",
                "company_public_url": "https://www.linkedin.com/company/goldenseeds",
                "date_range": "2019 - present",
                "description": "50% of the U.S. population are women. 42% of entrepreneurial ventures are women-owned. Since our founding in 2005, we have been propelled to identify promising women entrepreneurs, to support their growth, and to better align these ratios to create value through the breakthrough ideas and tenaciousness of women entrepreneurs. Women are starting businesses at record levels, with the ideas, skills and talents to build great companies.  Golden Seeds, one of the nation’s largest and most active early-stage investment groups, focuses squarely on female founders. Our investment thesis rests on extensive research with a compelling conclusion: gender diverse teams produce better return on equity. By seeking companies where women hold leadership positions and own substantial equity, we fund companies likely to have diverse perspectives that will contribute to ultimate success.\nGolden Seeds members have invested over $140 million in over 200 exciting women-led companies … and counting. Headquartered in New York City, Golden Seeds has chapters in Arizona, Atlanta, Boston, Dallas, Houston, New Jersey, New York and Silicon Valley",
                "duration": "5 yrs 5 mos",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "New York City Metropolitan Area",
                "start_month": "",
                "start_year": 2019,
                "title": "Early Stage Investor"
              },
              {
                "company": "IMMINENT",
                "company_id": "6609201",
                "company_linkedin_url": "https://www.linkedin.com/company/6609201",
                "company_public_url": null,
                "date_range": "2014 - 2019",
                "description": "SUCCESSFUL 7X EXIT FOR OUR INVESTORS! \n\nWe have a big idea - an operating system with everything you need in one place to get your employees more engaged. We believe workforce productivity begins with purpose.\n\nSo it is our mission to create technology and content that harnesses employees' passion for doing good while also providing them with resources they need to stay healthy. Finally, we want to support employees by providing them the information that they need as well as a social environment where they can be heard.\n\nIntroducing OAHU- IMMINENT's holistic approach to workforce wellbeing. Giving  + Habitat + Wellbeing + Social = Inspired.  We assist Fortune 1000 companies & brands to achieve amazing workforce goals by treating their employees as their first customers.\nEmployee360™ is a simple, yet powerful employee engagement portal that streamlines the onboarding process to engage employees and galvanize their passion to get involved. We provide state-of-the-art software tools to improve bi-directional workplace communication. We identify social impact movements, successful non-profits or non-governmental organizations around which to create holistic CSR campaigns. And we produce or curate employee-created video stories, immersive or full VR, that enable progressive brands to build truly authentic relationships with their employees and customers alike. \n\nFinally, our integrated social toolkit enables the marketing department to distribute the original content or their curated employee stories to a highly targeted audience informed by proprietary data insights. \n\nHappiness, productivity, volunteering, sharing... that’s why we feel IMMINENT offers a better way for companies to achieve 360-degree wellbeing. That’s what we believe in. That’s what drives us. That’s our cause.\n \nIn the world of doing good, the future is IMMINENT.",
                "duration": "5 yrs",
                "end_month": "",
                "end_year": 2019,
                "is_current": false,
                "location": "United States",
                "start_month": "",
                "start_year": 2014,
                "title": "Founder & CEO"
              },
              {
                "company": "Economic Innovation Group",
                "company_id": "9357069",
                "company_linkedin_url": "https://www.linkedin.com/company/9357069",
                "company_public_url": "https://www.linkedin.com/company/economicinnovationgroup",
                "date_range": "2016 - 2018",
                "description": "Founded by Sean Parker, John Lettieri, and Steve Glickman, EIG is a bipartisan public policy organization that combines innovative research and data-driven advocacy to address America’s most pressing economic challenges. From our headquarters in the nation’s capital, EIG convenes leading experts from the public and private sectors, develops original research, and advances creative policy proposals that bring new jobs, investment, and economic dynamism to U.S. communities.",
                "duration": "2 yrs",
                "end_month": "",
                "end_year": 2018,
                "is_current": false,
                "location": "Washington D.C. Metro Area",
                "start_month": "",
                "start_year": 2016,
                "title": "Member Of The Board Of Advisors"
              },
              {
                "company": "Ten Paces Media",
                "company_id": "1948038",
                "company_linkedin_url": "https://www.linkedin.com/company/1948038",
                "company_public_url": null,
                "date_range": "1994 - 2015",
                "description": "Oscar-winning producer (Slingblade) and head of studios. Builder and investor in physical  studio infrastructure as well as SVOD, immersive video (VR/AR/360°). Created subsidiary to build content IP library & publishing.",
                "duration": "21 yrs",
                "end_month": "",
                "end_year": 2015,
                "is_current": false,
                "location": "NYC",
                "start_month": "",
                "start_year": 1994,
                "title": "Executive Producer"
              },
              {
                "company": "Gun For Hire Digital Studios",
                "company_id": "",
                "company_linkedin_url": "",
                "company_public_url": null,
                "date_range": "1997 - 2003",
                "description": "Mr. Follini served as CEO of the Gun For Hire Media Studios, the largest digital production facility in New York from 1996 - 2001. He conceived, designed, and supervised construction of all of Gun For Hire’s 400,000+ square feet of digital media centers in New York, Miami, Vancouver, Toronto and Los Angeles. His New York facility earned the 1998 Crain’s Magazine Small Business Award.",
                "duration": "6 yrs",
                "end_month": "",
                "end_year": 2003,
                "is_current": false,
                "location": "NYC, Miami, Toronto, Vancouver, Los Angeles",
                "start_month": "",
                "start_year": 1997,
                "title": "CEO"
              },
              {
                "company": "Shooting Gallery Films",
                "company_id": "",
                "company_linkedin_url": "",
                "company_public_url": null,
                "date_range": "Sep 1993 - 2003",
                "description": "Producer of several award-winning films & digital media content",
                "duration": "9 yrs 5 mos",
                "end_month": "",
                "end_year": 2003,
                "is_current": false,
                "location": "NYC",
                "start_month": 9,
                "start_year": 1993,
                "title": "Principle & Oscar-winning Producer"
              },
              {
                "company": "Blackstone",
                "company_id": "7834",
                "company_linkedin_url": "https://www.linkedin.com/company/7834",
                "company_public_url": "https://www.linkedin.com/company/blackstonegroup",
                "date_range": "1988 - 1993",
                "description": "",
                "duration": "5 yrs",
                "end_month": "",
                "end_year": 1993,
                "is_current": false,
                "location": "New York City Metropolitan Area",
                "start_month": "",
                "start_year": 1988,
                "title": "Associate"
              }
            ],
            "first_name": "CJ",
            "followers_count": 14648,
            "full_name": "CJ Follini",
            "headline": "NYU Professor of Real estate | CIO & Multi-Family Office Allocator |  #AlternativeInvestment Expert | Board Member | Publisher of #1 Subscribed Newsletter | #FinancialEducation Nonprofit | Public Speaker | Proud dad",
            "honors_and_awards": [
              {
                "associated": "Associated with NOYACK Wealth Club",
                "date": "Sep 2021",
                "description": "We at GLOBEST has selected our annual group of power players and influencers in the industrial RE sector. As always the selection was based on accomplishments and peer reviews.",
                "issuer": "GLOBEST",
                "title": "GlobeSt Industrial Influencer of 2021"
              },
              {
                "associated": "Associated with IMMINENT",
                "date": "Sep 2016",
                "description": "The Future of Employee Engagement and Inside-Out Marketing\n\nThe Fortune 500 alone has 27 million employees with an average social reach of 846 people. 40% of these Fortune 500 companies will not survive by 2022 without significant employee engagement initiatives. Increasingly, corporate culture is influencing marketing and the environment a company creates for its workforce is affecting the bottom line. Hear from thought leaders about the latest ideas, VR content technology & software infrastructure available to attract, retain and motivate employees to become brand evangelists.",
                "issuer": "AdvertisingWeek",
                "title": "Moderator & Speaker - AdvertisingWeek"
              },
              {
                "associated": null,
                "date": "Jun 2014",
                "description": null,
                "issuer": "HERE Arts Center",
                "title": "HEREmanitarian Award"
              },
              {
                "associated": "Associated with Ten Paces Media",
                "date": "Jan 2008",
                "description": "Executive Producer",
                "issuer": "Pare Lorentz Award",
                "title": "Best Documentary"
              },
              {
                "associated": "Associated with Ten Paces Media",
                "date": "Dec 2002",
                "description": null,
                "issuer": "SlamDance Film Festival",
                "title": "Best Short Film"
              },
              {
                "associated": "Associated with Ten Paces Media",
                "date": "Dec 2002",
                "description": null,
                "issuer": "Rotterdam Film Festival",
                "title": "Best Short Film - \" Bullet in the Brain\""
              },
              {
                "associated": "Associated with Ten Paces Media",
                "date": "Nov 2002",
                "description": null,
                "issuer": "GenArt Film Festival",
                "title": "Best Narrative Short Film"
              },
              {
                "associated": "Associated with Ten Paces Media",
                "date": "Feb 2001",
                "description": "The Chrysler Million Dollar Film Festival is a partnership between Chrysler, Hypnotic and Universal Pictures, and is one of the largest branded entertainment campaigns.",
                "issuer": "Universal Studios",
                "title": "Winner of The Chrysler/Universal Studios Million Dollar Film Award"
              },
              {
                "associated": "Associated with Gun For Hire Digital Studios",
                "date": "Sep 1999",
                "description": null,
                "issuer": "MediaPost",
                "title": "Rising Stars in New Media"
              },
              {
                "associated": "Associated with Shooting Gallery Films",
                "date": "Mar 1999",
                "description": null,
                "issuer": "Toronto Film Commission",
                "title": "40 Under 40 Media Executives To watch"
              },
              {
                "associated": "Associated with Gun For Hire Digital Studios",
                "date": "Jan 1998",
                "description": "The precursor to the current Top Entrepreneurs Award",
                "issuer": "CrainsNY",
                "title": "Best Small Business Award"
              },
              {
                "associated": "Associated with Shooting Gallery Films",
                "date": "Feb 1996",
                "description": null,
                "issuer": "Academy of Motion Picture Arts and Sciences",
                "title": "Academy Award for Best Adapted Screenplay"
              }
            ],
            "hq_city": "New York",
            "hq_country": "US",
            "hq_region": "NY",
            "job_title": "Professor of Real Estate",
            "languages": "Italian, Spanish",
            "last_name": "Follini",
            "linkedin_url": "https://www.linkedin.com/in/cjfollini",
            "location": "New York, New York, United States",
            "organizations": [
              {
                "associated": "Associated with IMMINENT",
                "date_range": "Nov 2015 - Present",
                "description": null,
                "name": "Mobile Marketing Association"
              },
              {
                "associated": "Associated with IMMINENT",
                "date_range": "Oct 2015 - Present",
                "description": null,
                "name": "Interactive Advertising Bureau"
              },
              {
                "associated": "Associated with Ten Paces Media",
                "date_range": "Jun 2015 - Present",
                "description": "http://www.imdb.com/name/nm1202656/",
                "name": "Producers Guild of America"
              }
            ],
            "patents": [],
            "phone": "",
            "profile_id": "26902278",
            "profile_image_url": "https://media.licdn.com/dms/image/D4E03AQGbJVJnATuprA/profile-displayphoto-shrink_800_800/0/1702576825399?e=1721865600&v=beta&t=r74_ZJruN-pR_lRw7hWdR3c9F-ZKrhcAbkMcVOxtUTI",
            "projects": [],
            "public_id": "cjfollini",
            "publications": [
              {
                "date": "Sep 10, 2016",
                "description": "What if your firm could attract, retain, and engage the world's best talent? What if you could empower your workforce on every level toward emotional, spiritual, physical, and professional growth? And what if your employees were inspired to become active brand evangelists reaching millions of people with just one click? Understanding these possibilities begins by defining employee engagement and cause marketing to identify their powerful nexus.",
                "link": "https://imminentdigital.com/paper",
                "publisher": "IMMINENT",
                "title": "The Customer Within: The Power of Employee Engagement And Inside-Out Marketing"
              },
              {
                "date": "Jul 29, 2016",
                "description": "How far can VR go in reshaping marketing? More specifically, can brands get their staffers to evangelize for their employers more authentically thanks to VR? It's an interesting question, and Imminent Digital—which specializes in video marketing programs—believes it can take corporate evangelism to a more immersive, impactful level.",
                "link": "http://www.adweek.com/news/technology/why-virtual-reality-could-inspire-more-impactful-and-emotional-employee-evangelism-172728",
                "publisher": "Adweek",
                "title": "Why Virtual Reality Could Inspire More Impactful and Emotional Employee Evangelism | Imminent has major brands intrigued"
              },
              {
                "date": "Jun 16, 2014",
                "description": null,
                "link": "http://www.broadwayworld.com/article/HERE-Hosts-Interstellar-Gala-Honoring-Anita-Contini-and-CJ-Follini-Tonight-20140616",
                "publisher": "Broadway World",
                "title": "HERE Hosts Interstellar Gala, Honoring CJ Follini"
              },
              {
                "date": "May 19, 2011",
                "description": null,
                "link": "http://blackswanzine.com/2010/05/19/noyack-medical-partners-forming-200-million-fund-for-to-invest-in-distressed-%E2%80%9Chess%E2%80%9D-opps-%E2%80%93-healthcare-student-housing-and-self-storage/",
                "publisher": "Blackswanzine.com",
                "title": "Noyack Medical Partners Forming $200 Million Fund to Invest in Alt-Real Estate"
              }
            ],
            "school": "Harvard Business School",
            "skills": "On-camera Interviewing|Teaching|Executive Management|Integrated Marketing|Crowdfunding|Financial Analysis|Equity Capital Markets|Distressed Debt|Film Production|Independent Film|New Media|Portfolio Management|Startups|Employee Engagement|Digital Media|Private Equity|Venture Capital|Start-ups|Film|Television|Media Production|Mobile Marketing|Content Marketing|Mobile Advertising|Content Strategy|Advertising|Content Development|Entrepreneurship|Strategy|Mobile Devices|Marketing|Real Estate Transactions|Commercial Real Estate|Investment Strategies|Investment Management|investment|Business Development|Public Speaking|Strategic Partnerships|Management|Angel Investing|Sponsorship Sales|Social Networking|Branded Content|Multi-platform Content Strategy|On-camera Host|Real Estate Investment Trust (REIT)|Real Estate Private Equity|Start-up Ventures|Corporate Venture Capital|Real Estate|Early-stage Startups|Leadership|Venture Financing|Alternative Investments|Early Stage Companies|Cold Storage|Mobility Strategy|Industrial |Supply Chain Management|Infrastructure as a Service (IaaS)",
            "state": "New York",
            "urn": "ACoAAAGafwYBi3pXOoVVwIyAFc453DuIv50jfTA",
            "volunteers": [
              {
                "company": "HERE Arts Center",
                "company_linkedin_url": "https://www.linkedin.com/company/2251752/",
                "date_range": "Jan 2007 - Jun 2014",
                "description": "HERE builds a community that nurtures career artists as they create innovative hybrid live performance in theatre, dance, music, puppetry, media and visual art. Best transmedia theater in New York City",
                "duration": "7 yrs 6 mos",
                "title": "Board Chairman",
                "topic": null
              },
              {
                "company": "Bay Street Theatre",
                "company_linkedin_url": "https://www.linkedin.com/company/405942/",
                "date_range": "Aug 2021 - Present",
                "description": "Bay Street Theater & the Sag Harbor Center For The Arts is a year-round, not-for-profit professional theater and community cultural center which endeavors to innovate, educate, and entertain a diverse community through the practice of the performing arts. We serve as a social and cultural gathering place, an educational resource, and a home for a community of artists.",
                "duration": "2 yrs 10 mos",
                "title": "Member Board Of Directors",
                "topic": "Arts and Culture"
              },
              {
                "company": "Chashama",
                "company_linkedin_url": "https://www.linkedin.com/company/1613546/",
                "date_range": "Jan 2013 - Dec 2016",
                "description": "chashama supports communities by transforming temporarily vacant properties into spaces where artists can flourish. By recycling and repurposing buildings in transition, we invest in neighborhoods, foster local talent, and sustain a vast range of creativity, commerce and culture. chashama is a 501(c)(3) nonprofit.",
                "duration": "4 yrs",
                "title": "Board Member",
                "topic": "Arts and Culture"
              },
              {
                "company": "Private Equity & Alternative Asset Investment",
                "company_linkedin_url": null,
                "date_range": "Jan 2017 - Present",
                "description": "#IMN & #Opalgroup",
                "duration": "7 yrs 5 mos",
                "title": "Public Speaker & Panel Moderator",
                "topic": "Education"
              }
            ]
          },
          "message": "ok"
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Profile's Posts
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-profile-posts') and
            i.nice_name == "Get Profile's Posts")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": [
            {
              "images": [],
              "num_appreciations": 1,
              "num_comments": 45,
              "num_empathy": 2,
              "num_interests": 8,
              "num_likes": 136,
              "num_reposts": 17,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133709424296165377/",
              "reshared": false,
              "text": "📍Do you want to make your presentations with Al magic using ChatGPT just in Minutes💥\n\n📍Unlock the untapped power of Al in your presentations with ChatGPT and transform them into masterpieces that captivate and inspire.\n\n📍Harness ChatGPT's creative genius to brainstorm fresh ideas, craft engaging content, and select stunning visuals that will elevate your presentations to new heights.\n\n💥Experience the seamless flow of content and captivating slide layouts that ChatGPT helps you create, leaving your audience mesmerized from start to finish.\n\n📍Embrace the future of presentations with ChatGPT and watch your audience's jaws drop.\n\n🎉And Follow Vijay Chollangi 🛡  For More Al tools stay tuned with me\n\nVC-Respective Creator\n\n #Alpresentations #ChatGPT #powerpoint #presentationmagic #aitools ",
              "time": "4h",
              "urn": "7133709424296165377",
              "video": {
                "duration": 51400,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQEACEREwfcYgA/feedshare-ambry-analyzed_servable_progressive_video/0/1700796656388?e=1701417600&v=beta&t=8fHfRtgXo83IpbsO26QWT7f23N3MJhMDpEhr4KAhF_M"
              }
            },
            {
              "images": [],
              "num_appreciations": 8,
              "num_comments": 68,
              "num_empathy": 17,
              "num_interests": 6,
              "num_likes": 576,
              "num_praises": 3,
              "num_reposts": 53,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133709401093283841/",
              "reshared": false,
              "text": "📍IT Companies in India.🎉💥\n\nApply here directly: (Share and comment for better reach)\n\n📍Company Career page Links:\n\n📍Google: https://lnkd.in/dKsmuXfh\n\n📍Amazon: https://lnkd.in/diJJqyr3\n\n📍intel: https://lnkd.in/d-QWtEfm\n\n📍Microsoft: https://lnkd.in/dTxGD7cy\n\n📍Mastercard: https://lnkd.in/dB83H-Jb\n\n📍nVIDIA: https://lnkd.in/dczs5y6d\n\n📍HARMAN: https://lnkd.in/dGr2bJiB\n\n📍Myntra: https://lnkd.in/d5NXB3Sw\n\n📍Flipkart: https://lnkd.in/dXR-mxQN\n\n📍Shell: https://lnkd.in/dzJiiFdF\n\n📍Siemens: https://lnkd.in/dDmAxYa6\n\n📍IBM: https://lnkd.in/d5QQgu7K\n\n📍Gap Inc: https://lnkd.in/dGyaAHRe\n\n📍Adobe: https://lnkd.in/d9jAyH4F\n\n📍Nike: https://lnkd.in/dxkGKZJi\n\n📍Moodys: https://lnkd.in/dm_u8S2r\n\n📍Mountblue: https://lnkd.in/dmivq6Zi\n\n📍Zycus: https://lnkd.in/gxUPvqxh\n\n📍Appypie: https://lnkd.in/gyScNsqj\n\n📍Tata Technologies: https://lnkd.in/d745BKSW\n\n📍Trimble: https://lnkd.in/dYHrXxnP\n\n📍Forcepoint: https://lnkd.in/dpebxvMN\n\n📍Siemens: https://lnkd.in/dWcE87ih\n\n📍DXC Technology: https://lnkd.in/ddWkRdCb\n\n📍BT Group: https://lnkd.in/d9zzwsav\n\n📍Ziplr: https://lnkd.in/dipniyrk\n\n📍Volvo: https://lnkd.in/dgfyUDwM\n\n📍ECI: https://lnkd.in/dRenRqFH\n\n📍Zoho: https://lnkd.in/dE5sE4-4\n\n📍Oracle: https://lnkd.in/d65KpPNq\n\n📍Morgan Stanley: https://lnkd.in/dxZkxkDx\n\n📍MoEngage: https://lnkd.in/dJQ9f55P\n\n📍JPMorgan: https://lnkd.in/d5q8E8x5\n\n📍Publicis Sapient: https://lnkd.in/dP8bjEcP\n\n📍Practo: https://lnkd.in/drTghJ9i\n\n📍Boston Consulting Group: https://lnkd.in/da7tUq6X\n\n📍PayPal: https://lnkd.in/dBadunAQ\n\n📍ABB: https://lnkd.in/d9H3xNcQ\n\n📍Mercedes Benz: https://lnkd.in/d9xY8Jak\n\n📍Tiger Analytics: https://lnkd.in/dR8uxR2P\n\n📍HP: https://lnkd.in/dJGUZHRS\n\n📍NetApp: https://lnkd.in/dPgQMsxr\n\n📍Airbus: https://lnkd.in/d9q_FKGg\n\n📍Phenom: https://lnkd.in/de57miGs\n\n📍Autodesk: https://lnkd.in/djGBv9Xg\n\n📍Salesforce: https://lnkd.in/dejdyvrW\n\n📍Goldman Sachs: https://lnkd.in/d4ak78sV\n\n📍Hexagon: https://lnkd.in/diZHrDEF\n\n📍Cisco: https://lnkd.in/dxDXGG_f\n\n📍Deutsche Bank: https://lnkd.in/dkq3dWhU\n\n📍Motorola: https://lnkd.in/d7hydH7n\n\n📍Renault: https://lnkd.in/dxSXFzW5\n\n📍SAP: https://lnkd.in/dcSqU5jb Societe\n\n📍 Generale: https://lnkd.in/dFXdCZFJ\n\n📍Atlassians: https://lnkd.in/dqtjnJcE\n\n📍Netflix: https://lnkd.in/d93NecpY\n\n📍Nissan: https://lnkd.in/dgAtM8_W\n\n📍Accenture: https://lnkd.in/dSm_JtF\n\n 📍Dell: https://lnkd.in/dutdNS8E\n\nFor more such information content follow Vijay Chollangi 🛡 \n\n#itcompany #indiajobs #companies #jobshiring #google ",
              "time": "2d",
              "urn": "7133709401093283841",
              "video": {
                "duration": 32000,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4E05AQGx3zPr4bsdww/feedshare-ambry-analyzed_servable_progressive_video/0/1700559190812?e=1701417600&v=beta&t=0qZPc6ODB5p_4zcPibI4_NJI5Si5WBq_FCgJ5cojaEk"
              }
            },
            {
              "images": [],
              "num_appreciations": 1,
              "num_comments": 45,
              "num_empathy": 2,
              "num_interests": 8,
              "num_likes": 136,
              "num_reposts": 17,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133679786110980096/",
              "reshared": false,
              "text": "📍Do you want to make your presentations with Al magic using ChatGPT just in Minutes💥\n\n📍Unlock the untapped power of Al in your presentations with ChatGPT and transform them into masterpieces that captivate and inspire.\n\n📍Harness ChatGPT's creative genius to brainstorm fresh ideas, craft engaging content, and select stunning visuals that will elevate your presentations to new heights.\n\n💥Experience the seamless flow of content and captivating slide layouts that ChatGPT helps you create, leaving your audience mesmerized from start to finish.\n\n📍Embrace the future of presentations with ChatGPT and watch your audience's jaws drop.\n\n🎉And Follow Vijay Chollangi 🛡  For More Al tools stay tuned with me\n\nVC-Respective Creator\n\n #Alpresentations #ChatGPT #powerpoint #presentationmagic #aitools ",
              "time": "4h",
              "urn": "7133679786110980096",
              "video": {
                "duration": 51400,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQEACEREwfcYgA/feedshare-ambry-analyzed_servable_progressive_video/0/1700796656388?e=1701417600&v=beta&t=8fHfRtgXo83IpbsO26QWT7f23N3MJhMDpEhr4KAhF_M"
              }
            },
            {
              "images": [],
              "num_appreciations": 1,
              "num_comments": 45,
              "num_empathy": 2,
              "num_interests": 8,
              "num_likes": 136,
              "num_reposts": 17,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133658225505157120/",
              "reshared": false,
              "text": "📍Do you want to make your presentations with Al magic using ChatGPT just in Minutes💥\n\n📍Unlock the untapped power of Al in your presentations with ChatGPT and transform them into masterpieces that captivate and inspire.\n\n📍Harness ChatGPT's creative genius to brainstorm fresh ideas, craft engaging content, and select stunning visuals that will elevate your presentations to new heights.\n\n💥Experience the seamless flow of content and captivating slide layouts that ChatGPT helps you create, leaving your audience mesmerized from start to finish.\n\n📍Embrace the future of presentations with ChatGPT and watch your audience's jaws drop.\n\n🎉And Follow Vijay Chollangi 🛡  For More Al tools stay tuned with me\n\nVC-Respective Creator\n\n #Alpresentations #ChatGPT #powerpoint #presentationmagic #aitools ",
              "time": "4h",
              "urn": "7133658225505157120",
              "video": {
                "duration": 51400,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQEACEREwfcYgA/feedshare-ambry-analyzed_servable_progressive_video/0/1700796656388?e=1701417600&v=beta&t=8fHfRtgXo83IpbsO26QWT7f23N3MJhMDpEhr4KAhF_M"
              }
            },
            {
              "document": {
                "page_count": 9,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGBoHA1k6ak2Q/feedshare-document-url-metadata-scrapper-pdf/0/1700753313013?e=1701417600&v=beta&t=-uoAo8eq6_DmkAtagaLrssQ1UWke4V4nPFF0SwcNeRE"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 44,
              "num_empathy": 6,
              "num_interests": 13,
              "num_likes": 467,
              "num_praises": 1,
              "num_reposts": 74,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133654226928357377/",
              "reshared": false,
              "text": "📍Email Writing Tips💥\n\n📍Email is important for communication because it allows users to send information in letter format, and email can replace traditional mail options.\n\n📍Emails can be more beneficial for communication because they can often include text, documents and multimedia, like photos and videos.\n\n📍Like & Repost if you find this useful.\n\n📍Follow Vijay Chollangi 🛡  & Hit icon to get notifications for more such contents.\n\n#email #writing #communication\n\nCredit english. ingeneral ",
              "time": "16h",
              "urn": "7133654226928357377"
            },
            {
              "document": {
                "page_count": 10,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQELs19o11PbWQ/feedshare-document-url-metadata-scrapper-pdf/0/1700708410608?e=1701417600&v=beta&t=mCKPUhrQ6MXT8suT0crd7tgq5nv_SX4LDB7l3_IqD30"
              },
              "images": [],
              "num_appreciations": 4,
              "num_comments": 63,
              "num_empathy": 2,
              "num_interests": 6,
              "num_likes": 253,
              "num_praises": 1,
              "num_reposts": 30,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133654208171438080/",
              "reshared": false,
              "text": "💥Amazing Website's That Will Make You Smarter!!!💡\n\n📍Cogram is an artificial intelligence company based in Berlin. We're a global team, with backgrounds in machine learning, software engineering, physics, and psychology, and are working on a future where humans and computers share a common language\n\n📍Cogram Features\n\n📍Al team meeting transcription platform.\n\n📍Generate meeting minutes.\n\n📍Summarise your meetings.\n\n📍Assign action items.\n\n📍Customizable Meeting Insights.\n\n📍Seamless Integrations.\n\n #technology #techcommunity #educational #chatgpt #learningeveryday ",
              "time": "1d",
              "urn": "7133654208171438080"
            },
            {
              "document": {
                "page_count": 9,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGBoHA1k6ak2Q/feedshare-document-url-metadata-scrapper-pdf/0/1700753313013?e=1701417600&v=beta&t=-uoAo8eq6_DmkAtagaLrssQ1UWke4V4nPFF0SwcNeRE"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 44,
              "num_empathy": 6,
              "num_interests": 13,
              "num_likes": 467,
              "num_praises": 1,
              "num_reposts": 74,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133632146535043072/",
              "reshared": false,
              "text": "📍Email Writing Tips💥\n\n📍Email is important for communication because it allows users to send information in letter format, and email can replace traditional mail options.\n\n📍Emails can be more beneficial for communication because they can often include text, documents and multimedia, like photos and videos.\n\n📍Like & Repost if you find this useful.\n\n📍Follow Vijay Chollangi 🛡  & Hit icon to get notifications for more such contents.\n\n#email #writing #communication\n\nCredit english. ingeneral ",
              "time": "16h",
              "urn": "7133632146535043072"
            },
            {
              "document": {
                "page_count": 9,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGBoHA1k6ak2Q/feedshare-document-url-metadata-scrapper-pdf/0/1700753313013?e=1701417600&v=beta&t=-uoAo8eq6_DmkAtagaLrssQ1UWke4V4nPFF0SwcNeRE"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 44,
              "num_empathy": 6,
              "num_interests": 13,
              "num_likes": 467,
              "num_praises": 1,
              "num_reposts": 74,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133556882153119745/",
              "reshared": false,
              "text": "📍Email Writing Tips💥\n\n📍Email is important for communication because it allows users to send information in letter format, and email can replace traditional mail options.\n\n📍Emails can be more beneficial for communication because they can often include text, documents and multimedia, like photos and videos.\n\n📍Like & Repost if you find this useful.\n\n📍Follow Vijay Chollangi 🛡  & Hit icon to get notifications for more such contents.\n\n#email #writing #communication\n\nCredit english. ingeneral ",
              "time": "16h",
              "urn": "7133556882153119745"
            },
            {
              "document": {
                "page_count": 9,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGBoHA1k6ak2Q/feedshare-document-url-metadata-scrapper-pdf/0/1700753313013?e=1701417600&v=beta&t=-uoAo8eq6_DmkAtagaLrssQ1UWke4V4nPFF0SwcNeRE"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 44,
              "num_empathy": 6,
              "num_interests": 13,
              "num_likes": 467,
              "num_praises": 1,
              "num_reposts": 74,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133496995742187520/",
              "reshared": false,
              "text": "📍Email Writing Tips💥\n\n📍Email is important for communication because it allows users to send information in letter format, and email can replace traditional mail options.\n\n📍Emails can be more beneficial for communication because they can often include text, documents and multimedia, like photos and videos.\n\n📍Like & Repost if you find this useful.\n\n📍Follow Vijay Chollangi 🛡  & Hit icon to get notifications for more such contents.\n\n#email #writing #communication\n\nCredit english. ingeneral ",
              "time": "16h",
              "urn": "7133496995742187520"
            },
            {
              "document": {
                "page_count": 9,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGBoHA1k6ak2Q/feedshare-document-url-metadata-scrapper-pdf/0/1700753313013?e=1701417600&v=beta&t=-uoAo8eq6_DmkAtagaLrssQ1UWke4V4nPFF0SwcNeRE"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 44,
              "num_empathy": 6,
              "num_interests": 13,
              "num_likes": 467,
              "num_praises": 1,
              "num_reposts": 74,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133476456415838208/",
              "reshared": false,
              "text": "📍Email Writing Tips💥\n\n📍Email is important for communication because it allows users to send information in letter format, and email can replace traditional mail options.\n\n📍Emails can be more beneficial for communication because they can often include text, documents and multimedia, like photos and videos.\n\n📍Like & Repost if you find this useful.\n\n📍Follow Vijay Chollangi 🛡  & Hit icon to get notifications for more such contents.\n\n#email #writing #communication\n\nCredit english. ingeneral ",
              "time": "16h",
              "urn": "7133476456415838208"
            },
            {
              "images": [],
              "num_appreciations": 7,
              "num_comments": 45,
              "num_empathy": 3,
              "num_interests": 1,
              "num_likes": 216,
              "num_praises": 1,
              "num_reposts": 8,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133433851485327361/",
              "reshared": false,
              "text": "🤯The dawn of a new era!👊💥\n\n📍Humane Al Pin just hit the market at $699, aiming to be the next-gen iPhone.\n\n► Crafted by ex-Apple designers, it's the first consumer product built from the ground up with Al integration.\n\n📍Key Features:\n\n📍Internet connection with access to Microsoft and OpenAl's Al models.\n\n📍Designed for the breast pocket, offering voice-controlled email summaries, language translation, and calendar invites.\n\n📍Equipped with a camera and computer vision software for object recognition, like food labels.\n\n📍Projects an interactive interface onto surfaces like hands or tables.\n\n📍While it may not replace smartphones just yet, it's a sneak peek into the future of everyday Al.\n\nThe future of computing is becoming beautifully invisible.\n\nFollow for more Al insights  Vijay Chollangi 🛡 \n\n#aiinnovation #ai #future #techenthusiast ",
              "time": "21h",
              "urn": "7133433851485327361",
              "video": {
                "duration": 53133,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQH29MEhlf8Gpw/feedshare-ambry-analyzed_servable_progressive_video/0/1700732918345?e=1701417600&v=beta&t=LLpFPpjSlM0h5Hwq8gzoTu9jdEH2nh6U1ZNZyACKCpg"
              }
            },
            {
              "images": [],
              "num_appreciations": 7,
              "num_comments": 45,
              "num_empathy": 3,
              "num_interests": 1,
              "num_likes": 216,
              "num_praises": 1,
              "num_reposts": 8,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133428949618999298/",
              "reshared": false,
              "text": "🤯The dawn of a new era!👊💥\n\n📍Humane Al Pin just hit the market at $699, aiming to be the next-gen iPhone.\n\n► Crafted by ex-Apple designers, it's the first consumer product built from the ground up with Al integration.\n\n📍Key Features:\n\n📍Internet connection with access to Microsoft and OpenAl's Al models.\n\n📍Designed for the breast pocket, offering voice-controlled email summaries, language translation, and calendar invites.\n\n📍Equipped with a camera and computer vision software for object recognition, like food labels.\n\n📍Projects an interactive interface onto surfaces like hands or tables.\n\n📍While it may not replace smartphones just yet, it's a sneak peek into the future of everyday Al.\n\nThe future of computing is becoming beautifully invisible.\n\nFollow for more Al insights  Vijay Chollangi 🛡 \n\n#aiinnovation #ai #future #techenthusiast ",
              "time": "21h",
              "urn": "7133428949618999298",
              "video": {
                "duration": 53133,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQH29MEhlf8Gpw/feedshare-ambry-analyzed_servable_progressive_video/0/1700732918345?e=1701417600&v=beta&t=LLpFPpjSlM0h5Hwq8gzoTu9jdEH2nh6U1ZNZyACKCpg"
              }
            },
            {
              "images": [],
              "num_appreciations": 7,
              "num_comments": 45,
              "num_empathy": 3,
              "num_interests": 1,
              "num_likes": 216,
              "num_praises": 1,
              "num_reposts": 8,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133390888482832384/",
              "reshared": false,
              "text": "🤯The dawn of a new era!👊💥\n\n📍Humane Al Pin just hit the market at $699, aiming to be the next-gen iPhone.\n\n► Crafted by ex-Apple designers, it's the first consumer product built from the ground up with Al integration.\n\n📍Key Features:\n\n📍Internet connection with access to Microsoft and OpenAl's Al models.\n\n📍Designed for the breast pocket, offering voice-controlled email summaries, language translation, and calendar invites.\n\n📍Equipped with a camera and computer vision software for object recognition, like food labels.\n\n📍Projects an interactive interface onto surfaces like hands or tables.\n\n📍While it may not replace smartphones just yet, it's a sneak peek into the future of everyday Al.\n\nThe future of computing is becoming beautifully invisible.\n\nFollow for more Al insights  Vijay Chollangi 🛡 \n\n#aiinnovation #ai #future #techenthusiast ",
              "time": "21h",
              "urn": "7133390888482832384",
              "video": {
                "duration": 53133,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQH29MEhlf8Gpw/feedshare-ambry-analyzed_servable_progressive_video/0/1700732918345?e=1701417600&v=beta&t=LLpFPpjSlM0h5Hwq8gzoTu9jdEH2nh6U1ZNZyACKCpg"
              }
            },
            {
              "document": {
                "page_count": 10,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQELs19o11PbWQ/feedshare-document-url-metadata-scrapper-pdf/0/1700708410608?e=1701417600&v=beta&t=mCKPUhrQ6MXT8suT0crd7tgq5nv_SX4LDB7l3_IqD30"
              },
              "images": [],
              "num_appreciations": 4,
              "num_comments": 63,
              "num_empathy": 2,
              "num_interests": 6,
              "num_likes": 253,
              "num_praises": 1,
              "num_reposts": 30,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133388569078894592/",
              "reshared": false,
              "text": "💥Amazing Website's That Will Make You Smarter!!!💡\n\n📍Cogram is an artificial intelligence company based in Berlin. We're a global team, with backgrounds in machine learning, software engineering, physics, and psychology, and are working on a future where humans and computers share a common language\n\n📍Cogram Features\n\n📍Al team meeting transcription platform.\n\n📍Generate meeting minutes.\n\n📍Summarise your meetings.\n\n📍Assign action items.\n\n📍Customizable Meeting Insights.\n\n📍Seamless Integrations.\n\n #technology #techcommunity #educational #chatgpt #learningeveryday ",
              "time": "1d",
              "urn": "7133388569078894592"
            },
            {
              "document": {
                "page_count": 10,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQELs19o11PbWQ/feedshare-document-url-metadata-scrapper-pdf/0/1700708410608?e=1701417600&v=beta&t=mCKPUhrQ6MXT8suT0crd7tgq5nv_SX4LDB7l3_IqD30"
              },
              "images": [],
              "num_appreciations": 4,
              "num_comments": 63,
              "num_empathy": 2,
              "num_interests": 6,
              "num_likes": 253,
              "num_praises": 1,
              "num_reposts": 30,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133376886616850432/",
              "reshared": false,
              "text": "💥Amazing Website's That Will Make You Smarter!!!💡\n\n📍Cogram is an artificial intelligence company based in Berlin. We're a global team, with backgrounds in machine learning, software engineering, physics, and psychology, and are working on a future where humans and computers share a common language\n\n📍Cogram Features\n\n📍Al team meeting transcription platform.\n\n📍Generate meeting minutes.\n\n📍Summarise your meetings.\n\n📍Assign action items.\n\n📍Customizable Meeting Insights.\n\n📍Seamless Integrations.\n\n #technology #techcommunity #educational #chatgpt #learningeveryday ",
              "time": "1d",
              "urn": "7133376886616850432"
            },
            {
              "images": [],
              "num_appreciations": 2,
              "num_comments": 40,
              "num_interests": 2,
              "num_likes": 181,
              "num_praises": 1,
              "num_reposts": 12,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133376861597794304/",
              "reshared": false,
              "text": "💥If Your Resume is not getting shortlisted then try this Hack📍\n\n📍Land your dream job with the help of this Al-powered career accelerator\n\n📍this advanced Al tool offers a comprehensive suite of features to streamline your job search and optimize your resume and LinkedIn profile.\n\n📍Benefit from automated job tracking, personalized recommendations, and expert resume feedback.\n\n📍Elevate your candidacy and increase your chances of getting shortlisted for interviews.\n\n📍Embrace the future of job hunting with our cutting-edge Al technology.\n\n📍Follow Vijay Chollangi 🛡  For More Job and Al update\n\nVC- Careerflow.ai \n\n #ai #aitools #resume #job ",
              "time": "1d",
              "urn": "7133376861597794304",
              "video": {
                "duration": 39933,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQGxoQ3Ep51ZtA/feedshare-ambry-analyzed_servable_progressive_video/0/1700664873224?e=1701417600&v=beta&t=xcD98VhtjSHm6gYmdqmAC6ldpx-MPIxuLACsc1OU2Yk"
              }
            },
            {
              "images": [],
              "num_appreciations": 8,
              "num_comments": 68,
              "num_empathy": 17,
              "num_interests": 6,
              "num_likes": 576,
              "num_praises": 3,
              "num_reposts": 53,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133376811870167040/",
              "reshared": false,
              "text": "📍IT Companies in India.🎉💥\n\nApply here directly: (Share and comment for better reach)\n\n📍Company Career page Links:\n\n📍Google: https://lnkd.in/dKsmuXfh\n\n📍Amazon: https://lnkd.in/diJJqyr3\n\n📍intel: https://lnkd.in/d-QWtEfm\n\n📍Microsoft: https://lnkd.in/dTxGD7cy\n\n📍Mastercard: https://lnkd.in/dB83H-Jb\n\n📍nVIDIA: https://lnkd.in/dczs5y6d\n\n📍HARMAN: https://lnkd.in/dGr2bJiB\n\n📍Myntra: https://lnkd.in/d5NXB3Sw\n\n📍Flipkart: https://lnkd.in/dXR-mxQN\n\n📍Shell: https://lnkd.in/dzJiiFdF\n\n📍Siemens: https://lnkd.in/dDmAxYa6\n\n📍IBM: https://lnkd.in/d5QQgu7K\n\n📍Gap Inc: https://lnkd.in/dGyaAHRe\n\n📍Adobe: https://lnkd.in/d9jAyH4F\n\n📍Nike: https://lnkd.in/dxkGKZJi\n\n📍Moodys: https://lnkd.in/dm_u8S2r\n\n📍Mountblue: https://lnkd.in/dmivq6Zi\n\n📍Zycus: https://lnkd.in/gxUPvqxh\n\n📍Appypie: https://lnkd.in/gyScNsqj\n\n📍Tata Technologies: https://lnkd.in/d745BKSW\n\n📍Trimble: https://lnkd.in/dYHrXxnP\n\n📍Forcepoint: https://lnkd.in/dpebxvMN\n\n📍Siemens: https://lnkd.in/dWcE87ih\n\n📍DXC Technology: https://lnkd.in/ddWkRdCb\n\n📍BT Group: https://lnkd.in/d9zzwsav\n\n📍Ziplr: https://lnkd.in/dipniyrk\n\n📍Volvo: https://lnkd.in/dgfyUDwM\n\n📍ECI: https://lnkd.in/dRenRqFH\n\n📍Zoho: https://lnkd.in/dE5sE4-4\n\n📍Oracle: https://lnkd.in/d65KpPNq\n\n📍Morgan Stanley: https://lnkd.in/dxZkxkDx\n\n📍MoEngage: https://lnkd.in/dJQ9f55P\n\n📍JPMorgan: https://lnkd.in/d5q8E8x5\n\n📍Publicis Sapient: https://lnkd.in/dP8bjEcP\n\n📍Practo: https://lnkd.in/drTghJ9i\n\n📍Boston Consulting Group: https://lnkd.in/da7tUq6X\n\n📍PayPal: https://lnkd.in/dBadunAQ\n\n📍ABB: https://lnkd.in/d9H3xNcQ\n\n📍Mercedes Benz: https://lnkd.in/d9xY8Jak\n\n📍Tiger Analytics: https://lnkd.in/dR8uxR2P\n\n📍HP: https://lnkd.in/dJGUZHRS\n\n📍NetApp: https://lnkd.in/dPgQMsxr\n\n📍Airbus: https://lnkd.in/d9q_FKGg\n\n📍Phenom: https://lnkd.in/de57miGs\n\n📍Autodesk: https://lnkd.in/djGBv9Xg\n\n📍Salesforce: https://lnkd.in/dejdyvrW\n\n📍Goldman Sachs: https://lnkd.in/d4ak78sV\n\n📍Hexagon: https://lnkd.in/diZHrDEF\n\n📍Cisco: https://lnkd.in/dxDXGG_f\n\n📍Deutsche Bank: https://lnkd.in/dkq3dWhU\n\n📍Motorola: https://lnkd.in/d7hydH7n\n\n📍Renault: https://lnkd.in/dxSXFzW5\n\n📍SAP: https://lnkd.in/dcSqU5jb Societe\n\n📍 Generale: https://lnkd.in/dFXdCZFJ\n\n📍Atlassians: https://lnkd.in/dqtjnJcE\n\n📍Netflix: https://lnkd.in/d93NecpY\n\n📍Nissan: https://lnkd.in/dgAtM8_W\n\n📍Accenture: https://lnkd.in/dSm_JtF\n\n 📍Dell: https://lnkd.in/dutdNS8E\n\nFor more such information content follow Vijay Chollangi 🛡 \n\n#itcompany #indiajobs #companies #jobshiring #google ",
              "time": "2d",
              "urn": "7133376811870167040",
              "video": {
                "duration": 32000,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4E05AQGx3zPr4bsdww/feedshare-ambry-analyzed_servable_progressive_video/0/1700559190812?e=1701417600&v=beta&t=0qZPc6ODB5p_4zcPibI4_NJI5Si5WBq_FCgJ5cojaEk"
              }
            },
            {
              "document": {
                "page_count": 10,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQELs19o11PbWQ/feedshare-document-url-metadata-scrapper-pdf/0/1700708410608?e=1701417600&v=beta&t=mCKPUhrQ6MXT8suT0crd7tgq5nv_SX4LDB7l3_IqD30"
              },
              "images": [],
              "num_appreciations": 4,
              "num_comments": 63,
              "num_empathy": 2,
              "num_interests": 6,
              "num_likes": 253,
              "num_praises": 1,
              "num_reposts": 30,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133369238379003905/",
              "reshared": false,
              "text": "💥Amazing Website's That Will Make You Smarter!!!💡\n\n📍Cogram is an artificial intelligence company based in Berlin. We're a global team, with backgrounds in machine learning, software engineering, physics, and psychology, and are working on a future where humans and computers share a common language\n\n📍Cogram Features\n\n📍Al team meeting transcription platform.\n\n📍Generate meeting minutes.\n\n📍Summarise your meetings.\n\n📍Assign action items.\n\n📍Customizable Meeting Insights.\n\n📍Seamless Integrations.\n\n #technology #techcommunity #educational #chatgpt #learningeveryday ",
              "time": "1d",
              "urn": "7133369238379003905"
            },
            {
              "document": {
                "page_count": 10,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQELs19o11PbWQ/feedshare-document-url-metadata-scrapper-pdf/0/1700708410608?e=1701417600&v=beta&t=mCKPUhrQ6MXT8suT0crd7tgq5nv_SX4LDB7l3_IqD30"
              },
              "images": [],
              "num_appreciations": 4,
              "num_comments": 63,
              "num_empathy": 2,
              "num_interests": 6,
              "num_likes": 253,
              "num_praises": 1,
              "num_reposts": 30,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133301683970875393/",
              "reshared": false,
              "text": "💥Amazing Website's That Will Make You Smarter!!!💡\n\n📍Cogram is an artificial intelligence company based in Berlin. We're a global team, with backgrounds in machine learning, software engineering, physics, and psychology, and are working on a future where humans and computers share a common language\n\n📍Cogram Features\n\n📍Al team meeting transcription platform.\n\n📍Generate meeting minutes.\n\n📍Summarise your meetings.\n\n📍Assign action items.\n\n📍Customizable Meeting Insights.\n\n📍Seamless Integrations.\n\n #technology #techcommunity #educational #chatgpt #learningeveryday ",
              "time": "1d",
              "urn": "7133301683970875393"
            },
            {
              "document": {
                "page_count": 10,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQELs19o11PbWQ/feedshare-document-url-metadata-scrapper-pdf/0/1700708410608?e=1701417600&v=beta&t=mCKPUhrQ6MXT8suT0crd7tgq5nv_SX4LDB7l3_IqD30"
              },
              "images": [],
              "num_appreciations": 4,
              "num_comments": 63,
              "num_empathy": 2,
              "num_interests": 6,
              "num_likes": 253,
              "num_praises": 1,
              "num_reposts": 30,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133288129716748289/",
              "reshared": false,
              "text": "💥Amazing Website's That Will Make You Smarter!!!💡\n\n📍Cogram is an artificial intelligence company based in Berlin. We're a global team, with backgrounds in machine learning, software engineering, physics, and psychology, and are working on a future where humans and computers share a common language\n\n📍Cogram Features\n\n📍Al team meeting transcription platform.\n\n📍Generate meeting minutes.\n\n📍Summarise your meetings.\n\n📍Assign action items.\n\n📍Customizable Meeting Insights.\n\n📍Seamless Integrations.\n\n #technology #techcommunity #educational #chatgpt #learningeveryday ",
              "time": "1d",
              "urn": "7133288129716748289"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQH9fVqca5uEnw/feedshare-shrink_2048_1536/0/1700673956174?e=1703721600&v=beta&t=JeLAXcbzLFQuqjQbRlCIn6a3wZBhNr7A2XFjrPdN6F0"
                }
              ],
              "num_appreciations": 3,
              "num_comments": 21,
              "num_empathy": 3,
              "num_interests": 2,
              "num_likes": 68,
              "num_reposts": 4,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133286696422440960/",
              "reshared": false,
              "text": "💥Not as easy as it looks, buddy...💥💯\n\nlike If U Agree 👍 ",
              "time": "1d",
              "urn": "7133286696422440960"
            },
            {
              "images": [],
              "num_appreciations": 2,
              "num_comments": 40,
              "num_interests": 2,
              "num_likes": 181,
              "num_praises": 1,
              "num_reposts": 12,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133268409575755777/",
              "reshared": false,
              "text": "💥If Your Resume is not getting shortlisted then try this Hack📍\n\n📍Land your dream job with the help of this Al-powered career accelerator\n\n📍this advanced Al tool offers a comprehensive suite of features to streamline your job search and optimize your resume and LinkedIn profile.\n\n📍Benefit from automated job tracking, personalized recommendations, and expert resume feedback.\n\n📍Elevate your candidacy and increase your chances of getting shortlisted for interviews.\n\n📍Embrace the future of job hunting with our cutting-edge Al technology.\n\n📍Follow Vijay Chollangi 🛡  For More Job and Al update\n\nVC- Careerflow.ai \n\n #ai #aitools #resume #job ",
              "time": "1d",
              "urn": "7133268409575755777",
              "video": {
                "duration": 39933,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQGxoQ3Ep51ZtA/feedshare-ambry-analyzed_servable_progressive_video/0/1700664873224?e=1701417600&v=beta&t=xcD98VhtjSHm6gYmdqmAC6ldpx-MPIxuLACsc1OU2Yk"
              }
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQH9fVqca5uEnw/feedshare-shrink_2048_1536/0/1700673956174?e=1703721600&v=beta&t=JeLAXcbzLFQuqjQbRlCIn6a3wZBhNr7A2XFjrPdN6F0"
                }
              ],
              "num_appreciations": 3,
              "num_comments": 21,
              "num_empathy": 3,
              "num_interests": 2,
              "num_likes": 68,
              "num_reposts": 4,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133227822646525952/",
              "reshared": false,
              "text": "💥Not as easy as it looks, buddy...💥💯\n\nlike If U Agree 👍 ",
              "time": "1d",
              "urn": "7133227822646525952"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQH9fVqca5uEnw/feedshare-shrink_2048_1536/0/1700673956174?e=1703721600&v=beta&t=JeLAXcbzLFQuqjQbRlCIn6a3wZBhNr7A2XFjrPdN6F0"
                }
              ],
              "num_appreciations": 3,
              "num_comments": 21,
              "num_empathy": 3,
              "num_interests": 2,
              "num_likes": 68,
              "num_reposts": 4,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133143582474977280/",
              "reshared": false,
              "text": "💥Not as easy as it looks, buddy...💥💯\n\nlike If U Agree 👍 ",
              "time": "1d",
              "urn": "7133143582474977280"
            },
            {
              "images": [],
              "num_appreciations": 2,
              "num_comments": 40,
              "num_interests": 2,
              "num_likes": 181,
              "num_praises": 1,
              "num_reposts": 12,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133141835627077632/",
              "reshared": false,
              "text": "💥If Your Resume is not getting shortlisted then try this Hack📍\n\n📍Land your dream job with the help of this Al-powered career accelerator\n\n📍this advanced Al tool offers a comprehensive suite of features to streamline your job search and optimize your resume and LinkedIn profile.\n\n📍Benefit from automated job tracking, personalized recommendations, and expert resume feedback.\n\n📍Elevate your candidacy and increase your chances of getting shortlisted for interviews.\n\n📍Embrace the future of job hunting with our cutting-edge Al technology.\n\n📍Follow Vijay Chollangi 🛡  For More Job and Al update\n\nVC- Careerflow.ai \n\n #ai #aitools #resume #job ",
              "time": "1d",
              "urn": "7133141835627077632",
              "video": {
                "duration": 39933,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQGxoQ3Ep51ZtA/feedshare-ambry-analyzed_servable_progressive_video/0/1700664873224?e=1701417600&v=beta&t=xcD98VhtjSHm6gYmdqmAC6ldpx-MPIxuLACsc1OU2Yk"
              }
            },
            {
              "document": {
                "page_count": 17,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D4E1FAQGI0qV8Mp56qA/feedshare-document-url-metadata-scrapper-pdf/0/1700496658718?e=1701417600&v=beta&t=XloHUd0eYAETY-DOUJVQ4FOljcVjxbW_G42yhtKPs64"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 72,
              "num_empathy": 6,
              "num_interests": 1,
              "num_likes": 360,
              "num_praises": 1,
              "num_reposts": 51,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133141799476371458/",
              "reshared": false,
              "text": "🎯15 Visuals Unveiling Universal Success Principles!💼\n\n📍Success holds different meanings for individuals, yet the principles leading to success remain consistent, often misconceived as mere luck.\n\n📍Visuals serve as the most effective conduit for these principles. Research affirms that \"90% of information transmitted to the brain is visual, processed 60,000X faster than text.\"\n\n📍Follow and integrate these 15 visuals into your life for tangible changes. Share your insights from these visuals in the comments.\n\n\n\n#trending #motivation #success ",
              "time": "3d",
              "urn": "7133141799476371458"
            },
            {
              "document": {
                "page_count": 5,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGeBUORCWXaYQ/feedshare-document-url-metadata-scrapper-pdf/0/1700622249087?e=1701417600&v=beta&t=VFPE-PtqPhl8ImwbE35Ct1SHD0D0IpkdPcM_UgASTRI"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 63,
              "num_empathy": 6,
              "num_interests": 6,
              "num_likes": 341,
              "num_reposts": 52,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133141655632678912/",
              "reshared": false,
              "text": "🎉💥Helpful Resources to Land your First Job or Internship in 2023💯\n\n\n\n📍Sites to get an Internship💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed - https://in.indeed.com\n\nInternshala - https://lnkd.in/dGGFv5tq\n\nGlassdoor - https://lnkd.in/daG2cCYF\n\nIdealist.org - https://lnkd.in/d_VErnK8\n\nAbsolute Internship - https://lnkd.in/drUaknHb\n\nLooksharp - https://looksharp.global\n\nIntern Queen Inc. - https://lnkd.in/dur9dcdt\n\nInternship Programs - https://lnkd.in/dTmwRW_D\n\nAlma Mater - https://lnkd.in/d5PpdVPj\n\n\n\n\n📍Sites for your Job Search💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed.com - https://in.indeed.com\n\nDice - https://www.dice.com\n\nGlassdoor - https://lnkd.in/daG2cCyF\n\nIdealist.org - https://www.idealist.org\n\nCareerBuilder - https://lnkd.in/dbhKHp-B\n\nLinkup - https://www.linkup.com\n\nGoogle For Jobs - https://lnkd.in/dkDQy6Hn\n\nMonster - https://www.foundit.in\n\nUS Jobs - https://www.usajobs.gov \n\n\n\n\n📍Sites to Build your Resume💥\n\nCanva - https://www.canva.com\n\nKickresume - https://lnkd.in/drhBTXJD\n\nVisualCV - https://www.visualcv.com\n\nZety: Resume Builder & Career Website - https://zety.com\n\nNovorésumé - https://novoresume.com\n\nMyPerfectResume - https://lnkd.in/dkp233pW\n\nResume Genius - https://resumegenius.com\n\nPongo - https://lnkd.in/dCrjBZWF\n\nCreddle-Dev- http://creddle.io\n\n\n\n\n📍Sites to Learn Tech Skills💥\n\nTreehouse - https://teamtreehouse.com\n\nKhan Academy - https://lnkd.in/d-Q2bM64\n\nCodeSchool - https://www.codeschool.co\n\nedX - https://www.edx.org\n\nCoursera - https://www.coursera.org\n\nCodewars - https://www.codewars.com\n\nfreeCodeCamp - https://lnkd.in/dcS6uxcH\n\nGitHub - https://github.com\n\nThe Odin Project - https://lnkd.in/dYQCAvdM \n\nW3Schools.com - https://www.w3schools.com\n\n\n\n\nFollow Vijay Chollangi 🛡  for more.\n\n\n#internships #resumewriting #jobs #career ",
              "time": "2d",
              "urn": "7133141655632678912"
            },
            {
              "images": [],
              "num_appreciations": 2,
              "num_comments": 40,
              "num_interests": 2,
              "num_likes": 181,
              "num_praises": 1,
              "num_reposts": 12,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133137773829517312/",
              "reshared": false,
              "text": "💥If Your Resume is not getting shortlisted then try this Hack📍\n\n📍Land your dream job with the help of this Al-powered career accelerator\n\n📍this advanced Al tool offers a comprehensive suite of features to streamline your job search and optimize your resume and LinkedIn profile.\n\n📍Benefit from automated job tracking, personalized recommendations, and expert resume feedback.\n\n📍Elevate your candidacy and increase your chances of getting shortlisted for interviews.\n\n📍Embrace the future of job hunting with our cutting-edge Al technology.\n\n📍Follow Vijay Chollangi 🛡  For More Job and Al update\n\nVC- Careerflow.ai \n\n #ai #aitools #resume #job ",
              "time": "1d",
              "urn": "7133137773829517312",
              "video": {
                "duration": 39933,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQGxoQ3Ep51ZtA/feedshare-ambry-analyzed_servable_progressive_video/0/1700664873224?e=1701417600&v=beta&t=xcD98VhtjSHm6gYmdqmAC6ldpx-MPIxuLACsc1OU2Yk"
              }
            },
            {
              "images": [],
              "num_appreciations": 2,
              "num_comments": 40,
              "num_interests": 2,
              "num_likes": 181,
              "num_praises": 1,
              "num_reposts": 12,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133105495535468544/",
              "reshared": false,
              "text": "💥If Your Resume is not getting shortlisted then try this Hack📍\n\n📍Land your dream job with the help of this Al-powered career accelerator\n\n📍this advanced Al tool offers a comprehensive suite of features to streamline your job search and optimize your resume and LinkedIn profile.\n\n📍Benefit from automated job tracking, personalized recommendations, and expert resume feedback.\n\n📍Elevate your candidacy and increase your chances of getting shortlisted for interviews.\n\n📍Embrace the future of job hunting with our cutting-edge Al technology.\n\n📍Follow Vijay Chollangi 🛡  For More Job and Al update\n\nVC- Careerflow.ai \n\n #ai #aitools #resume #job ",
              "time": "1d",
              "urn": "7133105495535468544",
              "video": {
                "duration": 39933,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5605AQGxoQ3Ep51ZtA/feedshare-ambry-analyzed_servable_progressive_video/0/1700664873224?e=1701417600&v=beta&t=xcD98VhtjSHm6gYmdqmAC6ldpx-MPIxuLACsc1OU2Yk"
              }
            },
            {
              "document": {
                "page_count": 124,
                "title": "Html 💯swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQFovhCSVfgw3Q/feedshare-document-url-metadata-scrapper-pdf/0/1700644739530?e=1701417600&v=beta&t=VrYtce4-F38vaB9n99daF2bNDmcChaOVKBPdCVMOX6E"
              },
              "images": [],
              "num_comments": 36,
              "num_empathy": 2,
              "num_interests": 4,
              "num_likes": 179,
              "num_reposts": 7,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133087830746009600/",
              "reshared": false,
              "text": "🌐 Demystifying HTML: The Backbone of the Web 🌐\n\n📍HTML, or HyperText Markup Language, is the language that structures content on the World Wide Web. It uses tags to define elements such as headings, paragraphs, links, and images, creating the fundamental building blocks of a webpage.\n\n🚀 Key Features:\n\n📍Semantic Structure: \n\nEmploy tags like <header>, <nav>, and <footer> for clear and meaningful content organization.\n\n📍Hyperlinks: \n\nConnect pages seamlessly using <a> tags, fostering navigation within websites.\nMedia Integration: Embed images and multimedia effortlessly with <img> and other media-specific tags.\n\n\n📍Forms: \n\nCapture user input with form elements like <input>, <textarea>, and <button>, enhancing interactivity.\n\n\n📍HTML lays the groundwork for web development, providing the structure that CSS styles and JavaScript enhances.\n\n📍 Mastering HTML is the gateway to crafting compelling, user-friendly web experiences.\n\n\n 💻✨ #HTML #WebDevelopment #TechSkills #linkedin ",
              "time": "1d",
              "urn": "7133087830746009600"
            },
            {
              "document": {
                "page_count": 105,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQHM9uhoDTHcIQ/feedshare-document-url-metadata-scrapper-pdf/0/1699847817748?e=1701417600&v=beta&t=yoSy0MSRReh9G2KP1h9IpkLvk59jmTU8YCrrxWQkji8"
              },
              "images": [],
              "num_appreciations": 2,
              "num_comments": 33,
              "num_empathy": 1,
              "num_interests": 6,
              "num_likes": 168,
              "num_reposts": 19,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133058787300540416/",
              "reshared": false,
              "text": "🎉LeetCode Important SQL Problems and Solutions.💥💡\n\nIn this document, you will find all the essential SQL questions from LeetCode and their solutions.\n\nSQL is one of the most crucial skills to master to be a data analyst or software developer.\n\nGood luck on your journey!\n\nDo Like & Repost if you find this helpful.\n\nFollow Vijay Chollangi 🛡  for more.\n\n\n\n#sql #leetcode #sqldeveloper #dba #webdevelopment #sqlserver #softwaredevelopment \n",
              "time": "1w",
              "urn": "7133058787300540416"
            },
            {
              "document": {
                "page_count": 124,
                "title": "Html 💯swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQFovhCSVfgw3Q/feedshare-document-url-metadata-scrapper-pdf/0/1700644739530?e=1701417600&v=beta&t=VrYtce4-F38vaB9n99daF2bNDmcChaOVKBPdCVMOX6E"
              },
              "images": [],
              "num_comments": 36,
              "num_empathy": 2,
              "num_interests": 4,
              "num_likes": 179,
              "num_reposts": 7,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133042725095952384/",
              "reshared": false,
              "text": "🌐 Demystifying HTML: The Backbone of the Web 🌐\n\n📍HTML, or HyperText Markup Language, is the language that structures content on the World Wide Web. It uses tags to define elements such as headings, paragraphs, links, and images, creating the fundamental building blocks of a webpage.\n\n🚀 Key Features:\n\n📍Semantic Structure: \n\nEmploy tags like <header>, <nav>, and <footer> for clear and meaningful content organization.\n\n📍Hyperlinks: \n\nConnect pages seamlessly using <a> tags, fostering navigation within websites.\nMedia Integration: Embed images and multimedia effortlessly with <img> and other media-specific tags.\n\n\n📍Forms: \n\nCapture user input with form elements like <input>, <textarea>, and <button>, enhancing interactivity.\n\n\n📍HTML lays the groundwork for web development, providing the structure that CSS styles and JavaScript enhances.\n\n📍 Mastering HTML is the gateway to crafting compelling, user-friendly web experiences.\n\n\n 💻✨ #HTML #WebDevelopment #TechSkills #linkedin ",
              "time": "1d",
              "urn": "7133042725095952384"
            },
            {
              "document": {
                "page_count": 124,
                "title": "Html 💯swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQFovhCSVfgw3Q/feedshare-document-url-metadata-scrapper-pdf/0/1700644739530?e=1701417600&v=beta&t=VrYtce4-F38vaB9n99daF2bNDmcChaOVKBPdCVMOX6E"
              },
              "images": [],
              "num_comments": 36,
              "num_empathy": 2,
              "num_interests": 4,
              "num_likes": 179,
              "num_reposts": 7,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133021206236073984/",
              "reshared": false,
              "text": "🌐 Demystifying HTML: The Backbone of the Web 🌐\n\n📍HTML, or HyperText Markup Language, is the language that structures content on the World Wide Web. It uses tags to define elements such as headings, paragraphs, links, and images, creating the fundamental building blocks of a webpage.\n\n🚀 Key Features:\n\n📍Semantic Structure: \n\nEmploy tags like <header>, <nav>, and <footer> for clear and meaningful content organization.\n\n📍Hyperlinks: \n\nConnect pages seamlessly using <a> tags, fostering navigation within websites.\nMedia Integration: Embed images and multimedia effortlessly with <img> and other media-specific tags.\n\n\n📍Forms: \n\nCapture user input with form elements like <input>, <textarea>, and <button>, enhancing interactivity.\n\n\n📍HTML lays the groundwork for web development, providing the structure that CSS styles and JavaScript enhances.\n\n📍 Mastering HTML is the gateway to crafting compelling, user-friendly web experiences.\n\n\n 💻✨ #HTML #WebDevelopment #TechSkills #linkedin ",
              "time": "1d",
              "urn": "7133021206236073984"
            },
            {
              "document": {
                "page_count": 5,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGeBUORCWXaYQ/feedshare-document-url-metadata-scrapper-pdf/0/1700622249087?e=1701417600&v=beta&t=VFPE-PtqPhl8ImwbE35Ct1SHD0D0IpkdPcM_UgASTRI"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 63,
              "num_empathy": 6,
              "num_interests": 6,
              "num_likes": 341,
              "num_reposts": 52,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7133004878485852160/",
              "reshared": false,
              "text": "🎉💥Helpful Resources to Land your First Job or Internship in 2023💯\n\n\n\n📍Sites to get an Internship💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed - https://in.indeed.com\n\nInternshala - https://lnkd.in/dGGFv5tq\n\nGlassdoor - https://lnkd.in/daG2cCYF\n\nIdealist.org - https://lnkd.in/d_VErnK8\n\nAbsolute Internship - https://lnkd.in/drUaknHb\n\nLooksharp - https://looksharp.global\n\nIntern Queen Inc. - https://lnkd.in/dur9dcdt\n\nInternship Programs - https://lnkd.in/dTmwRW_D\n\nAlma Mater - https://lnkd.in/d5PpdVPj\n\n\n\n\n📍Sites for your Job Search💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed.com - https://in.indeed.com\n\nDice - https://www.dice.com\n\nGlassdoor - https://lnkd.in/daG2cCyF\n\nIdealist.org - https://www.idealist.org\n\nCareerBuilder - https://lnkd.in/dbhKHp-B\n\nLinkup - https://www.linkup.com\n\nGoogle For Jobs - https://lnkd.in/dkDQy6Hn\n\nMonster - https://www.foundit.in\n\nUS Jobs - https://www.usajobs.gov \n\n\n\n\n📍Sites to Build your Resume💥\n\nCanva - https://www.canva.com\n\nKickresume - https://lnkd.in/drhBTXJD\n\nVisualCV - https://www.visualcv.com\n\nZety: Resume Builder & Career Website - https://zety.com\n\nNovorésumé - https://novoresume.com\n\nMyPerfectResume - https://lnkd.in/dkp233pW\n\nResume Genius - https://resumegenius.com\n\nPongo - https://lnkd.in/dCrjBZWF\n\nCreddle-Dev- http://creddle.io\n\n\n\n\n📍Sites to Learn Tech Skills💥\n\nTreehouse - https://teamtreehouse.com\n\nKhan Academy - https://lnkd.in/d-Q2bM64\n\nCodeSchool - https://www.codeschool.co\n\nedX - https://www.edx.org\n\nCoursera - https://www.coursera.org\n\nCodewars - https://www.codewars.com\n\nfreeCodeCamp - https://lnkd.in/dcS6uxcH\n\nGitHub - https://github.com\n\nThe Odin Project - https://lnkd.in/dYQCAvdM \n\nW3Schools.com - https://www.w3schools.com\n\n\n\n\nFollow Vijay Chollangi 🛡  for more.\n\n\n#internships #resumewriting #jobs #career ",
              "time": "2d",
              "urn": "7133004878485852160"
            },
            {
              "document": {
                "page_count": 5,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGeBUORCWXaYQ/feedshare-document-url-metadata-scrapper-pdf/0/1700622249087?e=1701417600&v=beta&t=VFPE-PtqPhl8ImwbE35Ct1SHD0D0IpkdPcM_UgASTRI"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 63,
              "num_empathy": 6,
              "num_interests": 6,
              "num_likes": 341,
              "num_reposts": 52,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132986604087889921/",
              "reshared": false,
              "text": "🎉💥Helpful Resources to Land your First Job or Internship in 2023💯\n\n\n\n📍Sites to get an Internship💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed - https://in.indeed.com\n\nInternshala - https://lnkd.in/dGGFv5tq\n\nGlassdoor - https://lnkd.in/daG2cCYF\n\nIdealist.org - https://lnkd.in/d_VErnK8\n\nAbsolute Internship - https://lnkd.in/drUaknHb\n\nLooksharp - https://looksharp.global\n\nIntern Queen Inc. - https://lnkd.in/dur9dcdt\n\nInternship Programs - https://lnkd.in/dTmwRW_D\n\nAlma Mater - https://lnkd.in/d5PpdVPj\n\n\n\n\n📍Sites for your Job Search💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed.com - https://in.indeed.com\n\nDice - https://www.dice.com\n\nGlassdoor - https://lnkd.in/daG2cCyF\n\nIdealist.org - https://www.idealist.org\n\nCareerBuilder - https://lnkd.in/dbhKHp-B\n\nLinkup - https://www.linkup.com\n\nGoogle For Jobs - https://lnkd.in/dkDQy6Hn\n\nMonster - https://www.foundit.in\n\nUS Jobs - https://www.usajobs.gov \n\n\n\n\n📍Sites to Build your Resume💥\n\nCanva - https://www.canva.com\n\nKickresume - https://lnkd.in/drhBTXJD\n\nVisualCV - https://www.visualcv.com\n\nZety: Resume Builder & Career Website - https://zety.com\n\nNovorésumé - https://novoresume.com\n\nMyPerfectResume - https://lnkd.in/dkp233pW\n\nResume Genius - https://resumegenius.com\n\nPongo - https://lnkd.in/dCrjBZWF\n\nCreddle-Dev- http://creddle.io\n\n\n\n\n📍Sites to Learn Tech Skills💥\n\nTreehouse - https://teamtreehouse.com\n\nKhan Academy - https://lnkd.in/d-Q2bM64\n\nCodeSchool - https://www.codeschool.co\n\nedX - https://www.edx.org\n\nCoursera - https://www.coursera.org\n\nCodewars - https://www.codewars.com\n\nfreeCodeCamp - https://lnkd.in/dcS6uxcH\n\nGitHub - https://github.com\n\nThe Odin Project - https://lnkd.in/dYQCAvdM \n\nW3Schools.com - https://www.w3schools.com\n\n\n\n\nFollow Vijay Chollangi 🛡  for more.\n\n\n#internships #resumewriting #jobs #career ",
              "time": "2d",
              "urn": "7132986604087889921"
            },
            {
              "images": [],
              "num_appreciations": 8,
              "num_comments": 68,
              "num_empathy": 17,
              "num_interests": 6,
              "num_likes": 576,
              "num_praises": 3,
              "num_reposts": 53,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132986572383125504/",
              "reshared": false,
              "text": "📍IT Companies in India.🎉💥\n\nApply here directly: (Share and comment for better reach)\n\n📍Company Career page Links:\n\n📍Google: https://lnkd.in/dKsmuXfh\n\n📍Amazon: https://lnkd.in/diJJqyr3\n\n📍intel: https://lnkd.in/d-QWtEfm\n\n📍Microsoft: https://lnkd.in/dTxGD7cy\n\n📍Mastercard: https://lnkd.in/dB83H-Jb\n\n📍nVIDIA: https://lnkd.in/dczs5y6d\n\n📍HARMAN: https://lnkd.in/dGr2bJiB\n\n📍Myntra: https://lnkd.in/d5NXB3Sw\n\n📍Flipkart: https://lnkd.in/dXR-mxQN\n\n📍Shell: https://lnkd.in/dzJiiFdF\n\n📍Siemens: https://lnkd.in/dDmAxYa6\n\n📍IBM: https://lnkd.in/d5QQgu7K\n\n📍Gap Inc: https://lnkd.in/dGyaAHRe\n\n📍Adobe: https://lnkd.in/d9jAyH4F\n\n📍Nike: https://lnkd.in/dxkGKZJi\n\n📍Moodys: https://lnkd.in/dm_u8S2r\n\n📍Mountblue: https://lnkd.in/dmivq6Zi\n\n📍Zycus: https://lnkd.in/gxUPvqxh\n\n📍Appypie: https://lnkd.in/gyScNsqj\n\n📍Tata Technologies: https://lnkd.in/d745BKSW\n\n📍Trimble: https://lnkd.in/dYHrXxnP\n\n📍Forcepoint: https://lnkd.in/dpebxvMN\n\n📍Siemens: https://lnkd.in/dWcE87ih\n\n📍DXC Technology: https://lnkd.in/ddWkRdCb\n\n📍BT Group: https://lnkd.in/d9zzwsav\n\n📍Ziplr: https://lnkd.in/dipniyrk\n\n📍Volvo: https://lnkd.in/dgfyUDwM\n\n📍ECI: https://lnkd.in/dRenRqFH\n\n📍Zoho: https://lnkd.in/dE5sE4-4\n\n📍Oracle: https://lnkd.in/d65KpPNq\n\n📍Morgan Stanley: https://lnkd.in/dxZkxkDx\n\n📍MoEngage: https://lnkd.in/dJQ9f55P\n\n📍JPMorgan: https://lnkd.in/d5q8E8x5\n\n📍Publicis Sapient: https://lnkd.in/dP8bjEcP\n\n📍Practo: https://lnkd.in/drTghJ9i\n\n📍Boston Consulting Group: https://lnkd.in/da7tUq6X\n\n📍PayPal: https://lnkd.in/dBadunAQ\n\n📍ABB: https://lnkd.in/d9H3xNcQ\n\n📍Mercedes Benz: https://lnkd.in/d9xY8Jak\n\n📍Tiger Analytics: https://lnkd.in/dR8uxR2P\n\n📍HP: https://lnkd.in/dJGUZHRS\n\n📍NetApp: https://lnkd.in/dPgQMsxr\n\n📍Airbus: https://lnkd.in/d9q_FKGg\n\n📍Phenom: https://lnkd.in/de57miGs\n\n📍Autodesk: https://lnkd.in/djGBv9Xg\n\n📍Salesforce: https://lnkd.in/dejdyvrW\n\n📍Goldman Sachs: https://lnkd.in/d4ak78sV\n\n📍Hexagon: https://lnkd.in/diZHrDEF\n\n📍Cisco: https://lnkd.in/dxDXGG_f\n\n📍Deutsche Bank: https://lnkd.in/dkq3dWhU\n\n📍Motorola: https://lnkd.in/d7hydH7n\n\n📍Renault: https://lnkd.in/dxSXFzW5\n\n📍SAP: https://lnkd.in/dcSqU5jb Societe\n\n📍 Generale: https://lnkd.in/dFXdCZFJ\n\n📍Atlassians: https://lnkd.in/dqtjnJcE\n\n📍Netflix: https://lnkd.in/d93NecpY\n\n📍Nissan: https://lnkd.in/dgAtM8_W\n\n📍Accenture: https://lnkd.in/dSm_JtF\n\n 📍Dell: https://lnkd.in/dutdNS8E\n\nFor more such information content follow Vijay Chollangi 🛡 \n\n#itcompany #indiajobs #companies #jobshiring #google ",
              "time": "2d",
              "urn": "7132986572383125504",
              "video": {
                "duration": 32000,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4E05AQGx3zPr4bsdww/feedshare-ambry-analyzed_servable_progressive_video/0/1700559190812?e=1701417600&v=beta&t=0qZPc6ODB5p_4zcPibI4_NJI5Si5WBq_FCgJ5cojaEk"
              }
            },
            {
              "document": {
                "page_count": 9,
                "title": "Must Read 📚 books",
                "url": "https://media.licdn.com/dms/document/media/D4D1FAQGzNtxW9KtZrA/feedshare-document-url-metadata-scrapper-pdf/0/1700580348423?e=1701417600&v=beta&t=dnQEHEe9I0MeUkMU7uUCbL5Gc9RnBWMs3fYwX-e0Hh8"
              },
              "images": [],
              "num_appreciations": 3,
              "num_comments": 47,
              "num_empathy": 3,
              "num_interests": 6,
              "num_likes": 274,
              "num_reposts": 28,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132986559821221889/",
              "reshared": false,
              "text": "😊Books You must read Before 30s💥🎉\n\n📍Reading books offers numerous benefits that can enrich our lives in various ways. Here are some compelling reasons why you should consider reading books:\n\n◆ Expands knowledge and learning.\n\n◆ Enhances vocabulary and language skills.\n\n◆ Promotes critical thinking.\n\n◆ Sparks imagination and creativity.\n\nReduces stress and offers escapism.\n\n◆ Cultivates empathy and understanding.\n\n◆ Improves concentration and focus.\n\n◆ Stimulates mental activity.\n\n◆ Facilitates personal growth.\n\n◆ Provides entertainment and enjoyment.\n\n◆ Offers inspiration and motivation.\n\n◆ Fosters social connections through shared reading experiences.\n\nFollow Vijay Chollangi 🛡  for more amazing content.\n\n#job #career #development #connections #ai #aidesign #communication #jobsearch #content #resume #softwaredevelopment #software #projects ",
              "time": "2d",
              "urn": "7132986559821221889"
            },
            {
              "images": [],
              "num_appreciations": 2,
              "num_comments": 63,
              "num_empathy": 2,
              "num_interests": 3,
              "num_likes": 142,
              "num_praises": 2,
              "num_reposts": 8,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132979722585608192/",
              "poster_linkedin_url": "https://www.linkedin.com/in/manish-kumar-shah",
              "reshared": false,
              "text": "Are you tired of spending hours creating content that doesn’t resonate with your audience? \n\nSay goodbye to the struggle!\n\nMeet Yarnit✨, the ultimate All-in-one GenAI-powered Personalized Content Creation engine.\n\nYarnit's AI constantly learns from external data and adapts to your business's unique data, guaranteeing on-brand and on-trend personalized content. 🎯 Ideal for journalists, marketers, and content creators.\n\n𝗪𝗶𝘁𝗵 Yarnit, 𝘆𝗼𝘂 𝗴𝗲𝘁:\n\n🌐 𝗜𝗱𝗲𝗮 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿: Generates content ideas from various sources, including news, articles, documents, text blocks, keywords, and public holiday events.\n\n🖼️𝗗𝗿𝗲𝗮𝗺𝗕𝗿𝘂𝘀𝗵: User-friendly AI image and background generator that requires no specialized prompts. Choose from a variety of options to create stunning images.\n\n✍️ 𝗔𝗜 𝗪𝗿𝗶𝘁𝗶𝗻𝗴: Creates personalized brand copies with capabilities such as rewriting, summarizing, expanding, shortening, changing tone, and incorporating content hooks.\n\n🎨 𝗔𝗜 𝗗𝗲𝘀𝗶𝗴𝗻: Generates presentations, carousels, ads, and post designs effortlessly with just a few clicks.\n\n🌐𝗕𝗿𝗮𝗻𝗱 𝗣𝗲𝗿𝘀𝗼𝗻𝗮𝗹𝗶𝘇𝗮𝘁𝗶𝗼𝗻: Ensures content is unique and aligns with brand tone and palette.\n\n📸 𝗔𝗜 𝗠𝘂𝗹𝘁𝗶𝗺𝗲𝗱𝗶𝗮 𝗥𝗲𝗰𝗼𝗺𝗺𝗲𝗻𝗱𝗮𝘁𝗶𝗼𝗻𝘀: Saves time by recommending the best set of images, icons, stats, research data, quotes, and music for each project.\n\n🧹 𝗔𝗜 𝗕𝗮𝗰𝗸𝗴𝗿𝗼𝘂𝗻𝗱 𝗥𝗲𝗺𝗼𝘃𝗲𝗿: Eliminates unwanted backgrounds from images in a single click.\n\n📄 𝗨𝘀𝗲-𝗖𝗮𝘀𝗲 𝗦𝗽𝗲𝗰𝗶𝗳𝗶𝗰 𝗧𝗲𝗺𝗽𝗹𝗮𝘁𝗲𝘀: Offers over 60 ready-to-use content templates for various purposes, such as blogs, emails, social media carousels, and presentations.\n\n🎨 𝗔𝗱𝘃𝗮𝗻𝗰𝗲𝗱 𝗘𝗱𝗶𝘁𝗶𝗻𝗴 𝗢𝗽𝘁𝗶𝗼𝗻𝘀 𝗳𝗼𝗿 𝗗𝗲𝘀𝗶𝗴𝗻𝗶𝗻𝗴: Allows users to edit designs on an easy-to-use canvas, offering features like filters, adjustments, layers, transparency, mockups, and text edits.\n\n🔍 𝗖𝗼𝗻𝘁𝗲𝗻𝘁 𝗔𝘂𝗱𝗶𝘁𝗼𝗿:Reviews and analyzes the impact of content before publishing.\n\n📆 𝗦𝗼𝗰𝗶𝗮𝗹 𝗠𝗲𝗱𝗶𝗮 𝗣𝘂𝗯𝗹𝗶𝘀𝗵𝗶𝗻𝗴 𝗮𝗻𝗱 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗿: Enables users to publish or schedule posts on multiple platforms, including Facebook, Instagram, Twitter, LinkedIn, Reddit, and Pinterest, all at once.\n\n📊 𝗖𝗼𝗺𝗯𝗶𝗻𝗲𝗱 𝗦𝗼𝗰𝗶𝗮𝗹 𝗠𝗲𝗱𝗶𝗮 𝗣𝗼𝘀𝘁 𝗔𝗻𝗮𝗹𝘆𝘁𝗶𝗰𝘀:\n Measures the performance of posts and provides consolidated insights from all social channels.\n\n🚀Yarnit's 𝗲𝘅𝗰𝗹𝘂𝘀𝗶𝘃𝗲 𝗕𝗹𝗮𝗰𝗸 𝗙𝗿𝗶𝗱𝗮𝘆 𝗢𝗳𝗳𝗲𝗿 makes all types of AI content creation even more budget-friendly, now priced at less than $0.5/day, Only for a limited time! 🚨⏰\n\n𝗧𝗿𝘆 𝗶𝘁 𝗡𝗼𝘄 𝗳𝗼𝗿 𝗙𝗿𝗲𝗲🔗:  https://lnkd.in/d4uBCvba\n\n#contentcreation #aicontent #marketingtech #contentmarketingtips #socialmediamarketing #brandstorytelling #aiwritingassistant #contentcollaboration #contentstrategy #visualcontent #socialmediaanalytics #ai #Yarnit #yarnitapp #technologytrends ",
              "time": "2d",
              "urn": "7132979722585608192",
              "video": {
                "duration": 60666,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4D05AQGQ1kE-AZXd1Q/mp4-720p-30fp-crf28/0/1700595956076?e=1701417600&v=beta&t=zgmTGIniXgO6xz07G41pQ-gt6OuhyDSoYNswwid7CPU"
              }
            },
            {
              "document": {
                "page_count": 5,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGeBUORCWXaYQ/feedshare-document-url-metadata-scrapper-pdf/0/1700622249087?e=1701417600&v=beta&t=VFPE-PtqPhl8ImwbE35Ct1SHD0D0IpkdPcM_UgASTRI"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 63,
              "num_empathy": 6,
              "num_interests": 6,
              "num_likes": 341,
              "num_reposts": 52,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132974497376206848/",
              "reshared": false,
              "text": "🎉💥Helpful Resources to Land your First Job or Internship in 2023💯\n\n\n\n📍Sites to get an Internship💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed - https://in.indeed.com\n\nInternshala - https://lnkd.in/dGGFv5tq\n\nGlassdoor - https://lnkd.in/daG2cCYF\n\nIdealist.org - https://lnkd.in/d_VErnK8\n\nAbsolute Internship - https://lnkd.in/drUaknHb\n\nLooksharp - https://looksharp.global\n\nIntern Queen Inc. - https://lnkd.in/dur9dcdt\n\nInternship Programs - https://lnkd.in/dTmwRW_D\n\nAlma Mater - https://lnkd.in/d5PpdVPj\n\n\n\n\n📍Sites for your Job Search💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed.com - https://in.indeed.com\n\nDice - https://www.dice.com\n\nGlassdoor - https://lnkd.in/daG2cCyF\n\nIdealist.org - https://www.idealist.org\n\nCareerBuilder - https://lnkd.in/dbhKHp-B\n\nLinkup - https://www.linkup.com\n\nGoogle For Jobs - https://lnkd.in/dkDQy6Hn\n\nMonster - https://www.foundit.in\n\nUS Jobs - https://www.usajobs.gov \n\n\n\n\n📍Sites to Build your Resume💥\n\nCanva - https://www.canva.com\n\nKickresume - https://lnkd.in/drhBTXJD\n\nVisualCV - https://www.visualcv.com\n\nZety: Resume Builder & Career Website - https://zety.com\n\nNovorésumé - https://novoresume.com\n\nMyPerfectResume - https://lnkd.in/dkp233pW\n\nResume Genius - https://resumegenius.com\n\nPongo - https://lnkd.in/dCrjBZWF\n\nCreddle-Dev- http://creddle.io\n\n\n\n\n📍Sites to Learn Tech Skills💥\n\nTreehouse - https://teamtreehouse.com\n\nKhan Academy - https://lnkd.in/d-Q2bM64\n\nCodeSchool - https://www.codeschool.co\n\nedX - https://www.edx.org\n\nCoursera - https://www.coursera.org\n\nCodewars - https://www.codewars.com\n\nfreeCodeCamp - https://lnkd.in/dcS6uxcH\n\nGitHub - https://github.com\n\nThe Odin Project - https://lnkd.in/dYQCAvdM \n\nW3Schools.com - https://www.w3schools.com\n\n\n\n\nFollow Vijay Chollangi 🛡  for more.\n\n\n#internships #resumewriting #jobs #career ",
              "time": "2d",
              "urn": "7132974497376206848"
            },
            {
              "document": {
                "page_count": 5,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGeBUORCWXaYQ/feedshare-document-url-metadata-scrapper-pdf/0/1700622249087?e=1701417600&v=beta&t=VFPE-PtqPhl8ImwbE35Ct1SHD0D0IpkdPcM_UgASTRI"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 63,
              "num_empathy": 6,
              "num_interests": 6,
              "num_likes": 341,
              "num_reposts": 52,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132946514867339264/",
              "reshared": false,
              "text": "🎉💥Helpful Resources to Land your First Job or Internship in 2023💯\n\n\n\n📍Sites to get an Internship💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed - https://in.indeed.com\n\nInternshala - https://lnkd.in/dGGFv5tq\n\nGlassdoor - https://lnkd.in/daG2cCYF\n\nIdealist.org - https://lnkd.in/d_VErnK8\n\nAbsolute Internship - https://lnkd.in/drUaknHb\n\nLooksharp - https://looksharp.global\n\nIntern Queen Inc. - https://lnkd.in/dur9dcdt\n\nInternship Programs - https://lnkd.in/dTmwRW_D\n\nAlma Mater - https://lnkd.in/d5PpdVPj\n\n\n\n\n📍Sites for your Job Search💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed.com - https://in.indeed.com\n\nDice - https://www.dice.com\n\nGlassdoor - https://lnkd.in/daG2cCyF\n\nIdealist.org - https://www.idealist.org\n\nCareerBuilder - https://lnkd.in/dbhKHp-B\n\nLinkup - https://www.linkup.com\n\nGoogle For Jobs - https://lnkd.in/dkDQy6Hn\n\nMonster - https://www.foundit.in\n\nUS Jobs - https://www.usajobs.gov \n\n\n\n\n📍Sites to Build your Resume💥\n\nCanva - https://www.canva.com\n\nKickresume - https://lnkd.in/drhBTXJD\n\nVisualCV - https://www.visualcv.com\n\nZety: Resume Builder & Career Website - https://zety.com\n\nNovorésumé - https://novoresume.com\n\nMyPerfectResume - https://lnkd.in/dkp233pW\n\nResume Genius - https://resumegenius.com\n\nPongo - https://lnkd.in/dCrjBZWF\n\nCreddle-Dev- http://creddle.io\n\n\n\n\n📍Sites to Learn Tech Skills💥\n\nTreehouse - https://teamtreehouse.com\n\nKhan Academy - https://lnkd.in/d-Q2bM64\n\nCodeSchool - https://www.codeschool.co\n\nedX - https://www.edx.org\n\nCoursera - https://www.coursera.org\n\nCodewars - https://www.codewars.com\n\nfreeCodeCamp - https://lnkd.in/dcS6uxcH\n\nGitHub - https://github.com\n\nThe Odin Project - https://lnkd.in/dYQCAvdM \n\nW3Schools.com - https://www.w3schools.com\n\n\n\n\nFollow Vijay Chollangi 🛡  for more.\n\n\n#internships #resumewriting #jobs #career ",
              "time": "2d",
              "urn": "7132946514867339264"
            },
            {
              "document": {
                "page_count": 5,
                "title": "swipe 👉 ",
                "url": "https://media.licdn.com/dms/document/media/D561FAQGeBUORCWXaYQ/feedshare-document-url-metadata-scrapper-pdf/0/1700622249087?e=1701417600&v=beta&t=VFPE-PtqPhl8ImwbE35Ct1SHD0D0IpkdPcM_UgASTRI"
              },
              "images": [],
              "num_appreciations": 6,
              "num_comments": 63,
              "num_empathy": 6,
              "num_interests": 6,
              "num_likes": 341,
              "num_reposts": 52,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132926778309808128/",
              "reshared": false,
              "text": "🎉💥Helpful Resources to Land your First Job or Internship in 2023💯\n\n\n\n📍Sites to get an Internship💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed - https://in.indeed.com\n\nInternshala - https://lnkd.in/dGGFv5tq\n\nGlassdoor - https://lnkd.in/daG2cCYF\n\nIdealist.org - https://lnkd.in/d_VErnK8\n\nAbsolute Internship - https://lnkd.in/drUaknHb\n\nLooksharp - https://looksharp.global\n\nIntern Queen Inc. - https://lnkd.in/dur9dcdt\n\nInternship Programs - https://lnkd.in/dTmwRW_D\n\nAlma Mater - https://lnkd.in/d5PpdVPj\n\n\n\n\n📍Sites for your Job Search💥\n\nLinkedIn - https://www.linkedin.com\n\nIndeed.com - https://in.indeed.com\n\nDice - https://www.dice.com\n\nGlassdoor - https://lnkd.in/daG2cCyF\n\nIdealist.org - https://www.idealist.org\n\nCareerBuilder - https://lnkd.in/dbhKHp-B\n\nLinkup - https://www.linkup.com\n\nGoogle For Jobs - https://lnkd.in/dkDQy6Hn\n\nMonster - https://www.foundit.in\n\nUS Jobs - https://www.usajobs.gov \n\n\n\n\n📍Sites to Build your Resume💥\n\nCanva - https://www.canva.com\n\nKickresume - https://lnkd.in/drhBTXJD\n\nVisualCV - https://www.visualcv.com\n\nZety: Resume Builder & Career Website - https://zety.com\n\nNovorésumé - https://novoresume.com\n\nMyPerfectResume - https://lnkd.in/dkp233pW\n\nResume Genius - https://resumegenius.com\n\nPongo - https://lnkd.in/dCrjBZWF\n\nCreddle-Dev- http://creddle.io\n\n\n\n\n📍Sites to Learn Tech Skills💥\n\nTreehouse - https://teamtreehouse.com\n\nKhan Academy - https://lnkd.in/d-Q2bM64\n\nCodeSchool - https://www.codeschool.co\n\nedX - https://www.edx.org\n\nCoursera - https://www.coursera.org\n\nCodewars - https://www.codewars.com\n\nfreeCodeCamp - https://lnkd.in/dcS6uxcH\n\nGitHub - https://github.com\n\nThe Odin Project - https://lnkd.in/dYQCAvdM \n\nW3Schools.com - https://www.w3schools.com\n\n\n\n\nFollow Vijay Chollangi 🛡  for more.\n\n\n#internships #resumewriting #jobs #career ",
              "time": "2d",
              "urn": "7132926778309808128"
            },
            {
              "document": {
                "page_count": 9,
                "title": "Must Read 📚 books",
                "url": "https://media.licdn.com/dms/document/media/D4D1FAQGzNtxW9KtZrA/feedshare-document-url-metadata-scrapper-pdf/0/1700580348423?e=1701417600&v=beta&t=dnQEHEe9I0MeUkMU7uUCbL5Gc9RnBWMs3fYwX-e0Hh8"
              },
              "images": [],
              "num_appreciations": 3,
              "num_comments": 47,
              "num_empathy": 3,
              "num_interests": 6,
              "num_likes": 274,
              "num_reposts": 28,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132892217140002817/",
              "reshared": false,
              "text": "😊Books You must read Before 30s💥🎉\n\n📍Reading books offers numerous benefits that can enrich our lives in various ways. Here are some compelling reasons why you should consider reading books:\n\n◆ Expands knowledge and learning.\n\n◆ Enhances vocabulary and language skills.\n\n◆ Promotes critical thinking.\n\n◆ Sparks imagination and creativity.\n\nReduces stress and offers escapism.\n\n◆ Cultivates empathy and understanding.\n\n◆ Improves concentration and focus.\n\n◆ Stimulates mental activity.\n\n◆ Facilitates personal growth.\n\n◆ Provides entertainment and enjoyment.\n\n◆ Offers inspiration and motivation.\n\n◆ Fosters social connections through shared reading experiences.\n\nFollow Vijay Chollangi 🛡  for more amazing content.\n\n#job #career #development #connections #ai #aidesign #communication #jobsearch #content #resume #softwaredevelopment #software #projects ",
              "time": "2d",
              "urn": "7132892217140002817"
            },
            {
              "images": [],
              "num_appreciations": 8,
              "num_comments": 68,
              "num_empathy": 17,
              "num_interests": 6,
              "num_likes": 576,
              "num_praises": 3,
              "num_reposts": 53,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132892189767987200/",
              "reshared": false,
              "text": "📍IT Companies in India.🎉💥\n\nApply here directly: (Share and comment for better reach)\n\n📍Company Career page Links:\n\n📍Google: https://lnkd.in/dKsmuXfh\n\n📍Amazon: https://lnkd.in/diJJqyr3\n\n📍intel: https://lnkd.in/d-QWtEfm\n\n📍Microsoft: https://lnkd.in/dTxGD7cy\n\n📍Mastercard: https://lnkd.in/dB83H-Jb\n\n📍nVIDIA: https://lnkd.in/dczs5y6d\n\n📍HARMAN: https://lnkd.in/dGr2bJiB\n\n📍Myntra: https://lnkd.in/d5NXB3Sw\n\n📍Flipkart: https://lnkd.in/dXR-mxQN\n\n📍Shell: https://lnkd.in/dzJiiFdF\n\n📍Siemens: https://lnkd.in/dDmAxYa6\n\n📍IBM: https://lnkd.in/d5QQgu7K\n\n📍Gap Inc: https://lnkd.in/dGyaAHRe\n\n📍Adobe: https://lnkd.in/d9jAyH4F\n\n📍Nike: https://lnkd.in/dxkGKZJi\n\n📍Moodys: https://lnkd.in/dm_u8S2r\n\n📍Mountblue: https://lnkd.in/dmivq6Zi\n\n📍Zycus: https://lnkd.in/gxUPvqxh\n\n📍Appypie: https://lnkd.in/gyScNsqj\n\n📍Tata Technologies: https://lnkd.in/d745BKSW\n\n📍Trimble: https://lnkd.in/dYHrXxnP\n\n📍Forcepoint: https://lnkd.in/dpebxvMN\n\n📍Siemens: https://lnkd.in/dWcE87ih\n\n📍DXC Technology: https://lnkd.in/ddWkRdCb\n\n📍BT Group: https://lnkd.in/d9zzwsav\n\n📍Ziplr: https://lnkd.in/dipniyrk\n\n📍Volvo: https://lnkd.in/dgfyUDwM\n\n📍ECI: https://lnkd.in/dRenRqFH\n\n📍Zoho: https://lnkd.in/dE5sE4-4\n\n📍Oracle: https://lnkd.in/d65KpPNq\n\n📍Morgan Stanley: https://lnkd.in/dxZkxkDx\n\n📍MoEngage: https://lnkd.in/dJQ9f55P\n\n📍JPMorgan: https://lnkd.in/d5q8E8x5\n\n📍Publicis Sapient: https://lnkd.in/dP8bjEcP\n\n📍Practo: https://lnkd.in/drTghJ9i\n\n📍Boston Consulting Group: https://lnkd.in/da7tUq6X\n\n📍PayPal: https://lnkd.in/dBadunAQ\n\n📍ABB: https://lnkd.in/d9H3xNcQ\n\n📍Mercedes Benz: https://lnkd.in/d9xY8Jak\n\n📍Tiger Analytics: https://lnkd.in/dR8uxR2P\n\n📍HP: https://lnkd.in/dJGUZHRS\n\n📍NetApp: https://lnkd.in/dPgQMsxr\n\n📍Airbus: https://lnkd.in/d9q_FKGg\n\n📍Phenom: https://lnkd.in/de57miGs\n\n📍Autodesk: https://lnkd.in/djGBv9Xg\n\n📍Salesforce: https://lnkd.in/dejdyvrW\n\n📍Goldman Sachs: https://lnkd.in/d4ak78sV\n\n📍Hexagon: https://lnkd.in/diZHrDEF\n\n📍Cisco: https://lnkd.in/dxDXGG_f\n\n📍Deutsche Bank: https://lnkd.in/dkq3dWhU\n\n📍Motorola: https://lnkd.in/d7hydH7n\n\n📍Renault: https://lnkd.in/dxSXFzW5\n\n📍SAP: https://lnkd.in/dcSqU5jb Societe\n\n📍 Generale: https://lnkd.in/dFXdCZFJ\n\n📍Atlassians: https://lnkd.in/dqtjnJcE\n\n📍Netflix: https://lnkd.in/d93NecpY\n\n📍Nissan: https://lnkd.in/dgAtM8_W\n\n📍Accenture: https://lnkd.in/dSm_JtF\n\n 📍Dell: https://lnkd.in/dutdNS8E\n\nFor more such information content follow Vijay Chollangi 🛡 \n\n#itcompany #indiajobs #companies #jobshiring #google ",
              "time": "2d",
              "urn": "7132892189767987200",
              "video": {
                "duration": 32000,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4E05AQGx3zPr4bsdww/feedshare-ambry-analyzed_servable_progressive_video/0/1700559190812?e=1701417600&v=beta&t=0qZPc6ODB5p_4zcPibI4_NJI5Si5WBq_FCgJ5cojaEk"
              }
            },
            {
              "document": {
                "page_count": 9,
                "title": "Must Read 📚 books",
                "url": "https://media.licdn.com/dms/document/media/D4D1FAQGzNtxW9KtZrA/feedshare-document-url-metadata-scrapper-pdf/0/1700580348423?e=1701417600&v=beta&t=dnQEHEe9I0MeUkMU7uUCbL5Gc9RnBWMs3fYwX-e0Hh8"
              },
              "images": [],
              "num_appreciations": 3,
              "num_comments": 47,
              "num_empathy": 3,
              "num_interests": 6,
              "num_likes": 274,
              "num_reposts": 28,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132831627847598080/",
              "reshared": false,
              "text": "😊Books You must read Before 30s💥🎉\n\n📍Reading books offers numerous benefits that can enrich our lives in various ways. Here are some compelling reasons why you should consider reading books:\n\n◆ Expands knowledge and learning.\n\n◆ Enhances vocabulary and language skills.\n\n◆ Promotes critical thinking.\n\n◆ Sparks imagination and creativity.\n\nReduces stress and offers escapism.\n\n◆ Cultivates empathy and understanding.\n\n◆ Improves concentration and focus.\n\n◆ Stimulates mental activity.\n\n◆ Facilitates personal growth.\n\n◆ Provides entertainment and enjoyment.\n\n◆ Offers inspiration and motivation.\n\n◆ Fosters social connections through shared reading experiences.\n\nFollow Vijay Chollangi 🛡  for more amazing content.\n\n#job #career #development #connections #ai #aidesign #communication #jobsearch #content #resume #softwaredevelopment #software #projects ",
              "time": "2d",
              "urn": "7132831627847598080"
            },
            {
              "document": {
                "page_count": 9,
                "title": "Must Read 📚 books",
                "url": "https://media.licdn.com/dms/document/media/D4D1FAQGzNtxW9KtZrA/feedshare-document-url-metadata-scrapper-pdf/0/1700580348423?e=1701417600&v=beta&t=dnQEHEe9I0MeUkMU7uUCbL5Gc9RnBWMs3fYwX-e0Hh8"
              },
              "images": [],
              "num_appreciations": 3,
              "num_comments": 47,
              "num_empathy": 3,
              "num_interests": 6,
              "num_likes": 274,
              "num_reposts": 28,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132779252382396416/",
              "reshared": false,
              "text": "😊Books You must read Before 30s💥🎉\n\n📍Reading books offers numerous benefits that can enrich our lives in various ways. Here are some compelling reasons why you should consider reading books:\n\n◆ Expands knowledge and learning.\n\n◆ Enhances vocabulary and language skills.\n\n◆ Promotes critical thinking.\n\n◆ Sparks imagination and creativity.\n\nReduces stress and offers escapism.\n\n◆ Cultivates empathy and understanding.\n\n◆ Improves concentration and focus.\n\n◆ Stimulates mental activity.\n\n◆ Facilitates personal growth.\n\n◆ Provides entertainment and enjoyment.\n\n◆ Offers inspiration and motivation.\n\n◆ Fosters social connections through shared reading experiences.\n\nFollow Vijay Chollangi 🛡  for more amazing content.\n\n#job #career #development #connections #ai #aidesign #communication #jobsearch #content #resume #softwaredevelopment #software #projects ",
              "time": "2d",
              "urn": "7132779252382396416"
            },
            {
              "images": [],
              "num_appreciations": 8,
              "num_comments": 68,
              "num_empathy": 17,
              "num_interests": 6,
              "num_likes": 576,
              "num_praises": 3,
              "num_reposts": 53,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132779219096371200/",
              "reshared": false,
              "text": "📍IT Companies in India.🎉💥\n\nApply here directly: (Share and comment for better reach)\n\n📍Company Career page Links:\n\n📍Google: https://lnkd.in/dKsmuXfh\n\n📍Amazon: https://lnkd.in/diJJqyr3\n\n📍intel: https://lnkd.in/d-QWtEfm\n\n📍Microsoft: https://lnkd.in/dTxGD7cy\n\n📍Mastercard: https://lnkd.in/dB83H-Jb\n\n📍nVIDIA: https://lnkd.in/dczs5y6d\n\n📍HARMAN: https://lnkd.in/dGr2bJiB\n\n📍Myntra: https://lnkd.in/d5NXB3Sw\n\n📍Flipkart: https://lnkd.in/dXR-mxQN\n\n📍Shell: https://lnkd.in/dzJiiFdF\n\n📍Siemens: https://lnkd.in/dDmAxYa6\n\n📍IBM: https://lnkd.in/d5QQgu7K\n\n📍Gap Inc: https://lnkd.in/dGyaAHRe\n\n📍Adobe: https://lnkd.in/d9jAyH4F\n\n📍Nike: https://lnkd.in/dxkGKZJi\n\n📍Moodys: https://lnkd.in/dm_u8S2r\n\n📍Mountblue: https://lnkd.in/dmivq6Zi\n\n📍Zycus: https://lnkd.in/gxUPvqxh\n\n📍Appypie: https://lnkd.in/gyScNsqj\n\n📍Tata Technologies: https://lnkd.in/d745BKSW\n\n📍Trimble: https://lnkd.in/dYHrXxnP\n\n📍Forcepoint: https://lnkd.in/dpebxvMN\n\n📍Siemens: https://lnkd.in/dWcE87ih\n\n📍DXC Technology: https://lnkd.in/ddWkRdCb\n\n📍BT Group: https://lnkd.in/d9zzwsav\n\n📍Ziplr: https://lnkd.in/dipniyrk\n\n📍Volvo: https://lnkd.in/dgfyUDwM\n\n📍ECI: https://lnkd.in/dRenRqFH\n\n📍Zoho: https://lnkd.in/dE5sE4-4\n\n📍Oracle: https://lnkd.in/d65KpPNq\n\n📍Morgan Stanley: https://lnkd.in/dxZkxkDx\n\n📍MoEngage: https://lnkd.in/dJQ9f55P\n\n📍JPMorgan: https://lnkd.in/d5q8E8x5\n\n📍Publicis Sapient: https://lnkd.in/dP8bjEcP\n\n📍Practo: https://lnkd.in/drTghJ9i\n\n📍Boston Consulting Group: https://lnkd.in/da7tUq6X\n\n📍PayPal: https://lnkd.in/dBadunAQ\n\n📍ABB: https://lnkd.in/d9H3xNcQ\n\n📍Mercedes Benz: https://lnkd.in/d9xY8Jak\n\n📍Tiger Analytics: https://lnkd.in/dR8uxR2P\n\n📍HP: https://lnkd.in/dJGUZHRS\n\n📍NetApp: https://lnkd.in/dPgQMsxr\n\n📍Airbus: https://lnkd.in/d9q_FKGg\n\n📍Phenom: https://lnkd.in/de57miGs\n\n📍Autodesk: https://lnkd.in/djGBv9Xg\n\n📍Salesforce: https://lnkd.in/dejdyvrW\n\n📍Goldman Sachs: https://lnkd.in/d4ak78sV\n\n📍Hexagon: https://lnkd.in/diZHrDEF\n\n📍Cisco: https://lnkd.in/dxDXGG_f\n\n📍Deutsche Bank: https://lnkd.in/dkq3dWhU\n\n📍Motorola: https://lnkd.in/d7hydH7n\n\n📍Renault: https://lnkd.in/dxSXFzW5\n\n📍SAP: https://lnkd.in/dcSqU5jb Societe\n\n📍 Generale: https://lnkd.in/dFXdCZFJ\n\n📍Atlassians: https://lnkd.in/dqtjnJcE\n\n📍Netflix: https://lnkd.in/d93NecpY\n\n📍Nissan: https://lnkd.in/dgAtM8_W\n\n📍Accenture: https://lnkd.in/dSm_JtF\n\n 📍Dell: https://lnkd.in/dutdNS8E\n\nFor more such information content follow Vijay Chollangi 🛡 \n\n#itcompany #indiajobs #companies #jobshiring #google ",
              "time": "2d",
              "urn": "7132779219096371200",
              "video": {
                "duration": 32000,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4E05AQGx3zPr4bsdww/feedshare-ambry-analyzed_servable_progressive_video/0/1700559190812?e=1701417600&v=beta&t=0qZPc6ODB5p_4zcPibI4_NJI5Si5WBq_FCgJ5cojaEk"
              }
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQEtO6Hi4m1xMw/feedshare-shrink_2048_1536/0/1700181043118?e=1703721600&v=beta&t=o-R6g7PNQkBOZrM4KH6-voT-8XK9inkzTqNt5TFoyKE"
                }
              ],
              "num_appreciations": 15,
              "num_comments": 97,
              "num_empathy": 38,
              "num_interests": 8,
              "num_likes": 1324,
              "num_praises": 5,
              "num_reposts": 58,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132777778629771264/",
              "reshared": false,
              "text": "🎯𝐋𝐞𝐚𝐝 𝐛𝐲 𝐄𝐱𝐚𝐦𝐩𝐥𝐞💼💥\n\n💡Leadership isn't about commands; it's about setting the pace through action.🎉💯\n\n📍Exceptional leaders lead by example, demonstrating the way forward through their actions.\n\n📍Instead of dictating, they inspire by actively participating in the challenges they present.\n\n📍A great leader's guidance is felt through their work ethic and commitment to excellence.\n\n📍They cultivate a culture of collaboration and continuous improvement by embodying the values they preach.\n\n📍By showing resilience in the face of adversity, they inspire their team to persevere and overcome obstacles.\n\n📍Effective leaders are hands-on, diving into the trenches alongside their team to drive success.\n\n📍Their ability to exemplify the desired outcome fosters trust and respect among team members.\n\n📍Through their actions, leaders instill a sense of purpose, aligning the team towards common goals.\n\n📍Leading through demonstration creates a dynamic and motivated workforce.\n\n\n📍In essence, great leaders don't just lead; they inspire others to follow through the power of their own example.\n\n\n. #Leadership #LeadByExample #SuccessInAction #motivation #success #linkedin ",
              "time": "1w",
              "urn": "7132777778629771264"
            },
            {
              "document": {
                "page_count": 9,
                "title": "Must Read 📚 books",
                "url": "https://media.licdn.com/dms/document/media/D4D1FAQGzNtxW9KtZrA/feedshare-document-url-metadata-scrapper-pdf/0/1700580348423?e=1701417600&v=beta&t=dnQEHEe9I0MeUkMU7uUCbL5Gc9RnBWMs3fYwX-e0Hh8"
              },
              "images": [],
              "num_appreciations": 3,
              "num_comments": 47,
              "num_empathy": 3,
              "num_interests": 6,
              "num_likes": 274,
              "num_reposts": 28,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132766174446034944/",
              "reshared": false,
              "text": "😊Books You must read Before 30s💥🎉\n\n📍Reading books offers numerous benefits that can enrich our lives in various ways. Here are some compelling reasons why you should consider reading books:\n\n◆ Expands knowledge and learning.\n\n◆ Enhances vocabulary and language skills.\n\n◆ Promotes critical thinking.\n\n◆ Sparks imagination and creativity.\n\nReduces stress and offers escapism.\n\n◆ Cultivates empathy and understanding.\n\n◆ Improves concentration and focus.\n\n◆ Stimulates mental activity.\n\n◆ Facilitates personal growth.\n\n◆ Provides entertainment and enjoyment.\n\n◆ Offers inspiration and motivation.\n\n◆ Fosters social connections through shared reading experiences.\n\nFollow Vijay Chollangi 🛡  for more amazing content.\n\n#job #career #development #connections #ai #aidesign #communication #jobsearch #content #resume #softwaredevelopment #software #projects ",
              "time": "2d",
              "urn": "7132766174446034944"
            },
            {
              "document": {
                "page_count": 9,
                "title": "Must Read 📚 books",
                "url": "https://media.licdn.com/dms/document/media/D4D1FAQGzNtxW9KtZrA/feedshare-document-url-metadata-scrapper-pdf/0/1700580348423?e=1701417600&v=beta&t=dnQEHEe9I0MeUkMU7uUCbL5Gc9RnBWMs3fYwX-e0Hh8"
              },
              "images": [],
              "num_appreciations": 3,
              "num_comments": 47,
              "num_empathy": 3,
              "num_interests": 6,
              "num_likes": 274,
              "num_reposts": 28,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132751174515970049/",
              "reshared": false,
              "text": "😊Books You must read Before 30s💥🎉\n\n📍Reading books offers numerous benefits that can enrich our lives in various ways. Here are some compelling reasons why you should consider reading books:\n\n◆ Expands knowledge and learning.\n\n◆ Enhances vocabulary and language skills.\n\n◆ Promotes critical thinking.\n\n◆ Sparks imagination and creativity.\n\nReduces stress and offers escapism.\n\n◆ Cultivates empathy and understanding.\n\n◆ Improves concentration and focus.\n\n◆ Stimulates mental activity.\n\n◆ Facilitates personal growth.\n\n◆ Provides entertainment and enjoyment.\n\n◆ Offers inspiration and motivation.\n\n◆ Fosters social connections through shared reading experiences.\n\nFollow Vijay Chollangi 🛡  for more amazing content.\n\n#job #career #development #connections #ai #aidesign #communication #jobsearch #content #resume #softwaredevelopment #software #projects ",
              "time": "2d",
              "urn": "7132751174515970049"
            },
            {
              "images": [],
              "num_appreciations": 8,
              "num_comments": 68,
              "num_empathy": 17,
              "num_interests": 6,
              "num_likes": 576,
              "num_praises": 3,
              "num_reposts": 53,
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7132734335467614208/",
              "reshared": false,
              "text": "📍IT Companies in India.🎉💥\n\nApply here directly: (Share and comment for better reach)\n\n📍Company Career page Links:\n\n📍Google: https://lnkd.in/dKsmuXfh\n\n📍Amazon: https://lnkd.in/diJJqyr3\n\n📍intel: https://lnkd.in/d-QWtEfm\n\n📍Microsoft: https://lnkd.in/dTxGD7cy\n\n📍Mastercard: https://lnkd.in/dB83H-Jb\n\n📍nVIDIA: https://lnkd.in/dczs5y6d\n\n📍HARMAN: https://lnkd.in/dGr2bJiB\n\n📍Myntra: https://lnkd.in/d5NXB3Sw\n\n📍Flipkart: https://lnkd.in/dXR-mxQN\n\n📍Shell: https://lnkd.in/dzJiiFdF\n\n📍Siemens: https://lnkd.in/dDmAxYa6\n\n📍IBM: https://lnkd.in/d5QQgu7K\n\n📍Gap Inc: https://lnkd.in/dGyaAHRe\n\n📍Adobe: https://lnkd.in/d9jAyH4F\n\n📍Nike: https://lnkd.in/dxkGKZJi\n\n📍Moodys: https://lnkd.in/dm_u8S2r\n\n📍Mountblue: https://lnkd.in/dmivq6Zi\n\n📍Zycus: https://lnkd.in/gxUPvqxh\n\n📍Appypie: https://lnkd.in/gyScNsqj\n\n📍Tata Technologies: https://lnkd.in/d745BKSW\n\n📍Trimble: https://lnkd.in/dYHrXxnP\n\n📍Forcepoint: https://lnkd.in/dpebxvMN\n\n📍Siemens: https://lnkd.in/dWcE87ih\n\n📍DXC Technology: https://lnkd.in/ddWkRdCb\n\n📍BT Group: https://lnkd.in/d9zzwsav\n\n📍Ziplr: https://lnkd.in/dipniyrk\n\n📍Volvo: https://lnkd.in/dgfyUDwM\n\n📍ECI: https://lnkd.in/dRenRqFH\n\n📍Zoho: https://lnkd.in/dE5sE4-4\n\n📍Oracle: https://lnkd.in/d65KpPNq\n\n📍Morgan Stanley: https://lnkd.in/dxZkxkDx\n\n📍MoEngage: https://lnkd.in/dJQ9f55P\n\n📍JPMorgan: https://lnkd.in/d5q8E8x5\n\n📍Publicis Sapient: https://lnkd.in/dP8bjEcP\n\n📍Practo: https://lnkd.in/drTghJ9i\n\n📍Boston Consulting Group: https://lnkd.in/da7tUq6X\n\n📍PayPal: https://lnkd.in/dBadunAQ\n\n📍ABB: https://lnkd.in/d9H3xNcQ\n\n📍Mercedes Benz: https://lnkd.in/d9xY8Jak\n\n📍Tiger Analytics: https://lnkd.in/dR8uxR2P\n\n📍HP: https://lnkd.in/dJGUZHRS\n\n📍NetApp: https://lnkd.in/dPgQMsxr\n\n📍Airbus: https://lnkd.in/d9q_FKGg\n\n📍Phenom: https://lnkd.in/de57miGs\n\n📍Autodesk: https://lnkd.in/djGBv9Xg\n\n📍Salesforce: https://lnkd.in/dejdyvrW\n\n📍Goldman Sachs: https://lnkd.in/d4ak78sV\n\n📍Hexagon: https://lnkd.in/diZHrDEF\n\n📍Cisco: https://lnkd.in/dxDXGG_f\n\n📍Deutsche Bank: https://lnkd.in/dkq3dWhU\n\n📍Motorola: https://lnkd.in/d7hydH7n\n\n📍Renault: https://lnkd.in/dxSXFzW5\n\n📍SAP: https://lnkd.in/dcSqU5jb Societe\n\n📍 Generale: https://lnkd.in/dFXdCZFJ\n\n📍Atlassians: https://lnkd.in/dqtjnJcE\n\n📍Netflix: https://lnkd.in/d93NecpY\n\n📍Nissan: https://lnkd.in/dgAtM8_W\n\n📍Accenture: https://lnkd.in/dSm_JtF\n\n 📍Dell: https://lnkd.in/dutdNS8E\n\nFor more such information content follow Vijay Chollangi 🛡 \n\n#itcompany #indiajobs #companies #jobshiring #google ",
              "time": "2d",
              "urn": "7132734335467614208",
              "video": {
                "duration": 32000,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4E05AQGx3zPr4bsdww/feedshare-ambry-analyzed_servable_progressive_video/0/1700559190812?e=1701417600&v=beta&t=0qZPc6ODB5p_4zcPibI4_NJI5Si5WBq_FCgJ5cojaEk"
              }
            }
          ],
          "message": "ok",
          "paging": {
            "count": 50,
            "pagination_token": "dXJuOmxpOmFjdGl2aXR5OjcxMzI3MzQzMzU0Njc2MTQyMDgtMTcwMDU3NjM4NTM2Mg==",
            "start": 0
          }
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        #  Search Posts
        #  Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/search-posts') and
            i.nice_name == "Search Posts")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": [
            {
              "num_comments": [
                0
              ],
              "num_likes": 0,
              "num_shares": null,
              "post_type": "article",
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7188717065229291520/",
              "posted": "2024-04-24 01:55:08",
              "poster_linkedin_url": "https://www.linkedin.com/in/ACoAAB0Ep3UB5q1KTrEnopcszHbmWS7QwINCZu0?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAB0Ep3UB5q1KTrEnopcszHbmWS7QwINCZu0",
              "poster_name": "Richard Cupal, LPT",
              "poster_title": "Full-Time College IT Instructor at Talisay City College",
              "text": "Learning how to earn extra money in the internet is ❤️ \n\n#rebzone #sepirothx",
              "urn": "7188717065229291520"
            },
            {
              "num_comments": [
                1
              ],
              "num_likes": 2,
              "num_shares": null,
              "post_type": "article",
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7188687706657382401/",
              "posted": "2024-04-23 23:58:28",
              "poster_linkedin_url": "https://www.linkedin.com/in/ACoAAABdXUEBBgUSMSyTH7Oox4CAmZ9jUlyHFl0?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAABdXUEBBgUSMSyTH7Oox4CAmZ9jUlyHFl0",
              "poster_name": "Per Ohstrom",
              "poster_title": "Fractional CMO and Partner | Servant Leader | B2B Marketing | Strategy | New Products | Industrial Services | Manufacturing | Board of Directors",
              "text": "William Collins shares some great insights around personality types and #marketing! ",
              "urn": "7188687706657382401"
            },
            {
              "num_comments": [
                0
              ],
              "num_likes": 0,
              "num_shares": null,
              "post_type": "article",
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7188701040282681344/",
              "posted": "2024-04-24 00:51:27",
              "poster_linkedin_url": "https://www.linkedin.com/in/ACoAADSe4VEBd0PbuY4rPSo84Th5-7KXz-X-eqk?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAADSe4VEBd0PbuY4rPSo84Th5-7KXz-X-eqk",
              "poster_name": "Frederic Thomas",
              "poster_title": "Founder of Veenest | Digital Marketing Strategist | Specializing in Web Design, Content Marketing, Branding, SEO, and Social Media Management for real estate, home improvement, regenerative, holistic and precision health",
              "text": "A treasure trove of valuable resources for real estate professionals. \n#realestate #digitalmarketing #veenest #veenestmarketing",
              "urn": "7188701040282681344"
            },
            {
              "num_comments": [
                0
              ],
              "num_likes": 0,
              "num_shares": null,
              "post_type": "article",
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7188709325933051906/",
              "posted": "2024-04-24 01:24:23",
              "poster_linkedin_url": "https://www.linkedin.com/company/the-hope-future/",
              "poster_name": "The Hope Future",
              "poster_title": "",
              "text": "My latest article on bold new leaders in the marketing and advertising industry.\n\nhttps://lnkd.in/gNQ5sBmi",
              "urn": "7188709325933051906"
            },
            {
              "num_comments": [
                6
              ],
              "num_likes": 12,
              "num_shares": null,
              "post_type": "article",
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7188694363189739520/",
              "posted": "2024-04-24 00:24:55",
              "poster_linkedin_url": "https://www.linkedin.com/in/ACoAAAAFICMB6eth1wZ26t5WgSk2a7IPMjN9dBM?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAAFICMB6eth1wZ26t5WgSk2a7IPMjN9dBM",
              "poster_name": "Jackie Yeaney",
              "poster_title": "Board Member | Advisor | Coach | Former CMO",
              "text": "Last week I had the privilege of guiding a robust member-only discussion with the CMO Collaborative on the topic of How to Approach Securing a Board Position.  My guests were Roxanne Taylor and Mary Egan–both career Marketing Executives, current Board members, and life-long friends of mine. \n\nHere is a short recap of our discussion (minus some of our personal stories).  Let me know if you have other pointers or questions. ",
              "urn": "7188694363189739520"
            },
            {
              "num_comments": [
                0
              ],
              "num_likes": 0,
              "num_shares": null,
              "post_type": "article",
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7188703203411013633/",
              "posted": "2024-04-24 01:00:03",
              "poster_linkedin_url": "https://www.linkedin.com/company/red-comm-indonesia/",
              "poster_name": "RED Comm Indonesia",
              "poster_title": "",
              "text": "🔥 Embrace These B2B Marketing Trends to Drive New Prospects in 2024 🚀 \n\n#B2BMarketing #2024Trends #BusinessGrowth ",
              "urn": "7188703203411013633"
            },
            {
              "num_comments": [
                0
              ],
              "num_likes": 1,
              "num_shares": null,
              "post_type": "article",
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7188692409801740291/",
              "posted": "2024-04-24 00:17:09",
              "poster_linkedin_url": "https://www.linkedin.com/company/gemedia2022/",
              "poster_name": "GEMedia",
              "poster_title": "",
              "text": "As a small business, integrating influencer marketing can be crucial for expanding your reach and driving growth. But how can you execute effective influencer campaigns within a limited budget?🤔\n\nDiscover actionable strategies and tips in our latest article below👇",
              "urn": "7188692409801740291"
            },
            {
              "num_comments": [
                0
              ],
              "num_likes": 0,
              "num_shares": null,
              "post_type": "article",
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7188683662312280065/",
              "posted": "2024-04-23 23:42:24",
              "poster_linkedin_url": "https://www.linkedin.com/in/ACoAABxmpHEBIUshg4Vg4QjpDvGxqvDdtRjCe3w?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABxmpHEBIUshg4Vg4QjpDvGxqvDdtRjCe3w",
              "poster_name": "Custom Packaging Pro For US",
              "poster_title": "SEO Expert",
              "text": "Gable Boxes have several benefits that make them an invaluable asset for any organization, from their utility and marketing potential to their simplicity of installation and customization options.\nGable Boxes, Eco-Friendly Boxes, Gable Packaging, Eco-Friendly Packaging, Custom Gable Boxes, Custom Eco-Friendly Boxes, Printed Gable Boxes, Printed Eco-Friendly Boxes, Printed Eco-Friendly Packaging, Gable Boxes Wholesale, Eco-Friendly Boxes Wholesale, Wholesale Gable Boxes, Custom Gable Packaging, Custom Eco-Friendly Packaging, Custom Printed Gable Boxes",
              "urn": "7188683662312280065"
            },
            {
              "num_comments": [
                0
              ],
              "num_likes": 0,
              "num_shares": null,
              "post_type": "article",
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7188692396346347521/",
              "posted": "2024-04-24 00:17:06",
              "poster_linkedin_url": "https://www.linkedin.com/company/hanaipartners/",
              "poster_name": "Hānai Marketing Partners",
              "poster_title": "",
              "text": "In the competitive landscape of food and beverage startups here in the tourism-fueled markets of #Hawaii, crafting a robust marketing plan can often seem daunting, especially when financial resources are limited. Here are 7 actionable strategies to develop a compelling marketing plan on a shoestring budget. #HanaiMarketing #HanaiPartners #MarketingStrategy",
              "urn": "7188692396346347521"
            },
            {
              "num_comments": [
                0
              ],
              "num_likes": 0,
              "num_shares": null,
              "post_type": "article",
              "post_url": "https://www.linkedin.com/feed/update/urn:li:activity:7188717000343404544/",
              "posted": "2024-04-24 01:54:52",
              "poster_linkedin_url": "https://www.linkedin.com/in/ACoAAAsZlz0BxuUAm7yV5B-P9khmt6aPKzv_QHA?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAsZlz0BxuUAm7yV5B-P9khmt6aPKzv_QHA",
              "poster_name": "Mark Khoder",
              "poster_title": "Restaurant Marketing Strategist For Restaurant Groups, Chains, Brands, National & International",
              "text": "You're not just in the food business; you're in the experience business. Invest in marketing the feeling, and watch your restaurant become the place everyone wants a taste of.",
              "urn": "7188717000343404544"
            }
          ],
          "message": "ok",
          "total": 486
        }\
        """
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Detect Activity Time
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-profile-recent-activity-time') and
            i.nice_name == "Detect Activity Time")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "recent_activity_time": "4d"
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Profile by Sales Nav URL
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-linkedin-profile-by-salesnavurl') and
            i.nice_name == "Get Profile by Sales Nav URL")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "about": "As a highly innovative, creative and technology-savvy individual with a passion for continuous learning and a natural talent for leadership, I am dedicated to driving positive change and shaping the future through ideas and innovation. With a proven track record of success and a drive to stay ahead of the curve, I am constantly seeking new challenges and opportunities to expand my knowledge and make an impact.\n\nMy experience in leading teams and implementing cutting-edge solutions has honed my ability to identify opportunities, overcome obstacles, and deliver results. I have a strong ability to bridge the gap between technology and business, leveraging my technical expertise and strategic thinking to drive meaningful change.\n\nWhether it's developing new solutions, commercialising existing ideas, mentoring and developing others, or staying on the forefront of emerging trends and technologies, I am constantly learning and growing. My insatiable curiosity and drive for excellence drive me to constantly seek new challenges and opportunities to make a difference.\n\nAs a visionary leader, I am always striving to create a better future and make a positive impact. Whether it's through ideas, creativity, products, cutting-edge technologies, or simply being a positive influence on those around me, I am always pushing the boundaries of what is possible.\n\nSo, if you're looking for someone who is passionate, driven, and committed to making a difference, look no further. I am eager to bring my skills, experience, and enthusiasm to the table and help drive the future of innovation and technology forward.",
            "city": "Sydney",
            "company": "Trinity Consulting Services",
            "company_domain": "",
            "company_employee_range": "2-10",
            "company_industry": "Advertising Services",
            "company_linkedin_url": "https://www.linkedin.com/company/trinity-consulting-services/",
            "company_logo_url": "https://media.licdn.com/dms/image/C4D0BAQGrLPvSJY2SNw/company-logo_400_400/0/1519932056711?e=1686787200&v=beta&t=eL16b3rEZ6NXK2IyIpkXGlRYrfYWolzJt5nifq7en70",
            "company_website": "https://www.linkedin.com/in/ajjames/",
            "company_year_founded": 2007,
            "connections_count": 500,
            "country": "Australia",
            "current_company_join_month": 5,
            "current_company_join_year": 2016,
            "educations": [
              {
                "activities": "",
                "date_range": "1990 - 1992",
                "degree": "Bachelor of Business, Marketing, Communications & Public Relations",
                "description": "",
                "eduId": 144921789,
                "end_month": "",
                "end_year": 1992,
                "field_of_study": "Marketing, Communications & Public Relations",
                "grade": "",
                "school": "University of Technology, Sydney",
                "school_id": "166678",
                "school_linkedin_url": "https://www.linkedin.com/company/166678/",
                "start_month": "",
                "start_year": 1990
              },
              {
                "activities": "",
                "date_range": "1986 - 1990",
                "degree": "Bachelor of Applied Science",
                "description": "",
                "eduId": 10472663,
                "end_month": "",
                "end_year": 1990,
                "field_of_study": "Computer Science & Information Science",
                "grade": "",
                "school": "",
                "school_id": "166678",
                "school_linkedin_url": "https://www.linkedin.com/company/166678/",
                "start_month": "",
                "start_year": 1986
              },
              {
                "activities": "",
                "date_range": "1978 - 1986",
                "degree": "Higher School Certificate",
                "description": "",
                "eduId": 54251304,
                "end_month": "",
                "end_year": 1986,
                "field_of_study": "Business/Commerce, General",
                "grade": "",
                "school": "Newington College",
                "school_id": "452716",
                "school_linkedin_url": "https://www.linkedin.com/company/452716/",
                "start_month": "",
                "start_year": 1978
              },
              {
                "activities": "",
                "date_range": "2000 - 2020",
                "degree": "Marketing, Sales, Growth",
                "description": "",
                "eduId": 503720954,
                "end_month": "",
                "end_year": 2020,
                "field_of_study": "Innovation, Commercialisation",
                "grade": "",
                "school": "Deep Asia Pacific Market Experience",
                "school_id": "",
                "school_linkedin_url": "",
                "start_month": "",
                "start_year": 2000
              }
            ],
            "experiences": [
              {
                "company": "Trinity Consulting Services",
                "company_id": "208844",
                "company_linkedin_url": "https://www.linkedin.com/company/208844",
                "company_logo_url": "",
                "current_company_join_month": 5,
                "current_company_join_year": 2016,
                "date_range": "May 2022 - present",
                "description": "If you’re ready to commercialise your idea to a global audience, to supercharge your digital transformation or to find growth in new markets then we can help!",
                "duration": "1 yr 1 mo",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "Sydney, New South Wales, Australia",
                "start_month": 5,
                "start_year": 2022,
                "title": "Chairperson of the Board"
              },
              {
                "company": "B2Bx",
                "company_id": "67952300",
                "company_linkedin_url": "https://www.linkedin.com/company/67952300",
                "company_logo_url": "",
                "date_range": "Nov 2021 - present",
                "description": "",
                "duration": "1 yr 7 mos",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "Sydney, New South Wales, Australia",
                "start_month": 11,
                "start_year": 2021,
                "title": "Chief Growth Officer & CEO"
              },
              {
                "company": "InfluencerActive",
                "company_id": "67952300",
                "company_linkedin_url": "https://www.linkedin.com/company/67952300",
                "company_logo_url": "",
                "date_range": "Oct 2020 - present",
                "description": "InfluencerActive is an influencer marketing platform that directly connects small and medium-sized brands and businesses with curated and vetted influencers to create a seamless marketplace for both buyer and influencer to engage. Influencers in the InfluencerActive network have built significant followings over traditional business channels. Their trusted voices are valued in both the B2C and B2B contexts.\n \nIn engaging with influencers through InfluencerActive, business owners can cut through the channel noise and marketing challenges of a fragmented media world. With Influencer Active, engagement is direct between business and influencer.",
                "duration": "2 yrs 8 mos",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "Greater Sydney Area",
                "start_month": 10,
                "start_year": 2020,
                "title": "Executive Director & Investor"
              },
              {
                "company": "Trinity Consulting Services",
                "company_id": "208844",
                "company_linkedin_url": "https://www.linkedin.com/company/208844",
                "company_logo_url": "",
                "date_range": "Apr 2020 - present",
                "description": "Working closely with clients to help them drive their growth strategy, digital transformation and generate new innovative ideas for global markets.",
                "duration": "3 yrs 2 mos",
                "end_month": "",
                "end_year": "",
                "is_current": true,
                "location": "Sydney, New South Wales, Australia",
                "start_month": 4,
                "start_year": 2020,
                "title": "Group CEO Innovation & Growth"
              },
              {
                "company": "Trinity Consulting Services",
                "company_id": "208844",
                "company_linkedin_url": "https://www.linkedin.com/company/208844",
                "company_logo_url": "",
                "date_range": "May 2016 - Mar 2021",
                "description": "Trinity Consulting Services [TCS] is a highly networked marketing strategy, innovation and business transformation agency, that works with brands who have a desire to increase their revenues and market share in some of the largest B2B and B2C markets in APAC (Asia Pacific) and EMEA (Europe, Middle East and Africa). \n\nI specifically help organisations generate additional revenues in these markets with creative, innovative and digital solutions - from up-front strategy to full tactical and practical implementation and roll-out planning.\n\nLeveraging my substantial APAC network and with a deep understanding of cultural differences and in-market influences across the target regions and countries, Trinity Consulting gives its partners the jump-start in digital and innovation that they often lack in penetrating new markets and delivering real, profitable solutions.\n\nTCS blends the creative and the strategic, within a highly flexible and dynamic framework. Assisting organisations to solve complex business problems and issues with the application of technology. Assisting in the packaging, presenting and pitching of solutions to potential markets, emerging markets and numerous industry verticals.\n\nWe have assisted organisations and provided measurable and profitable solutions to: Advertising, Business Travel & Leisure, Consumer Brands, Consumer Marketing, Digital / Online / Social Media, Entertainment, Fast Moving Consumer Goods (FMCG), Financial Services & FINTECH, Franchising, Health & Wellbeing, Information Technology, Media & Publishing, Promotions, Merchandising, Retail, Sports & Sponsorship, Quick Service Restaurants (QSR)\n\nRecent clients include: The Australia Government, Digital Transformation Agency, Nokia, News Corp Australia",
                "duration": "4 yrs 11 mos",
                "end_month": 3,
                "end_year": 2021,
                "is_current": false,
                "location": "APAC - Marketing, Transformation, Digital & Consumer Engagement",
                "start_month": 5,
                "start_year": 2016,
                "title": "Executive Director - Marketing, Innovation and Growth"
              },
              {
                "company": "DDB Group Asia Pacific",
                "company_id": "3524674",
                "company_linkedin_url": "https://www.linkedin.com/company/3524674",
                "company_logo_url": "",
                "date_range": "Mar 2015 - May 2016",
                "description": "As Chief Innovation Officer, Asia Pacific, I was tasked with taking head on, the challenge to: \n\n•  provide focus to DDB Group’s innovative business and marketing growth solutions\n•  commercialise new and existing digital and tech solutions to generate growth for agency clients\n•  engage creativity and innovation for drive long-term business growth for agency and clients\n•  apply creative thinking across business processes to deliver a competitive advantage and new revenue streams\n•  to connect the best minds within the agency in order to look at business problems from a different perspective\n\nAJ spearheaded the commercial success of innovative digital solutions for DDB's clients – from mobile apps to web-ordering systems to e-stores and interactive retail assets – as well as enhancing client revenue streams and customer engagement to 'hack' into creative business growth opportunities.",
                "duration": "1 yr 3 mos",
                "end_month": 5,
                "end_year": 2016,
                "is_current": false,
                "location": "Asia Pacific",
                "start_month": 3,
                "start_year": 2015,
                "title": "Chief Innovation & Growth Officer"
              },
              {
                "company": "Sample Central",
                "company_id": "814226",
                "company_linkedin_url": "https://www.linkedin.com/company/814226",
                "company_logo_url": "",
                "date_range": "Dec 2007 - Mar 2015",
                "description": "Sample Central is a unique retail / consumer product / insights / experience that places a focus on consumers, allowing them to try, touch, feel and experience products, and brand innovations before buying the products. As the pioneer of 'tryvertising' or try-before-you-buy, Sample Central ignites the conversation and interaction between brands and consumers, consumer who are willing to provide their insights about products or services they have chosen to explore or shown and interest in.\n\nHaving created the global go-to-market strategy, AJ was the driving-force behind launching the concept to the market, taking an active, hands-on approach selling the concept into brands and growing the business worldwide via a franchise framework.\n\nKEY ACHIEVEMENTS:\n•  Took the business global via a franchise model (custom built for the concept)\n•  Negotiated franchise agreements in over 20 countries in less than 5 years\n•  Established global and franchise level operational plans and budgets\n•  Coach, motivate and support new franchisees and business owners\n•  Play and active and key role selling the concept to brands globally\n•  Establish clear success metrics, systems and reporting arrangements\n•  Changed the FMCG landscape with a model that truly influences consumers purchasing decisions\n•  Built a robust, centralized, big-data engine, SaaS information management and software platform operating in over 10 languages supporting franchise partners and consumers worldwide",
                "duration": "7 yrs 4 mos",
                "end_month": 3,
                "end_year": 2015,
                "is_current": false,
                "location": "Worldwide, Japan, Brazil, USA, Middle East, Eastern Europe (Budapest), UK",
                "start_month": 12,
                "start_year": 2007,
                "title": "Group CEO Marketing and Innovation"
              },
              {
                "company": "Creata",
                "company_id": "21449",
                "company_linkedin_url": "https://www.linkedin.com/company/21449",
                "company_logo_url": "",
                "date_range": "2004 - Dec 2007",
                "description": "Creata is one of the largest marketing and sales promotions agencies in the world, serving some of the largest corporations including McDonald's, Kellogg's, Coca Cola, Nestle, & others since 1973.\n\nAJ took a key leadership role during his time at Creata & was part for the global management team. Working across 15 offices in 11 countries on 5 continents. And was responsible for the design & production of over 1.3 billion happy meal toys.\n\nMAIN RESPONSIBILITIES:\n• Setting creative direction and strategy for the agency globally\n• Focus the agency on innovation and idea generation built upon creative marketing & promotion strategies\n• Transitioned from a premiums manufacturer to a full-service creative & digital agency\n• Accelerate the pace of Creata’s ability to deliver a full spectrum of below-the-line marketing services\n• Leadership role in all major account pitches globally & was the driving force of the Company’s sales / marketing efforts\n\nKEY ACHIEVEMENTS: \n• Built and launched Creata Digital\n• Positioned Creata to be invited to pitch for global technology pitches with several of the Company’s global brand clients\n• Secured Creata's first large scale digital project with McDonald's against the incumbent digital agencies\n• Extend the HappyMeal.com franchise into Asia Pacific - Digital contract extended despite intense lobbying by rival agencies\n• Personally managed the relationship and negotiated the deals across North America, Europe & Asia\n• Restructured Creata's Creative division from a \"Support Function\" to a \"Business Unit\", having full P&L accountability\n• Established the relationship & negotiated the contract between Creata & China Central Television (CCTV) to secure the exclusive licensing rights to China's oldest & most recognised cartoon property. Drove the establishment of a separate business entity in the Chinese Free Trade Zone",
                "duration": "4 yrs",
                "end_month": 12,
                "end_year": 2007,
                "is_current": false,
                "location": "Worldwide - Asia Pacific, North America, Latin america, Europe, Middle East",
                "start_month": "",
                "start_year": 2004,
                "title": "Executive Vice-President Global Sales & Marketing"
              },
              {
                "company": "Fujitsu Consulting - Management Consulting / Digital Solutions",
                "company_id": "1374",
                "company_linkedin_url": "https://www.linkedin.com/company/1374",
                "company_logo_url": "",
                "date_range": "2000 - 2004",
                "description": "Fujitsu Consulting is one of the worlds top-tier global IT services organizations. With a focus on boosting efficiencies, cutting IT operational costs and create a sustainable competitive advantage with the client-focused IT consulting and integration services.\n\nAs Vice President of Marketing I was responsible for ensuring that clients business objectives were integrally linked to delivering true business value and the offerings of Fujitsu Consulting.\n\n• Directed the strategy, planning and implementation of all Fujitsu Consulting Asia Pacific internal and external corporate marketing activities supporting the business goals toward growth and profitability\n• Focus on solutions marketing\n• Ensured a consistent brand and message to the marketplace, making sure corporate style and standards were followed across all initiatives\n• Key executive on the Global Brand Program Team\n\n• As Director of eBusiness Solutions, Asia Pacific, provided focus, direction and leadership to position Fujitsu as the partner of choice for eBusiness solutions\n• Developed eBusiness solution offerings and the alignment to delivery capabilities",
                "duration": "4 yrs 5 mos",
                "end_month": "",
                "end_year": 2004,
                "is_current": false,
                "location": "Asia Pacific, Australia, New Zealand, Hong Kong, Japan",
                "start_month": "",
                "start_year": 2000,
                "title": "Vice-President Marketing & Digital, Asia Pacific"
              },
              {
                "company": "ZIVO Pty Limited - Digital / Web Solutions",
                "company_id": "",
                "company_linkedin_url": "",
                "company_logo_url": "",
                "date_range": "1999 - 2000",
                "description": "• All sales and marketing of Internet Solutions\n• Cross-industry focus, managing a team of Business Development Managers across Australia and New Zealand\n• Developed a ZIVO-wide business development and acquisition strategy\n• Negotiation of all intellectual property and professional services contracts\n• Lead engagement management for ZIVO clients including personal management of key accounts\n• Major influencer of the ZIVO marketing and branding strategies",
                "duration": "1 yr 5 mos",
                "end_month": "",
                "end_year": 2000,
                "is_current": false,
                "location": "Asia Pacific",
                "start_month": "",
                "start_year": 1999,
                "title": "Director, Sales, Marketing & Communications, Asia Pacific"
              },
              {
                "company": "IBM Global Services",
                "company_id": "1009",
                "company_linkedin_url": "https://www.linkedin.com/company/1009",
                "company_logo_url": "",
                "date_range": "1997 - 1999",
                "description": "• One of the key executives responsible for building and launching the IBM e-business Solutions team globally\n• Focused on a wide range of industry sectors, specialising in the banking & finance, entertainment, media, sports, travel, transport and tourism sectors across Asia Pacific\n• Lead the Asia Pacific sales team to ensure new business sign-off with clients\n• Played a leadership role in the relationship build, management and engagement of IBM e-business clients\n• Defined strategies for the marketing and sales of e-business and Interactive Media Design Studio services, including: internet/Intranet Solutions, CD-ROM, Kiosk, Electronic-commerce solutions, content creation cybercasting, digital design and print",
                "duration": "2 yrs 5 mos",
                "end_month": "",
                "end_year": 1999,
                "is_current": false,
                "location": "",
                "start_month": "",
                "start_year": 1997,
                "title": "Managing Consultant - eBusiness, Global"
              },
              {
                "company": "Computer Sciences Corporation (CSC)",
                "company_id": "1120",
                "company_linkedin_url": "https://www.linkedin.com/company/1120",
                "company_logo_url": "",
                "date_range": "1992 - 1997",
                "description": "• Established the MultiMedia Laboratory at CSC in Sydney and grew this to a global capability (and team of 350 people)\n• Project managed a variety of multimedia and Internet application design and development and implementation projects\n• Built processes for sales and client engagement\n• Full responsibility for major projects being delivered on time and within budget\n• Ensured all projects met quality assurance standards of CSC\n• Held the position of Worldwide Chair of the CSC Special Interest Group for MultiMedia and Interactive Technologies for 4 years, and through this time spent the majority of time in the United States speaking on the International Speakers Circuit",
                "duration": "5 yrs 5 mos",
                "end_month": "",
                "end_year": 1997,
                "is_current": false,
                "location": "",
                "start_month": "",
                "start_year": 1992,
                "title": "Internet Sales & Marketing Manager"
              },
              {
                "company": "IBM",
                "company_id": "1009",
                "company_linkedin_url": "https://www.linkedin.com/company/1009",
                "company_logo_url": "",
                "date_range": "Feb 1987 - Feb 1992",
                "description": "",
                "duration": "5 yrs 1 mo",
                "end_month": 2,
                "end_year": 1992,
                "is_current": false,
                "location": "Australia",
                "start_month": 2,
                "start_year": 1987,
                "title": "Interactive Designer and Programmer"
              },
              {
                "company": "Optical & Graphic Services",
                "company_id": "",
                "company_linkedin_url": "",
                "company_logo_url": "",
                "date_range": "Jan 1985 - Jan 1987",
                "description": "Optical & Graphic was established in January 1973 creating titles and shooting opticals for films including Peter Weir's Picnic at Hanging Rock, through to titles for Mad Max, The Man from Snowy River and Crocodile Dundee. O & G pioneered the use in Australia of shooting titles onto intermediate stock.",
                "duration": "2 yrs 1 mo",
                "end_month": 1,
                "end_year": 1987,
                "is_current": false,
                "location": "",
                "start_month": 1,
                "start_year": 1985,
                "title": "Graphic Designer / Computer Animator"
              }
            ],
            "first_name": "Anthony",
            "followers_count": 4081123,
            "full_name": "Anthony J James",
            "headline": "CEO, Innovation, Technology & Growth at Trinity Consulting",
            "hq_city": "Sydney",
            "hq_country": "Australia",
            "hq_region": "NSW",
            "job_title": "Chairperson of the Board",
            "last_name": "James",
            "linkedin_url": "https://www.linkedin.com/in/ajjames",
            "location": "Sydney, New South Wales, Australia",
            "profile_id": "4444590",
            "profile_image_url": "https://media.licdn.com/dms/image/D4D03AQH70ioIIQkzPg/profile-displayphoto-shrink_800_800/0/1674214515612?e=1690416000&v=beta&t=EN4_7JbdJextklwzAQA0vNVo5POn5hXGLs387PWyctU",
            "public_id": "ajjames",
            "redirected_url": "https://www.linkedin.com/in/ajjames",
            "school": "University of Technology, Sydney",
            "skills": "International Marketing, Social Media Marketing, Entrepreneurship, Business Strategy, Marketing Strategy, Strategic Planning, Strategy, Customer Insight, Brand Development, Brand Management, Marketing Management, Go-to-market Strategy, Direct Marketing, International Business, International Sales, Consumer Behaviour, Consumer Behavior, Product Management, FMCG, Change Management, Big Data, Content Strategy, Consumer Insights, Email Marketing, Franchising, Concept Development, Digital Media, Retail, Business Development, Marketing, E-commerce, Start-ups, Strategic Partnerships, Leadership, Managing Creative Teams, Innovation Management, Contract Negotiation, Management, Creative Problem Solving, Public Speaking, Global Management, Innovative Thinking, Idea Generation, Business Innovation, Concept Ideation, Free, Tryvertising, Campaigns, Concept Generation, Creative Direction",
            "state": "New South Wales"
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Company by URL
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-by-linkedinurl') and
            i.nice_name == "Get Company by URL")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "company_id": "162479",
            "company_name": "Apple",
            "description": "We’re a diverse collective of thinkers and doers, continually reimagining what’s possible to help us all do what we love in new ways. And the same innovation that goes into our products also applies to our practices — strengthening our commitment to leave the world better than we found it. This is where your work can make a difference in people’s lives. Including your own.\n\nApple is an equal opportunity employer that is committed to inclusion and diversity. Visit apple.com/careers to learn more.",
            "domain": "apple.com",
            "email": "",
            "employee_count": 271504,
            "employee_range": "10001+",
            "follower_count": 18590762,
            "hq_address_line1": "1 Apple Park Way",
            "hq_address_line2": "",
            "hq_city": "Cupertino",
            "hq_country": "United States",
            "hq_full_address": "1 Apple Park Way, Cupertino, California 95014, United States",
            "hq_postalcode": "95014",
            "hq_region": "California",
            "industries": [
              "Consumer Electronics"
            ],
            "linkedin_url": "https://www.linkedin.com/company/apple/",
            "locations": [
              {
                "city": "Cupertino",
                "country": "US",
                "full_address": "1 Apple Park Way, Cupertino, California 95014, US",
                "is_headquarter": true,
                "line1": "1 Apple Park Way",
                "line2": "",
                "region": "California",
                "zipcode": "95014"
              }
            ],
            "logo_url": "https://media.licdn.com/dms/image/C560BAQHdAaarsO-eyA/company-logo_400_400/0/1595530301220?e=1692835200&v=beta&t=dMZacSXgf5hSuO-M5sX2OcDJo64TlkEo3_7CQ0VB0Ak",
            "phone": null,
            "specialties": "Innovative Product Development, World-Class Operations, Retail, Telephone Support",
            "tagline": "",
            "type": "Public Company",
            "website": "http://www.apple.com/careers",
            "year_founded": 1976
          },
          "message": "ok"
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Company's Posts
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-posts') and
            i.nice_name == "Get Company's Posts")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": [
            {
              "article_subtitle": "aboutamazon.com • 8 min read",
              "article_title": "The FTC’s lawsuit against Amazon would lead to higher prices and slower deliveries for consumers—and hurt businesses",
              "images": [],
              "num_appreciations": 42,
              "num_comments": 66,
              "num_empathy": 11,
              "num_interests": 62,
              "num_likes": 1826,
              "num_praises": 18,
              "text": "We think the FTC’s lawsuit against Amazon is misguided.  Here’s our initial response.",
              "time": "1w",
              "url": "https://www.linkedin.com/posts/zapolsky_the-ftcs-lawsuit-against-amazon-would-lead-activity-7112527462189715456-BQMG",
              "urn": "7112833961902424065"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQHaLwPZ730gcg/feedshare-shrink_2048_1536/0/1695645376706?e=1699488000&v=beta&t=Bhg0PKLaUR0PV2joOAHzS9h3fGhQ_In3wbmapYxg6ag"
                }
              ],
              "num_appreciations": 17,
              "num_comments": 143,
              "num_empathy": 171,
              "num_interests": 28,
              "num_likes": 8163,
              "num_praises": 593,
              "text": "Excited to share we’re expanding our collaboration with Anthropic. AWS will now be Anthropic’s primary cloud provider and help build, train, and deploy its future foundation models on Trainium and Inferentia chips. I have tremendous respect for Dario, the Anthropic team, and their foundation models, and believe that together we can help improve many customer experiences. https://lnkd.in/g_Zpn5CG",
              "time": "1w",
              "url": "https://www.linkedin.com/posts/andy-jassy-8b1615_excited-to-share-were-expanding-our-collaboration-activity-7112052187530235904-ZCg8",
              "urn": "7112060934084276225"
            },
            {
              "images": [],
              "num_appreciations": 17,
              "num_comments": 155,
              "num_empathy": 222,
              "num_interests": 29,
              "num_likes": 7144,
              "num_praises": 481,
              "text": "Today, we announced our newest Amazon devices and the latest AI advancements powering them. It's an exciting step forward in our mission to make homes smarter and more helpful for customers. \n\nToday also marked the final Amazon launch for Dave Limp, who is moving on after 13 years leading this important and innovative business. Thanks for your many contributions, Dave, and congrats to the team on today’s launch!",
              "time": "1w",
              "url": "https://www.linkedin.com/posts/andy-jassy-8b1615_today-we-announced-our-newest-amazon-devices-ugcPost-7110356580289667073-RY5n",
              "urn": "7110362963051520000",
              "video": {
                "duration": 90566,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4E05AQHyQd0_zB4vyg/mp4-720p-30fp-crf28/0/1695241198480?e=1697000400&v=beta&t=z2wzaeRUuyRjj6pGRS2OudbSFFPZT9rEsI8o-b7biCQ"
              }
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGorYk3MMTyrg/image-shrink_1280/0/1695316081454?e=1697000400&v=beta&t=VwklL4io9gVFpFKwf0hAgowz6Uk8kxIsn1HA6t3rXWs"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQF-q4gylBh-fQ/image-shrink_1280/0/1695316082521?e=1697000400&v=beta&t=aoL4x-CG8MELA9SydyExh0zc0nMz9xyL9DViH_0n6x0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHjvDRQ-TVwig/image-shrink_1280/0/1695316083456?e=1697000400&v=beta&t=1-rSIZsMZf_DQ9iDWGWDOKPIwigfC33QsVdO1GulYWQ"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFnB9u9QoUf4Q/image-shrink_1280/0/1695316084809?e=1697000400&v=beta&t=woLl73REYfyQwLwjphhtivdMgd1R3pSHcCktCY47VQ4"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEeqpAL11uwIQ/image-shrink_1280/0/1695316085886?e=1697000400&v=beta&t=3E3nZsHyEj6AZN6NcPEnXOQAqLNoAc5aLeU0JoXa71w"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHzV0ou7dTqag/image-shrink_1280/0/1695316086803?e=1697000400&v=beta&t=P55vCFi2YDHj2zf0DrN1YWye-jpE0hb6bbqaFx9PqMc"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGuH4reUIGsYw/image-shrink_1280/0/1695316088102?e=1697000400&v=beta&t=hGtVZ0MT505n7u3iQmq76Rez_H67kzzQBHriuiyUhRw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHiXB5XvvT0yA/image-shrink_1280/0/1695316089504?e=1697000400&v=beta&t=c9_gXZXBPemiIdyNggQp0krul4oy4GUFt0mNBNl-vtw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHyDq7xs6HJkg/image-shrink_1280/0/1695316090667?e=1697000400&v=beta&t=m4tdNhGkwv25CwiQsT_wjdOGCoLfRXdlYF2dD7kB8tU"
                }
              ],
              "num_appreciations": 18,
              "num_comments": 108,
              "num_empathy": 149,
              "num_interests": 14,
              "num_likes": 4561,
              "num_praises": 163,
              "text": "This week we hosted our annual Devices & Services event. There is so much new, cool stuff that we are SO excited to share with you. Let’s get into it. ⬇️ \n\nIntroducing Echo Show 8.\n🆕 One of our most ambient devices yet. Featuring a sleek new design and upgraded hardware, your video calls just got a huge upgrade. 😎 ✨ Even better, we’ve added a built-in smart home hub, so you can easily control all your devices.\n\nIntroducing Echo Hub.\n🆕 Echo Hub is a new, mountable control panel powered by Amazon Alexa that allows you to (literally) tap 👇 in to control all of your smart home devices in one nifty place. Time to power-up all of your routines. \n\nWhat Else is New with Alexa?\n🆕 Eye gaze mode - an upcoming capability that will allow customers with speech or mobility disabilities to use Alexa with their eyes through the power of AI. 👀 \n🆕 Enhanced large language model (LLM) - experience deeper conversations with Alexa about a wider range of topics: stats from the football game you missed, details about something you heard on a podcast, or tips to get started on a new hobby. And you can combine multiple requests in a single ask: “Alexa, close the blinds, turn off the lights, and start the vacuum.” \n🆕 Fast access to emergency help - Anyone in your home can get hands-free, fast access to emergency help services with Alexa Emergency Assist. Just say, “Alexa, call for help.” 🆘 🚨\n\nLet’s talk Fire TV.\n🆕 Want your TV to better match your aesthetic when you’re not screening? With the new Ambient Experience available on Fire TV, you can display your family calendar, local weather, or even gallery artwork. The new Fire TV Stick 4K Max comes with the Ambient Experience making it Fire TV’s smartest and most powerful streaming stick. 🖼️\n🆕 Ever think to yourself, “Hmm, what to watch tonight?” Through conversational search on Fire TV, Alexa can make suggestions based on your interests and happens to be the best video store clerk in history. 📼 \n🆕 Fire TV Soundbar enhances content with immersive sound, crisper dialog, and improved bass—all in a compact design. \n\nUpdated Designs and Features with Echo Frames\n🆕 Our all-new smart glasses with Alexa – available in next-generation Echo Frames come in seven stylish new options, including two designs by Carrera Eyewear and Safilo Group. These are designed to make customers feel like they’re wearing a traditional pair of eyewear while benefiting from the convenience of Alexa on the go. 👓\n\nThe All New Ring Camera.\n🆕 The all new Ring Stick Up Cam Pro features 3D Motion Detection, Audio+, Color Pre-Roll, and Color Night Vision. And best of all it’s easy to install, and you can stick it anywhere.\n\nLearn about everything else here: https://amzn.to/3LySfPk",
              "time": "1w",
              "url": "https://www.linkedin.com/posts/amazon_this-week-we-hosted-our-annual-devices-activity-7110671067727220736-sNtr",
              "urn": "7110671067727220736"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGbmDpN7Wv20A/image-shrink_1280/0/1695393902900?e=1697000400&v=beta&t=xnCMU0OQ6TknAyJwo78ix2NFCXI5PWV5a3OiSwf3PUQ"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHHk2H0pS333w/image-shrink_1280/0/1695393904201?e=1697000400&v=beta&t=ZnjRSdgprpEIyvx1Rmtzgy0mu0v8VVvxV7s1-2ZCqag"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEpwjEUFI7qzA/image-shrink_1280/0/1695393906420?e=1697000400&v=beta&t=lWkICMHRsE2d0s71sMG3cbFvQfDSdxCB7IxylHS2bEU"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQH37Z0oa1bmtQ/image-shrink_1280/0/1695393907758?e=1697000400&v=beta&t=k6Gv3GMcGASXv2CThR_e-KnAVTtAZq5H5COtEqqyTCE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHTgfhbFaEDUw/image-shrink_1280/0/1695393909108?e=1697000400&v=beta&t=KP1QOQQ2n1ktkp7ZTdI9fqvq6j_NXu5AMETdGCs7LFI"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEk16muAboqZw/image-shrink_1280/0/1695393912002?e=1697000400&v=beta&t=fXw7dQdoH_v4AAKhx7IS_pgxu_znrPTcHRayoIkoB5c"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHE3MFpyyfD8Q/image-shrink_1280/0/1695393910860?e=1697000400&v=beta&t=6trqXH8MAHwzwBCBzOvOVLEA7FQ-F9xRhEU1XUulwWs"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGLtWTkBJoWTA/image-shrink_1280/0/1695393912401?e=1697000400&v=beta&t=BtLKEZ1GZdhhUATSHUEnR7sAtPwxrSRT9q9nl6mpxes"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEj3_Ga5BUDiw/image-shrink_1280/0/1695393913483?e=1697000400&v=beta&t=MLP-2UnH0tGqkTLwGtv_DyJH7hKiJXqGMaawPLD-xnA"
                }
              ],
              "num_appreciations": 21,
              "num_comments": 68,
              "num_empathy": 103,
              "num_interests": 2,
              "num_likes": 2895,
              "num_praises": 103,
              "text": "Wahoo! The energy continues into Week 3 of Global Month of Volunteering. Our employees truly are the most incredible, generous and inspiring people. We are so happy to have Amazonians all around the world that are giving back to their communities. Go give our volunteering heroes some love and positive encouragement in the comments! 💙 🌎 🧡 #AmazonGMV ",
              "time": "1w",
              "url": "https://www.linkedin.com/posts/amazon_amazongmv-activity-7110997482234384384-55ly",
              "urn": "7110997482234384384"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHuzWEFpwa9fQ/image-shrink_1280/0/1695666601831?e=1697000400&v=beta&t=iRZTUj3EMDbQeRLQdIYNyxayG5Vi7-v8lV8YCSUXFL8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQE4fTzuFDO2Kw/image-shrink_1280/0/1695666602202?e=1697000400&v=beta&t=-YspUd2oscJCu-xgRCu0nZIcoi6cKkXK9aSlJpxS8Yc"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQG3mCGdcVCgzg/image-shrink_1280/0/1695666603019?e=1697000400&v=beta&t=Wm4qHtxp6DaHyR4qQQWzYp6GR7m-lHkqOWiOmjvsClE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFUTB1Wiyj4wg/image-shrink_1280/0/1695666603768?e=1697000400&v=beta&t=23WpgLOSsAAkFzNtGVF1ODlxj2Yy2YmJir6Jxk49pPA"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFHyLQZgp7G1Q/image-shrink_1280/0/1695666604074?e=1697000400&v=beta&t=N9wOeTKQ58S8L_GzUP9i8WcsQWj3kzs4r8PMkJpDv-c"
                }
              ],
              "num_appreciations": 128,
              "num_comments": 95,
              "num_empathy": 783,
              "num_interests": 3,
              "num_likes": 5077,
              "num_praises": 55,
              "text": "Meet Aspen, a service dog with the need for speed. 🐶 ⚡\n\nShortly after Adam joined Amazon in 2021 as a technical infrastructure program manager, he had a heart attack and went on short-term leave. During his recovery, Adam began experiencing symptoms of post-traumatic stress disorder (PTSD) linked to his previous career in the U.S. Air Force. \n\nThat’s when Adam first met Aspen, a yellow Labrador retriever trained to help with his PTSD symptoms. Adam brings Aspen to work, and she is the best helper. She ensures he is safe, leads him into a comfortable location if he gets anxious, and is trained to get help if he were to fall.\n\nAs soon as her vest is put on Aspen is ready to go to work, just like her fellow Amazon employees. 🐾\n\nRead their story, and learn about our commitment to creating an inclusive and equitable workplace for everyone. ➡️ https://amzn.to/3EWLQJK\n\n#NationalServiceDogMonth #AmazonBenefits #InsideAmazon #DogsAtWork",
              "time": "1w",
              "url": "https://www.linkedin.com/posts/amazon_nationalservicedogmonth-amazonbenefits-insideamazon-activity-7112141226073587712-vIRo",
              "urn": "7112141226073587712"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEVujHqigke6g/image-shrink_1280/0/1695058082119?e=1697000400&v=beta&t=6GVm25f6hDG-GgCsTcGo01PP5iQF0rxx5iQv2rzB06s"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGbhvJM6KqrWg/image-shrink_1280/0/1695058083073?e=1697000400&v=beta&t=dWThwqVHefg7RHONriwerYzRFp8GfVKVfFAMfKo9Pco"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGPazdrX82lkQ/image-shrink_1280/0/1695058084603?e=1697000400&v=beta&t=xXxRBFP3gbFc1zfprcOk196xvAqe56wniBi9kjlAyzQ"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQE4HcM1kEPzCQ/image-shrink_1280/0/1695058084971?e=1697000400&v=beta&t=9i4xuy4gfSE5HLKIJIGnQEj7C-JT3IrtutV69MU2JPk"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEQmdzs9Zx-vg/image-shrink_1280/0/1695058086018?e=1697000400&v=beta&t=JqVD_5NnKyUFoiUiHsh2n0yCyEncY2k6BbcHMD33biE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQExYxWGzQJ0MA/image-shrink_1280/0/1695058086384?e=1697000400&v=beta&t=jaZGpghk-Kgb0qLWHe7hKWknE8dZ9rfa6Q7ak-DKcM0"
                }
              ],
              "num_appreciations": 7,
              "num_comments": 98,
              "num_empathy": 88,
              "num_interests": 72,
              "num_likes": 2320,
              "num_praises": 50,
              "text": "Imagine never having to wait in a checkout line at the store again. Well, you don’t need to imagine anymore. 💭 \n\nOur Just Walk Out Technology is exactly as it sounds. Just step inside a store, grab what you want, and leave. Simple as that. But pulling this off was no small feat. \n\nTo create this technology, Amazon Web Services (AWS) used a combination of computer vision, object recognition, advanced sensors, deep machine learning models, and generative AI – a type of artificial intelligence that has recently captured the public’s imagination.\n\nWe are so incredibly proud and thankful to all of our amazing employees who worked to create this technology that almost feels like magic. 💫 🔮 \n\nIf you believe in magic, read no further. But if you want to learn how this incredible technology works, click here: https://amzn.to/48e3S7T",
              "time": "2w",
              "url": "https://www.linkedin.com/posts/amazon_imagine-never-having-to-wait-in-a-checkout-activity-7109588917263237121-4d-C",
              "urn": "7109588917263237121"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHjCaBNfp06Tg/image-shrink_1280/0/1694788982434?e=1697000400&v=beta&t=r4WIIQyEt6iMOOU5n9iVjn_F7oPUdF3Apqqnt8tF0aw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEKgRVOtVNQLg/image-shrink_1280/0/1694788983089?e=1697000400&v=beta&t=pWzfLmDt1mv2YvfCpeOosOosvxvucON9YPj4P6Ar6mM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFzVTEuePU3Ng/image-shrink_1280/0/1694788984163?e=1697000400&v=beta&t=YkvVuQzIR-atAA2_8CkbFC08G1G69ZXraube4mGpAG8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGhsWiKuo5-ag/image-shrink_1280/0/1694788983881?e=1697000400&v=beta&t=4LQ9jQIpU-cjGtp8op_2aYUhbivZpZL7TVL8eE5kc4E"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGZxxcA6ex3dQ/image-shrink_1280/0/1694788984818?e=1697000400&v=beta&t=X75QG9FCao985LjZvZ2gBmp1FZBJYPquNusCzWmiN3g"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHpbvoWClfi0w/image-shrink_1280/0/1694788986300?e=1697000400&v=beta&t=Lu7ZtGq9xf09aFqACz3WOsqsNMM-HUhfOaPtlT65J-c"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGIWiUcQxAMPQ/image-shrink_1280/0/1694788986917?e=1697000400&v=beta&t=g1i2iXIEsYSEKwQH2mBza7S_XY1VqrcZrZjr4vn6pyY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQE87wv7KC2FPA/image-shrink_1280/0/1694788988566?e=1697000400&v=beta&t=6JnoOMnGzaB8w6eVIDpwukbI3-c0txiw0xtrYrN4pRY"
                }
              ],
              "num_appreciations": 59,
              "num_comments": 96,
              "num_empathy": 137,
              "num_interests": 5,
              "num_likes": 3015,
              "num_praises": 46,
              "text": "Last week, the UK celebrated 10 years of Amazon apprenticeships with a special treat for our employees - a private concert by the one and only British-nominated artist Cat Burns. 🎵 🎤 \n\nWorking with Apprentice Nation, the evening also brought together Amazon employees and prospective apprentices for mentoring sessions, inspirational talks, and skills sessions to help shape their future career paths.\n\nA special thanks to Cat Burns for an amazing night, and a special thanks to our employees for all of your amazing, hard work! 💙 🧡 \n\nRead more about the special day here: https://amzn.to/3Preh7Q\n\n#InsideAmazon #EmployeeBenefits #CareerGrowth",
              "time": "2w",
              "url": "https://www.linkedin.com/posts/amazon_insideamazon-employeebenefits-careergrowth-activity-7108460239582089216-pMOb",
              "urn": "7108460239582089216"
            },
            {
              "article_subtitle": "aboutamazon.com • 2 min read",
              "article_title": "Andy Jassy and Dave Limp welcome Panos Panay as Amazon's new Devices & Services leader",
              "images": [],
              "num_appreciations": 8,
              "num_comments": 95,
              "num_empathy": 90,
              "num_interests": 14,
              "num_likes": 4436,
              "num_praises": 261,
              "text": "Amazon CEO Andy Jassy  announced that Panos Panay will join Amazon in October to lead our Devices & Services business. From Andy’s note: \n\n“Panos has spent the last 19+ years at Microsoft, where he was most recently EVP and Chief Product Officer, leading the Windows + Devices division. Before this latest role, Panos held a variety of leadership positions, including Corporate VP for Microsoft Devices, as well as GM of Surface and PC Hardware, where he drove the creation and introduction of the Surface product line. As a strong product builder and inventor who has deep experience in both hardware and integrated services, Panos will be a great addition to our D&S organization moving forward.”\n\nRead more here: https://amzn.to/3rtfYtc\n",
              "time": "6d",
              "url": "https://www.linkedin.com/posts/amazon_andy-jassy-and-dave-limp-welcome-panos-panay-activity-7112861478348623875-f0ci",
              "urn": "7112861478348623875"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGKJvTzHYwbdg/image-shrink_1280/0/1693843447771?e=1697000400&v=beta&t=JT4f49U4MQqffwOXIwPQXyod9JMUPs_6vZyRkf5u774"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFdI7nrdTV0bQ/image-shrink_1280/0/1693843449163?e=1697000400&v=beta&t=GrOxADDb9xbpfIcMHCv5rV-DaTlCqLtFNS_Ir4xN3sk"
                }
              ],
              "num_appreciations": 20,
              "num_comments": 51,
              "num_empathy": 96,
              "num_interests": 4,
              "num_likes": 2590,
              "num_praises": 84,
              "text": "How about this for an epic school trip? \n\nTo inspire and nurture young creative talent, students from Lochgelly High School in Fife, Scotland visited the set of Prime Video's The Rig and met the show's star-studded cast. 🌟🎥\n\nRead more: https://lnkd.in/gVVSbFtm",
              "time": "1mo",
              "url": "https://www.linkedin.com/posts/amazon_how-about-this-for-an-epic-school-trip-activity-7104494372703924224-9vfL",
              "urn": "7104494372703924224"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQH43cRduhdiGg/image-shrink_1280/0/1694115902088?e=1697000400&v=beta&t=8iVOUZ9ie1wxKSeRtM-NCIBnh3glJ1Am0SohhOudkrc"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEoF_a2VtqvsQ/image-shrink_1280/0/1694115902940?e=1697000400&v=beta&t=VQ7LzJdkO4CXY8L7fq7sKOUFKzgjvQ-G5UNwuLgEX4A"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGPyzX4eiJ26A/image-shrink_1280/0/1694115903435?e=1697000400&v=beta&t=m6Wv3OSKj7ouNPzh4xXqIn1GvB1pCE0i4bMIvJi0h5I"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFYYz5DGAjkwg/image-shrink_1280/0/1694115904358?e=1697000400&v=beta&t=YudG7QDYrlQ6Q0Z7iRRzsOQB3CJM7kfMblfgkIsWj1U"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQF08rSePoLHog/image-shrink_1280/0/1694115908993?e=1697000400&v=beta&t=2ugnMr2eJ6TkoGptu-vyQMzPlPLt2PLT6tBizps06p0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFIYte_ybaVqQ/image-shrink_1280/0/1694115906785?e=1697000400&v=beta&t=hAFOWmqPuwj1xsRxNph5iom3dx2kx7bg8GfrZy59R2k"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGnLGzxijjkaA/image-shrink_1280/0/1694115907644?e=1697000400&v=beta&t=X8US0VQvoNBSh6uL1Y_UckImb_oE_cGlGb1DItjUi4I"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQG38tNIYQzLkw/image-shrink_1280/0/1694115908685?e=1697000400&v=beta&t=v3Ja0vck32QrDsz7yCDOWHETz9jbTf6bgJWYGwNea7c"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGH5XIIcW1uZQ/image-shrink_1280/0/1694115908946?e=1697000400&v=beta&t=aXidK55t87TSh9TEV9_hYc_YYeyQm3WvrMowQqaETHQ"
                }
              ],
              "num_appreciations": 31,
              "num_comments": 207,
              "num_empathy": 186,
              "num_interests": 10,
              "num_likes": 5144,
              "num_praises": 179,
              "text": "Have you heard of our Career Choice program? It offers pre-paid college degrees, industry certifications, and more, providing eligible hourly employees with the tools for success, no matter where they plan to work in the future.\n\nOur employees are our greatest asset, which is why we’ve invested over $1.2 billion into skills training and education programs by 2025 to help employees like Haileigh, Megan, Pissi, Samuel, and Sayeda thrive.\n\nHere are some fast facts:\n\n🎓 The vast majority of Amazon’s hourly employees – nearly 700,000 globally – are eligible for Career Choice.\n\n🎓There are more than 150,000 worldwide Career Choice participants since the program launched over 10 years ago.\n\n🎓Students are able to attend their classes at one of more than 400 education partners around the world, including community colleges, local and national colleges, HBCUs, and other skills training providers. \n\n 🎓Over 40% of Career Choice participants identify as BIPOC.\n\n Learn all about the program and all that it has to offer: https://amzn.to/3sHOfFw\n\n#CareerGrowth #CareerChoice #AmazonBenefits #Upskilling \n",
              "time": "3w",
              "url": "https://www.linkedin.com/posts/amazon_careergrowth-careerchoice-amazonbenefits-activity-7105637144508993537-lxn5",
              "urn": "7105637144508993537"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHtr_UYsGHmBw/image-shrink_1280/0/1694536202181?e=1697000400&v=beta&t=MkMu4PPcRYHPQBwhLJxyOfnTeGBtaxfhTaRb2-M8yDM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFcH1XiinDXQg/image-shrink_1280/0/1694536202739?e=1697000400&v=beta&t=6u99DglSkCfvy2H82z3my-CksZ4hIgeyDHg8oVwRgbI"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQE6ln3666gJ7Q/image-shrink_1280/0/1694536203658?e=1697000400&v=beta&t=oGZbgr5JudcGYgQykICVRZ11dXBzCmsiVs1QsqUitBA"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFo81wuoGPBsA/image-shrink_1280/0/1694536204121?e=1697000400&v=beta&t=zAqHYeYIaL0fKc56Iznuzoz5GjPZJYKovU9UJxl1eaw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGTSz0UdTcZsg/image-shrink_1280/0/1694536204810?e=1697000400&v=beta&t=toZfNJnbMOjfhO-WxZqXnso_13kE00XdOgNZ99icWZw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFXqGav8jSMpA/image-shrink_1280/0/1694536206518?e=1697000400&v=beta&t=B1eKygpTOmau2GmOLGy1S8uv-0C0E2RmoPxse5i_QiE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEwg0d1ZG3KWQ/image-shrink_1280/0/1694536207376?e=1697000400&v=beta&t=JEOYvOJ7qh2s-ErtQIgnbNVWtIok1mt44AxWBFiD9BE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEyricOqIAogA/image-shrink_1280/0/1694536207963?e=1697000400&v=beta&t=0H_6mzRszpdHeWC-7mPemrxd3inGGpozquK14Iibtv0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEcIV_fBCGzgA/image-shrink_1280/0/1694536208749?e=1697000400&v=beta&t=6i3zGgBkR_g-fGxnKnBsdiSk73i1yU11lODl2Hn8GWg"
                }
              ],
              "num_appreciations": 28,
              "num_comments": 98,
              "num_empathy": 157,
              "num_interests": 1,
              "num_likes": 3204,
              "num_praises": 107,
              "text": "Global Month of Volunteering is in full swing. Here are some events that took place during Week 1 across the world. 🧡 🌎 \n\nAmazonians in Germany, and the UK packed backpacks with useful school supplies for children from families in need at the start of the school year, with Clean the World Global.\n\nAmazonians in Austria partnered with local fire departments and the #RedCross to support disaster relief efforts and help locals affected by flooding in Southern Austria and Slovenia, by providing clean drinking water, clearing roads, and coordinating emergency shelters for those affected. \n\nAmazonians in Canada sorted and packed food for families experiencing food insecurity with Moisson Montréal.\n\nAmazonians in the U.S. participated in kayak cleanups to clear waterways of harmful plastics, volunteered at food banks, and helped build houses with Habitat for Humanity.\n\nAmazonians in India participated in a 5K run to raise money and awareness for the environment, through #GiveIndia. Over 3,000 employees and their family members participated, and Amazon is planting 1 tree for each 1 km ran, as well as donating school kits to government schools for every 2.5 km covered.\n\nWhere in the world are you from? And what causes are you passionate about? 🧡 \n\n#AmazonGMV #Community #Inspiring\n",
              "time": "3w",
              "url": "https://www.linkedin.com/posts/amazon_redcross-giveindia-amazongmv-activity-7107400011604230145-zIyg",
              "urn": "7107400011604230145"
            },
            {
              "article_subtitle": "aboutamazon.com • 6 min read",
              "article_title": "AWS announces the general availability of Amazon Bedrock and powerful new offerings to accelerate generative AI innovation",
              "images": [],
              "num_comments": 25,
              "num_empathy": 16,
              "num_interests": 3,
              "num_likes": 523,
              "num_praises": 14,
              "text": "🆕 An AI update: Amazon Web Services (AWS) just announced new capabilities and services designed to make it easy for organizations big and small to use #GenerativeAI in creative ways, helping them transform how work gets done. Companies such as adidas, BMW Group, GoDaddy, Merck, NatWest Group, Persistent, the PGA TOUR, Takenaka Corporation, and Traeger Grills are among customers applying generative AI innovations from AWS to transform their products and services.\n\nHere's what’s new:\n\n1️⃣ Generally available, Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models from leading AI companies, along with a broad set of capabilities to build generative AI applications, simplifying development while maintaining privacy and security.\n\n2️⃣ With the addition of Amazon Titan Embeddings and Meta’s Llama 2 models, Amazon Bedrock gives customers even greater choice and flexibility to find the right models for each use case.\n\n3️⃣ New Amazon CodeWhisperer capability will deliver customized, generative AI-powered code suggestions that leverage an organization's own internal codebase, increasing developer productivity.\n\n4️⃣ Generative BI dashboard: Authoring capabilities in Amazon QuickSight make it faster and easier for business analysts to explore data and create compelling visuals simply by describing what they want in natural language.\n\n5️⃣ Amazon Titan Embeddings is a large language model (LLM) that converts text into numerical representations called embeddings to power retrieval-augmented generation (RAG) use cases.\n\n6️⃣ New free generative AI training for Amazon Bedrock: Today, we’ve launched Amazon Bedrock – Getting Started, a free, self-paced digital course introducing learners to the service. This 60-minute course will introduce developers and technical audiences to Amazon Bedrock's benefits, features, use cases, and technical concepts.\n\nLearn more here. ➡️ https://amzn.to/3LF9u1q\n\n#GenerativeAI #Innovation #AmazonBedrock",
              "time": "5d",
              "url": "https://www.linkedin.com/posts/amazon_aws-announces-the-general-availability-of-activity-7113212788054921219-7Rnl",
              "urn": "7113212788054921219"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHYptoH3Hnuhg/image-shrink_1280/0/1692634324921?e=1697000400&v=beta&t=aEPFJhwGg2RaimnLdDO56SKijAv1Edv_wTARAYsjsDY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEoTdYDDbLq_w/image-shrink_1280/0/1692634326690?e=1697000400&v=beta&t=2J3tEBrNGhZ3dmmS7ZfS0oaMMxZ-tfGzpk0bEaxZlI0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQFZSf6SEBsROw/image-shrink_1280/0/1692634332221?e=1697000400&v=beta&t=6rVX90tDd8pKJheIoVeSm54Rvx_4ooTZynwTNltN4AQ"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQENdLkTrrRo7g/image-shrink_1280/0/1692634333134?e=1697000400&v=beta&t=0SvhRReS6WnGuTjdYJCW7mU2g1XINJqWCyEMS_w1JEE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHkqek07547gA/image-shrink_1280/0/1692634332934?e=1697000400&v=beta&t=w04TaHAHy8oLrnrsMkAJmFLPHdCClshU6Ww8xU0T9FA"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQH5ZKuho3BEiQ/image-shrink_1280/0/1692634333399?e=1697000400&v=beta&t=pTCuY0VJdMOuDmPoKBePNzKYm06t6KN_unnk0Xkud34"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHU7VZ3EZMhPQ/image-shrink_1280/0/1692634338282?e=1697000400&v=beta&t=dwH6sUUFqGB8XVyc5AmXDVDcyeb4m-4ob9MA3oLFU00"
                }
              ],
              "num_appreciations": 53,
              "num_comments": 136,
              "num_empathy": 341,
              "num_interests": 12,
              "num_likes": 8283,
              "num_praises": 348,
              "text": "🆕 Amazon Web Services (AWS) just opened its first international AWS Skills Center in Cape Town, South Africa, continuing on a mission to remove the barriers of access to cloud skills training.\n\nAnyone in the local community – regardless of background, education level, or social status – will now be able to explore how cloud computing technology is powering everything from weather predictions to smart homes.\n\nThe new Skills Center includes:\n\n🔵 Immersive exhibits, classroom training, and community events\n\n🔵 Essential resources to build a skilled cloud workforce\n\nLearn more: https://amzn.to/3QLiRQC",
              "time": "1mo",
              "url": "https://www.linkedin.com/posts/amazon_amazon-web-services-aws-just-opened-activity-7099422986461458432-ogur",
              "urn": "7099422986461458432"
            },
            {
              "article_subtitle": "aboutamazon.com • 8 min read",
              "article_title": "Amazon and Anthropic announce strategic collaboration to advance generative AI",
              "images": [],
              "num_appreciations": 3,
              "num_comments": 62,
              "num_empathy": 39,
              "num_interests": 8,
              "num_likes": 1960,
              "num_praises": 84,
              "text": "Anthropic has selected Amazon Web Services (AWS) as its primary cloud provider and will train and deploy its future foundation models on AWS Trainium and Inferentia chips, taking advantage of AWS’s high-performance, low-cost machine learning accelerators. Learn more ⬇️\n\nhttps://amzn.to/48GXMNN",
              "time": "1w",
              "url": "https://www.linkedin.com/posts/amazon_amazon-and-anthropic-announce-strategic-collaboration-activity-7112180738438959104-dpLz",
              "urn": "7112180738438959104"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHNwClBH2d-eQ/image-shrink_1280/0/1692108984654?e=1697000400&v=beta&t=tbmwouyn34_bT7RUgBsgAJ1XJBRDj5B5BXJrT6_mmA0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQG3uaMXDmfmgA/image-shrink_1280/0/1692108984337?e=1697000400&v=beta&t=D3ky-5ljJD6BYA2ZoL99Ntw0JjT2r0gFhD9z5eZYINo"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFyLhQsOTBJXQ/image-shrink_1280/0/1692108985279?e=1697000400&v=beta&t=v58cQJWJ6YuqNE2heGNzAiw90sLc649VKQvBUmhskCI"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFscpO3Aclctw/image-shrink_1280/0/1692108986270?e=1697000400&v=beta&t=Eq5qD3fSzmx-mxo6pBTyvZYp4VW_wrs2hetp1e6oEJw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHHcVbxa2q9Yw/image-shrink_1280/0/1692108987145?e=1697000400&v=beta&t=9jYhd6-HYokOh01l5GNPI6yeZ1_QPPZ_mYToq6lpdJw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFOFV4rxxrVvA/image-shrink_1280/0/1692108987696?e=1697000400&v=beta&t=uxZoQGigKVVjey2bAfj4zNYo_VGbPgYjocKtIkiAQpE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFGiPqY_oVtwA/image-shrink_1280/0/1692108988347?e=1697000400&v=beta&t=N5w8Drek1E82QR5yUyTOE3AaHZbkz6SbqGUOPmLXWPo"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGo5Px0I1tgkQ/image-shrink_1280/0/1692108989467?e=1697000400&v=beta&t=rdOzvLIO6mwp6oA1PE3nYxdNPgn6oKgpzF03bdw8sGY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFgvd9zPN8MSA/image-shrink_1280/0/1692108990400?e=1697000400&v=beta&t=uH3tat-QRCiD3ftEYPCYnVJJE4BepxuNtv6ylCCr3os"
                }
              ],
              "num_appreciations": 35,
              "num_comments": 107,
              "num_empathy": 288,
              "num_interests": 7,
              "num_likes": 5839,
              "num_praises": 168,
              "text": "Amazon founder Jeff Bezos opened up the company’s first “office” from his garage in Bellevue, Washington in 1994. Though the company now requires a ‘bit’ more space than that garage can provide, Amazon’s love for its hometown in Puget Sound remains strong.\n\nWe might be biased, but here are some things that make our headquarters the most unique place to call the office. 😊\n\n☑ We offer a variety of perks to make the commute more sustainable and convenient, including free public transportation and reimbursement for bike purchases and maintenance.\n\n☑Dogs are welcome! Make sure to grab a dog treat at the reception desk on your way in so that they can also start their day off happy. And when they’re needing a bit of a break from the office, head on down to the dog park, which offers amenities like a fire hydrant, turf, and a hose so pups can play. And if they get a little muddy, head over to the paw wash station where you can clean your pup before heading back up to the office.\n\n☑And when our employees need a play break as well, you can head to the top floor to play some games, gather with friends and enjoy the incredible city views.\n\n☑We’ve got the tastiest cafeteria with a variety of fresh-made salads, ramen, and sandwiches. The cafeteria also features some art installations and murals, such as a hallway full of blue neon lights, and a mural of Jimi Hendricks and Janis Joplin. There are also amazing local restaurants and retailers on the street level.\n\n☑This is where it gets funky: Free bananas at our Banana Stand. The community banana stand is open and free for anyone, employees or the community. \n\nThe list goes on and on, so make sure to click the link here to get a look at all 25 exclusive photos of our office. https://amzn.to/3OuCj14 \n\nWhat is your favorite office perk? \n\n#InsideAmazon #team ",
              "time": "1mo",
              "url": "https://www.linkedin.com/posts/amazon_insideamazon-team-activity-7097219519214993408-sb19",
              "urn": "7097219519214993408"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFQywXsURlD7Q/image-shrink_1280/0/1693581902451?e=1697000400&v=beta&t=nfdiX0LOjli-UPmJBhDFCQEbicvsbECU5R_QP7ZyW9s"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHOe0sej9ZiAQ/image-shrink_1280/0/1693581903568?e=1697000400&v=beta&t=6km1hwKTEg5TFx9VIUkoDmbfY4ssm_-nFmZJP4HmRv0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFNFuiXuFgkqg/image-shrink_1280/0/1693581904240?e=1697000400&v=beta&t=QrxYH8-iSx7TP-A0n5BY_n96Pbz3-TMxn3godmGLFW0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHjTkskNcRzhg/image-shrink_1280/0/1693581905270?e=1697000400&v=beta&t=dA45krX3Q5rFH81Z0TdooGHoGbrzqYo6XZ5ec7dX9mk"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGZ6oMiEy9Qyg/image-shrink_1280/0/1693581906265?e=1697000400&v=beta&t=WEHHOx4Lpk6-OnqffqjTolYDAHvYj5CRBmrXkLvyAGM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFQD4cUFoG-AA/image-shrink_1280/0/1693581907005?e=1697000400&v=beta&t=OntovUspvWBtk2WpxANu7dedDPhGzgfhfnm9xYX4Sqc"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEAo1haA--Mag/image-shrink_1280/0/1693581907353?e=1697000400&v=beta&t=DxwaSiX-bnkcSjM4-bMeqotKHJdz3qpj6SzxzHyh2PM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEx_TX2lxrbWw/image-shrink_1280/0/1693581908174?e=1697000400&v=beta&t=u50vvfIuGow7wdTzYt0OySmLQO6fUHj5QnCF6grce3E"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQECTQKvL1Nv0g/image-shrink_1280/0/1693581909196?e=1697000400&v=beta&t=gouM4XN3nvhAUnb6RQgr6d2rUVcjQEr5oNL82DKGwPY"
                }
              ],
              "num_appreciations": 78,
              "num_comments": 141,
              "num_empathy": 258,
              "num_interests": 7,
              "num_likes": 5504,
              "num_praises": 212,
              "text": "September is Global Month of Volunteering (GMV) here at Amazon. During September, tens of thousands of Amazonians will come together to volunteer for causes they’re passionate about to positively impact communities where our employees live and work. 👏 \n\nLast year, Amazon employees from over 50 countries participated in Global Month of Volunteering, supporting more than 400 organizations and volunteering in 1,800 events. And Amazon donated more than $450 million in cash contributions to hundreds of organizations from around the world. \n\nThis year, Amazonians will participate in a variety of volunteer initiatives – from kayak cleanups, home food delivery services and back to school donations to hygiene-kit building, literacy tutoring, habitat restorations, and more.  \n\nWe employ more than 1.4 million people across dozens of countries, and we believe our employees’ passion, ideas, and volunteer efforts can make a positive impact on our communities. Amazonians, make sure you are signed up for a volunteer event!  ✅ \n\nLearn more about #AmazonGMV here: https://amzn.to/45IWxLA\n\nWhat causes are you passionate about? 🔽 🧡 \n\n#AmazonInTheCommunity #Inspiring #Community\n\n",
              "time": "1mo",
              "url": "https://www.linkedin.com/posts/amazon_amazongmv-amazoninthecommunity-inspiring-activity-7103397385959051265-co8m",
              "urn": "7103397385959051265"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEBH9zICdqCQA/image-shrink_1280/0/1691044898991?e=1697000400&v=beta&t=yYE9N_46_1IkWgJzjXoi1DPR9b5-NKNGIpK9vT0EZ20"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQG06kPThtL8bw/image-shrink_1280/0/1691044901010?e=1697000400&v=beta&t=_0kh-N03scvPH0gSg1XK6O6wfaNOs20thSznsPK-NmY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFnJteEa03BmQ/image-shrink_1280/0/1691044902425?e=1697000400&v=beta&t=pTrO-7N5c25xbQIWLCUzFPnWX8t-8aWmxTiewWTIZcs"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFFran6_hewzQ/image-shrink_1280/0/1691044903372?e=1697000400&v=beta&t=6IDPkW0VcMHcLhVW8o4WYl9hVSwWtfFNvlomvgFFGyg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFfFDOpZDnSwQ/image-shrink_1280/0/1691044904214?e=1697000400&v=beta&t=tSA7bNxnNGbz9MKhL7ENoZ25n5rgKwWMimIH8RT0jKE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQG_spMBaof6-Q/image-shrink_1280/0/1691044905824?e=1697000400&v=beta&t=z_Bm75Ol_FQRsE7pOeSCZHWGOKdEdTTTS6jfgqSWkkQ"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQExdHgg36pd0g/image-shrink_1280/0/1691044907362?e=1697000400&v=beta&t=TOl5w2N_36Otgc6T1FHpir1K1SxPCjxrw_cjD0LVN0E"
                }
              ],
              "num_appreciations": 8,
              "num_comments": 41,
              "num_empathy": 63,
              "num_interests": 4,
              "num_likes": 1932,
              "num_praises": 61,
              "text": "Read on as our leaders share their thoughts on fostering inclusion & belonging during the celebration of 'Women in Technology' at the #AmazeWIT 2023 event. \n\nDeepti Varma Sandy Gordon Rajiv Chopra Gitanjali Bhutani Liz Gebhard\n",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_amazewit-activity-7092756426523086848--n_Q",
              "urn": "7092756426523086848"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFSWr-wQtbnGQ/feedshare-shrink_2048_1536/0/1691414612858?e=1699488000&v=beta&t=1wEfKEU39-Y5H87gJEJz1PTBgRA1KieHRlDIp0w1qIg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGfD7hzr7VgoA/feedshare-shrink_2048_1536/0/1691414613702?e=1699488000&v=beta&t=APqIPvdwgSX3_VMcRiH7ZjKsEHYU1V35TdLuUPElMk0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQH0Mj2ggQcymQ/feedshare-shrink_2048_1536/0/1691414612685?e=1699488000&v=beta&t=aohcd7GNVOkO7vgNUyR0aujQsunUQD1TnOCjKiLrsKY"
                }
              ],
              "num_appreciations": 30,
              "num_comments": 87,
              "num_empathy": 146,
              "num_interests": 9,
              "num_likes": 4850,
              "num_praises": 133,
              "text": "Justine Hastings, VP of People eXperience and Technology (PXT) Science for Amazon and her team are dedicated to helping HR teams make fact-based decisions to support tomorrow’s leaders. \n\nHastings, who came to Amazon 2.5 years ago from a tenured faculty position at Brown University, has built a team where women are leading science at all levels, and different disciplines are encouraged to collaborate to solve complex customer problems. We spoke to Justine and learned about her main inspirations for building and leading teams, including advice she gives herself and her team as she continues to learn and grow as a leader. ⬇️\n\n🔹 Teamwork makes the dream work: Across industries, the challenges we face are large-scale, complex, and ambiguous. Solving them takes a diverse team of people with unique skills, specializations, and perspectives.\n\n🔹 Hear people: Inclusive leaders work to hear all ideas and encourage people from all backgrounds to bring their ideas to the team.\n\n🔹 Why not me?: It can be hard to step forward to lead when you are the only one from your background in the room. When you see a problem and have an idea for a solution, ask yourself: “Why not me?”\n\n🔹 Find mentors, and be a mentor: To advance in society, we must find mentors to learn from.\n\n🔹 Make sure your science is people-centered: To successfully address human problems, we must get specific and dive deep into the root cause of a problem, and that starts with getting to know the people behind the data.\n\nhttps://lnkd.in/gqsWfiT2",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_justine-hastings-vp-of-people-experience-activity-7094307086527787008-5uJK",
              "urn": "7094307086527787008"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEHuTHnSv4eLQ/image-shrink_1280/0/1689172981001?e=1697000400&v=beta&t=0jrTFWCyv0nSWGuA2W0XNcgQwHo2EaQ3CZWsbsgjcdE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQELe8RNziiozw/image-shrink_1280/0/1689172983022?e=1697000400&v=beta&t=MIuzuRePJpJPe9ri9aTqibgg3hf3gXqZUByf_BqIixM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQH8pTyh4RP3dA/image-shrink_1280/0/1689172983833?e=1697000400&v=beta&t=l1c1P4G_Pa5vKCcgxt25wVcSbwsSSnBfyEEvGJyQfJg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEHQYJB5o_m6g/image-shrink_1280/0/1689172984671?e=1697000400&v=beta&t=mQ_uOV1L561caZFbi3Zan2d4aQllWEcY4tioX8ks7ik"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQF8P3eipOlkqA/image-shrink_1280/0/1689172984740?e=1697000400&v=beta&t=xj9jFhXt0HDWXxpkcBLvfQUEZIUksdL4ucnTHbBb6t8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQGhJsTf-J-tkA/image-shrink_1280/0/1689172985010?e=1697000400&v=beta&t=fVAz-fN-RVGzmDPB6WGgg6hSqTYHTQjrIVk-4oPyIFw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQE5jDVDLHwUsQ/image-shrink_1280/0/1689172985259?e=1697000400&v=beta&t=qpggAO8zInfNAFcb-3SsXtXczJeVGv_S5CzsgJpmrL4"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHB-6oelQeCoA/image-shrink_1280/0/1689172985579?e=1697000400&v=beta&t=B8gfKYaMovN_BvETQj37nUUd6WxKTHf3ATUu8-EUrjE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQGoK9zA0jV9TA/image-shrink_1280/0/1689172986538?e=1697000400&v=beta&t=VG0F9yFaPC72KATISlZHDyT8uQD21OUCJfh-5c74-GA"
                }
              ],
              "num_appreciations": 66,
              "num_comments": 238,
              "num_empathy": 643,
              "num_interests": 14,
              "num_likes": 13180,
              "num_praises": 570,
              "text": "Prime Day brings Amazonians together from all around the world. 25 countries participated in Prime Day this year, with customers in Australia, Austria, Belgium, Brazil, Canada, China, Egypt, France, Germany, Italy, Japan, Luxembourg, Mexico, the Netherlands, Poland, Portugal, Saudi Arabia, Singapore, Spain, Sweden, Turkey, the United Arab Emirates, the U.S., and the UK. And Prime members in India can shop on Prime Day July 15-16.📦 \n\nAt the center of all the magic are our passionate employees across the operations network, who help make it all possible. That’s why we work to provide them with leading compensation and benefits, including health insurance, ways to save money for retirement, and up to 20 weeks of paid family leave.\n\nAgain, a sincere thank you to each and every Amazonian for all that you did to make Prime Day a huge success. You’ve raised the bar once again, and we truly appreciate your efforts and hard work. Drop a comment below with where in the world you are this #PrimeDay to rep your country! 📍 🌎 ",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_primeday-activity-7084905021045129216-QjKu",
              "urn": "7084905021045129216"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHlMsQJGcRx3g/image-shrink_1280/0/1691593202913?e=1697000400&v=beta&t=byr2EuCvMBszElsHnknPD3fH8Bta-a_ogFqNUQ4DLe8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQERtnPOqgzf2w/image-shrink_1280/0/1691593202892?e=1697000400&v=beta&t=50veaplFROIEWoyfS_hOpTUU5G-VM0tFHWw2Bz6whtQ"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEQ028QX8x1ug/image-shrink_1280/0/1691593204427?e=1697000400&v=beta&t=bVe5OMQ1dVsRlSDebf5IWagTj636Ld5XwYbqIqF8LTk"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFn8eBLNrOnVA/image-shrink_1280/0/1691593205430?e=1697000400&v=beta&t=9ZCrGdslW94x_BenIx11c_qk_-Xnd2fjEZrnZjafAcs"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQE9Foflt2BsNA/image-shrink_1280/0/1691593208929?e=1697000400&v=beta&t=wv9urfCDlchB56XelMrm-x7G9021CzdQSWigcXLu4vo"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHVKb1gsa5QGA/image-shrink_1280/0/1691593210902?e=1697000400&v=beta&t=RyOxf2UwYKnGqJQj15lRh7iK-8r6rO730l6NZuBDB4M"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGz919lx88P3A/image-shrink_1280/0/1691593211577?e=1697000400&v=beta&t=Pkq_sJLhNLe07QjBUw8hk_QNQqp4OtwDfcW-CE9N3Pc"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGSQsEQLqmEgg/image-shrink_1280/0/1691593212468?e=1697000400&v=beta&t=yOWopzfILzeH1KOZP_YB4cnRkqp9S3j1cz8rV8KBDoY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQE7Kx5rRRyp6Q/image-shrink_1280/0/1691593214834?e=1697000400&v=beta&t=kM4isKYsudwL4hrQS9GdCLI19uAZ0hcuJeasfE5wnbk"
                }
              ],
              "num_appreciations": 40,
              "num_comments": 76,
              "num_empathy": 125,
              "num_interests": 5,
              "num_likes": 3390,
              "num_praises": 119,
              "text": "Our 2022 Sustainability Report recently dropped. Here is a breakdown of some top highlights:\n\nSince 2015, we've reduced the average weight of packaging per shipment by 41%, avoiding more than 2 million metric tons of packaging. That is the weight of more than 230 Space Needles - the iconic Seattle landmark located near our HQ.\n\nIn 2022, 90% of the electricity consumed by Amazon was powered by renewable energy sources. This includes more than 400 wind and solar projects from around the world.\n\nWe had more than 9,000 electric delivery vehicles in our global fleet, and 145 million packages were delivered by EVs in the U.S. and Europe.\n\nWe co-founded The Climate Pledge, a commitment to reach net-zero carbon by 2040. By the end of 2022, we had 396 companies sign the pledge, and today, there are more than 400 across 55 industries and 39 countries.\n\nThese are just a few examples of how we are taking big swings to decarbonize our operations. Decarbonizing Amazon's operations is a challenging goal, but as a company, we don't shy away from grand challenges. It is our mission to minimize Amazon's impact on the planet and the communities in which we live and work, through meaningful actions that address climate change. 🌱 ♻️\n\nRead more about the Sustainability Report here: https://amzn.to/3PY2Sy7\n\n#Sustainability #TheClimatePledge #InsideAmazon",
              "time": "1mo",
              "url": "https://www.linkedin.com/posts/amazon_sustainability-theclimatepledge-insideamazon-activity-7095056199527641088-hQHt",
              "urn": "7095056199527641088"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEM9I3U6Id2Pg/image-shrink_1280/0/1690992906221?e=1697000400&v=beta&t=a4muaD9MCRCC7c2RuUNr93RNTI2P584M2TL33dSmq-U"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEqvckZtR2IxQ/image-shrink_1280/0/1690992908179?e=1697000400&v=beta&t=imHqXF_wcrMy5-yb5bLzPA4hN3gZhzrqigyKprU4n0w"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHJmNbxwaRcHw/image-shrink_1280/0/1690992910014?e=1697000400&v=beta&t=9FVDRPr_QmA_0i0IckPGv3mRELJM46Vm_HSDR_d8CqA"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGJ1Us-HJ290Q/image-shrink_1280/0/1690992907448?e=1697000400&v=beta&t=JRaZjj8YMxu5u1z1AoEZmlqUohZsDZiYk1DgnFqIHH0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGLukZ9I4qmXw/image-shrink_1280/0/1690992913336?e=1697000400&v=beta&t=d5WcxUNFdpl8N5qFMjVQ337U55548ln51BUa4Ikro1A"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQE5jTu-R9aurQ/image-shrink_1280/0/1690992911025?e=1697000400&v=beta&t=EkWf3W_IVYExYT2CBBg3VP3JRdOKncD5E1Vr76s2-X0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEk3jhZspH5uQ/image-shrink_1280/0/1690992912870?e=1697000400&v=beta&t=Ef8sjd7ZFtpg97S5b-UOHB72_YrnoAqU9xX1EpqYM0M"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHJSDngvxlrBA/image-shrink_1280/0/1690992918315?e=1697000400&v=beta&t=Zcg9Amckws0CORkHDCRkRfUhP5llntL77-IuafMXLk0"
                }
              ],
              "num_appreciations": 75,
              "num_comments": 141,
              "num_empathy": 427,
              "num_interests": 6,
              "num_likes": 6777,
              "num_praises": 172,
              "text": "Welcome to Plant Camp! A free plant-based arts and craft open to the community every other Wednesday on the Day 1 playfield in front of the Seattle Spheres. 🌿 🎨 🌱\n\nPlant Camp is a place to spark creativity by combining art and nature into a fun 30-minute activity. Every other Wednesday, the Amazon Horticulture Team partners with South Lake Union and Urban Craft Uprising to explore the intersection of these two mediums, which have positive benefits, like increasing productivity and decreasing mental fatigue and stress.\n\nPlant Camp started when the Spheres opened to the public, and we wanted a fun way to give back to the community and our employees.\n\nLearn from the Amazon Horticulture Team how to care for plants that share the same home, why some plants need their own space, and the proper way to curate a terrarium, so that each plant has a chance to thrive.\n\nTo learn more about the available dates and activities, check us out here ➡️ https://amzn.to/44PIXG0\n",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_welcome-to-plant-camp-a-free-plant-based-activity-7092538368755974145-Z05s",
              "urn": "7092538368755974145"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHktmUxEJKBXQ/image-shrink_1280/0/1692718503676?e=1697000400&v=beta&t=f2Az2RRwIa4DiXOiHc1ebiVgort4UafMs4n0hvYlMiE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFK_C1AGMz6pw/image-shrink_1280/0/1692718505175?e=1697000400&v=beta&t=4H4gcuLf-TJIH32iJXD-_uxljxK_4y1mZARTed8gLcs"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHdLfkfSan5gA/image-shrink_1280/0/1692718506433?e=1697000400&v=beta&t=S3nHuqRwIN7Ff_K9Yc_V6Iq0czFIG8hRiXSBxkh-qw8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGgR2kid8rpOA/image-shrink_1280/0/1692718509803?e=1697000400&v=beta&t=wI9x3wlyrLZ1fzt_3FC4iXL-Q7YFo96z0E7rziWrBew"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQH0eQJPu511wQ/image-shrink_1280/0/1692718506565?e=1697000400&v=beta&t=oaeGTDcAZcXlswyXUiFFqMWZWYINPtIGLFlI4waQlt4"
                }
              ],
              "num_appreciations": 49,
              "num_comments": 109,
              "num_empathy": 463,
              "num_interests": 8,
              "num_likes": 5168,
              "num_praises": 120,
              "text": "Meet Lawrence Tam and his ‘colleague’ Ashe 🐶 who take advantage of Amazon's commuter benefits that cover the cost of bike maintenance, rentals, and more. 🚲 \n\nLawrence is a Senior Technical Program Manager, and works out of our Seattle HQ1 office 3 days a week.\n\n“Amazon offers two of the best employee benefits in Seattle: the Dogs at Work program and the Bike Commuter benefits. During the beautiful Seattle summers, Ashe and I take advantage of both! Not only are we doing our part to reduce emissions and avoid traffic, but Ashe also enjoys the wind in her face the whole ride home.”\n\nAmazon U.S. employees who bike to work receive bike perks such as:\n✅ Bike leases: Employees can lease a take-home bike, including e-bikes for a monthly fee eligible for reimbursement.\n✅ Bike share: Employees can expense costs for dockless or docked short-term, app-based rental bicycles.\n✅ Maintenance: Employees can take advantage of two complimentary tune-ups each year.\n✅ Bike parking: Employees can access bike parking at our offices.\n\nIn addition to offering bike cages for employees to store their bikes, most of Amazon's corporate offices also have showers for bikers to get ready at work.\n\nAnd fear not, if biking to work is not for you, we provide free transit passes to employees that use public transportation. We're thrilled to report that in Seattle, more than 20% of our employees walk or bike to work and another 50% use public transportation or carpooling options.\n\nAnd while Lawrence found his dog backpack at a garage sale, we've got plenty of options available on Amazon!\n\nLearn more about the benefits here: https://amzn.to/47IQacK \n",
              "time": "1mo",
              "url": "https://www.linkedin.com/posts/amazon_meet-lawrence-tam-and-his-colleague-ashe-activity-7099776026129432577-YVxK",
              "urn": "7099776026129432577"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEh3ergqxllRw/image-shrink_1280/0/1688392804448?e=1697000400&v=beta&t=KCisEjYfD6xCz1i6fre-puRi9N86YErk5sUVY3YlUlU"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQFACQZ8256rBQ/image-shrink_1280/0/1688392804335?e=1697000400&v=beta&t=EwNgO-brXh3SgfRVgfueoAAAp7GQNrXbsrhMVnwPNxs"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQFqdGV7ItedAw/image-shrink_1280/0/1688392807763?e=1697000400&v=beta&t=KQ0nXErxvrP1f2oVn9wLcb32rlK9PgZecgaJFdq76yg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEzAjNFWK4HMA/image-shrink_1280/0/1688392809104?e=1697000400&v=beta&t=zACAWulKv-FGxzWIDOguIIP_k5ECk1SnIQA6y6OFH8c"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHiHgzp9eqpxg/image-shrink_1280/0/1688392810886?e=1697000400&v=beta&t=gFLseUc_9_IF2IXsNcGGRP1TbAuXtVU1AkYuTA9s_Po"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQF0LIFk49yrLQ/image-shrink_1280/0/1688392813108?e=1697000400&v=beta&t=hKF44BWoWFbdlE5H3CJHYEsBkLWdLzXx0ZhGRXms3-A"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQGKC2ZYngJnEQ/image-shrink_1280/0/1688392814479?e=1697000400&v=beta&t=YrHkO8CuzF7h-M7iwWEKfu5Tf-uMxTZTV6qX1YfqxQw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQG5WCi7n3b87A/image-shrink_1280/0/1688392817251?e=1697000400&v=beta&t=zSrAYWJ_LNbSFoQ5I8wB880gsUrpCtodyT4AtsF3Rj0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQFRnYZhomqJvw/image-shrink_1280/0/1688392819882?e=1697000400&v=beta&t=655YdOz6ioK31yzkFFlofW91KR7nE0Ly8l6k3tL_cEs"
                }
              ],
              "num_appreciations": 17,
              "num_comments": 103,
              "num_empathy": 255,
              "num_interests": 16,
              "num_likes": 5703,
              "num_praises": 128,
              "text": "Fun fact: Each Amazon office is designed to capture the spirit and personality of the place it's at. So what unique features can be found in our 15-storey UK HQ in Shoreditch, London?\n\n☀️ A large roof skylight that floods the the interior atrium with natural light. Designing the space to capture as much light as possible was a specific consideration for this city, where sunshine can be scarce! \n\n🚘 A plush leather couch converted from an iconic, cherry red Mini Cooper, which used to sit in the offices of Lovefilm. Lovefilm was a UK DVD-by-mail service (remember those?) that was acquired by Amazon in 2011.\n\n☎️ A phone box...only this one looks different from the classic British icon because it resembles a giant Amazon Echo speaker. Anyone can take a call inside the soundproof booth that sits in the reception area, or just step in to chat to Alexa.\n\nExplore our Shoreditch office – our biggest corporate workplace in Europe – at https://amzn.to/3Cumpy2, or share your own photos of it in the comments below!\n\n#LifeAtAmazon #OfficeDesign #InsideAmazon",
              "time": "3mo",
              "url": "https://www.linkedin.com/posts/amazon_lifeatamazon-officedesign-insideamazon-activity-7081632764063621120-zaM1",
              "urn": "7081632764063621120"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGhgDFKt3KGPw/image-shrink_1280/0/1692977701752?e=1697000400&v=beta&t=VSrGqY7HfH6AuIQdkLRPNVrXtQkl1Oqz7yza-GAlDCM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHvV8wJkI9Fyw/image-shrink_1280/0/1692977702708?e=1697000400&v=beta&t=YQDpkV0GLQQaqcb8Pvk1iD7i6U62OQPGIF4-uZU1vqw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGbze_W8CTTpQ/image-shrink_1280/0/1692977703006?e=1697000400&v=beta&t=e7o4aJY-o9qw3vL4c95_ExDLIfcTsuFn2squ3MIygyg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFKqqWudQ1kSw/image-shrink_1280/0/1692977707827?e=1697000400&v=beta&t=NR0gKPa-UfPHLtsL6bMKkEjF6OL660zIyKCQwqF7hFU"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQF4jqX02U9oPw/image-shrink_1280/0/1692977705854?e=1697000400&v=beta&t=mNavrsG7jHUn7MgtLMlSwhiBFtlh0tgXwF2coUYdc-Q"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHIeGGTh4GixA/image-shrink_1280/0/1692977707840?e=1697000400&v=beta&t=bgXALjvvGDnnjcyRMlCzrmFDGkI1neK8aJCCVV_sOY0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEfHKvyB-YI2w/image-shrink_1280/0/1692977709570?e=1697000400&v=beta&t=d4S0XneDOkzbuT44wTJS8xbHJqb3nXsItHOxt_nkRAA"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFSRl1OP53UBg/image-shrink_1280/0/1692977710589?e=1697000400&v=beta&t=O2_EpxLUJq6nFN7tmPigVOYoM01YFV_p4dwfNEoxmsM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGewsoS_-WtrQ/image-shrink_1280/0/1692977711615?e=1697000400&v=beta&t=s7cFo9V9ylgGOOp7vayjrcUcjd8ppHGueryoZI8M6Fw"
                }
              ],
              "num_appreciations": 196,
              "num_comments": 233,
              "num_empathy": 1401,
              "num_interests": 12,
              "num_likes": 8748,
              "num_praises": 111,
              "text": "Tomorrow is International Dog Day, and we are celebrating all of our beloved office dogs. 🦮 🐩 🐕‍🦺 🐕 \n\nAmazon has been ranked among the most dog-friendly companies in the U.S.\n\nIt all started with Rufus the corgi. In the early days of Amazon.com, a husband and wife team brought their Welsh corgi, Rufus, to work with them, and he became a surprisingly productive part of the team. Employees would even use Rufus's paw to click the computer mouse to launch some of the earliest pages of Amazon.com.\n\nRufus's memory is still honored at Amazon: There are photos of him around the Puget Sound campus, and there's even a building in South Lake Union that was named after him.\n\nAnd now, thousands of office dogs follow in Rufus's paw steps. 🐾 \n\nHaving dogs in our workplace has been found to lower stress and boost morale, and we're proud this is such a uniquely Amazonian tradition.\n\nWe would love to see a photo of your dog in the office in the comments! 🔽 \n\n#InsideAmazon #DogsAtWork #InternationalDogDay",
              "time": "1mo",
              "url": "https://www.linkedin.com/posts/amazon_insideamazon-dogsatwork-internationaldogday-activity-7100863199238897664-Myry",
              "urn": "7100863199238897664"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQF28qE9Gbb2Lw/image-shrink_1280/0/1691481601300?e=1697000400&v=beta&t=G1NSlZgLwZjqEBqWz3dCvI07JoYKu8_ivuPDhJsjZ1g"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQGcaFFqCES-6A/image-shrink_1280/0/1691481602463?e=1697000400&v=beta&t=LmGzE3W4zubWfkn_pvoA458nmHSNFxHvoRNR883YClo"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQF_9rGBbYbtQw/image-shrink_1280/0/1691481602599?e=1697000400&v=beta&t=EfAH5Ea1SzY2cv5qB2CDJ9iKRPtf8tre2_V0ZgxG5XY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQH49b_-1P19iA/image-shrink_1280/0/1691481603980?e=1697000400&v=beta&t=sQKyELDRCjbsSmIuBEQ6CvXJFnRLs_GdmyUDtTNP3L8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEcKdp-VZurbg/image-shrink_1280/0/1691481604050?e=1697000400&v=beta&t=w1-W40G9m6WcDEiTU7tmXyt0RHipq8EOcvBKQnBAddY"
                }
              ],
              "num_appreciations": 22,
              "num_comments": 31,
              "num_empathy": 24,
              "num_interests": 2,
              "num_likes": 794,
              "num_praises": 8,
              "text": "Dans le cadre du Programme Nature 2050 co-porté par CDC Biodiversité et le Fonds Nature 2050, le Right Now Climate Fund d’Amazon apporte son soutien à différents projets consacrés à la préservation et à la restauration de la biodiversité.\n\nConnaissez-vous la Nonette ?\n\nDirection l'Oise ➡️ La Nonette est une rivière de 40 km qui prend sa source dans la ville de Nanteuil-le-Haudouin.\nDepuis des siècles, elle fait malheureusement face à de nombreuses pressions humaines qui accentuent les impacts du changement climatique.\nDécouvrez aujourd'hui son histoire et le nouveau projet de restauration porté par le Syndicat Interdépartemental du SAGE de la Nonette, qui vise à rendre son cours naturel à la rivière.\n\nLe projet se base sur 3 axes :\n\n👉 Préserver et restaurer la biodiversité\n👉 Atténuer les changements climatiques\n👉 Adapter les territoires aux changements climatiques\n\nIl est désormais urgent de répondre à l'accélération des changements climatiques et la restauration de la Nonette est un exemple concret de l’engagement d’Amazon en ce sens.\n\nhttps://lnkd.in/gY2ua5x5 ",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_dans-le-cadre-du-programme-nature-2050-co-port%C3%A9-activity-7094588062139056130-zCSR",
              "urn": "7094588062139056130"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQGCTnE_39fXKw/image-shrink_1280/0/1690415100854?e=1697000400&v=beta&t=1OtRDglimi1g0P5KQ9IKw0UDuDFuikm58oVJKwrr1eQ"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHpzjnZInngSw/image-shrink_1280/0/1690415102554?e=1697000400&v=beta&t=ZkjT_V88uRHpo6CKiHI8j3E-__QMciPoREpdO1LfhxY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQG560LOALp39w/image-shrink_1280/0/1690415104382?e=1697000400&v=beta&t=1L1xfi1di_lSzfF-nmiuI4cvZEnftF-QCDtDVXIMtfY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHWKdonfqI8tw/image-shrink_1280/0/1690415105228?e=1697000400&v=beta&t=Z6V9GqGntdzzHb9vWQ0y_ioPeGP3R_zCbYwxuRUKWG0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQF4ul2pA3wmAQ/image-shrink_1280/0/1690415105857?e=1697000400&v=beta&t=yJ5PTf4UF7MwTc2I_WUZFKXLGn8njI6Lt6o_-LLEphw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHR5oiJ6yaDNA/image-shrink_1280/0/1690415106103?e=1697000400&v=beta&t=NC-CxaNotonryxL_xDH7r8H5hLZnbbf7MaDKRZHcADw"
                }
              ],
              "num_appreciations": 16,
              "num_comments": 95,
              "num_empathy": 132,
              "num_interests": 8,
              "num_likes": 4808,
              "num_praises": 135,
              "text": "We announced some pretty exciting AI updates today at the Amazon Web Services (AWS) Summit in New York City! 🗽 🎆 Here are two updates that we're excited about:\n\n1. AWS HealthScribe will use generative AI to create tools that ease the paperwork burden for health care professionals, giving more time back for patients.\n\n2. AWS will now offer seven free and low-cost skills training courses to help you start building with AI.\n\nIt was invigorating and inspiring to see AWS builders and cloud enthusiasts alike learning and sharing how generative AI is transforming organizations, across all kinds of industries and applications.\n\nLearn more about the event and other AI innovations: https://amzn.to/3Qictjl\n\n#GenerativeAI #AWSSummit #Amazon #HealthcareAI",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_generativeai-awssummit-amazon-activity-7090114847719251968-d43A",
              "urn": "7090114847719251968"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHak8hQq7rJMQ/image-shrink_1280/0/1690297621588?e=1697000400&v=beta&t=rMtlVbJHXGZOXOtdny5E_M8wmHHZiIQMwnW2xdmdKLM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQG83N0qAigtaw/image-shrink_1280/0/1690297621640?e=1697000400&v=beta&t=YzmNCFll4Hx7rqmAUDJGEyRpY00BPiO5rPe2_HqrLbU"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQE3v0ufmz54Vw/image-shrink_1280/0/1690297621890?e=1697000400&v=beta&t=KltE0kH-2baXdySbm37_Xn5w2Ie95V6Nz3BGiE1zugU"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHyTZIWt4_IAA/image-shrink_1280/0/1690297623245?e=1697000400&v=beta&t=mSV5N7dtBPt2i-k7TOB8umB0yWTSUlgTDZT1ehqMii0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEfjv9ccV07Cg/image-shrink_1280/0/1690297623738?e=1697000400&v=beta&t=295vQYz0a4MdX41cujfqbSA-ytoXpELCNoK5WdH4F5A"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQFRFMBD6Ovkcw/image-shrink_1280/0/1690297624285?e=1697000400&v=beta&t=EapuyJsanr-zCn45-r9irQlUGIOd3WPqy3ZuBxkdzMc"
                }
              ],
              "num_appreciations": 49,
              "num_comments": 285,
              "num_empathy": 351,
              "num_interests": 7,
              "num_likes": 10706,
              "num_praises": 411,
              "text": "You might be looking at Amazon's strongest employee... literally. 💪 \n\nOver the weekend, Strongman and Operations Specialist Luke Sperduti competed to become Wales' Strongest Man, and secured 3rd place! Congratulations on your amazing result, Luke! 🎉 We love celebrating our employees wins both at work and outside of work. \n\nDrop a comment below of something you've recently achieved that you are proud of. Big or small! 🎖️ ",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_you-might-be-looking-at-amazons-strongest-activity-7089622091250974720-cmmW",
              "urn": "7089622091250974720"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEQ2p86IZUXpg/image-shrink_1280/0/1691528521251?e=1697000400&v=beta&t=v0NinK3qedH-Zn8p6Xs7JwQRH1hfHaVO_imdm5GbKko"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFlcPk_6-JC3g/image-shrink_1280/0/1691528523271?e=1697000400&v=beta&t=pQvSygwVc94yXwNaHwRPnJ3qoy4G0TKNHyIr4Hjiv5I"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEwNGxtmUMXvg/image-shrink_1280/0/1691528523402?e=1697000400&v=beta&t=zpnFVnN1Xzsj5Dinm1_OIdsItHcmlxLlb329CUEKKmg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGd_Xzm6neilQ/image-shrink_1280/0/1691528524169?e=1697000400&v=beta&t=XDoqI6CikDeukraR0zkKdAGbneJ3PsxvMf_KqWa6uSQ"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGmarl6hZHQ8g/image-shrink_1280/0/1691528526085?e=1697000400&v=beta&t=eOXuWFQIPb6oI3M2aXAWjo5sEN7KVNlozShG2pFgNg0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGm4KX5YGFKtw/image-shrink_1280/0/1691528528710?e=1697000400&v=beta&t=859mnuLc5c0bMv_zHuSgxeUFnhq3GLsQDpJ7yZN0umA"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQGLMrYbwrjY_A/image-shrink_1280/0/1691528529628?e=1697000400&v=beta&t=rFGuo8hI3NjhYf7qu5YoGfkkjFMbvVQtfNfc9OgHX44"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQFixH6rCwpooA/image-shrink_1280/0/1691528530686?e=1697000400&v=beta&t=zcHgjWDVwlJX7C84oy0SxQuivz5xHw7msmVj20p-BwM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEeC512g2b1ng/image-shrink_1280/0/1691528531716?e=1697000400&v=beta&t=cehctR--IPQyIw4YzIUBv7uJb4H9NDcbnfr1KVxjreQ"
                }
              ],
              "num_appreciations": 184,
              "num_comments": 351,
              "num_empathy": 2541,
              "num_interests": 7,
              "num_likes": 13275,
              "num_praises": 92,
              "text": "In honor of #InternationalCatDay, we thought we'd share some adorable photos from some of our favorite 'cat'stomers. 🐱 📦 \n\nWhile your Amazon order might be for you, the box is always for the cats. As the saying goes, \"If it sits, it fits!\"\n\nWe would love to see a photo of your cat curled up in an Amazon box in the comments! 🔽 😍 \n",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_internationalcatday-activity-7094784894072999936-Q0ay",
              "urn": "7094784894072999936"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEEOnFoA2WYMQ/image-shrink_1280/0/1690480804099?e=1697000400&v=beta&t=Rgt_V_DUOhEry5kIS06AWdlD3qtR8qsAI63FSuwNOjg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQHwVRXSm3MUnw/image-shrink_1280/0/1690480805716?e=1697000400&v=beta&t=xcpQWXG96SdmzZJKLLhp-D-RQ0Xj4f-MkfPvtrmq-3I"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEVYZj0KAUATw/image-shrink_1280/0/1690480807354?e=1697000400&v=beta&t=cMZN-rNrU5jWjj0qT3GDVY7ktC9t7X7Nfl39GrOPt1Q"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQET6Ed7c9u-Iw/image-shrink_1280/0/1690480808505?e=1697000400&v=beta&t=cdXcKhTFEcwejI3vj5HNSZdTNZL0-24MSwk_ss-8cuw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQE4hokPHdfffw/image-shrink_1280/0/1690480808402?e=1697000400&v=beta&t=9Yy1vdSpUvBeqJ9CpnhqCusYlyx840Tk9_7RqPAn6vM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQH9qLj-ockQlQ/image-shrink_1280/0/1690480808901?e=1697000400&v=beta&t=xZT1ahF0jzHN7kykuQ5qroupbPpTE-TgBj2Wpx8V9wo"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEq1I7WpsyU9A/image-shrink_1280/0/1690480810945?e=1697000400&v=beta&t=51nfBKPba4eu0W16XnmY_tRXJKnh64k894s8gtdtzBw"
                }
              ],
              "num_appreciations": 41,
              "num_comments": 101,
              "num_empathy": 144,
              "num_interests": 7,
              "num_likes": 3150,
              "num_praises": 113,
              "text": "Abe Diaz, principal technical product manager for Disaster Relief by Amazon and his team are making a world of a difference, providing critical support to those affected by disasters worldwide.\n\nDiaz, who was born and raised in Puerto Rico, is no stranger to hurricanes, having experienced these disasters firsthand. He grew up knowing how important it was to be prepared when disaster strikes, and brought his learnings into his career.\n\nWe’re proud to have Abe Diaz and his disaster relief team on the front lines, helping communities recover and rebuild after disasters strike. \n\nLearn how their team mobilizes resources, partners with local organizations, and deploys cutting-edge technology to provide swift aid when it matters most. ➡️ https://amzn.to/479nZU4\n\n#AmazonInTheCommunity #DisasterRelief #team #inspiration",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_amazoninthecommunity-disasterrelief-team-activity-7090390432584470529-Z40K",
              "urn": "7090390432584470529"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQGbWseFVxalqA/image-shrink_1280/0/1688973302544?e=1697000400&v=beta&t=-TllAh5JAB9zvuW4WWJdof98BKPmizEww8Am_XacMZw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQE2dQHxMmAd1w/image-shrink_1280/0/1688973303487?e=1697000400&v=beta&t=-Nrfpy3oRuYS6JstjQzMJUrejvsxYkSieWiqUw7szPo"
                }
              ],
              "num_appreciations": 65,
              "num_comments": 156,
              "num_empathy": 396,
              "num_interests": 10,
              "num_likes": 9088,
              "num_praises": 407,
              "text": "From London 🇬🇧 to Paris 🇫🇷\nThese incredible Amazonians embarked on an epic 280 km cycle fundraiser, while another group cycled 118 km from London to Brighton, altogether raising £41k+ for NHS Charities Together 💙 \n\nDonations are still open, with all money going to support NHS charities in their vital work to ensure that everyone can have better healthcare. https://amzn.to/3CZX6UX",
              "time": "3mo",
              "url": "https://www.linkedin.com/posts/amazon_from-london-to-paris-these-incredible-activity-7084067502091100162-DUBQ",
              "urn": "7084067502091100162"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHADVllQzPp7g/image-shrink_1280/0/1691154003263?e=1697000400&v=beta&t=9QLbl_uTLmz2wOIqo4tPSv7SeM6Ebye39k7y9viRy10"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHTk8fQGUJ1ig/image-shrink_1280/0/1691154005531?e=1697000400&v=beta&t=GWjwMXc8_v0VwiqsCGPX_tVwKLFm1RTpo5DRsNFF0DU"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQEdlkamwgSFTg/image-shrink_1280/0/1691154007692?e=1697000400&v=beta&t=PCzmczCpb6RccuV1n8QkXP1g_ad9qup1s22NzKpGi14"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQF5BDmAtwPiHg/image-shrink_1280/0/1691154009425?e=1697000400&v=beta&t=AL0ITkUiTuqCoEAhPpkRMK5hfKIf2NuFkYZwXay4XKI"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQF7i07drMEaOg/image-shrink_1280/0/1691154010804?e=1697000400&v=beta&t=wDdU8TgS8Ra_O3XFlz5IlWoYvodSLEpPSEIXcER6hZk"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5610AQHhudBE255Urg/image-shrink_1280/0/1691154013123?e=1697000400&v=beta&t=TH4W0ioxrW4Hvu5wkWAKLxeDBSq324gfCfPzHCo676g"
                }
              ],
              "num_appreciations": 30,
              "num_comments": 106,
              "num_empathy": 284,
              "num_interests": 22,
              "num_likes": 5027,
              "num_praises": 196,
              "text": "We deliver to one of the Seven Wonders of the World - the bottom of the Grand Canyon.\n\nNine miles below the South Rim lies Phantom Ranch, a historic oasis. There are no roads at the bottom - the only way to get there is on foot, river raft, or by mule.\n\nOur delivery partners travel by mule on a 4-hour journey to deliver packages (and smiles) to customers who live and work at Phantom Ranch.\n\nSaddle up 🐴 and take a ride on a mule with us as we follow them on their journey! https://amzn.to/3q97Hu1",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_we-deliver-to-one-of-the-seven-wonders-of-activity-7093214047340265472-A0Ii",
              "urn": "7093214047340265472"
            },
            {
              "images": [],
              "num_appreciations": 22,
              "num_comments": 136,
              "num_empathy": 120,
              "num_interests": 8,
              "num_likes": 2592,
              "num_praises": 136,
              "text": "Our 2022 Sustainability Report just dropped. Here is a breakdown of some top highlights:\n\nSince 2015, we've reduced the average weight of packaging per shipment by 41%, avoiding more than 2 million metric tons of packaging. That is the weight of more than 230 Space Needles - the iconic Seattle landmark located near our HQ.\n\nIn 2022, 90% of the electricity consumed by Amazon was powered by renewable energy sources. This includes more than 400 wind and solar projects from around the world. \n\nWe had more than 9,000 electric delivery vehicles in our global fleet, and 145 million packages were delivered by EVs in the U.S. and Europe. \n\nWe co-founded The Climate Pledge, a commitment to reach net-zero carbon by 2040. By the end of 2022, we had 396 companies sign the pledge, and today, there are more than 400 across 55 industries and 39 countries. \n\nThese are just a few examples of how we are taking big swings to decarbonize our operations. Decarbonizing Amazon's operations is a challenging goal, but as a company, we don't shy away from grand challenges. It is our mission to minimize Amazon's impact on the planet and the communities in which we live and work, through meaningful actions that address climate change. 🌱 ♻️ \n\nRead more about the Sustainability Report here: https://amzn.to/3PY2Sy7\n\n#Sustainability #TheClimatePledge #InsideAmazon \n",
              "time": "2mo",
              "url": "https://www.linkedin.com/posts/amazon_sustainability-theclimatepledge-insideamazon-activity-7087083850429792256-TrPP",
              "urn": "7087083850429792256",
              "video": {
                "duration": 57766,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4D10AQHRs7VzUTVrQg/mp4-720p-30fp-crf28/0/1689692433486?e=1697000400&v=beta&t=xLvnAVmITVR2gI4CWYkKwXhD8UeEBolq37T7FqvdpDU"
              }
            },
            {
              "images": [],
              "num_appreciations": 25,
              "num_comments": 75,
              "num_empathy": 182,
              "num_interests": 8,
              "num_likes": 2996,
              "num_praises": 94,
              "text": "Today's the day! We hit the streets near our Seattle HQ1 campus to ask people what they're most excited to buy this Prime Day. What would your answer be? 📦 🎉 \n\n*Bonus points if you can comment it in emojis, and a +1 if it's a Climate Pledge Friendly product or from an independent seller. ♻️ \n",
              "time": "3mo",
              "url": "https://www.linkedin.com/posts/amazon_todays-the-day-we-hit-the-streets-near-activity-7084527532733079552-U-KV",
              "urn": "7084527532733079552",
              "video": {
                "duration": 45666,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4D10AQE-F8cZCaV3Ow/mp4-720p-30fp-crf28/0/1689082984406?e=1697000400&v=beta&t=RLkN11O1PvmzFRb-KGdCxyx1vTBGTDEpdUP48_Bw2Do"
              }
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQFXfrhpwyflGQ/feedshare-shrink_2048_1536/0/1687109498009?e=1699488000&v=beta&t=wB49ECTvrDHWbv9I89kOHSj2Tm-uxaAq5-4qAPSJMNU"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQElAiQ6BvmMLg/feedshare-shrink_2048_1536/0/1687109495776?e=1699488000&v=beta&t=aIvTAteE3ugajey2unYDe_Dt32eu7sFSb0-8AU7Z3MQ"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQEdyG-bl29wXA/feedshare-shrink_2048_1536/0/1687109496063?e=1699488000&v=beta&t=XnPfatRTY_TNqrVOXxYLBY3AJvuK7Qop_NmXq0m2Oac"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQFOaYxZ54rfFg/feedshare-shrink_2048_1536/0/1687109495496?e=1699488000&v=beta&t=letK8-pFSMsZDY55MZh6AH02oscGIZymXZZHbX1YjC4"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQH1dXRv5K-VDA/feedshare-shrink_2048_1536/0/1687109498354?e=1699488000&v=beta&t=sG79LazyK_rqiLG4fM7bDw71lHPy_KhLlAVssygcCV4"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQFj2UBgrRIkSg/feedshare-shrink_2048_1536/0/1687109496373?e=1699488000&v=beta&t=FAsngl-curJ6ijh4oiMukJt81AlF22tEJgeSAI12Xuw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQES9RKCFPvEBA/feedshare-shrink_2048_1536/0/1687109496987?e=1699488000&v=beta&t=HKMLXng55c0MMYfU1X6DZ_sAqUpYkaS42hZ6FoAK1ZA"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D5622AQEhnO54dUE8dw/feedshare-shrink_2048_1536/0/1687109497089?e=1699488000&v=beta&t=6bx6OyE0aoYSLEJ_7GZz2_j_SSBadO6dJBqJeQyLpLQ"
                }
              ],
              "num_appreciations": 87,
              "num_comments": 125,
              "num_empathy": 803,
              "num_interests": 7,
              "num_likes": 10307,
              "num_praises": 286,
              "text": "Happy Father's Day to all the dads out there, especially our Dadazonians.\n\nTo all those who have lost fathers, and fathers who have lost children. To stepfathers and fathers who've adopted. To those who have great relationships with their fathers, and those with strained ones. \n\nWe're sending lots of love your way today. 💙 \n\n#Amazon #FathersDay",
              "time": "3mo",
              "url": "https://www.linkedin.com/posts/amazon_amazon-fathersday-activity-7076250124670156800-ZHva",
              "urn": "7076250124670156800"
            },
            {
              "article_subtitle": "aboutamazon.com • 2 min read",
              "article_title": "4 cool facts about Hercules, the small-but-mighty robot in Amazon's fulfillment centers",
              "images": [],
              "num_appreciations": 8,
              "num_comments": 68,
              "num_empathy": 54,
              "num_interests": 110,
              "num_likes": 4037,
              "num_praises": 115,
              "text": "Meet Hercules, our small-but-mighty robot that plays an important part in packing your Amazon order! 📦 🤖 \n \nHercules improves safety and efficiency for our employees by traveling around our facilities to retrieve shelves of products and deliver them to employees, who then pick and pack the items that our customers ordered.\n \nLast week, Hercules was honored at a new gallery featuring iconic artifacts from innovative companies at Nasdaq’s headquarters in New York City, and we’re thrilled that Hercules was included.\n\nLearn more here: https://amzn.to/3PdlxnE\n\n#Amazon #Innovation \n",
              "time": "2w",
              "url": "https://www.linkedin.com/posts/amazon_4-cool-facts-about-hercules-the-small-but-mighty-activity-7107769674251059200-eIpq",
              "urn": "7107769674251059200"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFL98vXyLecTw/feedshare-shrink_2048_1536/0/1686316203181?e=1699488000&v=beta&t=2alK0au2Hl2ge7feQOyizOuHHY-yAHqJh3S8_0ad1JI"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGuQ6Cs50WC6A/feedshare-shrink_2048_1536/0/1686316204134?e=1699488000&v=beta&t=4GGN5tjaJ7dJkTFHYBcuXj7jXbqdaH5Hzhlk_AKyVSg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQE0dNhlVPNSqg/feedshare-shrink_2048_1536/0/1686316205758?e=1699488000&v=beta&t=ZKg2nuYMhgiJ0-GUTiNDCv4hLK5Rze9oxONnbbnb-hI"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFBxYRE6UNt6w/feedshare-shrink_2048_1536/0/1686316206396?e=1699488000&v=beta&t=kAJY0cEH7xATmn2TGkdAX-I84T44vj2ONh-uZdrwLvg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQG0iJMTSpKHtQ/feedshare-shrink_2048_1536/0/1686316207838?e=1699488000&v=beta&t=LCY1UAO4Zw9jGFcxuyi94z0_NHQAXB5h30rQeou4OI4"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEAaVGpK0Spmg/feedshare-shrink_2048_1536/0/1686316209178?e=1699488000&v=beta&t=B4ZH1QP2fDuXDELyYGaYUTWogcTOgOXuOJgpV76eFxY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGsDy0kKY3eKg/feedshare-shrink_2048_1536/0/1686316210625?e=1699488000&v=beta&t=7EBJoUnmQgKaLpdtJANGDBOVEAkn2n4OdSQb3356TE8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFgjaGZKtI_9w/feedshare-shrink_2048_1536/0/1686316211718?e=1699488000&v=beta&t=D-PrtL2r9Y4wjYTMOJ9Ri-vT83p-IZFhWmgNWmrA59Y"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQH4weqXm_nyTA/feedshare-shrink_2048_1536/0/1686316213152?e=1699488000&v=beta&t=W3DT-eLzE4S8DHNPcEDrKtm3uuj5SMd6W_10I7HNHf4"
                }
              ],
              "num_appreciations": 83,
              "num_comments": 424,
              "num_empathy": 1654,
              "num_interests": 53,
              "num_likes": 27267,
              "num_praises": 518,
              "text": "We might be biased, but we believe we have the coolest office setups around the world. 🌎🌳 This month we’re celebrating the 5th birthday of the Spheres located in Amazon’s Puget Sound headquarters. The Spheres offer a natural oasis in the middle of Downtown Seattle. The three domes house four stories of waterfalls, fish tanks, and flexible workspaces. \n\nHere are several unique features that make The Spheres a beyond cool place to call 'the office.'\n\n❇️ Fish from the Amazon rainforest. Most people know the Seattle Spheres for the plants, but there are other living species that call the facility home. We’ve hired an expert with a doctorate in animal behavior to help design the environment within each tank and provide ongoing care to keep the fish happy and healthy.\n\n❇️ There are indoor waterfalls. The three domes house 4 stories of waterfalls, and one of the first things you see upon entering the Spheres is a large waterfall. The sound of it creates a calming environment.\n\n❇️ Serene workspaces. Booths and tables throughout the Spheres offer a space where Amazon employees have everything they need to work among the natural surroundings. Imagine calling a forest your workspace?!\n\n❇️ The ultimate relaxation space. The third floor of the Spheres offers a quiet corner with lounge chairs where visitors can sit back and relax in the sun.\n\n❇️ Free bananas. That’s right, free to anyone who passes by! As the saying goes, there’s no such thing as a free lunch, but at HQ1 there sure are free bananas at our Banana Stand, located just outside the Spheres.\n\nLearn more about the many other features that make the Spheres a unique and incredible place to call ‘the office': https://amzn.to/43tfi4N \n\nWhat is your favorite thing about them?\n\n#LifeAtAmazon #CoolWorkplaces #InsideAmazon \n",
              "time": "4mo",
              "url": "https://www.linkedin.com/posts/amazon_lifeatamazon-coolworkplaces-insideamazon-activity-7072922863250333696-98vA",
              "urn": "7072922863250333696"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4D22AQF7e2-_ttnvxA/feedshare-shrink_2048_1536/0/1687348801398?e=1699488000&v=beta&t=wr4jj5QW7UAWjtJSDsE8ngEW7GPIaqvMEC3ytBk2j2k"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D22AQGK7O1WcePUmw/feedshare-shrink_2048_1536/0/1687348806072?e=1699488000&v=beta&t=jxDR_sHEngs3aW_xkYyMQ6jWqnoZx9k5l3EWdOz6rjs"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D22AQEJS0dFBC9tsg/feedshare-shrink_2048_1536/0/1687348803566?e=1699488000&v=beta&t=j_SaIICZhi12syCBVrFqIgS-HD8YQO85O-n06u32MNs"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D22AQHmwf3JtFnfvg/feedshare-shrink_2048_1536/0/1687348802955?e=1699488000&v=beta&t=Oe9fZacbtnjuxktjWEKWMQFx-O6zZj_-vIpBGQCe-zY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D22AQF3Ma6ZKJ704g/feedshare-shrink_2048_1536/0/1687348804193?e=1699488000&v=beta&t=yasgBK_KHFzYJvNQBV-LZKt0cohnbQrl0kqmJMF7VSY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D22AQHQsPytWoKd_A/feedshare-shrink_2048_1536/0/1687348804616?e=1699488000&v=beta&t=Xfw1UoWjG0OHLvzVj70l3bBPFaBKdhCodsSfdRnGwqM"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D22AQGWIeuPFMJrVg/feedshare-shrink_2048_1536/0/1687348805056?e=1699488000&v=beta&t=582HlkcG7I-8HsdzGAFJWHxWiXCqv3wbUcf30AAggv0"
                }
              ],
              "num_appreciations": 40,
              "num_comments": 67,
              "num_empathy": 141,
              "num_interests": 4,
              "num_likes": 3097,
              "num_praises": 100,
              "text": "We’ve just set up our first Disaster Relief Hub in Japan, a country that is one of the world's most vulnerable to natural disasters. The hub will help us quickly respond to calamities in the region, and is an especially meaningful initiative for us because we've been a part of the Japanese community for 23 years. \n\nThe facility, located in the area where the devastating Great Hanshin-Awaji earthquake took place in 1995, is a dedicated space within our logistics network to store and quickly pack items that are most needed following earthquakes, damaging storms and other emergencies. It will enable us to swiftly distribute over 15,000 essential supplies within 72 hours, including traditional local items like Japanese folding fans, and solar-powered generators that don't emit any smoke or smell.\n\nThanks to our teams, NGO partners and the Amagasaki City government for working to build this together. We're committed and ready to lend support through even the worst of times.\n\n#AmazonInTheCommunity #Amazon",
              "time": "3mo",
              "url": "https://www.linkedin.com/posts/amazon_amazoninthecommunity-amazon-activity-7077253879771373569-BDmf",
              "urn": "7077253879771373569"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQE__Dy2HI5N0w/image-shrink_1280/0/1688044501228?e=1697000400&v=beta&t=7hCDQLGttSB74iixrW7WFNEzRKOVsd5V9zSAPu4o-Jk"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQGVmRimzPlLJg/image-shrink_1280/0/1688044505733?e=1697000400&v=beta&t=BmZQhINHXNZBc1BSUN97MgfEguU1rDsAp_p9qvXo6CY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQGno2RNHgR_sw/image-shrink_1280/0/1688044505469?e=1697000400&v=beta&t=pj2sVSHzrpeMZp6_wOnvda4FNUCnp5bGIIfIWcvSujc"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQEKhDYcNYE6fg/image-shrink_1280/0/1688044506812?e=1697000400&v=beta&t=Jw7QnZphw8LRs7sK81TE4D3RgQy3E1oZplM_PEPt-U8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4D10AQH6KDSsR43G2Q/image-shrink_1280/0/1688044507044?e=1697000400&v=beta&t=HglfTuNImKl5kkRkINMklCLONh7UGha0q-aluamw0cM"
                }
              ],
              "num_appreciations": 148,
              "num_comments": 68,
              "num_empathy": 207,
              "num_interests": 6,
              "num_likes": 3068,
              "num_praises": 57,
              "text": "Meet Craig. Craig was able to beat a rare and difficult-to-treat cancer with the help of Amazon benefits.\n\nBefore his diagnosis, Craig was a pillar of health. His evenings were spent having quality time with his wife, daughter, and their dog, and on weekends, you could catch him practicing Krav Maga martial arts. All of that changed when he developed invasive squamous cell carcinoma – a difficult-to-treat type of head and neck cancer.\n\nTo support employees like Craig, Amazon has signed the Working with Cancer pledge to signify a continued commitment to providing a supportive workplace culture for employees with cancer. That includes providing leading health care benefits and a dedication to fostering compassion in managers and leaders across the company. A supportive work culture is just one way Amazonians can feel supported amid cancer diagnosis, treatment, and recovery.\n\nHere are three ways Amazon supports employees and their family members impacted by cancer. ⬇️\n\n🟣 In-house case management team dedicated to helping any and all cancer-related needs: We have a team dedicated to helping navigate work, care, benefits, and resources amid cancer diagnosis, treatment, and recovery.\n\n🟣 World-class cancer resources and information: We partner with AccessHope to provide employees and their families access to the latest in cancer knowledge directly from National Cancer Institute – Designated Comprehensive Cancer Centers.\n\n🟣 Covered travel and lodging to get expert opinions at leading cancer centers: Employees and family members can also use AccessHope to receive an expert evaluation from a center of excellence.\n\nThrough these benefits, Craig is happily cancer free once again and able to focus his time on his family and his work at Amazon Web Services (AWS) as a solutions architect. https://amzn.to/441DfAJ",
              "time": "3mo",
              "url": "https://www.linkedin.com/posts/amazon_meet-craig-craig-was-able-to-beat-a-rare-activity-7080171832934342657-fCWG",
              "urn": "7080171832934342657"
            },
            {
              "images": [],
              "num_appreciations": 75,
              "num_comments": 349,
              "num_empathy": 2356,
              "num_interests": 16,
              "num_likes": 19821,
              "num_praises": 105,
              "text": "Thanks to our team over at Ring, we interrupt your work day with a 'beary' important message. 🐻 ",
              "time": "1mo",
              "url": "https://www.linkedin.com/posts/amazon_thanks-to-our-team-over-at-ring-we-interrupt-activity-7097614294422360064-zFmN",
              "urn": "7097614294422360064",
              "video": {
                "duration": 41800,
                "stream_url": "https://dms.licdn.com/playlist/vid/D5610AQHi0Ja-2jq36Q/mp4-720p-30fp-crf28/0/1692203113310?e=1697000400&v=beta&t=KK6oJSylCdy6drotk982N6hSODoADsba6oVjShbsOVU"
              }
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGMWnDABIfeXw/feedshare-shrink_2048_1536/0/1686588121567?e=1699488000&v=beta&t=rXQp4EFz0T4oJbxLTQp5L9HpkgtyxJJeTMDVNtoUUjE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGkkydq-Ny8Gw/feedshare-shrink_2048_1536/0/1686588122135?e=1699488000&v=beta&t=T169AFSGWZU8cYrO5nKaIG3w4nda4woch9kHg7C5Fyk"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFWg-2Q3YCz7w/feedshare-shrink_2048_1536/0/1686588122894?e=1699488000&v=beta&t=7zN0U2JhlQo-CcYAIIYozzhsSbQavZg4FfPhwW0SYmQ"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFZsCxPxTObbA/feedshare-shrink_2048_1536/0/1686588123852?e=1699488000&v=beta&t=YPnG4AUeKkothQxfbmRov18lUTO0OLC_CfmLn3f8s5k"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQF_w-ggHnkATQ/feedshare-shrink_2048_1536/0/1686588124604?e=1699488000&v=beta&t=-_noXfv2Sq8zZ-CkWgQC3tFmYGaFmvCD8UcINuIqCsk"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFsHySFqtjMkg/feedshare-shrink_2048_1536/0/1686588125995?e=1699488000&v=beta&t=nF-0bgT6bH3LYg_8XitWY1qDM6-AZW0ddLRzzbtJoVI"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQG5n_wN2Fs8pg/feedshare-shrink_2048_1536/0/1686588126078?e=1699488000&v=beta&t=P-_CFj-9u9Q4ng6w73iwVSP_0RPAyWJmM18NI9B1kEY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEYbMVAGGPCYg/feedshare-shrink_2048_1536/0/1686588127014?e=1699488000&v=beta&t=rjF1Zy9kIhKQ3dcCat7caGqG7SQRka9NX1Qbl99HbnQ"
                }
              ],
              "num_appreciations": 30,
              "num_comments": 56,
              "num_empathy": 299,
              "num_interests": 9,
              "num_likes": 4628,
              "num_praises": 136,
              "text": "We are excited to share Amazon’s 2022 Small Business Empowerment Report, which further highlights the success of independent sellers in Amazon’s store. \n\nThe economy this past year saw rising interest rates and inflation not seen in nearly 40 years. Many businesses faced supply chain issues as a result of the global pandemic and its after effects. Despite these challenges, small and independent business sellers in Amazon’s store continued to provide a vast selection of amazing products, low prices, and great convenience for our customers.\n\nBut we know that photos of graphs can sometimes be boring, and our followers love it when we post photos of dogs. So we’re using our ‘small’ Pupazonians to help us deliver some highlights from our Small Business Empowerment Report.\n\nWhat is your favorite takeaway? Full report here: https://amzn.to/45TqTMp\n\n#SmallBusiness #Amazon \n",
              "time": "4mo",
              "url": "https://www.linkedin.com/posts/amazon_smallbusiness-amazon-activity-7074063334978789376-4X9l",
              "urn": "7074063334978789376"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQF81H3m8LTrKQ/feedshare-shrink_2048_1536/0/1686664804506?e=1699488000&v=beta&t=bu8sCK7GVe2isjqGraUfJq0Ta0ZYzKIEuP1ufD0X3vY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFV7ZmV3Dub4A/feedshare-shrink_2048_1536/0/1686664805427?e=1699488000&v=beta&t=8fvdakSt3_QisfojKTYtJwbQypIw6qQXMFo0tWmhtr8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFWLReWgzta5Q/feedshare-shrink_2048_1536/0/1686664806307?e=1699488000&v=beta&t=gL6nCU1DfzQ0jCrfy-CtBvGIYN9ZqMiY1do-Xz4p61g"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFifGAH74grxw/feedshare-shrink_2048_1536/0/1686664807501?e=1699488000&v=beta&t=v7vplqtyE0_ifpDTbeiS7PtElzu03Kw1TLeWYTJLyIw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFK9foVgwrGvg/feedshare-shrink_2048_1536/0/1686664808809?e=1699488000&v=beta&t=LY-kzUFAsZpX0sYp8CLENe8juxH8WBPqaxDtXEQV4gE"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGSQXD0sxAtGw/feedshare-shrink_2048_1536/0/1686664810600?e=1699488000&v=beta&t=i47pfBGAzIAcnpajXiAfKuqknZrDkb0NFLWZOwEUwi0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFFgY1MfE-GyA/feedshare-shrink_2048_1536/0/1686664810881?e=1699488000&v=beta&t=tU0mdp5NSlml1prf3JP3s1uYnV8tPnPxo5womw00N74"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQHrjfxWe_LFNQ/feedshare-shrink_2048_1536/0/1686664811606?e=1699488000&v=beta&t=9scpqk565tRjOQ4iPfUG73zplZTrLSPLuzVdpeX2YOk"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGCnXv6i5uqyw/feedshare-shrink_2048_1536/0/1686664817490?e=1699488000&v=beta&t=15bQOIJXkrdB-jU80owZIH167Gn5uXqYkJ0z6drVUMU"
                }
              ],
              "num_appreciations": 47,
              "num_comments": 165,
              "num_empathy": 471,
              "num_interests": 13,
              "num_likes": 11280,
              "num_praises": 510,
              "text": "We’re celebrating a big milestone in India this June: 10 years of Amazon.in! 🎉\n \nWhen we went live in India in 2013 (check out the last photo capturing that moment!), sellers weren't exactly queuing to sign up. \n\nThey were unfamiliar with the concept of selling online and couldn't imagine that people across India would actually want to buy products that were not in a physical store.\n \nIt was clear that the India marketplace was built differently, and that we needed not just innovation, but Indian ingenuity and execution agility to make things happen. \n\nSo we searched for a team of builders who were inspired by the idea of helping to digitize India and making a difference to lives in the country they grew up in.\n \nCut to today, and we've digitized over 4 million small businesses, enabled over $5 billion in cumulative exports, and created more than 1.1 million direct and indirect jobs in India.\n \nThank you to the people who built a business that is truly \"made in India\" and invented unique solutions for our Indian customers. \n\nWith India’s young and vibrant population, rising income levels, and growing penetration of internet and social media, the next 10 years looks to be even more exciting. We’re really just getting started.\n \nLearn more about Amazon India's milestones over the last decade at https://lnkd.in/e6w6WjC9.",
              "time": "4mo",
              "url": "https://www.linkedin.com/posts/amazon_were-celebrating-a-big-milestone-in-india-activity-7074385015115018240-5eOz",
              "urn": "7074385015115018240"
            },
            {
              "images": [],
              "num_appreciations": 29,
              "num_comments": 80,
              "num_empathy": 160,
              "num_interests": 26,
              "num_likes": 3700,
              "num_praises": 121,
              "text": "Imagine breaking the Amazon.com website... 6 months into your job.\n\nAs part of the \"Meet the Amazon Leader\" series, Howard Cohen sat down with Vice President of Last Mile Delivery & Technology Beryl Tomay, where she recounted a moment when she broke the Amazon.com website just as she was starting out as a software engineer at Amazon 18 years ago.  \n\nIn her words: \"If you imagine this page blank white for several hours on Amazon.com, then you just might feel a sliver of the terror I felt six months out of school.\" \n\nHer advice for leaders: Don’t be afraid to fail and always take away learnings from your mistakes to make you even stronger. \n\nYou can watch the interview in its entirety here: https://amzn.to/3qomBfz\n\nTell us about a time when you learned from a failure in the comments! #LifeAtAmazon #Engineering #Leadership",
              "time": "4mo",
              "url": "https://www.linkedin.com/posts/amazon_lifeatamazon-engineering-leadership-activity-7071849549773860864-g1sl",
              "urn": "7071849549773860864",
              "video": {
                "duration": 58433,
                "stream_url": "https://dms.licdn.com/playlist/vid/D4E05AQFDMAIlf6J6uA/mp4-720p-30fp-crf28/0/1686060300545?e=1697000400&v=beta&t=x4UpsU8vbZxYtYQXx89p1IBtmxnu_eZ1iPVTHYPbDPg"
              }
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFCRp655STEHQ/feedshare-shrink_2048_1536/0/1684780502300?e=1699488000&v=beta&t=sc1K62B4411m2b4I97mEJeNV3cMfrMw27GiGMBAuf-s"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEGcNpeyTj_fA/feedshare-shrink_2048_1536/0/1684780503199?e=1699488000&v=beta&t=U7GvM-CtLSZRJRUyL7uEdh7KpbS12_07v6ItYDXrBsY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEpOg86R2YdZQ/feedshare-shrink_2048_1536/0/1684780504504?e=1699488000&v=beta&t=cnKsSdyFcgHUmvtgFOnm3BviDgzg5rIhGay1e8aocig"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEQgY6_NbhQ4Q/feedshare-shrink_2048_1536/0/1684780505177?e=1699488000&v=beta&t=S0h3r_UKIQti3AW6EIo5dmeONAeJ9JK6eov38BTHUY0"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQE8c1nv7k8w1w/feedshare-shrink_2048_1536/0/1684780505850?e=1699488000&v=beta&t=A3S7TW8HsmbMAXZDeB9nHkd5xIQpH6B5ReGYL8Rdw2E"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQHyZFkwpEa2-w/feedshare-shrink_2048_1536/0/1684780506918?e=1699488000&v=beta&t=P1tk29QkXo6XS4R7BOJylfUDPQg0f2PcvORfdEfxWMo"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGlgBvObtR9gw/feedshare-shrink_2048_1536/0/1684780507464?e=1699488000&v=beta&t=8kNsgsznDNRbPkaGqZ5b14weL8V80OYLppGyrLcACiU"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEfhDTic-TimQ/feedshare-shrink_2048_1536/0/1684780509503?e=1699488000&v=beta&t=BjruIVuKPNJUbQ35PfK-JpqUjJ2VwBemQ_iJj_vxRwY"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQG5JzXJBIzquw/feedshare-shrink_2048_1536/0/1684780508705?e=1699488000&v=beta&t=mgNoAapR1K2MlIuRkxmOgieOfaOM9jKpaPRXRZLTLfo"
                }
              ],
              "num_appreciations": 38,
              "num_comments": 414,
              "num_empathy": 999,
              "num_interests": 29,
              "num_likes": 13695,
              "num_praises": 503,
              "text": "We're giving you an exclusive first look inside our new HQ2 office, which opened today in Arlington, Virginia! 👀 \n \nFrom dog parks, children's areas, and seasonal farmer's markets, to rooftop terrace meetings and lunch at local small business eateries, there's so much to enjoy. \n \nWhether you're an Amazonian or happen to be in the community, we hope that you come say hi! 🎉 \n\nhttps://lnkd.in/gPMybudQ\n",
              "time": "4mo",
              "url": "https://www.linkedin.com/posts/amazon_were-giving-you-an-exclusive-first-look-activity-7066481651291148288-qfTv",
              "urn": "7066481651291148288"
            },
            {
              "images": [],
              "num_appreciations": 17,
              "num_comments": 112,
              "num_empathy": 131,
              "num_interests": 9,
              "num_likes": 2909,
              "num_praises": 120,
              "text": "Amazon Web Services (AWS) has invested in Hugging Face, further expanding our collaboration. This is the next step in our efforts to accelerate the availability of next-generation machine learning models by making them more accessible—and helping developers optimize performance at a lower cost. Congrats to Clem Delangue 🤗 and the entire team, and we look forward to seeing what developers create for customers using these models.",
              "time": "1mo",
              "url": "https://www.linkedin.com/posts/amazon_super-excited-to-welcome-our-new-investors-activity-7100481244798312448-yQBV",
              "urn": "7100481244798312448"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGKU5FhsudoUA/feedshare-shrink_2048_1536/0/1685630161898?e=1699488000&v=beta&t=CX4GAtc_Zqhoh0dg2oEgSa9hObiiBtbyVZxk1eoObFU"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQF65WYAr3tOCQ/feedshare-shrink_2048_1536/0/1685630162897?e=1699488000&v=beta&t=cBuayd62xyMvcshbIdH9PLAWEDEkHHlxlQpdZ4Suxi4"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFmlaLuCd6VPA/feedshare-shrink_2048_1536/0/1685630163585?e=1699488000&v=beta&t=rr7XMAGhwVHctbIxTvAuA9ftS4zr1bwyhek_uSNd15Y"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEJFg0JDttyMQ/feedshare-shrink_2048_1536/0/1685630164431?e=1699488000&v=beta&t=3j-xZ12xHcC9rgry_KkGy-UOWGZpcrbBhSnQyZX0418"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQHRx9sq8W0QhA/feedshare-shrink_2048_1536/0/1685630165286?e=1699488000&v=beta&t=qmXT2HgdzJyOxoouT9_Xh56mJlMlSxJiex0-_2eq_e4"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEvs4wDu9QAnA/feedshare-shrink_2048_1536/0/1685630166087?e=1699488000&v=beta&t=Iv29qINelsny1DRfYX-Fx4TdZ-nGyt31BZQ5DY2g1Gg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQF-eZbzf2pPKQ/feedshare-shrink_2048_1536/0/1685630166621?e=1699488000&v=beta&t=HRtA-gR0K01awclvf7IIeQf6zJ9ylgwmv7dD30sW3cg"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQHZLwHhwaPdXg/feedshare-shrink_2048_1536/0/1685630167216?e=1699488000&v=beta&t=v5xu-My5dWtiszsb-ALDj4T2fUhFlmRcJNoJzyAd2pk"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQHlH_eDPpRs-w/feedshare-shrink_2048_1536/0/1685630167819?e=1699488000&v=beta&t=MawA5N0uFOZstV8qy41jzbifWvmFi_5TDEuTtcTHKv8"
                }
              ],
              "num_appreciations": 13,
              "num_comments": 62,
              "num_empathy": 185,
              "num_interests": 5,
              "num_likes": 4683,
              "num_praises": 137,
              "text": "This month, we are proudly and publicly opening our doors to our HQ2 at Metropolitan Park in Arlington, Virginia. Why is this important? This office is so much more than just an office; it's a community.\n \nThe Met Park office is surrounded by vibrant small businesses that will bring together employees, residents, and visitors to create one amazing neighborhood. These small businesses are women- and minority-owned, as well as some local favorites that provide an opportunity to support entrepreneurs and owners in a variety of industries. You can find a new bike to ride around the area, drop your kids off at daycare, get your pets groomed, get your sweat on, and even take in some contemporary art. Here is a sampling of some of the small businesses that you'll find at Met Park:\n \nConte's Bike Shop: A family-owned shop that’s been a mainstay of the Eastern Seaboard bicycling community since 1957. Biking to work has never been so fun or accessible!\n\nCelebree School: From infant care, to before and after-school programs, to summer camp, Celebree plays an important role in helping families raise independent, thoughtful children who are excited about learning.\n \nHUSTLE Fitness: Launched during the pandemic but as an online platform, HUSTLE is opening its very first brick-and-mortar location at Met Park and welcomes participants of all fitness levels.\n\nMaker's Union: Another business that only recently opened during the pandemic, the Maker's Union earns its name by serving up produce, proteins, beer, and coffee from local makers.\n \nClick the link below to learn more about all the other businesses that call Met Park home! \n \nIf you were to come visit us, where would your first stop be? #LifeAtAmazon #Community #SmallBusiness\n \nhttps://amzn.to/3MKxFLv\n",
              "time": "4mo",
              "url": "https://www.linkedin.com/posts/amazon_lifeatamazon-community-smallbusiness-activity-7070045363126071296-cwpE",
              "urn": "7070045363126071296"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQHIm57E6gF9UQ/feedshare-shrink_2048_1536/0/1685067301681?e=1699488000&v=beta&t=TZWo6c0i2ZnRwx4C3GQ9VZi-hEVuMMu14ptEwz5pHpI"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEF6QjNtTGuNg/feedshare-shrink_2048_1536/0/1685067302597?e=1699488000&v=beta&t=JarET5E01A3Zm29fGSOJLJSDAfR2TfCqVWJCMgIAacU"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQFgW-Qx4h00tw/feedshare-shrink_2048_1536/0/1685067304330?e=1699488000&v=beta&t=QMBojzAZQ7w9gEy1yIU7smPsXsSjpL9D76kMaiZuLJE"
                }
              ],
              "num_appreciations": 2,
              "num_comments": 7,
              "num_empathy": 40,
              "num_likes": 325,
              "num_praises": 26,
              "text": "Have you ever wondered what kind of impactful work our interns at Amazon take on? Hear from Jasmine, our Program Manager Intern in Singapore who has been with Amazon for four months now!\n\n\"I own experimental customer success and sales programs in Amazon. My team is a specialist sales team that focuses on Enterprise Resource Planning (ERP) systems.\"\n\nJasmine gets to invent and run sales programs utilizing innovative methods like gamification. She is passionate about creating breakthroughs for customers. \n\n\"At Amazon, I'm encouraged to dive deep, think big, and be the best version of myself! Additionally, I have supportive Amazon leaders who always makes time for our 1:1’s in their work to share their experience\".\n\n#InsideAmazon #AmazonIntern",
              "time": "4mo",
              "url": "https://www.linkedin.com/posts/amazon_insideamazon-amazonintern-activity-7067684550855774208-r0XA",
              "urn": "7067684550855774208"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQF4QIm3SxoR3A/feedshare-shrink_2048_1536/0/1684074479209?e=1699488000&v=beta&t=Tp1t5f8pZzwLjaf-zLMvTC5kKlNJNX1AsPgcjhLo_us"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQG2gIbOYWyF6g/feedshare-shrink_2048_1536/0/1684074479694?e=1699488000&v=beta&t=nPuiqibFBsygzJwIoaYcGhhh6kqR3VhXwd3WT2X4Hjo"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEJEz6pkJSS6Q/feedshare-shrink_2048_1536/0/1684074480629?e=1699488000&v=beta&t=n8WLnm4jL5giX2wG8p82eQ7pVbm_FIXRZrrEaG7MGHs"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQHmgMUgfjsyHw/feedshare-shrink_2048_1536/0/1684074483726?e=1699488000&v=beta&t=ZibtjGXH1V6-NJIjJoNrbuZl5QNkES8cnmL8iziZAlA"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGhkhc6I7iKRw/feedshare-shrink_2048_1536/0/1684074481877?e=1699488000&v=beta&t=Oi9cnBSI0OCJINXHMvd_rAttiJcxs4nyJyqSRSPJeNw"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEVwT9pQLY7_w/feedshare-shrink_2048_1536/0/1684074482534?e=1699488000&v=beta&t=zIWD-9J6s2PPziCyPkztjeNtNQTaA6J7rMXS3zTEsv8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGIeGxNxinUxw/feedshare-shrink_2048_1536/0/1684074483502?e=1699488000&v=beta&t=IUN5Jc9TMIvl1J7RBkM0ea64p488z7sAPr5XBvD662U"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGUJXZPvNDirA/feedshare-shrink_2048_1536/0/1684074487227?e=1699488000&v=beta&t=QlCEL6ErJ7PFi6T2jvol5KFxhziCHH9w-zY6NRhtvr8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQHG6ELvGmF45w/feedshare-shrink_2048_1536/0/1684074484680?e=1699488000&v=beta&t=dPf_2Ccnl-z5Lt0kbI6LlR3No4U5s9_PtKLpbw7YigA"
                }
              ],
              "num_appreciations": 509,
              "num_comments": 327,
              "num_empathy": 1802,
              "num_interests": 10,
              "num_likes": 19316,
              "num_praises": 208,
              "text": "Happy Mother's Day to all mothers.🌸 \n\nMothers who have lost children.\n\nThose who have lost mothers.\n\nThose with strained mother relationships.\n\nMothers with strained child relationships.\n\nThose who have chosen not to be mothers.\n\nThose yearning to be mothers.\n\nAnd of course, to our amazing Momazonians. We are so lucky to have you on board.❤️ ",
              "time": "5mo",
              "url": "https://www.linkedin.com/posts/amazon_happy-mothers-day-to-all-mothers-mothers-activity-7063520372112924672-RRrz",
              "urn": "7063520372112924672"
            },
            {
              "images": [
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQGc2MvKu5lSVw/feedshare-shrink_2048_1536/0/1685725202479?e=1699488000&v=beta&t=tGhvNuVdKV2jzB4Lfp_BFHCKT2FSflb_73M1BrExlD8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQG6JWnVnZbf1g/feedshare-shrink_2048_1536/0/1685725203425?e=1699488000&v=beta&t=THLbavCcexTgHh747WHLCx7gR2lUAFG73h_9anNw4Ww"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQG7YA50wRlGSg/feedshare-shrink_2048_1536/0/1685725204771?e=1699488000&v=beta&t=5OXqZ-6Fy2STTc42wEn3vVx6uyrT18GmKqPXYDaiOT8"
                },
                {
                  "url": "https://media.licdn.com/dms/image/D4E22AQEZ9rXMbNX7eQ/feedshare-shrink_2048_1536/0/1685725205340?e=1699488000&v=beta&t=N5nKLFgIBtxe0hShUYRA9walnacHnJnIINaKViPJm8Y"
                }
              ],
              "num_appreciations": 12,
              "num_comments": 106,
              "num_empathy": 115,
              "num_interests": 13,
              "num_likes": 3839,
              "num_praises": 161,
              "text": "Mikell Taylor is a principal technical program manager. She led the design of our Proteus mobile robot, Amazon’s first ever autonomous robotic drive that will work alongside employees and help transport carts carrying packages for loading onto trucks for customer delivery.\n\nTye Brady is the chief technologist for Amazon Robotics, where he has been heavily involved in innovations like our new approach to inventory management, called Containerized Storage, which uses robots to deliver products to employees in a more ergonomically friendly manner.\n\nWe’re so proud of both of them for being named top tech leaders by Boston Globe Media. Thanks for all that you do to drive innovation for employees and help improve the customer experience! https://lnkd.in/eucdXyZn",
              "time": "4mo",
              "url": "https://www.linkedin.com/posts/amazon_mikell-taylor-is-a-principal-technical-program-activity-7070443976637440000-e7IG",
              "urn": "7070443976637440000"
            }
          ],
          "message": "ok",
          "paging": {
            "count": 50,
            "paginationToken": "1152111763-1696392222753-4d3f8c47faec693e86a967677436a51e",
            "start": 0,
            "total": 300
          }
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Company by Domain
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-by-domain') and
            i.nice_name == "Get Company by Domain")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "confident_score": "100%",
          "data": {
            "company_id": "162479",
            "company_name": "Apple",
            "description": "We’re a diverse collective of thinkers and doers, continually reimagining what’s possible to help us all do what we love in new ways. And the same innovation that goes into our products also applies to our practices — strengthening our commitment to leave the world better than we found it. This is where your work can make a difference in people’s lives. Including your own.\n\nApple is an equal opportunity employer that is committed to inclusion and diversity. Visit apple.com/careers to learn more.",
            "domain": "apple.com",
            "email": "",
            "employee_count": 164144,
            "employee_range": "10000+",
            "follower_count": 17438946,
            "hq_address_line1": "1 Apple Park Way",
            "hq_address_line2": "",
            "hq_city": "Cupertino",
            "hq_country": "US",
            "hq_full_address": "1 Apple Park Way, Cupertino, California 95014, US",
            "hq_postalcode": "95014",
            "hq_region": "California",
            "industries": [
              "Computers and Electronics Manufacturing"
            ],
            "linkedin_url": "https://www.linkedin.com/company/apple",
            "locations": [
              {
                "city": "Cupertino",
                "country": "US",
                "full_address": "1 Apple Park Way, Cupertino, California 95014, US",
                "is_headquarter": true,
                "line1": "1 Apple Park Way",
                "line2": "",
                "region": "California",
                "zipcode": "95014"
              }
            ],
            "logo_url": "https://media.licdn.com/dms/image/C560BAQHdAaarsO-eyA/company-logo_400_400/0/1630637844948/apple_logo?e=1714003200&v=beta&t=yo0bibg5ZTPni_eUF6txGFxIapSRi7Gc3epnx_YhJyE",
            "phone": null,
            "specialties": "Innovative Product Development, World-Class Operations, Retail, Telephone Support",
            "tagline": "",
            "type": "Public Company",
            "website": "http://www.apple.com/careers",
            "year_founded": 1976
          },
          "message": "ok"
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Company by ID
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-by-id') and
            i.nice_name == "Get Company by ID")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "company_id": "162479",
            "company_name": "Apple",
            "description": "We’re a diverse collective of thinkers and doers, continually reimagining what’s possible to help us all do what we love in new ways. And the same innovation that goes into our products also applies to our practices — strengthening our commitment to leave the world better than we found it. This is where your work can make a difference in people’s lives. Including your own.\n\nApple is an equal opportunity employer that is committed to inclusion and diversity. Visit apple.com/careers to learn more.",
            "domain": "apple.com",
            "email": "",
            "employee_count": 169883,
            "employee_range": "10000+",
            "follower_count": 17562442,
            "funding_info": {
              "crunchbase_url": "https://www.crunchbase.com/organization/apple",
              "last_funding_round_amount": null,
              "last_funding_round_currency": null,
              "last_funding_round_month": 4,
              "last_funding_round_type": "POST_IPO_EQUITY",
              "last_funding_round_year": 2021,
              "num_funding_rounds": 7
            },
            "hq_address_line1": "1 Apple Park Way",
            "hq_address_line2": "",
            "hq_city": "Cupertino",
            "hq_country": "US",
            "hq_full_address": "1 Apple Park Way, Cupertino, California 95014, US",
            "hq_postalcode": "95014",
            "hq_region": "California",
            "industries": [
              "Computers and Electronics Manufacturing"
            ],
            "linkedin_url": "https://www.linkedin.com/company/apple",
            "locations": [
              {
                "city": "Cupertino",
                "country": "US",
                "full_address": "1 Apple Park Way, Cupertino, California 95014, US",
                "is_headquarter": true,
                "line1": "1 Apple Park Way",
                "line2": "",
                "region": "California",
                "zipcode": "95014"
              }
            ],
            "logo_url": "https://media.licdn.com/dms/image/C560BAQHdAaarsO-eyA/company-logo_400_400/0/1630637844948/apple_logo?e=1722470400&v=beta&t=xtCgKrPu0EkhO9strsErAr1GW0daOdc-cUZ2fXRAdYY",
            "phone": null,
            "specialties": "Innovative Product Development, World-Class Operations, Retail, Telephone Support",
            "tagline": "",
            "type": "Public Company",
            "website": "http://www.apple.com/careers",
            "year_founded": 1976
          },
          "message": "ok"
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Find Custom Headcount
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/find-custom-headcount') and
            i.nice_name == "Find Custom Headcount")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "headcount": 2146
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Company Jobs Count
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-jobs-count') and
            i.nice_name == "Get Company Jobs Count")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "jobs_count": 3764
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Crunchbase Details
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-company-details-from-crunchbase') and
            i.nice_name == "Get Crunchbase Details")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "about": "Kinly is a diverse financial technology company dedicated to meeting the specific needs of African-Americans and their allies.",
            "acquired_by": {
              "name": "Greenwood Bank",
              "url": "https://crunchbase.com/organization/greenwood-bank"
            },
            "actively_hiring": false,
            "cb_rank": 21268,
            "company_type": "For Profit",
            "contact_email": "support@bekinly.com",
            "crunchbase_url": "https://www.crunchbase.com/organization/kinly-c638",
            "description": "Kinly is a diverse financial technology company dedicated to meeting the specific needs of African-Americans and their allies.",
            "employee_range": "1-10",
            "facebook": "https://www.facebook.com/kinlyofficial/",
            "founded": 2020,
            "founders": [
              "https://crunchbase.com/person/donald-hawkins"
            ],
            "funding_raised": 20000000,
            "funding_raised_currency": "$",
            "funding_rounds": [
              {
                "currency": "$",
                "date": "Jun 13, 2022",
                "funding_raised": 15000000,
                "funding_type": "Series A",
                "number_investors": 7
              },
              {
                "currency": "$",
                "date": "Jan 1, 2021",
                "funding_raised": 5000000,
                "funding_type": "Seed",
                "number_investors": null
              }
            ],
            "headquarter_location": "Greater Atlanta Area, East Coast, Southern US",
            "industries": "Financial Services, FinTech",
            "ipo_status": "Private",
            "last_funding_type": "Series A",
            "latest_funding_date": "Jun 13, 2022",
            "legal_name": "",
            "linkedin": "https://www.linkedin.com/company/kinlyofficial/",
            "location": "Atlanta, Georgia, United States",
            "number_of_exits": "",
            "number_of_funding_round": 2,
            "operating_status": "Active",
            "organization": "Kinly",
            "phone_number": "(833) 332-4323",
            "stock_ticker": "",
            "twitter": "https://twitter.com/kinlyofficial",
            "website": "https://bekinly.com/"
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Search Employees
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/search-employees') and
            i.nice_name == "Search Employees")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        import requests
        import csv
        import time
        from math import ceil

        #change the value to your api key
        API_KEY = "YOUR_API_KEY"
        host = "fresh-linkedin-profile-data.p.rapidapi.com"

        #Search requirements
        #100 employees are working at Apple
        search_url = "https://fresh-linkedin-profile-data.p.rapidapi.com/search-employees"
        search_payload = {
            "current_company_ids": [162479],
            "limit": 100
        }
        search_headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": host
        }

        #Check Search requirements
        check_url = "https://fresh-linkedin-profile-data.p.rapidapi.com/check-search-status"
        check_headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": host
        }

        #Get Result requirements
        get_result_url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-search-results"
        get_result_headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": host
        }

        data_fields = ["linkedin_url","first_name","last_name","full_name","location","headline","about","company","job_title","company_domain"]

        #Init a search employees request, check status and get result when done
        def full_search_employees():
            #Init search
            search_response = requests.post(search_url, json=search_payload, headers=search_headers)
            if search_response.status_code == 200:
                request_id = search_response.json().get('request_id')
            else:
                print(search_response.json().get('message'))
                quit()

            done = False
            data = []

            #Check
            while not done:
                # check search status every 5 minutes
                time.sleep(300)
                check_response = requests.get(check_url, headers=check_headers, params={'request_id': request_id})

                if check_response.status_code == 200 and check_response.json().get('status') == 'done':
                    #Done
                    total_scraped = check_response.json().get('total_employees')
                    total_result_pages = ceil(total_scraped/100)

                    #Get all results
                    for page in range(1,total_result_pages+1):
                        querystring = {'request_id': request_id, 'page':page}
                        get_result_response = requests.get(get_result_url, headers=get_result_headers, params=querystring)
                        if get_result_response.status_code == 200:
                            for rs in get_result_response.json().get('data'):
                                dict_info = {}
                                for f in data_fields:
                                    dict_info[f] = rs.get(f)
                                data.append(dict_info)
                else:
                    #Not done
                    continue

                #save
                filename = "result.csv"

                with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=data_fields)
                    writer.writeheader()
                    writer.writerows(data)

                #finish
                done = True


        if __name__ == '__main__':
            full_search_employees()
        """,
            ),
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "message": "Use this request_id to check your search with 'Check Search Status' endpoint",
          "request_id": "0bb8360c779317e5f6fc1722a8bd26a1"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Check Search Status
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/check-search-status') and
            i.nice_name == "Check Search Status")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "message": "Found 1/1 employees. Please use 'Get Search Results' endpoint to get your data!",
          "status": "done"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Search Results
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-search-results') and
            i.nice_name == "Get Search Results")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": [
            {
              "about": "J’ai été pendant plusieurs années chef d’entreprise et obtenu plusieurs trophées dont le meilleur commerce de France catégorie communication et marketing\nPar cette expérience je suis polyvalente dans les domaines vente management et événementiel",
              "city": "Cannes",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 11,
              "current_company_join_year": 2018,
              "educations": [
                {
                  "activities": "",
                  "date_range": "",
                  "degree": "Licence",
                  "description": "",
                  "eduId": 547419995,
                  "end_month": "",
                  "end_year": "",
                  "field_of_study": "Langue et littérature françaises",
                  "grade": "",
                  "school": "Faculté Lille 3 ",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": ""
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 11,
                  "current_company_join_year": 2018,
                  "date_range": "Nov 2018 - present",
                  "description": "",
                  "duration": "5 yrs 7 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Cannes, Provence-Alpes-Côte d’Azur, France",
                  "start_month": 11,
                  "start_year": 2018,
                  "title": "Directrice boutique Personal Shopper Digital France Présidente Association Cannes Centre Commerces"
                },
                {
                  "company": "Neo Retro Agency (Cabaret & Burlesque show)",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "2010 - present",
                  "description": "",
                  "duration": "14 yrs 5 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Région de Nice, France",
                  "start_month": "",
                  "start_year": 2010,
                  "title": "Danseuse"
                },
                {
                  "company": "Tara Jarmon Officiel",
                  "company_id": "1176564",
                  "company_linkedin_url": "https://www.linkedin.com/company/1176564",
                  "company_public_url": null,
                  "date_range": "Sep 2015 - Nov 2018",
                  "description": "",
                  "duration": "3 yrs 3 mos",
                  "end_month": 11,
                  "end_year": 2018,
                  "is_current": false,
                  "location": "Cannes",
                  "start_month": 9,
                  "start_year": 2015,
                  "title": "Directrice de boutique"
                },
                {
                  "company": "SANDRO",
                  "company_id": "674473",
                  "company_linkedin_url": "https://www.linkedin.com/company/674473",
                  "company_public_url": null,
                  "date_range": "Jul 2013 - Sep 2015",
                  "description": "",
                  "duration": "2 yrs 3 mos",
                  "end_month": 9,
                  "end_year": 2015,
                  "is_current": false,
                  "location": "Région de Cannes, France",
                  "start_month": 7,
                  "start_year": 2013,
                  "title": "Directrice de boutique"
                },
                {
                  "company": "Le Danielli",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Feb 2008 - Feb 2014",
                  "description": "",
                  "duration": "6 yrs",
                  "end_month": 2,
                  "end_year": 2014,
                  "is_current": false,
                  "location": "Grasse",
                  "start_month": 2,
                  "start_year": 2008,
                  "title": "Gerante"
                },
                {
                  "company": "Pooh Pooh Bee Doo",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Mar 2010 - Sep 2013",
                  "description": "3 trophées\nÉlu meilleur Commerce de France en 2011 en catégorie Communication et Marketing\nÉlu meilleur commerce de la PACA dans l'activité de la vie locale en 2012\nTalent des cité en 2013",
                  "duration": "3 yrs 7 mos",
                  "end_month": 9,
                  "end_year": 2013,
                  "is_current": false,
                  "location": "Grasse",
                  "start_month": 3,
                  "start_year": 2010,
                  "title": "Gerante"
                },
                {
                  "company": "Tara Jarmon",
                  "company_id": "1176564",
                  "company_linkedin_url": "https://www.linkedin.com/company/1176564",
                  "company_public_url": null,
                  "date_range": "Feb 2007 - Apr 2008",
                  "description": "",
                  "duration": "1 yr 3 mos",
                  "end_month": 4,
                  "end_year": 2008,
                  "is_current": false,
                  "location": "Région de Paris, France",
                  "start_month": 2,
                  "start_year": 2007,
                  "title": "Directrice de boutique"
                },
                {
                  "company": "Prada",
                  "company_id": "8666",
                  "company_linkedin_url": "https://www.linkedin.com/company/8666",
                  "company_public_url": null,
                  "date_range": "Sep 2003 - 2007",
                  "description": "",
                  "duration": "3 yrs 5 mos",
                  "end_month": "",
                  "end_year": 2007,
                  "is_current": false,
                  "location": "Région de Paris, France",
                  "start_month": 9,
                  "start_year": 2003,
                  "title": "Vendeuse"
                },
                {
                  "company": "LANCEL",
                  "company_id": "26964",
                  "company_linkedin_url": "https://www.linkedin.com/company/26964",
                  "company_public_url": null,
                  "date_range": "Feb 2000 - Sep 2003",
                  "description": "",
                  "duration": "3 yrs 8 mos",
                  "end_month": 9,
                  "end_year": 2003,
                  "is_current": false,
                  "location": "Paris 09, Île-de-France, France",
                  "start_month": 2,
                  "start_year": 2000,
                  "title": "Vendeuse"
                }
              ],
              "first_name": "Alexia",
              "full_name": "Alexia Routier",
              "headline": "Store Manager",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Directrice boutique Personal Shopper Digital France Présidente Association Cannes Centre Commerces",
              "last_name": "Routier",
              "linkedin_url": "https://www.linkedin.com/in/alexia-routier-84664655",
              "location": "Cannes, Provence-Alpes-Côte d'Azur, France",
              "profile_id": "195676470",
              "profile_image_url": "https://media.licdn.com/dms/image/D4E03AQHeh1xigFT1VA/profile-displayphoto-shrink_800_800/0/1701297276331?e=1720051200&v=beta&t=Z5vw7i859jxbKw6_gH0EdAAmozkmNwpI50TROqs-nqQ",
              "public_id": "alexia-routier-84664655",
              "school": "Faculté Lille 3 ",
              "state": "Provence-Alpes-Côte d'Azur"
            },
            {
              "about": "•\t15 années d’expérience en industrie Textile et Lingerie, dont 8 années en Chine\n•\tExpérience variée en développement matieres et produits, innovations, sourcing, accompagnement fournisseurs, achats, collection, management et gestion de projets\n•\tHabilité à communiquer en Anglais (bilingue), Portugais (bilingue), et Chinois (intermédiaire)\n•\tPragmatique, dynamique, esprit d’analyse et force de propositions, sens produit, habilité à gérer un projet dans un environnement multiculturel\n•\tVolonté de m’inscrire dans une industrie Textile durable et Mode Luxe",
              "city": "Lille",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 8,
              "current_company_join_year": 2020,
              "educations": [
                {
                  "activities": "",
                  "date_range": "",
                  "degree": "MASTER",
                  "description": "",
                  "eduId": 46181852,
                  "end_month": "",
                  "end_year": "",
                  "field_of_study": "SCIENCES DE GESTION",
                  "grade": "",
                  "school": "IAE Lille",
                  "school_id": "1607828",
                  "school_linkedin_url": "https://www.linkedin.com/company/1607828/",
                  "start_month": "",
                  "start_year": ""
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 8,
                  "current_company_join_year": 2020,
                  "date_range": "Aug 2020 - present",
                  "description": "",
                  "duration": "3 yrs 10 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 8,
                  "start_year": 2020,
                  "title": "RESPONSABLE ACHATS, RECHERCHE ET DÉVELOPPEMENT"
                },
                {
                  "company": "Etam",
                  "company_id": "15180046",
                  "company_linkedin_url": "https://www.linkedin.com/company/15180046",
                  "company_public_url": null,
                  "date_range": "Mar 2020 - Jun 2020",
                  "description": "",
                  "duration": "4 mos",
                  "end_month": 6,
                  "end_year": 2020,
                  "is_current": false,
                  "location": "Lille, Hauts-de-France, France",
                  "start_month": 3,
                  "start_year": 2020,
                  "title": "CHEF DE PROJETS ACHATS ET PRODUCTION - nouvelle marque groupe Etam"
                },
                {
                  "company": "Jules",
                  "company_id": "117912",
                  "company_linkedin_url": "https://www.linkedin.com/company/117912",
                  "company_public_url": null,
                  "date_range": "Sep 2016 - Feb 2020",
                  "description": "",
                  "duration": "3 yrs 6 mos",
                  "end_month": 2,
                  "end_year": 2020,
                  "is_current": false,
                  "location": "Lille, Hauts-de-France, France",
                  "start_month": 9,
                  "start_year": 2016,
                  "title": "CHEF DE MARCHE ACCESSOIRES"
                },
                {
                  "company": "Etam",
                  "company_id": "15180046",
                  "company_linkedin_url": "https://www.linkedin.com/company/15180046",
                  "company_public_url": null,
                  "date_range": "May 2010 - May 2016",
                  "description": "",
                  "duration": "6 yrs",
                  "end_month": 5,
                  "end_year": 2016,
                  "is_current": false,
                  "location": "Shanghai City, China",
                  "start_month": 5,
                  "start_year": 2010,
                  "title": "RESPONSABLE DEVELOPPEMENT INNOVATION SOURCING MATIERES ET PRODUITS "
                }
              ],
              "first_name": "Natalina",
              "full_name": "Natalina Rodrigues",
              "headline": "RESPONSABLE ACHATS, RECHERCHE ET DEVELOPPEMENTS, INNOVATION chez AUBADE Paris",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "RESPONSABLE ACHATS, RECHERCHE ET DÉVELOPPEMENT",
              "last_name": "Rodrigues",
              "linkedin_url": "https://www.linkedin.com/in/natalina-rodrigues-704a10b",
              "location": "Greater Lille Metropolitan Area",
              "profile_id": "35355892",
              "profile_image_url": "https://media.licdn.com/dms/image/C4E03AQHKDzU8_lGbYg/profile-displayphoto-shrink_800_800/0/1562099834102?e=1720051200&v=beta&t=eIp6MZvoPQdpDIavFC0A9TEr9rzaq4ZhrYgIHOOZ2S4",
              "public_id": "natalina-rodrigues-704a10b",
              "school": "IAE Lille",
              "state": ""
            },
            {
              "about": "",
              "city": "Malakoff",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 1,
              "current_company_join_year": 2011,
              "educations": [
                {
                  "activities": "",
                  "date_range": "Sep 2001 - Jun 2003",
                  "degree": "Master",
                  "description": "",
                  "eduId": 842132593,
                  "end_month": 6,
                  "end_year": 2003,
                  "field_of_study": "Commerce international / commerce",
                  "grade": "",
                  "school": "ISEG",
                  "school_id": "15129497",
                  "school_linkedin_url": "https://www.linkedin.com/company/15129497/",
                  "start_month": 9,
                  "start_year": 2001
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 1,
                  "current_company_join_year": 2011,
                  "date_range": "Jan 2016 - present",
                  "description": "Membre du Codir.\nManagement du réseau de boutiques en France et à l’International et des corners en Grands Magasins : 150 points de vente. \nAnalyse et développement du chiffre d’affaires, suivi financier, suivi budgétaire et P&L.\nManagement d’une équipe siège de 14 personnes (dont 6 Directeurs Régionaux) et en N+2 d’une force de vente d’environ 300 collaborateurs.\nNégociation commerciale avec les Grands Magasins.\nApprovisionnement des points de vente : budgets d’achats, sélection des mises en place, suivi des taux de revente et des réassorts, gestion et optimisation des stocks, prévisions d’achat.\nMarketing Retail : planning commercial, opérations spécifiques sur les points de vente, évènementiel, vitrines, merchandising.\nOmnicanilité et CRM : mise en place et suivi des outils (clienteling, Eréservation, shop to central…)\nElaboration et mise en place de la stratégie de développement en France et à l’étranger : recherche d’emplacement, négociation, élaboration projet & prévisionnel, plan d’aménagement,\nsuivi de travaux et gestion des ouvertures et des fermetures des boutiques. \nParticipation à l’élaboration des collections.",
                  "duration": "8 yrs 5 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 1,
                  "start_year": 2016,
                  "title": "Retail Director "
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "date_range": "Jan 2013 - Jan 2016",
                  "description": "Négociation commerciale",
                  "duration": "3 yrs",
                  "end_month": 1,
                  "end_year": 2016,
                  "is_current": false,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 1,
                  "start_year": 2013,
                  "title": "Directrice Grands Comptes France et Belgique "
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "date_range": "Jan 2011 - Jan 2013",
                  "description": "Management des 80 corners en France & en Belgique",
                  "duration": "2 yrs",
                  "end_month": 1,
                  "end_year": 2013,
                  "is_current": false,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 1,
                  "start_year": 2011,
                  "title": "Directrice régionale"
                },
                {
                  "company": "VF Lingerie (France) SA - Marque Lou ",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Nov 2009 - Dec 2010",
                  "description": "Garantir l'atteinte des objectifs de chiffre d’affaires de 60 points de vente \nGestion des budgets de frais de personnel, de frais généraux et de démarque inconnue.\nConcevoir et suivre des plans d'action de développement ou de redressement du chiffre d'affaires. \nVeiller à l'adéquation des stocks selon les besoins des stands. \nAssurer l'interface avec les services supports du siège et construire des plans d'action concertés.",
                  "duration": "1 yr 2 mos",
                  "end_month": 12,
                  "end_year": 2010,
                  "is_current": false,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 11,
                  "start_year": 2009,
                  "title": "Directrice régionale"
                },
                {
                  "company": "TWS - fashionshopping.com ",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Jun 2006 - Jun 2009",
                  "description": "",
                  "duration": "3 yrs",
                  "end_month": 6,
                  "end_year": 2009,
                  "is_current": false,
                  "location": "Saint-Denis, Île-de-France, France",
                  "start_month": 6,
                  "start_year": 2006,
                  "title": "Responsable e-commerce"
                },
                {
                  "company": "Printemps",
                  "company_id": "15658",
                  "company_linkedin_url": "https://www.linkedin.com/company/15658",
                  "company_public_url": null,
                  "date_range": "Feb 2003 - Jun 2006",
                  "description": "",
                  "duration": "3 yrs 5 mos",
                  "end_month": 6,
                  "end_year": 2006,
                  "is_current": false,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 2,
                  "start_year": 2003,
                  "title": "Manager des Ventes "
                }
              ],
              "first_name": "Aline",
              "full_name": "Aline BEBON (LOURDAIS)",
              "headline": "Retail Director chez Aubade Paris",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Retail Director ",
              "last_name": "BEBON",
              "linkedin_url": "https://www.linkedin.com/in/aline-bebon-lourdais-280857256",
              "location": "Malakoff, Île-de-France, France",
              "profile_id": "1059145152",
              "profile_image_url": "https://media.licdn.com/dms/image/D4D03AQEswt_INtu7ZQ/profile-displayphoto-shrink_800_800/0/1668464496610?e=1720051200&v=beta&t=E2QrPJPnoLdRUUzUICewPhbIIii1mRjxVvwfhVsrV4A",
              "public_id": "aline-bebon-lourdais-280857256",
              "school": "ISEG",
              "state": "Île-de-France"
            },
            {
              "about": "Mon parcours se résume en quelques mots:\n l envie d apprendre, de se dépasser, le goût du challenge que je transmets aujourd'hui...passionner par le produit et ce lien exceptionnel que l on peut tisser avec chacune de nos clientes me porte tous les jours un peu plus...\nJ ai évolué avec de belles marques et de\n belles personnes...\nMon maître mot et ma devise au quotidien : \nPERSÉVÉRANCE !!!💪",
              "city": "Lyon",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 1,
              "current_company_join_year": 2019,
              "educations": [
                {
                  "activities": "",
                  "date_range": "",
                  "degree": "",
                  "description": "",
                  "eduId": 583242617,
                  "end_month": "",
                  "end_year": "",
                  "field_of_study": "",
                  "grade": "",
                  "school": "lycée les chassagnes",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": ""
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 1,
                  "current_company_join_year": 2019,
                  "date_range": "Jan 2019 - present",
                  "description": "",
                  "duration": "5 yrs 5 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "",
                  "start_month": 1,
                  "start_year": 2019,
                  "title": "Responsable boutique"
                },
                {
                  "company": "SIMONE PERELE SAS",
                  "company_id": "156503",
                  "company_linkedin_url": "https://www.linkedin.com/company/156503",
                  "company_public_url": null,
                  "date_range": "Jul 2016 - Jan 2019",
                  "description": "responsable corner  Simone perele & implicite",
                  "duration": "2 yrs 7 mos",
                  "end_month": 1,
                  "end_year": 2019,
                  "is_current": false,
                  "location": "Région de Lyon, France",
                  "start_month": 7,
                  "start_year": 2016,
                  "title": "Responsable corner "
                },
                {
                  "company": "RougeGorge Lingerie",
                  "company_id": "1424760",
                  "company_linkedin_url": "https://www.linkedin.com/company/1424760",
                  "company_public_url": null,
                  "date_range": "Sep 2010 - Jul 2016",
                  "description": "",
                  "duration": "5 yrs 11 mos",
                  "end_month": 7,
                  "end_year": 2016,
                  "is_current": false,
                  "location": "Région de Lyon, France",
                  "start_month": 9,
                  "start_year": 2010,
                  "title": "Responsable adjoint"
                },
                {
                  "company": "Etam",
                  "company_id": "15180046",
                  "company_linkedin_url": "https://www.linkedin.com/company/15180046",
                  "company_public_url": null,
                  "date_range": "Sep 2007 - Sep 2010",
                  "description": "",
                  "duration": "3 yrs",
                  "end_month": 9,
                  "end_year": 2010,
                  "is_current": false,
                  "location": "Région de Lyon, France",
                  "start_month": 9,
                  "start_year": 2007,
                  "title": "Conseillère de vente"
                }
              ],
              "first_name": "laura",
              "full_name": "laura mezaber",
              "headline": "Responsable boutique Aubade 💖              ",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Responsable boutique",
              "last_name": "mezaber",
              "linkedin_url": "https://www.linkedin.com/in/laura-mezaber-3a82b695",
              "location": "Greater Lyon Area",
              "profile_id": "338152880",
              "profile_image_url": "https://media.licdn.com/dms/image/C4E03AQFIujxAXD0rcA/profile-displayphoto-shrink_800_800/0/1516785190764?e=1720051200&v=beta&t=ppHEeKopceryoLKk59CGaAzkhX_Mpe-GgGM0P36D91A",
              "public_id": "laura-mezaber-3a82b695",
              "school": "lycée les chassagnes",
              "state": ""
            },
            {
              "about": "",
              "city": "Sainte-Geneviève-des-Bois",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 9,
              "current_company_join_year": 2021,
              "educations": [
                {
                  "activities": "",
                  "date_range": "2016 - 2018",
                  "degree": "Master de Marketing et de la Communication dans le luxe",
                  "description": "",
                  "eduId": 329135076,
                  "end_month": "",
                  "end_year": 2018,
                  "field_of_study": "Marketing / Communication / Commerce",
                  "grade": "",
                  "school": "EIML Paris",
                  "school_id": "15098430",
                  "school_linkedin_url": "https://www.linkedin.com/company/15098430/",
                  "start_month": "",
                  "start_year": 2016
                },
                {
                  "activities": "",
                  "date_range": "2013 - 2016",
                  "degree": "Licence Economie Gestion",
                  "description": "",
                  "eduId": 332618808,
                  "end_month": "",
                  "end_year": 2016,
                  "field_of_study": "macroéconomie, microéconomie",
                  "grade": "",
                  "school": "Université Paris Ouest Nanterre La Défense",
                  "school_id": "352250",
                  "school_linkedin_url": "https://www.linkedin.com/company/352250/",
                  "start_month": "",
                  "start_year": 2013
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 9,
                  "current_company_join_year": 2021,
                  "date_range": "Dec 2022 - present",
                  "description": "",
                  "duration": "1 yr 6 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 12,
                  "start_year": 2022,
                  "title": "Gestionnaire des approvisionnements et achats Grands Magasins"
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "date_range": "Sep 2021 - Feb 2023",
                  "description": "",
                  "duration": "1 yr 6 mos",
                  "end_month": 2,
                  "end_year": 2023,
                  "is_current": false,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 9,
                  "start_year": 2021,
                  "title": "Responsable de magasin"
                },
                {
                  "company": "Princesse tam.tam",
                  "company_id": "129447",
                  "company_linkedin_url": "https://www.linkedin.com/company/129447",
                  "company_public_url": null,
                  "date_range": "Jan 2019 - Nov 2021",
                  "description": "",
                  "duration": "2 yrs 11 mos",
                  "end_month": 11,
                  "end_year": 2021,
                  "is_current": false,
                  "location": "Région de Paris, France",
                  "start_month": 1,
                  "start_year": 2019,
                  "title": "Responsable adjointe itinérante"
                },
                {
                  "company": "Un Jour Ailleurs",
                  "company_id": "3203564",
                  "company_linkedin_url": "https://www.linkedin.com/company/3203564",
                  "company_public_url": null,
                  "date_range": "May 2018 - Jan 2019",
                  "description": "",
                  "duration": "9 mos",
                  "end_month": 1,
                  "end_year": 2019,
                  "is_current": false,
                  "location": "Paris 16, Île-de-France, France",
                  "start_month": 5,
                  "start_year": 2018,
                  "title": "Responsable Adjointe de Magasin"
                },
                {
                  "company": "Lancel",
                  "company_id": "26964",
                  "company_linkedin_url": "https://www.linkedin.com/company/26964",
                  "company_public_url": null,
                  "date_range": "Jun 2016 - May 2018",
                  "description": "- Accueil de la clientèle dans l’univers de la Maison, présentation des collections et du savoir-faire, Cérémonial de vente\n- Fidélisation, remerciement client, invitation clients à des événements boutiques\n- Gestion des stocks et de la livraison\n- Gestion du CRM, mise à jour de la base de données Clienteling\n- Gestion du merchandising \n- Gestion du service après vente et des litiges\n- Reportings et analyse des KPI's \n- Respect des objectifs mensuels",
                  "duration": "2 yrs",
                  "end_month": 5,
                  "end_year": 2018,
                  "is_current": false,
                  "location": "Vélizy-Villacoublay, Île-de-France, France",
                  "start_month": 6,
                  "start_year": 2016,
                  "title": "Conseillère de vente - Retail"
                },
                {
                  "company": "DECATHLON FRANCE",
                  "company_id": "6150",
                  "company_linkedin_url": "https://www.linkedin.com/company/6150",
                  "company_public_url": null,
                  "date_range": "Jun 2015 - Aug 2015",
                  "description": "Conseil auprès de la clientèle, accompagnement client.\nGestion des stocks et réception des produits\nGestion du merchandising\nGestion de la caisse",
                  "duration": "3 mos",
                  "end_month": 8,
                  "end_year": 2015,
                  "is_current": false,
                  "location": "Vélizy 2",
                  "start_month": 6,
                  "start_year": 2015,
                  "title": "Conseillère de vente - Retail"
                }
              ],
              "first_name": "ELSA",
              "full_name": "ELSA LESESTRE",
              "headline": "Gestionnaire des approvisionnements et achats Grands Magasins",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Gestionnaire des approvisionnements et achats Grands Magasins",
              "last_name": "LESESTRE",
              "linkedin_url": "https://www.linkedin.com/in/elsalesestre",
              "location": "Sainte-Geneviève-des-Bois, Île-de-France, France",
              "profile_id": "480310079",
              "profile_image_url": "https://media.licdn.com/dms/image/D4E03AQGo3dkXMxjG6A/profile-displayphoto-shrink_800_800/0/1676380603872?e=1720051200&v=beta&t=bnBw_Np4gaBlQc3bu4ehAb0GVsp6j-keBLdpberGnps",
              "public_id": "elsalesestre",
              "school": "EIML Paris",
              "state": "Île-de-France"
            },
            {
              "about": "Créer un échange avec le client, le mettre en confiance et l'amener à déterminer ses besoins et ses désirs. ",
              "city": "Lyon",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 8,
              "current_company_join_year": 2018,
              "educations": [
                {
                  "activities": "",
                  "date_range": "",
                  "degree": "Licence",
                  "description": "",
                  "eduId": 264798181,
                  "end_month": "",
                  "end_year": "",
                  "field_of_study": "LANGUES ET CIVILISATIONS ETRANGERES",
                  "grade": "",
                  "school": "Université Jean Monnet Saint-Etienne",
                  "school_id": "15093530",
                  "school_linkedin_url": "https://www.linkedin.com/company/15093530/",
                  "start_month": "",
                  "start_year": ""
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 8,
                  "current_company_join_year": 2018,
                  "date_range": "Aug 2018 - present",
                  "description": "",
                  "duration": "5 yrs 10 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "lyon",
                  "start_month": 8,
                  "start_year": 2018,
                  "title": "Démonstratrice corner "
                },
                {
                  "company": "Les Georgettes by Altesse",
                  "company_id": "15196146",
                  "company_linkedin_url": "https://www.linkedin.com/company/15196146",
                  "company_public_url": null,
                  "date_range": "Dec 2017 - Dec 2018",
                  "description": "",
                  "duration": "1 yr",
                  "end_month": 12,
                  "end_year": 2018,
                  "is_current": false,
                  "location": "lyon",
                  "start_month": 12,
                  "start_year": 2017,
                  "title": "conseillère de vente"
                },
                {
                  "company": "Galeries Lafayette",
                  "company_id": "13258",
                  "company_linkedin_url": "https://www.linkedin.com/company/13258",
                  "company_public_url": null,
                  "date_range": "Dec 2016 - Sep 2017",
                  "description": "différents contrats en cdd sur les secreurs bijouterie, confection femme, lingerie et saison du bain.",
                  "duration": "10 mos",
                  "end_month": 9,
                  "end_year": 2017,
                  "is_current": false,
                  "location": "Lyon, Rhône-Alpes, France",
                  "start_month": 12,
                  "start_year": 2016,
                  "title": "conseillère de vente"
                },
                {
                  "company": "CHRISTINE LAURE",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Sep 2012 - Apr 2015",
                  "description": "Vente conseil dans un but de fidélisation et développement du CA. Réalisation des objectifs. Merchandising et réalisation des vitrines",
                  "duration": "2 yrs 8 mos",
                  "end_month": 4,
                  "end_year": 2015,
                  "is_current": false,
                  "location": "Région de Lyon, France",
                  "start_month": 9,
                  "start_year": 2012,
                  "title": "CONSEILLERE DE VENTE"
                },
                {
                  "company": "UN JOUR AILLEURS",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Feb 2012 - Sep 2012",
                  "description": "vente selon le protocole de la marque, encaissement, vitrines",
                  "duration": "8 mos",
                  "end_month": 9,
                  "end_year": 2012,
                  "is_current": false,
                  "location": "Région de Lyon, France",
                  "start_month": 2,
                  "start_year": 2012,
                  "title": "Conseillère de vente"
                },
                {
                  "company": "playtex",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Sep 1994 - Apr 2008",
                  "description": "autonome sur un corner au sein des Galeries Lafayette. Gestion des stocks, réception de la marchandise, merchandising, réalisation des objectifs.",
                  "duration": "13 yrs 8 mos",
                  "end_month": 4,
                  "end_year": 2008,
                  "is_current": false,
                  "location": "",
                  "start_month": 9,
                  "start_year": 1994,
                  "title": "démonstratrice"
                }
              ],
              "first_name": "laetitia",
              "full_name": "laetitia pedrini",
              "headline": "Démonstratrice chez Aubade Paris",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Démonstratrice corner ",
              "last_name": "pedrini",
              "linkedin_url": "https://www.linkedin.com/in/laetitia-pedrini-a6b3652b",
              "location": "Lyon, Auvergne-Rhône-Alpes, France",
              "profile_id": "105390515",
              "profile_image_url": "https://media.licdn.com/dms/image/C5603AQHkq_ch4PxwQQ/profile-displayphoto-shrink_800_800/0/1639471404171?e=1720051200&v=beta&t=HnCMJ4EBoKtNyact4IjxYKGPdh4X_LIBalA_9nB7NEI",
              "public_id": "laetitia-pedrini-a6b3652b",
              "school": "Université Jean Monnet Saint-Etienne",
              "state": "Auvergne-Rhône-Alpes"
            },
            {
              "about": "",
              "city": "Le Vésinet",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 1,
              "current_company_join_year": 2022,
              "educations": [],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 1,
                  "current_company_join_year": 2022,
                  "date_range": "Jan 2022 - present",
                  "description": "",
                  "duration": "2 yrs 5 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Paris, France",
                  "start_month": 1,
                  "start_year": 2022,
                  "title": "Directrice E-Commerce & Service Clients"
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Jan 2012 - Dec 2021",
                  "description": "",
                  "duration": "10 yrs",
                  "end_month": 12,
                  "end_year": 2021,
                  "is_current": false,
                  "location": "",
                  "start_month": 1,
                  "start_year": 2012,
                  "title": "Secrétaire  Générale"
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Oct 2006 - Dec 2011",
                  "description": "",
                  "duration": "5 yrs 3 mos",
                  "end_month": 12,
                  "end_year": 2011,
                  "is_current": false,
                  "location": "",
                  "start_month": 10,
                  "start_year": 2006,
                  "title": "Directrice Administration des Ventes"
                },
                {
                  "company": "Manuel Canovas",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Oct 2003 - Oct 2006",
                  "description": "",
                  "duration": "3 yrs",
                  "end_month": 10,
                  "end_year": 2006,
                  "is_current": false,
                  "location": "",
                  "start_month": 10,
                  "start_year": 2003,
                  "title": "Responsable Export"
                },
                {
                  "company": "ITC (Groupe Vanderschooten)",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Apr 1993 - Oct 2003",
                  "description": "",
                  "duration": "10 yrs 7 mos",
                  "end_month": 10,
                  "end_year": 2003,
                  "is_current": false,
                  "location": "Paris",
                  "start_month": 4,
                  "start_year": 1993,
                  "title": "Responsable Export et ADV Export"
                },
                {
                  "company": "C3I",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Apr 1989 - Mar 1993",
                  "description": "",
                  "duration": "4 yrs",
                  "end_month": 3,
                  "end_year": 1993,
                  "is_current": false,
                  "location": "Paris",
                  "start_month": 4,
                  "start_year": 1989,
                  "title": "Commerciale Export"
                }
              ],
              "first_name": "Cornelia",
              "full_name": "Cornelia Aubert-Kiesling",
              "headline": "Directrice E-Commerce & Service Clients chez Aubade Paris",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Directrice E-Commerce & Service Clients",
              "last_name": "Aubert-Kiesling",
              "linkedin_url": "https://www.linkedin.com/in/cornelia-aubert-kiesling-54059358",
              "location": "Le Vésinet, Île-de-France, France",
              "profile_id": "204483648",
              "profile_image_url": "https://media.licdn.com/dms/image/D4E03AQHyAQg-psZLPA/profile-displayphoto-shrink_800_800/0/1674939831105?e=1720051200&v=beta&t=eXr2m44Kpc5BCbLt5EpXt-JUlttJM_JgyOfw86Fq8Vc",
              "public_id": "cornelia-aubert-kiesling-54059358",
              "school": "",
              "state": "Île-de-France"
            },
            {
              "about": "",
              "city": "Paris",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 6,
              "current_company_join_year": 2002,
              "educations": [
                {
                  "activities": "",
                  "date_range": "1989 - 1990",
                  "degree": "European Business Certificate",
                  "description": "",
                  "eduId": 111811856,
                  "end_month": "",
                  "end_year": 1990,
                  "field_of_study": "Buyer & Consumer Behaviour / Marketing",
                  "grade": "",
                  "school": "London South Bank University",
                  "school_id": "12252",
                  "school_linkedin_url": "https://www.linkedin.com/company/12252/",
                  "start_month": "",
                  "start_year": 1989
                },
                {
                  "activities": "",
                  "date_range": "1986 - 1989",
                  "degree": "Diplôme de l'ESCE",
                  "description": "",
                  "eduId": 111811550,
                  "end_month": "",
                  "end_year": 1989,
                  "field_of_study": "Gestion d'entreprise et commerce international",
                  "grade": "",
                  "school": "ESCE International Business School",
                  "school_id": "1746730",
                  "school_linkedin_url": "https://www.linkedin.com/company/1746730/",
                  "start_month": "",
                  "start_year": 1986
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 6,
                  "current_company_join_year": 2002,
                  "date_range": "Jan 2008 - present",
                  "description": ">Management opérationnel et coordination des activités de Demand Planning, Planification industrielle, approvisionnements composant/Production interne et des sous-traitants / Logistique (flux d'approche/douane/distribution/gestion des retours)/ Facturation/Bureau d' Etudes et Industrialisation (développement produits)-Costing / RSE\n\n>Gestion de projet :\nDélocalisation de la totalité des activités industrielles (magasin composants/coupe/méthodes/production)\nMise en place du PLM Centric \nOptimisation de la consommation des matières \nRéorganisation totale de l'implantation d'un site logistique\nMise en place de la suite Next (CEGID) pour la gestion du Demand planning, la planification industrielle, les achats matière et les lancements en production",
                  "duration": "16 yrs 5 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Région de Paris, France",
                  "start_month": 1,
                  "start_year": 2008,
                  "title": "Directeur des Opérations et Supply chain"
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "date_range": "Jan 2005 - Dec 2007",
                  "description": "Mise en place de la planification des Activités opérationnelles (master planning) et du développement produit.\nGain de 2 semaines sur les leadtimes en production, baisse des stocks produits finis de 20% par un accroissement de la fiabilité de la chaîne de procurement.",
                  "duration": "3 yrs",
                  "end_month": 12,
                  "end_year": 2007,
                  "is_current": false,
                  "location": "",
                  "start_month": 1,
                  "start_year": 2005,
                  "title": "Directeur Supply Chain"
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "date_range": "Jun 2002 - Dec 2004",
                  "description": "Mise en place du \"Demand Planning\" : Processus, intervenants, indicateurs d'extrapolation des commandes, segmentation des clients par comportement d'achat, courbe de vie des produits.",
                  "duration": "2 yrs 7 mos",
                  "end_month": 12,
                  "end_year": 2004,
                  "is_current": false,
                  "location": "",
                  "start_month": 6,
                  "start_year": 2002,
                  "title": "Responsable Demand"
                },
                {
                  "company": "Brandt",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Jan 1995 - May 2002",
                  "description": "",
                  "duration": "7 yrs 5 mos",
                  "end_month": 5,
                  "end_year": 2002,
                  "is_current": false,
                  "location": "IdF",
                  "start_month": 1,
                  "start_year": 1995,
                  "title": "Responsable Approvisionnements et Prévisions de ventes"
                }
              ],
              "first_name": "Annie",
              "full_name": "Annie B.",
              "headline": "Directeur des Opérations et Supply Chain",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Directeur des Opérations et Supply chain",
              "last_name": "B.",
              "linkedin_url": "https://www.linkedin.com/in/annie-b-039a6023",
              "location": "Greater Paris Metropolitan Region",
              "profile_id": "83234349",
              "profile_image_url": "https://media.licdn.com/dms/image/C4E03AQHUBOrRj6bCOw/profile-displayphoto-shrink_800_800/0/1611859952513?e=1720051200&v=beta&t=-tA7cF74ljNfTy2F438B9g20fkas5_wPfYCjFrgDKxc",
              "public_id": "annie-b-039a6023",
              "school": "London South Bank University",
              "state": "Paris"
            },
            {
              "about": "",
              "city": "Paris",
              "company": "Aubade Paris",
              "company_domain": "",
              "company_employee_range": null,
              "company_id": "",
              "company_industry": null,
              "company_linkedin_url": "",
              "company_logo_url": null,
              "company_website": null,
              "company_year_founded": null,
              "country": "France",
              "current_company_join_month": 10,
              "current_company_join_year": 2011,
              "educations": [
                {
                  "activities": "",
                  "date_range": "",
                  "degree": "BTS IMS",
                  "description": "",
                  "eduId": 218361833,
                  "end_month": "",
                  "end_year": "",
                  "field_of_study": "",
                  "grade": "",
                  "school": "Elisa Lemonnier",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": ""
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "current_company_join_month": 10,
                  "current_company_join_year": 2011,
                  "date_range": "Oct 2011 - present",
                  "description": "",
                  "duration": "12 yrs 8 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "",
                  "start_month": 10,
                  "start_year": 2011,
                  "title": "Modéliste lingerie"
                }
              ],
              "first_name": "Sandrine",
              "full_name": "Sandrine Valentim",
              "headline": "Modéliste lingerie chez Aubade Paris",
              "hq_city": null,
              "hq_country": null,
              "hq_region": null,
              "job_title": "Modéliste lingerie",
              "last_name": "Valentim",
              "linkedin_url": "https://www.linkedin.com/in/sandrine-valentim-4a4ab395",
              "location": "Greater Paris Metropolitan Region",
              "profile_id": "340138492",
              "profile_image_url": "",
              "public_id": "sandrine-valentim-4a4ab395",
              "school": "Elisa Lemonnier",
              "state": "Paris"
            },
            {
              "about": "Périmètre : Retail, FO France/export et Grands Magasins en fermes et conditions/consignations France, Belgique, Suisse, Danemark (160 points de vente). \nÉlaboration des référencements  par canal de distribution et module de magasin. \nMise en place des commandes d'implantation et besoins pour les opérations commerciales dans le respect des budgets d'achat. \nPilotage des stocks. \nGestion des propositions de réassort. \nAnalyse des ventes, stocks, taux d'écoulement, taux de défilement, slow moving et ajustement seuil d'approvisionnement, afin d'atteindre les objectifs de taux de retour. \n\nOrganisation séminaire :  Défilé, ateliers, présentation technique des collections, O.D.J....\nSupport à la force de vente. \nSuivi de la bonne exécution des contrats cadres. \nSuivi budgets service. \nMise à jour des tableaux de bord.\nResponsable d'une équipe de 4 personnes.",
              "city": "Paris",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 7,
              "current_company_join_year": 2000,
              "educations": [
                {
                  "activities": "",
                  "date_range": "2001 - 2002",
                  "degree": "Diploma in European Business studies",
                  "description": "",
                  "eduId": 213648303,
                  "end_month": "",
                  "end_year": 2002,
                  "field_of_study": "",
                  "grade": "",
                  "school": "The University of Sheffield",
                  "school_id": "8421",
                  "school_linkedin_url": "https://www.linkedin.com/company/8421/",
                  "start_month": "",
                  "start_year": 2001
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 7,
                  "current_company_join_year": 2000,
                  "date_range": "Nov 2015 - present",
                  "description": "",
                  "duration": "8 yrs 7 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Région de Paris, France",
                  "start_month": 11,
                  "start_year": 2015,
                  "title": "Responsable Achats et Approvisionnements Retail et Grands-Magasins"
                },
                {
                  "company": "AUBADE",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "date_range": "Jul 2000 - Oct 2015",
                  "description": "",
                  "duration": "15 yrs 4 mos",
                  "end_month": 10,
                  "end_year": 2015,
                  "is_current": false,
                  "location": "",
                  "start_month": 7,
                  "start_year": 2000,
                  "title": "Gestionnaire Approvisionnement"
                },
                {
                  "company": "DELTA FRANCE",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Feb 1995 - Feb 2000",
                  "description": "",
                  "duration": "5 yrs",
                  "end_month": 2,
                  "end_year": 2000,
                  "is_current": false,
                  "location": "Gonesse",
                  "start_month": 2,
                  "start_year": 1995,
                  "title": "Assisante chef de produits"
                }
              ],
              "first_name": "Céline",
              "full_name": "Céline Robin",
              "headline": "Responsable Achats et Approvisionnements Retail et Grands-Magasins chez Aubade Paris",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Responsable Achats et Approvisionnements Retail et Grands-Magasins",
              "last_name": "Robin",
              "linkedin_url": "https://www.linkedin.com/in/c%C3%A9line-robin-93573782",
              "location": "Greater Paris Metropolitan Region",
              "profile_id": "294443897",
              "profile_image_url": "https://media.licdn.com/dms/image/D4E03AQEqoxQme_VQog/profile-displayphoto-shrink_800_800/0/1703534017344?e=1720051200&v=beta&t=F7DTEUl4OBURsbQ3HCv0plZskrBG7qF6U9Z_opp67Do",
              "public_id": "c%C3%A9line-robin-93573782",
              "school": "The University of Sheffield",
              "state": "Paris"
            },
            {
              "about": "",
              "city": "Paris",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 1,
              "current_company_join_year": 2023,
              "educations": [
                {
                  "activities": "",
                  "date_range": "",
                  "degree": "Master of Fashion Business",
                  "description": "",
                  "eduId": 833553932,
                  "end_month": "",
                  "end_year": "",
                  "field_of_study": "Marketing",
                  "grade": "",
                  "school": "MODART International",
                  "school_id": "2337224",
                  "school_linkedin_url": "https://www.linkedin.com/company/2337224/",
                  "start_month": "",
                  "start_year": ""
                }
              ],
              "experiences": [
                {
                  "company": "BrandAlley",
                  "company_id": "98393",
                  "company_linkedin_url": "https://www.linkedin.com/company/98393",
                  "company_public_url": null,
                  "date_range": "Sep 2023 - present",
                  "description": "",
                  "duration": "9 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Paris, France",
                  "start_month": 9,
                  "start_year": 2023,
                  "title": "Acheteuse junior"
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 1,
                  "current_company_join_year": 2023,
                  "date_range": "Jan 2023 - present",
                  "description": "",
                  "duration": "1 yr 5 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Paris, France",
                  "start_month": 1,
                  "start_year": 2023,
                  "title": "Gestionnaire E-Commerce"
                }
              ],
              "first_name": "Elise",
              "full_name": "Elise Laloy",
              "headline": "Master Marketing de la mode à Mod'Art International",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Gestionnaire E-Commerce",
              "last_name": "Laloy",
              "linkedin_url": "https://www.linkedin.com/in/elise-laloy-54a7591a7",
              "location": "Paris, Île-de-France, France",
              "profile_id": "811063498",
              "profile_image_url": "",
              "public_id": "elise-laloy-54a7591a7",
              "school": "MODART International",
              "state": "Île-de-France"
            },
            {
              "about": "",
              "city": "Metz",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 4,
              "current_company_join_year": 2023,
              "educations": [
                {
                  "activities": "",
                  "date_range": "Sep 2021 - May 2022",
                  "degree": "Certification",
                  "description": "",
                  "eduId": 750029032,
                  "end_month": 5,
                  "end_year": 2022,
                  "field_of_study": "Management d'unité marchande",
                  "grade": "",
                  "school": "AFPA",
                  "school_id": "21430",
                  "school_linkedin_url": "https://www.linkedin.com/company/21430/",
                  "start_month": 9,
                  "start_year": 2021
                },
                {
                  "activities": "",
                  "date_range": "",
                  "degree": "Baccalauréat professionnel gestion administration",
                  "description": "",
                  "eduId": 677377599,
                  "end_month": "",
                  "end_year": "",
                  "field_of_study": "",
                  "grade": "",
                  "school": "Ste Chrétienne- Metz",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": ""
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 4,
                  "current_company_join_year": 2023,
                  "date_range": "Apr 2023 - present",
                  "description": "",
                  "duration": "1 yr 2 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Metz, Grand Est, France",
                  "start_month": 4,
                  "start_year": 2023,
                  "title": "Responsable de magasin"
                },
                {
                  "company": "Pandora",
                  "company_id": "232381",
                  "company_linkedin_url": "https://www.linkedin.com/company/232381",
                  "company_public_url": null,
                  "date_range": "Nov 2022 - Mar 2023",
                  "description": "",
                  "duration": "5 mos",
                  "end_month": 3,
                  "end_year": 2023,
                  "is_current": false,
                  "location": "Thionville, Grand Est, France",
                  "start_month": 11,
                  "start_year": 2022,
                  "title": "Store Manager "
                },
                {
                  "company": "LA HALLE",
                  "company_id": "133458",
                  "company_linkedin_url": "https://www.linkedin.com/company/133458",
                  "company_public_url": null,
                  "date_range": "Aug 2022 - Nov 2022",
                  "description": "",
                  "duration": "4 mos",
                  "end_month": 11,
                  "end_year": 2022,
                  "is_current": false,
                  "location": "Terville, Grand Est, France",
                  "start_month": 8,
                  "start_year": 2022,
                  "title": "Directrice de magasin"
                },
                {
                  "company": "LA HALLE",
                  "company_id": "133458",
                  "company_linkedin_url": "https://www.linkedin.com/company/133458",
                  "company_public_url": null,
                  "date_range": "Mar 2022 - Mar 2022",
                  "description": "",
                  "duration": "1 mo",
                  "end_month": 3,
                  "end_year": 2022,
                  "is_current": false,
                  "location": "Semécourt ",
                  "start_month": 3,
                  "start_year": 2022,
                  "title": "Directrice de magasin"
                },
                {
                  "company": "Stokomani",
                  "company_id": "9957270",
                  "company_linkedin_url": "https://www.linkedin.com/company/9957270",
                  "company_public_url": null,
                  "date_range": "Jan 2022 - Feb 2022",
                  "description": "",
                  "duration": "2 mos",
                  "end_month": 2,
                  "end_year": 2022,
                  "is_current": false,
                  "location": "Semécourt",
                  "start_month": 1,
                  "start_year": 2022,
                  "title": "Directrice de magasin"
                },
                {
                  "company": "ORCHESTRA-PREMAMAN",
                  "company_id": "10849543",
                  "company_linkedin_url": "https://www.linkedin.com/company/10849543",
                  "company_public_url": null,
                  "date_range": "Nov 2021 - Dec 2021",
                  "description": "",
                  "duration": "2 mos",
                  "end_month": 12,
                  "end_year": 2021,
                  "is_current": false,
                  "location": "Semécourt",
                  "start_month": 11,
                  "start_year": 2021,
                  "title": "Adjoint de direction "
                },
                {
                  "company": "Edora Bijoux",
                  "company_id": "72554657",
                  "company_linkedin_url": "https://www.linkedin.com/company/72554657",
                  "company_public_url": null,
                  "date_range": "Dec 2020 - Dec 2020",
                  "description": "",
                  "duration": "1 mo",
                  "end_month": 12,
                  "end_year": 2020,
                  "is_current": false,
                  "location": "Metz, Grand Est, France",
                  "start_month": 12,
                  "start_year": 2020,
                  "title": "Vendeuse"
                },
                {
                  "company": "Sud express",
                  "company_id": "1456688",
                  "company_linkedin_url": "https://www.linkedin.com/company/1456688",
                  "company_public_url": null,
                  "date_range": "Aug 2008 - Aug 2020",
                  "description": "",
                  "duration": "12 yrs",
                  "end_month": 8,
                  "end_year": 2020,
                  "is_current": false,
                  "location": "Talange, Grand Est, France",
                  "start_month": 8,
                  "start_year": 2008,
                  "title": "Responsable de magasin"
                },
                {
                  "company": "Bleu Cerise",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Jul 2004 - Jun 2008",
                  "description": "",
                  "duration": "4 yrs",
                  "end_month": 6,
                  "end_year": 2008,
                  "is_current": false,
                  "location": "Mondelange, Grand Est, France",
                  "start_month": 7,
                  "start_year": 2004,
                  "title": "Responsable de magasin"
                },
                {
                  "company": "Agatha Paris",
                  "company_id": "18424472",
                  "company_linkedin_url": "https://www.linkedin.com/company/18424472",
                  "company_public_url": null,
                  "date_range": "Mar 2000 - Jun 2004",
                  "description": "",
                  "duration": "4 yrs 4 mos",
                  "end_month": 6,
                  "end_year": 2004,
                  "is_current": false,
                  "location": "Semécourt",
                  "start_month": 3,
                  "start_year": 2000,
                  "title": "Vendeuse"
                },
                {
                  "company": "Boutique Marlene",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Oct 1994 - Mar 2000",
                  "description": "",
                  "duration": "5 yrs 6 mos",
                  "end_month": 3,
                  "end_year": 2000,
                  "is_current": false,
                  "location": "Hagondange, Grand Est, France",
                  "start_month": 10,
                  "start_year": 1994,
                  "title": "Responsable de magasin"
                },
                {
                  "company": "SYM",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Oct 1990 - Oct 1994",
                  "description": "",
                  "duration": "4 yrs",
                  "end_month": 10,
                  "end_year": 1994,
                  "is_current": false,
                  "location": "Semécourt",
                  "start_month": 10,
                  "start_year": 1990,
                  "title": "Vendeuse"
                }
              ],
              "first_name": "Sandrine",
              "full_name": "Sandrine Muratori",
              "headline": "Store Manager chez Aubade Paris",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Responsable de magasin",
              "last_name": "Muratori",
              "linkedin_url": "https://www.linkedin.com/in/sandrine-muratori-3760b51b4",
              "location": "Metz, Grand Est, France",
              "profile_id": "836312778",
              "profile_image_url": "",
              "public_id": "sandrine-muratori-3760b51b4",
              "school": "AFPA",
              "state": "Grand Est"
            },
            {
              "about": "",
              "city": "Anglet",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 9,
              "current_company_join_year": 2023,
              "educations": [
                {
                  "activities": "",
                  "date_range": "2020 - 2020",
                  "degree": "Reussir sa mission de formateur terrain ",
                  "description": "",
                  "eduId": 656615578,
                  "end_month": "",
                  "end_year": 2020,
                  "field_of_study": "",
                  "grade": "",
                  "school": "Formation Alain Renault Communication",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": 2020
                },
                {
                  "activities": "",
                  "date_range": "2019 - 2019",
                  "degree": "Les Fondamentaux du Management",
                  "description": "",
                  "eduId": 653813563,
                  "end_month": "",
                  "end_year": 2019,
                  "field_of_study": "",
                  "grade": "",
                  "school": "Formation Interne Entreprise",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": 2019
                },
                {
                  "activities": "",
                  "date_range": "2017 - 2017",
                  "degree": "Législation du travail",
                  "description": "",
                  "eduId": 653814441,
                  "end_month": "",
                  "end_year": 2017,
                  "field_of_study": "",
                  "grade": "",
                  "school": "Formation Interne Entreprise",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": 2017
                },
                {
                  "activities": "",
                  "date_range": "2015 - 2015",
                  "degree": "Pilotage des performances d’un point de vente",
                  "description": "",
                  "eduId": 653815221,
                  "end_month": "",
                  "end_year": 2015,
                  "field_of_study": "",
                  "grade": "",
                  "school": "Formation Interne entreprise",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": 2015
                },
                {
                  "activities": "",
                  "date_range": "2011 - 2012",
                  "degree": "Licence professionnelle",
                  "description": "",
                  "eduId": 653808965,
                  "end_month": "",
                  "end_year": 2012,
                  "field_of_study": "Dermo-cosmétique",
                  "grade": "",
                  "school": "Université Paul Sabatier Toulouse III",
                  "school_id": "15250261",
                  "school_linkedin_url": "https://www.linkedin.com/company/15250261/",
                  "start_month": "",
                  "start_year": 2011
                },
                {
                  "activities": "",
                  "date_range": "2009 - 2011",
                  "degree": "BTS Esthétique et Cosmétique",
                  "description": "",
                  "eduId": 653811026,
                  "end_month": "",
                  "end_year": 2011,
                  "field_of_study": "",
                  "grade": "",
                  "school": "École Joffre Esthétique ",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": 2009
                },
                {
                  "activities": "",
                  "date_range": "2009 - 2009",
                  "degree": "Baccalauréat scientifique",
                  "description": "",
                  "eduId": 653818523,
                  "end_month": "",
                  "end_year": 2009,
                  "field_of_study": "",
                  "grade": "",
                  "school": "Lycée Gaston Fébus",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": 2009
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 9,
                  "current_company_join_year": 2023,
                  "date_range": "Sep 2023 - present",
                  "description": "",
                  "duration": "9 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Bayonne, Nouvelle-Aquitaine, France",
                  "start_month": 9,
                  "start_year": 2023,
                  "title": "Responsable de magasin"
                },
                {
                  "company": "ApriL Beauty ",
                  "company_id": "5306535",
                  "company_linkedin_url": "https://www.linkedin.com/company/5306535",
                  "company_public_url": null,
                  "date_range": "Oct 2021 - May 2022",
                  "description": "",
                  "duration": "8 mos",
                  "end_month": 5,
                  "end_year": 2022,
                  "is_current": false,
                  "location": "Anglet, Nouvelle-Aquitaine, France",
                  "start_month": 10,
                  "start_year": 2021,
                  "title": "Directrice opérationnelle"
                },
                {
                  "company": "NOCIBE",
                  "company_id": "118440",
                  "company_linkedin_url": "https://www.linkedin.com/company/118440",
                  "company_public_url": null,
                  "date_range": "Feb 2019 - Nov 2021",
                  "description": "J’assure la direction et le développement, d’un grand magasin avec institut, en centre commercial.\nJe manage une équipe de 11 collaborateurs, je suis responsable de la mise en place et du suivi des stratégies commerciales, et marketings de l’entreprise.\n\nMes missions:\nRecruter, former, accompagner et manager les collaborateurs\nDévelopper des services de différenciation, et programme de fidélisation \nFixer, animer et contrôler les objectifs individuels et collectifs des collaborateurs\nVeiller à l’application des procédures de sécurité entreprise\nMise en application et animation de stratégies commerciales\nRéalisation d’études statistiques\nAnalyse, interprétation des résultats objectivisés\nParticipe au développement logistique de commande digitale sur point de vente\nVeille à l’amélioration de l’expérience client, score eNPS\nDévelopper un support de formation \nGestion administrative et logistique ",
                  "duration": "2 yrs 10 mos",
                  "end_month": 11,
                  "end_year": 2021,
                  "is_current": false,
                  "location": "Anglet, Nouvelle-Aquitaine, France",
                  "start_month": 2,
                  "start_year": 2019,
                  "title": "Directrice opérationnelle"
                },
                {
                  "company": "NOCIBE",
                  "company_id": "118440",
                  "company_linkedin_url": "https://www.linkedin.com/company/118440",
                  "company_public_url": null,
                  "date_range": "Nov 2015 - Feb 2019",
                  "description": "Responsable polyvalente des opérations entreprise\nManagement de 4 collaborateurs\n",
                  "duration": "3 yrs 4 mos",
                  "end_month": 2,
                  "end_year": 2019,
                  "is_current": false,
                  "location": "Bayonne, Nouvelle-Aquitaine, France",
                  "start_month": 11,
                  "start_year": 2015,
                  "title": "Responsable opérationnelle"
                },
                {
                  "company": "NOCIBE",
                  "company_id": "118440",
                  "company_linkedin_url": "https://www.linkedin.com/company/118440",
                  "company_public_url": null,
                  "date_range": "Oct 2013 - Nov 2015",
                  "description": "",
                  "duration": "2 yrs 2 mos",
                  "end_month": 11,
                  "end_year": 2015,
                  "is_current": false,
                  "location": "Bayonne, Nouvelle-Aquitaine, France",
                  "start_month": 10,
                  "start_year": 2013,
                  "title": "Responsable adjointe"
                },
                {
                  "company": "Parashop",
                  "company_id": "1950676",
                  "company_linkedin_url": "https://www.linkedin.com/company/1950676",
                  "company_public_url": null,
                  "date_range": "Dec 2012 - Jun 2013",
                  "description": "",
                  "duration": "7 mos",
                  "end_month": 6,
                  "end_year": 2013,
                  "is_current": false,
                  "location": "Toulouse, Occitanie, France",
                  "start_month": 12,
                  "start_year": 2012,
                  "title": "Conseillère de vente"
                }
              ],
              "first_name": "Alice",
              "full_name": "Alice Amalfitano",
              "headline": "Directrice Opérationnelle ",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Responsable de magasin",
              "last_name": "Amalfitano",
              "linkedin_url": "https://www.linkedin.com/in/alice-amalfitano-a230701a9",
              "location": "Anglet, Nouvelle-Aquitaine, France",
              "profile_id": "815320251",
              "profile_image_url": "https://media.licdn.com/dms/image/C4E03AQFE_vHcExULsQ/profile-displayphoto-shrink_800_800/0/1662722571249?e=1720051200&v=beta&t=SGt-AopjGsTE_70XZOumqBLh2Lbk6FDQMSbaXsfr7_o",
              "public_id": "alice-amalfitano-a230701a9",
              "school": "Formation Alain Renault Communication",
              "state": "Nouvelle-Aquitaine"
            },
            {
              "about": "",
              "city": "Paris",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": null,
              "current_company_join_year": null,
              "educations": [
                {
                  "activities": "",
                  "date_range": "",
                  "degree": "Diplôme d'études supérieures en management, option expertise comptable ",
                  "description": "",
                  "eduId": 828159077,
                  "end_month": "",
                  "end_year": "",
                  "field_of_study": "Économie de gestion",
                  "grade": "",
                  "school": "Université de Toulon",
                  "school_id": "127062",
                  "school_linkedin_url": "https://www.linkedin.com/company/127062/",
                  "start_month": "",
                  "start_year": ""
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": "",
                  "current_company_join_year": "",
                  "date_range": "",
                  "description": "",
                  "duration": "less than one year",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "",
                  "start_month": "",
                  "start_year": "",
                  "title": "Responsable principal chaîne logistique"
                }
              ],
              "first_name": "Magali",
              "full_name": "Magali de VARGAS",
              "headline": "Responsable Supply Chain chez Aubade Paris",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Responsable principal chaîne logistique",
              "last_name": "de",
              "linkedin_url": "https://www.linkedin.com/in/magali-de-vargas-8951a321b",
              "location": "Paris, Île-de-France, France",
              "profile_id": "929103665",
              "profile_image_url": "https://media.licdn.com/dms/image/D4E03AQGl8b-uSBEPHw/profile-displayphoto-shrink_800_800/0/1710781316224?e=1720051200&v=beta&t=BzLaQo-qibkCKo3-0iaB1ffMJdqBCDeymw6CBAkw-qY",
              "public_id": "magali-de-vargas-8951a321b",
              "school": "Université de Toulon",
              "state": "Île-de-France"
            },
            {
              "about": "",
              "city": "Paris",
              "company": "Aubade Paris franchise",
              "company_domain": "",
              "company_employee_range": null,
              "company_id": "",
              "company_industry": null,
              "company_linkedin_url": "",
              "company_logo_url": null,
              "company_website": null,
              "company_year_founded": null,
              "country": "France",
              "current_company_join_month": 10,
              "current_company_join_year": 2007,
              "educations": [],
              "experiences": [
                {
                  "company": "Aubade Paris franchise",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "current_company_join_month": 10,
                  "current_company_join_year": 2007,
                  "date_range": "Oct 2007 - present",
                  "description": "",
                  "duration": "16 yrs 8 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Paris 17, Île-de-France, France",
                  "start_month": 10,
                  "start_year": 2007,
                  "title": "directrice aubade"
                },
                {
                  "company": "Jeux de séduction",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Jun 2004 - Jul 2007",
                  "description": "Boutique de lingerie multimarque ",
                  "duration": "3 yrs 2 mos",
                  "end_month": 7,
                  "end_year": 2007,
                  "is_current": false,
                  "location": "Région de Paris, France",
                  "start_month": 6,
                  "start_year": 2004,
                  "title": "Gérante"
                },
                {
                  "company": "Nespresso product specialist - market manager",
                  "company_id": "1216148",
                  "company_linkedin_url": "https://www.linkedin.com/company/1216148",
                  "company_public_url": null,
                  "date_range": "Jan 2000 - Jun 2004",
                  "description": "",
                  "duration": "4 yrs 6 mos",
                  "end_month": 6,
                  "end_year": 2004,
                  "is_current": false,
                  "location": "Région de Paris , France",
                  "start_month": 1,
                  "start_year": 2000,
                  "title": "Assistant commercial"
                }
              ],
              "first_name": "laurence",
              "full_name": "laurence hudelot",
              "headline": "directrice aubade chez Aubade Courcelles Paris ",
              "hq_city": null,
              "hq_country": null,
              "hq_region": null,
              "job_title": "directrice aubade",
              "last_name": "hudelot",
              "linkedin_url": "https://www.linkedin.com/in/laurence-hudelot-a7985b11b",
              "location": "Paris, Île-de-France, France",
              "profile_id": "500774205",
              "profile_image_url": "https://media.licdn.com/dms/image/D4E03AQH-MhTcbfIf6Q/profile-displayphoto-shrink_800_800/0/1687330455682?e=1720051200&v=beta&t=YvpRn46LU-o-XNQN429jAc67nag8A4aRKC3CeaZrJWc",
              "public_id": "laurence-hudelot-a7985b11b",
              "school": "",
              "state": "Île-de-France"
            },
            {
              "about": "Après une mission de transition de 3 mois, j'ai rejoint les équipes Aubade au poste de DSI.\nFier d'avoir rejoint cette belle marque française et le groupe Calida.",
              "city": "Paris",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 8,
              "current_company_join_year": 2021,
              "educations": [
                {
                  "activities": "",
                  "date_range": "1992 - 1995",
                  "degree": "Diplôme d'ingénieur",
                  "description": "",
                  "eduId": 540727110,
                  "end_month": "",
                  "end_year": 1995,
                  "field_of_study": "Ingénierie des télécommunications",
                  "grade": "",
                  "school": "ESIGETEL - École Supérieure d'Ingénieurs en Informatique et Génie des Télécommunications",
                  "school_id": "11147032",
                  "school_linkedin_url": "https://www.linkedin.com/company/11147032/",
                  "start_month": "",
                  "start_year": 1992
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 8,
                  "current_company_join_year": 2021,
                  "date_range": "Aug 2021 - present",
                  "description": "",
                  "duration": "2 yrs 10 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 8,
                  "start_year": 2021,
                  "title": "DSI Aubade Paris"
                },
                {
                  "company": "Aubade",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "May 2021 - present",
                  "description": "",
                  "duration": "3 yrs",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 5,
                  "start_year": 2021,
                  "title": "DSI de transition"
                },
                {
                  "company": "Sans E",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Oct 2020 - present",
                  "description": "",
                  "duration": "3 yrs 8 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 10,
                  "start_year": 2020,
                  "title": "En Recherche Active Salarié/ Freelance"
                },
                {
                  "company": "PARASHOP",
                  "company_id": "1950676",
                  "company_linkedin_url": "https://www.linkedin.com/company/1950676",
                  "company_public_url": null,
                  "date_range": "Jul 2011 - Oct 2020",
                  "description": "",
                  "duration": "9 yrs 4 mos",
                  "end_month": 10,
                  "end_year": 2020,
                  "is_current": false,
                  "location": "PARIS",
                  "start_month": 7,
                  "start_year": 2011,
                  "title": "Directeur des Systèmes d'Information"
                },
                {
                  "company": "MIM.",
                  "company_id": "803273",
                  "company_linkedin_url": "https://www.linkedin.com/company/803273",
                  "company_public_url": null,
                  "date_range": "Jun 1996 - Jun 2011",
                  "description": "",
                  "duration": "15 yrs",
                  "end_month": 6,
                  "end_year": 2011,
                  "is_current": false,
                  "location": "",
                  "start_month": 6,
                  "start_year": 1996,
                  "title": "Directeur Informatique"
                },
                {
                  "company": "MIM",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Jun 1996 - Jun 2011",
                  "description": "",
                  "duration": "15 yrs",
                  "end_month": 6,
                  "end_year": 2011,
                  "is_current": false,
                  "location": "Thiais, Île-de-France, France",
                  "start_month": 6,
                  "start_year": 1996,
                  "title": "Directeur informatique"
                }
              ],
              "first_name": "Frédéric",
              "full_name": "Frédéric JOLY",
              "headline": "DSI chez Aubade Paris",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "DSI Aubade Paris",
              "last_name": "JOLY",
              "linkedin_url": "https://www.linkedin.com/in/fr%C3%A9d%C3%A9ric-joly-2baa42b3",
              "location": "Paris, Île-de-France, France",
              "profile_id": "405682990",
              "profile_image_url": "https://media.licdn.com/dms/image/C4E03AQEvM7fs-3kjog/profile-displayphoto-shrink_800_800/0/1517620768337?e=1720051200&v=beta&t=prifJ5dhBaRjjBZOsG9cVaTgqPcCMeTGVT5js9WIr3g",
              "public_id": "fr%C3%A9d%C3%A9ric-joly-2baa42b3",
              "school": "ESIGETEL - École Supérieure d'Ingénieurs en Informatique et Génie des Télécommunications",
              "state": "Île-de-France"
            },
            {
              "about": "",
              "city": "St.-Ouen",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 3,
              "current_company_join_year": 2023,
              "educations": [],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 3,
                  "current_company_join_year": 2023,
                  "date_range": "Mar 2023 - present",
                  "description": "",
                  "duration": "1 yr 3 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "La defense",
                  "start_month": 3,
                  "start_year": 2023,
                  "title": "Conseiller ventes"
                },
                {
                  "company": "La Boutique du Coiffeur",
                  "company_id": "33203919",
                  "company_linkedin_url": "https://www.linkedin.com/company/33203919",
                  "company_public_url": null,
                  "date_range": "Oct 2020 - Mar 2023",
                  "description": "",
                  "duration": "2 yrs 6 mos",
                  "end_month": 3,
                  "end_year": 2023,
                  "is_current": false,
                  "location": "",
                  "start_month": 10,
                  "start_year": 2020,
                  "title": "Conseiller ventes"
                }
              ],
              "first_name": "Emma",
              "full_name": "Emma Leneez",
              "headline": "Conseiller de vente ",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Conseiller ventes",
              "last_name": "Leneez",
              "linkedin_url": "https://www.linkedin.com/in/emma-leneez-44071b21a",
              "location": "St.-Ouen, Île-de-France, France",
              "profile_id": "927437232",
              "profile_image_url": "https://media.licdn.com/dms/image/D4E03AQGXsLTMuY2c-g/profile-displayphoto-shrink_800_800/0/1711853742616?e=1720051200&v=beta&t=R4xgrFgwgKg4lVrwgvdksHhHh-NOe8irnEEXDwebCMc",
              "public_id": "emma-leneez-44071b21a",
              "school": "",
              "state": "Île-de-France"
            },
            {
              "about": "Travaillant depuis plus de 20 ans dans la lingerie féminine (créneau multimarque indépendant), j'apprécie beaucoup le contact et guider \"mes\" clientes sur le meilleur choix au niveau des collections. Profitant d'une notoriété importante concernant la marque Aubade, je développe une grande partie de ma tournée à de la prospection : Développement de la partie balnéaire, mais aussi la lingerie masculine et depuis peu le \"homewear\".\nEtre autonome, organiser mon planning afin qu'il soit le plus \"percutant\" possible, tout en proposant les nombreuses nouveautés au total 22 nouvelles lignes lingerie sur l'année.",
              "city": "La Rochelle",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 11,
              "current_company_join_year": 2018,
              "educations": [
                {
                  "activities": "",
                  "date_range": "2006 - 2008",
                  "degree": "Master 1 (formation continue) \"Objectif Manager\"",
                  "description": "",
                  "eduId": 545028957,
                  "end_month": "",
                  "end_year": 2008,
                  "field_of_study": "Economie, droit du travail, contrôle de gestion, marketing",
                  "grade": "",
                  "school": "NEOMA Business School",
                  "school_id": "3330082",
                  "school_linkedin_url": "https://www.linkedin.com/company/3330082/",
                  "start_month": "",
                  "start_year": 2006
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 11,
                  "current_company_join_year": 2018,
                  "date_range": "Nov 2018 - present",
                  "description": "- Suivi de 90 magasins réseau : multimarques indépendants\n- Présentation des collections (Printemps- Eté / Automne-Hiver)\n- Développement part de marché dont le balnéaire la lingerie masculine\n- Formation vente personnel du magasin\n- Prospections avec l'ouverture de nouveaux points de ventes\n- Formation du personnel (merchandising)",
                  "duration": "5 yrs 7 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Le grand \"grand\" ouest (16,17, 22, 23, 29, 33, 35, 44, 49, 50, 56 ,72, 76, 79, 85, 86)",
                  "start_month": 11,
                  "start_year": 2018,
                  "title": "CHEF DE SECTEUR AUBADE LINGERIE"
                },
                {
                  "company": "BARBARA LINGERIE",
                  "company_id": "26799612",
                  "company_linkedin_url": "https://www.linkedin.com/company/26799612",
                  "company_public_url": null,
                  "date_range": "Jul 2002 - Nov 2018",
                  "description": "- Suivi d'une centaine de magasins indépendants (réseau détail) / CA annuel : 750 k€\n- Suivi de 7 grands magasins (Printemps, Galeries Lafayette)\n- Présentation des collections, formation du personnel\n- Partie importante de mon travail, la prospection\n- 1 er secteur en C.A sur les 5 au niveau national\n- 1 er secteur en ouvertures de nouveaux points de ventes (2016/2017/2018)",
                  "duration": "16 yrs 5 mos",
                  "end_month": 11,
                  "end_year": 2018,
                  "is_current": false,
                  "location": "GRAND OUEST",
                  "start_month": 7,
                  "start_year": 2002,
                  "title": "CHEF DE SECTEUR"
                },
                {
                  "company": "JEAN COUZON",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Jun 1995 - Jun 2002",
                  "description": "",
                  "duration": "7 yrs",
                  "end_month": 6,
                  "end_year": 2002,
                  "is_current": false,
                  "location": "Ile de France",
                  "start_month": 6,
                  "start_year": 1995,
                  "title": "Responsable de secteur"
                },
                {
                  "company": "ROUSSEL stores d'intérieur",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Sep 1989 - Jul 1995",
                  "description": "Pendant un an j'ai été préparateur de commande et suite au retrait de permis d'un commercial sur la normandie j'ai dû le conduire pour assurer ses rdv, 3 mois après je prenais sa place.\nPar la suite je suis devenu \"merchandiser\" pour implanter notre gamme de tringles à rideaux dans les hypermarchés principalement chez Carrefour suite au rachat d'Euromarché par celui-ci.",
                  "duration": "5 yrs 11 mos",
                  "end_month": 7,
                  "end_year": 1995,
                  "is_current": false,
                  "location": "MELUN (77)",
                  "start_month": 9,
                  "start_year": 1989,
                  "title": "MERCHANDISER"
                }
              ],
              "first_name": "Laurent",
              "full_name": "Laurent HUET",
              "headline": "CHEF DE SECTEUR LINGERIE MULTI MARQUE INDEPENDANT",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "CHEF DE SECTEUR AUBADE LINGERIE",
              "last_name": "HUET",
              "linkedin_url": "https://www.linkedin.com/in/laurent-huet-27b2baba",
              "location": "La Rochelle, Nouvelle-Aquitaine, France",
              "profile_id": "424753151",
              "profile_image_url": "https://media.licdn.com/dms/image/D4E03AQHpBD08zjTdYQ/profile-displayphoto-shrink_800_800/0/1710082582344?e=1720051200&v=beta&t=INRt3z-aM0YPNkR9Y1NjuCmDq-HZDp4C0nb042ZeXm4",
              "public_id": "laurent-huet-27b2baba",
              "school": "NEOMA Business School",
              "state": "Nouvelle-Aquitaine"
            },
            {
              "about": "En formation « Administrateur d’Infrastructure Sécurisées » en Alternance chez IMIE Paris.",
              "city": "Drancy",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 10,
              "current_company_join_year": 2023,
              "educations": [
                {
                  "activities": "",
                  "date_range": "Oct 2023 - Sep 2024",
                  "degree": "",
                  "description": "",
                  "eduId": 928653765,
                  "end_month": 9,
                  "end_year": 2024,
                  "field_of_study": "",
                  "grade": "",
                  "school": "IMIE PARIS",
                  "school_id": "25246624",
                  "school_linkedin_url": "https://www.linkedin.com/company/25246624/",
                  "start_month": 10,
                  "start_year": 2023
                },
                {
                  "activities": "",
                  "date_range": "Sep 2022 - Apr 2023",
                  "degree": "Technicien Supérieur en Système et Réseaux",
                  "description": "",
                  "eduId": 843974049,
                  "end_month": 4,
                  "end_year": 2023,
                  "field_of_study": "",
                  "grade": "",
                  "school": "CEFIAC Formation",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": 9,
                  "start_year": 2022
                },
                {
                  "activities": "",
                  "date_range": "Jan 2021 - Mar 2021",
                  "degree": "",
                  "description": "",
                  "eduId": 709068881,
                  "end_month": 3,
                  "end_year": 2021,
                  "field_of_study": "Informatique",
                  "grade": "",
                  "school": "EPIE Formation",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": 1,
                  "start_year": 2021
                },
                {
                  "activities": "",
                  "date_range": "Sep 2020 - Jan 2021",
                  "degree": "",
                  "description": "",
                  "eduId": 710602858,
                  "end_month": 1,
                  "end_year": 2021,
                  "field_of_study": "",
                  "grade": "",
                  "school": "EPIE Formation",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": 9,
                  "start_year": 2020
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 10,
                  "current_company_join_year": 2023,
                  "date_range": "Oct 2023 - present",
                  "description": "",
                  "duration": "8 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "",
                  "start_month": 10,
                  "start_year": 2023,
                  "title": "Administrateur d’infrastructure Sécurisées (en Alternance)"
                },
                {
                  "company": "CEFIAC FORMATION",
                  "company_id": "25627487",
                  "company_linkedin_url": "https://www.linkedin.com/company/25627487",
                  "company_public_url": null,
                  "date_range": "Sep 2022 - Oct 2023",
                  "description": "1) Assister les utilisateurs en centre de services\n- Mettre en service un équipement numérique\n- Assister les utilisateurs sur leurs équipements numériques\n- Gérer les incidents et les problèmes\n- Assister à l'utilisation des ressources collaboratives\n2) Maintenir, exploiter et sécuriser une infrastructure centralisée\n- Maintenir et exploiter le réseau local et la téléphonie\n- Sécuriser les accès à Internet\n- Maintenir et exploiter un environnement virtualisé\n- Maintenir et exploiter un domaine ActiveDirectory et les serveurs Windows\n- Maintenir et exploiter un serveur Linux\n3) Maintenir et exploiter une infrastructure distribuée et contribuer à sa sécurisation\n- Configurer les services de déploiement et de terminaux clients légers\n- Automatiser les tâches à l'aide de scripts\n- Maintenir et sécuriser les accès réseaux distants\n- Superviser l'infrastructure\n- Intervenir dans un environnement de Cloud Computing\n- Assurer sa veille technologique",
                  "duration": "1 yr 2 mos",
                  "end_month": 10,
                  "end_year": 2023,
                  "is_current": false,
                  "location": "Sarcelles, Île-de-France, France",
                  "start_month": 9,
                  "start_year": 2022,
                  "title": "Technicien Supérieur en Système et Réseaux (en formation)"
                },
                {
                  "company": "EPIE Formation",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Jan 2021 - Oct 2021",
                  "description": "",
                  "duration": "10 mos",
                  "end_month": 10,
                  "end_year": 2021,
                  "is_current": false,
                  "location": "Saint-Denis, Île-de-France, France",
                  "start_month": 1,
                  "start_year": 2021,
                  "title": "Actuellement en formation"
                },
                {
                  "company": "EPIE Formation",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Nov 2020 - Dec 2020",
                  "description": "• Installer, entretenir et dépanner des équipements informatiques\n• Démonter et remonter un équipement numérique (Changement de composants)\n• Revalorisation des PC fixe ou mobile\n• Installation Systèmes d’exploitation (Windows XP – 7 – 8 –10)\n• Créer d’un support d’amorçage avec le logiciel (RUFUS)\n• Utilisation d’un logiciel de virtualisation (VMware, Packet Tracer)\n• Audité des ordinateurs\n• Sauvegarder et restaurer un fichier image avec (Acronis true Image)\n• Connecter un équipement en réseau",
                  "duration": "2 mos",
                  "end_month": 12,
                  "end_year": 2020,
                  "is_current": false,
                  "location": "Saint-Denis, Île-de-France, France",
                  "start_month": 11,
                  "start_year": 2020,
                  "title": "Installateur dépanneur en informatique"
                },
                {
                  "company": "GTIE EXPO",
                  "company_id": "26312429",
                  "company_linkedin_url": "https://www.linkedin.com/company/26312429",
                  "company_public_url": null,
                  "date_range": "Sep 2014 - Aug 2016",
                  "description": "Apprenti plombier au Parc des Expositions à Paris-Nord Villepinte. ",
                  "duration": "2 yrs",
                  "end_month": 8,
                  "end_year": 2016,
                  "is_current": false,
                  "location": "Villepinte, Île-de-France, France",
                  "start_month": 9,
                  "start_year": 2014,
                  "title": "Plombier"
                }
              ],
              "first_name": "Kévin",
              "full_name": "Kévin MARTIN",
              "headline": "Administrateur d’Infrastructure Sécurisées (en Alternance) ",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Administrateur d’infrastructure Sécurisées (en Alternance)",
              "last_name": "MARTIN",
              "linkedin_url": "https://www.linkedin.com/in/kevin-martin-it",
              "location": "Drancy, Île-de-France, France",
              "profile_id": "883579100",
              "profile_image_url": "https://media.licdn.com/dms/image/D5603AQEXUcmdQcwC_A/profile-displayphoto-shrink_800_800/0/1670253909592?e=1720051200&v=beta&t=ZmUC1d-3HmBZhsjpqypeaAbCul1eMf_PVwYtcL-elq8",
              "public_id": "kevin-martin-it",
              "school": "IMIE PARIS",
              "state": "Île-de-France"
            },
            {
              "about": "Créative et passionnée par le monde du design et de la mode, j'ai évolué à travers ces univers depuis de nombreuses années.\nJ'ai pu travailler pour de grandes marques de lingerie depuis maintenant 18 ans. Cette expérience me permet de pouvoir suivre la création d'un produit du croquis de la styliste au suivi de production en usine.\nJe suis dynamique, rigoureuse et curieuse des nouvelles technologies.",
              "city": "Paris",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 4,
              "current_company_join_year": 2015,
              "educations": [
                {
                  "activities": "",
                  "date_range": "Sep 2003 - Sep 2005",
                  "degree": "Contrat de qualification en Styliste Modéliste",
                  "description": "",
                  "eduId": 764555852,
                  "end_month": 9,
                  "end_year": 2005,
                  "field_of_study": "Spécialité lingerie et corseterie",
                  "grade": "",
                  "school": "FORMAMOD",
                  "school_id": "9440791",
                  "school_linkedin_url": "https://www.linkedin.com/company/9440791/",
                  "start_month": 9,
                  "start_year": 2003
                },
                {
                  "activities": "",
                  "date_range": "Sep 2001 - Jul 2003",
                  "degree": "Brevet de technicien supérieur (BTS)",
                  "description": "",
                  "eduId": 764555835,
                  "end_month": 7,
                  "end_year": 2003,
                  "field_of_study": "Industrie des matériaux souples option Modéliste Industrielle",
                  "grade": "",
                  "school": "Lycée Le Castel",
                  "school_id": "34942755",
                  "school_linkedin_url": "https://www.linkedin.com/company/34942755/",
                  "start_month": 9,
                  "start_year": 2001
                },
                {
                  "activities": "",
                  "date_range": "Sep 1998 - Jun 2001",
                  "degree": "Baccalauréat littéraire ",
                  "description": "",
                  "eduId": 764556717,
                  "end_month": 6,
                  "end_year": 2001,
                  "field_of_study": "option Art Plastique",
                  "grade": "",
                  "school": "Lycée Pasteur",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": 9,
                  "start_year": 1998
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 4,
                  "current_company_join_year": 2015,
                  "date_range": "Mar 2023 - present",
                  "description": "",
                  "duration": "1 yr 3 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Paris, France",
                  "start_month": 3,
                  "start_year": 2023,
                  "title": "Modéliste balnéaire et lingerie"
                },
                {
                  "company": "BorDesignCreation",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Sep 2022 - present",
                  "description": "",
                  "duration": "1 yr 9 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 9,
                  "start_year": 2022,
                  "title": "Modéliste freelance"
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "date_range": "Apr 2015 - Nov 2021",
                  "description": "- Création du premier prototype, du dessin de la styliste, gradation des produits, mise au point et industrialisation avec le logiciel Modaris V8.\n- Développement d’une coque avec la société Art Martin.\n- En charge du développement de la collection maillot de bain en collaboration avec la styliste et les sous-traitants en sourcing. \n- Réalisation des commentaires en anglais du premier prototype à l’industrialisation.\n- Déplacement en usine pour le suivi des produits dans les usines de Tunisie et de Chine.",
                  "duration": "6 yrs 8 mos",
                  "end_month": 11,
                  "end_year": 2021,
                  "is_current": false,
                  "location": "Paris",
                  "start_month": 4,
                  "start_year": 2015,
                  "title": "Modéliste"
                },
                {
                  "company": "Groupe Chantelle",
                  "company_id": "17928",
                  "company_linkedin_url": "https://www.linkedin.com/company/17928",
                  "company_public_url": null,
                  "date_range": "Mar 2008 - Mar 2015",
                  "description": "- Développement de produits en lingerie et maillots de bain:\n     -> Création du premier prototype à partir du dessin de la styliste\n     -> Gradation des produits \n     -> Mise au point et industrialisation\n- Développement d’une coque à mémoire de forme\n- Déplacement en usine en Tunisie",
                  "duration": "7 yrs",
                  "end_month": 3,
                  "end_year": 2015,
                  "is_current": false,
                  "location": "Cachan, Île-de-France, France",
                  "start_month": 3,
                  "start_year": 2008,
                  "title": "Modéliste"
                },
                {
                  "company": "SOCIETE INTERNATIONALE DE LINGERIE",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Sep 2004 - Mar 2008",
                  "description": "Création du premier prototype puis mise au point et industrialisation des collections de corseterie et de balnéaire. \nPour les licences LACROIX, GALLIANO, KENZO, SONIA RYKIEL & CACHAREL.",
                  "duration": "3 yrs 7 mos",
                  "end_month": 3,
                  "end_year": 2008,
                  "is_current": false,
                  "location": "Vanves",
                  "start_month": 9,
                  "start_year": 2004,
                  "title": "Modéliste junior corseterie & balnéaire"
                }
              ],
              "first_name": "Delphine",
              "full_name": "Delphine Bordy",
              "headline": "Modéliste Sénior en lingerie & balnéaire",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Modéliste balnéaire et lingerie",
              "last_name": "Bordy",
              "linkedin_url": "https://www.linkedin.com/in/delphine-bordy",
              "location": "Paris, Île-de-France, France",
              "profile_id": "291830221",
              "profile_image_url": "https://media.licdn.com/dms/image/C4E03AQGKIErRVaa20Q/profile-displayphoto-shrink_800_800/0/1638986513103?e=1720051200&v=beta&t=Mx4VqH7Vah--BmZbKY7eAKOgUbwI-6s8tb1Ob2mdi1Y",
              "public_id": "delphine-bordy",
              "school": "FORMAMOD",
              "state": "Île-de-France"
            },
            {
              "about": "",
              "city": "Paris",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 4,
              "current_company_join_year": 2017,
              "educations": [],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 4,
                  "current_company_join_year": 2017,
                  "date_range": "Apr 2017 - present",
                  "description": "",
                  "duration": "7 yrs 2 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Région de Paris, France",
                  "start_month": 4,
                  "start_year": 2017,
                  "title": "Responsable régional"
                },
                {
                  "company": "CLEOR",
                  "company_id": "10289927",
                  "company_linkedin_url": "https://www.linkedin.com/company/10289927",
                  "company_public_url": null,
                  "date_range": "2016 - 2017",
                  "description": "",
                  "duration": "1 yr",
                  "end_month": "",
                  "end_year": 2017,
                  "is_current": false,
                  "location": "",
                  "start_month": "",
                  "start_year": 2016,
                  "title": "Directeur régional"
                },
                {
                  "company": "Cleor",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Oct 2014 - 2016",
                  "description": "",
                  "duration": "1 yr 4 mos",
                  "end_month": "",
                  "end_year": 2016,
                  "is_current": false,
                  "location": "",
                  "start_month": 10,
                  "start_year": 2014,
                  "title": "Store Manager"
                },
                {
                  "company": "marithé françois girbaud",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Apr 2010 - 2013",
                  "description": "",
                  "duration": "2 yrs 10 mos",
                  "end_month": "",
                  "end_year": 2013,
                  "is_current": false,
                  "location": "Barcelona",
                  "start_month": 4,
                  "start_year": 2010,
                  "title": "coordinatrice reseau"
                }
              ],
              "first_name": "delphine",
              "full_name": "delphine morizé",
              "headline": "Paris ouest - Normandie ",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Responsable régional",
              "last_name": "morizé",
              "linkedin_url": "https://www.linkedin.com/in/delphine-moriz%C3%A9-52125425",
              "location": "Greater Paris Metropolitan Region",
              "profile_id": "87202537",
              "profile_image_url": "https://media.licdn.com/dms/image/C4D03AQGCNds-aJRMsg/profile-displayphoto-shrink_800_800/0/1517257405581?e=1720051200&v=beta&t=QtQg-Yt2BKPVE8ogP1eqFbyuhfIKOzLDcey5QnkXQfI",
              "public_id": "delphine-moriz%C3%A9-52125425",
              "school": "",
              "state": "Paris"
            },
            {
              "about": "",
              "city": "Clamart",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 9,
              "current_company_join_year": 2016,
              "educations": [
                {
                  "activities": "",
                  "date_range": "1997 - 2000",
                  "degree": "Diplôme d'ingénieur",
                  "description": "",
                  "eduId": 435456166,
                  "end_month": "",
                  "end_year": 2000,
                  "field_of_study": "Ingénieur textile option R&D",
                  "grade": "",
                  "school": "Ecole Supérieur des Industries Textile d'Epinal",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": 1997
                },
                {
                  "activities": "",
                  "date_range": "1995 - 1997",
                  "degree": "Brevet de Technicien Supérieur",
                  "description": "",
                  "eduId": 435457096,
                  "end_month": "",
                  "end_year": 1997,
                  "field_of_study": "Gestion de production ",
                  "grade": "",
                  "school": "lycée Edouard Herriot",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": 1995
                },
                {
                  "activities": "",
                  "date_range": "1995 - 1995",
                  "degree": "Baccalauréat F1 option Bonneterie",
                  "description": "",
                  "eduId": 435455342,
                  "end_month": "",
                  "end_year": 1995,
                  "field_of_study": "Bonneterie ",
                  "grade": "",
                  "school": "Lycée des Lombard à Troyes",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": 1995
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 9,
                  "current_company_join_year": 2016,
                  "date_range": "Sep 2016 - present",
                  "description": "",
                  "duration": "7 yrs 9 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Région de Paris, France",
                  "start_month": 9,
                  "start_year": 2016,
                  "title": "Responsable Innovation et Développement"
                },
                {
                  "company": "Petit Bateau",
                  "company_id": "32754",
                  "company_linkedin_url": "https://www.linkedin.com/company/32754",
                  "company_public_url": null,
                  "date_range": "Nov 2011 - Sep 2016",
                  "description": "",
                  "duration": "4 yrs 11 mos",
                  "end_month": 9,
                  "end_year": 2016,
                  "is_current": false,
                  "location": "Région de Troyes, France",
                  "start_month": 11,
                  "start_year": 2011,
                  "title": "Responsable Innovation et Développement matières"
                },
                {
                  "company": "Petit Bateau",
                  "company_id": "32754",
                  "company_linkedin_url": "https://www.linkedin.com/company/32754",
                  "company_public_url": null,
                  "date_range": "Jan 2011 - Nov 2011",
                  "description": "",
                  "duration": "11 mos",
                  "end_month": 11,
                  "end_year": 2011,
                  "is_current": false,
                  "location": "troyes",
                  "start_month": 1,
                  "start_year": 2011,
                  "title": "Responsable des Laboratiores Qualités supports et filés"
                },
                {
                  "company": "Petit Bateau",
                  "company_id": "32754",
                  "company_linkedin_url": "https://www.linkedin.com/company/32754",
                  "company_public_url": null,
                  "date_range": "May 2010 - Dec 2010",
                  "description": "",
                  "duration": "8 mos",
                  "end_month": 12,
                  "end_year": 2010,
                  "is_current": false,
                  "location": "Région de Troyes, France",
                  "start_month": 5,
                  "start_year": 2010,
                  "title": "Technien Laboratoire Qualité supports et filés"
                },
                {
                  "company": "Middle Sud ",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Nov 2006 - Jan 2010",
                  "description": "",
                  "duration": "3 yrs 3 mos",
                  "end_month": 1,
                  "end_year": 2010,
                  "is_current": false,
                  "location": "Préfecture de Casablanca, Morocco",
                  "start_month": 11,
                  "start_year": 2006,
                  "title": "Responsable Import Matières textiles"
                },
                {
                  "company": "Rapid Pant ( Confection Pantalon Ville)",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Mar 2003 - Sep 2006",
                  "description": "",
                  "duration": "3 yrs 7 mos",
                  "end_month": 9,
                  "end_year": 2006,
                  "is_current": false,
                  "location": "Préfecture de Casablanca, Morocco",
                  "start_month": 3,
                  "start_year": 2003,
                  "title": "Responsable Qualité Produits finis"
                },
                {
                  "company": "Torkay ( Confection Pantalons 5 poches)",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Nov 2001 - Jan 2003",
                  "description": "",
                  "duration": "1 yr 3 mos",
                  "end_month": 1,
                  "end_year": 2003,
                  "is_current": false,
                  "location": "Préfecture de Casablanca, Morocco",
                  "start_month": 11,
                  "start_year": 2001,
                  "title": "Responsable Qualité Produits Finis"
                },
                {
                  "company": "Princesse tam.tam ",
                  "company_id": "129447",
                  "company_linkedin_url": "https://www.linkedin.com/company/129447",
                  "company_public_url": null,
                  "date_range": "Aug 2000 - Oct 2001",
                  "description": "",
                  "duration": "1 yr 3 mos",
                  "end_month": 10,
                  "end_year": 2001,
                  "is_current": false,
                  "location": "Région de Paris, France",
                  "start_month": 8,
                  "start_year": 2000,
                  "title": "Contrôleur qualité"
                }
              ],
              "first_name": "MEHDI",
              "full_name": "MEHDI SAMAHRI",
              "headline": "Responsable Innovation & Développement Produit",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Responsable Innovation et Développement",
              "last_name": "SAMAHRI",
              "linkedin_url": "https://www.linkedin.com/in/mehdi-samahri-92a981146",
              "location": "Clamart, Île-de-France, France",
              "profile_id": "593633266",
              "profile_image_url": "",
              "public_id": "mehdi-samahri-92a981146",
              "school": "Ecole Supérieur des Industries Textile d'Epinal",
              "state": "Île-de-France"
            },
            {
              "about": "",
              "city": "Grenoble",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 9,
              "current_company_join_year": 2018,
              "educations": [],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 9,
                  "current_company_join_year": 2018,
                  "date_range": "Nov 2023 - present",
                  "description": "",
                  "duration": "7 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Grenoble, Auvergne-Rhône-Alpes, France",
                  "start_month": 11,
                  "start_year": 2023,
                  "title": "Démonstratrice"
                },
                {
                  "company": "Claudie Pierlot",
                  "company_id": "9040931",
                  "company_linkedin_url": "https://www.linkedin.com/company/9040931",
                  "company_public_url": null,
                  "date_range": "Jun 2019 - Mar 2022",
                  "description": "",
                  "duration": "2 yrs 10 mos",
                  "end_month": 3,
                  "end_year": 2022,
                  "is_current": false,
                  "location": "Romans-sur-Isère, Auvergne-Rhône-Alpes, France",
                  "start_month": 6,
                  "start_year": 2019,
                  "title": "Conseiller ventes"
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "date_range": "Sep 2018 - Jun 2019",
                  "description": "",
                  "duration": "10 mos",
                  "end_month": 6,
                  "end_year": 2019,
                  "is_current": false,
                  "location": "Romans-sur-Isère, Auvergne-Rhône-Alpes, France",
                  "start_month": 9,
                  "start_year": 2018,
                  "title": "Conseiller ventes"
                }
              ],
              "first_name": "ELISA",
              "full_name": "ELISA MOONS",
              "headline": "Démonstratrice AUBADE PARIS & CALIDA",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Démonstratrice",
              "last_name": "MOONS",
              "linkedin_url": "https://www.linkedin.com/in/elisa-moons-a79962292",
              "location": "Grenoble, Auvergne-Rhône-Alpes, France",
              "profile_id": "1190790525",
              "profile_image_url": "https://media.licdn.com/dms/image/D4E03AQGRcRzkzCf-mA/profile-displayphoto-shrink_800_800/0/1704355399646?e=1720051200&v=beta&t=3L_stPO8-pdpMdHq26Wh1XyrdfVTKo2KNy7RI2pMYmI",
              "public_id": "elisa-moons-a79962292",
              "school": "",
              "state": "Auvergne-Rhône-Alpes"
            },
            {
              "about": "- Proven experience in negociation with different type of clients and authorized networks\n- Expertize in realization and follow up of a budget in line with a worldwide company's strategy\n- Perfect knowledge of the selective distribution networks for high level brand image with a specific visibility\n- Management and motivation of operational and functional teams",
              "city": "Paris",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 9,
              "current_company_join_year": 2018,
              "educations": [
                {
                  "activities": "",
                  "date_range": "Sep 1993 - Jul 1996",
                  "degree": "Master",
                  "description": "",
                  "eduId": 2783338,
                  "end_month": 7,
                  "end_year": 1996,
                  "field_of_study": "",
                  "grade": "",
                  "school": "EDC Paris Business School",
                  "school_id": "15141609",
                  "school_linkedin_url": "https://www.linkedin.com/company/15141609/",
                  "start_month": 9,
                  "start_year": 1993
                },
                {
                  "activities": "",
                  "date_range": "Sep 1992 - Jun 1993",
                  "degree": "",
                  "description": "",
                  "eduId": 967695328,
                  "end_month": 6,
                  "end_year": 1993,
                  "field_of_study": "Économie",
                  "grade": "",
                  "school": "Panthéon-Assas université",
                  "school_id": "1231179",
                  "school_linkedin_url": "https://www.linkedin.com/company/1231179/",
                  "start_month": 9,
                  "start_year": 1992
                },
                {
                  "activities": "",
                  "date_range": "1989 - 1992",
                  "degree": "",
                  "description": "",
                  "eduId": 967699048,
                  "end_month": "",
                  "end_year": 1992,
                  "field_of_study": "",
                  "grade": "",
                  "school": "Lycée Chaptal",
                  "school_id": "20571411",
                  "school_linkedin_url": "https://www.linkedin.com/company/20571411/",
                  "start_month": "",
                  "start_year": 1989
                }
              ],
              "experiences": [
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 9,
                  "current_company_join_year": 2018,
                  "date_range": "Sep 2018 - present",
                  "description": "",
                  "duration": "5 yrs 9 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 9,
                  "start_year": 2018,
                  "title": "International Sales Manager Northern Hemisphere"
                },
                {
                  "company": "Lancel",
                  "company_id": "26964",
                  "company_linkedin_url": "https://www.linkedin.com/company/26964",
                  "company_public_url": null,
                  "date_range": "Jul 2004 - Apr 2018",
                  "description": "",
                  "duration": "13 yrs 10 mos",
                  "end_month": 4,
                  "end_year": 2018,
                  "is_current": false,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 7,
                  "start_year": 2004,
                  "title": "International Sales Manager EMEA South Pacific"
                },
                {
                  "company": "Montblanc",
                  "company_id": "12007",
                  "company_linkedin_url": "https://www.linkedin.com/company/12007",
                  "company_public_url": null,
                  "date_range": "Nov 2002 - Jul 2004",
                  "description": "",
                  "duration": "1 yr 9 mos",
                  "end_month": 7,
                  "end_year": 2004,
                  "is_current": false,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 11,
                  "start_year": 2002,
                  "title": "Area Sales Manager France"
                },
                {
                  "company": "Meyers Watches",
                  "company_id": "72766976",
                  "company_linkedin_url": "https://www.linkedin.com/company/72766976",
                  "company_public_url": null,
                  "date_range": "Jun 2001 - Oct 2002",
                  "description": "",
                  "duration": "1 yr 5 mos",
                  "end_month": 10,
                  "end_year": 2002,
                  "is_current": false,
                  "location": "Ville de Paris, Île-de-France, France",
                  "start_month": 6,
                  "start_year": 2001,
                  "title": "Sales Director France"
                },
                {
                  "company": "Charriol, Swiss watches and jewellery",
                  "company_id": "2747402",
                  "company_linkedin_url": "https://www.linkedin.com/company/2747402",
                  "company_public_url": null,
                  "date_range": "May 1999 - Jun 2001",
                  "description": "",
                  "duration": "2 yrs 2 mos",
                  "end_month": 6,
                  "end_year": 2001,
                  "is_current": false,
                  "location": "Joinville-le-Pont, Île-de-France, France",
                  "start_month": 5,
                  "start_year": 1999,
                  "title": "Key Account Manager Charriol & Technomarine France"
                },
                {
                  "company": "EBEL",
                  "company_id": "48914",
                  "company_linkedin_url": "https://www.linkedin.com/company/48914",
                  "company_public_url": null,
                  "date_range": "Nov 1997 - May 1999",
                  "description": "",
                  "duration": "1 yr 7 mos",
                  "end_month": 5,
                  "end_year": 1999,
                  "is_current": false,
                  "location": "Joinville-le-Pont, Île-de-France, France",
                  "start_month": 11,
                  "start_year": 1997,
                  "title": "Area Sales Manager France"
                }
              ],
              "first_name": "Thomas",
              "full_name": "Thomas Grisvard",
              "headline": "International Sales Manager Aubade",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "International Sales Manager Northern Hemisphere",
              "last_name": "Grisvard",
              "linkedin_url": "https://www.linkedin.com/in/thomas-grisvard-2751802",
              "location": "Greater Paris Metropolitan Region",
              "profile_id": "6387065",
              "profile_image_url": "https://media.licdn.com/dms/image/C5603AQGwO-rF6w18Dw/profile-displayphoto-shrink_800_800/0/1516250131831?e=1720051200&v=beta&t=XvxWqONwG_Tb-velLAVcTTAWV7xeMTnGgrixNvpjymo",
              "public_id": "thomas-grisvard-2751802",
              "school": "EDC Paris Business School",
              "state": "Paris"
            },
            {
              "about": "",
              "city": "St.-Chamas",
              "company": "Aubade Paris",
              "company_domain": "aubade.fr",
              "company_employee_range": "201 - 500",
              "company_id": "1324737",
              "company_industry": "Retail Apparel and Fashion",
              "company_linkedin_url": "https://www.linkedin.com/company/aubade",
              "company_logo_url": "https://media.licdn.com/dms/image/C560BAQEuVjYGuOSRvw/company-logo_400_400/0/1630593101061/aubade_logo?e=1723075200&v=beta&t=PLnoxP_JITM1-Qi9FJgMfppKwzvmC6LpDbi4GkFg0DM",
              "company_website": "http://www.aubade.fr",
              "company_year_founded": 1958,
              "country": "France",
              "current_company_join_month": 11,
              "current_company_join_year": 2018,
              "educations": [
                {
                  "activities": "",
                  "date_range": "2000 - 2002",
                  "degree": "Managment des Unités Commerçiales à MONTPELLIER",
                  "description": "",
                  "eduId": 309740134,
                  "end_month": "",
                  "end_year": 2002,
                  "field_of_study": "",
                  "grade": "",
                  "school": "ESARC CEFIRE",
                  "school_id": "",
                  "school_linkedin_url": "",
                  "start_month": "",
                  "start_year": 2000
                }
              ],
              "experiences": [
                {
                  "company": "Cache cache-Bonobo",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "",
                  "description": "",
                  "duration": "less than one year",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "",
                  "start_month": "",
                  "start_year": "",
                  "title": "responsable adjointe"
                },
                {
                  "company": "Aubade Paris",
                  "company_id": "1324737",
                  "company_linkedin_url": "https://www.linkedin.com/company/1324737",
                  "company_public_url": null,
                  "current_company_join_month": 11,
                  "current_company_join_year": 2018,
                  "date_range": "Nov 2018 - present",
                  "description": "",
                  "duration": "5 yrs 7 mos",
                  "end_month": "",
                  "end_year": "",
                  "is_current": true,
                  "location": "",
                  "start_month": 11,
                  "start_year": 2018,
                  "title": "Responsable de magasin"
                },
                {
                  "company": "Tape à l'oeil",
                  "company_id": "1228413",
                  "company_linkedin_url": "https://www.linkedin.com/company/1228413",
                  "company_public_url": null,
                  "date_range": "Sep 2017 - Oct 2018",
                  "description": "",
                  "duration": "1 yr 2 mos",
                  "end_month": 10,
                  "end_year": 2018,
                  "is_current": false,
                  "location": "",
                  "start_month": 9,
                  "start_year": 2017,
                  "title": "Responsable de magasin"
                },
                {
                  "company": "Armand Thiery",
                  "company_id": "",
                  "company_linkedin_url": "",
                  "company_public_url": null,
                  "date_range": "Apr 2016 - Aug 2017",
                  "description": "",
                  "duration": "1 yr 5 mos",
                  "end_month": 8,
                  "end_year": 2017,
                  "is_current": false,
                  "location": "",
                  "start_month": 4,
                  "start_year": 2016,
                  "title": "Directrice de magasin"
                },
                {
                  "company": "ARMAND THIERY SAS",
                  "company_id": "5030550",
                  "company_linkedin_url": "https://www.linkedin.com/company/5030550",
                  "company_public_url": null,
                  "date_range": "Apr 2016 - Aug 2017",
                  "description": "",
                  "duration": "1 yr 5 mos",
                  "end_month": 8,
                  "end_year": 2017,
                  "is_current": false,
                  "location": "",
                  "start_month": 4,
                  "start_year": 2016,
                  "title": "directrice de magasin"
                }
              ],
              "first_name": "Joëlle",
              "full_name": "Joëlle RANDRIA MAMPIANINA",
              "headline": "Responsable de magasin chez Aubade Paris",
              "hq_city": "Paris",
              "hq_country": "FR",
              "hq_region": "",
              "job_title": "Responsable de magasin",
              "last_name": "RANDRIA",
              "linkedin_url": "https://www.linkedin.com/in/jo%C3%ABlle-randria-mampianina-413662b7",
              "location": "St.-Chamas, Provence-Alpes-Côte d'Azur, France",
              "profile_id": "416673231",
              "profile_image_url": "",
              "public_id": "jo%C3%ABlle-randria-mampianina-413662b7",
              "school": "ESARC CEFIRE",
              "state": "Provence-Alpes-Côte d'Azur"
            }
          ],
          "message": "Showing 1 of 1 pages",
          "search_params": {
            "current_company_ids": [
              1324737
            ],
            "geo_codes": [
              105015875
            ]
          },
          "total_count": 353,
          "total_employees": 25
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Search Companies
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/search-companies') and
            i.nice_name == "Search Companies")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "message": "Use this request_id to check your search with 'Check Search Companies Status' endpoint",
          "request_id": "ba072fac0b38d12378ef5023742f0184s34e1i8n2a7p0m9o"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Check Company Search Status
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/check-search-companies-status') and
            i.nice_name == "Check Company Search Status")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "message": "Found 100/100 companies. Please use 'Get Search Companies Results' endpoint to get your data!",
          "search_params": {
            "company_headcounts": [
              "1-10",
              "11-50"
            ],
            "headquarters_location": [
              103644278
            ],
            "hiring_on_linkedin": "false",
            "industry_codes": [
              3,
              4
            ],
            "keywords": "",
            "limit": 100,
            "recent_activities": []
          },
          "status": "done",
          "total_companies": 100,
          "total_count": 120982
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Companies
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-search-companies-results') and
            i.nice_name == "Get Companies")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": [
            {
              "company_id": "80245327",
              "company_name": "ByteByteGo",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHTJOlDEd71QA/company-logo_200_200/0/1649264538350?e=1708560000&v=beta&t=fSlDCkhDJ4ybJZF57TuM0MxF3w4i1CQIniwP9jw-W8s"
            },
            {
              "company_id": "13056448",
              "company_name": "Fermat's Library",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGt_5BxNS6_zA/company-logo_200_200/0/1630658417042/fermatslibrary_logo?e=1708560000&v=beta&t=PJgqi56YKcJQVTEqAbd2l5hIJDI6YuoIcc4XH7DTL1c"
            },
            {
              "company_id": "33194007",
              "company_name": "DevFactory",
              "employee_range": "1,001-5,000 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQE9BHE8LYQpcw/company-logo_200_200/0/1630665143605/dev_factory_logo?e=1708560000&v=beta&t=3yw5IW8XGigyEjlPy25Sus9ni_nXteWoTsaQMZxLN70"
            },
            {
              "company_id": "71409420",
              "company_name": "Datamam",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQEkOuKKUxkqHw/company-logo_200_200/0/1660571089781/datamamscraping_logo?e=1708560000&v=beta&t=y56jHQ_521UnbF4dHG-nJLUVXRSDpDg612jk6fjcRbc"
            },
            {
              "company_id": "13274443",
              "company_name": "Quartic.ai",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQGpzWORgkFHrA/company-logo_200_200/0/1630634561480/quarticai_logo?e=1708560000&v=beta&t=PfZMgfa5Kz12HChyKkPChwGuG6JRiCTCK2Eq9Sd0T7Y"
            },
            {
              "company_id": "74892218",
              "company_name": "Metaphor",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQH-uT_8_KGgsQ/company-logo_200_200/0/1694540766921/metaphor_systems_logo?e=1708560000&v=beta&t=neicc7lF3yN01xb97QIPKo5xBW8IjipqdzEiLb0K0j8"
            },
            {
              "company_id": "2987720",
              "company_name": "BigRio",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQHE0aehA8eFZQ/company-logo_200_200/0/1630652178767/bigrio_logo?e=1708560000&v=beta&t=k-MRtiT747DMV4lFcwu-edCWYPUkBU3836ilO3nGTio"
            },
            {
              "company_id": "71301545",
              "company_name": "Mercor",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D4E0BAQH9Gn3NF9HQTQ/company-logo_200_200/0/1698629074328/mercor_io_logo?e=1708560000&v=beta&t=eBiajNesME21woLW1dumC2ianmfZkn7IvPasbgrH17I"
            },
            {
              "company_id": "71049830",
              "company_name": "Agile Datapro",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHD-jexUIaXWw/company-logo_200_200/0/1630670746827/agile_datapro_logo?e=1708560000&v=beta&t=Uatl8gErnJsadO_jiLFyX15W93zdMOscyokmDpp-Mjc"
            },
            {
              "company_id": "151896",
              "company_name": "Connect Tech+Talent",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D4D0BAQF882XMgbkv7g/company-logo_200_200/0/1665567754887/connecttel_logo?e=1708560000&v=beta&t=e8CADaJb_GSG6sJFDxEz4Rr-npmNlqcct1eEHmbkcKw"
            },
            {
              "company_id": "37489372",
              "company_name": "Reveation Labs",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQFxclZUJaLJIA/company-logo_200_200/0/1630530320794/reveation_labs_logo?e=1708560000&v=beta&t=bPFhBdnc1KEm8WQ1A2pu0QMRc7ng1kICzzCX5yUwn_E"
            },
            {
              "company_id": "79994924",
              "company_name": "Inflection AI",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQFr8rR19fo6iw/company-logo_200_200/0/1646755622740/inflectionai_logo?e=1708560000&v=beta&t=mX6Gv_PHJMiWjalZbmCEIuqh-nhmkg4YEYmHW3_JhkA"
            },
            {
              "company_id": "72055323",
              "company_name": "Artmac",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGlr02eM4CPGw/company-logo_200_200/0/1663506375203/artmac_soft_llc_logo?e=1708560000&v=beta&t=HK0B9Sbu6X8Qa9gbOStIsJyDUNQucxeV7t3VtyXKADk"
            },
            {
              "company_id": "4812884",
              "company_name": "Glint",
              "employee_range": "201-500 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQEXAllZSpu3iQ/company-logo_200_200/0/1632845400554/glint_inc__logo?e=1708560000&v=beta&t=keLeykzPP52DItHyLqk__mr58OsTKfSG9IQTUSNn3Ss"
            },
            {
              "company_id": "93597096",
              "company_name": "Superorder (formerly Forward Kitchens)",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D4D0BAQHSbJ1ZFU1bQQ/company-logo_200_200/0/1688478579279/superorderdotcom_logo?e=1708560000&v=beta&t=xV3izaHUrt3Em2UzP9YBGXHSlxdIu9Ic94rYzPKEero"
            },
            {
              "company_id": "18313260",
              "company_name": "Bottomless",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHpHyvRTqAC7Q/company-logo_200_200/0/1659209459807/bottomless_logo?e=1708560000&v=beta&t=DgvSgyl3j0dH2FBFTlDHSJimwFzNHrY0lTO2-fUl9aw"
            },
            {
              "company_id": "18723495",
              "company_name": "Vendition",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQFhS9BeTvlwpg/company-logo_200_200/0/1660747221789/govendition_logo?e=1708560000&v=beta&t=Y1BOk_pGrrei-yNdR2QRBQkLBNZkn42OnGTobHZOOBk"
            },
            {
              "company_id": "34225044",
              "company_name": "Guy in a Cube",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQE-tUq39m_YZA/company-logo_200_200/0/1630572177553/guyinacube_logo?e=1708560000&v=beta&t=Fq65WxQXVJzOpF5g9avZYP4p1AHVxdVnq5iB8ve1eiE"
            },
            {
              "company_id": "12588185",
              "company_name": "PieCyfer",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D4D0BAQFHWE0NU6659g/company-logo_200_200/0/1693917308367/piecyfer_logo?e=1708560000&v=beta&t=HHutWaACbm9m7hJfNl8MFiGgrxO7KuGztlGCrFbfJp0"
            },
            {
              "company_id": "47574659",
              "company_name": "Work With Indies",
              "employee_range": "1-10 employees",
              "industry": "Computer Games",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQGZG-l-HFx5Fw/company-logo_200_200/0/1697336556444/work_with_indies_logo?e=1708560000&v=beta&t=9zF7h-kAGCLX2H0wZc8Oi9c6zCIRH_dsjwSBvHMhE78"
            },
            {
              "company_id": "69501840",
              "company_name": "Welcome, an Optimizely Company",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHvLUTIPO80WA/company-logo_200_200/0/1646995384959/welcomesoftware_logo?e=1708560000&v=beta&t=1-p5EjhvKZPpGPQDCP8Aw5Nnn44Q2FZvDX697a6_jW4"
            },
            {
              "company_id": "81889327",
              "company_name": "MLflow",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQEo7OyxURpB5w/company-logo_200_200/0/1653532016747?e=1708560000&v=beta&t=dqg74NVmuQfzwdxmgEcX6KXt7pIvCkG8ZX5W2e3gYlA"
            },
            {
              "company_id": "18055275",
              "company_name": ".NET Foundation",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQEqYP0vFsgzjQ/company-logo_200_200/0/1631322224728?e=1708560000&v=beta&t=ACTqyNh1SfBbz3Yzw4ANlA5XKjGwM9NsblulNMBQQNQ"
            },
            {
              "company_id": "78792265",
              "company_name": "Delta Lake",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGNzm6_cuIfrw/company-logo_200_200/0/1643845273114?e=1708560000&v=beta&t=RyptbYwil_4s1QUIaLKmC3G4CrRe286n2yYWZ_DnGJ8"
            },
            {
              "company_id": "14505349",
              "company_name": "Recko | A Stripe company",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQFkP-cSbCe28A/company-logo_200_200/0/1630645165117/recko_logo?e=1708560000&v=beta&t=4472ZKIrGGbvXmNwlrYJ62wxp5whwN4n4hJvJY6ROnw"
            },
            {
              "company_id": "5215226",
              "company_name": "Underdog.io",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQEq6OEw509HRQ/company-logo_200_200/0/1631345935209?e=1708560000&v=beta&t=6lSlDuKlVXhdcKbgcpfTyNL1mECu3gzncWXeSKgzg6o"
            },
            {
              "company_id": "71239875",
              "company_name": "21Packets",
              "employee_range": "11-50 employees",
              "industry": "Computer Networking Products",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQGQ78YnkMfzEg/company-logo_200_200/0/1630505100888?e=1708560000&v=beta&t=cM0b1i3rq-TX5SO6QLCmW3c_KX_TNQWTkAUE69kUnhM"
            },
            {
              "company_id": "374941",
              "company_name": "Telltale Games",
              "employee_range": "11-50 employees",
              "industry": "Computer Games",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQEv-K1NWDGM_w/company-logo_200_200/0/1689183955032/telltale_games_logo?e=1708560000&v=beta&t=YvO94B10jFYUVbBLuQkEkgn9a2FylfGpN51fWW69rl4"
            },
            {
              "company_id": "31025284",
              "company_name": "Hatica",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHhdeDhCiIO9w/company-logo_200_200/0/1630670442091/hatica_logo?e=1708560000&v=beta&t=6T5nJMNa-s33Z7JPML--jRxvGiCFX0xKI0dx518z6GI"
            },
            {
              "company_id": "16218133",
              "company_name": "Markovate",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQGsWs2bk05osQ/company-logo_200_200/0/1674540275968/markovate_logo?e=1708560000&v=beta&t=onAk6hP8yZolz1JwUQAejiymNaVKhAwq1wj1kJOwn6A"
            },
            {
              "company_id": "30645878",
              "company_name": "acquire.com",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGIBh6yp6_q3Q/company-logo_200_200/0/1672882518452/acquiredotcom_logo?e=1708560000&v=beta&t=Iz8EkrFuiQPKQu1M7oU_iDpG8tN0x9xpIFp8eNDUAbo"
            },
            {
              "company_id": "92896345",
              "company_name": "ChainGPT",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D4D0BAQEgrZpe9Ca4Tg/company-logo_200_200/0/1693553830117/chaingpt_logo?e=1708560000&v=beta&t=O9EgmiuGoofYeqk-KLXoHftdlAnhyk0cE5LAkcbBkrE"
            },
            {
              "company_id": "79684550",
              "company_name": "ReaCredence IT Solutions Inc",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQGuj9HTLGT-7w/company-logo_200_200/0/1630647446382/reacredence_it_solutions_inc_logo?e=1708560000&v=beta&t=IXZbqe4Aez3XGVRYt8VslM3GF_IcdclY_wnBLYNqqNY"
            },
            {
              "company_id": "3497316",
              "company_name": "Mental Canvas",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQH5-Pj_c3NMyw/company-logo_200_200/0/1630614694844/mental_canvas_logo?e=1708560000&v=beta&t=MipHZxCOj9G638wLA4OqVD5-ALGrlAiYujL006es2Ko"
            },
            {
              "company_id": "2946878",
              "company_name": "GNS3 Technologies Inc.",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQERH_LfZPreTA/company-logo_200_200/0/1630522363375/gns3_net_logo?e=1708560000&v=beta&t=HjLhvFLwYts795LhY7s7jU2pQhOusbrLDlPjZR6SxPM"
            },
            {
              "company_id": "35436138",
              "company_name": "Avolin",
              "employee_range": "201-500 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQGqqaeB9_lsCQ/company-logo_200_200/0/1630608336939/avolin_logo?e=1708560000&v=beta&t=Xvf4C91TjjivgA1iZPk-YVbzx9iPbGyTj8qeqDl5a30"
            },
            {
              "company_id": "9205688",
              "company_name": "DigiCollect",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGyrR1nG6__4A/company-logo_200_200/0/1672658242972?e=1708560000&v=beta&t=qtnb5SzO0OKYvr3_5YgQIVAkvwUVAMzodLWqkVYwmT4"
            },
            {
              "company_id": "80347916",
              "company_name": "Luma AI",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQE0nT3a5Zw0Qg/company-logo_200_200/0/1686162321563/luma_ai_logo?e=1708560000&v=beta&t=e7iiJGuQi1bhAdfds7xM_9x1ngUKBzxw3rhbW9esQpU"
            },
            {
              "company_id": "13744932",
              "company_name": "Prime Consulting Inc",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C510BAQFMLYPsp_hYBw/company-logo_200_200/0/1631396683637/prime_consulting_inc_logo?e=1708560000&v=beta&t=Yu3Kj2pXKvM-c_Dhu-D1xZc03ts3fU45ZJs5fUzyUiQ"
            },
            {
              "company_id": "10838635",
              "company_name": "Chorus by ZoomInfo",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQFE8zKGQedU_g/company-logo_200_200/0/1630639369988/chorusai_logo?e=1708560000&v=beta&t=BKbR8H1caP1petqUf_svpk-Kdv3KK_8K844a5TYjno4"
            },
            {
              "company_id": "2714872",
              "company_name": "pymetrics (now Harver)",
              "employee_range": "201-500 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQGtuVcLBAedHg/company-logo_200_200/0/1677701659558/pymetrics_logo?e=1708560000&v=beta&t=AuU8DGQ3Nq2-A46J2HP93Ke60QX30jB9Cth5VkFHY-0"
            },
            {
              "company_id": "27171191",
              "company_name": "odiggo",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQF9bV8NmyrwyQ/company-logo_200_200/0/1667434607428/odiggo_logo?e=1708560000&v=beta&t=FLjMkY8OtrKAt8O02eV8BwEgM1IHqhXmdvyHj4RXlyE"
            },
            {
              "company_id": "13266971",
              "company_name": "MergerWare",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQGRaOqeBXw3Kg/company-logo_200_200/0/1643542803794/mergerware_logo?e=1708560000&v=beta&t=VxsI7-CJPhCk58rDHDnqukVPo8vuIhwNr-uFEjRlst4"
            },
            {
              "company_id": "76718489",
              "company_name": "SmartSuite",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQHw54aq09-tUw/company-logo_200_200/0/1630648913223/hellosmartsuite_logo?e=1708560000&v=beta&t=8Gn0i-TEJKTDYpJM6DzuO_FXbaMv3iqJYFWD37qI55c"
            },
            {
              "company_id": "2098890",
              "company_name": "Percolate by Seismic",
              "employee_range": "201-500 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHPbfJlSWFWyg/company-logo_200_200/0/1630671138150/percolate_inc_logo?e=1708560000&v=beta&t=aL4mCGMya_gSibJxMDehCN2f0BDbAHd4MYIjVSR_VMo"
            },
            {
              "company_id": "91507115",
              "company_name": "OmniVoid",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQGnhD-cO_b1Sg/company-logo_200_200/0/1670844181499/omnivoid_logo?e=1708560000&v=beta&t=GucCrhjaqmpqFsQ8jCTuZahw3KnM3CnMaF-FxIWdwZg"
            },
            {
              "company_id": "1316444",
              "company_name": "ThingWorx, a PTC Technology",
              "employee_range": "5,001-10,000 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQEngCwLtza4hw/company-logo_200_200/0/1630555234163/ptc_thingworx_logo?e=1708560000&v=beta&t=_lCbeN3XzvGkjkGDcjHsupHxJajz7M1YUaMb1VmD0lI"
            },
            {
              "company_id": "18993699",
              "company_name": "Nestor",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGVnO8kIVnQaw/company-logo_200_200/0/1630624833033/nestorup_logo?e=1708560000&v=beta&t=O_gZyQMz_6hUQV7py_Tf3Z6E81fmHkZjWovHAh2e99E"
            },
            {
              "company_id": "7601819",
              "company_name": "Datatron ",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGQspUTOEcv5w/company-logo_200_200/0/1634599385007/datatron_io_logo?e=1708560000&v=beta&t=qgPaMhJsEt7JviC4WDPy-x-lOF5oBCgSzr6BHE2fRT4"
            },
            {
              "company_id": "15195536",
              "company_name": "Salesforce Revenue Cloud",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQHDxiyPfprjHg/company-logo_200_200/0/1630577249771/salesforce_quote_to_cash_logo?e=1708560000&v=beta&t=lfSL79yxjx_2UZRXeCZbNDpoktaQul_RoyCp9bXpbk4"
            },
            {
              "company_id": "31560790",
              "company_name": "Signalytics",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQHoz3Dom5p4FQ/company-logo_200_200/0/1679783193334/howardthai_logo?e=1708560000&v=beta&t=oJv6Dei4rpwWLEYU3IyrdVXdDvVrP5eaflEazjhE2Hg"
            },
            {
              "company_id": "13225446",
              "company_name": "RootLiquids",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQFIwEjT1fJPIg/company-logo_200_200/0/1631358200457?e=1708560000&v=beta&t=jdJjVaI_CGE392Nhz4h0QszAlCOTV0wYdIU3sq-iP-4"
            },
            {
              "company_id": "4873004",
              "company_name": "Facet",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHOUDzWZqrsjA/company-logo_200_200/0/1630632693146/facetdev_logo?e=1708560000&v=beta&t=VaSLciUI-LZwe-FAddwpSuhXWEweeIF418eWCBXDBFY"
            },
            {
              "company_id": "73804631",
              "company_name": "Slope",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D4D0BAQF7oLdcDlWQ1w/company-logo_200_200/0/1692806833889/slope_tech_logo?e=1708560000&v=beta&t=dqGLGMoyaFxNDvfL0DnNAJdCmYyfjGa6JYATcQK3Elw"
            },
            {
              "company_id": "42676982",
              "company_name": "Dreamhaven",
              "employee_range": "11-50 employees",
              "industry": "Computer Games",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQGZDGrZNdWQqw/company-logo_200_200/0/1691106786015/dreamhaven_logo?e=1708560000&v=beta&t=jldN9_ITw5EfNiz36i1VmrriKWF0UhwLbrXOKmVIKDo"
            },
            {
              "company_id": "861363",
              "company_name": "Supergiant Games",
              "employee_range": "11-50 employees",
              "industry": "Computer Games",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQGpmRCcfvZBZA/company-logo_200_200/0/1630578373427/supergiant_games_logo?e=1708560000&v=beta&t=X47hzrOlvnuCjxyFrPuKeSR3Aq11YLhvccZ1JGGBO6M"
            },
            {
              "company_id": "2893973",
              "company_name": "Cumulus Networks",
              "employee_range": "201-500 employees",
              "industry": "Computer Networking Products",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQEPMwz8RK28eg/company-logo_200_200/0/1630528771599/cumulus_networks_logo?e=1708560000&v=beta&t=Dder7rh1Is2w9uML8v6m-h31uvVwjSjpOGmAhRcyvoU"
            },
            {
              "company_id": "77034372",
              "company_name": "CoreTek Labs",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHgMvsACWCe9w/company-logo_200_200/0/1669990904037/coreteklabs_logo?e=1708560000&v=beta&t=vqHTQd2w3bSBOvgw4rW0CMUzrvXXb_FeOP5-AnBCIng"
            },
            {
              "company_id": "10600798",
              "company_name": "WeCP | We Create Problems",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQE8kGrqsy5MuQ/company-logo_200_200/0/1691746004861/wecreateproblems_logo?e=1708560000&v=beta&t=z1P7od8AhsP2VIFCoNVxVAiDzb6G0QUIGzdWpYik1lU"
            },
            {
              "company_id": "87431258",
              "company_name": "Agency Upp",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQGDW7XUwJ6vRA/company-logo_200_200/0/1669643817113/agencyupp_logo?e=1708560000&v=beta&t=zXmpp845PNbqGlNPZiEZor1ctfaUWufwvDKPdqAUch0"
            },
            {
              "company_id": "5205148",
              "company_name": "ThisWay Global",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQFQlsiMxc6aug/company-logo_200_200/0/1662565353045/thisway_global_logo?e=1708560000&v=beta&t=HcSs6IpVQfTj2Y5AIY4kKhE3i94E4ojWbJGDGz1yDg4"
            },
            {
              "company_id": "80650579",
              "company_name": "Speak_",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQGaVwPNNE_nhg/company-logo_200_200/0/1636821130263/speakcareers_logo?e=1708560000&v=beta&t=sVGRyW4ddNtowAuiSFmdL8NEn4O0fLFvXE4hw-gmIiY"
            },
            {
              "company_id": "30587144",
              "company_name": "InsideSales",
              "employee_range": "501-1,000 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQE6LzUDYWeYaA/company-logo_200_200/0/1633380139022/xant_ai_logo?e=1708560000&v=beta&t=4uOy_l-zI16fMau13Lm2Hnl4YzefTMiKTk3X4YqSB1Q"
            },
            {
              "company_id": "11379543",
              "company_name": "The LCN Firm, Inc .",
              "employee_range": "1-10 employees",
              "industry": "Computer Networking Products",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGm_mrNufhnCw/company-logo_200_200/0/1631340690848?e=1708560000&v=beta&t=oTd0o6EDK4x4Vaeq5y7IdG4i06cVRDRxu9ALzuOFg2s"
            },
            {
              "company_id": "75020882",
              "company_name": "Sunday Labs",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQFlGHZypQTXCg/company-logo_200_200/0/1648451147760/horsetails_logo?e=1708560000&v=beta&t=uAuiz6UhcIhjrfrpSIHSzfyfQ6oufKC8eF9FQvthqy4"
            },
            {
              "company_id": "13579747",
              "company_name": "Chezuba",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C510BAQFJFT6WWDUP3Q/company-logo_200_200/0/1631422112101?e=1708560000&v=beta&t=L3FERmgBzCugI8cDLssniSyv0DkvTt5AUbXv_1DwnBk"
            },
            {
              "company_id": "18660478",
              "company_name": "RYVYL",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQGAOZ_VIZ5-8Q/company-logo_200_200/0/1668097145353/ryvyl_logo?e=1708560000&v=beta&t=ZJsiuKDJifHAxR0e804ZNh4_Xc-88ZE15fmIxrOkC-A"
            },
            {
              "company_id": "11329925",
              "company_name": "DataFinery Inc.",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGqn54b-3YnIw/company-logo_200_200/0/1674055247475/datafinery_logo?e=1708560000&v=beta&t=dsYeJ0Jfh4i_5AylLiSDJpEtnp0GNVqhrb6WR5m2JEE"
            },
            {
              "company_id": "80013344",
              "company_name": "engineersmind",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQHBlR-zmDdPgg/company-logo_200_200/0/1646962573572?e=1708560000&v=beta&t=MuB453oEBWekPKX5BQG2O6ooCBP_DuDdYYMeyDpgL6w"
            },
            {
              "company_id": "3284959",
              "company_name": "ALSCO",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQGrWT-mk-7hTw/company-logo_200_200/0/1631347002485?e=1708560000&v=beta&t=DA-fJNA0lbvdqBEDS_A_6DkPuOSK99DAxk8WDCA997U"
            },
            {
              "company_id": "18578562",
              "company_name": "Arbor ",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHd-Uar2Nb27Q/company-logo_200_200/0/1631396201375?e=1708560000&v=beta&t=1DTHyFTbbliy7xJ-iYjYflhrU3E6D1jQcptEvsBm7WU"
            },
            {
              "company_id": "71614174",
              "company_name": "Tech Career Growth Community",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQEm3xIzfGPg2g/company-logo_200_200/0/1630672824373/techcareergrowth_logo?e=1708560000&v=beta&t=wzE3u2d3hC3qHkzpCi-Ocj_59Tim86LP0nCt2PMMUY0"
            },
            {
              "company_id": "88007673",
              "company_name": "Perplexity",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQFNCoFCub_8sw/company-logo_200_200/0/1698290900915/perplexity_ai_logo?e=1708560000&v=beta&t=cBxCDH6BuK_7F-8Hkm32bpQjxpuRWDBWxaUpqt7PVYY"
            },
            {
              "company_id": "5273603",
              "company_name": "Peer Consulting Resources Inc.",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQG4hw1g3x1eNA/company-logo_200_200/0/1674517825162/peer_consulting_logo?e=1708560000&v=beta&t=nmK7y2HLFbommoEA8_1j72Mc0ATXw2i1UVa4AaZYiLM"
            },
            {
              "company_id": "89848",
              "company_name": "VMware Horizon",
              "employee_range": "10,001+ employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQG92NfoTJiSjA/company-logo_200_200/0/1630636878699/vmwarehorizon_logo?e=1708560000&v=beta&t=8CCqw-a06R323MxBYw2kcBzR_CKy68j2nSHxn0UBSII"
            },
            {
              "company_id": "16217177",
              "company_name": "PickNik Robotics",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQF9nTZigRN7uQ/company-logo_200_200/0/1680644683559/picknik_logo?e=1708560000&v=beta&t=9y0EH_esXO3eEXaAnv5X-1NAXj2sfKvslTtzU5SJ5Eo"
            },
            {
              "company_id": "82825689",
              "company_name": "Microsoft Power Platform Community",
              "employee_range": "10,001+ employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQFhPajkk8Oypw/company-logo_200_200/0/1662089970627?e=1708560000&v=beta&t=RRzRb-XcEPenWkf5hLHi4sAYX3-kQIuIGAC_GdAKrjk"
            },
            {
              "company_id": "31338988",
              "company_name": "Fundamento",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQHoXhBoQcjiBQ/company-logo_200_200/0/1669102255408/fundamento_ai_logo?e=1708560000&v=beta&t=94Hdv3OWjuxUaZS0EB1hbiTnzfb6xQjasvfmZDZM4Nc"
            },
            {
              "company_id": "35516406",
              "company_name": "Kafka",
              "employee_range": "1-10 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQEzCUKm7nud_g/company-logo_200_200/0/1630565037182/kafka_stream_logo?e=1708560000&v=beta&t=fziHogN3QlEbC1zKjgl7MEUps8-7LhjoDE-FujeCUfM"
            },
            {
              "company_id": "91626670",
              "company_name": "InteliX Systems",
              "employee_range": "51-200 employees",
              "industry": "IT Services and IT Consulting",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGYe8TnPgRhqA/company-logo_200_200/0/1672479595443/intelix_systems_logo?e=1708560000&v=beta&t=c6hrTJ5uk7VBg54mz9xLWJH4Uzf3Gdupt02jqxOxZdQ"
            },
            {
              "company_id": "68608005",
              "company_name": "Caroo",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQE6pckGqvntcw/company-logo_200_200/0/1684172222096/caroo_logo?e=1708560000&v=beta&t=ztQofrRb3bjCCY-429ID9Na10w4qcszX5S8oxDXnfPI"
            },
            {
              "company_id": "31248402",
              "company_name": "EOXS",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQGVpvvk_Ggrxg/company-logo_200_200/0/1630646552949/eoxs_steel_logo?e=1708560000&v=beta&t=MAZNYA6mx2ThaPktZHXPW0qhBejWhS-6ShdLgyM9pZA"
            },
            {
              "company_id": "15257232",
              "company_name": "Autzu",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQE9pB63_jqMeQ/company-logo_200_200/0/1630568303214/autzu_logo?e=1708560000&v=beta&t=p3XI7STr7xM5flEmNwrgfg2Zvgb_kZ2j6TRf-Y5um9U"
            },
            {
              "company_id": "10681658",
              "company_name": "The Tor Project",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQF6FMIM3zakTg/company-logo_200_200/0/1697464471045/tor_project_logo?e=1708560000&v=beta&t=Pgj_Mjfct2v07RAxZgMv6bCDZuPi_Vu6bEVmQIcwYMo"
            },
            {
              "company_id": "3281593",
              "company_name": "Quip",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQFtLBSNRgxEqw/company-logo_200_200/0/1630652124315/quip_com_logo?e=1708560000&v=beta&t=MmOI3a6HY4EDvTHNPj3FsiybQDYAiJUb-1ZtCKJaueQ"
            },
            {
              "company_id": "220061",
              "company_name": "Birst",
              "employee_range": "10,001+ employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQHBOkJphU5qYA/company-logo_200_200/0/1699631599768/birst_logo?e=1708560000&v=beta&t=4sdbwe0mBGvlYptXP-bGsynQhgRFvh0wOhO8CJy9sDw"
            },
            {
              "company_id": "82914",
              "company_name": "InsideSales.com",
              "employee_range": "501-1,000 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQGEuGqPQrbuQQ/company-logo_200_200/0/1633699798229/insidesales_logo?e=1708560000&v=beta&t=bcXwd9BP3BQPVt8wiszJ-rfzIpidNx8IpMh4snw6AP4"
            },
            {
              "company_id": "2707347",
              "company_name": "PlanGrid, an Autodesk company",
              "employee_range": "201-500 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQFSS6NsCYMb7g/company-logo_200_200/0/1690487229938/plangrid_logo?e=1708560000&v=beta&t=Oq0D7xdNJqpZygMpww--rUsX3ePLNormK-XhEV4PGJw"
            },
            {
              "company_id": "1180889",
              "company_name": "Greenlots",
              "employee_range": "201-500 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHcEltOPmGgGw/company-logo_200_200/0/1630607175629/greenlots_logo?e=1708560000&v=beta&t=JfIdkj05syC_N7DcHfc2cm5orr3pSDnGUJL9f4KyBO8"
            },
            {
              "company_id": "3595230",
              "company_name": "ClientSuccess",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQHnikQqEdwwIw/company-logo_200_200/0/1698726806658/clientsuccess_logo?e=1708560000&v=beta&t=e1EofaxEU3Kg8kCXrJ4F3L-ADS8YjBX1fhP2aMIcwWA"
            },
            {
              "company_id": "10214178",
              "company_name": "GrowthHackers",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQF9winrh4hg7w/company-logo_200_200/0/1630625794935/growthhackershq_logo?e=1708560000&v=beta&t=VOO2xVmtGvDu1Q9samhCd1yLMK7EpMDKCT_v0dzjWQ4"
            },
            {
              "company_id": "10988776",
              "company_name": "Innovyt",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQEqZOJ19Fdvfg/company-logo_200_200/0/1631357159896?e=1708560000&v=beta&t=GhYYlFTgg-6CVAT_lj9EBVC4CY5FpIpvYjr6Lig-G3o"
            },
            {
              "company_id": "18131896",
              "company_name": "Alkymi",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D4E0BAQF92TldF_RYiw/company-logo_200_200/0/1686708867675/alkymi_logo?e=1708560000&v=beta&t=T44E9WlQP_7Bhu3OmwDMCh-WczQBiYDhR1G-Fu5f1xE"
            },
            {
              "company_id": "492926",
              "company_name": "Altair RapidMiner",
              "employee_range": "1,001-5,000 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQFK5k_r2gO70Q/company-logo_200_200/0/1651579826463/rapidminer_logo?e=1708560000&v=beta&t=3Yf_lezW8IH2hIKZHKUDUAU6GPWP8fOLLHtHRuGGHRk"
            },
            {
              "company_id": "10820999",
              "company_name": "TestGrid.io",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4D0BAQEF4wlMjvN1vA/company-logo_200_200/0/1630456583254/testgridio_logo?e=1708560000&v=beta&t=lLRpFhR5pMiUSxMUdVlqY1hK_s5_-coYhO9flmAay08"
            },
            {
              "company_id": "28601613",
              "company_name": "Airkit.ai",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D4E0BAQE8mNOcd8KtLA/company-logo_200_200/0/1689876404266/airkitcx_logo?e=1708560000&v=beta&t=WdP0lEnv1wzzMlNvEASXtuC1FjcWXMeyvYFvNMFRLJo"
            },
            {
              "company_id": "3724051",
              "company_name": "ZineOne",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/D560BAQFlLhQt2Z0aUQ/company-logo_200_200/0/1694620399170/zineone_logo?e=1708560000&v=beta&t=EvThFUusU8bI_lmTMJz7bM0ELHbBvYllaYXaEwGoOsY"
            },
            {
              "company_id": "29366061",
              "company_name": "Guise AI",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQHuvY5ezW5BCA/company-logo_200_200/0/1643631600630/guise_ai_logo?e=1708560000&v=beta&t=s8YqaePdhSDbbfCAn0ktG9fbHZcOkcD_nX2R5fUACX4"
            },
            {
              "company_id": "2423176",
              "company_name": "Velocity FinCrime Solutions Suite",
              "employee_range": "51-200 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C560BAQE77YvexrB-2w/company-logo_200_200/0/1676010943468/velocity_fincrime_solutions_suite_logo?e=1708560000&v=beta&t=7GdSwiAHtdU1g8VhyfKRKHMq1fB1sDbnw5Wkl41qPaU"
            },
            {
              "company_id": "18762491",
              "company_name": "Strategic DX - Your Dealer Experience",
              "employee_range": "11-50 employees",
              "industry": "Software Development",
              "logo_url": "https://media.licdn.com/dms/image/C4E0BAQFfTqkxAD-PEA/company-logo_200_200/0/1630655118910/strategic_dx_logo?e=1708560000&v=beta&t=xNVZZzwaHbg1b5uQa4WrmeOn9UqMXUWOHI8dXxZzs4c"
            }
          ],
          "message": "Showing 1 of 2 pages",
          "search_params": {
            "company_headcounts": [
              "1-10",
              "11-50"
            ],
            "headquarters_location": [
              103644278
            ],
            "hiring_on_linkedin": "false",
            "industry_codes": [
              3,
              4
            ],
            "keywords": "",
            "limit": 100,
            "recent_activities": []
          },
          "total_companies": 105,
          "total_count": 120982
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Search Jobs
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/search-jobs') and
            i.nice_name == "Search Jobs")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": [
            {
              "company": "iSqFt logo",
              "company_linkedin_url": "https://www.linkedin.com/company/isqft/life",
              "company_logo": "https://media.licdn.com/dms/image/C4D0BAQEZKtVKXXF6Fg/company-logo_",
              "job_description": "iSqFt",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3890867613,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712850960000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_CREATE",
                  "entityUrn": "urn:li:fsd_jobPosting:3890867613",
                  "repostedJob": false,
                  "title": "Product Training Specialist, Data",
                  "trackingUrn": "urn:li:jobPosting:3890867613"
                },
                "jobPostingTitle": "Product Training Specialist, Data",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3890867613",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3890867613"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3890867613",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3890867613",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3890867613",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "iSqFt logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/isqft/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:38662",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1631310598620?e=1721260800&v=beta&t=vo62kajOhRqnHdp3JlNWUR2r3R_b1IvAR8NMx9MLJLs",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1631310598620?e=1721260800&v=beta&t=OXEsznkjUeJLJZlHC1kKEITQ2mWEzwnsyD_PGCv-_CA",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1631310598620?e=1721260800&v=beta&t=iS4jagz2NRY6CDmYVtWwirunwX34L9V51pKLkIu2Lpg",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C4D0BAQEZKtVKXXF6Fg/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:38662"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3890867613",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Product Training Specialist, Data job",
                        "accessibilityNameSelected": "Product Training Specialist, Data job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3890867613"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3890867613"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "iSqFt",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 33,
                      "start": 0
                    }
                  ],
                  "text": "Product Training Specialist, Data",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "BA9kDRsCCQnwrYtGbQAiXw=="
              },
              "job_title": "Product Training Specialist, Data",
              "job_urn": "urn:li:fsd_jobPosting:3890867613",
              "posted_time": "2024-04-11 15:56:00",
              "remote": "Remote",
              "salary": ""
            },
            {
              "company": "Hearth logo",
              "company_linkedin_url": "https://www.linkedin.com/company/gethearth/life",
              "company_logo": "https://media.licdn.com/dms/image/C560BAQFnJk1eV3lcMg/company-logo_",
              "job_description": "Hearth",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3895280497,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712870199000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [],
                      "text": "Easy Apply",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "EASY_APPLY_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3895280497",
                  "posterId": "768723211",
                  "repostedJob": false,
                  "title": "Account Executive",
                  "trackingUrn": "urn:li:jobPosting:3895280497"
                },
                "jobPostingTitle": "Account Executive",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3895280497",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3895280497?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3895280497"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3895280497",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3895280497",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3895280497",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Hearth logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/gethearth/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:12908147",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1673447568673/gethearth_logo?e=1721260800&v=beta&t=440xvoOby4S0dX0ogx_JfBWhsfTlJfVl-X5COeWakUY",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1673447568673/gethearth_logo?e=1721260800&v=beta&t=PTHizIhpg7YH9V0OmV_w415SHqCc8Q6mMmYIfTOAB6I",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1673447568673/gethearth_logo?e=1721260800&v=beta&t=BzSmgbTOOmsjI93eUJRMSH33BCIJPVKthQkP3kWL5HE",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C560BAQFnJk1eV3lcMg/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:12908147"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3895280497",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Account Executive job",
                        "accessibilityNameSelected": "Account Executive job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895280497"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895280497"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Hearth",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$35K/yr + Commission · 401(k) benefit",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 17,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 18
                    }
                  ],
                  "text": "Account Executive  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "8zb0CX3oxeols+cjx6jErg=="
              },
              "job_title": "Account Executive",
              "job_urn": "urn:li:fsd_jobPosting:3895280497",
              "posted_time": "2024-04-11 21:16:39",
              "remote": "Remote",
              "salary": "$35K/yr + Commission · 401(k) benefit"
            },
            {
              "company": "Levelset, a Procore Company logo",
              "company_linkedin_url": "https://www.linkedin.com/company/levelset/life",
              "company_logo": "https://media.licdn.com/dms/image/D560BAQGEkq1sFxyejA/company-logo_",
              "job_description": "Levelset, a Procore Company",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3895564983,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712894629000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3895564983",
                  "posterId": "47253449",
                  "repostedJob": false,
                  "title": "Research & Data Administrator - Levelset",
                  "trackingUrn": "urn:li:jobPosting:3895564983"
                },
                "jobPostingTitle": "Research & Data Administrator - Levelset",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3895564983",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3895564983?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3895564983"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3895564983",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3895564983",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3895564983",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Levelset, a Procore Company logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/levelset/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:2608095",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1662564660837/levelset_logo?e=1721260800&v=beta&t=W-rmsEWPU65Ba_aI_xo4_Z0vimkPh7f_qAiA2uN4KD4",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1662564660837/levelset_logo?e=1721260800&v=beta&t=RIcDMml2UuJB-uOM1TtrBeAcu5zgT6utsbvSlfa7Hig",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1662564660837/levelset_logo?e=1721260800&v=beta&t=bFX0WKFETPxfESXCObz7vGx8jPEBZeEEenirj01V-lI",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D560BAQGEkq1sFxyejA/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:2608095"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3895564983",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Research & Data Administrator - Levelset job",
                        "accessibilityNameSelected": "Research & Data Administrator - Levelset job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895564983"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895564983"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Levelset, a Procore Company",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "New Orleans, LA",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$19/hr - $22/hr",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 40,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 41
                    }
                  ],
                  "text": "Research & Data Administrator - Levelset  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "M+URGUvZsNMPd7sW6KhEfQ=="
              },
              "job_title": "Research & Data Administrator - Levelset",
              "job_urn": "urn:li:fsd_jobPosting:3895564983",
              "posted_time": "2024-04-12 04:03:49",
              "remote": "New Orleans, LA",
              "salary": "$19/hr - $22/hr"
            },
            {
              "company": "ChiroTouch logo",
              "company_linkedin_url": "https://www.linkedin.com/company/chirotouch/life",
              "company_logo": "https://media.licdn.com/dms/image/C560BAQEN27GDgqANGQ/company-logo_",
              "job_description": "ChiroTouch",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3889683451,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712769564000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [],
                      "text": "Easy Apply",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "EASY_APPLY_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3889683451",
                  "posterId": "319248234",
                  "repostedJob": false,
                  "title": "Chiropractic Software Onboarding Specialist (Remote)",
                  "trackingUrn": "urn:li:jobPosting:3889683451"
                },
                "jobPostingTitle": "Chiropractic Software Onboarding Specialist (Remote)",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3889683451",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3889683451"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3889683451",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3889683451",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3889683451",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "ChiroTouch logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/chirotouch/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:371531",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1630664218198/chirotouch_logo?e=1721260800&v=beta&t=3GZl3zECRneUnpeysO3g0Inl9MCKTNydCk2_c3ABaBM",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1630664218198/chirotouch_logo?e=1721260800&v=beta&t=ql6hnrSatb8kI7jtmp3Jj3WIJQ_DCX1SW9pjMl6ra3Q",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1630664218198/chirotouch_logo?e=1721260800&v=beta&t=pCSicYlGJU2jypHOAz_mmC-qgT1rPtfj-VroGpThmfk",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C560BAQEN27GDgqANGQ/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:371531"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3889683451",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Chiropractic Software Onboarding Specialist (Remote) job",
                        "accessibilityNameSelected": "Chiropractic Software Onboarding Specialist (Remote) job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3889683451"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3889683451"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "ChiroTouch",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 52,
                      "start": 0
                    }
                  ],
                  "text": "Chiropractic Software Onboarding Specialist (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "nrWxQACXx9u9DOGLjkKedA=="
              },
              "job_title": "Chiropractic Software Onboarding Specialist (Remote)",
              "job_urn": "urn:li:fsd_jobPosting:3889683451",
              "posted_time": "2024-04-10 17:19:24",
              "remote": "Remote",
              "salary": ""
            },
            {
              "company": "Centerbase logo",
              "company_linkedin_url": "https://www.linkedin.com/company/centerbase/life",
              "company_logo": "https://media.licdn.com/dms/image/C560BAQFhRtU_Ga8Gqw/company-logo_",
              "job_description": "Centerbase",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3892597013,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712763104000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [],
                      "text": "Easy Apply",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "EASY_APPLY_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3892597013",
                  "posterId": "953288827",
                  "repostedJob": false,
                  "title": "Business Development Representative",
                  "trackingUrn": "urn:li:jobPosting:3892597013"
                },
                "jobPostingTitle": "Business Development Representative",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3892597013",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3892597013?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3892597013"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3892597013",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3892597013",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3892597013",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Centerbase logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/centerbase/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:348836",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1630670136820/centerbase_logo?e=1721260800&v=beta&t=bbV2BaNdMuye2S_kTaP5tJ8XNPDVwSJxtd2Gn118o-0",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1630670136820/centerbase_logo?e=1721260800&v=beta&t=aiMFfW-mnn1UY6heNMqndy4iH2I0JAe7cF8qVwJ1i1Q",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1630670136820/centerbase_logo?e=1721260800&v=beta&t=Ab7ZyGBYH0lEvVEaK_E2phQ4xJcd0C5eq20O7BUM1-4",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C560BAQFhRtU_Ga8Gqw/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:348836"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3892597013",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Business Development Representative job",
                        "accessibilityNameSelected": "Business Development Representative job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3892597013"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3892597013"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Centerbase",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "6 benefits",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 35,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 36
                    }
                  ],
                  "text": "Business Development Representative  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "Ix4AFjb6h44AOu9SyzP/9A=="
              },
              "job_title": "Business Development Representative",
              "job_urn": "urn:li:fsd_jobPosting:3892597013",
              "posted_time": "2024-04-10 15:31:44",
              "remote": "Remote",
              "salary": "6 benefits"
            },
            {
              "company": "Paytronix logo",
              "company_linkedin_url": "https://www.linkedin.com/company/paytronix-systems/life",
              "company_logo": "https://media.licdn.com/dms/image/D4E0BAQHKHnSLlWpRXw/company-logo_",
              "job_description": "Paytronix",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3893692311,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712853008000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3893692311",
                  "posterId": "609437919",
                  "repostedJob": false,
                  "title": "Sales Development Representative",
                  "trackingUrn": "urn:li:jobPosting:3893692311"
                },
                "jobPostingTitle": "Sales Development Representative",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3893692311",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3893692311?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3893692311"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3893692311",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3893692311",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3893692311",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Paytronix logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/paytronix-systems/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:131209",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1688560890804/paytronix_systems_logo?e=1721260800&v=beta&t=rguZ2htil0xxBK9-AZynPUtNCIMEnWEHkq8cJVQyglA",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1688560890804/paytronix_systems_logo?e=1721260800&v=beta&t=DyY6WBN3WOJP0oTDkxJnJI8L0mkGudz6Pq_BYAL_8do",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1688560890804/paytronix_systems_logo?e=1721260800&v=beta&t=ce-WfUfYW7SzL-XF0ZfiUkg5WcqN2wvJGOt7by896eI",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D4E0BAQHKHnSLlWpRXw/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:131209"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3893692311",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Sales Development Representative job",
                        "accessibilityNameSelected": "Sales Development Representative job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3893692311"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3893692311"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Paytronix",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Newton, MA (Hybrid)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "401(k) benefit",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 32,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 33
                    }
                  ],
                  "text": "Sales Development Representative  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "KKmC8qyWPQqq4uW+X+R8fg=="
              },
              "job_title": "Sales Development Representative",
              "job_urn": "urn:li:fsd_jobPosting:3893692311",
              "posted_time": "2024-04-11 16:30:08",
              "remote": "Hybrid",
              "salary": "401(k) benefit"
            },
            {
              "company": "Tebra logo",
              "company_linkedin_url": "https://www.linkedin.com/company/tebra/life",
              "company_logo": "https://media.licdn.com/dms/image/C560BAQEfNZEbv6Oxww/company-logo_",
              "job_description": "Tebra",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3891633187,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712703008000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [],
                      "text": "Easy Apply",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "EASY_APPLY_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3891633187",
                  "posterId": "384240660",
                  "repostedJob": false,
                  "title": "Account Executive, Billing Company",
                  "trackingUrn": "urn:li:jobPosting:3891633187"
                },
                "jobPostingTitle": "Account Executive, Billing Company",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3891633187",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3891633187?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3891633187"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3891633187",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3891633187",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3891633187",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Tebra logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/tebra/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:76976606",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1656512021246/tebra_logo?e=1721260800&v=beta&t=ZT0axz4-C6V2m--drHQ2JNi5li6uxIgUiAa1ye8mWSg",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1656512021246/tebra_logo?e=1721260800&v=beta&t=k06Lkdq5LpKWkSiN-b1nc2YztB07onPzFl6rlkGr3Io",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1656512021246/tebra_logo?e=1721260800&v=beta&t=hSxo3SrIGzZiElpUwXhenMfFbLdr5ONP4TamIaPiUmg",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C560BAQEfNZEbv6Oxww/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:76976606"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3891633187",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Account Executive, Billing Company job",
                        "accessibilityNameSelected": "Account Executive, Billing Company job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891633187"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891633187"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Tebra",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$110K/yr - $130K/yr",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 34,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 35
                    }
                  ],
                  "text": "Account Executive, Billing Company  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "Jza72V+ejhN0wG4RNhYOUA=="
              },
              "job_title": "Account Executive, Billing Company",
              "job_urn": "urn:li:fsd_jobPosting:3891633187",
              "posted_time": "2024-04-09 22:50:08",
              "remote": "Remote",
              "salary": "$110K/yr - $130K/yr"
            },
            {
              "company": "Dark Matter Technologies logo",
              "company_linkedin_url": "https://www.linkedin.com/company/darkmattertechnologies/life",
              "company_logo": "https://media.licdn.com/dms/image/D4E0BAQGNs6D3RTb0NQ/company-logo_",
              "job_description": "Dark Matter Technologies",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3891116103,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712763744000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3891116103",
                  "posterId": "4784353",
                  "repostedJob": false,
                  "title": "Security Analyst I",
                  "trackingUrn": "urn:li:jobPosting:3891116103"
                },
                "jobPostingTitle": "Security Analyst I",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3891116103",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3891116103"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3891116103",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3891116103",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3891116103",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Dark Matter Technologies logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/darkmattertechnologies/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:98721845",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1694782294356?e=1721260800&v=beta&t=L197Unh0KzP2SUyygpjFXMjuTpet9J0QcVuULPCmvRA",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1694782294357?e=1721260800&v=beta&t=5cuSLl9GnlA_US_1-HgXVWMcd3OmpxHtXE0OZKiPNYY",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1694782294357?e=1721260800&v=beta&t=LyqF_HDmcnFfBTjxBSPyffkq5Ui6qUSUyeHwsSjjB9Y",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D4E0BAQGNs6D3RTb0NQ/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:98721845"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3891116103",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Security Analyst I job",
                        "accessibilityNameSelected": "Security Analyst I job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891116103"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891116103"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Dark Matter Technologies",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "401(k) benefit",
                  "textDirection": "USER_LOCALE"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 18,
                      "start": 0
                    }
                  ],
                  "text": "Security Analyst I",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "W1dZarbWIqWdegFWuylRuw=="
              },
              "job_title": "Security Analyst I",
              "job_urn": "urn:li:fsd_jobPosting:3891116103",
              "posted_time": "2024-04-10 15:42:24",
              "remote": "Remote",
              "salary": "401(k) benefit"
            },
            {
              "company": "Applied Systems logo",
              "company_linkedin_url": "https://www.linkedin.com/company/applied-systems/life",
              "company_logo": "https://media.licdn.com/dms/image/D4E0BAQElMFrJdKQjcw/company-logo_",
              "job_description": "Applied Systems",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3890867170,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712853570000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3890867170",
                  "posterId": "695639445",
                  "repostedJob": false,
                  "title": "Applications Administrator",
                  "trackingUrn": "urn:li:jobPosting:3890867170"
                },
                "jobPostingTitle": "Applications Administrator",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3890867170",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3890867170?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3890867170"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3890867170",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3890867170",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3890867170",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Applied Systems logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/applied-systems/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:162482",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1712244040021/applied_systems_logo?e=1721260800&v=beta&t=FpTOkV-O-pv0n190KmYLcSRFOgAWxu8Padb1RDCj3Wk",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1712244040021/applied_systems_logo?e=1721260800&v=beta&t=i4bQ-hz2xhgyiZKoJZq7I0lkdJZjVMMpT0C9QANnRV4",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1712244040021/applied_systems_logo?e=1721260800&v=beta&t=ijsgcffgC1QVouZoaspCjk3VBB25Y3UcJqfqpQJhQ6s",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D4E0BAQElMFrJdKQjcw/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:162482"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3890867170",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Applications Administrator job",
                        "accessibilityNameSelected": "Applications Administrator job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3890867170"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3890867170"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Applied Systems",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Medical, 401(k)",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 26,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 27
                    }
                  ],
                  "text": "Applications Administrator  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "Id/Qtr7VbWkjljw/S3bzXQ=="
              },
              "job_title": "Applications Administrator",
              "job_urn": "urn:li:fsd_jobPosting:3890867170",
              "posted_time": "2024-04-11 16:39:30",
              "remote": "Remote",
              "salary": "Medical, 401(k)"
            },
            {
              "company": "FinQuery, Formerly LeaseQuery logo",
              "company_linkedin_url": "https://www.linkedin.com/company/finquery/life",
              "company_logo": "https://media.licdn.com/dms/image/D4E0BAQE0d2eUCg7FBA/company-logo_",
              "job_description": "FinQuery, Formerly LeaseQuery",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3895210141,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712863859000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3895210141",
                  "posterId": "172893652",
                  "repostedJob": false,
                  "title": "Data Operations Intern",
                  "trackingUrn": "urn:li:jobPosting:3895210141"
                },
                "jobPostingTitle": "Data Operations Intern",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3895210141",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3895210141?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3895210141"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3895210141",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3895210141",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3895210141",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "FinQuery, Formerly LeaseQuery logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/finquery/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:3163130",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1707747860822/finquery_logo?e=1721260800&v=beta&t=KS_Zjo7rIbm5at9L37Fi9I9wQEyD4jAJm5GkdII0QPs",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1707747860823/finquery_logo?e=1721260800&v=beta&t=RCmlZEdsyH9iGEg64AmaEEJwqCXXH4_Xopxash_G91s",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1707747860823/finquery_logo?e=1721260800&v=beta&t=rtTtPhi_cp-FOH7ochLvERBBmwZQhNe3sYslEjnc-PE",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D4E0BAQE0d2eUCg7FBA/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:3163130"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3895210141",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Data Operations Intern job",
                        "accessibilityNameSelected": "Data Operations Intern job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895210141"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895210141"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "FinQuery, Formerly LeaseQuery",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 22,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 23
                    }
                  ],
                  "text": "Data Operations Intern  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "aC6MuBZzT+ruR8grvj5LbQ=="
              },
              "job_title": "Data Operations Intern",
              "job_urn": "urn:li:fsd_jobPosting:3895210141",
              "posted_time": "2024-04-11 19:30:59",
              "remote": "Remote",
              "salary": ""
            },
            {
              "company": "Natera logo",
              "company_linkedin_url": "https://www.linkedin.com/company/natera/life",
              "company_logo": "https://media.licdn.com/dms/image/C560BAQEz-66bMs5DFw/company-logo_",
              "job_description": "Natera",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3890050862,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712715519000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [],
                      "text": "Easy Apply",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "EASY_APPLY_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3890050862",
                  "posterId": "495055721",
                  "repostedJob": true,
                  "title": "Revenue Cycle Manager",
                  "trackingUrn": "urn:li:jobPosting:3890050862"
                },
                "jobPostingTitle": "Revenue Cycle Manager",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3890050862",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3890050862?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3890050862"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3890050862",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3890050862",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3890050862",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Natera logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/natera/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:1051903",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1630660562488/natera_logo?e=1721260800&v=beta&t=Tr1-hkTuglRv90lmg9rsLHRk7oHBIRsLtgJjvh4RtQI",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1630660562488/natera_logo?e=1721260800&v=beta&t=dFcDVM8AG9ws_tp8HPnuQzfCNEP6goyOwiqn4s159yA",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1630660562488/natera_logo?e=1721260800&v=beta&t=8XFlZcJQqZIPKTvnAoc1Ke7bMAUuW3WXe-Cd7HbaEq4",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C560BAQEz-66bMs5DFw/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:1051903"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3890050862",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Revenue Cycle Manager job",
                        "accessibilityNameSelected": "Revenue Cycle Manager job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3890050862"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3890050862"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Natera",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "401(k), +1 benefit",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 21,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 22
                    }
                  ],
                  "text": "Revenue Cycle Manager  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "shOUMB2UTtFyZ2in9CNW4Q=="
              },
              "job_title": "Revenue Cycle Manager",
              "job_urn": "urn:li:fsd_jobPosting:3890050862",
              "posted_time": "2024-04-10 02:18:39",
              "remote": "Remote",
              "salary": "401(k), +1 benefit"
            },
            {
              "company": "symplr logo",
              "company_linkedin_url": "https://www.linkedin.com/company/symplr/life",
              "company_logo": "https://media.licdn.com/dms/image/D4E0BAQHEDABaIXjkog/company-logo_",
              "job_description": "symplr",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3895559539,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712893939000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3895559539",
                  "posterId": "12838610",
                  "repostedJob": false,
                  "title": "Associate Solution Executive - Healthcare SaaS Sales",
                  "trackingUrn": "urn:li:jobPosting:3895559539"
                },
                "jobPostingTitle": "Associate Solution Executive - Healthcare SaaS Sales",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3895559539",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3895559539?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3895559539"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3895559539",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3895559539",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3895559539",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "symplr logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/symplr/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:5400751",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1688673323462/symplr_logo?e=1721260800&v=beta&t=1bKjtW0Vgf_COCRmfI0IFWG7HPLm0kZPF7gq8Ufwxo8",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1688673323463/symplr_logo?e=1721260800&v=beta&t=nFd5HXrlwyakMHMC-uzpO2Tbv2EFLmkpjTP5G1ynSXE",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1688673323463/symplr_logo?e=1721260800&v=beta&t=meOwGzA1J3dlpBRetXqs4ws_XTjYqaB8QePZuSRje3s",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D4E0BAQHEDABaIXjkog/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:5400751"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3895559539",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Associate Solution Executive - Healthcare SaaS Sales job",
                        "accessibilityNameSelected": "Associate Solution Executive - Healthcare SaaS Sales job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895559539"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895559539"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "symplr",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$60K/yr - $80K/yr",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 52,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 53
                    }
                  ],
                  "text": "Associate Solution Executive - Healthcare SaaS Sales  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "C6is+M5WbTxAJC0KNj5pGg=="
              },
              "job_title": "Associate Solution Executive - Healthcare SaaS Sales",
              "job_urn": "urn:li:fsd_jobPosting:3895559539",
              "posted_time": "2024-04-12 03:52:19",
              "remote": "Remote",
              "salary": "$60K/yr - $80K/yr"
            },
            {
              "company": "ClearCompany Talent Management Software logo",
              "company_linkedin_url": "https://www.linkedin.com/company/clearcompany-talent-management-software/life",
              "company_logo": "https://media.licdn.com/dms/image/D560BAQHkdV3XXevfAg/company-logo_",
              "job_description": "ClearCompany Talent Management Software",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3894427110,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712275200000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [
                        {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                          "detailDataUnion": {
                            "style": "BOLD"
                          },
                          "length": 13,
                          "start": 0
                        },
                        {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                          "detailDataUnion": {
                            "color": "POSITIVE"
                          },
                          "length": 13,
                          "start": 0
                        }
                      ],
                      "text": "11 applicants",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "APPLICANT_COUNT_TEXT"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [],
                      "text": "Easy Apply",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "EASY_APPLY_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_CREATE",
                  "entityUrn": "urn:li:fsd_jobPosting:3894427110",
                  "repostedJob": false,
                  "title": "Client Support Specialist, Tier 1",
                  "trackingUrn": "urn:li:jobPosting:3894427110"
                },
                "jobPostingTitle": "Client Support Specialist, Tier 1",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3894427110",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3894427110"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3894427110",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3894427110",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3894427110",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "ClearCompany Talent Management Software logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/clearcompany-talent-management-software/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:2944518",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1688221192697?e=1721260800&v=beta&t=q9b25_Z_i9kqA9SAxq0ItGzOCl3LqlA4FOCmuItflRc",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1688221192697?e=1721260800&v=beta&t=XzNQPH5OFRC9x-KBHAX1pdM59Ryjr3LRF9qNFd305As",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1688221192697?e=1721260800&v=beta&t=8Rp5tswdJDZ0HwUBqG9YVH2tpxwXBy_RO7LqbGuBlNA",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D560BAQHkdV3XXevfAg/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:2944518"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3894427110",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Client Support Specialist, Tier 1 job",
                        "accessibilityNameSelected": "Client Support Specialist, Tier 1 job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3894427110"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3894427110"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "ClearCompany Talent Management Software",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "401(k) benefit",
                  "textDirection": "USER_LOCALE"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 33,
                      "start": 0
                    }
                  ],
                  "text": "Client Support Specialist, Tier 1",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "leb8pGQElklJT08lSASqeg=="
              },
              "job_title": "Client Support Specialist, Tier 1",
              "job_urn": "urn:li:fsd_jobPosting:3894427110",
              "posted_time": "2024-04-05 00:00:00",
              "remote": "Remote",
              "salary": "401(k) benefit"
            },
            {
              "company": "Businessolver logo",
              "company_linkedin_url": "https://www.linkedin.com/company/businessolver/life",
              "company_logo": "https://media.licdn.com/dms/image/D560BAQEM2twhMn-nPA/company-logo_",
              "job_description": "Businessolver",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3891585656,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712700085000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3891585656",
                  "posterId": "1420015",
                  "repostedJob": false,
                  "title": "Client Services Manager (100% remote)",
                  "trackingUrn": "urn:li:jobPosting:3891585656"
                },
                "jobPostingTitle": "Client Services Manager (100% remote)",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3891585656",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3891585656?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3891585656"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3891585656",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3891585656",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3891585656",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Businessolver logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/businessolver/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:232793",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1705503775149/businessolver_logo?e=1721260800&v=beta&t=o9EZLUqOIa9kTjlS65K2TBTQ6cehccVMOmcUAcKHHvA",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1705503775149/businessolver_logo?e=1721260800&v=beta&t=C7aawQoBVnN0UVrQdoDw000xmDdC0XNCboCwsGRm3DM",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1705503775149/businessolver_logo?e=1721260800&v=beta&t=jfsqtRJLQBEtiDxt5H7Zcn_lA1DuIuBuSF2LabnewVc",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D560BAQEM2twhMn-nPA/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:232793"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3891585656",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Client Services Manager (100% remote) job",
                        "accessibilityNameSelected": "Client Services Manager (100% remote) job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891585656"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891585656"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Businessolver",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$60K/yr - $119K/yr",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 37,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 38
                    }
                  ],
                  "text": "Client Services Manager (100% remote)  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "xsl+Eg6wKNGOuXeACaa2sA=="
              },
              "job_title": "Client Services Manager (100% remote)",
              "job_urn": "urn:li:fsd_jobPosting:3891585656",
              "posted_time": "2024-04-09 22:01:25",
              "remote": "Remote",
              "salary": "$60K/yr - $119K/yr"
            },
            {
              "company": "Dice logo",
              "company_linkedin_url": "https://www.linkedin.com/company/dice/life",
              "company_logo": "https://media.licdn.com/dms/image/C560BAQEYK67Tel_mng/company-logo_",
              "job_description": "Dice",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3894357828,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712849477000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3894357828",
                  "posterId": "1307337",
                  "repostedJob": false,
                  "title": "Help Desk - REMOTE",
                  "trackingUrn": "urn:li:jobPosting:3894357828"
                },
                "jobPostingTitle": "Help Desk - REMOTE",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3894357828",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3894357828"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3894357828",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3894357828",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3894357828",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Dice logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/dice/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:6849",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1630655500596/dice_logo?e=1721260800&v=beta&t=Ow7oL1UUgtkfrtI-27aJGeA9EeRJ9iRFdlFhAq2w_Sc",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1630655500596/dice_logo?e=1721260800&v=beta&t=2J1QWCBW0-gSWVUZMlGQDFV1TXh5bLgR_eIfzgJrngM",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1630655500596/dice_logo?e=1721260800&v=beta&t=-J570FGo2f0TQh0fV16k2Pt13ze_NRIPmP9nIsdeIew",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C560BAQEYK67Tel_mng/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:6849"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3894357828",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Help Desk - REMOTE job",
                        "accessibilityNameSelected": "Help Desk - REMOTE job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3894357828"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3894357828"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Dice",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 18,
                      "start": 0
                    }
                  ],
                  "text": "Help Desk - REMOTE",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "RsFATQ1x2o0cVkKjCrEe1A=="
              },
              "job_title": "Help Desk - REMOTE",
              "job_urn": "urn:li:fsd_jobPosting:3894357828",
              "posted_time": "2024-04-11 15:31:17",
              "remote": "Remote",
              "salary": ""
            },
            {
              "company": "Rippling logo",
              "company_linkedin_url": "https://www.linkedin.com/company/rippling/life",
              "company_logo": "https://media.licdn.com/dms/image/C560BAQGTg3igNET25Q/company-logo_",
              "job_description": "Rippling",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3895273625,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712869943000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3895273625",
                  "posterId": "289172954",
                  "repostedJob": false,
                  "title": "Customer Support Specialist",
                  "trackingUrn": "urn:li:jobPosting:3895273625"
                },
                "jobPostingTitle": "Customer Support Specialist",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3895273625",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3895273625?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3895273625"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3895273625",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3895273625",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3895273625",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Rippling logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/rippling/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:17988315",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1654722845874/rippling_logo?e=1721260800&v=beta&t=uJV0FGqXG1udQCPvLJUUOnPN8ghSdqt5P8IAccH4yXo",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1654722845874/rippling_logo?e=1721260800&v=beta&t=vjEPzxbWgEi_jdneLKopncrF3guO8VBO1f5AempwcVE",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1654722845874/rippling_logo?e=1721260800&v=beta&t=UB3yyTKi6eLzXxHJXi2gH_UhOvHi7XWjR-NS6GI_yGM",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C560BAQGTg3igNET25Q/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:17988315"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3895273625",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Customer Support Specialist job",
                        "accessibilityNameSelected": "Customer Support Specialist job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895273625"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895273625"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Rippling",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "San Francisco, CA (Hybrid)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$22/hr - $23/hr",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 27,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 28
                    }
                  ],
                  "text": "Customer Support Specialist  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "cQkmMWqrZDrnNZYrxgJ5ug=="
              },
              "job_title": "Customer Support Specialist",
              "job_urn": "urn:li:fsd_jobPosting:3895273625",
              "posted_time": "2024-04-11 21:12:23",
              "remote": "Hybrid",
              "salary": "$22/hr - $23/hr"
            },
            {
              "company": "HireVue logo",
              "company_linkedin_url": "https://www.linkedin.com/company/hirevue/life",
              "company_logo": "https://media.licdn.com/dms/image/C4E0BAQG378CTFFjnEw/company-logo_",
              "job_description": "HireVue",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3891615985,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712701847000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [],
                      "text": "Easy Apply",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "EASY_APPLY_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3891615985",
                  "posterId": "449263414",
                  "repostedJob": false,
                  "title": "Staff Accountant - International | Fully Remote USA",
                  "trackingUrn": "urn:li:jobPosting:3891615985"
                },
                "jobPostingTitle": "Staff Accountant - International | Fully Remote USA",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3891615985",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3891615985"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3891615985",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3891615985",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3891615985",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "HireVue logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/hirevue/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:134703",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1630613073886/hirevue_logo?e=1721260800&v=beta&t=cTAvHQTOT5rea9YDmbcGXoztZflzA6KUYfjXeZRVcxE",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1630613073886/hirevue_logo?e=1721260800&v=beta&t=8eKU7UI_J1dMpYAdRFBYTaOk2vWP38u_k5ouq4p90ek",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1630613073886/hirevue_logo?e=1721260800&v=beta&t=-jNHzomWUDyyDOFY6KO8XItMxU_gqFqlJvGFK4SJIJw",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C4E0BAQG378CTFFjnEw/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:134703"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3891615985",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Staff Accountant - International | Fully Remote USA job",
                        "accessibilityNameSelected": "Staff Accountant - International | Fully Remote USA job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891615985"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891615985"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "HireVue",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "South Jordan, UT (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "401(k) benefit",
                  "textDirection": "USER_LOCALE"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 51,
                      "start": 0
                    }
                  ],
                  "text": "Staff Accountant - International | Fully Remote USA",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "2OcAIoqN9wm7Q8LNiBDEpg=="
              },
              "job_title": "Staff Accountant - International | Fully Remote USA",
              "job_urn": "urn:li:fsd_jobPosting:3891615985",
              "posted_time": "2024-04-09 22:30:47",
              "remote": "Remote",
              "salary": "401(k) benefit"
            },
            {
              "company": "Businessolver logo",
              "company_linkedin_url": "https://www.linkedin.com/company/businessolver/life",
              "company_logo": "https://media.licdn.com/dms/image/D560BAQEM2twhMn-nPA/company-logo_",
              "job_description": "Businessolver",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3895415102,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712872888000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3895415102",
                  "posterId": "1420015",
                  "repostedJob": false,
                  "title": "Accounts Receivable Specialist",
                  "trackingUrn": "urn:li:jobPosting:3895415102"
                },
                "jobPostingTitle": "Accounts Receivable Specialist",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3895415102",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3895415102?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3895415102"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3895415102",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3895415102",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3895415102",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Businessolver logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/businessolver/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:232793",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1705503775149/businessolver_logo?e=1721260800&v=beta&t=o9EZLUqOIa9kTjlS65K2TBTQ6cehccVMOmcUAcKHHvA",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1705503775149/businessolver_logo?e=1721260800&v=beta&t=C7aawQoBVnN0UVrQdoDw000xmDdC0XNCboCwsGRm3DM",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1705503775149/businessolver_logo?e=1721260800&v=beta&t=jfsqtRJLQBEtiDxt5H7Zcn_lA1DuIuBuSF2LabnewVc",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D560BAQEM2twhMn-nPA/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:232793"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3895415102",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Accounts Receivable Specialist job",
                        "accessibilityNameSelected": "Accounts Receivable Specialist job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895415102"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895415102"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Businessolver",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 30,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 31
                    }
                  ],
                  "text": "Accounts Receivable Specialist  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "D+11365Q2oC74uQ94Ms1mg=="
              },
              "job_title": "Accounts Receivable Specialist",
              "job_urn": "urn:li:fsd_jobPosting:3895415102",
              "posted_time": "2024-04-11 22:01:28",
              "remote": "Remote",
              "salary": ""
            },
            {
              "company": "Amity logo",
              "company_linkedin_url": "https://www.linkedin.com/company/amity-hq/life",
              "company_logo": "https://media.licdn.com/dms/image/D4E0BAQEBkkMnPq3qrA/company-logo_",
              "job_description": "Amity",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3895254739,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712867725000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3895254739",
                  "posterId": "352628319",
                  "repostedJob": false,
                  "title": "Junior Inbound Sales Development Representative (SDR)",
                  "trackingUrn": "urn:li:jobPosting:3895254739"
                },
                "jobPostingTitle": "Junior Inbound Sales Development Representative (SDR)",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3895254739",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3895254739"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3895254739",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3895254739",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3895254739",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Amity logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/amity-hq/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:68217401",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1712739030767/amity_hq_logo?e=1721260800&v=beta&t=PYArkJNmtMAIRDfUrWWefj58Zn_dTwkAYXGjaVDqjcc",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1712739030767/amity_hq_logo?e=1721260800&v=beta&t=4KZViuf7aW6z4LuSudJ6TzuqZOkiUo-thHoBe5khgBc",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1712739030767/amity_hq_logo?e=1721260800&v=beta&t=JIzmRCNT4ddRtt6cYldcyZ3uYQDnmFYbO6fawQUWJXM",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D4E0BAQEBkkMnPq3qrA/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:68217401"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3895254739",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Junior Inbound Sales Development Representative (SDR) job",
                        "accessibilityNameSelected": "Junior Inbound Sales Development Representative (SDR) job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895254739"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3895254739"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Amity",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "New Haven, CT (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Medical benefit",
                  "textDirection": "USER_LOCALE"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 53,
                      "start": 0
                    }
                  ],
                  "text": "Junior Inbound Sales Development Representative (SDR)",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "NURYNxjzc5r+19zQfYYMhQ=="
              },
              "job_title": "Junior Inbound Sales Development Representative (SDR)",
              "job_urn": "urn:li:fsd_jobPosting:3895254739",
              "posted_time": "2024-04-11 20:35:25",
              "remote": "Remote",
              "salary": "Medical benefit"
            },
            {
              "company": "WEX logo",
              "company_linkedin_url": "https://www.linkedin.com/company/wexinc/life",
              "company_logo": "https://media.licdn.com/dms/image/D560BAQFhAT_f2S08EQ/company-logo_",
              "job_description": "WEX",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3893352125,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712784968000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3893352125",
                  "posterId": "477251714",
                  "repostedJob": false,
                  "title": "Client Service Analyst",
                  "trackingUrn": "urn:li:jobPosting:3893352125"
                },
                "jobPostingTitle": "Client Service Analyst",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3893352125",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3893352125?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3893352125"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3893352125",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3893352125",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3893352125",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "WEX logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/wexinc/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:11637",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1699284516534/wexinc_logo?e=1721260800&v=beta&t=s8nheZu12fMg9ZxXq2WkWz3pstSo83jyL15riv_-cy0",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1699284516534/wexinc_logo?e=1721260800&v=beta&t=oT8yuXdb1ANSVhoKUq8JSmPU8tlxoiEw7DmZ2VxEbN0",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1699284516534/wexinc_logo?e=1721260800&v=beta&t=PUbizlLZq0NsHPCChBXemgFRkaTYn92kSX90G1oEEp0",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D560BAQFhAT_f2S08EQ/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:11637"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3893352125",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Client Service Analyst job",
                        "accessibilityNameSelected": "Client Service Analyst job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3893352125"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3893352125"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "WEX",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$16/hr - $21/hr · 1 benefit",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 22,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 23
                    }
                  ],
                  "text": "Client Service Analyst  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "sBaU42UR2C9ucSSGCgXbUA=="
              },
              "job_title": "Client Service Analyst",
              "job_urn": "urn:li:fsd_jobPosting:3893352125",
              "posted_time": "2024-04-10 21:36:08",
              "remote": "Remote",
              "salary": "$16/hr - $21/hr · 1 benefit"
            },
            {
              "company": "Intact Insurance Specialty Solutions logo",
              "company_linkedin_url": "https://www.linkedin.com/company/intact-insurance-specialty-solutions/life",
              "company_logo": "https://media.licdn.com/dms/image/D560BAQGxfqzYOjCVVw/company-logo_",
              "job_description": "Intact Insurance Specialty Solutions",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3892438965,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712275200000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [
                        {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                          "detailDataUnion": {
                            "style": "BOLD"
                          },
                          "length": 12,
                          "start": 0
                        },
                        {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                          "detailDataUnion": {
                            "color": "POSITIVE"
                          },
                          "length": 12,
                          "start": 0
                        }
                      ],
                      "text": "6 applicants",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "APPLICANT_COUNT_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_CREATE",
                  "entityUrn": "urn:li:fsd_jobPosting:3892438965",
                  "repostedJob": false,
                  "title": "Claim Representative (Hybrid or Remote)",
                  "trackingUrn": "urn:li:jobPosting:3892438965"
                },
                "jobPostingTitle": "Claim Representative (Hybrid or Remote)",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3892438965",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3892438965"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3892438965",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3892438965",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3892438965",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Intact Insurance Specialty Solutions logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/intact-insurance-specialty-solutions/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:42117012",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1688561399967/intact_insurance_specialty_solutions_logo?e=1721260800&v=beta&t=Y7QQuBHtSjs2WAT7UL-hvk0LJSl3TY6dKCZIm5SCtes",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1688561399967/intact_insurance_specialty_solutions_logo?e=1721260800&v=beta&t=gA_189m30E-SlYDtthQIkhKbZZPFeSFz1jHOxfMyhCw",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1688561399967/intact_insurance_specialty_solutions_logo?e=1721260800&v=beta&t=N95xia2KYqYyFlsEMv5DF3iDBEeaDcDPFzfRkQ83dvk",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D560BAQGxfqzYOjCVVw/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:42117012"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3892438965",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Claim Representative (Hybrid or Remote) job",
                        "accessibilityNameSelected": "Claim Representative (Hybrid or Remote) job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3892438965"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3892438965"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Intact Insurance Specialty Solutions",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$60K/yr - $88K/yr · 401(k), +1 benefit",
                  "textDirection": "USER_LOCALE"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 39,
                      "start": 0
                    }
                  ],
                  "text": "Claim Representative (Hybrid or Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "b6SzhhhDti90RK5hTCl53g=="
              },
              "job_title": "Claim Representative (Hybrid or Remote)",
              "job_urn": "urn:li:fsd_jobPosting:3892438965",
              "posted_time": "2024-04-05 00:00:00",
              "remote": "Remote",
              "salary": "$60K/yr - $88K/yr · 401(k), +1 benefit"
            },
            {
              "company": "Workling logo",
              "company_linkedin_url": "https://www.linkedin.com/company/workling-jobs/life",
              "company_logo": "https://media.licdn.com/dms/image/C560BAQEznWRrO24Vzw/company-logo_",
              "job_description": "Workling",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3891079986,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712866834000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [],
                      "text": "Easy Apply",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "EASY_APPLY_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3891079986",
                  "posterId": "1016390884",
                  "repostedJob": false,
                  "title": "Work From Home Sales Associate",
                  "trackingUrn": "urn:li:jobPosting:3891079986"
                },
                "jobPostingTitle": "Work From Home Sales Associate",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3891079986",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3891079986"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3891079986",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3891079986",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3891079986",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Workling logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/workling-jobs/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:53237848",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1641945371362/workling_jobs_logo?e=1721260800&v=beta&t=38KCKvP3Wbn-W9gTwe-2TVGtK4pMMRz4IvE5TS4j3tw",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1641945371362/workling_jobs_logo?e=1721260800&v=beta&t=ZMTUw_Utfzz4toqFd7q3KnPEW8frYohxyI0tKBmpJJk",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1641945371362/workling_jobs_logo?e=1721260800&v=beta&t=_IkvcT778_tUc6DINjPJzHj9el8OdFzoykp9QSNPsP8",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C560BAQEznWRrO24Vzw/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:53237848"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3891079986",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Work From Home Sales Associate job",
                        "accessibilityNameSelected": "Work From Home Sales Associate job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891079986"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891079986"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Workling",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Dallas, TX (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$5,000/yr - $600K/yr",
                  "textDirection": "USER_LOCALE"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 30,
                      "start": 0
                    }
                  ],
                  "text": "Work From Home Sales Associate",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "rphSi3IVQBjaD7bSzHQWpg=="
              },
              "job_title": "Work From Home Sales Associate",
              "job_urn": "urn:li:fsd_jobPosting:3891079986",
              "posted_time": "2024-04-11 20:20:34",
              "remote": "Remote",
              "salary": "$5,000/yr - $600K/yr"
            },
            {
              "company": "Workling logo",
              "company_linkedin_url": "https://www.linkedin.com/company/workling-jobs/life",
              "company_logo": "https://media.licdn.com/dms/image/C560BAQEznWRrO24Vzw/company-logo_",
              "job_description": "Workling",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3891084671,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712867258000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [],
                      "text": "Easy Apply",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "EASY_APPLY_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3891084671",
                  "posterId": "1016390884",
                  "repostedJob": false,
                  "title": "Work From Home Client Relations Representative",
                  "trackingUrn": "urn:li:jobPosting:3891084671"
                },
                "jobPostingTitle": "Work From Home Client Relations Representative",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3891084671",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3891084671"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3891084671",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3891084671",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3891084671",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Workling logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/workling-jobs/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:53237848",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1641945371362/workling_jobs_logo?e=1721260800&v=beta&t=38KCKvP3Wbn-W9gTwe-2TVGtK4pMMRz4IvE5TS4j3tw",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1641945371362/workling_jobs_logo?e=1721260800&v=beta&t=ZMTUw_Utfzz4toqFd7q3KnPEW8frYohxyI0tKBmpJJk",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1641945371362/workling_jobs_logo?e=1721260800&v=beta&t=_IkvcT778_tUc6DINjPJzHj9el8OdFzoykp9QSNPsP8",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/C560BAQEznWRrO24Vzw/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:53237848"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3891084671",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Work From Home Client Relations Representative job",
                        "accessibilityNameSelected": "Work From Home Client Relations Representative job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891084671"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3891084671"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Workling",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Houston, TX (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$5,000/yr - $60K/yr",
                  "textDirection": "USER_LOCALE"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 46,
                      "start": 0
                    }
                  ],
                  "text": "Work From Home Client Relations Representative",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "4dJWbUC36uIYBqfqGn0SOg=="
              },
              "job_title": "Work From Home Client Relations Representative",
              "job_urn": "urn:li:fsd_jobPosting:3891084671",
              "posted_time": "2024-04-11 20:27:38",
              "remote": "Remote",
              "salary": "$5,000/yr - $60K/yr"
            },
            {
              "company": "Blend logo",
              "company_linkedin_url": "https://www.linkedin.com/company/blend-/life",
              "company_logo": "https://media.licdn.com/dms/image/D560BAQFSVLD-zJ-9jQ/company-logo_",
              "job_description": "Blend",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3889054754,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712707200000,
                    "type": "LISTED_DATE"
                  },
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "text": {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                      "attributesV2": [
                        {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                          "detailDataUnion": {
                            "style": "BOLD"
                          },
                          "length": 12,
                          "start": 0
                        },
                        {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                          "detailDataUnion": {
                            "color": "POSITIVE"
                          },
                          "length": 12,
                          "start": 0
                        }
                      ],
                      "text": "0 applicants",
                      "textDirection": "USER_LOCALE"
                    },
                    "type": "APPLICANT_COUNT_TEXT"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_CREATE",
                  "entityUrn": "urn:li:fsd_jobPosting:3889054754",
                  "repostedJob": false,
                  "title": "Insurance Client Advisor",
                  "trackingUrn": "urn:li:jobPosting:3889054754"
                },
                "jobPostingTitle": "Insurance Client Advisor",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3889054754",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "attributes": []
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3889054754"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3889054754",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3889054754",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3889054754",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Blend logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/blend-/life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:3280260",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1688401102918/blend__logo?e=1721260800&v=beta&t=qkvB4aBKiJhcmVZDIKSGp87go0U7yBwx9rOb958pXwU",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1688401102918/blend__logo?e=1721260800&v=beta&t=tp3krVPFM4Hegt-iFcuw9NFANdKYTp2LHT20gY6Dt7k",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1688401102918/blend__logo?e=1721260800&v=beta&t=AsBppaZJxpapQsKhSXPBhMJanwL-IeCuEr3mej5pd18",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D560BAQFSVLD-zJ-9jQ/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:3280260"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3889054754",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Insurance Client Advisor job",
                        "accessibilityNameSelected": "Insurance Client Advisor job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3889054754"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3889054754"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Blend",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "United States (Remote)",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$26.92/hr - $30/hr · 401(k) benefit",
                  "textDirection": "USER_LOCALE"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 24,
                      "start": 0
                    }
                  ],
                  "text": "Insurance Client Advisor",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "Kucw1unskYwWYqpnRD5dpQ=="
              },
              "job_title": "Insurance Client Advisor",
              "job_urn": "urn:li:fsd_jobPosting:3889054754",
              "posted_time": "2024-04-10 00:00:00",
              "remote": "Remote",
              "salary": "$26.92/hr - $30/hr · 401(k) benefit"
            },
            {
              "company": "Harris Computer logo",
              "company_linkedin_url": "https://www.linkedin.com/company/harris-computer./life",
              "company_logo": "https://media.licdn.com/dms/image/D4E0BAQGQoeSrD6yzYw/company-logo_",
              "job_description": "Harris Computer",
              "job_info": {
                "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1317657387",
                "encryptedBiddingParameters": "NOT_ELIGIBLE_FOR_CHARGING",
                "entityUrn": "urn:li:fsd_jobPostingCard:(3894400193,JOBS_SEARCH)",
                "footerItems": [
                  {
                    "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1254114640",
                    "timeAt": 1712866263000,
                    "type": "LISTED_DATE"
                  }
                ],
                "jobPosting": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1578943416",
                  "contentSource": "JOBS_PREMIUM_OFFLINE",
                  "entityUrn": "urn:li:fsd_jobPosting:3894400193",
                  "posterId": "192689584",
                  "repostedJob": false,
                  "title": "Support Analyst",
                  "trackingUrn": "urn:li:jobPosting:3894400193"
                },
                "jobPostingTitle": "Support Analyst",
                "jobPostingUrn": "urn:li:fsd_jobPosting:3894400193",
                "jobPostingVerification": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2036323012",
                  "badge": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                    "actionTarget": "https://www.linkedin.com/jobs/view/3894400193?openBottomSheet=verifiedHiringV2",
                    "attributes": [
                      {
                        "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                        "detailDataUnion": {
                          "systemImage": "SYS_ICN_VERIFIED_MEDIUM"
                        }
                      }
                    ]
                  },
                  "controlName": "verification_show_all",
                  "entityUrn": "urn:li:fsd_jobPostingVerification:3894400193"
                },
                "jobPostingVerificationUrn": "urn:li:fsd_jobPostingVerification:3894400193",
                "jobSeekerJobState": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon94463982",
                  "entityUrn": "urn:li:fsd_jobSeekerJobState:3894400193",
                  "jobSeekerJobStateActions": []
                },
                "jobSeekerJobStateUrn": "urn:li:fsd_jobSeekerJobState:3894400193",
                "logo": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageViewModel",
                  "accessibilityText": "Harris Computer logo",
                  "accessibilityTextAttributes": [],
                  "actionTarget": "https://www.linkedin.com/company/harris-computer./life",
                  "attributes": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.image.ImageAttribute",
                      "detailData": {
                        "companyLogo": {
                          "$recipeType": "com.linkedin.voyager.dash.deco.common.image.Company",
                          "entityUrn": "urn:li:fsd_company:13524",
                          "logo": {
                            "vectorImage": {
                              "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution",
                              "artifacts": [
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "200_200/0/1690316235316/harris_computer_logo?e=1721260800&v=beta&t=0B6gMZKlmVVYMOAJzkJ47rQFiAlYCT2QLCuW5hG_UuQ",
                                  "height": 200,
                                  "width": 200
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "100_100/0/1690316235316/harris_computer_logo?e=1721260800&v=beta&t=umS51Qx1iJy1_hajva76IoCXNtYYeFrvaxCe9woJ2vk",
                                  "height": 100,
                                  "width": 100
                                },
                                {
                                  "$recipeType": "com.linkedin.voyager.dash.deco.common.VectorArtifact",
                                  "expiresAt": 1721260800000,
                                  "fileIdentifyingUrlPathSegment": "400_400/0/1690316235316/harris_computer_logo?e=1721260800&v=beta&t=wGCcoXPtT8TjsBddCvDvwIPq9NEs2wE1g2E3zkQdBCU",
                                  "height": 400,
                                  "width": 400
                                }
                              ],
                              "rootUrl": "https://media.licdn.com/dms/image/D4E0BAQGQoeSrD6yzYw/company-logo_"
                            }
                          }
                        }
                      },
                      "detailDataUnion": {
                        "companyLogo": "urn:li:fsd_company:13524"
                      }
                    }
                  ]
                },
                "preDashNormalizedJobPostingUrn": "urn:li:fs_normalized_jobPosting:3894400193",
                "primaryActionsUnions": [
                  {
                    "dismissJobAction": {
                      "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon221142415",
                      "channel": "JOB_SEARCH",
                      "dismissControlName": "jobs_search_job_action_dismiss",
                      "dismissUndoControlName": "jobs_search_job_action_dismiss_undo",
                      "jobActionInfo": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon1847657914",
                        "accessibilityNameDefault": "Dismiss Support Analyst job",
                        "accessibilityNameSelected": "Support Analyst job is dismissed, undo",
                        "controlNameDefault": "jobs_search_job_action_dismiss",
                        "controlNameSelected": "jobs_search_job_action_dismiss_undo",
                        "iconDefault": "SYS_ICN_CLOSE_SMALL",
                        "iconSelected": "SYS_ICN_UNDO_SMALL"
                      },
                      "jobPostingRelevanceFeedback": {
                        "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon454131792",
                        "dismissed": false,
                        "entityUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3894400193"
                      },
                      "jobPostingRelevanceFeedbackUrn": "urn:li:fsd_jobPostingRelevanceFeedback:urn:li:fsd_jobPosting:3894400193"
                    }
                  }
                ],
                "primaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "Harris Computer",
                  "textDirection": "USER_LOCALE"
                },
                "referenceId": "C+wbo4u1Fy7rHS8MF8I9Ug==",
                "secondaryActionsV2": [],
                "secondaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "New York, United States",
                  "textDirection": "USER_LOCALE"
                },
                "tertiaryActionsV2": [],
                "tertiaryDescription": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [],
                  "text": "$50K/yr - $75K/yr · Medical, 401(k)",
                  "textDirection": "USER_LOCALE"
                },
                "tip": {
                  "$recipeType": "com.linkedin.deco.recipe.anonymous.Anon2050407127",
                  "legoTrackingToken": "cjRBuCBjum5Is7dFp2oMbz0Zpn9LoRdT9zROol1Ipl9T9zRArQRIpl9T9zkZp6lQsSlRsmlirnlK9AVfilh9kQZgfnB2sClAsAZQpmtAqnsCs6BQnSVLqnhxoSBCqn9BtBZIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQpmtAqnsCc3RKrSBQqndLk7hBpShFtOoMbz0Zpn9LoRdOpOoZsC5gr6lisCsCfmhLjmNBkD9D9z0ZrCZFt6BPrR1MtmZOpOoNfmhBt7dBtn5BkCRRjD1RrT9D9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DdIomhLrlZMqnhvpSVFt7dLs5ZyrSEZp4BQrSNP9DhItm5CpmgZp4BQtmZVomMCs6BQnStKqnhPrT1voCZGfmlJokVBpS5M9D9BpS5VrToZp4BMs64CdzoQdP8Nfmh9rCZFsT9BtyoVdPcOejASdz4Nfmh9tioMe3sSejhycz0Toz8JpC9xoyQOpjgQbjkVdCkJcS4Rp39Cem8Zp4BQu6lQrCZz",
                  "text": {
                    "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                    "attributesV2": [],
                    "text": "To view company or job poster verifications, click the badge next to the job title.",
                    "textDirection": "USER_LOCALE"
                  },
                  "type": "VERIFICATION_TIP",
                  "viewImpressionTrackingKey": "job_posting_verification_tip"
                },
                "title": {
                  "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextViewModelV2",
                  "attributesV2": [
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "style": "BOLD"
                      },
                      "length": 15,
                      "start": 0
                    },
                    {
                      "$recipeType": "com.linkedin.voyager.dash.deco.common.text.TextAttributeV2",
                      "detailDataUnion": {
                        "systemImage": "SYS_ICN_VERIFIED_SMALL"
                      },
                      "length": 1,
                      "start": 16
                    }
                  ],
                  "text": "Support Analyst  ",
                  "textDirection": "USER_LOCALE"
                },
                "trackingId": "C7IuiD9trGga1GMcbNngeA=="
              },
              "job_title": "Support Analyst",
              "job_urn": "urn:li:fsd_jobPosting:3894400193",
              "posted_time": "2024-04-11 20:11:03",
              "remote": "New York, United States",
              "salary": "$50K/yr - $75K/yr · Medical, 401(k)"
            }
          ],
          "message": "ok",
          "total": 72089
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Job Details
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-job-details') and
            i.nice_name == "Get Job Details")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "company_description": "Building a Healthier Future\n\nOur mission is to improve the health, vitality, and longevity of human beings through bioengineering.\n\nWho We Are\nAt Ossium, we believe that science is humanity’s best weapon in the fight against disease, and we embrace the challenge of mobilizing the world’s healthcare ecosystem to win that fight. In pursuit of this goal, we empower our employees, maintain the highest standards of excellence, and are a force for good.\n\nPRINCIPLES\n\nThe values we live by\n\nImpact\nWe are mission-driven and results-oriented. We believe that a healthier world is a better one and that our work should drive positive change.\n\nTruth\nEmbracing the truth empowers us to learn from both our successes and our mistakes. We follow the data wherever it leads.\n\nOwnership\nWe hold ourselves and each other to the highest bar. We care deeply about the work we do and know that even the smallest details can make a difference.",
            "company_id": "18940375",
            "company_linkedin_url": "https://www.linkedin.com/company/ossiumhealth",
            "company_name": "Ossium Health",
            "company_public_id": "ossiumhealth",
            "employee_count": 87,
            "employee_range": "51 - 200",
            "experience_level": "Mid-Senior level",
            "follower_count": 1969,
            "hq_address_line1": "80 Tehama St",
            "hq_address_line2": null,
            "hq_city": "San Francisco",
            "hq_country": "US",
            "hq_full_address": "80 Tehama St, San Francisco, California 94105, US",
            "hq_postalcode": "94105",
            "hq_region": "California",
            "industries": [
              "Biotechnology Research"
            ],
            "job_description": "Ossium’s mission is to improve the health, vitality, and longevity of human beings through bioengineering. We develop, manufacture, and bank cell therapy products that apply the power of stem cell science to revolutionize treatment for patients with blood and immune diseases. At Ossium, we empower our employees, maintain the highest standards of operational excellence, and are a force for good.\nAbout The Job\nWe’re looking for a motivated, high achieving, and versatile individual who will play an essential role in a broad range of activities necessary to drive and execute critical operational and strategic aspects of our growing company. You’ll get an unparalleled view into the inner workings of Ossium as you help develop go-to-market strategies, own products’ financial models, develop materials based on market research and product strategy, and assist on various projects across many of Ossium’s verticals. The Business Strategist will be responsible for helping us tell the story of Ossium – both internally and externally – through metrics, decks, one pagers, and other materials.\nYou’ll have the opportunity to project manage essential external clinical and business partnerships and work closely with many members of Ossium’s leadership team as we continue to scale. The Business Strategist will be exposed to many of the highest-priority workstreams and projects at Ossium—to be successful in this role, you must realize that no task is too small; ego and deadlines are the only enemies here. You will report directly to the CEO.\nRequired Qualifications\nA bachelor’s degree in life science, bioengineering, or a related field2+ years of experience in management consulting, business development, investment banking, or data & analytics, preferably in a life science and/or healthcare-related company or practiceStrong sense of ownership and excellent project management skills, with hands-on experience managing multiple projects concurrentlyRobust problem-solving skills and the ability to apply logical frameworks and data-driven insights to ambiguous situationsComfortable operating both at the board level and at the administrative and tactical levels, handling whatever is required to support the CEO and the broader Ossium agenda Excellent written and oral communication skills, including making and delivering dynamic presentations in PowerPoint, synthesizing findings, and drafting external communications and internal reportsStrong quantitative skills, including the ability to value market opportunities, navigate financial models, and analyze and interpret statistical data; strong Excel skillsCapable of operating with a high level of organization and excellent time management in a startup environmentMust show rigorous attention to detail in work productThis position is based in our San Francisco office; we maintain a hybrid schedule of Monday - Thursday in the office, with Friday as a remote work day\nPreferred Qualifications\nExperience at a high-growth startupA familiarity with the drug development and commercialization landscapeInterest in trends, advancements, and news in the biotech and pharmaceutical space\nKey Responsibilities\nProvide general leverage and support to the CEO and executive team, including managing a broad range of internal and external facing projects as required in a startup environmentAct as Ossium’s internal consultant, working cross-functionally with members of the Ossium leadership team on key business projectsAct as a link with executive leaders to acquire and formulate the information and data necessary to develop content for the Board of Directors meetingsOversee and assist with various internal operations and activities, such as taking notes for leadership meetings, developing content for All Hands programming, and helping to design bi-annual leadership retreatsCreate, track, and report on KPIs across the companyDevelop a keen understanding of product-market fit for multiple product lines through data analysis and market research and clearly communicate findings to executive teamWork at the intersection of product, data analysis, and marketing to ensure Ossium understands business opportunities and new products reach the correct audienceProvide up-to-date assessments of the broader biotech competitive landscape and keep the organization apprised of the latest developments and their potential impact to OssiumProduce materials that contribute to the development of the company’s brand and imageDrive progress and own project management for critical clinical and business partnershipsSupport the timely execution and rapid growth of Ossium’s operations and business development through taking on a broad range of logistical, administrative, research, partnership, or other assignments as requested by the CEO\nIn your first six months some projects you’ll work on include:\nHelping to develop and refine the go-to-market strategies for several of Ossium’s products slated to enter the clinic over the next 18 months Producing materials and reports for Ossium’s Q4 Board of Directors meeting, working with various members of the Ossium leadership team to acquire information and data as neededBecoming intimately familiar with Ossium’s financial model and all of the various levers that have an impact on the long-term success of the companyPlanning Ossium’s bi-annual leadership retreat, which will take place in Q1 2024\nThis position has a salary range of $108,500 to $186,000 annually. Ossium Health takes a market-based approach to pay. The successful candidate’s starting salary will be determined based on, but not limited to, job-related skills, experience, qualifications, and market conditions. This range may be modified in the future.\nOssium provides equal employment opportunities (EEO) to all employees and applicants for employment without regard to race, color, religion, sex, national origin, age, disability, sexual orientation, gender identity or gender expression. Pursuant to the San Francisco Fair Chance Ordinance, we will consider for employment qualified applicants with arrest and conviction records.",
            "job_id": "3690897280",
            "job_location": "San Francisco Bay Area",
            "job_title": "Business Strategist",
            "job_type": "Full-time",
            "job_url": "https://www.linkedin.com/jobs/view/3690897280/",
            "remote_allow": false,
            "salary_details": {
              "compensation_type": "BASE_SALARY",
              "currency_code": "USD",
              "max_salary": "186000.0",
              "min_salary": "108500.0",
              "pay_period": "YEARLY"
            },
            "salary_display": "USD108500.0/yr - USD186000.0/yr",
            "skills": [
              "Biotechnology",
              "Business Development",
              "Clinical Trials",
              "Communication",
              "Microsoft PowerPoint",
              "Oral Communication",
              "Pharmaceuticals",
              "Problem Solving",
              "Project Management",
              "Time Management"
            ],
            "specialities": [
              "Bone marrow banking",
              "Cryopreservation",
              "Stem cell biology",
              "Research",
              "Stem Cell Therapy",
              "Stem Cell Transplant",
              "Bone Marrow Transplant"
            ]
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Search Linkedin Company Pages via Google
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/google-profiles') and
            i.nice_name == "Search Linkedin Profile via Google "
                           "/google-profiles")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": [
            "https://www.linkedin.com/apple",
            "https://www.linkedin.com/apple-california",
            "https://www.linkedin.com/apple-info-technology",
            "https://www.linkedin.com/apple-one-technologies",
            "https://www.linkedin.com/app-store-apple",
            "https://www.linkedin.com/appleinc",
            "https://www.linkedin.com/apple-foundation-program-uts",
            "https://www.linkedin.com/apple-fix-pros-llc",
            "https://www.linkedin.com/magic-apple-technology",
            "https://www.linkedin.com/applemothershipcom",
            "https://www.linkedin.com/greenapple",
            "https://www.linkedin.com/tech-to-school",
            "https://www.linkedin.com/town-of-apple-valley",
            "https://www.linkedin.com/tube-bending-technology",
            "https://www.linkedin.com/apple-g-web-technology-pvt-ltd---india",
            "https://www.linkedin.com/thecoretg",
            "https://www.linkedin.com/hcs-technology-group",
            "https://www.linkedin.com/mazaroth-it-solutions",
            "https://www.linkedin.com/applecomputers",
            "https://www.linkedin.com/induction-technology-corporation",
            "https://www.linkedin.com/digital-apple",
            "https://www.linkedin.com/green-apple-solutions",
            "https://www.linkedin.com/global-technology-estore",
            "https://www.linkedin.com/claris-international-inc",
            "https://www.linkedin.com/aickman-and-greene",
            "https://www.linkedin.com/itechia-advanced-information-technology",
            "https://www.linkedin.com/iplus-apple-authorized-reseller",
            "https://www.linkedin.com/apple-developer-academy-uc",
            "https://www.linkedin.com/select-tech-group",
            "https://www.linkedin.com/green-apple-it",
            "https://www.linkedin.com/interlaced",
            "https://www.linkedin.com/necessary-technology",
            "https://www.linkedin.com/patagol",
            "https://www.linkedin.com/apple-banana",
            "https://www.linkedin.com/custard-apple-technologies-cat-",
            "https://www.linkedin.com/green-apple-books-on-the-park",
            "https://www.linkedin.com/blue-apple-technologies-llc",
            "https://www.linkedin.com/talented-young-geeks",
            "https://www.linkedin.com/stone-apple-solutions",
            "https://www.linkedin.com/apple-inc.-kuwait",
            "https://www.linkedin.com/compu-b",
            "https://www.linkedin.com/apple-consulting-group",
            "https://www.linkedin.com/aeras-technologies",
            "https://www.linkedin.com/adg-manipal"
          ],
          "message": "ok"
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Recommendation Given
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-recommendations-given') and
            i.nice_name == "Get Recommendation Given")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": [
            {
              "profile_url": "https://www.linkedin.com/in/marksephtonbusinessmentor/",
              "text": "Mark is an amazing podcast host! I truly enjoyed working with him on my recently Brainz Magazine podcast. He is a skilled interviewer with a great grasp on the subject matter. Mark has a real knack of being able to ask the right questions. I highly recommend you listening to his interviews and reach out if you need a host."
            },
            {
              "profile_url": "https://www.linkedin.com/in/nusrat-zahan/",
              "text": "Nusrat is a significant contributor to the InfluencerActive team. She consistently demonstrates strong marketing and communication skills, with a real dedication to the success of the brands she works with. Nusrat's positivity inspires and motivates those around her. She is a very talented social media influencer.\nI highly recommend you follow her on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/demitafr/",
              "text": "Mia is an inspiring person with a vibrant personality. Her engagements are always thoughtful, meaningful, and respectful. She is a lifelong learner and advocate for women's holistic wellness. As an integrative coach and entrepreneur in the holistic health and wellness space. I highly recommend you follow her."
            },
            {
              "profile_url": "https://www.linkedin.com/in/massimobrebbia/",
              "text": "I have the privilege of being connected with Massimo. He is wonderful to work with and has unique insights and expertise in business influence, leadership, and brand growth. He has a very strong work ethic and unparalleled analytical and problem-solving skills. Massimo is very giving with his time, always willing to work through business challenges and provide solutions. I am lucky to have him in my network. I highly recommend you follow him today."
            },
            {
              "profile_url": "https://www.linkedin.com/in/derickmildred-linked-in-for-business-coach/",
              "text": "Derick constantly amazes me with his insight and original approaches to LinkedIn strategy and application for business. He is open, willing to give advice, and well respected within the LinkedIn community. Derick leads by example and many people find his enthusiasm and dedication to both brand building and position for business as well as his industry insights extremely valuable. \nThe success he has achieved personally and professionally shows his extensive knowledge and dedication. I highly recommend Derick, follow him today."
            },
            {
              "profile_url": "https://www.linkedin.com/in/brianthemacman/",
              "text": "Brian has been a growing influencer on LinkedIn, especially since joining InfluencerActive, and has created a presence as a content creator. He is always giving kindness and positivity to his network and is a rising star and supporter.\n\nIt will be fun seeing Brian’s continued growth on LinkedIn, his company SellYourMac.com’s success, and his ability to coach and provide value to others on this network. I highly recommend you follow his profile today!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/kumarjha42/",
              "text": "Kumar is doing a great job for our communities. He has recently started a Not For Profit Opportunities Australia which is helping so many people in finding jobs. His team of 70 volunteers mentor people and make them job ready. Kumar has a great intention in helping out struggling Australians and I really wish him well. \n\nWe need more leaders like him! "
            },
            {
              "profile_url": "https://www.linkedin.com/in/w-kevin-ward-speaker-messenger/",
              "text": "W.Kevin Ward is one of those wonderful generous people here on LinkedIn. Proactive, energetic and amazingly giving, he is truly a 'Creative Follower'. He is an energetic coach, consultant and trainer! W.Kevin Ward has always gone that extra step to extend a helping hand. I highly recommend following him on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/jerin-hossain-678a1120/",
              "text": "Jerin is most likely one of the most giving professionals on social media. She has a very strong work ethic and is always willing to help. Her support of InfluencerActive as we grow is amazing. Her leadership and organisational skills are invaluable. Jerin makes the impossible possible. I definitely would recommend her as an entrepreneur and humanitarian."
            },
            {
              "profile_url": "https://www.linkedin.com/in/tiarne-hawkins/",
              "text": "Tiarne is among the best among tech thought leaders around. Wise, intelligent, brilliant and well educated who is very well worth following. She delivers real insights on the future of AI - that's Tiarne's way. Certainly someone I'd want to have on my team. I highly recommend you following her."
            },
            {
              "profile_url": "https://www.linkedin.com/in/ms-suchi-0078b765/",
              "text": "Ms Suchi is wonderful to work with and has unique experience in personal branding, social networking, personal development. Her knowledge is vast and thorough. Her leadership and organizational skills have been invaluable to many organisations. Ms Suchi builds deep relationships with everyone she touches. She is an asset to any business."
            },
            {
              "profile_url": "https://www.linkedin.com/in/steve-blakeman-a294795/",
              "text": "I have been fortunate enough to know Steve for many years now, and he is the first one I turn to when it comes to global strategy and perspectives in the media world. His thinking, approach and insights are second to none. He is a true influencer and amazing communicator. I would highly recommend Steve in any global role."
            },
            {
              "profile_url": "https://www.linkedin.com/in/amber-cheema-digitalmarketer/",
              "text": "Amber is an amazing networker and digital marketer. She simply gets what it takes to connect, network and build deep lasting relationships in a meaningful way. Amber is a motivated, forward-thinking as well as and intelligent Influencer with deep knowledge in her field. She is detail-oriented, goal-oriented, ambitious, her knowledge is vast and extensive. I would recommend her to any project that requires the very best in networking execution. She has a very positive attitude towards everything she does. Amber makes the impossible possible. She learns quickly and I would have no hesitation in recommending Amber."
            },
            {
              "profile_url": "https://www.linkedin.com/in/jerin-hossain-678a1120/",
              "text": "Jerin is an international influencer with impact. Inspirational, caring and always willing to help. I highly recommend you follow her on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/ricardoamorimricam/",
              "text": "Ricardo is a true global networker and influencer. He understands social media. I would highly recommend you follow him on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/corywarfield/",
              "text": "Cory is just an all-round good guy! I have no hesitation in recommending you follow him today! Do it. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/charikleiastouka/",
              "text": "Charikleia is an inspirational leader with a caring heart and a brilliant career on Real Estate in Greece. She respects herself and others and enriches the world making a difference to her job and the community. She has a great vision and extraordinary achievements and takes clients where they ought to be. I highly recommend Charikleia and ALMA Real Estate Hellas Agency."
            },
            {
              "profile_url": "https://www.linkedin.com/in/guan-hin-tay-a757404/",
              "text": "Guan Hin is it true storytelling master. Beyond his exceptional creativity, he also a genuine, humble and caring professional. It’s been my honour to work with him on stage and in the real world as well as here on LinkedIn. I highly recommend you reaching out and connecting to him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/egitto3000/",
              "text": "Mohamed is an industry visionary and leader, with a passion, drive and energy to see himself snd those around him succeed. He is definitely a person to follow on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/mattlevy87/",
              "text": "I was fortunate enough to connect to Matt through LinkedIn, and meet him in the real world face-to-face. He is truly an inspirational speaker and motivator. His stories are captivating and fascinating. There’s a lot you can learn from Matt and his journey to the number 1 spot on the Olympic podium. I highly recommend you connecting with him and engage him as your next motivational speaker."
            },
            {
              "profile_url": "https://www.linkedin.com/in/saheb-youssef-bakhsh/",
              "text": "Joseph's attention to detail when it comes to relationship building through effective communication is outstanding! He has established himself as a well respected Sales and Marketing thought leader on this platform who bases his actions and interactions with others on integrity and respect.\n\nI highly recommend you to follow him. I wish him the very best in all his future endeavours."
            },
            {
              "profile_url": "https://www.linkedin.com/in/radutheodorescu/",
              "text": "I would highly recommend Radu, he is ambitious, and has a highly inspirational persona. The type of person you want on your team. He is highly analytical with the ability to generate new revenue, implement strategy and build deep lasting relationships with clients - a rare blend of skills indeed. He can also fluently speak English, French and Romanian. \n\nIf you’re looking for a passionate, enthusiastic and true team player for your organisation Radu is your man!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/alina-tkachenko-31157578/",
              "text": "I highly recommend Alina - she is a passionate and highly energetic business development professional, with strong sales, marketing and specialist development credentials. The fact that she is also fluent in 4 languages makes her a serious asset to any organisation! Reach out and connect with Alina today."
            },
            {
              "profile_url": "https://www.linkedin.com/in/andyfoote/",
              "text": "Andy's insights on branding and content are second to none. Andy actually helped to kick start my growth on LinkedIn, openly providing me tips to clean up my profile...this started my growth! He continue to surprise me with \"new things\" I did not know about the platform. If you need help with LinkedIn, or just want to follow a smart thinker, Andy is definitely the person to be following on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/mousa-al-bharna-28534611/",
              "text": "Mousa is a truly genuine and giving person, interested in others and very willing to give his time and energy to help and support. I am honoured to be connected and in his circle of influence. I would highly recommend him as a mentor and coach. \nReach out and start a conversation today with Mousa."
            },
            {
              "profile_url": "https://www.linkedin.com/in/roones/",
              "text": "Roones this is true content and creative “queen” her passion, enthusiasm and creativity are reflected in everything she does. If you want your brand to truly stand out Roones is the one to turn to! "
            },
            {
              "profile_url": "https://www.linkedin.com/in/munmun-singh-41829723/",
              "text": "Munmun Singh has shown passion and dedication in her professional and personal life. She is a beautiful soul with a kind heart and has always shown empathy and compassion with the destitute and the less fortunate. She will be an asset to any organisation that she will be a part of.\n"
            },
            {
              "profile_url": "https://www.linkedin.com/in/emsclean/",
              "text": "Manuel is totally dedicated when it comes to giving his customers world class service and support. He is always a great guy to bounce ideas off, able to direct technical support and resource to best serve when faced with challenging process issues."
            },
            {
              "profile_url": "https://www.linkedin.com/in/medfuel/",
              "text": "I have been following Frank’s content for some time now, and I can say he is authentic and good at what he does. He does not just post about branding, but how to generate real revenue using strategies that really work!  If you are considering working with him, I highly recommend him!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/kimpetersonstone/",
              "text": "Kim has the uncanny ability to identify ideal strategies for organisations looking to rise above the noise and definitively establish their presence on LinkedIn.\n\nShe offers a combination of purpose and passion-driven methodologies when training teams and is able to generate enthusiasm around the platform which results in client acquisition, sales generation, new market penetration, and thought leadership positioning based on her client's objectives.\n\nKim’s eye is always on achieving tangible results. She helps her clients build a bridge from where they are currently to how they actually want to be represented in the B2B space.\n\nI have no hesitation in recommending Kim - engage with her today."
            },
            {
              "profile_url": "https://www.linkedin.com/in/tonyabbacchi/",
              "text": "If you’re looking for a digital advertising professional who can drive true ROI and scale national and global campaigns for your organisation then Tony is the man you want on your team.\nHis skills span both B2B and B2C companies.\nIn everything he does he is passionate, focused and highly collaborative. I have no hesitation in recommending Tony on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/titia-niehorster/",
              "text": "Titia is a strong advocate for the wellbeing of children. Via her posts and valuable content, she shares important and educational skills on how to empower our children, enabling them to develop and grow up to be strong confident adults - people that the world needs today. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/yücel-ulusoy-mba-00698bb6/",
              "text": "Yücel is a motivated, forward thinking and intelligent Linkedin professional who is generous with his time and engagement. He provides advice and guidance using the platform and is quick to help put his connections where he can. Whenever I had a question, there has never been a time he has left me without a solution. Yücel is a dedicated and goal oriented strategist that cannot be overestimated. Yücel makes the impossible possible. I have no hesitation is recommending him on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/chinedujuniorihekwoaba/",
              "text": "I have had the great pleasure of connecting with Chinedu on LinkedIn. He is a content producer extraordinaire! A wonderful writer and even a poet. His feed is constantly full of thought provoking posts which truly make you think!\nChinedu is also a true professional, often first with a like or insightful comment on my posts.\nI highly recommend the work he is doing here on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/mike-podesto/",
              "text": "Mike is a business owner, savvy networker, great writer, and friend...\nIn everything he does he strives for excellence. This is what sets him apart from others. \nMike truly cares about people and knows exactly how to deliver the messages that people are often not ready or find uncomfortable to hear in a professional and caring manner.\nHis company has been recognised as the #1 executive resume writing service. There is nothing else out there like it!\nI would highly recommend Mike and his company."
            },
            {
              "profile_url": "https://www.linkedin.com/in/nataliawiechowski/",
              "text": "One of the numerous benefits of LinkedIn is that it allows you to easily find and engage with likeminded individuals. \nI am truly fortunate to say this is how Natalia’s and my paths crossed. \nNatalia is one of the leading thinkers in the Middle East. Her content around personal branding is “edutaining”, full of insights, lessons learned and vibrant stories. \nShe also does an amazing job in building her (online) community, collaborating and supporting others. In short, it is worth following her on LinkedIn.\n—ANthony J James"
            },
            {
              "profile_url": "https://www.linkedin.com/in/dinopacellaofficial/",
              "text": "It’s always great to be able to meet online connections in the real world, but deep down inside you hope that what you see online is going to be the same in person. \nAfter liaising with Dino for a few months online, we recently got to catch up for a coffee in Sydney and I am pleased to say that....what you see is what you get...with him. \nHe is authentic, real, transparent and honest. \nHis Ubervation brand is true to who he is which is all about assisting the people around him through inspiration, education and motivation by keeping it humanised.\nRecommend connecting with Dino if you haven’t already.\n-- Anthony J James"
            },
            {
              "profile_url": "https://www.linkedin.com/in/chloehacquard/",
              "text": "Chloe is a highly creative, passionate and influential Brand advocate on LinkedIn. \nWhen you are retargeted by HighChloeCloud your ideas and concepts become visible to the world. \nChloe’s reach on social media is extraordinary, she is highly intelligent and has a deep understanding of the digital marketing landscape.\nI would highly recommend Chloe to somebody to follow on LinkedIn, connect with and engage on her content.\n\nChloé est une personne très créative, passionnée et influente elle défends les marques sur LinkedIn. \n\nLorsque vous êtes reciblé par HighChloeCloud vos idées et vos concepts deviennent visibles et se répandent partout dans le monde. \nLa portée de Chloe sur les médias sociaux est extraordinaire, elle est très intelligente et possède une grande compréhension du paysage marketing numérique.\n\nJe recommande fortement Chloé à toute personne désirant la suivre sur LinkedIn, de communiquer avec elle et de s’engager sur son contenu.\n\n\nRédiger une recommandation à Chloe :\nhttps://www.linkedin.com/recs/give?senderId=chloehacquard"
            },
            {
              "profile_url": "https://www.linkedin.com/in/mehran-fassihi-fasihi-hoor/",
              "text": "Mehran is an excellent Business Management Instructor. He is very thorough in everything he does and can be depended upon to get the job done. I would recommend him with any project that requires the very best in management execution. He is always able to successfully complete any tasks with favorable results despite deadline pressure. The success achieved in his job requires extensive knowledge and dedication. Mehran is the one you want on your team to get the job done."
            },
            {
              "profile_url": "https://www.linkedin.com/in/jules-burdin-803a9424/",
              "text": "Working with Jules was fantastic. I found him as someone with great experience as well as a broad minded Executive Search Consultant - his exceptional communication skills and people management across cultures made him so easy to work with. His performance in securing me a Country Manager role for Asia Pacific was outstanding - especially as we had never meet face-to-face. Besides being great to work with, Jules is a take-charge person who is able to present creative solutions to human resource challenges and is able to communicate and negotiate to the benefit of all parties. Jules is one of the best Executive Search Consultants I have ever had the privilege of working with."
            },
            {
              "profile_url": "https://www.linkedin.com/in/rajkgrover/",
              "text": "Raj is a detail oriented, goal oriented, ambitious and powerful networker, his knowledge in innovative, leading advertising technologies is vast and thorough. Besides being a great networker and communicator, Raj is a can-do person who is able to present creative solutions to complex problems and communicate the benefits. From this perspective he is a leader and entrepreneur in one! I thoroughly appreciated dealing with Raj and would highly recommend you reach out connect with him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/kishwar-rahman-gaicd-9676292b/",
              "text": "I worked closely with Kishwar while consulting to the Digital Transformation Agency (DTA) as Head of Engagement. Kishwar was the lead advisor on policy and legal compliance as they engaged with DTA systems and platforms.\r\nKishwar at every step, not only demonstrated a deep understanding of her core role, but also had the ability to understand the fundamental challenges that Agencies faced from a compliance, re-visioning and commercial perspective - often before they did.\r\nHer consultative and collaborative approach, coupled with her commercial acumen allowed her to design solutions and outcomes to meet all requirements.\r\nI certainly miss working with Kishwar on a daily basis, and have no hesitation in recommending her to future employers."
            },
            {
              "profile_url": "https://www.linkedin.com/in/audreynormannicoll/",
              "text": "Audrey is one of those rare people you wish you had on your team, but just never managed to find! \r\nI worked closely with Audrey in her role as VP Global Marketing for PageUp.  Audrey’s dedication and understanding of data-driven marketing and converting to actionable deliverables and outcomes is exceptional. She was always backed her decisions, especially as it related to the success of the marketing team and the company. \r\nShe always did the unconventional well. With a real ability to drive project from start to finish, she is innovative in her thinking and disciplined and motivated to assist the marketing team to achieve success. Audrey juggled multiple projects, like nobody in my team before, which lead to dramatic productivity increases from her team. I have no hesitation in recommending Audrey in any marketing leadership role.\r\n"
            },
            {
              "profile_url": "https://www.linkedin.com/in/jithoong/",
              "text": "Jit is not only a technically brilliant digital creative but also an inspiring professional. He is detail oriented, self motivated and an ambitious employee. HIs experience and huge knowledge stands him apart. Jit always maintains very good relation with his team and clients. His digital knowledge and high levels of creativity, combined with his dedication gives Jit the ability to view solutions instead of problems. I would highly recommend him to any employer and look forward to working with him again in the future."
            },
            {
              "profile_url": "https://www.linkedin.com/in/akshayabhatia/",
              "text": "Akshaya is a highly professional result driven individual. He is an exceptional leader, and his teams constantly look to his for advice and guidance in the delivery of complex and challenging projects. No situation is to complex or to challenging for Akshaya, he is extremely calm under pressure situations, and is always about finding outstanding innovation solutions for his clients.\r\nHis amazing innovative spirit and his ability to communicate at all levels within an organisations makes him a true asset to any potential future employer."
            },
            {
              "profile_url": "https://www.linkedin.com/in/isseimatsui/",
              "text": "Issei has provided great leadership and management to the Japan office. He is open and collaborates with thought-leaders from across the region to ensure the very best ideas and innovations are present to clients. He leads a cohesive team, providing opportunities for growth to all his staff. He strives for sustainable thought and action.\r\n\r\nI would highly recommend him to any project leaders - invite Issei and his team - especially if you require success, innovation and growth."
            },
            {
              "profile_url": "https://www.linkedin.com/in/philromans/",
              "text": "As Regional Business Director on Mars / Wrigley, Philip has the keen sense of what it takes to achieve the Agencies goals and objectives as well as putting the clients first. He has exceptional verbal and nonverbal communication skills, he has great skills in brining the \"right team\" to the table and provide break-thru, innovation solutions to his client. His other great asset is his ability to listen, to clients business problems and issues and translate this back into the Agency teams delivering solutions.\r\nPhilip is very open to sharing the credit with his team members and accepting responsibility for the growth of his clients business. These two traits sets him apart as a Regional Business Director.\r\nI would have no hesitation in recommending Philip, especially if you need someone running, complex regional accounts, that require a growth and innovation perspective. He is a great addition to any team!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/herlaw/",
              "text": "As DDB China Groups Creative Technologist, Herbert was simply fantastic to work with. He worked exceptionally well under pressure situations, putting in the time and effort to ensure we delivered exceptional solutions and outcomes to clients. Herbert is also very strong at \"finding\" solutions, while he might not always have the answers immediately, his ability to understand complex technologies and build easy to understand pitches to clients is second to none.\r\nHerbert was always a pleasure to work with and I would not hesitate to recommend him for future roles."
            },
            {
              "profile_url": "https://www.linkedin.com/in/karenlumsee/",
              "text": "Karen is a motivated, intelligent and cool under pressure person, always willing to give guidance and advice - and my experience has shown that from a Marketing & Communications perspective her advice is spot-on, each and every time. Karen was an exceptional Chief Communications Officer. She was a great spokesperson for the agency both externally and internally. Her network and depth of contacts across all media channels were key to her success and the results that she delivered for DDB. Karens inclusive nature and ability to connect people, ideas and stories would motivate me to work with her in a heartbeat."
            },
            {
              "profile_url": "https://www.linkedin.com/in/stuartnyman/",
              "text": "Stuart is an exceptionally talented and creative digital solutions architect. He is one of the most capable digital natives, having a very broad view of the landscape and then being able to focus on specific client business problems and issues and applying his knowledge to develop solutions. Stuart is a exceptional presenter with a quick capability to connect with clients and any level within an organisation. I would highly recommend Stuart if you are looking for someone who works at the intersect of technology and creativity and has a unique ability to develop break-thru, innovative solutions."
            },
            {
              "profile_url": "https://www.linkedin.com/in/kiley-charteris-947ab129/",
              "text": "As Business Development for Asia, Kiley was a real pleasure to work with. Nothing ever seems to much for her, apart from being focused and driven she approached every challenge with a smile and a determination to complete the task at hand. Kiley's approach is proactive, honest and delivered results for Creata's clients. She has a great ability to pull together the right mix of skills within internal project teams to ensure the best outcome for clients. \r\nI feel confident that I could recommend Kiley to anyone and she would do a fabulous job each and every time!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/eszter-hencz-pálinkó-60719398/",
              "text": "Eszter worked for our start-up in Hungary as a lead sales and marketing professional. Eszter is highly professional with the ability to quickly understand business concepts and innovative models and present these in a creative and articulate way to clients. She builds deep lasting relationships with clients and has the ability to engage at the all levels within a company. I would highly recommend Eszter to future employers as a dedicated, professional and detailed oriented person."
            },
            {
              "profile_url": "https://www.linkedin.com/in/benjamin-deregt-8a594930/",
              "text": "Benjamin is a real pleasure to work with. He is very focused and driven with a unique ability to listening and interpret requirements into true partnering solutions. Bens' approach is proactive, honest and delivered results - even when he needed to hand off a project to his internal team members. He keeps his promises, listens and connects you with outstanding opportunities, always keeping you up to speed with any developments. I feel confident that I could recommend Benjamin to anyone and he would do a fabulous job every time!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/lucywestdesign/",
              "text": "Lucy is a wonderful designer and all-round creative person. Her body of work covers all forms of media from hands on painting and sculpture to photography and film. Now mastering the digital tools, she has built an impressive digital/online portfolio of work. \r\n\r\nLucy has an instinctive and keen eye for design - and is not afraid to ask the right questions to understand exactly what the client requires. I would highly recommend her creative talents to anyone."
            },
            {
              "profile_url": "https://www.linkedin.com/in/burda/",
              "text": "Steven is a leader of the open networking community, his ability to connect people locally or globally, no matter if its personal or professional is quite amazing! Steven has pioneered a new way of socially networking on LinkedIn. If you are not connected to him...now is the time...thanks Steven for all your efforts - from one networker to another."
            },
            {
              "profile_url": "https://www.linkedin.com/in/nalini-nair-b33a0b2a/",
              "text": "Nalini is one of those wonderful people who is always happy to help and nothing is ever too much. You would only need to ask and Nalini was always there to lend a helping hand. She is a very level-headed, multi-skilled person who can juggle many tasks at the one time. A logical and analytic thinker who knows how to get the job done. I would highly recommend Nalini to anyone considering her skills and professional approach to everything she undertakes."
            },
            {
              "profile_url": "https://www.linkedin.com/in/kayepomarancwhite/",
              "text": "Kaye is one of those \"special people\" not only is she highly creative but also a deep strategic thinker, a truly rare talent in one individual - I would highly recommend Kaye to anyone considering working with her..."
            },
            {
              "profile_url": "https://www.linkedin.com/in/alfacebruno/",
              "text": "Bruno is a young, energetic and bright individual. I was very pleased when I met Bruno for the first time in Brasil working for our Master Franchisee. Bruno clearly had leadership qualities and quickly became a Supervisor in our operation. Bruno has the ability to quickly understand new business models and concepts and can translate these to team leadership and demonstrative management capability to his peers. This will hold Bruno in good-stead for the future. I have no hesitation in recommending him, Bruno will be a major asset to any future employer."
            },
            {
              "profile_url": "https://www.linkedin.com/in/tomas-saiz-68123a4/",
              "text": "Tomas was talented, energetic and focused Account Director, working in a very complex market sector – Latin America. It was my privilege as Chief Creative Officer, Globally to work with Account Managers all over the world in every region. Tomas was able to clearly articulate needs and desires his clients had in the region as well as being able to identify trends and issues before they impacted his clients bottom line. I would happy recommend Tomas to any prospective employer."
            },
            {
              "profile_url": "https://www.linkedin.com/in/anthonyorgill/",
              "text": "Anthony is a brilliant mind, a strategic thinker with strong business, operational and finance capabilities. His background in consulting, CRM and call centres allows him to turn his hand to the largest and smallest projects. With his international experience Anthony is also able to cross the cultural divide delivering solutions, experiences and business results to clients.\r\n\r\nAs a recognised leader in CRM consulting, strategy, management, operations, technologies and contact centre transformation I would highly recommend Anthony."
            },
            {
              "profile_url": "https://www.linkedin.com/in/dinaellithorpe/",
              "text": "I am very happy to recommend Dina. Dina is one of those special Account Directors, one who understands the business in which she works as well as the clients business without loosing sight of objectives and strategic outcomes. She was extremely good at managing client expectations and deliverables, in what was often a difficult and complex client/vendor situation. Above all, Dina maintained high credibility and relationships (over the long-term) with her clients, accounts and peers. I would highly recommend Dina to anyone considering engaging her skills and services."
            },
            {
              "profile_url": "https://www.linkedin.com/in/julie-duran-335113/",
              "text": "Julie has a clear, level-headed and direct approach to strategic business development, she understood what it took to pull the right team together to benefit the client and deliver on their business initiatives."
            },
            {
              "profile_url": "https://www.linkedin.com/in/craig-jarman-8549571/",
              "text": "Craig is a detail-oriented solutions developer with the ability to think out-side the square and think laterally about ways to solve complex business problems for clients - this is the first reason I would always want him leading a delivery project for our clients...he job got done - on-time and on budget...and exceeded all client expectations."
            },
            {
              "profile_url": "https://www.linkedin.com/in/servantofchaos/",
              "text": "I very results, solution and detail orientated person...a really sharp mind!"
            }
          ],
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Recommendation Received
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-recommendations-received') and
            i.nice_name == "Get Recommendation Received")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": [
            {
              "profile_url": "https://www.linkedin.com/in/innovationews/",
              "text": "Anthony is and amazing influencer and leader in the global technology industry. His vision and solutions are the best I’ve seen. I highly recommend to follow his profile, to be update with the most amazing innovations! It´s a great pleasure work with you AJ! Best regards!\n\nAnthony é um incrível influenciador e líder na indústria global de tecnologia. Sua visão e soluções são excepcionais. Eu recomendo seguir o perfil dele, para estar atualizado com as novidades mais incríveis! É um grande prazer trabalhar com você AJ! Atenciosamente!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/mariahedgington/",
              "text": "Anthony James and I are both content creators on LinkedIn. Anthony is a solid resource here on LinkedIn and around the globe. I've had the good fortune to be guided by his high-quality content, written and video. He is a visionary whose insights, practical tips & tools provide a resource for all who read his content and follow/connect with him. Anthony is a true leader and entrepreneur. He’s an optimist who knows with imagination, creativity and resilience, obstacles can be overcome. I highly recommend Anthony James."
            },
            {
              "profile_url": "https://www.linkedin.com/in/marksephtonbusinessmentor/",
              "text": "Had the privilege of spending 30 minutes sat down with AJ on the Brainz Magazine Podcast. Loved AJ’s energy and the depth of knowledge within the art form of creating influence. AJ’s extensive network especially here in LinkedIn is evident to his Integrity and his heart felt leadership which builds huge trust. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/nusrat-zahan/",
              "text": "I have met many incredible people from around the world during my journey on LinkedIn.  But Anthony stands out in many ways, which has inspired me to write a few words about him.  He is much more than just a wonderful networker and business influencer with more than 3 million followers.  He is a kind, creative, and caring person whose generous attitude is amazing, and he is always there to provide guidance and wisdom.\n\nHis extensive knowledge and experience in technology, innovation, and business strategy provide businesses access to a vast pool of consolidated information - whether this is understanding of customers' needs, business environment or the skills and experience requirements of their staff.\n\nHis vision for marketing and business has changed the landscape for business-minded people.\n\nAs CEO of influencer active, he has established a unique global B2B Influencer marketplace to work with real business people to impact and amplify their marketing.\n\nHe is a true leader And influencer who has directly impacted many other Influencers.\n\nI highly recommend Anthony and encourage you to follow him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/demitafr/",
              "text": "Anthony is an amazing networker and business influencer on LinkedIn. Always generous with his time and willing to provide guidance and wisdom. His finger is firmly on the pulse of global innovation and technology. I highly recommend you follow him on LinkedIn.\n~~~~\nAnthony est un networker et un influenceur d'affaires incroyable sur LinkedIn. Toujours généreux de son temps et prêt à fournir conseils et sagesse .Il suit les évolutions de l'innovation et de la technologie au niveau mondial, je vous recommande fortement de le suivre sur LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/kumarjha42/",
              "text": "Anthony is an amazing networker and influencer on LinkedIn. He presents the most amazing global innovations and technologies. \n\nI like what he does and highly recommend following him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/brianthemacman/",
              "text": "What hasn’t Anthony done? He has grown to 2M+ followers and created billions of toys to make kids smile around the world... and now he has created a platform called Influencer Active to help influencers monetize their presence on LinkedIn!\n\nI'd definitely recommend getting on his platform if you are an influencer, the possibilities of being an early adopter here are endless!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/w-kevin-ward-speaker-messenger/",
              "text": "I have the good fortune to work with Anthony on several different occasions! I have come to appreciate his generosity and willingness to help others.\n\nAdditionally I have seen first hand Anthony's innovation and willingness to develop and execute as an entrepreneur.\n\nI recommend Anthony as a friend, colleague and collaborator here on LinkedIn and other areas!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/piya-saini-10947971/",
              "text": "I have been connected to Anthony for a number of years now. He is a kind, creative and caring person, always ready assist and give advice. Anthony is also a visionary. As the founder of Influencer Active, he is changing the marketing and advertising landscape forever. He has unique insights into digital solutions, future-technologies and strategies that engage consumers and solve big business problems. Follow him today, you wont be sorry."
            },
            {
              "profile_url": "https://www.linkedin.com/in/steve-blakeman-a294795/",
              "text": "I've known AJ for some time now and you won't meet a guy who knows more about business influencers than he does. His posts on LinkedIn are always fascinating, whether they are about technology, innovation, influencers, social media etc. and he regularly racks up views in excess of 1 million+ so I guess he must be doing something right! Plus he is a genuinely decent bloke to do business with. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/jerin-hossain-678a1120/",
              "text": "Anthony is a real LinkedIn influencer. It does not a matter the size of his network he still makes time for each person. Anthony leads by example at InfluencerActive, he is not only inspirational but sets the strategy and drives the global growth this true focus and passion. His enthusiasm and dedication are inspirational. Whenever I have a problem, there has never been a time has has left me without a solution. For Anthony people always are the most important. He has a very positive attitude to everything he does. Follow him today."
            },
            {
              "profile_url": "https://www.linkedin.com/in/massimobrebbia/",
              "text": "Anthony is a true influencer and the founder of the world's first business-to-business influencer platform. He is a visionary and innovator with an amazing grasp of global technology trends and concepts. I absolutely recommend clicking the follow button on his profile. You will not regret it."
            },
            {
              "profile_url": "https://www.linkedin.com/in/tiarne-hawkins/",
              "text": "Anthony is an innovation thought leader working at the intersection of technology and marketing. His LinkedIn feed is an endless pipeline of amazing ideas and concepts from around the world. I highly recommend you click the follow button on his profile today.\n"
            },
            {
              "profile_url": "https://www.linkedin.com/in/ms-suchi-0078b765/",
              "text": "Anthony is a master networker and a genuine LinkedIn influencer. As the founder of the world's first B2B influencer marketplace, Influencer Active, he is helping build reach and growth for global SMEs. I highly recommend following Anthony on LinkedIn today."
            },
            {
              "profile_url": "https://www.linkedin.com/in/amber-cheema-digitalmarketer/",
              "text": "Anthony J James is a global leader having expertise in Innovation, Technology, Business  & Marketing. He is a Top Linkedin Influencer, Storyteller, Content Creator. Recently he launched the world's top Influncers marketplace IA which is a next-level initiative as this is the era of influncer marketing. I know Anthony since day one as a follower,  I just love his creative content. Luckily after the launch of IA  I get a chance to work with him directly, he is so kind supportive & down earth person. A humble & highly professional personality with a positive attitude is called Anthony J James. \n\nHe is perfect for any kind of business Collaboration. He got 2.6 Million Followers, they are not just numbers. He got a true network. He always shares something innovative which can help you to explore more opportunities in some way or other. \n\n"
            },
            {
              "profile_url": "https://www.linkedin.com/in/w-kevin-ward-speaker-messenger/",
              "text": "It's a real honor to work with and engage with Anthony! We've worked together on LinkedIn in a variety of settings and projects...\n\nAnthony has proven to be of great support, much encouragement and practical help!\n\nAnthony also contributes to the LinkedIn community in many ways and generously!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/corywarfield/",
              "text": "Anthony J James has escalated to the status of Global Influencer for all the right reasons! His video shares, profile highlights, and the dots that he connects on LinkedIn and beyond have touched many thousands of lives, and his reach is indicative of how listening, sharing, contributing and understanding the computer science behind social media builds community and catalyzes growth. A fun, honest, creative and resourceful leader, Anthony’s work with Influencer Active has already has global implications. I am genuinely enthused to leave this highest recommendation."
            },
            {
              "profile_url": "https://www.linkedin.com/in/charikleiastouka/",
              "text": "Anthony is a true global marketing and technology expert. He is the one thought leader in innovation that I highly recommend you follow. Each of his posts is a real WOW!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/stevenouri/",
              "text": "Anthony is a total LinkedIn professional, he has a great marketing mindset and passion to drive it. He is very humble and kind who shares his knowledge openly and seriously with people.\n\nI know him for some time, he always brings the latest innovations and creative technology ideas. \n\nI highly recommend following him on LinkedIn, to see some great posts daily on your feed.\n"
            },
            {
              "profile_url": "https://www.linkedin.com/in/egitto3000/",
              "text": "Anthony is a global innovation storyteller. He has his finger on the pulse of global innovations and digital solutions. I highly recommend following him on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/mattlevy87/",
              "text": "Anthony is the sort of person that sees obstacles as opportunities. Always looking for the next innovation that can change the way people experience the world. His feed is a constant source of amazing ideas. I would highly recommend you following him here on Linkedin."
            },
            {
              "profile_url": "https://www.linkedin.com/in/saheb-youssef-bakhsh/",
              "text": "Some people stand out from the very beginning with their content, insights and approach. Anthony J James is a true thought leader on LinkedIn when it comes to innovation, technology and marketing. \n\nHe has opened my eyes to many new ideas and concepts from around the world. I would highly recommend you following his profile today.\n\nHis knowledge, experience and expertise in his field is second to none and he is an asset to any organisation he works with. \n\nA well deserved Top Voice on LinkedIn. Keep up the great work Anthony. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/radutheodorescu/",
              "text": "It’s rare that you come across standout Leadership and Influence Skills like Anthony. His capacity for strategic, tactical and operational plans in order to grow your business is unbelievable.\n\nAnthon’s ability to juggle multiple projects was unlike any I’ve seen before and would make a dramatic difference in the productivity level of any company.\n\nI would highly recommend you follow Anthony here in LinkedIn. And if your company is looking for growth reach out to him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/scottleeau/",
              "text": "I highly recommend following Anthony's profile on LinkedIn. He posts the best #innovation and #technology ideas. They are sure to spark growth ideas for your company. Follow his stuff ASAP"
            },
            {
              "profile_url": "https://www.linkedin.com/in/alina-tkachenko-31157578/",
              "text": " It’s my pleasure to recommend Anthony. \nHe is a great leader, an international adviser, and digital transformation expert. His deep knowledge in sales, marketing & branding helps to bring businesses to a new level. \n\nI’m impressed by how easily he combines leading a company and being a stupendous influencer. If you want to learn more about technology innovation you have to follow Anthony!\n\n\nМое удовольствие посоветовать Антони.\n\nЭто человек который имеет глубокое понимание в бизнесе. Его знания в продажах, маркетинге и брендинге могут поднять на новый уровень как начинающий старт ап, так же и успешный интерпрайз. Его заслуги досказывают такие награды как LinkedIn Power Profile #1 in Marketing & Advertising и Top Voice Australia.\n\nМеня восхищает его умение быть лидером успешной компании и при этом быть отличным инфлуенсером, который всегда информирует интересных инновационных технологиях. \n\nСоветую подписываться на Антони и следить за последними новостями в мире технологий!\n\n"
            },
            {
              "profile_url": "https://www.linkedin.com/in/andyfoote/",
              "text": "Anthony and I go way back and I'm so pleased, and completely unsurprised by his phenomenal professional success. It's obvious to me why LinkedIn has recognised Anthony’s efforts on LinkedIn, #1 Marketing & Advertising Power Profile, Top Voice and Most Influential Voice in Asia Pacific. If you want the latest innovation and technology ideas, I highly recommend you follow his profile."
            },
            {
              "profile_url": "https://www.linkedin.com/in/mousa-al-bharna-28534611/",
              "text": "Anthony is a marketing, creative and innovation leader! His knowledge of networking, marketing and collaboration is really wonderful. Beside all of that he is a great man who love to support, help and influence others.\n\nI would definitely recommend following and get to learn from him.\n\nI am really honored meeting him and getting to know him in person. Anthony! You are the man,"
            },
            {
              "profile_url": "https://www.linkedin.com/in/crystallbarkley/",
              "text": "Anthony is the one to follow on LinkedIn if you want the latest and greatest technology and innovation ideas. His knowledge and experience in this space is like nobody else on this platform. Follow his profile for daily updates on the newest and freshest ideas which might just help your business find growth. He is one of the top leaders/ voices on this platform. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/kamsingh1313/",
              "text": "Anthony J James is one of my favorite linkie in my professional network. I am feeling so honor by giving my recommendation for all his spectacular posts. He always surprised me by posting amazing content on technology. He is a powerhouse of new ideas and technology. He is really blessed with lots of wisdom.\n\nI am proud to have a wise mate like him.\n\nI am having a tremendous trust on him.\n\nDelighted to have a mate like him, in my connection.\n\nWarm Regards \n#kamaldeepsingh \n#mylovelylinkie family \n"
            },
            {
              "profile_url": "https://www.linkedin.com/in/strati-georgopoulos/",
              "text": "Anthony, Is LinkedIn’s technology and innovation leader. If your brand is looking for global growth Anthony is the man to connect with. I highly recommend him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/roones/",
              "text": "Anthony is the #Technology and #Innovation leader on LinkedIn. His posts are the most innovative, thought-provoking technologies and ideas on the platform. Someone everybody should follow. Click that follow button on his profile. ❤️❤️ 😁😁💪💪💪💪💪💪"
            },
            {
              "profile_url": "https://www.linkedin.com/in/munmun-singh-41829723/",
              "text": "Anthony is a person who sees a problem, he has the ability to find solutions, and he is a person, who through his actions goes out and does something about it.\n\nAnthony is a human being, a visionary and has an entrepreneurial spirit. In today’s world a true asset to any organisation. I highly recommend his LinkedIn feed and engaging with him in the real-world."
            },
            {
              "profile_url": "https://www.linkedin.com/in/emsclean/",
              "text": "Anthony is an innovation influencer here on LinkedIn, constantly bringing the latest #technology and #innovation ideas to the platform. If you are looking for someone to help you take you innovation to market and find growth globally then I highly recommend you reach out to Anthony."
            },
            {
              "profile_url": "https://www.linkedin.com/in/derickmildred-linked-in-for-business-coach/",
              "text": "Anthony J James is a marketing and content Rockstar, when it comes to LinkedIn his content is amazing, importantly the strategy behind it is all about inspiring his audience and keeping them informed without selling. I would best describe him as an online marketing genius. Highly Recommended.  "
            },
            {
              "profile_url": "https://www.linkedin.com/in/madeline-storey/",
              "text": "Anthony is a marketing, creative and innovation genius! I’ve had the pleasure working with him at Rehab Management, where I’ve learned a lot from his skills and experience. Anthony has helped us deliver successful, exciting and engaging events, innovative workflow solutions and has contributed invaluable insights into our team strategy. It’s the least to say his contribution to my team has been unrivaled."
            },
            {
              "profile_url": "https://www.linkedin.com/in/ranakordahi/",
              "text": "Anthony James is one of the most innovative marketers on LinkedIn. He understands both human psychology, as well as technology and AI. He got to influencer and top voice status on LinkedIn, by simply applying his techniques and can help any business thrive and grow. And this is what makes stand out from the crowd. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/kimpetersonstone/",
              "text": "Anthony is the creative and visionary leader you need on your team.\n\nHe has a unique ability to see just over the horizon, to guide and advise brands and agencies on technologies and digital solutions to solve big customer problems. Anthony is a true evangelist and innovation specialist, encouraging and motivating all around him to delivering amazing breakthrough solutions.\n\nHe has both broad and deep Asia Pacific experience, helping clients penetrate and generate growth in some of the largest consumer markets in the world. If you are looking for an out of the box competitive advantage thinker, Anthony is your man."
            },
            {
              "profile_url": "https://www.linkedin.com/in/rodrigo--martinez/",
              "text": "First of all Anthony is a gentleman. It was a pleasure to get to know him in person here in Singapore. He is also one of the most active and awarded (Top Voice) influencers on LinkedIn. Anyone that follows him will receive tremendous value from the content he shares."
            },
            {
              "profile_url": "https://www.linkedin.com/in/tonyabbacchi/",
              "text": "Anthony is a growth minded leader who has an uncanny ability to craft and deploy scalable business strategies that rapidly expand market share, improve company culture and transform organizational leadership for the better. He's extremely tenured in both the B2B and B2C space and aside from being named one of LinkedIn's top Voices for 2018, he's an incredibly humble, compassionate and integrity oriented human being. I have been blessed to work with Anthony in terms of networking and collaborations and have an immense amount of respect for not only the way he conducts himself as a professional but also how he makes a lasting, positive impact on all who he crosses paths with. If you get the opportunity to collaborate, learn from or hire Anthony, don't hesitate as it will be one of the most rewarding experiences you'll encounter. Glad to have him as a friend and peer. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/cbdcp/",
              "text": "AJ is the guy you want on your team. His knowledge of networking, marketing and collaboration is second to none.  As the LinkedIn 2018 Power Profile for Marketing & Advertising I highly recommend you follow his profile."
            },
            {
              "profile_url": "https://www.linkedin.com/in/corywarfield/",
              "text": "Anthony is  prolific thinker, strategic, motivator, connector, and influencer. His efforts on and off line to help companies and entrepreneurs are wide reaching and impactful, and he is a master of his craft. I am honored to have worked with and to recommend Anthony."
            },
            {
              "profile_url": "https://www.linkedin.com/in/kirkfrancis/",
              "text": "Anthony James is someone who has dedicated himself to providing encouragement and support to others. \n\nHis posts, videos, and words are an inspiration to many.  Anthony is extremely professional and personable.  Although we live on different continents, he still manages to check in with me from time to time along with providing support.  For someone I have not met in person, Anthony has far exceeded my expectations and went above and beyond to support me and my success.\n\nThe world needs more people like Anthony James."
            },
            {
              "profile_url": "https://www.linkedin.com/in/janineleafe/",
              "text": "Anthony is a digital transformation expert. His consistency, attention to detail and results speak volumes. Having implemented some of Anthony's strategy to my own business with success I would highly recommend him to anyone seeking his professional services. His approachable and friendly disposition makes working with him a breeze. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/sheri-lally/",
              "text": "Anthony is the kind of guy that you want on your team. Digital in nature, highly creative and has a global perspective on all things innovation. A brilliant communicator and collaborator. It’s no surprise to me that LinkedIn awarded him as the #1 Media Agency voice in Asia Pacific. If you’re looking for a leader with true innovation credentials, he’s the man for your team!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/titia-niehorster/",
              "text": "It’s been a true pleasure to get to know Anthony in this digital world. He is someone who gets innovation on a global scale. He inspires many through his messages and knowledge about technology and\nmodernization. I highly recommend following his profile on LinkedIn"
            },
            {
              "profile_url": "https://www.linkedin.com/in/lisajonessrs/",
              "text": "I have worked closely with Anthony over the past few years and been fortunate enough to experience his creativity and deep understanding of technology. He is super generous with his time and always willing to engage and participate in worthwhile cases. Anthony is also a great storyteller which is reflected in his posts and the articles he publishes on LinkedIn. I highly recommend Anthony as someone to connect with and follow on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/corywarfield/",
              "text": "Anthony is one of the most prolific content curators and innovators on LinkedIn. If you’re not following his feed you’re missing out.\nIf you’re looking for a daily dose of the most innovative ideas, creative marketing solutions, and digital concepts then click the follow button on his profile today. I would definitely recommend following Anthony."
            },
            {
              "profile_url": "https://www.linkedin.com/in/yücel-ulusoy-mba-00698bb6/",
              "text": "It's an honor to have had the great opportunity to connect to Anthony via Linkedin. He has one of the best feeds on LinkedIn. He constantly ensures that his followers learn about the latest technology that can change lives. Anthony is a pioneer in the innovation space.\nAnthony is a top voice to follow on LinkedIn, I highly recommend him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/catherine-de-la-poer/",
              "text": "I was fortunate to spend time with Anthony (AJ) when he was in London on a speaking tour. Over lunch he openly shared his journey on LinkedIn. AJ is exceptionally generous with his time and sharing what has worked and not worked as he has built his network.\nAJ is a powerful master networker. \nI highly recommend following AJ, he is unequivocally LinkedIn’s innovation and marketing top voice. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/chinedujuniorihekwoaba/",
              "text": "I have had the pleasure of connecting with Anthony here on LinkedIn.\n\nHe has one of the best feeds on LinkedIn. If you’re not following him you’re missing the latest and greatest innovative ideas come to the market.\n\nHe is also very humble and affectionate.\nHe is definitely worth following."
            },
            {
              "profile_url": "https://www.linkedin.com/in/mike-podesto/",
              "text": "Anthony is without a shadow of a doubt one of Australia’s top voices on LinkedIn (the #1 in my opinion). If you are not following Anthony and the gold nuggets he posts on LinkedIn then you’re missing out. He shares some of the best content and most innovative ideas.\n\nAnthony is highly collaborative and super creative. His network is one of the most engaged on LinkedIn - take one look at his posts and you will agree.\n\nI am proud to recommend Anthony as an amazing person to follow on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/garydfrey/",
              "text": "Anthony is a content powerhouse. His posts are constantly in my feed and every single one leaves me saying WOW. He even wrote an article on the subject. I have no doubt he leaves his customers saying “wow” all the time.\n\nI would highly recommend checking out Anthony‘s posts and articles here on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/simonchanpmba/",
              "text": "I had the great pleasure of having lunch with Anthony when he was in London in 2017. He shared his experiences of being a LinkedIn Influencer and his engagement strategies with me. Anthony is a proven world leader in the art of B2B social media and a true gent offline too, who has empathy and integrity in spades. A modern master networker and collaborator.  Anthony’s entrepreneurial experience and ability to connect the dots and see solutions in the digital world is what sets him apart from other top voices on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/juliantalbot/",
              "text": "Anthony is someone who understands how to build great collaborative relationships. I am continually inspired by his creativity and the never ending supply of amazing innovations he shares here on LinkedIn . Anthony is among the most collaborative connections I have interacted with on this platform. Always open and willing to share insights and engage with others. He has his finger on the pulse of future technology. His posts leave me constantly in a state of 'WOW'. This is why I have no hesitation in recommending Anthony to anyone seeking an innovative thinker, a curious minded creative, and a generous open collaborator."
            },
            {
              "profile_url": "https://www.linkedin.com/in/medfuel/",
              "text": "Anthony is a collaborative, experienced, passionate, and clear leader in the digital and innovation space, and I am so grateful to have him as part of my LinkedIn network!\nAs somebody who helps teams and individuals leverage the power of LinkedIn, Anthony‘s is one profile and feed that leverages this power and then some. He shows us on a daily basis incredible digital and business ideas. He also writes extensively about how this innovation can be applied to your business.\nI would highly recommend Anthony and his work here on LinkedIn, he is a top voice worth following."
            },
            {
              "profile_url": "https://www.linkedin.com/in/nataliawiechowski/",
              "text": "Having interacted and engaged with Anthony here on LinkedIn, I have found him to be a true visionary and creative thought-leader in the innovation space. The way he curates and produces content, shares ideas and collaborates with his network makes Anthony someone definitely worth following on LinkedIn. He’s one of the top voices in Australia that I follow."
            },
            {
              "profile_url": "https://www.linkedin.com/in/andrada-anitei/",
              "text": "- English - \n\n\nIt's an honor to have had the great opportunity to connect to Anthony via Linkedin. His activity adds an instant value, due to the innovative projects he highlights; in the same time, community is a very important aspect to him, thoroughly proven by the amazing insights we are fortunate to discover each time his posts come up. \n\n\nAs a human, he constantly ensures that his followers learn about the latest technology that can change lives. \n\n\nAs a professional, he is a passionate networker and collaborator who brings a real energy to every discussion. He is a leading influencer in Australia and his posts stand out throughout \"background noise\". \n\n\nFollow him and avoid missing out important outlines of everyday life! \n\n\n- Romanian - \n\n\nSunt onorata de a fi avut minunata ocazie de a ma număra printre contactele lui Anthony, prin intermediul LinkedIn. Datorita proiectelor inovative pe care le expune, activitatea sa poate fi considerata o reala valoare adăugata; in același timp, comunitatea reprezinta un aspect foarte important pentru dumnealui, lucru dovedit in mod constant prin ideile pe care avem norocul de a le descoperi cu fiecare postare a sa. \n\n\nCa si om, are grija ca cei ce ii urmaresc activitatea sa afle despre ultimele noutati din domeniul tehnic, create pentru a aduce o schimbare in viata oamenilor. \n\n\nAnthony este un influencer de top in Australia, iar activitatea sa rupe monotonia “zgomotului de fundal”. Ca si om de business, este un colaborator si un networker pasionat si energetic.\n\n\nAbonati-va la postarile sale si aflati printre primii despre inovatii ce servesc diverselor aspecte importante ale vietii de zi cu zi.\n\n"
            },
            {
              "profile_url": "https://www.linkedin.com/in/dinopacellaofficial/",
              "text": "Anthony is a pioneer in the innovation space. His entrepreneurial mindest set is driving the digital agenda across Australia and Asia Pacific. I am fortunate, to have had the privilege of meeting this inspirational futurist face-to-face. His passion and energy for adding value to his network is extraordinary. \nAnthony is a top voice to follow on LinkedIn, I highly recommend him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/talalalmurad/",
              "text": "It’s been a pleasure to get to know Anthony here on LinkedIn. He’s the guy to go to for digital ideas. Somebody definitely worth following on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/that-startup-guy/",
              "text": "I have been fortunate to meet AJ in the real world on a number of occasions, and he is as genuine, real and collaborative as he is here on LinkedIn. A consummate networker and great person to have in your network. I am looking forward to collaborating with him on our upcoming events! \nI highly recommend following ‘top voices’ like Anthony here on LinkedIn."
            },
            {
              "profile_url": "https://www.linkedin.com/in/doylebuehler/",
              "text": "Anthony is the real deal - friend, colleague, thought-leader. You just need to look at AJs LinkedIn feed to know this is a person who understands and gets, technology, innovation and digital solutions, and always presents some great new ideas and concepts that I wish I had found! He is a fantastic networker, always quick to jump in and collaborate or connect the dots and make introductions. I highly recommend that you follow him, as one of the most influential voices in Australia. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/chloehacquard/",
              "text": "Anthony J James is one of the most creative and innovative top voices in Australia, arguably Asia Pacific. He constantly shares new and innovative ideas and concepts from around the world. Ideas that constantly make me say... WOW! \nif you are looking for a highly active, highly networked, visionary and evangelist in the technology and digital space Anthony is definitely the person to be following on LinkedIn.\nChloé Hacquard \nAnthony J James est l’une des personnes les plus créatives et innovantes en Australie, et de la région de l’Asie Pacifique. \nIl partage constamment des idées nouvelles, innovantes et des concepts provenant de partout dans le monde. Ces idées qui sans cesse me font dire... WOW ! \nSi vous cherchez une personne très active , connectée en réseau, visionnaire et un évangéliste des technologies et de l’espace numérique alors Anthony est certainement la personne à suivre sur LinkedIn.\nChloé Hacquard \n"
            },
            {
              "profile_url": "https://www.linkedin.com/in/kathrynsforcina/",
              "text": "I had the pleasure of meeting Anthony J James (better known as AJ) when he was speaking at World Forum Disrupt Sydney on future technologies and innovation. AJ has an amazing grasp on digital technologies and their impact on consumers and brands across the globe. If you’re looking for somebody with true innovation and commercialisation prowess, then go no further than AJ"
            },
            {
              "profile_url": "https://www.linkedin.com/in/csaba-hegyi-cio/",
              "text": "AJ is a unique individual who combines business acumen, creativity and strategic prowess. He has the ability to create the most innovative ideas that sell. He consistently delivers a truly inspiring and integrated approach to leadership and execution in everything he does. AJ's thought-leadership in the innovation and transformation arena is second to none. His success in both big corporate and global agencies is no surprise."
            },
            {
              "profile_url": "https://www.linkedin.com/in/rajkgrover/",
              "text": "Anthony J James (better known as ‘AJ’) is an outstanding communicator and networker. He has exceptional expertise in innovation, marketing, consumer engagement solutions, and business transformation. His passion and drive for thought-leadership in these areas sets him apart from others on LinkedIn.\n\nHe consistently demonstrates a solid and collaborative approach to all things he does as well as a true dedication to success. \n\nAJ always leads by example - his enthusiasm and dedication are both inspiring and highly-motivating. Whenever I have had a challenge or a question, there has never been a time he has left me without a solution. No matter how complex the problem is, he will always come up with brilliant, creative, innovative, elegant, and cost-effective solutions. He is highly professional in everything he does. AJ is definitely worth recommending. Wish you all the best, AJ!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/audreynormannicoll/",
              "text": "Anthony J James (better known as AJ) is the most creative and innovative business thinkers I have ever met. With the ability to quickly understand global positioning, develop strategy and develop breakthrough ideas and concepts never before seen. What makes him unique is his ideas have real commercial application which can be implemented and executed. I have never seen growth (both in marketshare and revenue) as many of the creative business ideas he has brought to market.\r\n\r\nI have worked with AJ from more than 3 years now, and collaborated on many successful projects. I am particularly impressed by AJ's ability to lead from the front, at both Board and CxO levels, and in front of clients. He is a pitch specialist. Clients continually want more of his time on their account.\r\n\r\nHis global credibility as well as his strong collaboration and communication skills made his one of the best leaders and mentors I have worked with. I have no hesitation in recommending AJ in a creative, innovation, global leadership role. Any organisation would be lucky to have him on their leadership team."
            },
            {
              "profile_url": "https://www.linkedin.com/in/akshayabhatia/",
              "text": "Having worked and interacted with Anthony J James, i found him a great visionary and highly creative both in thoughts and action. His approach in finding online as well offline digital solutions has always been very innovative. He is a great networker and open to fresh insights from others. He is a prolific writer and shares his valuable ideas with confidence and without any inhibition. Surely, he will be a great asset to any organization which engages him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/jithoong/",
              "text": "I've worked with AJ on a number of projects and admire his focus as well as clear thinking in delivering what's best for our clients. Sometimes technology can be daunting but AJ explained it well making it simple for clients to buy into the idea.\r\n\r\nIf there's an opportunity, I would gladly work with AJ again."
            },
            {
              "profile_url": "https://www.linkedin.com/in/kevinleightonau/",
              "text": "I had the wide-eyed experience of working with AJ in one of the best experiences of my career. AJ was then and is now, unique. Then (circa 2001) AJ was ahead of his time in positioning company value propositions. To this day many companies are yet to embrace AJ's first generation strategies, things he has continued to mature into a globally relevant and influential portfolio of marketing and business strategy IP. I'm fortunate to maintain the collegiate relationship, memories of the earlier days, and the opportunity to try and keep up today. I hope you get the same opportunity going forward. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/neilholt/",
              "text": "Although I only worked with AJ for a short period of time I feel like I've known him for years. He is a great thinker, a smart operator and one of the good guys. It was a true pleasure working with him and I'm sure our paths will cross again sometime in the future - I look forward to it."
            },
            {
              "profile_url": "https://www.linkedin.com/in/rowanavis/",
              "text": "AJ is a pioneering talent. His visionary mindset combined with Entrepreneurial skill set is driving the digital capability of the industry across Australia and Asia. I am fortunate, to have had the privilege to work with such an inspirational Futurist"
            },
            {
              "profile_url": "https://www.linkedin.com/in/karenlumsee/",
              "text": "Despite constantly claiming he was not an ad guy, AJ was quickly able to articulate and realise the brand problem and then identify innovative, out of the box-solutions -- maybe not an ad in the true sense of the word - but definitely creative! While at DDB we built a strong working relationship which supported each other to excel and succeed. I very much appreciated the support he gave me in my role, and as a brand ambassador for DDB he was excellent. "
            },
            {
              "profile_url": "https://www.linkedin.com/in/laurenahearn/",
              "text": "AJ was a great sounding board and mentor during our working relationship.  Having worked all over the world - he is the embodiment of the global marketer and his understanding and intuition about true innovation is spot-on.  He’s also an all-around nice person with a great sense of humor ;)  I look forward to working with him again in the future."
            },
            {
              "profile_url": "https://www.linkedin.com/in/isseimatsui/",
              "text": "I did a tremendous works with Anthony J James (AJ) who not only has strong leadership, but also has experitise and experience in agency growth, new market penetration and revenue growth. AJ is an exceptional innovation and creative thinker. He has demonstrated many times in the Japanese market the ability to go beyond the client brief and truly understand the business problems and challenges faced, and creatively develop solutions that provide true competitive advance. Mostly he is very proactive.\r\nAJ has the ability to attract new clients through his start-up and high-growth thinking. I would really want to keep working with him throughout my life."
            },
            {
              "profile_url": "https://www.linkedin.com/in/philromans/",
              "text": "Exceptional passionate, results driven Innovation and Growth specialist. AJ brings energy to every discussion, new ideas to every meeting and builds compelling relationships."
            },
            {
              "profile_url": "https://www.linkedin.com/in/stuartnyman/",
              "text": "AJ is a rare breed in this industry, he is one of the most genuine senior executives I have worked with in my 15+ years in the marketing industry. He has an amazing combination of charm, personal warmth, strategic and creative dexterity, he's a great guy to have around!\r\n\r\nHe is a sponge for new information and is relentless in finding the source of opportunities that have positive brand and business impact, then pursuing it through to completion.\r\n\r\nThere are few people you will meet of his calibre. AJ is someone i would work with again in a heartbeat! "
            },
            {
              "profile_url": "https://www.linkedin.com/in/benjamin-deregt-8a594930/",
              "text": "AJ is a true marketing whiz and an absolute pleasure to work alongside, from the planning and creativity stages to execution and post project evaluation. It is rare to have a experienced Marketer who is happy to grapple with the challenges that arise along a marketing campaign, and AJ does it with fervor and diligence. I have no hesitation in highly recommending AJ. A as a professional you won’t find a better marketing figurehead and as a colleague you won’t find a more loyal team player."
            },
            {
              "profile_url": "https://www.linkedin.com/in/benjamin-deregt-8a594930/",
              "text": "AJ is a true marketing whiz and an absolute pleasure to work alongside, from the planning and creativity stages to execution and post project evaluation. It is rare to have a experienced CMO who is happy to grapple with the challenges that arise along a marketing campaign, and AJ does it with fervor and diligence. I have no hesitation in highly recommending AJ. As a professional you won’t find a better marketing figurehead and as a colleague you won’t find a more loyal team player."
            },
            {
              "profile_url": "https://www.linkedin.com/in/gordondurich/",
              "text": "AJ is an exceptionally talented ideas and tech. guy. He is a pleasure to work with. I would recommend him in a New York minute."
            },
            {
              "profile_url": "https://www.linkedin.com/in/kiley-charteris-947ab129/",
              "text": "AJ makes an immediate impact with any project he takes on.  He always has his eye on the end goal and is driven in his approach, which makes him a great addition to any team or organisation.  His willingness to discuss and debate strategies demonstrates his passion for constant improvement and the respect he has for colleagues at all levels.\r\n\r\nLike any true creative, he thinks outside of the box and you come away from any interaction with him having learned something new.\r\n\r\nAside from his sales and creative acumen, he is all round great guy."
            },
            {
              "profile_url": "https://www.linkedin.com/in/julie-duran-335113/",
              "text": "AJ is such a brilliant and thought provoking partner to work with.   He is able to quickly access situations and readily provide solutions that change the dynamics of the business he is working with.  He is refreshingly direct and responsive to the needs of his clients.\r\nIt was a great pleasure to work with him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/martin-caddick-508801/",
              "text": "I worked in Fujitsu Consulting Marketing in UK/Europe during the rebranding and times of rapid change - I remain proud of our achievements from this time. Anthony was an important part of this and he was a pleasure to work with bringing energy and ideas to the international stage - he was quick to share and easy to relate to."
            },
            {
              "profile_url": "https://www.linkedin.com/in/vincent-parrinello-3069301/",
              "text": "I worked with Anthony in the early stages of Sample Lab. I saw him as having a passionate, entrepreneurial, and strategic approach to business. He's a big thinker who has the ability to bring it down to the details of how all channels connect to achieve tangible business goals. We look forward to working with him and his team on future endevours."
            },
            {
              "profile_url": "https://www.linkedin.com/in/burda/",
              "text": "It's a pleasure to get to know Anthony in the digital world.  Simply put, Anthony is the man to go to -- he just gets it.  Highly recommend him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/neil-docherty-ab10654/",
              "text": "AJ  was a high performing marketeer at DMR with advanced, creative ideas and very high delivery standards, In the right role AJ would be a valued addition to any marketing and creative team. Very professional and demanding of high standards of those around him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/gordondurich/",
              "text": "Anthony James a.k.a. \"A.J\" is a brilliant bloke with internal stamina, drive, creativity and an amazing maturity, which impressed me when we collaborated in Sydney, on design projects and were always great mates. \r\nI am so thrilled we have reconnected via Linked In. He's no garden variety business maestro and loyal and trustworthy bud."
            },
            {
              "profile_url": "https://www.linkedin.com/in/peterirvinekingdommomentum/",
              "text": "Anthony James is passionate about retail and his track record shows he continually provides innovative ideas in the FMCG and retail category.Through his knowledge leadership abilities he can motive and empower his team to grow and use creative ways of tapping into the changing marketplace.\r\nPeter Irvine\r\nCo-Founder\r\nGloria Jean's Coffees"
            },
            {
              "profile_url": "https://www.linkedin.com/in/servantofchaos/",
              "text": "Under the executive direction of Anthony James, Sample Central has been transformed from a one-country success into a breakthrough global retail innovation.  \r\n\r\nWith a focus on customer experience and capturing the data behind buying behaviour, Anthony has created a new category and go-to-market model within the retail sector. \r\n\r\nHis ability to work with franchisors/owners spread across the globe - and the necessary challenges that come with such complex stakeholder environments - have been core to his retail success."
            },
            {
              "profile_url": "https://www.linkedin.com/in/kayepomarancwhite/",
              "text": "Anthony J is a wonderful, hard-working creative officer with keen, strategic long-range vision. He has enormous breadth and is expert in a wide range of work areas. He can work completely independently or, as an insightful and definitive manager. AJ is articulate and present with clients. If you need someone to help with direction, creatvitiy and vision, AJ is the man you want on your team."
            },
            {
              "profile_url": "https://www.linkedin.com/in/flaviotanabe/",
              "text": "AJ is the former Chief Creative Officer from Creata.\r\nAs his direct contact overseas, in Brazil agency, I could put all the confidence on him due to managing skills and outstanding creativity."
            },
            {
              "profile_url": "https://www.linkedin.com/in/johnbankscom/",
              "text": "Focussed and creative at the same time. A rare skill."
            },
            {
              "profile_url": "https://www.linkedin.com/in/revill/",
              "text": "Anthony (AJ) created CSC's MultiMedia Group both in Australia and globally and his talents and leadership were highly prized and respected by Directors of the company.  His passionate interest in multimedia and web marketing were only matched by his superb presentation skills."
            },
            {
              "profile_url": "https://www.linkedin.com/in/jeffrushton/",
              "text": "Anthony did some amazing work on marketing, position and product strategy that was very helpful in articulating our new strategic direction"
            },
            {
              "profile_url": "https://www.linkedin.com/in/gavin-thwaites/",
              "text": "AJ is a focused sales professional, with a determined passion to achieve.  I had the pleasure of working with him for 9 months, and would gladly recommend him."
            },
            {
              "profile_url": "https://www.linkedin.com/in/jeffwallace913/",
              "text": "AJ is a hard-driving, results-oriented executive capable of managing multiple projects simultaneously.  He is VERY dedicated to his employer/clients and works tirelessly for their best interests.  He is very open and honest in his communications and very creative in his thinking."
            },
            {
              "profile_url": "https://www.linkedin.com/in/marcus-naylor-a4bb57/",
              "text": "AJ provides a great combination of creative content married with a realistic understanding of business constraints that must be worked within. AJ delivers excellent creativity as well as the ability to think creatively to meet challenges and restrictions that arise as part of the concept development process. I worked with AJ whilst at the Kellogg Company and he is very capable of working with Blue Chip clients on multi national promotional briefs (pan European promotions with me). His service is built around delivering against consumer insight whilst meeting the key corporate objectives. The time I have spent working with AJ has been stimulating and a great learning process for me - he has in depth knowledge and insight which he is able to share in a relaxed way as a good team player. He presents his concepts and ideas very well - even to a multi-cultural audience. He is good fun to work with too!"
            },
            {
              "profile_url": "https://www.linkedin.com/in/dinaellithorpe/",
              "text": "“I was fortunate enough to work with AJ at Creata Promotion on the McDonald’s account.  He is a highly strategic professional who is exceptional at creating a vision.  AJ worked closely with clients to develop solutions to several complex challenges, I found him to be committed to a team-approach, highly collaborative, honest and innovative. On all projects, AJ brought creative and relevant ideas to the table that could be executed.  His knowledge, passion and intellect for technology distinguish him from others since he knows how to apply it masterfully within the overall mix.  He has a high level of integrity, great people skills and is one of the finest people I’ve had the pleasure of working with.”"
            },
            {
              "profile_url": "https://www.linkedin.com/in/manojkheerbat/",
              "text": "I know AJ from our time at DMR / Fujitsu Consulting. At that time AJ was bringing DMR/Fujitsu to a new level of operation through a strong focus on internal and external brand management and consistent and focussed marketing messages. I know AJ to be a passionate and knowledgeable individual in his area of expertise. He is a strong communicator and able to paint a clear vision to his team and colleagues. He backs this up with an attention to detail that ensures consistent success in delivery."
            },
            {
              "profile_url": "https://www.linkedin.com/in/nicolai-truhin-3b8a59/",
              "text": "Worked closely with Anthony for several years at IBM Global Services - eBusiness division. Have remained in close friendship since moving on from IBM."
            },
            {
              "profile_url": "https://www.linkedin.com/in/mikemaddaloni/",
              "text": "AJ was instrumental with instructing key management and staff in my office on Internet and multimedia technologies and how we could leverage both them and his own work to offer critical solutions to our existing clients.  On a personal level, he was a trusted adviser and mentor as I made a career transition from traditional mainframe computing to the Internet and continues to do so today, where his experience and thought leadership based on his own experiences continue to support my own endeavors."
            }
          ],
          "message": "ok"
        }
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Years of Experience
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-year-of-experiences') and
            i.nice_name == "Get Years of Experience")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "current_company": "Bill & Melinda Gates Foundation",
            "current_company_join_month": null,
            "current_company_join_year": 2000,
            "current_job_title": "Co-chair",
            "time_spent_at_current_company": "23 yrs 10 mos",
            "years_of_experience": "48 yrs 10 mos"
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Open to Work Status
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-opentowork-status') and
            i.nice_name == "Get Open to Work Status")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "open_to_work": false
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Open Profile Status
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-open-profile-status') and
            i.nice_name == "Get Open Profile Status")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "open_profile": false
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Profile PDF CSV
        # Freshdata | Fresh LinkedIn Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-profile-pdf-cv') and
            i.nice_name == "Get Profile PDF CSV")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "base64encoded_pdf": "data:application/pdf;base64,JVBERi0xLjQKJaqrrK0KMSAwIG9iago8PAovVGl0bGUgKFJlc3VtZSkKL0F1dGhvciAoTGlua2VkSW4pCi9TdWJqZWN0IChSZXN1bWUgZ2VuZXJhdGVkIGZyb20gcHJvZmlsZSkKL1Byb2R1Y2VyIChBcGFjaGUgRk9QIFZlcnNpb24gMi4yKQovQ3JlYXRpb25EYXRlIChEOjIwMjMwNTIzMDMzNTE2WikKPj4KZW5kb2JqCjIgMCBvYmoKPDwKICAvTiAzCiAgL0xlbmd0aCAzIDAgUgogIC9GaWx0ZXIgL0ZsYXRlRGVjb2RlCj4+CnN0cmVhbQp4nO2ZZ1AU2RqGT3dPDgzMDEOGIQ5BooQBJOckQbKowAwZRhiSAiZkcQVWEBFJiiCigAuuLkFWURHFgCgoYEB3kEVAWRdXERWVHfTH3qp76966P2/d+X6cfurtU/X16T5V/VQdAGTHEzlJqbABAEm8NL6fiz0zOCSUiR0FJCAPqAALGBGc1GQ7Hx9PIKyVueCf6t0ogFau93T/9f1/W0RuEo8LAIQTcjw3KpUj5DQhx3KTuCv5+ApnpiULM9hRyHS+8AGFHLzCkd84cYVjvvHOr3P8/RyEXAYAjhTzlQlHVzjyK1NPrTAnlp8EgGyXcL7at75fS1xzZRHMOF5aFJ8Xkaj1Xy7nP9c/9BJLXXnhkelxiWm6cbz/0T4r++UbvbH6ug8gRsXf2WbhN2C/AgAp+TtTOwwAZTcAHT1/Z5HHAegsAUD6KSedn/EtQ60MaEAAFEAHMkARqAJNoAuMgBmwBLbACbgDb+APQsBGwAGxIAnwQSbIAbtAPigEJeAgqAK1oAE0gVZwBnSC8+AyuAZugbtgBDwGAjAFXoJ58A4sQRCEhcgQDZKBlCB1SAcygtiQNeQEeUJ+UAgUDsVAPCgdyoF2Q4VQKVQF1UFN0E/QOegydAMagh5CE9As9Cf0EUZgEkyHFWANWB9mw3awB+wPb4Bj4BQ4C86D98EVcD18Cu6AL8O34BFYAL+EFxCAEBEGoozoImzEAfFGQpFohI9sRwqQcqQeaUW6kX7kHiJA5pAPKAyKhmKidFGWKFdUAIqDSkFtRxWhqlAnUR2oPtQ91ARqHvUFTUbLo3XQFmg3dDA6Bp2JzkeXoxvR7eir6BH0FPodBoNhYFgYM4wrJgQTj8nGFGEOY9owlzBDmEnMAhaLlcHqYK2w3tgIbBo2H1uJPYW9iB3GTmHf44g4JZwRzhkXiuPhcnHluGZcD24YN41bwovj1fEWeG88F78VX4xvwHfj7+Cn8EsECQKLYEXwJ8QTdhEqCK2Eq4RxwhsikahCNCf6EuOIO4kVxNPE68QJ4gcSlaRNciCFkdJJ+0gnSJdID0lvyGSyBtmWHEpOI+8jN5GvkJ+S34vRxPTE3MS4YjvEqsU6xIbFXlHwFHWKHWUjJYtSTjlLuUOZE8eLa4g7iEeIbxevFj8nPia+IEGTMJTwlkiSKJJolrghMUPFUjWoTlQuNY96jHqFOklDaKo0BxqHtpvWQLtKm6Jj6Cy6Gz2eXkj/kT5In5ekShpLBkpukayWvCApYCAMDYYbI5FRzDjDGGV8lFKQspOKktor1So1LLUoLSdtKx0lXSDdJj0i/VGGKeMkkyCzX6ZT5oksSlZb1lc2U/aI7FXZOTm6nKUcR65A7ozcI3lYXlveTz5b/pj8gPyCgqKCi0KyQqXCFYU5RYairWK8Yplij+KsEk3JWilOqUzpotILpiTTjpnIrGD2MeeV5ZVdldOV65QHlZdUWCoBKrkqbSpPVAmqbNVo1TLVXtV5NSU1L7UctRa1R+p4dbZ6rPoh9X71RQ2WRpDGHo1OjRmWNMuNlcVqYY1rkjVtNFM06zXva2G02FoJWoe17mrD2ibasdrV2nd0YB1TnTidwzpDq9CrzFfxVtWvGtMl6drpZui26E7oMfQ89XL1OvVe6avph+rv1+/X/2JgYpBo0GDw2JBq6G6Ya9ht+KeRthHHqNro/mryaufVO1Z3rX5trGMcZXzE+IEJzcTLZI9Jr8lnUzNTvmmr6ayZmlm4WY3ZGJvO9mEXsa+bo83tzXeYnzf/YGFqkWZxxuIPS13LBMtmy5k1rDVRaxrWTFqpWEVY1VkJrJnW4dZHrQU2yjYRNvU2z2xVbbm2jbbTdlp28Xan7F7ZG9jz7dvtFx0sHLY5XHJEHF0cCxwHnahOAU5VTk+dVZxjnFuc511MXLJdLrmiXT1c97uOuSm4cdya3Obdzdy3ufd5kDzWeVR5PPPU9uR7dnvBXu5eB7zG16qv5a3t9Abebt4HvJ/4sHxSfH7xxfj6+Fb7Pvcz9Mvx619HW7dpXfO6d/72/sX+jwM0A9IDegMpgWGBTYGLQY5BpUGCYP3gbcG3QmRD4kK6QrGhgaGNoQvrndYfXD8VZhKWHza6gbVhy4YbG2U3Jm68sImyKWLT2XB0eFB4c/inCO+I+oiFSLfImsh5jgPnEOcl15Zbxp2NsooqjZqOtooujZ6JsYo5EDMbaxNbHjsX5xBXFfc63jW+Nn4xwTvhRMJyYlBiWxIuKTzpHI/KS+D1bVbcvGXzULJOcn6yIMUi5WDKPN+D35gKpW5I7UqjC3/MA+ma6d+lT2RYZ1RnvM8MzDy7RWILb8vAVu2te7dOZzlnHc9GZXOye3OUc3blTGyz21a3Hdoeub13h+qOvB1TO112ntxF2JWw63auQW5p7tvdQbu78xTyduZNfufyXUu+WD4/f2yP5Z7a71Hfx30/uHf13sq9Xwq4BTcLDQrLCz8VcYpu/mD4Q8UPy/ui9w0WmxYfKcGU8EpG99vsP1kqUZpVOnnA60BHGbOsoOztwU0Hb5Qbl9ceIhxKPySo8KzoqlSrLKn8VBVbNVJtX91WI1+zt2bxMPfw8BHbI621CrWFtR+Pxh19UOdS11GvUV9+DHMs49jzhsCG/uPs402Nso2FjZ9P8E4ITvqd7Gsya2pqlm8uboFb0ltmT4Wduvuj449drbqtdW2MtsLT4HT66Rc/hf80esbjTO9Z9tnWn9V/rmmntRd0QB1bO+Y7YzsFXSFdQ+fcz/V2W3a3/6L3y4nzyuerL0heKO4h9OT1LF/MurhwKfnS3OWYy5O9m3ofXwm+cr/Pt2/wqsfV69ecr13pt+u/eN3q+vkbFjfO3WTf7LxleqtjwGSg/bbJ7fZB08GOO2Z3uu6a3+0eWjPUM2wzfPme471r993u3xpZOzI0GjD6YCxsTPCA+2DmYeLD148yHi093jmOHi94Iv6k/Kn80/pftX5tE5gKLkw4Tgw8W/fs8SRn8uVvqb99msp7Tn5ePq003TRjNHN+1nn27ov1L6ZeJr9cmsv/XeL3mlear37+w/aPgfng+anX/NfLfxa9kXlz4q3x294Fn4Wn75LeLS0WvJd5f/ID+0P/x6CP00uZn7CfKj5rfe7+4vFlfDlpeVnkAiIXELmAyAVELiByAZELiFxA5AIiFxC5gMgFRC4gcgGRC/wfu8DXsxthISvDsTEA/LMB8LwNQGUVABrRAFDC/gJ4igM0CmVuZHN0cmVhbQplbmRvYmoKMyAwIG9iagoyNDE5CmVuZG9iago0IDAgb2JqClsvSUNDQmFzZWQgMiAwIFJdCmVuZG9iago1IDAgb2JqCjw8CiAgL1R5cGUgL01ldGFkYXRhCiAgL1N1YnR5cGUgL1hNTAogIC9MZW5ndGggNiAwIFIKPj4Kc3RyZWFtCjw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+PHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyI+CjxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CjxyZGY6RGVzY3JpcHRpb24geG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiByZGY6YWJvdXQ9IiI+CjxkYzpkZXNjcmlwdGlvbj5SZXN1bWUgZ2VuZXJhdGVkIGZyb20gcHJvZmlsZTwvZGM6ZGVzY3JpcHRpb24+CjxkYzpjcmVhdG9yPkxpbmtlZEluPC9kYzpjcmVhdG9yPgo8ZGM6Zm9ybWF0PmFwcGxpY2F0aW9uL3BkZjwvZGM6Zm9ybWF0Pgo8ZGM6dGl0bGU+UmVzdW1lPC9kYzp0aXRsZT4KPGRjOmxhbmd1YWdlPmVuPC9kYzpsYW5ndWFnZT4KPGRjOmRhdGU+MjAyMy0wNS0yM1QwMzozNToxNlo8L2RjOmRhdGU+CjwvcmRmOkRlc2NyaXB0aW9uPgo8cmRmOkRlc2NyaXB0aW9uIHhtbG5zOnBkZj0iaHR0cDovL25zLmFkb2JlLmNvbS9wZGYvMS4zLyIgcmRmOmFib3V0PSIiPgo8cGRmOlByb2R1Y2VyPkFwYWNoZSBGT1AgVmVyc2lvbiAyLjI8L3BkZjpQcm9kdWNlcj4KPHBkZjpQREZWZXJzaW9uPjEuNDwvcGRmOlBERlZlcnNpb24+CjwvcmRmOkRlc2NyaXB0aW9uPgo8cmRmOkRlc2NyaXB0aW9uIHhtbG5zOnBkZnVhaWQ9Imh0dHA6Ly93d3cuYWlpbS5vcmcvcGRmdWEvbnMvaWQvIiByZGY6YWJvdXQ9IiI+CjxwZGZ1YWlkOnBhcnQ+MTwvcGRmdWFpZDpwYXJ0Pgo8L3JkZjpEZXNjcmlwdGlvbj4KPHJkZjpEZXNjcmlwdGlvbiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHJkZjphYm91dD0iIj4KPHhtcDpNZXRhZGF0YURhdGU+MjAyMy0wNS0yM1QwMzozNToxNlo8L3htcDpNZXRhZGF0YURhdGU+Cjx4bXA6Q3JlYXRlRGF0ZT4yMDIzLTA1LTIzVDAzOjM1OjE2WjwveG1wOkNyZWF0ZURhdGU+CjwvcmRmOkRlc2NyaXB0aW9uPgo8L3JkZjpSREY+CjwveDp4bXBtZXRhPjw/eHBhY2tldCBlbmQ9InIiPz4KCmVuZHN0cmVhbQplbmRvYmoKNiAwIG9iagoxMDQwCmVuZG9iago3IDAgb2JqCjw8IC9VUkkgKGh0dHBzOi8vd3d3LmxpbmtlZGluLmNvbS9pbi93aWxsaWFtaGdhdGVzP2pvYmlkPTEyMzQmbGlwaT11cm4lM0FsaSUzQXBhZ2UlM0FkX2pvYnNfZWFzeWFwcGx5X3BkZmdlbnJlc3VtZSUzQlp3QTBxWFNZVHJXUmk3dUhxeGp1RVElM0QlM0QmbGljdT11cm4lM0FsaSUzQWNvbnRyb2wlM0FkX2pvYnNfZWFzeWFwcGx5X3BkZmdlbnJlc3VtZS12MDJfcHJvZmlsZSkKL1MgL1VSSSA+PgplbmRvYmoKOCAwIG9iago8PCAvVHlwZSAvQW5ub3QKL1N1YnR5cGUgL0xpbmsKL1JlY3QgWyAyMS42IDcwNC4wODcgMTkwLjI0MSA3MTQuMzk0IF0KL0MgWyAwIDAgMCBdCi9Cb3JkZXIgWyAwIDAgMCBdCi9BIDcgMCBSCi9IIC9JCi9TdHJ1Y3RQYXJlbnQgMQoKPj4KZW5kb2JqCjkgMCBvYmoKPDwgL1R5cGUgL0Fubm90Ci9TdWJ0eXBlIC9MaW5rCi9SZWN0IFsgMjEuNiA2ODkuNjg3IDcwLjQ5NSA2OTkuOTk0IF0KL0MgWyAwIDAgMCBdCi9Cb3JkZXIgWyAwIDAgMCBdCi9BIDcgMCBSCi9IIC9JCi9TdHJ1Y3RQYXJlbnQgMgoKPj4KZW5kb2JqCjEwIDAgb2JqCjw8IC9VUkkgKGh0dHBzOi8vZ2F0ZXNub3QuZXMvbGlua2VkaW4pCi9TIC9VUkkgPj4KZW5kb2JqCjExIDAgb2JqCjw8IC9UeXBlIC9Bbm5vdAovU3VidHlwZSAvTGluawovUmVjdCBbIDIxLjYgNjc2LjIxMiAxNzIuNTQyIDY4Ni41MTkgXQovQyBbIDAgMCAwIF0KL0JvcmRlciBbIDAgMCAwIF0KL0EgMTAgMCBSCi9IIC9JCi9TdHJ1Y3RQYXJlbnQgMwoKPj4KZW5kb2JqCjEyIDAgb2JqClsxMyAwIFIgMTQgMCBSIDE1IDAgUiAxNiAwIFIgMTcgMCBSIDE4IDAgUiAxOSAwIFIgMjAgMCBSIDIxIDAgUiAyMiAwIFIgMjIgMCBSIDIyIDAgUiAyMyAwIFIgMjQgMCBSIDI1IDAgUiAyNiAwIFIgMjcgMCBSIDI4IDAgUiAyOSAwIFIgMzAgMCBSIDMxIDAgUiAzMiAwIFIgMzMgMCBSIDM0IDAgUiAzNSAwIFIgMzYgMCBSIDM3IDAgUiAzOCAwIFIgMzkgMCBSXQplbmRvYmoKNDAgMCBvYmoKPDwgL0xlbmd0aCA0MSAwIFIgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCniczVjbahw5EH3vr+gfiCyV7mAMc90LG9gQQx5CHkJ2bcKOzdoE9ve3SlPqVks9N6/ZhKHpbo26LqeOqkp66lQv8feGbj5C/+Whe8IfjT30IJWITkrp8XVXvtLUHX+ySxJ2/YfusbtaPH/7evf5y7du+XbVSaGcDL0UYLSiW3C6f75P0ithz3/2d90Gv3mH/95Xcpa33dVW2V5Bf3tXWqyk0MqgEKX724f+47WUWt586m9/7Ta3SdwTT1esEB/RxbPEg9RC24DCvTpD0zv8jdpkb7QY4BxsUIIteOre8MtDrwIKJyhUwrF4tR6EBisVobz/YGboMvDzN0UACpllHEQIYPDLqLSnm9ZJwNXPqr++vnq7+mXdy5ubbrkuINR1hJRQXqMWbTJukl4JSotXMgCvQM8TPBXR4Levj38NylStTFXKDAhDQVLGDcpicS3wWuK1YuVrvDZ4bYuxBRtDYigGavwvPUd+XxayPM8Fogc75PaylZk4JYVzQGC6aCgonqAlTN///flxcBROOWqdCErHGFXIjioy0M07pzw7EFqEJ4r1KcWeeBQnCLceswGGxxbjeELwaARegJY5bnT0yEDUrd2c9RS4BF1kKxfsQfbC7y2uoCuXOoAWlpe1FDKGfrpGbGUfuApUwNVnfCLQAGoGKdOMzFwdpdbV74NGVyNS503MTTbxJ7arEvYLgMictK0YlDVbMWfZhu9bDmcZ4i3LmfVgP06qSDeo6pvMZzNHDeLEfem2P+W2DZjLpvkBgE3O6hybvxldBmZ4+hSKfKB5PnNlmJ+5sxpdTS4p1ufk8RzBHBo9C7VnVnhbORedsBqlgp04R5iqve69Ewuacog58RSECskqL6RO0k3hdfzseE6mzXejFGenQ/M3tf2HYFNNHWxwMxhWMs5bXy5ytSj4tx6xSeNsD/Es4UV2ciofcpWmcI5+lLEAd45PBc4rjh/rznkQ8rrIWOX6uJBj8V4V9nIMJr6VuhcHcWxKfIMjruEaR8DcDQu2YVtwjO2DbMeytIF9iWw/82KYS/9lPhqOgT7sw6T1wv5ZWAn9T93HT2jzH1gk/sG2VgVctmS7xaZPO+ECrqNQDu/691haalCadmBm9QM2WoGWv3VDESGuAPm0LuxesX+W/d4caJepLNl9B1va0nQITYCw3CYC6OPF7P8vGaUbbc8gakS1xr4hZbR4XqKbKpu0KKruAXA7UeszHgkRJj0doMOwHS9ST7rpTg2LKlqrIaiu2ZlUtjTdQW2LV8Jrvd/3zFhF7RJZprmsgB2XeW6fjrRLSCwsVQYZXFHrZPk+QK1XS6HqIF2a+nsWXQ7XlGPhaUrwRVTRRA/9SlSBpqy9gCravJAm2nnRsAROV4gZlpwsbociD+1W7NJEcbgKH0O+ybNnsSBFnzB3r8mCJlm+hAX+QiacVVGNCVj1QkTky4paDM9WVGjS8UxFNd6I6KCpqBS/FMtwsuJMjoNCoDOWms4nt2oKGjrrMGIHi/F52GMU+4/czwz7Wt6T1FuAacSbVNyyD6LwKZB6ZB+9RWabrdiopmysmXo0E1gd57BrsvIZ2Km898o9UcYk9yF5j5bLez4LWDaHffWBn/dSmP3Z3qnjU2Vw5i5tC/jhPx2gJik/wglqnEhXAfeKYGLUscdUru1ETTpx8WNXXZffMxSAtMIS2wFBajVouFwiMR08pq8wJ3G6a7pcOmiRzsCUnUOksnfPsH8BiCDd9gplbmRzdHJlYW0KZW5kb2JqCjQxIDAgb2JqCjEyOTkKZW5kb2JqCjQyIDAgb2JqClsKOCAwIFIKOSAwIFIKMTEgMCBSCl0KZW5kb2JqCjQzIDAgb2JqCjw8CiAgL1Jlc291cmNlcyA0NCAwIFIKICAvVHlwZSAvUGFnZQogIC9NZWRpYUJveCBbMCAwIDYxMiA3OTJdCiAgL0Nyb3BCb3ggWzAgMCA2MTIgNzkyXQogIC9CbGVlZEJveCBbMCAwIDYxMiA3OTJdCiAgL1RyaW1Cb3ggWzAgMCA2MTIgNzkyXQogIC9QYXJlbnQgNDUgMCBSCiAgL1N0cnVjdFBhcmVudHMgMAogIC9UYWJzIC9TCiAgL0Fubm90cyA0MiAwIFIKICAvQ29udGVudHMgNDAgMCBSCj4+CmVuZG9iago0NiAwIG9iago8PAogIC9UeXBlIC9Gb250RGVzY3JpcHRvcgogIC9Gb250TmFtZSAvRUFBQUFBK0FyaWFsVW5pY29kZU1TCiAgL0ZvbnRCQm94IFstMTAxMSAtMzI5IDIyNjAgMTA3OF0KICAvRmxhZ3MgMzMKICAvQ2FwSGVpZ2h0IDcxNQogIC9Bc2NlbnQgMTA3OAogIC9EZXNjZW50IC0zMjkKICAvSXRhbGljQW5nbGUgMAogIC9TdGVtViAwCiAgL01pc3NpbmdXaWR0aCA1MDAKICAvRm9udEZpbGUyIDQ3IDAgUgogIC9DSURTZXQgNDggMCBSCj4+CmVuZG9iago0NyAwIG9iago8PAogIC9MZW5ndGgxIDMyNTIwCiAgL0xlbmd0aCA0OSAwIFIKICAvRmlsdGVyIC9GbGF0ZURlY29kZQo+PgpzdHJlYW0KeJy0vQl8VEXWB3qq6t7e9+70koV0E0ICARISyIJROqwRRBnWgAYIJCSsIewICIoYFhUZRBAcRUVAVIwJSkBRRBTUwV3BfQPRUWYcR8VPSOf963YnBMb5vfm+93t9PXXq1q31bHVO3UskRkQWWk6CwtcNz8ye9+GDrxNd/RxKR02aPzd45bD4Acj/FZUWTp5VOeOxHjO3E1n7EemnVk5fNLnLksdtRHH3EfUIVlWUlZ8IZqUSDfKgTW4VClx3mlB30DW471A1Y+7Cczu9T+N+Fu6/nV49qYzUe7KJPHW4/2FG2cJZTmb4mGhwCe6DM8tmVMx6sf+1uF9IZNs3q3rO3OZcmkw0Nks+nzW7YtZ3X28Zj/uh6B79yp96gAJId8i07U9JjZY0n7m0PFIlS2T6+wAKKGfIyl9s/hd6sdL/+meIwf/n32oqpvjmBc2Nzd/QdppA1uYbmrc1/4sd5QVtqylzlDl0Q/N2epVeoMPUSHtpN1ICJnqU7mmTv52IL8DTbbQH9xtoh/ZsA2APPRLtjY1jU9n9rJqNYkWXzWc54DiuKrqGhf5gvrtwbaNFyN1ON9MSXH9lARqPax29wGfRYmHAWI2x2qObH9XwDBoGkL9RgJrmdahxHLIGaaNbMPt5TH/JKLU0jlZipHVSBmK/TvQ4f4LfyGeyO2kcX073sYP0V/44/c5300x+HW2NVlNnUICvJAP4u5fW0010B0beTKnNP9IB3HenlyiJwmwjnu7COKNokJa7P5pnH9N9ZCIvxVN5832U3fwGXatdd+OqBwUl7R/CtYyWiW28RCzjA5reF6ngz6hmg3IfcVz3RLrSFJpLo5QZZNJ5dNubf41MEDNYBngRld0dmNNZmoP130tbaBbdqd0db13rlSjdgnQyTadBwk272Ida+VZ6XOPySCrX7qtxrQZX9yvblPo25WW0FOkJwPjWnI9C1JUKaChNpMV0F6Tt0l8vGkBjQfGH/4DrW+kZcP0ZSNVDoNU9uP749yV9RreLyTRUXKCe7ArMLZ3vZjeDGiNFP5rFdtBgWijnxxbRz8xLGfRumzHWY66Lmr9s/jt/nly43oAkzaSXAW1/92H2G+jP2lqqwb1srPqPfhNxFVMxs+HqxDqBMtliu9iAa7s6jyayZPpMHFECWPN4+Qxra8kR+5C9KerFo+wt9hE7RT0pE3LTiz/PX+HPgVe/Yw3X8GPgzs00S1evq2d3qQt1Uscm4/k8up5uRE/blXG0n4+jFcxPe9j42Kxac0ojDRaz2AHxqXKcV7KoxmRTIShUDlmQXNv2H8o+U1+gAUoifUfzxeugwKvg6XyWq81+plavFrTcSo/8UVkMb0PuSdoPbThOC/6gbD71p1+YkeW14uOQx164LmDdPXH9//W7FdZlFF1HN/xh2QBoRPQ3iyZBrtqu7Mk/LBsA6owFFVrwSNDk8jpyzf9OA/rDsj9q+0dlW0WDslZZKxogFZ3pGNVAGoaBfnfgqmdHKEz5yihl1H9NlxtxVVMJuDkYK5mA8W4BPQZRyWX1Sv9gNpeXyF852k6loawCsj2TpNWWO9pf6E7lM3KxBkqlVSyOVhGjTexzqkOdPvp0+gr76mc0EOU3MROueEh3Jax1E1qOgUY+BD2aB07dgRneRJtoBY0GT/4M6AaZuoYc9AB62gEtugIjnqATfADyf/DTPaO7mzw6lzqRHMoDygYxFSOfb/5n8/dNf7+kotSPFt5KSV8CutwOC7UNM9kLW25l69luev7f6i28pN7f2EjMahf6a/yj2fwff7nNr2HlY5t3UES9mlLAgTyMvIPKWX/o1bam9ymbrcPYE/iLF9ZHPgTNiBIwu2nYgUq5UZDyovgBs9umzfQTdoDWkI1U6i0s4jPYt/00Vb2CracPdAdYJdpdS+3ZfUIPGpjoHOhbQn0VK/L/ogX8CVK5ny2AfCyntfSl2EZeNhr7zxt8iJgjbhFfXpw25OAp2PBRmMUwOgh9f5X20TDRhP62g4J16v2yVvPf4CXUgu/Xo1R6HEuYihXdzrN4P1jt52kQL+YLIREjeAnk4A0pW9CCx6I7j94WG2kL6LIYlnQjdoM/UwQ82sQqlU8xa2JO2NrFGOlXVF0A7Yug/+hvHChxs7YbraU04KmwC73Rvhr7wylcUU9luGx96U/tGRv3Hsx4EKzKCsAU5MbBvnURz4C6xMazMPYuam6VtNi4D7JHuI/msF30DiR8IXhJOgU7kezPA23sAM9zJGbmQX/3YTZTlbfAT/krpR50rPk0cs+CondG/qKVXgldns/700OsC3sOtEyib2AZ1OY+zefR6xbsl16sewtWNgqSMxjcqEDfHSkfpbf+u7gpDuqszaUEdBsESX4P0r4d+XHYBwPiVfJjbQ+LQn4j1vYtGgzFk8rY2raKT7HXHYcM3Yw13ILWc1ijeJwd1SfSi+zJP/QL/pc/3XG5uxqkl9kTvE3HumYxG7yVAbSVXaF8QtLjnA8L0StG+35taH835rQdVH8cNYbxRHoKPFoICm4G3e6kndCZIbKa/toYf2dh7ZNhhxej5Rotf5B3Vp+TNKCdzAcbFaOByObtYmPko++7mQ6+wa2Y1RxYxz+LXzDKCFrO4b+Gw8OuLr7yil4F+Xm5PXvkZHfPyuzWtUtG507paR1TO6S0DwWT2yUlJsQH/D5vnMftcjrsNqvFbDIa9DpVEZxRF+av8/ct6T+1LtB3Qt2AlH4pjmDdgGt/HJJZR66EUIozmJM5pmusVp2aUUfuwXWeoSVPUTh/TJ0u4/Iq19aJVMdPITQekhDsX6ek4r+UQWXldenDSkIpjg8SWp+PQZu6+L4loVBCHU/Ff1fjEf4bVBYsr3MMRXkoIVpydR0NLZHQ2PxVPgopPzQG6bCSunYtt2PG/NEk94Oih1qnmYMq17I1jqcGBPr2qyPPUzTgqzqKk5V+zMd+UliXnoFpOJDT+qLMOub5qY6561jcEEz40gFksy/y/4AC/cunpvQvnwJ6lk+4SNEfo/QMBdcE1wwrceYgq015cN2xP5U8ZTb1TelbYUIBaQX0lMmMErMsQBeznmIDrmJahg/o3+spTgYriOeS0+0vYWpdeO0EZFL6gWp44r74pLH50O1tHxGateTc0Vx0EnW6vnX66CSCU+rCZXW0NvhUl0Nrbm900MQJGZbylPKyG0rqRBkqPEUitX/ViLrEwUPHoghDASZUBSWz+2mJZF2wf1VwDe5l3QlIU/pJll9SXl5VMUEKCZuQ0g/PjH1LakOHEupcwP3rnBl1A1Ft4I2nEsSa/v4pQXm7Zk1tsG4bptvmaUimEAE/pr6mfwpGQ2f9p/aRLMlsZZsmi1eXa8wJry0L1i2fODUqeWW3t0h/aI2jbsCvIXAH/EFLrWGMlOUTpsopTy2Ty+w/NbhmbYW21Nu1pUFag/2n9pMgG0L2aSRajy3pX5XS/+KAWDgyIvXytqFQXSBDNlyzpr+cYlk5Zh+dMh5cnL/UiIQMhvn0rQuP0BCN0HiAEcNl/cbEimIVxspm8smEfmPGhKJ8R9U6fWqt2i0luEb2qE+t82Q4Qkfw7FDXLoOHlfTvl6Ctvo73LbnyrD/hLPKDh7YWMz/qrMk8mxCl0eDhKYP/FJWCqpZkwoio+vJWzqNqrL7W63F/wnHkB6QMmLBmzYCU4IA1E9aUNTYvn5gSdKSseWrw4DWz+k8IanrPUH5gbULdgNvH1DkmVLFeYLKUtwHDJGcGBKvKolaid0ooPyHkHNPyeOh/ehxTMQg7RF6q2BrHD5iWBaYoIThA2pVGGISEOke+1FBMYmQJVGCSJq5aAtUYjs4TpJKIMan9pwyP0QaCGJMVafD+FCtFJ6GQVJ+1jWGaiJu65X8qid4HaWJCPYUzM8C2CfLJoZYncSPlk+UtT1qbT0gBm/yDh/+/iHNbUV7jTHEFCzI10mt2trzu0Ais8bf8OkN+jNPuviUigcdyPEHInCkDlquwzpehNZQ0gYFc40gJvpVS58ioU/uWHEooHBN0OGHZWKscxHqUEup4K+VVJu0neRx1rLCOeWU5wZ5qRl348vGwtWGw/5oJMQmTywPvNELWnYYxeeo09RsTumzlsc2hvOrfl2/B8lHHkVJn+TUhWt/pSpFE+KumApcLxuWzHzyiNTesZGnCjWO6troM/WIwC54LIh3eDvA3IrEKnhwHnMSO/2fAIcBv2Pf7EBl3E5nqiMzvEFnhCFgnE9niiezwWp35gGNELpS7woA3iNyIPzzwS+KGEnknAr4gCriI4ucC4CEkICpIak/UbgdRcjFREP2G8Cz0I1H7j4g69CBKxRw7Ypw0zDMd43SC95JBUeiymairhajbfKIs1O1+GEEL+szBfQ7G6uEhLg9n9aTDwoASwmY9UxipwqiQwfHZcfxHmTnHM493zwo5Q85UJAyVf1+u0nmJabl0WqkPa+RV8FMEOZ9hWyV1eKYzJ5Myz3bPYqGeIV7V9BHvyBqfRt2q5jPqAvVd+Ku14XHpSpXCebqVWa2O9UZFH2C+QFpgdKAysCmgUiDgXS/cqwK7Ao2BkwHF5x7t5qusLM8y0LLAIlbpWB7iwQUkuOpmRhG4iaw3WdxLdeEESzWP103nGRks3u8YctZx9oOz48eVji/VftT7bE7m+NIaiUq7Z40vZTolJUhOB4WyFZ++G0tpz3GTk52bpy4IR178PLI5so+tYFkfsKwrn886suHH35j6zuMnMtjb5/7FXmJXwmm/46N3ut67JfJy5FzkjcgHB54lTsXNZ5QM5Uoyk4+mhwePtlTKSZe4qlwLXcK1kRyWjTp3sZ0NjGP6OFYZtyDuXJww2FmVfaH9N7vgBiNbKJheMIOwrxBxK4zhgJjC/cbJbZaFRZViWTW45LJ6ny3Fgli2XEtKe5m6s+Eudkxpr4vzeHnBCZYQeePQq5GTrN27W7Y9vXJ1XYNyZeTbSCRyNNKEkDrE/Mx94apTB46+dvz1145Lzq6FYPyAVfjolvCIl+MYXyOYOOn41sGh9j0d/R1C9cR5Uj1C6D3MkK8r1pXoqnRKseQrMzmYVdjN6kaXw2InM1tJVtNKczhAVRycdpPfXMEzGBYRXVDTEcdZyizs3fusqwDL0DhWM66Uxss1ygsOmFyMjcU54eXF5VzFcrLb8Tjxw9PzqoauK9z7kFKwc+aI7aV+vvLhG6+985am55TUe0aPLly4aq5cS0rzTzxN3YLIZmQ4V8kyOnMd+o16C4uyptaiWKwmu9dzD3fbi+Hcc9JZnSsNZr0uTbdPJ0in8/ucrgKITuErTYWOT0tfod5Nr/QuPF5a2lSI+Wak6lLad2M9nSk9c5x5mF+K0+PNyc7jaUPz5k/3r1ixd+/eUN+0TtwxfPlsPmktM8yIrF3btGFoX5gETtdCXkKgdAiq+2t499jOTJxIZfmpxaklqYJvjmNsl/lbM19gYvmmYlOJqdF0zKT6dem6KNFVvjHARF7iwMQTiWcSFa5P9CWmJQpDlXGhkRv0fj03smN6xuNFZ8GFLyMtg+9TmVBTNm627bI12o7ZFF5sY8xmU73b3BvjHZ02QqtcI71M2ESf9mwFtV+Z7F1p8DET+XwdVxjCXZOreBfDRXGEUo0r1XTNcbpwPORRCuQpjWDjS886c6RoSmYy3ENux2ksJU0pZU7jb8c00LBjzx65vVluXo9uHJKrT9PYzJKYxyt66pQ4SdRcJXQw3vz0O7sOP3tm17grTd2nXz+3NlCX9OM7LzR0cr58R6RqZuXK17P/dN+uNbc+lhiwe//Ut7jLqHm+h7fXbLvpp083sbVFmXnrrx7/gJSLoc1nxN9B+XhaHh69wMU2WfZZjlrEJjMzKKuUk8q3imIwrDJww0DG0nws3clsDzo3mhzxD/k2Cnd6fH4813t8njSPsBpsfhu38/iVZFtp9azQhROtU3iCbvLlpmicpq+n8J+msbinUgZCMJu0Pj17yCV7o7ZIF11wnvh7yu/3n7mw/qOF279L2JOwaNym++69a+5KJ6t+/SDL/P3N/6nY/UjCtOkfHDry/sqVWJUJVhjyTx42JXy00cSET2U+HfPpGfXXM/GbiW0ysM2CnSPGWWeP21NLzANy2LmOr3LbPW633WbQGVZZbB6LxWbsbLaYa01Gj8lkRC+0EypxVCeYzmyy2zxk3+c+6uYl7oVuWHN3vrvYLZjJHe/m+yysxFJlWWgR3G9Jt+Rbii0KM1mY4aSFcbfFaODM5dHDvIymSoTSKjnkliROuFmJu8rN3WaDyQ9hrzLtMqkmE3yTcDKCWpPQW3wWbieLzW5xKzpdMM6r61Oe1ehlEKgMlu/05QSkOPpy/Jn540pxUxrNl+ZQ78LCwpyc8TEBjAmfLESxzMNhHpJRG/MHjtR282fULr0EtTySNkrbUKL94MbIUgTEN0WksBx3njvH7fXluNXnIg3P7mLpyrvPRQ48e6bDwf3rCnXKP5XU8x/zpY8bLryppF5oXMf3N733TbLoDs49Ay6soOPYTb1hM69jLnoSkkcsc3zNWUgNtmJYGLbi+HHNQq9GcqV6ALWDYScXqL0yzJhatdKgsAopd/7M+CFo11u2c+awK/fuRW3epp2e0sNxqk5wO9OjsY4xI1obWloXxg9pKqTM3r2PR3voKUdHL3v3Kqmv/hUzqMUe8Rt6MrMe4Xf8RoadK1tvYH0hX+QznAOLz0CVjH7jb0bxLRJ+jP3GOH7MbDKTSZjNJohgLZkhfmaD0VhrEhAzYRBMFey0+EVw1l+w0aJSLBCbxE6xTxwVJ4SB6wBmIQSZjHaFmKuRw0Zyxk3ExC5izEy7+Lf8Ny42cXYjyrkw6k2jTQtMtaZNpp2mfaajphMmo9HkMJn0lAZXopKO0gk6Q3qz9N/EMjVsUeUOpW1OhY5XIFDZmjghC4Y7CwpKx9doVgzi07sQps6X0xt7Fv6rgRRlKEsdR4AhMoalR/QGR6GhMCozNZCZmvGzx5WycaU1oRSml/uZk+VALT+NPLBs7162+2+RqTx5UWSseuDCQbYnsgAcg51SUmCnPJRAO8LVr9nZL5yJBdAXg4MZoFOsWGX5/mI/1ys+5ahyQlHMPGHjAlYL8jKzf6PTsQnar39Y2Wh2++PS4/LjxAkby9cz/QpDH0Mci1tBCXrGLHrmY2lMWDlbYQsn0RSeaGu1YE2a9XrZcbb017NRZ+rU+Bq5Y2eWau6ItGYSR5WChdoxabx80q5Rzx4kLXnUrOmVlAunzQ23Vd6eur/rj3v/EfkXU8/OPXHPfnPD1GXbrex03YEZM3076llq5DzLn/zLlIfW7a4FFQbBWn8NaXNQEh0JrxiYyHien7E84GNxJ+Ngy1xMpFmkkyjYGex4nRUm9F6fF7RS3AoXercPVkpY3BZIj7RiPN/H8pyMv2+Fa8OZXVh9G80O7tQ2QH086BHvi0+L3xm/L161co+9DxyZeGyAyfBj2rXZAB1Np45o1JFbX4H8L2pbYiSJbXdtLxb1anqm6CR1HK6cbF8OVPSi09aOia93KWVHXoqc//W15ycpeyN95m+/5/bb1w1ZU7uN9fyVMdZ5Pbf9/uLhlw9/8+W+W/fdAH1cSaRLg5y0p3fCVoPT7+QGg9/AAyzY2Pxt2Oj25+qDzEAJ0Ttvrj4Bd6HG5i8acBOSpclGc64/iewb43Ubw/H6ZF9yWrKw8GRHnN1jJlcS6oZz3Qm5+iRfUlqSMDJQ5HQSfDuve2XYc9psrkjpldLBvLI8K71DcQeu78D0HfI6VHYQBgIhakqlXXEM+TkeHl/Tyz9Luckgv9Sh3sjC3mCbdBVIHzADYYz2tCXRfMDotuiMeoO6mDOYK3dMmcTp0vZ6hpdM3bK3bMzcjXAKp789b1P7+W8/8gi/f9CUP929o2kzr18zedvHTR8qqXc/Xlp6oL4eVKPmN3mBZg+vCnesZAsYbCmxO7nwQFgECWxXA3kt58W0ClLIUMKh7plSBaD7Ut2xP0hWYxNgvCBSsp7tUg/8Hqd+H7PS4gf07qY54RS90+fc6dznVIy8UscMuqgXp/iVfDjNBpU5uFVSOMVkzTULK6kb7Q4jQu+VZDGuNIXjpPscB/fZY7rUfS6E+4y5gHS9NVpptqZGil6oLamcuVIJpdc8q3rmE3v3Lj9U+dw1/P5bbrn35abn1ANNP60fsWer9EgHRIZpflEipTNT+BlDiP0WYkwks5F+NtYx1XGjQ8RZWYV1npVvNJ42QrNS2blUpk9j59IYN3gZ07vYOReyLmQl7Qzc1z6tPWduR4oDTmi7tHacu/0pfi6KU0pS+MCk0Umc/xLPfrczEZ+y0edIsNuTNjpder1Pv0AvTKTfbt6oJOo7Qic7+jqmdYSNCib0sa8gw0pZJ00vEkmv77jCE+4MKnXy/Jt3elFFz0qxk0oK0LzPKL1iWspiCquZd8RXpFltzbSneqQx69jTJ03bVaynTvPYNN3t2VZ3veLvY7/ZtvfHJ02LZt1+S9K8+jfP/3zyufnKjkjOnPrdS5c/+Oi6rz5fsu2ZhBEjZm+/ay3L/u5vLH/Tsgsz9514/vW3nn77RSk3vWHt6sCDNJYSvk+fwmhTgG1CLIBAkfQqO6cyvlllm2EH9nU82pHzXsFBQS4aXcdcvD88rJ4WJgxJzJBkMBlqk5M8yclJPh/zQ5inJt+YzMXOZLi0yYyrpjjTy6b3TadNql1UYjs2mJKTFIcBM3hEbOzgQHDnJM/Dvo1hh9sQ8ofSQ/khRW/1WbmbhxxGS65VumYhmI1kQ5JJsYZoZVpa/AqrZ6XbrVsZCneCG5weassNqDgSp8tXkKHJcCkMABT/lMaUU6UoH99iNDUjWmuDgtmWHqFxLXxqjR9iXJL2tMVh9iEs9MhQIi1P24B6wmakITbroVkJ/qFlXlXlsoqNu3aWfnv4ta/jG2yrF8+/qdfozV+tf6/h+Xfj+IXRowf07Z2bltFnwdQ7Dz/2WEL1zEkDs3olpeZumbby8Y13gy6LI8P4BPVdstCYcEFnhFLpJsa2gObSNU3D3oPIkm+CaTRoHhE36Fi6DmrA9ApLhKNlMBjMa5XMs+/lF75fqLlnNZp4jY/5FNr+kNKRY1vIyzGxOAefcPOO51/bcnP9osiw99ivv2KT/uyvkU8ixV9HkjCfLURKJiyMSqEwlEvZAE9Qryxj8Oem8ZYd6g15StA9qxODGQgpmRemHebvwkj9jPbPQdyWafYvWbZntEy6kTOXwY2cdtGNzGxxI5e99BIqo90g0CFTo8OIcGcD82Olql/leoPPwPlmA2MbzSgy+83p5nyzwkjRJ+pIb2ls/i1sssDHS0eksFZkni2tASU+jVKidf2lpW6vC0vXp8Szng72egsB3lfffS9iOhf5W6T9X1kHtu9rdop9Lm3W/aDCBUzMQnFUE+5XqzA+z86W2NmN8ArglMrzFGbd4DelmziZTOa4DSTMrjRYYQezccdSndW8zBIGr5zk01Vzr0VbOwSxxcJqoqodUSCuPRs9ppDCR3Izd4fkeYRHAX1T3KGgtlOF7uedVhx8aHjkfOSLyOrDh9kiNnbsipsja9UD8TOenfz6L017BDFLSW1IUnMFFvEy9N1OM8I2A7aEdGwKxYpqYtqW4DbacvVmnxnBvFlvY2KTLWyTmhdISM61OYx2vUtP8HvJadKvNIQdhlbv9YjmvWLi2Bq0glecrgJtjyBteUx/6VbKX76qb7iiau92ZdTaGxRlR9rTDze9q6Rua4R8bAaN5V5mR8ScQrvD1XozqzVvMp8xnzMrfEmIiVpVI7uoZVAH+P6MUjY4wkaDY0MgK36DUSRsMLgMyczms6ZZF1hrrZusKo+jVOKCUAxPlMfdZLD6relWYSdr8lLhSFhmCKeKat7BMK3VEwU33pNGHdTXArdx0TOw6ALPth4htdr0GoZtTxrvkDMU9MI+pIak/daY5AxFDXdIfLhm9ZJTLzW9yTsy88cVTQnsqokrJ1eumxX5mM04svmhdyOPC0vng4sXv1GmHvj2zgkPu73jJlVN8p5/6Lb5C2TcPbX5jPoM9CFJ+uh5iDZ4pbJA4Xy0odLABwZGB2ABfD7faJ8wOPyOEofgAfLFb8hLqkxakCSSkrgx3Vpl5RQ9EfVt4G7psI52C2OJlUnbAr/WwhMS3AHrTZbATeReqsITrebt1LYHnu+d1Y6qtHMWjSryyNOpeekIWzRjGTuOKU1VQkFy9nB1yIkdf+LO41JysvOcoZ4h9ZnI95F9kScjkx5lV//9HMvosafTe49FzkV+WsHYpm9eiQzl049/w7aykW+xypc//LD7/Q9Enov8fiRyYeUm5nhSyvTjkc/huxwnI40Mt09Ve6r9VSFkjAEpVuoNwi9JgDDUZagL61xKY/OhsM3ozFX0uqcQ+cqIBZHvz2cdr2RE94jehRrbo/xFIBXy6PRpuXkyLF1ZNrD7LFZxfNltiddkPXJcnmqXNH+qpoEf7agz9WCrw3+/MWdNDh/ZvaI753FuJlZBRv0Oxnw+f5euXTK6epOTOyMutZqCyclBn8/r98cntUtKbNcZYWqXLl0zMnoIoXCLPyM+UyQZEpLbp5u7+ITHxju361xr4R6LhQe7eruuMgURxAZXwINf0I4RtiHerjOlcgsb6K30LvAKluYd7eW8qzfbaQqmJvjjWW08i49XUzc6EcxmI/gwBQ3tu3ozPWiXjnY2Ru1XyGOmPM9Aj7LAs8/DPeSJX5FgSEtgCT3TV+TZBtp4LarZBmYynrnCD70zSCs1vvQ9SP9Zx3ul+Wdz4LLWnM3MgSwUtAUIySvZ0TiuNMcZLZN647qYHd+6CQP7tQyTGziet/TSPUtvKIxe0Xg3ljtiOBJNWeuGnqrXDvsQFObmtezM0Ek9Q7So03uZ1MyYI2XE2qOnYGraogk37/n17Wbas+dPw9/ZuuHFtWuYMa3ds92HzWh6avqQSX37TY5niyLPLFm8cfGfds+4q/ddLzPdjtpPRpTec+1th/fdMrWhOFI3bHHai0vW8tNXTu9/TenYgYEhTYJtGbR16MR95VJe70P8ZJO+OvOGD451sZFm1svFeprZJvNO8z7zUbNyVGXHFKa47K5buIL4QFHNdvMtetWj16txsHu77MfsnJfY5Vn+KrsCb81vT7fn2xWq0M/Tcz5QX6uHu8xYLWclnPGBvJJzpkPsqei5ywwrqCouRbXbyegy6/ly0i83hg3GY0Zu8BnzjAONtcZNxhPGM0a93phm3Gc8ajxnVE0w/TZsezPlq4Mk8hintUQHmsdbE93DYBucOdngVSAzJ0cLuhC95CDqbDmEvRie1sSCmtjZl7QX8ldTAwcgBUEOUmeIeX05uXkspLM1KpGxeyI36BpZe3Z9L6OSkMPGMa68fr6n8vn5kHrg/E9PdBl5j7gACm/HDnIzKGykgeF0dQMPG/QcWwPbYBCwAgozKcR1y/Rhg/wQywzjZtJftg+/Eo2yY7ZevmVyhuJCckLKzRdO86earjssPlUtkV57mqqifkotPOnTSioItCR8TYWLqbZUG3cKZ9BszS1UmJBbLTfomYfr/UZTrt6BMIwHEYJx1WOyO7TDAOZGDLbSGPbJEMyHEMxrvCQEQ3xxRDv3LnQVtIRgGTEPgVriVy3al+8JcpyeqHPqzBGnH1RvfLf6YO+9CbOvm7x3731PVz59F/9z0947brzujs94HuZ/Q/MZ7LrvUipj4bqVHeDNIIhPT2I8LS4vbmCc8JlZOstnxUyw0R1YSbAquDAoFrZjJS422sb4SEuFhYtExAE3JyV6kpISF6JpZRJTUpN6JnGR5xvoq/QJPtA02lRpEiJfFAvEa0mmRMXRvopYOuXDuyKxob1S6WHR425ph0Z7dCbyeHwbHO4kQyI8/2R6KzX+LavurWTPW+5wmrWad3Rf3Jg+iG1NvoLoWzgQRHsNV+qMOvytV4ulafH1o8espaXRY9tL/Xz59q7Vz+/YoWPPHtpWpiiW+h33PLf++DPfbI+8+1Pk9chxY6P11z0Pv/pOxPkR8/z9Z9bJqFhuv2PWtPGl3dJHPLXx4O/M84mj7sHb5iycOe3w1rpvTr8rJSdApF8AIUqEPZgYZ2ZiIHZv7OJenzcPNnyBV7UYPIx3drM8hFt+FcFYYiDx5uhxOo8LxN2ico+qcoPH7rlFNSBrMMJe3Bw9TTcE/IH0gIiaCGHnamPzW+HB2P/sAaaaTZ64RBJGA+OuYqqiYyQGgj9HwSHG9wVYIEDorNHO7HZTHDo2JUbPMWtpJx2Vb3XbmU2Z2nFltlPTeGnfc3KcUTRei7o0CyB/2c6cnKiQykPLIZcfe7ciGh8NwWLMGF8jTzw6pqXomTz2BlXipEXIcbukZXDrF0SmH4gcCuiVTpFjRyKLXvmqq4Ur6T7m++Gta1OUuO5nEIAMUFaM6bbn/Hb1wIWrDo5xieeHiU+bEiI//LzgmNgjefAQvKoU8MBHo8L5J91sn/2EnS80HDNwvZOZZcTRqJ5UFYvXLJwb9NjwuZer7rhlZFkmXzjO5H7ztDbuEcmDJqipNIxRu8awg0MteataXiU1VE0JTPvnq0d+nJV8uONDjz72eI+X+NSaQ6/XLnz+jWVi6IWGW1+4e/7L94khmGEoMkz8CPviY93Dj421sekqG2ljj8BJ3wWBGMiY6O+CpXczqnKzo27G8tw73ZxsNrvb7fT6rLVOVqIwdlRhDruP7IrV7DbYSmxVNmEgm8tovkeXKLcTPtDO0uw77ZIAykKENyNhuwaioQwU+IKopu6iRjpJKjf6YEFriRXL8y2bVVFq3azYzQxu5na4jWKVnZEdDoJ8WVJTo70gQQyandnyViR6Ui1fcoJaEJ0CKSfgNxtcZxxeEvZafb5aUiDlCrrzOmrtNo/dbpO7hqHl5NuGzBhWqrcVGrD7U0ucPr60JcirQeAEAdLp5aFKJtNedWlSJGVH/BiZylivreuy+rt6ZJcPyYrMOPy7N6AE0r5TUs+/ytW9X3p2O2bepaQ1XR2umDuFL5Oy4kAMtRSW0ks3hK9wBxEyMXFPnGI1bXTo7RZXiYGlGZhBT/I02a832xzmlfLNFAL3NEutZZNlp0Uli6XlZW/N2cJXHIWOD0qPaIFfYVMhCKLZdS1kSmLyRW+KfOkbfW3Hlybk9igafvz43m3b2t1821D1xftNeTPK116YLLasnTP0lilSmkGy7+QbE7om3Nm4QRfG5r/Bn4WdUJgQtxsUg0Kq0YTgXdsBrdgBLezSHbAQypqZ2Tbg0cJ6uQlqoHx3fr+SeuEvIuPC+2KlemBPJLwn4sDYFiK1WBu7Lrxwi363/oBebGI72T4mNvNdvJELsdDE+AK1VuUHjK8ZPzL+zfi7UZ1qvNG4xrjFuNuoxhs7G3sZBxnHGlVhMrLfjYwjGjW3GDxFr9wsuEcIrodrQ2ZFCB/JMycMKd/t6fWKgCUKZEp5yx6vHaAWFjqwoEv9DTa+Zvb42bNnd8+KiiJpJ6s5MYdDLW46/ErTsbfZ0oyQ0q4bu0NaETgZJyavnnej0gki0BzBSkuwUj3ZYbnb9TIyvY6ZVGgkYlK9BT6SgTNmtAtFsZkbm5eHR6dn5FaYEQpoXt4Zs2K2GRm7mfQe+dW4ApdFBxurM9p0XPw5bLAzg8FuV/U6xO9MUVkaMT3lwfpugu09RzojOeCSkaLKCL2nQWUmUtP1TB5UHtWf0Ct5Opamy9NxeQB8THdSpzi4zajTq6Qzm4MOp7lPeVb0VaY0yTWlpX65X+Zjt8yHN5dDmZJo2lsnmDH5jg4KKiloa6t7JB27mgy96ihcekTvKCxEwC+7Y1q4DE9OhLSXlRz2W6cXasnHjzfd99BxnvP23Xu7JaqJmdvZ85E+MMv3s09unn73TZGrpYYlwBM4A1tnpg+fKdaXwKNljc1vhDtm5+fybCSNZrYPZomxf0nLN5pxC2cXOCvmJRxur6w6oXN2rjG7oDBXSk7tRcmpvVRy7GYDyQP3Y6SgkiY+fj10t1i/Sn9Mf1KvHtOzWklSxSfYOcHki0G+CqImpObWzM7R3vzWzJaiBsv2nyQtgzKih+Wz5X+lGdgFo8LWYofORKp3RWY8//FVFsWR9qt8daukNm3Zc1V4Ot8h36XKN3Oxd1KHwqtM/ng/N5niTfzlxPcTuSkxHgmLZ9ws/ImsMXAswH1+BvbnK4iCGcOSGrEc7jedNHEfpUGITpDi96X78n3C50xz5jmFTZBvI3eYnBsNbqsL/gZ8Dr9ns2eXR7FxyFZAeFao8fY+lpXWcLI6hbezVrQelJw6op1bXfZuqjT6ZqqGYt9FaX6qxIjEXHHyC6K0lDjtvWTb91GsT/mB479GzjY+W6Xs2susSx++59ZbHuizUuxZF/ngx8j3kQ/vh7Vp+vnC8ROHn/34qyceXVclJcYGifkJEmOhv4avhxCoOlXRMaPRZCGLmaQAWcwWMgujUa8qqk4xQZX0tTrm0UFlhVnUKiaPopiMKrcoZDbpdXYFXHZZUIBis5lBy6HQJA8P4s3OXGx3ep1ObozFSonCixW2Sp49ZmqH+bCcCHgyNWsKM+rPzNEc0pgjhHz0E4BW+dBC10vC2Ggqj0IhJkaG9vLl7U+fRX6IfPcxWxnZ8vlHHqaciKxn2yM38E7sQmRfR1YdsUFW1kaqlFTlSshKIr0VvktKMY8KSxs5ecT9tJuLxgCjVYHNgV0Bwfxxu+Ia4+RnYX5julHAkvl0abpK3QId4haGUNLK/D4m3yxxyIOJBZhDyovNDokJQ2QS4sMFV+VG5YZJ0Un3CCu/KDPtIDNJ/y4zNdFXc/LYJfqmRBMjuXtLYam5+CYz+iVaW9nRzhLbvg9hORWvvf1T5OeXHqtU925nCTc98sCS5Y/cL+57MPL2vyJNkTdXNf2PenD1hc/ffvOld/524GX5bUFv7JQm9UWKp1/DD+gDzEowu9yvCvUOr9/j9fp3eVmafNMkF+7gJofFniu/E+CqFxFdwGm1mu516gNbw9hVA8zCd3oZPe1lC7ybvDu9sDPw4M95hc0gTgqexITDG8g1Cfa7YKJEbJYRkGBm4VXRFyRstUcf8AXyAucCii1gYJA3Zl1tCyd6lvAE2+JW91KeTr08rtRx9ogMamLvkWJRuHR/auSxVfQkC7GPjHyi7zajbzmk490a+Iwr7cR65Oa1nIXo03I7aMckXNXpQ4rpQs8nzq4/9ZeFi7az/U4mjp785+uRtx/owd9eEnlhbvPN1es33h33xkf/ePSOyOc/LbtBno/LKNIHehrhSe8L39KLDWL8Gjvr763w8r6uSS5eaL7GzMVAKFcOiFAMi9sLtrjYAGxgbkuKJcfS16K4vSneHG9fr5Jo72IvtF9jVxLdXdyF7mvcyi4d26yyTYRd1oTdi+WZmAEuOnfeS3rTvarbupp7VuvDAb6E+/WLL/HJQY+oDYq9NKfS0tI25xGl0c9tSlnQ6eApSFzubFf0bTB3elxeXsA+O3cmknLum/V3F62YtP7PfW5RX2xyRVZG1vEf2GI25/cDUIvenzUvjXwVOfJxs/xnrYzGgiIJoEhn5g87LUFmE3mBnQEuv1C0s4DcurtbbLlp9jw75+nOfCdn8pV6lVOM7sT4oBQmRqcyQzt/u/x2wqK9EfNx7WVYJiRRfpjHeRy57z3hZV6vLlUfYpZQqN29qXqfiZHJZL03rHPr0xkkV7bJQxt9yBfKC6EvRHjywyjuYJQeF9c+YXV6OD1sc+WmO1aL0Nr2prXGcBexhGcYF18SXh+J5eEXOHM0qYodAUVFTp4DS7EbFz0NbipAbKhJ37jWF6BEGrVjMilfDshzc2r7Ng3CqM/Lvoq3iKX2vVqcRy8Mq9ZGPn398IW4vQnr5t305APLewyOKx5R1W/9+BmrXXtT/rFj3y+vikD8u0uORZq/OhBYf9dTyxc/5L7fllsxeMbCNctDLzz/6bbjYyVfvpaHt+CLAT5yAVe2lqhV6kJ1FXYH2D49ra1C9LNKaVQURXoYlUz6sGr0y5WBTH7zsg+1mDT4b5Q2HafM3h+UNr2svbzS6Xt2yMsRtLf2K5ZXM09ZvHzMno2fyDFHyW8w1R2I9E3hpBNONtJZ4eQ8z8pGWyutfDTMLS/RvmxNlEG6O7tH7ljPVA/PdzC4zIjcOMnyCSg/Q6y/DLqYLxGXP/GOgN8TCPj725kg7j/p+9b3G7b2uPv2ye+SDIlbA7p8C3xzi/1eg/uXAOMnAmcCkLSAP8CNaf48/0D/aL9icPldcKUS5CYX8CblJrhWqz4KJCp+y2ozLPgSnmS+KAyv+LIdZ5ceyYhacY2x/t4x/musf6U021Wgfe+mxWt6uaGxmtIMTcsyWr7M1Gw6afzvcAn/09wINFi/2+7axxyRH77YF/nZ85zvnpmrd+9Z/UTp7nX8RFOjqLkh0nTyo8ibb75uW7v6zU1b6u/w8J/2gLGjYlrnpfbUDRHzWlNCfMLUhC0JimVz+q50LirjWJWVGTr5OxV3EnwT9Eyf4ksZmCL8ScVJC5OEzzfQt8AnonGKgfzEbcJsgKaSudO98gULHtrJ51OTYP9T7g2r7pJ4NjrIBiIaNrO0Liy9o3aMxbVPNvXQ2uhXMg7eRWqiEZrYUW4mQXnXHpl4eYfAwQ7H1Ba/2hP2hJ2eXE/H1Ty4WnsLdyjscHlybV1WG8JZ/H2eaXivlRVHWo3cRe2UO0NGRuzld8uvZVuIvrs5WxA9RWz9TFE7qgAfoZKK06PETs97dmw5Pdentdlu2377LWC7Iz+990HkX5uWf/Ltcy98f+LNitVrKypvW1OxbPeTN63Y/qgIlES+PBhh9OLat7xKv9MPffjFAyeH9L25bNKq266fsawpYfuKFbueuHHZ43IXKYlxz08dmCd8sNLHqpJYFZywSVYmKq2sMoVVhVgV9tqxSewGMxvuYyOtLMfa1zrcKrSzxtE+QfN8TCx0rHJwXmtFnICg8/2k00lc+L3pXs5Geio8XCx0rnJudoo8G5Nns/BzWX5ycXJJ8rfJCidj4L5i+X28H5u1MJIQ9uR7jXq3O+5eu1vfXn5qsq+9YtGOLhMT28tQGq66xb3W1X61LtzRsoSn6trs2tHv6Z3QjHHRfyPQwoaas1JNWo68Lr5PvHhF3Wdtv4p9Cxr7jpdyYh/jw3R64Ro51bZMKe+5f/rTTYy//lfWOfJj0yOf+R/v9NqOusjxW7c+sGTp44/y+lFTmfGDj5g3cjiyKDInsvDpRtsZlskMKc+uW//SmxvWPiWt1kT4SD5YLRMi+jnDdUzkMRgVnaq7g3EPsirXMYRWZNhq1Ckuvz4fwZNg+1TGB6qV6iZViPzoZyRiC2rLV/jRg+QSpjPCsNaiM4buEJiK1WH5TprbSEF3FlrCzQaNgthLtOgUwnv5lxvR7yPhOkpH55JjXfmZjY5EiovcoZ4hxXcyciSxUc8CXzTliKfVhLNNAyK3swz+OuN7IHPJWKUHMZYJscRd4Qk7IRGp1kesfKONWWy2O3V6hAr6DbqHdQ06gd0TUfp9TFHgKAsXGfR8raVSikq6drKtNIpvxW9Cujl5SLgQNvkVPZf/dmGhbpVOIZ08BNPeleEqbCoofAVrkKG2PHmJGU35eWdMI6PvQnoyhBUhZwpTPK/sbVrJt979SuQ2JVLAxkUeYuN2iGcuDOL3NE2l6BsQ7TzTTIXhoNhgCOtUw4ZAllmHPc/ElskvN9SwlWZyi9r2hbf8EBdBSuuJD3azkPZNV0ieVb7UpDt8mP/+Eq9vuhYx2A4+Vn5NzKeyFSIPNjchbGVfcvqKhRWVfZWdFRP86L/SiX1SzKde/Fsw8iffj95FKhnULWoO7jdFMTfRZL7QoHKzTpFf8nKlGb/vAKjTWzbsXjS8L4Up2NykvhsZxmyGO3jGhN4sWkNSAKAmB5ePdI23F/5CCdG/afTQ10mHJX7dcfjqc981lbriDNu0f1TNtBZaO8Md8t9Mu9znvvs95IqLlV/89ZKV5d8w4rupj3qUqpQ5VAxYi7IU4GsVoqEoN+H+GXaUVktAWS2eDQUM0u2mlbI98qsBA/CsN/pajPwWlD+H/CB1FN0PvAJ4s66ApqL8ceRL0PY+5Wvajrq1uL9BfwcFMNZD6COEOg6UPQSwqKOaIyhL0MZArCrnB+gt/9ZSbOyxgK8Bo2JQApgISEZ/2+XctZX3YjWURicRV3NElJk0nMiRoZsAjsmnWXxAK332x6gePSHdH8tzxM2vxvICUdZbsbzSpo6K3v8Wy+ugfb/G8nqaRKNi+WbaxBT0wBT4N2RhW7W8KmfFdmp5nVa+T8vrtfKXtLxBy7+r5Y2Y3AT2dSzPKCj6xvKcbGJSLC+oh6iJ5ZU2dVTyi0dieR0lioOxvJ5e4UtjeQOliw9jeSNNRlQXzZvopFIZy5spX+0dy1voBnVBLG9VX1Nb5mmja81/0fKmNus1y7WYv9fyljblMu63mM9reYdci0Wv5d3IuyxxWt7Tpn6c7MeSpuW9bcoDWts8LZ+g1emv5ZPa1Eluk++g1R+p5btqeY2GhjZzNrTp39Km3BKbf78plVPmTrmxojxYXja3LDipetai2VMqq+YG0/t2CnYvKMjpmp2VlRUcUVURHFI9s3ruolkVwb7Vs2dVzy6bO6V6Zrdg0fTpQa3FnODsijkVs+dXlKNw9pSy6buCU+YEy4JzZ5eVV8womz0tWD35P/YTXFA1ZVJVcEbZouDECnRUOWXO3IrZmNWUmcFJFbPnlgFPnTd7ypzyKZNk/TndtCGCI2dOmVRdjj6HD6uonDe9bPblxcE+86ZMLw92z+o+qmL2HDlS925Z2VqtWKUhwwdUz5wbnDW7unzeJIw4cVGvYB88nymXVjGzS7D/fEwg2Gd6dcWMOTPKugQHVaA82KdauxmIKuVlQYw1cN6NM8pQfVD1nKp5ZcHisvLpFYu6BEeXTZ9eNqkiWFzdJTi4bAYmN6Rs5pzqebO7BIfPrZiPOZbNnVsxpxotR1RVzyibExw2ZdK0mRWzu9G1VE2zaQaV0XTkJtIiZqUKmkoz6TvAxWfDaS7wTCpHOpvKxRbxlDgoXgDsFwfE49SPplCl9ofDptCN6KGcglpd2SoIJa+mWbQILWWtKpQGKZ36UifgEbivAB6COnLEuag3Syvpq40/S0vLtJ5ljW54EqQizGk68MUe52h3FcAVwPO1OXTTaso6cg17cDdFqyfnNFfrtRz1Zmhrmoayapr8f5hRkBagxRSssgp52dsi4IlaCzmjSm3Uudq8opSZorWapJVICkXvp9I8ba5zUEf21tL/HKzj4iqCNBJlUzSalsfmOVz74yqVaD9dW8v/W+0g9UHdKXguZ9OdsgCjtNnMaV1Td4yaRdlt+rq0J9lPEerLVczUSmb/RwpdF+OTXGd0VuUap2TZTOqF+2Ga9EXpcG2MltXaauZQF5QN1XqbrT2ZovFvONJ5rSNLGo3QuCD5W0ELNXpHn8o1zr9sdVFOt6XTJO1JCzdkL5Uol5yv0u4ma2sKarVb6kcpKlc7RWs7R5MFqQVVsbW0yNLlXLhMn7Q1Xs6BbKxJckFK91yM0gubcyb6l1c3jTJtaT8pRvluWm4Gav5f27XIe1setdBY9jkD679GW02FRim5nn5a3UkaPWe18r1XjAJTWik4U9P9ORr952I+ZZpOtOjl3Bi15mtUnod0InCUxrM1GxLVmEVtOPjfSWAwRu3MGBenxLg1B6PMwjUdJdE1ttS8WGdebI0TtXEXoYd5rTOWNJvfRrPntZlJy2qimj9Dqx+dtZTf6ZdRsAx0lr1Ie1Sh0anb/5J6l/ZYro1c3WbG0fn/9xRrkfho+9kaF6I0qm7V42iNiRqNpmhyMucSmkV7kjRumc1k1Jsf4+nlvUUlcBbqz22VuCCNic2/xbJGbfLFMeb+VzSKzmSGNuOWVmWxdf5vZhTl8fTWlbZQV/Y2PzbSxFY7EuXDH/F7sibRM/6QI1FKlWupnI2kQn/YNFlrlra+spj0yhlLizhZ6z1qmxa1rmSGJsNzY7OI8r9FKi+dT5c2K7mczi27939H6W5kxXW1Juf/ThtJcdlTDcortF2xZY/ros1a0rUsRiHZ23xNLxf8x3n/kd5cHHe2Rp2KGH/L21jn/24tXf7NblzcJSZpLf5bbZIclHTpe1n7q3E3udXPumg3rf91z1YajecTNSr/X+z9/3WXqIh5G9J7uLgvXPQnyzROtdx/eckzyeW2O2B0D2z7HFKitFO6K4OVgcqVSAsu6Unq1bWaTJVpfxCxWtvJZ2uaKXtF9BENKXPa/A3eNr+wiRFrxwYwMrLnlAbEqocpzFY2uBIKwo1sZXi4wVjw+RdeX+J77yNZvMSbMH5x9eJli0Xvxdct5ouXBN5+B+XzFyCZMQvJ9Gok02Z6E66bOX5m9cwHZio0bdm05dPqpilvTmPTZi6bHX9dUQLvJiNdpA5AEPAF4EeAirsMCgM4ZbEemEoPGgoQrAfrWe+JS9zPsllOOBe5ufOQVE5FMnkKkooqT8KyqnVVb1Z9XqVkVbDkClZRtbImPjDHe2PfQGgRgO9v/kLXvsFqL8hq1IUanO6C3KJuukRM5XpdL3oPwMmMe6suBMikJOAk4K6ADF0urdV1oc2Al1HHRAW6LLTsokunR3Rp9Bju9gI/C/w6QKfL1wXqeUa4UZdQb7EXHNQl6OLkX5LRddW56kVGsFHnrff4UZ6n82HcDJ1f56tXMkYUGXHPaDXSe7UnQZ2voVtWARr4GpKCUezyFGSgYk+6AsBR2U1M50HHPGNUUUDnwl2Srp0umSw6m86ucwB30nXWZWBZKboOulSoSj+dwITl+UJQ/Xu9K1BQ5NJxNUIKpmJUv4PcZKj/iOHfY/i8ehojBBvV0w3ehIKrn1VPy2MFtbneFyg4qP6ontJq/ayeitY6Vd81q6DIq9OpX2grNABLCuiBZcUmYAynXog+b/5C/arBYsMK1S8aUtKi2OUrMBe1U/9GtwI4Xad+SuMBXP1e/UE9Sxb1E/VT9TOyUKb6CTH1nPqb+j9kVf+p/qT+C/gZdW+9mnGkyK3upfcAnDqr26iD+jj1AAxVH6AJgFkAHYXV/Q1x8QUJRSZ1C/VW76e96mP0C0ChLHVLQ1wAYqNur88Lg1RqnbpRzlndHsP3xvDmGN6o3gUuo8GG+riEAgieuqHB6ZE9bGpweAr6Pa9uAu0Wqbsx6d3qPSDY4CKzeg9dD5gGELQVKWt+S727we6EoJpV+e9qb5Opuke9SyPgI9ogoNNdDXkFBRoOtpdjrK/HGHLQ9VLazUXxqvxjQdfLVN2q3qf+BYS7Xb1DvROEM6tbUbpT3aU+CoI9qD6kPkzW5kPqLQ1pGQVqkUW9BU1/0VKTig0UwNUp6tX17UIJRT51CpUCpgEWA9YCVOqoVtIV6gwaDKhAfiNABX0nNJjjChY/q07FgPPUoVEpGdOQnSvnPqYe0n1Qna4O1Qg4VB0UJeD4epsT5ePVcegjQ71OHQY12XpQHUaPAaT4TmsIpcoepjW4vBKX13fLLtivVqjXoofbnkVDKaXj6pM6onSQOgTj+huBshcXFOWrM9Vqsqmz1BqyE+7oXsCjGswC52XaiDtOS5DOxd1a4C2xOioEciYEciYIMJMmaS3syCUDMgBXAGTJQNqhVqGPsDqwHnMsGqKOVEepo8GFAepAtRhc0Kkjta/bBqCdhJEYayQ9AlDpdaQfoPR7VR4+2ZG21BkMuB75CcCLgR/TYCQZ1TJ1ojoJ/LxevUEthbonqNdD9K+nAkAxQIE6hDFiP/VKqNaVdDdAgEp96yHn+9VCNQV6A1p2bmgXLAC1MhqCoYLiF9R0sK6T2kFjRZqaGq2UXR9MRaMOuNfEMbWh4ArJiNT6YEoB1Km7GkIIF1KzWnF38NB8UO0OunWHOLXXhhtT1F1NoSkArnZVu6mZoE87NVkNAheovdQrsJ4ctYfaE+sxqV0xe6PyI92o/ExrAN+oRvpVlQeXPXHXH7AF8ChqPIPS/1E9UPGg8ktDfGKB+rwij137K79okhHX0K17gbGol+qmgCpPEeerdlqtynPDXspZMNEOQtvBeDf0Lw4CYoJyukmv2pQfNFm1xrAFWOqlIYZ1MawCS0MnovWUf0TLlR+Ub0Cw+UVxqkObzgUaCeCqQ/kG9xmqAizbcWBZ/2+oTyBTR+35ai3dgnQ3gCv/VH5S/kUW5Svla+UUROpq5SsaA+BKkxJRmsmqnFN+U/5HEk95k55R/kq8+Qvlr/UdUqWpQCYxKZaxOAqKOiufKB9Lc618rLyi4Y+UtzV8Qnlaw+8oT8nZKW/H8FGlXlvdQeVlDe9TpMXKUI7huZx9vfJ0vSHDVJSonCSmnMQc9Cj9UDmiPf1AeU3r5TXUhnApr8RaPYfRJH5eax1sBIK2F9mUF1BBhwfPxIbfH8ONylMQrvwiJ+6Z0qDsJRvZ4dkkA4oBQjmsvARddyjGhpSOBUqRW3mQPIDXAR8DvgecB+hIQToCwJsPKQ82uPwFjqI45SEaClgO2ApQ6BDStwA/A4SyTXmAAhjrAXG+3pa8rCheuZ/WAR4APAl4AfAmQIc696FU/q8GOih/oVsB7wFE81vK5gajreB6NN2M4s2Yz2b6EaCQWdlCCQAYPeUeCgMmAGYBlgNUZaOirx8c8hSlKOuoPaAcILDQdai/jrJiJbMBywF3AbYB6gBGLGYDPQbgtEO5G4S7S2lf3znZXJSs/Blj/hmE/TNdAdgKeAygu6T0WYCCktUoWY0+rlfWoI+1iq0+KfnnZ5XbpZ4pdzT4kgqsYN2dqHknat6JtnfSUsBagA5UXtVgchVQkV2Rf7BcUWqpH2AE4G7AKYCqPKrsqu+QPKvIpexCnbu0tIdyC2rdQnMBdwP2AlQseGl98Z8KDipLlfbkB8GXKpPqOyWXFzmUJai6BPO8FendWu5u5WZQ42aNtrfW+xPR7FbFpjVbgWV0SrYXpSnz0Ww+xpwPjs+nLwAqZGseZomoGCCUHcoCjf+PxPBi4HbAN8bwohheqCyob5fcD8K3ADNfoE1lAVbyvVKN1Iw0AZABEFDJWQ1Ga8G0ohJlNi0GcBoce8d1FnAeoECC56CjOVjHHPD8emU6TQNwSPVMSLXcwEiZBlmYhly5UglxrUTuPaSntNz1ymS0mIzyyWg/XpFf1l+vVNEBRW5c1ym3UTXgAQC2IKSZgLsALwA+B6ggwCS02Yr0MYC0LRMb7PEFVxalK+PBoQmY9HhQagKgDEONx1LGYxHj0WQ8BFBRbsAiboA23EDblVLwsBSTvwGTvwFUuYEMEPSxmhyNaTBaCra+oIzBQGMgemNAo0NKen16pwKYxnZgdntQOBk4GTgInAkcAp4DnArcGTgFuBNwR2ALcBqw5Fh6FGP67evhfR5U2kMMhqLgkOKJDWFCiRzCDCyHsABnAVtj2A68E9gB3AvYCSyHcgHLodzAcigPBCsu2fwsbhnG6yb9elg4Wz1MzX7xP+I3iIi9aKb4F9nFOcBvlIx8pga/As4BfgOhdoKHOxGSBMXvxMQv4meKE7/haRyZ8ZzROiF3it5IrwOMB1QDtgIeA8AUiUY894qnaC6A021IX9dy94rj6PFr8YS0weIr8ZGGv4zdfxbD7wv5TUGGeC+G34zhA+Kwhp+O3b8ijmh4f/S++Quxp97lLjgo9qAjnVZwqr5ngdyFkGmfhswn4lSD3Q2qiI8auvWR+PWGxPYF5UUmcRqzPU1cvCzku0/Z+KX6hHZa4yP1GV2ReQslFic2C/FxbKYngeUM3o3ht8UTmhcKhIk8L54UdRrVniTGR9b37RgqMvJr+VC5sfDB/FoNFzf0bRcKF5m5/IdA/ZCOANwNgBTiodFc8H2RRb4r5kN5P7nHoYd+ck9rfov3q/cH5MR4Ub0RC+dF/Aq5l6IgXJ+apj0J13uTChqB+qaFGnnvBqCgxDBJz2I2vTHoXn4VHQFwVL+q3uvX2l1VD604yHvxPKhKBi/gedgvsxp5XkN2AWJ5UdHQrl0UY6UaNpsLsg7yTjQBAN+Una43Ogsa2emGJ0VGuMjIvpKiwzYgHS9TflhbeCM/0GCyFdif5TKmCPO99Vjx/uZDrGtDoF1BZpGTdaXlgC8AzQCFgkjrAD8CBFIW7sjCzWxCZFvkrcgXkR8jalbThKa7mg41KXQh68KEC3ddUC70SQ+ZsdzRlADYDtgLUPiwhr5dQxlFLj5M2iek07gMAvbygbgfwYfTXMBjAMGHyKogwJAGu6tgcJGPy39YlsEHIe2gVX8W6fcAzv/E+0v549cBKxo7+ktGHeS5vIdGzZ68B6hpBl97YEI9MHIPjNwDI/UglV/JC+GXnX+WF4JKOTy7vkNGQlE3no0xDmlpD6SDAXMBywF1AJW2xXKnAOcBMOJIg4BywCyt5DyXf8SuHOlcwF6AoLAoj/GyPMbL8nrwslFc3/A8xyRDPAmTlK+xg9wPCIBLfkCAhgIPBZ4APAF4FvAsYBP9zE5hnAfY18TY1+zLelfyA8+yL3HzBNsDH3Xd82yzJgdIwerNDQYzxuXPNhgdUhL2a5LQGO4FUQj/1L5jwU8beYb8Nuaow1XwyHYlY/nD7OHtImP5Q+yhB9WMB2V2G9sGRNsd2ydsn7VdKcrlEf67xqEmYCgrvwAsFe58DP/Of9RwhP9DU95CkSvriyuA5X0vYDwXBTGcDwyuirwY7hnDPUQulsSL4kWiSNJqJogkrQe3cGpmwgUsyx0xbI+V24QT5oIXteN1/EltLk/yPZrk7OFPaPdP8Mc0/DiwLN8dw4/G8C7+WMP/U9e1xsZRXeF75q7teGOv13Y2WWexvd71M2O8jtPYDKR4H3ZaMGmcB5LNQzHgVsAfTHfdX4Q4IUvCI5BgkjZNWghJ+GNVzM6k7ZpgOyq0QmorUYnyh1YKatWqlIKh/0Bq+p07169WrPLd78ydO/dx7rnn3JmdjdG2SFUaeREEokA3kASGgVLjmDvtM0UqaRwR/YAhgnKf6AbGAAkbaRBHgUuARMrPrzYgHQDGgaOAjz6hf7HLkXvkLjWyYTCPYLfm72i+S/OQvFON9A59/G3Jt8lGkd50TvnMIhWdaaZ55ykDNOfkma46h0pAs87BEjPlpxN0GJZk0vM0pfg4HcNO/MBV/tEkHaODqPDAPPHGop9T2NGjTqQeN4j0PXqYlxk9TPdxb2k37cD9YOMc8WJN8su/9E0n39PIbuY2pz5meULNBiXc4qQHldC3JPS6EJILxi9wYQfxqx8mtVMbepMsUpvbs40fbrY5DTG4u7ZkGMb663cM87cY4stA8qUtndZL09Is3rjmnhp/xFI8er/Hu+5m/uWp1B3WqWk/l0l2TW/vtaZPk/nC6RLz/NkSM3muvtFKnkVyDjlngR8CPwLOAOqN49NdCSt5uqsbSTSGBGPZPU27zxIi20/keTUJ58A8KT+W55XBBuRpOa2m82Uwn3lJ8yk5zdM1Z3yh18jnxiJGi8Cx6DThHjxmfIpFwydeNy5wDcZlMB9f0nwRDIMxXtP8quZXdPmfGhfYcFHjBafPslINskd2quW3Fcx96gZzXxKauzTfDGZTNDVvkZ08mtkbixCqOfyHZZ0quUnWedG4zt3cYBmpGlkuy5Qm1oG5RKnmEp3vk2XKTI2n3Lwfk2t8l+PvY/PGuHgRsAEpx5w5WKs84NFed44fUtCfnXg7B076wK0KWc0L9IHYD/wVkPQHowUevTl1k9GCRdWCZdaill6zCh4xhPuYijpRxOEoPzZG2gwcBSR9aDSpZ1f0J9dfYa1P8RtZiE70ezEOGOJD+h0ChaD/iD7RSP+kj2HsU2/Rx+IkYOAQqysVk9+SO5XCdqqXskw5qHkAzEpIg1nxKc1Jzf2ab5cZh2A2fjpM6oEhTYF543WNnnCamtVSecKp3WjN0iniR4nXUPYkujrBKT1JB7kdOujmS8xMkbJOdxPo+x49zvQWTWDH23TjOj3ubthoiTl6XAQB7P5pwqnmmifpIfQCC/9BtfAfVAv/IRcLH2twzG03rQOpAI2p6IOUxuEDuNX7tS+4z8kr77KH9vJmim6nHWKct+N0q3PXsBrDrU4qo4WtPUrY4ezap4XMHZ7gbtnKLaadTZtURsqxbtVCh6mFus1awFaKhX6nv18L1m1agPPwhJsTWojGtMCaZMEt91vJecPBaGIU5zmkuJsvNReuytfVi3gXncpKtVG9yLcyY6mEfE1MAFPASeBVwAauAe8B6xADLuO6y4gDl8UC8BlwAyjFmUv8EqK8yPXi/EXsDy4iAtRRvXiX9YTWerarjkXcnj7rJMzxJvVrigimKoLdWQR2F4HOF5Hy5EScm5p1+eow7sZv0SVxC0m1kGqxv6vFNbXiVcAGrgFlcNS1YhgYAyb+p1QZZjcs3gAWACl2Iz0APAYcAl4EbgClqCXsdiR4qsJOzw7VD78zPKyFngG4bL97zG8GU1VUrsahXm7k36eg7lKkjVTCvyF2DsE7k5Ecykvzq4+k+cq/6b1Dw41v4PAjLLAb79Cv3pbm9bfpL8j5R57M34CTc8n55IJcmPOb88AcvMqJ5/zmM8Bz+TIVEab6B1QkmIJWmY/AHSrO7GROThxp77KOHPaZh9GBKeBJ4CCQPLTvbusQajmO5o/BHo7mfeZT7LfyMKqpPEX6QuHeUGh7qOYboaptoYqeUPnWUGl3SCZCoivU2hZob6vaYgY6zapYPNAcr2poDEQbq6pSlXQdg+YvUSTSED1Dz4pmtUSedTfWWclUJzLGgCngJGADJXQP3SsCtJ/u5idkxgI0x2kI6TwqCVI18hMUxFwFMVdBaDcIuwpQFZcnPhe4YsgvQ3KevsAFi/Q5sj+lz34eSNZ2eDoJdnQonSR8HTdbVcHqiorKQEW5f31Fadm6CukrqYAfrHismaKx92JGMjYcuxa7HluMlfA1rTHExFbZZpYC/VVUJT+TRoTqK8NlmytDwU2VNb4NlcPbyK4ZEkP703Ytgfel7W3mUFFG99o95pC9bvjekQLRC6PItY3jRXhh23e8aIBqMvfcO1KkOj6dj2AHS8IeGsufGC0YIm3TcTu+b4QpuWfEjh4vBsX+kYJB6YjtOzE6Omr3DQ2PcMlRs94e57+vMVU/avewcLJ+VPBvUbJZTnKcrnyypso1l4g/hfbWQXvL4AN25+DYwOrCtPbalU9udU1oKJvNefloDjm5yUkcTKpcHE5+TS3qdG65G7hMUWZkFsvpMH/1hlCccWPN1tOzCCncG+gpiqwadUeecaJRyzRH1/Qryx3gHmV1vVldoyxzt/fxZWVua4fHoc3WuVlEcjXOiFemZqP1R5WX0xVnRiKpVtkhY2qz0a65TbaoGNequUXnxzU3a27SHNXcKGMFWqWD0aURB2Wnm9hqBYtgjFgxhsnsrCu3uFjkTXGM9zy5lRFnRt7C7dsFdkDYH7UnLN4fuZG4Yv6qB04eQrBaVTDJY+RynV65hkZdrtYy1+hRdQnhYdrpSlieEG2ytI6mnZqQtdxxnDyvvu9iwY02s2bPO6Ew1xhJBcXL2ENeAq6oPSWn7wDvq6MoSiJmYeK5NpHLfY2h6I+2I2XXbDgrxTMjc/JO9R+38GOYXU5Dk+rPLsfs8gQXd9NPX0WJM3w/oiqIpMpFKe46SF1p6CsxBd6VanvCwoY6T3cr6tHWlRlZgO5n1EOYGTUDM25MaX5mSfMzrHkWCs7GiOXZeEQdu5uV7mfcLZ0ee3Mxo+diZTJYxYu47VMhlIV4i6VM4X3cE66Ygles1xswCw1RCJ9ACEd0TvUGz4p4WL1OwpuyXt6ee0J1+P+sgFdPjpdVbmnNs96zSgNLmshh2S6vtZy3+jiLPD3pBa780LI7We2UsqbnPETWpFWZKmttVyibm5VXZGHw4aL82eAjDwwoKkrH+0tddnKsKN34AJoUyhGYVPQFUNgXiA+s9UJrKkbDqJpTuC/KQmKB/xE6qj2b9qZCHXImKQeTE6YaYo47Z876zvjOcINdg48+wG2jj1wdCue06nJoO2uuMfTs6t6QzlDFJz2drpxXiuW2c7O+r3yL3NTflCKYir6/ryjC92V8QCgt5pbVLrxJ5K6LST1N2ppzumWtj2WN87CzqtN67nU3TKEGvXoWWSG62JqwIZYUT95AJ6E0LpBbyldKzylHC+Ozw3Y3oiiyJ7NLmldtLR8pKpRzeB3em0aM3avirL05joN3cdCLgwo+GN9rl8RVQEb+SKGU0oUykS74wetFOkIFITYGCzvFREHsvL3oe3NQFH1XB+31pu3HZevjadHfHzaDO+gHiVvCpRV2KXLL4ulRIcR/AVeRak8KZW5kc3RyZWFtCmVuZG9iago0OSAwIG9iagoyMTIxNQplbmRvYmoKNDggMCBvYmoKPDwgL0xlbmd0aCA1MCAwIFIgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFtCnicmxD5fwffz0kP+H9//6HAwOAAAFE3CHMKZW5kc3RyZWFtCmVuZG9iago1MCAwIG9iagoyNQplbmRvYmoKNTEgMCBvYmoKPDwKICAvVHlwZSAvRm9udAogIC9TdWJ0eXBlIC9UeXBlMAogIC9CYXNlRm9udCAvRUFBQUFBK0FyaWFsVW5pY29kZU1TCiAgL0VuY29kaW5nIC9JZGVudGl0eS1ICiAgL1RvVW5pY29kZSA1MiAwIFIKICAvRGVzY2VuZGFudEZvbnRzIFs1MyAwIFJdCj4+CmVuZG9iago1MyAwIG9iago8PCAvVHlwZSAvRm9udAovQmFzZUZvbnQgL0VBQUFBQStBcmlhbFVuaWNvZGVNUyAKL0NJRFRvR0lETWFwIC9JZGVudGl0eSAKL1N1YnR5cGUgL0NJREZvbnRUeXBlMgovQ0lEU3lzdGVtSW5mbyA8PCAvUmVnaXN0cnkgKEFkb2JlKSAvT3JkZXJpbmcgKFVDUykgL1N1cHBsZW1lbnQgMCA+PgovRm9udERlc2NyaXB0b3IgNDYgMCBSCi9EVyAwCi9XIFsgMCBbMTAwMCAyNzcgMzMzIDcyMiA1NTYgNTU2IDI3NyA1NTYgNTAwIDcyMiAyNzcgMjIyIDIyMiA1MDAgNTU2IDU1NiA4MzMgMjc3IDU1NiA1NTYgNTAwIDMzMyA1NTYgMjc3IDMzMyA2NjYgMzMzIDY2NiA3NzcgMjc3IDY2NiA4MzMgNjEwIDU1NiA2NjYgOTQzIDcyMiA1MDAgMjc3IDY2NiA2NjYgNjY2IDUwMCA1NTYgNTAwIDU1NiA1NTYgNTU2IDI3NyA1NTYgNTU2IDU1NiA1NTYgNTU2IDU1NiA1NTYgNzIyIDI3NyBdIF0KPj4KZW5kb2JqCjUyIDAgb2JqCjw8IC9MZW5ndGggNTQgMCBSIC9GaWx0ZXIgL0ZsYXRlRGVjb2RlID4+CnN0cmVhbQp4nF2U246bMBBA3/MVftw+rMAXYFdaRapSVcpDL2raDwDbpEgNIIc85O8LPrOpVKRcDjMez3EyFIfjp+M4LKr4niZ/iovqhzGkeJ1uyUfVxfMw7rRRYfCLUH73l3beFevi0/26xMtx7CdlyQq3WTKVKn6sX65Luqunj2Hq4gcVYr/d/5ZCTMN4Vk+/DqfH3dNtnv/ESxwXVeZ7cQz5szh8aeev7SWqItd5PoY1aVjuz+vyfxk/73NUJrOmBz+FeJ1bH1M7nuPurVyvvXr7vF77rfp/8apmWdf73216pPfrtc+kVypLU0IGCpDN5CzkMtWyroIiVGdqHNQQ09ALJFVeyWyglv2kSkemhzz0CgWogyJUQT3E7rqEcNDiR9cav/oFwq+mF41fQ58aPyOZ+Dk60/g5OtP4GSH8Ks5T49cYCD8nhJ+T3fEzsgN+pobwcxgZ/Bwxg1/DSRj8KhwMfhU7GPwqycSvoWuDXy01xU8y8askhp/jtzXiJzH5/fAz+DWcoMGv4VwMflYy8bPELH6tEH4WI4ufZXeLn6VPi4PF1uJg+U9YHBy9WBy6Jg+MTIZ+n5PHXFn3Xl5Rgmzi26RtT4zHGPtbSusE5wdGHt1taIcxPp488zRvq/LrL4mDIPkKZW5kc3RyZWFtCmVuZG9iago1NCAwIG9iago0ODAKZW5kb2JqCjU1IDAgb2JqCjw8CiAgL1MgL0RvY3VtZW50CiAgL1AgNTYgMCBSCiAgL0sgWzU3IDAgUl0KPj4KZW5kb2JqCjU3IDAgb2JqCjw8CiAgL1MgL1BhcnQKICAvUCA1NSAwIFIKICAvTGFuZyAoZW4tVVMpCiAgL0sgWzU4IDAgUl0KPj4KZW5kb2JqCjU4IDAgb2JqCjw8CiAgL1MgL1NlY3QKICAvUCA1NyAwIFIKICAvSyBbNTkgMCBSXQo+PgplbmRvYmoKNTkgMCBvYmoKPDwKICAvUyAvRGl2CiAgL1AgNTggMCBSCiAgL0sgWzYwIDAgUl0KPj4KZW5kb2JqCjYwIDAgb2JqCjw8CiAgL1MgL1RhYmxlCiAgL1AgNTkgMCBSCiAgL0sgWzYxIDAgUl0KPj4KZW5kb2JqCjYxIDAgb2JqCjw8CiAgL1MgL1RSCiAgL1AgNjAgMCBSCiAgL0sgWzYyIDAgUiA2MyAwIFJdCj4+CmVuZG9iago2MiAwIG9iago8PAogIC9TIC9URAogIC9QIDYxIDAgUgogIC9LIFs2NCAwIFJdCj4+CmVuZG9iago2NCAwIG9iago8PAogIC9TIC9EaXYKICAvUCA2MiAwIFIKICAvSyBbMTMgMCBSIDY1IDAgUiA2NiAwIFIgNjcgMCBSIDY4IDAgUl0KPj4KZW5kb2JqCjEzIDAgb2JqCjw8CiAgL1MgL0gxCiAgL1AgNjQgMCBSCiAgL0sgWzw8CiAgL1R5cGUgL01DUgogIC9QZyA0MyAwIFIKICAvTUNJRCAwCj4+XQo+PgplbmRvYmoKNjUgMCBvYmoKPDwgL1MgL1AgL1AgNjQgMCBSID4+CmVuZG9iago2NiAwIG9iago8PAogIC9TIC9QCiAgL1AgNjQgMCBSCiAgL0sgWzY5IDAgUl0KPj4KZW5kb2JqCjY5IDAgb2JqCjw8IC9TIC9TcGFuIC9QIDY2IDAgUiA+PgplbmRvYmoKNjcgMCBvYmoKPDwKICAvUyAvUAogIC9QIDY0IDAgUgogIC9LIFsxNCAwIFJdCj4+CmVuZG9iagoxNCAwIG9iago8PAogIC9TIC9MaW5rCiAgL1AgNjcgMCBSCiAgL0FsdCAoVGhpcyBpcyB0aGUgTGlua2VkaW4gcHJvZmlsZSBsaW5rKQogIC9LIFs8PAogIC9UeXBlIC9NQ1IKICAvUGcgNDMgMCBSCiAgL01DSUQgMQo+PiAxNSAwIFIgPDwKICAvVHlwZSAvT0JKUgogIC9QZyA0MyAwIFIKICAvT2JqIDggMCBSCj4+IDw8CiAgL1R5cGUgL09CSlIKICAvUGcgNDMgMCBSCiAgL09iaiA5IDAgUgo+Pl0KPj4KZW5kb2JqCjE1IDAgb2JqCjw8CiAgL1MgL1NwYW4KICAvUCAxNCAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDIKPj5dCj4+CmVuZG9iago2OCAwIG9iago8PAogIC9TIC9QCiAgL1AgNjQgMCBSCiAgL0sgWzcwIDAgUl0KPj4KZW5kb2JqCjcwIDAgb2JqCjw8CiAgL1MgL0xpbmsKICAvUCA2OCAwIFIKICAvQWx0IChUaGlzIGlzIHRoZSB3ZWJzaXRlIGxpbmspCiAgL0sgWzE2IDAgUiA8PAogIC9UeXBlIC9PQkpSCiAgL1BnIDQzIDAgUgogIC9PYmogMTEgMCBSCj4+XQo+PgplbmRvYmoKMTYgMCBvYmoKPDwKICAvUyAvU3BhbgogIC9QIDcwIDAgUgogIC9LIFs8PAogIC9UeXBlIC9NQ1IKICAvUGcgNDMgMCBSCiAgL01DSUQgMwo+PiAxNyAwIFJdCj4+CmVuZG9iagoxNyAwIG9iago8PAogIC9TIC9TcGFuCiAgL1AgMTYgMCBSCiAgL0sgWzw8CiAgL1R5cGUgL01DUgogIC9QZyA0MyAwIFIKICAvTUNJRCA0Cj4+XQo+PgplbmRvYmoKNjMgMCBvYmoKPDwKICAvUyAvVEQKICAvUCA2MSAwIFIKICAvSyBbMTggMCBSIDE5IDAgUiAyMCAwIFIgMjEgMCBSIDIyIDAgUiA3MSAwIFIgMjMgMCBSIDcyIDAgUiA3MyAwIFIgNzQgMCBSIDc1IDAgUiAzNiAwIFIgNzYgMCBSIDc3IDAgUiA3OCAwIFJdCj4+CmVuZG9iagoxOCAwIG9iago8PAogIC9TIC9IMQogIC9QIDYzIDAgUgogIC9LIFs8PAogIC9UeXBlIC9NQ1IKICAvUGcgNDMgMCBSCiAgL01DSUQgNQo+Pl0KPj4KZW5kb2JqCjE5IDAgb2JqCjw8CiAgL1MgL1AKICAvUCA2MyAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDYKPj5dCj4+CmVuZG9iagoyMCAwIG9iago8PAogIC9TIC9QCiAgL1AgNjMgMCBSCiAgL0sgWzw8CiAgL1R5cGUgL01DUgogIC9QZyA0MyAwIFIKICAvTUNJRCA3Cj4+XQo+PgplbmRvYmoKMjEgMCBvYmoKPDwKICAvUyAvUAogIC9QIDYzIDAgUgogIC9LIFs8PAogIC9UeXBlIC9NQ1IKICAvUGcgNDMgMCBSCiAgL01DSUQgOAo+Pl0KPj4KZW5kb2JqCjIyIDAgb2JqCjw8CiAgL1MgL1AKICAvUCA2MyAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDkKPj4gPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDEwCj4+IDw8CiAgL1R5cGUgL01DUgogIC9QZyA0MyAwIFIKICAvTUNJRCAxMQo+Pl0KPj4KZW5kb2JqCjcxIDAgb2JqCjw8IC9TIC9QIC9QIDYzIDAgUiA+PgplbmRvYmoKMjMgMCBvYmoKPDwKICAvUyAvUAogIC9QIDYzIDAgUgogIC9LIFs8PAogIC9UeXBlIC9NQ1IKICAvUGcgNDMgMCBSCiAgL01DSUQgMTIKPj5dCj4+CmVuZG9iago3MiAwIG9iago8PAogIC9TIC9UYWJsZQogIC9QIDYzIDAgUgogIC9LIFs3OSAwIFJdCj4+CmVuZG9iago3OSAwIG9iago8PAogIC9TIC9UUgogIC9QIDcyIDAgUgogIC9LIFs4MCAwIFJdCj4+CmVuZG9iago4MCAwIG9iago8PAogIC9TIC9URAogIC9QIDc5IDAgUgogIC9LIFs4MSAwIFJdCj4+CmVuZG9iago4MSAwIG9iago8PAogIC9TIC9EaXYKICAvUCA4MCAwIFIKICAvSyBbMjQgMCBSIDI1IDAgUiAyNiAwIFIgODIgMCBSXQo+PgplbmRvYmoKMjQgMCBvYmoKPDwKICAvUyAvUAogIC9QIDgxIDAgUgogIC9LIFs8PAogIC9UeXBlIC9NQ1IKICAvUGcgNDMgMCBSCiAgL01DSUQgMTMKPj5dCj4+CmVuZG9iagoyNSAwIG9iago8PAogIC9TIC9QCiAgL1AgODEgMCBSCiAgL0sgWzw8CiAgL1R5cGUgL01DUgogIC9QZyA0MyAwIFIKICAvTUNJRCAxNAo+Pl0KPj4KZW5kb2JqCjI2IDAgb2JqCjw8CiAgL1MgL1NwYW4KICAvUCA4MSAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDE1Cj4+IDI3IDAgUl0KPj4KZW5kb2JqCjI3IDAgb2JqCjw8CiAgL1MgL1NwYW4KICAvUCAyNiAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDE2Cj4+XQo+PgplbmRvYmoKODIgMCBvYmoKPDwgL1MgL1AgL1AgODEgMCBSID4+CmVuZG9iago3MyAwIG9iago8PAogIC9TIC9UYWJsZQogIC9QIDYzIDAgUgogIC9LIFs4MyAwIFJdCj4+CmVuZG9iago4MyAwIG9iago8PAogIC9TIC9UUgogIC9QIDczIDAgUgogIC9LIFs4NCAwIFJdCj4+CmVuZG9iago4NCAwIG9iago8PAogIC9TIC9URAogIC9QIDgzIDAgUgogIC9LIFs4NSAwIFJdCj4+CmVuZG9iago4NSAwIG9iago8PAogIC9TIC9EaXYKICAvUCA4NCAwIFIKICAvSyBbMjggMCBSIDI5IDAgUiAzMCAwIFIgODYgMCBSXQo+PgplbmRvYmoKMjggMCBvYmoKPDwKICAvUyAvUAogIC9QIDg1IDAgUgogIC9LIFs8PAogIC9UeXBlIC9NQ1IKICAvUGcgNDMgMCBSCiAgL01DSUQgMTcKPj5dCj4+CmVuZG9iagoyOSAwIG9iago8PAogIC9TIC9QCiAgL1AgODUgMCBSCiAgL0sgWzw8CiAgL1R5cGUgL01DUgogIC9QZyA0MyAwIFIKICAvTUNJRCAxOAo+Pl0KPj4KZW5kb2JqCjMwIDAgb2JqCjw8CiAgL1MgL1NwYW4KICAvUCA4NSAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDE5Cj4+IDMxIDAgUl0KPj4KZW5kb2JqCjMxIDAgb2JqCjw8CiAgL1MgL1NwYW4KICAvUCAzMCAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDIwCj4+XQo+PgplbmRvYmoKODYgMCBvYmoKPDwgL1MgL1AgL1AgODUgMCBSID4+CmVuZG9iago3NCAwIG9iago8PAogIC9TIC9UYWJsZQogIC9QIDYzIDAgUgogIC9LIFs4NyAwIFJdCj4+CmVuZG9iago4NyAwIG9iago8PAogIC9TIC9UUgogIC9QIDc0IDAgUgogIC9LIFs4OCAwIFJdCj4+CmVuZG9iago4OCAwIG9iago8PAogIC9TIC9URAogIC9QIDg3IDAgUgogIC9LIFs4OSAwIFJdCj4+CmVuZG9iago4OSAwIG9iago8PAogIC9TIC9EaXYKICAvUCA4OCAwIFIKICAvSyBbMzIgMCBSIDMzIDAgUiAzNCAwIFIgOTAgMCBSXQo+PgplbmRvYmoKMzIgMCBvYmoKPDwKICAvUyAvUAogIC9QIDg5IDAgUgogIC9LIFs8PAogIC9UeXBlIC9NQ1IKICAvUGcgNDMgMCBSCiAgL01DSUQgMjEKPj5dCj4+CmVuZG9iagozMyAwIG9iago8PAogIC9TIC9QCiAgL1AgODkgMCBSCiAgL0sgWzw8CiAgL1R5cGUgL01DUgogIC9QZyA0MyAwIFIKICAvTUNJRCAyMgo+Pl0KPj4KZW5kb2JqCjM0IDAgb2JqCjw8CiAgL1MgL1NwYW4KICAvUCA4OSAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDIzCj4+IDM1IDAgUl0KPj4KZW5kb2JqCjM1IDAgb2JqCjw8CiAgL1MgL1NwYW4KICAvUCAzNCAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDI0Cj4+XQo+PgplbmRvYmoKOTAgMCBvYmoKPDwgL1MgL1AgL1AgODkgMCBSID4+CmVuZG9iago3NSAwIG9iago8PCAvUyAvUCAvUCA2MyAwIFIgPj4KZW5kb2JqCjM2IDAgb2JqCjw8CiAgL1MgL1AKICAvUCA2MyAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDI1Cj4+XQo+PgplbmRvYmoKNzYgMCBvYmoKPDwKICAvUyAvVGFibGUKICAvUCA2MyAwIFIKICAvSyBbOTEgMCBSXQo+PgplbmRvYmoKOTEgMCBvYmoKPDwKICAvUyAvVFIKICAvUCA3NiAwIFIKICAvSyBbOTIgMCBSXQo+PgplbmRvYmoKOTIgMCBvYmoKPDwKICAvUyAvVEQKICAvUCA5MSAwIFIKICAvSyBbOTMgMCBSXQo+PgplbmRvYmoKOTMgMCBvYmoKPDwKICAvUyAvRGl2CiAgL1AgOTIgMCBSCiAgL0sgWzM3IDAgUiA5NCAwIFJdCj4+CmVuZG9iagozNyAwIG9iago8PAogIC9TIC9QCiAgL1AgOTMgMCBSCiAgL0sgWzw8CiAgL1R5cGUgL01DUgogIC9QZyA0MyAwIFIKICAvTUNJRCAyNgo+Pl0KPj4KZW5kb2JqCjk0IDAgb2JqCjw8CiAgL1MgL1AKICAvUCA5MyAwIFIKICAvSyBbMzggMCBSXQo+PgplbmRvYmoKMzggMCBvYmoKPDwKICAvUyAvU3BhbgogIC9QIDk0IDAgUgogIC9LIFs8PAogIC9UeXBlIC9NQ1IKICAvUGcgNDMgMCBSCiAgL01DSUQgMjcKPj5dCj4+CmVuZG9iago3NyAwIG9iago8PAogIC9TIC9UYWJsZQogIC9QIDYzIDAgUgogIC9LIFs5NSAwIFJdCj4+CmVuZG9iago5NSAwIG9iago8PAogIC9TIC9UUgogIC9QIDc3IDAgUgogIC9LIFs5NiAwIFJdCj4+CmVuZG9iago5NiAwIG9iago8PAogIC9TIC9URAogIC9QIDk1IDAgUgogIC9LIFs5NyAwIFJdCj4+CmVuZG9iago5NyAwIG9iago8PAogIC9TIC9EaXYKICAvUCA5NiAwIFIKICAvSyBbMzkgMCBSIDk4IDAgUl0KPj4KZW5kb2JqCjM5IDAgb2JqCjw8CiAgL1MgL1AKICAvUCA5NyAwIFIKICAvSyBbPDwKICAvVHlwZSAvTUNSCiAgL1BnIDQzIDAgUgogIC9NQ0lEIDI4Cj4+XQo+PgplbmRvYmoKOTggMCBvYmoKPDwKICAvUyAvUAogIC9QIDk3IDAgUgogIC9LIFs5OSAwIFJdCj4+CmVuZG9iago5OSAwIG9iago8PCAvUyAvU3BhbiAvUCA5OCAwIFIgPj4KZW5kb2JqCjc4IDAgb2JqCjw8IC9TIC9QIC9QIDYzIDAgUiA+PgplbmRvYmoKNDUgMCBvYmoKPDwgL1R5cGUgL1BhZ2VzCi9Db3VudCAxCi9LaWRzIFs0MyAwIFIgXSA+PgplbmRvYmoKMTAwIDAgb2JqCjw8CiAgL1R5cGUgL0NhdGFsb2cKICAvUGFnZXMgNDUgMCBSCiAgL0xhbmcgKGVuKQogIC9NYXJrSW5mbyA8PCAvTWFya2VkIHRydWUgPj4KICAvU3RydWN0VHJlZVJvb3QgNTYgMCBSCiAgL01ldGFkYXRhIDUgMCBSCiAgL1BhZ2VMYWJlbHMgMTAxIDAgUgogIC9WaWV3ZXJQcmVmZXJlbmNlcyA8PCAvRGlzcGxheURvY1RpdGxlIHRydWUgPj4KPj4KZW5kb2JqCjQ0IDAgb2JqCjw8CiAgL0ZvbnQgPDwgL0YxNSA1MSAwIFIgPj4KICAvUHJvY1NldCBbL1BERiAvSW1hZ2VCIC9JbWFnZUMgL1RleHRdCiAgL0NvbG9yU3BhY2UgPDwgL0RlZmF1bHRSR0IgNCAwIFIgPj4KPj4KZW5kb2JqCjU2IDAgb2JqCjw8CiAgL1R5cGUgL1N0cnVjdFRyZWVSb290CiAgL0sgWzU1IDAgUl0KICAvUGFyZW50VHJlZSA8PCAvS2lkcyBbMTAyIDAgUl0gPj4KPj4KZW5kb2JqCjEwMSAwIG9iago8PCAvTnVtcyBbMCA8PCAvUyAvRCA+Pl0gPj4KZW5kb2JqCjEwMiAwIG9iago8PCAvTnVtcyBbMCAxMiAwIFIgMSAxNCAwIFIgMiAxNCAwIFIgMyA3MCAwIFJdIC9MaW1pdHMgWzAgM10gPj4KZW5kb2JqCnhyZWYKMCAxMDMKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMDE1IDAwMDAwIG4gCjAwMDAwMDAxODEgMDAwMDAgbiAKMDAwMDAwMjY4NSAwMDAwMCBuIAowMDAwMDAyNzA1IDAwMDAwIG4gCjAwMDAwMDI3MzggMDAwMDAgbiAKMDAwMDAwMzg2NyAwMDAwMCBuIAowMDAwMDAzODg3IDAwMDAwIG4gCjAwMDAwMDQxMjggMDAwMDAgbiAKMDAwMDAwNDI3OSAwMDAwMCBuIAowMDAwMDA0NDI5IDAwMDAwIG4gCjAwMDAwMDQ0OTUgMDAwMDAgbiAKMDAwMDAwNDY0OCAwMDAwMCBuIAowMDAwMDI5OTc3IDAwMDAwIG4gCjAwMDAwMzAyNjAgMDAwMDAgbiAKMDAwMDAzMDQ5NiAwMDAwMCBuIAowMDAwMDMwNzg2IDAwMDAwIG4gCjAwMDAwMzA4ODcgMDAwMDAgbiAKMDAwMDAzMTEzNiAwMDAwMCBuIAowMDAwMDMxMjI4IDAwMDAwIG4gCjAwMDAwMzEzMTkgMDAwMDAgbiAKMDAwMDAzMTQxMCAwMDAwMCBuIAowMDAwMDMxNTAxIDAwMDAwIG4gCjAwMDAwMzE3MTYgMDAwMDAgbiAKMDAwMDAzMjA2MSAwMDAwMCBuIAowMDAwMDMyMTUzIDAwMDAwIG4gCjAwMDAwMzIyNDUgMDAwMDAgbiAKMDAwMDAzMjM0NyAwMDAwMCBuIAowMDAwMDMyNzMzIDAwMDAwIG4gCjAwMDAwMzI4MjUgMDAwMDAgbiAKMDAwMDAzMjkxNyAwMDAwMCBuIAowMDAwMDMzMDE5IDAwMDAwIG4gCjAwMDAwMzM0MDUgMDAwMDAgbiAKMDAwMDAzMzQ5NyAwMDAwMCBuIAowMDAwMDMzNTg5IDAwMDAwIG4gCjAwMDAwMzM2OTEgMDAwMDAgbiAKMDAwMDAzMzg2MiAwMDAwMCBuIAowMDAwMDM0MTkzIDAwMDAwIG4gCjAwMDAwMzQzNDEgMDAwMDAgbiAKMDAwMDAzNDY3NSAwMDAwMCBuIAowMDAwMDA0ODY5IDAwMDAwIG4gCjAwMDAwMDYyNDQgMDAwMDAgbiAKMDAwMDAwNjI2NSAwMDAwMCBuIAowMDAwMDA2MzA0IDAwMDAwIG4gCjAwMDAwMzUxNzYgMDAwMDAgbiAKMDAwMDAzNDkwMiAwMDAwMCBuIAowMDAwMDA2NTQ1IDAwMDAwIG4gCjAwMDAwMDY4MDYgMDAwMDAgbiAKMDAwMDAyODE0MCAwMDAwMCBuIAowMDAwMDI4MTE4IDAwMDAwIG4gCjAwMDAwMjgyNDEgMDAwMDAgbiAKMDAwMDAyODI2MCAwMDAwMCBuIAowMDAwMDI4ODc5IDAwMDAwIG4gCjAwMDAwMjg0MjEgMDAwMDAgbiAKMDAwMDAyOTQzNSAwMDAwMCBuIAowMDAwMDI5NDU1IDAwMDAwIG4gCjAwMDAwMzUzMDIgMDAwMDAgbiAKMDAwMDAyOTUxOCAwMDAwMCBuIAowMDAwMDI5NTkzIDAwMDAwIG4gCjAwMDAwMjk2NTIgMDAwMDAgbiAKMDAwMDAyOTcxMCAwMDAwMCBuIAowMDAwMDI5NzcwIDAwMDAwIG4gCjAwMDAwMjk4MzQgMDAwMDAgbiAKMDAwMDAzMDk4MSAwMDAwMCBuIAowMDAwMDI5ODkxIDAwMDAwIG4gCjAwMDAwMzAwNjkgMDAwMDAgbiAKMDAwMDAzMDEwNyAwMDAwMCBuIAowMDAwMDMwMjA0IDAwMDAwIG4gCjAwMDAwMzA1OTAgMDAwMDAgbiAKMDAwMDAzMDE2MyAwMDAwMCBuIAowMDAwMDMwNjQ2IDAwMDAwIG4gCjAwMDAwMzE2NzggMDAwMDAgbiAKMDAwMDAzMTgwOCAwMDAwMCBuIAowMDAwMDMyNDgwIDAwMDAwIG4gCjAwMDAwMzMxNTIgMDAwMDAgbiAKMDAwMDAzMzgyNCAwMDAwMCBuIAowMDAwMDMzOTU0IDAwMDAwIG4gCjAwMDAwMzQ0MzYgMDAwMDAgbiAKMDAwMDAzNDg2NCAwMDAwMCBuIAowMDAwMDMxODY4IDAwMDAwIG4gCjAwMDAwMzE5MjUgMDAwMDAgbiAKMDAwMDAzMTk4MiAwMDAwMCBuIAowMDAwMDMyNDQyIDAwMDAwIG4gCjAwMDAwMzI1NDAgMDAwMDAgbiAKMDAwMDAzMjU5NyAwMDAwMCBuIAowMDAwMDMyNjU0IDAwMDAwIG4gCjAwMDAwMzMxMTQgMDAwMDAgbiAKMDAwMDAzMzIxMiAwMDAwMCBuIAowMDAwMDMzMjY5IDAwMDAwIG4gCjAwMDAwMzMzMjYgMDAwMDAgbiAKMDAwMDAzMzc4NiAwMDAwMCBuIAowMDAwMDM0MDE0IDAwMDAwIG4gCjAwMDAwMzQwNzEgMDAwMDAgbiAKMDAwMDAzNDEyOCAwMDAwMCBuIAowMDAwMDM0Mjg1IDAwMDAwIG4gCjAwMDAwMzQ0OTYgMDAwMDAgbiAKMDAwMDAzNDU1MyAwMDAwMCBuIAowMDAwMDM0NjEwIDAwMDAwIG4gCjAwMDAwMzQ3NjcgMDAwMDAgbiAKMDAwMDAzNDgyMyAwMDAwMCBuIAowMDAwMDM0OTYyIDAwMDAwIG4gCjAwMDAwMzUzOTggMDAwMDAgbiAKMDAwMDAzNTQ0MyAwMDAwMCBuIAp0cmFpbGVyCjw8CiAgL1Jvb3QgMTAwIDAgUgogIC9JbmZvIDEgMCBSCiAgL0lEIFs8QTJENUIxNDA3MzU3QTcxQThDNUQ3RDQ5RDdDODg4MjQ+IDxBMkQ1QjE0MDczNTdBNzFBOEM1RDdENDlEN0M4ODgyND5dCiAgL1NpemUgMTAzCj4+CnN0YXJ0eHJlZgozNTUyNAolJUVPRgo="
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Extra Profile Data
        # Freshdata | Fresh Linkedin Profile Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in
            API_Endpoint_List if i.http_path == (
                'https://fresh-linkedin-profile-data.p.rapidapi.com'
                '/get-extra-profile-data') and
            i.nice_name == "Get Extra Profile Data")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
        {
          "data": {
            "awards": [
              "Innovation Judge: Spikes Asia Festival of Creativity",
              "2016 LinkedIn Agency Publisher of the Year - Asia Pacific",
              "LinkedIn Global Goodwill Ambassador",
              "Top 1% - Industry Social Selling Index",
              "2018 LinkedIn Power Profile - Marketing & Advertising"
            ],
            "certifications": [
              "Programmatic Advertising Foundations",
              "The 3-Minute Rule: Say Less to Get More",
              "Communicating with Confidence",
              "How to Become a Thought Leader and Advance Your Career",
              "Delivering an Authentic Elevator Pitch"
            ],
            "languages": [
              "English (Native or Bilingual)"
            ],
            "patents": [
              "Wine Cube"
            ],
            "publications": [
              "Young Consumers: Insights and Ideas for Responsible Marketers",
              "Innovation Invigorates Agency Growth",
              "Anthony James on Tackling Digital Transformation",
              "The Maker Movement delivering cutting-edge marketing tech",
              "The Yawn Known as HR Gamification"
            ],
            "skills": [
              "International Marketing",
              "Social Media Marketing",
              "Entrepreneurship"
            ]
          },
          "message": "ok"
        }\
        """,
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " +
              str(new_api_endpoint_nice_name))

        db.session.close()
        print(APIEndpointExtra.__tablename__ + " seeded successfully! (1/9)")

    except Exception as e:
        print(f"Error committing data: {e}")

# Example Seed Format
# extra_documentation stores LONGTEXT in the column.
"""
        # API Endpoint Nice Name
        # API List URL Nice Name,
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List
            if i.http_path == (
                '') and
            i.nice_name == "")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation="""\
\
""",
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))
"""
