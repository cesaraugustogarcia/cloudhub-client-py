import sys
import importlib
import argparse

from modules import GetApplicationInfo
from modules import GetAllApplications
from modules import DeployApplication
from modules import GetNotifications
from modules import GetSingleTenant
from modules import GetAllTenants
from modules import LoadTenant
from modules import DeleteTenant
from modules import UpdateTenant
from modules import UpdateTenantStatus

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',description='valid subcommands')

getApplicationInfo_parser = subparsers.add_parser('gai', help='Get Application Info method')
getApplicationInfo_parser.add_argument('-app_name',required=True)
getApplicationInfo_parser.add_argument('-cloudhub_user',required=True)
getApplicationInfo_parser.add_argument('-cloudhub_pass',required=True)
getApplicationInfo_parser.set_defaults(func=GetApplicationInfo.make_request)

getAllApplications_parser = subparsers.add_parser('gaa', help='Get All Applications method')
getAllApplications_parser.add_argument('-cloudhub_user',required=True)
getAllApplications_parser.add_argument('-cloudhub_pass',required=True)
getAllApplications_parser.set_defaults(func=GetAllApplications.make_request)

deployApplication_parser = subparsers.add_parser('dam', help='Get Application Info method')
deployApplication_parser.add_argument('-app_name',required=True)
deployApplication_parser.add_argument('-cloudhub_user',required=True)
deployApplication_parser.add_argument('-cloudhub_pass',required=True)
deployApplication_parser.add_argument('-file_path',required=True)
deployApplication_parser.set_defaults(func=DeployApplication.make_request)

getNotifications_parser = subparsers.add_parser('gno', help='Get notifications for a CloudHub Application. Filters can be applied.')
getNotifications_parser.add_argument('-app_name',required=True)
getNotifications_parser.add_argument('-cloudhub_user',required=True)
getNotifications_parser.add_argument('-cloudhub_pass',required=True)
getNotifications_parser.add_argument('-tenant_id',required=False,default="")
getNotifications_parser.add_argument('-status',required=False,default="unread",help="Filter notifications by status (unread -default-, read or all)")
getNotifications_parser.add_argument('-priority',required=False,default="ERROR",help="Filter notifications by priority (ERROR -default-, WARN or INFO)")
getNotifications_parser.add_argument('-message_filter',required=False,default="",help="Show notifications that match the string in message.")
getNotifications_parser.add_argument('-output_format',required=False,default="CSV1")
getNotifications_parser.set_defaults(func=GetNotifications.make_request)

getSingleTenant_parser = subparsers.add_parser('gst', help='Get tenant from a CloudHub Application and save its properties to a properties file.')
getSingleTenant_parser.add_argument('-app_name',required=True)
getSingleTenant_parser.add_argument('-cloudhub_user',required=True)
getSingleTenant_parser.add_argument('-cloudhub_pass',required=True)
getSingleTenant_parser.add_argument('-tenant_id',required=True)
getSingleTenant_parser.set_defaults(func=GetSingleTenant.make_request)

getAllTenants_parser = subparsers.add_parser('gat', help='Get all tenants from a CloudHub Application and save its properties to separate properties files.')
getAllTenants_parser.add_argument('-app_name',required=True)
getAllTenants_parser.add_argument('-cloudhub_user',required=True)
getAllTenants_parser.add_argument('-cloudhub_pass',required=True)
getAllTenants_parser.set_defaults(func=GetAllTenants.make_request)

loadTenant_parser = subparsers.add_parser('lte', help='Load tenant from a properties file to a CloudHub Application.')
loadTenant_parser.add_argument('-app_name',required=True)
loadTenant_parser.add_argument('-cloudhub_user',required=True)
loadTenant_parser.add_argument('-cloudhub_pass',required=True)
loadTenant_parser.add_argument('-tenant_name',required=True)
loadTenant_parser.add_argument('-tenant_email',required=True)
loadTenant_parser.add_argument('-file_path',required=True)
loadTenant_parser.set_defaults(func=LoadTenant.make_request)

deleteTenant_parser = subparsers.add_parser('dte', help='Delete tenant from a CloudHub Application.')
deleteTenant_parser.add_argument('-app_name',required=True)
deleteTenant_parser.add_argument('-cloudhub_user',required=True)
deleteTenant_parser.add_argument('-cloudhub_pass',required=True)
deleteTenant_parser.add_argument('-tenant_id',required=True)
deleteTenant_parser.set_defaults(func=DeleteTenant.make_request)

updateTenant_parser = subparsers.add_parser('ute', help='Update tenant properties in a CloudHub Application.')
updateTenant_parser.add_argument('-app_name',required=True)
updateTenant_parser.add_argument('-cloudhub_user',required=True)
updateTenant_parser.add_argument('-cloudhub_pass',required=True)
updateTenant_parser.add_argument('-file_path',required=True)
updateTenant_parser.set_defaults(func=UpdateTenant.make_request)

updateTenantStatus_parser = subparsers.add_parser('uts', help='Update tenant status in a CloudHub Application.')
updateTenantStatus_parser.add_argument('-app_name',required=True)
updateTenantStatus_parser.add_argument('-cloudhub_user',required=True)
updateTenantStatus_parser.add_argument('-cloudhub_pass',required=True)
updateTenantStatus_parser.add_argument('-tenant_id',required=True)
updateTenantStatus_parser.add_argument('-status',required=True,help="Tenant status to be set (enabled or disabled).")
updateTenantStatus_parser.set_defaults(func=UpdateTenantStatus.make_request)

args = parser.parse_args()
args.func(vars(args))