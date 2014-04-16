import requests
import sys
import json
import pprint

# Documentation: http://www.mulesoft.org/documentation/display/current/Get+Application
def make_request(app_name, cloudhub_user, cloudhub_pass):
    baseurl = 'https://cloudhub.io/api/applications/'

    response = requests.get(baseurl + app_name, auth=(cloudhub_user, cloudhub_pass))

    json_response = json.loads(response.text)

    pp = pprint.PrettyPrinter()

    def my_safe_repr(object, context, maxlevels, level):
        typ = pprint._type(object)
        if typ is unicode:
            object = str(object)
        return pprint._safe_repr(object, context, maxlevels, level)


    pp.format = my_safe_repr

    pp.pprint(json_response)
