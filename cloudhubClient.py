import sys
from modules import GetApplicationInfo
from modules import GetAllApplications

# Recieve from commandline parameters
if sys.argv[1]=='getApplicationInfo':
	if len(sys.argv)==5:
		app_name = sys.argv[2]
		cloudhub_user = sys.argv[3]
		cloudhub_pass =	sys.argv[4]
		GetApplicationInfo.make_request(app_name, cloudhub_user, cloudhub_pass)
	else:
		print "Missing parameters. Should be like 'python cloudhubClient.py getApplicationInfo applicationDomain accountUser accountPassword'"

if sys.argv[1]=='getAllAplications':
	if len(sys.argv)==4:
		cloudhub_user = sys.argv[2]
		cloudhub_pass =	sys.argv[3]
		GetAllApplications.make_request(cloudhub_user, cloudhub_pass)
	else:
		print "Missing parameters. Should be like 'python cloudhubClient.py getAllAplications accountUser accountPassword'"