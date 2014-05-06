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
def save_all_tenants():
	response = requests.get(baseurl + app_domain + api_call_paths['tenants'], headers=headers, auth=(cloudhub_user, cloudhub_pass))

	if (response.status_code == 200):
		json_response = json.loads(response.text)
		tenant_list = json_response['data']
	
		for tenant in tenant_list:
			tenant_id = tenant['id']
			print "Saving tenant. ID = " + tenant_id
			print ""
			print "Tenant information"
			print "******************"
			print "ID: " + tenant_id
			print "Name: " + tenant['name']
			print "E-mail: " + tenant['email']
			print "Created: " + tenant['created']
			print "Enabled: " + str(tenant['enabled'])
			propertiesSaver(tenant['configuration'], tenant_id + ".properties")
			print "Properties saved in \'" + tenant_id + ".properties\' file."
			print "******************"
			print ""
	else:
		print "Retrieve operation failed."

# Utils
def propertiesSaver(configuration, file_path):
	with open(file_path, "w") as propertiesFile:
		for key in configuration.keys():
			propertiesFile.write(key + "=" + configuration[key] + "\n")
		propertiesFile.close()

# Entry point
def make_request(arguments):
	global app_domain
	global cloudhub_user
	global cloudhub_pass

	app_domain = arguments.get('app_name')
	cloudhub_user = arguments.get('cloudhub_user')
	cloudhub_pass = arguments.get('cloudhub_pass')

	save_all_tenants()