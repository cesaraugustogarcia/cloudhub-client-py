import requests
import sys
import json
import pprint

# Documentation: http://www.mulesoft.org/documentation/display/current/Get+Application
def make_request(arguments):
    app_name = arguments.get('app_name')
    cloudhub_user = arguments.get('cloudhub_user')
    cloudhub_pass = arguments.get('cloudhub_pass')
    
    baseurl = 'https://cloudhub.io/api/applications/'

    response = requests.get(baseurl + app_name, auth=(cloudhub_user, cloudhub_pass))

    if (response.status_code == 200):
        json_response = json.loads(response.text)

        pp = pprint.PrettyPrinter()

        def my_safe_repr(object, context, maxlevels, level):
            typ = pprint._type(object)
            if typ is unicode:
                object = str(object)
            return pprint._safe_repr(object, context, maxlevels, level)

        pp.format = my_safe_repr

        pp.pprint(json_response)
    else:
        print "Get Application Failed. Check App name and credentials."

    

