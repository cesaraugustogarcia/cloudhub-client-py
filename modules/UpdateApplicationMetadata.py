import requests
import sys
import json
import pprint

# Parse file and build configurations map
def propertiesParser(file_path):
	configuration = {}
	with open(file_path, "rb") as propertiesFile:
		i = iter(propertiesFile)
		for line in i:
			if ("=" in line) and ("#" not in line):
				pair = line.rstrip().split("=")
				configuration[pair[0]] = pair[1]
	return {"properties" : configuration}


# Documentation: http://www.mulesoft.org/documentation/display/current/Update+Application+Metadata
def make_request(cloudhub_user, cloudhub_pass, app_name, propertiesFilePath):

	baseurl = "https://cloudhub.io/api/applications/"

	headers = {"content-type": "application/json"}

	body=propertiesParser(propertiesFilePath)

	response = requests.put(baseurl + app_name, data=json.dumps(body), auth=(cloudhub_user, cloudhub_pass), headers=headers)

	print response
	print response.text