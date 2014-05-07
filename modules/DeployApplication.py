import requests

def make_request(arguments):
	app_name = arguments.get('app_name')
	cloudhub_user = arguments.get('cloudhub_user')
	cloudhub_pass = arguments.get('cloudhub_pass')
	file_path = arguments.get('file_path')

	base_url = "https://cloudhub.io/api/applications/"
	headers = {"content-type": "application/octet-stream"}

	with open(file_path) as f:
		response = requests.post(base_url + app_name + "/deploy", data=f, auth=(cloudhub_user, cloudhub_pass), headers=headers, stream=True)

	print response.request.headers        