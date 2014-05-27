import requests
import json
import datetime

# Documentation: http://www.mulesoft.org/documentation/display/current/Notifications

# Constants
baseurl = 'https://cloudhub.io/api/applications/'
app_domain = ""
cloudhub_user = ""
cloudhub_pass = ""

# Cloudhub operations

# Get notifications
# Status: "read", "unread" or "all"
# Priority: "INFO", "WARN" or "ERROR"
def get_logs(tenant_id, start_date, end_date, priority, message_filter, output_format, cols, max_size):
	query_string  =  {
	    "limit": 10,
	    "offset": 0,
	    "startDate": start_date,
	    "endDate": end_date,
	    "priority": priority,
	    "tail": "false"
	}

	if (tenant_id != ""):
		query_string['tenantId'] = tenant_id

	page_counter = 0
	has_next = True

	# Automatic Pagination
	while (has_next):
		query_string["offset"] = (page_counter * query_string["limit"])
		response = requests.get(baseurl + app_domain + "/logs", params=query_string, auth=(cloudhub_user, cloudhub_pass))

		if response.status_code == 200:
			json_response = json.loads(response.text)
			filter_logs(json_response, message_filter, output_format, cols, max_size, page_counter)
			page_counter += 1 
			if (json_response["total"] < (page_counter * query_string["limit"])):
				has_next = False
		else:
			print "Error retrieving logs."
			has_next = False

		pass

# Utils
def filter_logs(json_response, message_filter, output_format, cols, max_size, page_counter):
	if output_format == "CSV":
		cols_list = cols.split(",")
		if page_counter == 0:
			print cols

		for line in json_response["data"]:
			# Line keys:
			# ['message', 'priority', 'sequenceNumber', 'timestamp']
			line_message = unicode(line["message"])
			time_stamp_api = str((line["timestamp"]))[:10]
			output_dict = {}
			output_dict["message"] = line_message[:int(max_size)].lstrip()
			output_dict["priority"] = line["priority"]
			output_dict["sequencenumber"] = line["sequenceNumber"]
			output_dict["timestamp"] = datetime.datetime.fromtimestamp(int(time_stamp_api)).strftime('%Y-%m-%d %H:%M:%S')

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
	start_date = arguments.get('start_date')
	end_date = arguments.get('end_date')
	priority = arguments.get('priority')
	message_filter = arguments.get('message_filter')
	output_format = arguments.get('output_format')
	cols = arguments.get('cols')
	max_size = arguments.get('max_size')

	get_logs(tenant_id, start_date, end_date, priority, message_filter, output_format, cols, max_size)
