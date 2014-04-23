import requests

# Documentation: http://www.mulesoft.org/documentation/display/current/Delete+Application
def make_request(arguments):
    cloudhub_user = arguments[2]
    cloudhub_pass = arguments[3]
    app_name = arguments[4]

    baseurl = "https://cloudhub.io/api/applications/"

    response = requests.delete(baseurl + app_name, auth=(cloudhub_user, cloudhub_pass))

    print "Response received: " + str(
        response) + " (if the resource is successfully deleted, the service returns a 204)"
