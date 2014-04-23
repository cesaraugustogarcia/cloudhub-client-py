import sys
import importlib

methods = {"getApplicationInfo":"GetApplicationInfo", "getAllAplications":"GetAllApplications", "updateApplicationMetada":"UpdateApplicationMetadata", "deleteApplication":"DeleteApplication", "createApplication":"CreateApplication"}


if sys.argv[1] in methods.keys():
    module = importlib.import_module("." + methods.get(sys.argv[1]),"modules")
    module.make_request(sys.argv)
else:
    print "Not a valid method. Try one of "
    print methods.keys()

