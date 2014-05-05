import sys
import importlib
import argparse

from modules import GetApplicationInfo
from modules import GetAllApplications
from modules import GetNotifications

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

getNotifications_parser = subparsers.add_parser('gno', help='Get notifications for a CloudHub Application. Filters can be applied.')
getNotifications_parser.add_argument('-app_name',required=True)
getNotifications_parser.add_argument('-cloudhub_user',required=True)
getNotifications_parser.add_argument('-cloudhub_pass',required=True)
getNotifications_parser.add_argument('-tenant_id',required=False,default="")
getNotifications_parser.add_argument('-status',required=False,default="unread")
getNotifications_parser.add_argument('-priority',required=False,default="ERROR")
getNotifications_parser.add_argument('-message_filter',required=False,default="")
getNotifications_parser.add_argument('-output_format',required=False,default="CSV1")
getNotifications_parser.set_defaults(func=GetNotifications.make_request)

args = parser.parse_args()
args.func(vars(args))