import sys
from modules import GetApplicationInfo

# Recieve from commandline parameters
if sys.argv[1]=='getApplicationInfo':
	if len(sys.argv)==5:
		app_name = sys.argv[2]
		cloudhub_user = sys.argv[3]
		cloudhub_pass =	sys.argv[4]
		GetApplicationInfo.make_request(app_name, cloudhub_user, cloudhub_pass)
	else:
		print "Missing parameters. Should be like 'python cloudhubClient.py getApplicationInfo applicationDomain accountUser accountPassword'"
else:
	print "No valid module was invoked. Modules available: getApplicationInfo."