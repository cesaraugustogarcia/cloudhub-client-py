import sys
import importlib
import argparse

from modules import GetApplicationInfo
from modules import GetAllApplications
from modules import DeployApplication
from modules import CreateApplication
from modules import DeleteApplication
from modules import UpdateApplicationMetadata
from modules import GetNotifications
from modules import GetSingleTenant
from modules import GetAllTenants
from modules import LoadTenant
from modules import DeleteTenant
from modules import UpdateTenant
from modules import UpdateTenantStatus
from modules import GetLogs

parser = argparse.ArgumentParser(epilog="More info on each subcommand try: 'python cloudhubClient.py {subcommand} -h'")
subparsers = parser.add_subparsers(title='subcommands')

credentials_parser = argparse.ArgumentParser(add_help=False)
credentials_parser.add_argument('-cu','--cloudhub-user',metavar='USERNAME',dest='cloudhub_user',required=True)
credentials_parser.add_argument('-cp','--cloudhub-pass',metavar='PASSWORD',dest='cloudhub_pass',required=True)
credentials_parser.add_argument('-an','--app-name',metavar='APP_NAME',dest='app_name',required=True)

getAllApplications_parser = subparsers.add_parser('gaa', help='Get All Applications', description='The GET operation specified with the /api/applications resource returns a list of all applications for your account. The resulting JSON contains a list of application objects.')
getAllApplications_parser.add_argument('-cu','--cloudhub-user',metavar='cloudhub_user',dest='cloudhub_user',required=True)
getAllApplications_parser.add_argument('-cp','--cloudhub-pass',metavar='cloudhub_pass',dest='cloudhub_pass',required=True)
getAllApplications_parser.set_defaults(func=GetAllApplications.make_request)

getApplicationInfo_parser = subparsers.add_parser('gai', help='Get Application Info',parents=[credentials_parser], description='The GET operation specified with the /api/applications/{domain} resource retrieves an application, where {domain} is the application domain.')
getApplicationInfo_parser.set_defaults(func=GetApplicationInfo.make_request)

updateApplicationMetaData_parser = subparsers.add_parser('uam', help='Update Application metadata',parents=[credentials_parser], description='The PUT method, specified with the /api/applications/{domain} resource (where {domain} is the application domain), updates your application metadata, including the number of workers and system properties. You can also use it to update an existing application. For information on how to update you application, see Updating Your Application. The update operation can update the workers, properties, muleVersion and filename properties. Properties which are not specified will not be updated.')
updateApplicationMetaData_parser.add_argument('--properties_path',required=True)
updateApplicationMetaData_parser.set_defaults(func=UpdateApplicationMetadata.make_request)

creteApplication_parser = subparsers.add_parser('cap', help='Create Application',parents=[credentials_parser], description='The POST operation specified with the /api/applications resource creates a new CloudHub application.')
creteApplication_parser.add_argument('--properties_path',required=True)
creteApplication_parser.add_argument('--mule_version',required=True)
creteApplication_parser.set_defaults(func=CreateApplication.make_request)

deleteApplication_parser = subparsers.add_parser('dea', help='Delete Application',parents=[credentials_parser], description='The DELETE operation, specified with the /api/applications/{domain} (where {domain} is the application domain), deletes the specified application.')
deleteApplication_parser.set_defaults(func=DeleteApplication.make_request)

deployApplication_parser = subparsers.add_parser('dap', help='Deploy Application',parents=[credentials_parser], description='The POST method, specified with the /api/applications/{domain}/deploy resource (where {domain} is the application domain), allows you to deploy a Mule application zip file to CloudHub. This is commonly done after you have created the application in Mule Studio or using Maven from the command line- then you need to upload the actual zip file to CloudHub. After you have deployed the zip file, you can monitor the status of your deployment by viewing the logs.')
deployApplication_parser.add_argument('--file_path',required=True)
deployApplication_parser.set_defaults(func=DeployApplication.make_request)

getNotifications_parser = subparsers.add_parser('gno', help='Get notifications for a CloudHub Application. Filters can be applied.',parents=[credentials_parser])
getNotifications_parser.add_argument('-t','--tenant-id',dest='tenant_id',required=False,default="",help="Get notifications from a specific tenant.")
getNotifications_parser.add_argument('-s','--status',dest='status',required=False,default="unread",help="Filter notifications by status (unread -default-, read or all)")
getNotifications_parser.add_argument('-p','--priority',dest='priority',required=False,default="ERROR",help="Filter notifications by priority (ERROR -default-, WARN or INFO)")
getNotifications_parser.add_argument('-m','--message-filter',dest='message_filter',required=False,default="",help="Show notifications that match the string in message.")
getNotifications_parser.add_argument('-c','--columns',dest='cols',metavar='COL1,COL2',required=False,default="createdAt,message",help="Columns to include in output file. Values are: domain, transactionId, read, priority, href, message, tenantId, id, createdAt")
getNotifications_parser.add_argument('-ms','--max-size',dest='max_size',required=False,default="512",help="Crop messages size. Default is 512 chars.")
getNotifications_parser.add_argument('-o','--output-format',dest='output_format',required=False,default="CSV",help="Output file format.")
getNotifications_parser.set_defaults(func=GetNotifications.make_request)

getSingleTenant_parser = subparsers.add_parser('gst', help='Get tenant from a CloudHub Application and save its properties to a properties file.',parents=[credentials_parser])
getSingleTenant_parser.add_argument('-t','--tenant-id',dest='tenant_id',required=True)
getSingleTenant_parser.set_defaults(func=GetSingleTenant.make_request)

getAllTenants_parser = subparsers.add_parser('gat', help='Get all tenants from a CloudHub Application and save its properties to separate properties files.',parents=[credentials_parser])
getAllTenants_parser.set_defaults(func=GetAllTenants.make_request)

loadTenant_parser = subparsers.add_parser('lte', help='Load tenant from a properties file to a CloudHub Application.',parents=[credentials_parser])
loadTenant_parser.add_argument('-tn','--tenant-name',dest='tenant_name',required=True)
loadTenant_parser.add_argument('-te','--tenant-email',dest='tenant_email',required=True)
loadTenant_parser.add_argument('-f','--file-path',dest='file_path',required=True)
loadTenant_parser.set_defaults(func=LoadTenant.make_request)

deleteTenant_parser = subparsers.add_parser('dte', help='Delete tenant from a CloudHub Application.',parents=[credentials_parser])
deleteTenant_parser.add_argument('-t','--tenant-id',dest='tenant_id',required=True)
deleteTenant_parser.set_defaults(func=DeleteTenant.make_request)

updateTenant_parser = subparsers.add_parser('ute', help='Update tenant properties in a CloudHub Application.',parents=[credentials_parser])
updateTenant_parser.add_argument('-f','--file-path',dest='file_path',required=True)
updateTenant_parser.set_defaults(func=UpdateTenant.make_request)

updateTenantStatus_parser = subparsers.add_parser('uts', help='Update tenant status in a CloudHub Application.',parents=[credentials_parser])
updateTenantStatus_parser.add_argument('-t','--tenant-id',dest='tenant_id',required=True)
updateTenantStatus_parser.add_argument('-s','--status',dest='status',required=True,help="Tenant status to be set (enabled or disabled).")
updateTenantStatus_parser.set_defaults(func=UpdateTenantStatus.make_request)

getLogs_parser = subparsers.add_parser('glo', help='Get logs for a CloudHub Application. Filters can be applied.',parents=[credentials_parser])
getLogs_parser.add_argument('-t','--tenant-id',dest='tenant_id',required=False,default="",help="Get logs from a specific tenant.")
getLogs_parser.add_argument('-s','--start-date',dest='start_date',required=True,help="Enter date in this format: YYYY-mm-ddT00:00:00.000Z. Also NOW, LAST_HOUR, TODAY, YESTERDAY, LAST_WEEK and LAST_MONTH are supported.")
getLogs_parser.add_argument('-e','--end-date',dest='end_date',required=True,help="Enter date in this format: YYYY-mm-ddT00:00:00.000Z. Also NOW, LAST_HOUR, TODAY, YESTERDAY, LAST_WEEK and LAST_MONTH are supported.")
getLogs_parser.add_argument('-p','--priority',dest='priority',required=False,default="INFO",help="The log level priority to return. Values are: DEBUG, INFO, WARN, ERROR, SYSTEM, CONSOLE.")
getLogs_parser.add_argument('-m','--message-filter',dest='message_filter',required=False,default="",help="Include only messages containing the specified string.")
getLogs_parser.add_argument('-o','--output-format',dest='output_format',required=False,default="CSV",help="Output file format.")
getLogs_parser.add_argument('-c','--columns',dest='cols',metavar='COL1,COL2',required=False,default="timestamp,message",help="Columns to include in output file. Values are: message, priority, sequenceNumber, timestamp")
getLogs_parser.add_argument('-ms','--max-size',dest='max_size',required=False,default="512",help="Crop messages size. Default is 512 chars.")
getLogs_parser.set_defaults(func=GetLogs.make_request)

args = parser.parse_args()
args.func(vars(args))