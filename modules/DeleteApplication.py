import requests

# Documentation: http://www.mulesoft.org/documentation/display/current/Delete+Application
def make_request(arguments):
    app_name = arguments.get('app_name')
    cloudhub_user = arguments.get('cloudhub_user')
    cloudhub_pass = arguments.get('cloudhub_pass')

    baseurl = "https://cloudhub.io/api/applications/"

    response = requests.delete(baseurl + app_name, auth=(cloudhub_user, cloudhub_pass))

    print "Response received: " + str(
        response) + " (if the resource is successfully deleted, the service returns a 204)"
