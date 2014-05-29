import requests
import json

def make_request(arguments):
	app_name = arguments.get('app_name')
	cloudhub_user = arguments.get('cloudhub_user')
	cloudhub_pass = arguments.get('cloudhub_pass')
	file_path = arguments.get('file_path')

	base_url = "https://cloudhub.io/api/applications/"

	files = {'file': open(file_path, 'rb')}

	response = requests.get(base_url + app_name, auth=(cloudhub_user, cloudhub_pass))

	if (response.status_code == 200):
		json_response = json.loads(response.text)

		form_data = {
			"muleVersion": json_response["muleVersion"],
			"workerType": json_response["workerType"],
			"workers": str(json_response["workers"])
		}

		app_properties = (json_response["properties"])
		
		for app_property in app_properties:
			form_data["properties." + app_property] = app_properties[app_property]

		response = requests.put(base_url + app_name, data=form_data, files=files, auth=(cloudhub_user, cloudhub_pass))

		if response.status_code == 200:
			print "Application deploy was accepted."
		else:
			print "Application deploy was rejected with HTTP error: " + str(response.status_code)
	else:
		print "There was an error while retrieving application info from CloudHub."