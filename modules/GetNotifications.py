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
def get_notifications(tenant_id, status, priority, message_filter, output_format, cols, max_size):
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

		filter_notifications(json_response, priority, message_filter, output_format, cols, max_size, page_counter)
		
		page_counter += 1 
		if (json_response["total"] < (page_counter * query_string["limit"])):
			has_next = False

		pass

# Utils
def filter_notifications(json_response, priority, message_filter, output_format, cols, max_size, page_counter):
	if output_format == "CSV":
		cols_list = cols.split(",")
		if page_counter == 0:
			print cols

		for line in json_response["data"]:
			# Line keys:
			# ['domain', 'transactionId', 'read', 'properties', 'priority', 'href', 'customProperties', 'message', 'tenantId', 'id', 'createdAt']
			line_message = unicode(line["message"])
			#time_stamp_api = str((line["timestamp"]))[:10]
			output_dict = {}
			output_dict["domain"] = line["domain"]
			output_dict["transactionid"] = line["transactionId"]
			output_dict["read"] = unicode(line["read"])
			output_dict["priority"] = line["priority"]
			output_dict["href"] = line["href"]
			output_dict["message"] = line_message[:int(max_size)].lstrip()
			if "tenantId" in line.keys():
				output_dict["tenantid"] = line["tenantId"]
			output_dict["id"] = line["id"]
			output_dict["createdat"] = line["createdAt"]

			# output_dict["timestamp"] = datetime.datetime.fromtimestamp(int(time_stamp_api)).strftime('%Y-%m-%d %H:%M:%S')

			if message_filter in line_message:
				output_line = ""
				for col in cols_list:
					output_line += output_dict[col.lower()]
					if col != cols_list[-1]:
						output_line += ","
				print output_line

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
	cols = arguments.get('cols')
	max_size = arguments.get('max_size')

	get_notifications(tenant_id, status, priority, message_filter, output_format, cols, max_size)
