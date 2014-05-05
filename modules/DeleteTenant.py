import requests
import json

# Documentation: http://www.mulesoft.org/documentation/display/current/Tenants

# Constants
baseurl = 'https://cloudhub.io/api/applications/'
api_call_paths = {
	'tenants': '/tenants'
}
headers = {'content-type': 'application/json'}
app_domain = ""
cloudhub_user = ""
cloudhub_pass = ""

# Cloudhub operations
def delete_tenant(tenant_id):
	print "Deleting tenant. ID = " + tenant_id
	response = requests.delete(baseurl + app_domain + api_call_paths['tenants'] + "/" + tenant_id, headers=headers, auth=(cloudhub_user, cloudhub_pass))

	if (response.status_code == 204):
		print "Tenant successfully deleted."
	else:
		print "Delete operation failed."

# Entry point
def make_request(arguments):
	global app_domain
	global cloudhub_user
	global cloudhub_pass

	app_domain = arguments.get('app_name')
	cloudhub_user = arguments.get('cloudhub_user')
	cloudhub_pass = arguments.get('cloudhub_pass')
	tenant_id = arguments.get('tenant_id')

	delete_tenant(tenant_id)