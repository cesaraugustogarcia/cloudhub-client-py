import requests
import sys
import json
import pprint

baseurl = 'https://cloudhub.io/api/applications/'

# Parse file and build configurations map
def esta(file_path):
	configuration = {}
	with open(file_path, 'rb') as propertiesFile:
		i = iter(propertiesFile)
		for line in i:
			if ("=" in line) and ("#" not in line):
				pair = line.rstrip().split("=")
				configuration[pair[0]] = pair[1]
	return configuration


# Documentation: http://www.mulesoft.org/documentation/display/current/Get+Application
def make_request(baseurl, app_name, cloudhub_user, cloudhub_pass):

	#print baseurl + app_name

	response = requests.get(baseurl + app_name, auth=(cloudhub_user, cloudhub_pass))

	json_response = json.loads(response.text)

	pp = pprint.PrettyPrinter()

	def my_safe_repr(object, context, maxlevels, level):
		typ = pprint._type(object)
		if typ is unicode:
			object = str(object)
		return pprint._safe_repr(object, context, maxlevels, level)


	pp.format = my_safe_repr
	
	pp.pprint(json_response)

	
# Recieve from commandline parameters
if len(sys.argv)==4:
	app_name = sys.argv[1]
	cloudhub_user = sys.argv[2]
	cloudhub_pass =	sys.argv[3]
	make_request(baseurl, app_name, cloudhub_user, cloudhub_pass)
else:
	print "Missing parameters. Should be like 'python GetApplicationInfo.py applicationDomain accountUser accountPassword'"