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
def set_tenant_status(tenant_id, status):
	new_tenant_map = {
		'id': tenant_id,
		'enabled': status
	}

	print "Updating tenant. ID = " + tenant_id
	response = requests.put(baseurl + app_domain + api_call_paths['tenants'] + "/" + tenant_id, data=json.dumps(new_tenant_map), headers=headers , auth=(cloudhub_user, cloudhub_pass))
	if (response.status_code == 200):
		print "Tenant successfully updated."
	else:
		print "Update operation failed."

# Entry point
def make_request(arguments):
	global app_domain
	global cloudhub_user
	global cloudhub_pass

	app_domain = arguments.get('app_name')
	cloudhub_user = arguments.get('cloudhub_user')
	cloudhub_pass = arguments.get('cloudhub_pass')
	tenant_id = arguments.get('tenant_id')
	status = arguments.get('status')

	# CloudHub Operation
	if status in ['enabled','disabled']:
		set_tenant_status(tenant_id, status == "enabled")
	else:
		print "Invalid status value. Possible values are 'enabled' or 'disabled'."
