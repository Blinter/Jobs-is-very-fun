"""
API Endpoint Extras 9

Seed file can be run
cd <base_dir>
PYTHONPATH=<base_dir> python3 <base_dir>/<file_name>.py
"""
from models.mariadb.api_list_url import APIListURL
from models.mariadb.api_headers import APIHeader
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.api_endpoint_params import APIEndpointParam
from models.mariadb.api_endpoint_bodies import APIEndpointBody
from models.mariadb.api_endpoint_headers import APIEndpointHeader
from models.mariadb.api_endpoint_extras import APIEndpointExtra
from app import create_app, db

app = create_app()

with app.app_context():
    try:

        # retrieve API Endpoints in order to reference foreign keys.
        API_Endpoint_List = db.session.query(APIEndpoint).all()

        # Company Search
        # sohailglt | Linkedin Live Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List
            if i.http_path == (
                'https://linkedin-live-data.p.rapidapi.com'
                '/company-search') and
            i.nice_name == "Company Search")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation='''\
{
  
"type"
: 
"object"
,
  
"properties"
: {
    
"per_page"
: {
      
"type"
: 
"integer"

    },
    
"offset"
: {
      
"type"
: 
"integer"

    },
    
"keyword"
: {
      
"type"
: 
"string"

    },
    
"followers"
: {
      
"type"
: 
"string"

    },
    
"industries"
: {
      
"type"
: 
"array"
,
      
"items"
: {
        
"type"
: 
"string"

      }
    },
    
"country_codes"
: {
      
"type"
: 
"array"
,
      
"items"
: {
        
"type"
: 
"string"

      }
    },
    
"company_size"
: {
      
"type"
: 
"string"

    },
    
"year_founded"
: {
      
"type"
: 
"string"

    },
    
"company_type"
: {
      
"type"
: 
"string"

    },
    
"website"
: {
      
"type"
: 
"string"

    }
  }
}
''',
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # People Search
        # sohailglt | Linkedin Live Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List
            if i.http_path == (
                'https://linkedin-live-data.p.rapidapi.com'
                '/people-search') and
            i.nice_name == "People Search")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation='''\
{
  
"type"
: 
"object"
,
  
"properties"
: {
    
"per_page"
: {
      
"type"
: 
"integer"

    },
    
"offset"
: {
      
"type"
: 
"integer"

    },
    
"keyword"
: {
      
"type"
: 
"string"

    },
    
"countries"
: {
      
"type"
: 
"array"
,
      
"items"
: {
        
"type"
: 
"string"

      }
    },
    
"current_companies"
: {
      
"type"
: 
"array"
,
      
"items"
: {
        
"type"
: 
"string"

      }
    },
    
"past_companies"
: {
      
"type"
: 
"array"
,
      
"items"
: {
        
"type"
: 
"string"

      }
    },
    
"current_job_title"
: {
      
"type"
: 
"string"

    },
    
"past_job_title"
: {
      
"type"
: 
"string"

    },
    
"industry"
: {
      
"type"
: 
"string"

    },
    
"certification"
: {
      
"type"
: 
"string"

    },
    
"edu_degree"
: {
      
"type"
: 
"string"

    },
    
"study_field"
: {
      
"type"
: 
"string"

    },
    
"school_name"
: {
      
"type"
: 
"string"

    }
  }
}
''',
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Profile Details
        # sohailglt | Linkedin Live Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List
            if i.http_path == (
                'https://linkedin-live-data.p.rapidapi.com'
                '/profile-details') and
            i.nice_name == "Get Profile Details")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation='''\
{
  
"type"
: 
"object"
,
  
"properties"
: {
    
"profile_id"
: {
      
"type"
: 
"string"

    },
    
"profile_type"
: {
      
"type"
: 
"string"

    },
    
"contact_info"
: {
      
"type"
: 
"boolean"

    },
    
"recommendations"
: {
      
"type"
: 
"boolean"

    },
    
"related_profiles"
: {
      
"type"
: 
"boolean"

    },
    
"network_info"
: {
      
"type"
: 
"boolean"

    }
  }
}
''',
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        # Get Company Details
        # sohailglt | Linkedin Live Data
        new_api_endpoint_id, new_api_endpoint_nice_name = next(
            (i.id, i.nice_name) for i in API_Endpoint_List
            if i.http_path == (
                'https://linkedin-live-data.p.rapidapi.com'
                '/profile-details') and
            i.nice_name == "Get Company Details")
        db.session.add_all([
            APIEndpointExtra(
                api_endpoint_id=new_api_endpoint_id,
                extra_documentation='''\
{
  
"type"
: 
"object"
,
  
"properties"
: {
    
"profile_id"
: {
      
"type"
: 
"string"

    },
    
"profile_type"
: {
      
"type"
: 
"string"

    },
    
"contact_info"
: {
      
"type"
: 
"boolean"

    },
    
"recommendations"
: {
      
"type"
: 
"boolean"

    },
    
"related_profiles"
: {
      
"type"
: 
"boolean"

    },
    
"network_info"
: {
      
"type"
: 
"boolean"

    }
  }
}\
''',
            ),
        ])
        db.session.commit()
        print(APIEndpointExtra.__tablename__ + " seeded " + str(new_api_endpoint_nice_name))

        db.session.close()
        print(APIEndpointExtra.__tablename__ + " seeded successfully! (9/9)")

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
