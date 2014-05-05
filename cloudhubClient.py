import sys
import importlib
import argparse

from modules import GetApplicationInfo
from modules import GetAllApplications


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

args = parser.parse_args()
args.func(vars(args))