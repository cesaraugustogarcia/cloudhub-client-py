import requests
import json

# Documentation: http://www.mulesoft.org/documentation/display/current/Notifications

# Constants
baseurl = 'https://cloudhub.io/api/applications/'
headers = {'content-type': 'application/json'}
app_domain = ""
cloudhub_user = ""
cloudhub_pass = ""

# Cloudhub operations

# Get notifications
# Status: "read", "unread" or "all"
# Priority: "INFO", "WARN" or "ERROR"
def get_notifications(tenant_id, status, priority, message_filter, output_format):
	query_string  =  {
	      "status": status,
	      "limit": 10,
	      "offset": 0
	}

	if (tenant_id != ""):
		query_string['tenantId'] = tenant_id

	page_counter = 0
	has_next = True

	# Automatic Pagination
	while (has_next):
		query_string["offset"] = (page_counter * query_string["limit"])
		response = requests.get(baseurl + app_domain + "/notifications", params=query_string, headers=headers, auth=(cloudhub_user, cloudhub_pass))
		json_response = json.loads(response.text)

		filter_notifications(json_response, priority, message_filter, output_format, page_counter)
		
		page_counter += 1 
		if (json_response["total"] < (page_counter * query_string["limit"])):
			has_next = False

		pass

# Utils
def filter_notifications(json_response, priority, message_filter, output_format, page_counter):
	if output_format == "CSV1":
		if page_counter == 0:
			print "createdAt,message"
		for line in json_response["data"]:
			# Line keys:
			# ['domain', 'transactionId', 'read', 'properties', 'priority', 'href', 'customProperties', 'message', 'tenantId', 'id', 'createdAt']
			if line["priority"] == priority:
				line_message = line["message"]
				if message_filter in line_message:
					print str(line["createdAt"]) + "," + line["tenantId"] + "," + unicode(line_message)

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
	priority = arguments.get('priority')
	message_filter = arguments.get('message_filter')
	output_format = arguments.get('output_format')

	get_notifications(tenant_id, status, priority, message_filter, output_format)
