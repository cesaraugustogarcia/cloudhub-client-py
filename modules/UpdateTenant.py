import requests
import json
import re

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

regex_filename = '^\/?(.+\/)*(.+)\.properties$'

# Cloudhub operations
def update_tenant(tenant_id, configuration):
	new_tenant_map = {
		'id': tenant_id,
		'configuration': configuration
	}

	print "Updating tenant. ID = " + tenant_id
	response = requests.put(baseurl + app_domain + api_call_paths['tenants'] + "/" + tenant_id, data=json.dumps(new_tenant_map), headers=headers , auth=(cloudhub_user, cloudhub_pass))
	if (response.status_code == 200):
		print "Tenant successfully updated."
	else:
		print "Update operation failed."

# Utils
def propertiesParser(file_path):
	configuration = {}
	with open(file_path, "rb") as propertiesFile:
		i = iter(propertiesFile)
		for line in i:
			if ("=" in line) and ("#" not in line):
				pair = line.rstrip().split("=")
				configuration[pair[0]] = pair[1]
	return configuration

# Entry point
def make_request(arguments):
	global app_domain
	global cloudhub_user
	global cloudhub_pass

	app_domain = arguments.get('app_name')
	cloudhub_user = arguments.get('cloudhub_user')
	cloudhub_pass = arguments.get('cloudhub_pass')
	# Tenant properties file
	file_path = arguments.get('file_path')
	configuration = propertiesParser(file_path)
	filename = re.search(regex_filename, file_path)
	tenant_id = filename.group(2)
	# CloudHub Operation
	update_tenant(tenant_id, configuration)
