import requests
import json
from UpdateApplicationMetadata import propertiesParser


# Documentation: http://www.mulesoft.org/documentation/display/current/Create+Application
def make_request(arguments):
    app_name = arguments.get('app_name')
    cloudhub_user = arguments.get('cloudhub_user')
    cloudhub_pass = arguments.get('cloudhub_pass')
    properties_path = arguments.get('properties_path')
    mule_version = arguments.get('mule_version')

    base_url = "https://cloudhub.io/api/applications"
    headers = {"content-type": "application/json"}
    body = {
        "domain": app_name,
        "workers": 1,
        "muleVersion": mule_version,
        "properties": propertiesParser(properties_path).get("properties")
    }
    
    response = requests.post(base_url, data=json.dumps(body), auth=(cloudhub_user, cloudhub_pass),
                             headers=headers)

    print "Response received: " + str(response.text)
