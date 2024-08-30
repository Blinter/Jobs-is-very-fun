"""
Conversions

Convert data for processing
"""

import json
from flask import jsonify


def convert_bytes_to_dict_raw(data: str, quiet=True):
    """
    Converts bytes into a dictionary
    """
    dict_new = json.loads(data)

    if isinstance(dict_new, dict):
        # print(str(dict_new), flush=True)

        # Jobwiz | Job Search API
        if dict_new.get('jobs', None) is not None:
            dict_new = dict_new.get('jobs')

        # Dodocr7 | Google Jobs
        elif dict_new.get('googleUrl', None) is not None:
            dict_new = {dict_new.get('googleUrl'): dict_new}

        # RockAPIs | Rapid Linkedin Jobs API
        # mgujjargamingm | LinkedIn Data Scraper
        elif dict_new.get('data', None) is not None:
            dict_new = dict_new.get('data')

            if isinstance(dict_new, dict):

                # APIJobs | Job Searching API
                # Flatroy | Jobs from Remoteok
                # Get job by id
                if dict_new.get('id', None) is not None:
                    dict_new = {str(dict_new.get('id')): dict_new}

                # Freshdata | Linkedin Jobs
                # Get Job Details
                elif dict_new.get('job_id', None) is not None:
                    dict_new = {str(dict_new.get('job_id')): dict_new}

                # Relu Consultancy | Indeed Scraper API - Germany
                # Job View
                elif dict_new.get('jobKey', None) is not None:
                    dict_new = {str(dict_new.get('jobKey')): dict_new}

                # mgujjargamingm | LinkedIn Data Scraper
                elif (isinstance(dict_new, dict) and
                        dict_new.get('companyId', None) is not None):
                    dict_new = {dict_new.get('companyId'): dict_new}

                # RockAPIs | Linkedin API
                elif (isinstance(dict_new, dict) and
                      dict_new.get('items', None) is not None):
                    dict_new = dict_new.get('items')

                # letscrape | Real-Time Glassdoor Data
                # Company Overview
                elif (isinstance(dict_new, dict) and
                        dict_new.get('company_id', None) is not None):
                    dict_new = {dict_new.get('company_id'): dict_new}

        # avadataservices | Job Postings
        elif dict_new.get('slug', None) is not None:
            dict_new = {str(dict_new.get('slug')): dict_new}

        # APIJobs | Job Searching API
        # Search jobs

        elif dict_new.get('hits', None) is not None:
            dict_new = dict_new.get('hits')

        # Lundehund | Twitter X Job API
        # Get Job Detail
        elif dict_new.get('id', None) is not None:
            dict_new = {str(dict_new.get('id')): dict_new}

        # mgujjargamingm | LinkedIn Data Scraper
        # Suggestion Company Size
        elif dict_new.get('suggestions', None) is not None:
            dict_new = dict_new.get('suggestions')

        # mgujjargamingm | LinkedIn Data Scraper
        elif dict_new.get('response', None) is not None:

            dict_new = dict_new.get('response')

            if isinstance(dict_new, list):

                # Empty Response bug
                if len(dict_new) == 0:
                    return {'error': "Empty response from API"}

                dict_new = dict_new[0]

            elif isinstance(dict_new, dict):

                # mgujjargamingm | Linkedin BULK data scraper
                if dict_new.get('jobs', None) is not None:
                    dict_new = dict_new.get('jobs')

                    if isinstance(dict_new, list):
                        new_dict = []
                        for i in dict_new:
                            if i.get('data') is not None:
                                new_dict.append(i.get('data'))

                        if len(new_dict) != 0:
                            dict_new = new_dict

                        # print(str(temp_dict), flush=True)
                # raise ValueError("Processing")

            # mgujjargamingm | LinkedIn Data Scraper
            if (isinstance(dict_new, dict) and
                    dict_new.get('data', None) is not None):
                dict_new = dict_new.get('data')

            # mgujjargamingm | LinkedIn Data Scraper
            if (isinstance(dict_new, dict) and
                    dict_new.get('jobs', None) is not None):
                dict_new = dict_new.get('jobs')

        # bareq | Remote Jobs API
        # sohailglt | Linkedin Live Data
        elif dict_new.get('results', None) is not None:
            dict_new = dict_new.get('results')

        # sohailglt | Linkedin Live Data
        # Get Company Details
        elif dict_new.get('details', None) is not None:
            dict_new = dict_new.get('details', None)

            if (isinstance(dict_new, dict) and
                    dict_new.get('company_id', None) is not None):
                dict_new = {dict_new.get('company_id'): dict_new}

        # mantiks | Indeed
        # Get Company Details
        elif dict_new.get('indeed_final_url', None) is not None:
            # Strip view ID
            new_id = dict_new['indeed_final_url']
            new_id = new_id.replace(
                'https://www.indeed.com/viewjob?jk=',
                ''
            ).replace(
                '&vjs=3',
                ''
            ).replace(
                'https://www.indeed.com/cmp/',
                ''
            )
            dict_new = {new_id: dict_new}

        # omarmohamed0 | Jobs API
        elif dict_new.get('freelancers', None) is not None:
            dict_new = dict_new.get('freelancers', None)
            # Extract profile
            if dict_new is not None and isinstance(dict_new, list):
                new_dict = {}
                for j, i in enumerate(dict_new):
                    new_dict[
                        (
                            dict_new[j]['freelancerProfile']
                        ).replace('https://freelancer.com/u/', '')] = (
                        dict_new[j]
                    )
                dict_new = new_dict

        # omarmohamed0 | Jobs API
        elif dict_new.get('posts', None) is not None:
            dict_new = dict_new.get('posts')
            # Extract project
            if dict_new is not None and isinstance(dict_new, list):
                new_dict = {}
                for j, i in enumerate(dict_new):
                    new_dict[
                        (
                            dict_new[j]['project-link']
                        ).replace(
                            'https://www.freelancer.com/projects/', '')] = (
                        dict_new[j]
                    )
                dict_new = new_dict

    if isinstance(dict_new, list):
        if len(dict_new) == 0:
            if not quiet:
                print("Error: Row data is empty.", flush=True)
            return {"error": "error - no results"}

        new_dict_from_list = {}

        # Iterate through the list and extract the dictionaries
        if not quiet:
            print("Processing List (Not a dictionary)", flush=True)

        for (index, i) in enumerate([i for i in dict_new]):
            if not isinstance(i, dict):
                if not quiet:
                    print("Error: Row data is not a dictionary", flush=True)
                return {"error": "Row data not a dictionary, no results."}

            # Find id and set to index
            new_id = index
            if i.get('id', None) is not None:
                new_id = i.get('id')
                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)

                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # Find IdNumber and set to index
            # Betoalien | USA Jobs for IT
            elif i.get('IdNumber', None) is not None:
                new_id = i.get('IdNumber')
                # find unique URL and set as key
                if i.get('url', None) is not None:
                    new_id = i.get('url')
                    if new_id.find("https://jooble.org/jdp/") != -1:
                        new_id = new_id[(
                                new_id.find("https://jooble.org/jdp/") +
                                len("https://jooble.org/jdp/")
                        ):]
                    elif (new_id.find(
                            "https://www.linkedin.com/jobs/view/") != -1 and
                          new_id.find('?position=')):
                        new_id = new_id[(
                                new_id.find(
                                    "https://www.linkedin.com/jobs/view/") +
                                len("https://www.linkedin.com/jobs/view/")
                        ):new_id.find('?position=')]
                    elif new_id == 'undefined':
                        # No link - Skip
                        continue

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # Find job_urn and set to index
            elif i.get('job_urn', None) is not None:
                new_id = i.get('job_urn')

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # Find ID and set to index
            elif i.get('ID', None) is not None:
                new_id = i.get('ID')

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # Find job_id and set to index
            # jaypat87 | Linkedin Jobs Search
            elif i.get('job_id', None) is not None:
                new_id = i.get('job_id')

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # Relu Consultancy | Indeed Scraper API - Germany
            elif i.get('jobKey', None) is not None:
                new_id = i.get('jobKey')

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # Relu Consultancy | Arbeitsagentur
            elif i.get('refnr', None) is not None:
                new_id = i.get('refnr')

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # sohailglt | Linkedin Live Data
            # Company Search
            elif i.get('company_id', None) is not None:
                new_id = i.get('company_id')

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))),
                    #       flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # mantiks | Indeed
            elif i.get('indeed_final_url', None) is not None:

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # mgujjargamingm | LinkedIn Data Scraper
            elif i.get('jobPostingUrl', None) is not None:
                # Strip view ID
                new_id = i.get('jobPostingUrl')
                new_id = new_id.replace(
                    'https://www.linkedin.com/jobs/view/',
                    ''
                ).replace(
                    '/?trk=jobs_biz_prem_srch',
                    ''
                )

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # mgujjargamingm | LinkedIn Bulk Data Scraper
            elif i.get('jobPostingUrn', None) is not None:
                new_id = i.get('jobPostingUrn')

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # mgujjargamingm | LinkedIn Data Scraper
            # Search GeoUrns
            elif i.get('urn', None) is not None:
                new_id = i.get('urn')

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # mgujjargamingm | LinkedIn Data Scraper
            # Search Companies with Filters
            elif i.get('companyId', None) is not None:
                new_id = i.get('companyId')

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # vuesdata | Indeed Jobs
            # vuesdata | Indeed Jobs - Sweden
            # vuesdata | Indeed Jobs - Finland
            # vuesdata | Indeed Jobs - Denmark
            # Search Jobs
            elif i.get('job_url', None) is not None:
                # Remove URL from link and extract job ID
                new_id = i.get('job_url')
                if (new_id.find("jk=") != -1 and
                        new_id.find("&from=vjs") != -1):
                    new_id = new_id[new_id.find("jk=") + len("jk="):
                                    new_id.find("&from=vjs")]

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # jaypat87 | Linkedin Jobs Search
            # Jobs Search
            elif i.get('url', None) is not None:
                # Extract from URL
                new_id = i.get('url')
                if (new_id.find("jk=") != -1 and
                        new_id.find("&bb=erp") != -1):
                    new_id = new_id[new_id.find("jk=") + len("jk="):
                                    new_id.find("&bb=erp")]

                if str(new_id) in new_dict_from_list:
                    if not quiet:
                        print("CONFLICTING ID: " + str(new_id) +
                              " Action: Keeping values with most data",
                              flush=True)
                    # print("old: " + str(len(str(
                    #     new_dict_from_list[str(new_id)]))), flush=True)
                    # print("new: " + str(len(str(dict_new[index]))),
                    #       flush=True)
                    if (len(str(new_dict_from_list[str(new_id)].values())) <
                            len(str(dict_new[index].values()))):
                        # print("Replacing", flush=True)
                        new_dict_from_list[str(new_id)] = dict_new[index]

                    else:
                        # print("KEEPING" + str(
                        #     new_dict_from_list[str(new_id)]), flush=True)
                        i = None

                else:
                    new_dict_from_list[str(new_id)] = dict_new[index]

            # Flatroy | Jobs from Remoteok
            # Get list
            elif (i.get('legal', None) is not None and
                    i.get('last_updated', None) is not None and
                    len(i.keys()) == 2):
                continue

            if i is not None and isinstance(i, dict):
                for j in [j for j in i.keys()]:
                    if i[str(j)] is not None:
                        i[str(j)] = ' '.join(str(i.get(str(j))).split())

                # Clean up data here
                new_dict_from_list[str(new_id)] = i

        return new_dict_from_list

    if not isinstance(dict_new, dict):
        return "Data is not a dictionary."
        # return jsonify(dict_new)

    return dict_new


def convert_bytes_to_dict(data: str):
    """
    Converts bytes into a dictionary
    """
    return jsonify(convert_bytes_to_dict_raw(data=data))
