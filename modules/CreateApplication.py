import requests
import json
from UpdateApplicationMetadata import propertiesParser


# Documentation: http://www.mulesoft.org/documentation/display/current/Create+Application
def make_request(arguments):
    cloudhub_user = arguments[2]
    cloudhub_pass = arguments[3]
    app_name = arguments[4]
    properties_path = arguments[5]
    mule_version = arguments[6]

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
