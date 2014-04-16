# Python Client for Cloudhub API

API Documentation: http://www.mulesoft.org/documentation/display/current/API

+ [Methods](#getapplicationinfo)
    * [Get Application Info](#getapplicationinfo)
    * [Get All Applications](#getallapplications)
    * [Update Application Metadata](#updateapplicationmetadata)
+ [Requirements](#requirements)

### Get Application Info <a name="getapplicationinfo"/>

Doc: http://www.mulesoft.org/documentation/display/current/Get+Application

**Usage** 
Lets say we want to get the belonging information for an app that placed in *https://fandermole.cloudhub.io/*. Then I should run the following command:
```
python cloudhubClient.py getApplicationInfo fandermole cloudhubUser cloudhubPassword
```

### Get All Applications <a name="getallapplications"/>

Doc: http://www.mulesoft.org/documentation/display/current/List+All+Applications

**Usage** 
```
python cloudhubClient.py getAllAplications cloudhubUser cloudhubPassword
```

### Update Application Metadata <a name="updateapplicationmetadata"/>

Doc: http://www.mulesoft.org/documentation/display/current/Update+Application+Metadata

**Usage** 
Lets now figure out we want to update the properties for an app that is placed in ```https://fandermole.cloudhub.io/```. Then I should run the following command:
```
python cloudhubClient.py updateApplicationMetada cloudhubUser cloudhubPassword fandermole propertiesFilePath
```

This method expects a properties file that should look like the following example:
```
#Endpoints configuration
propertyname.a=propertya
propertyname.b=propertyb
```


## Requirements <a name="requirements"/>

### Python requests module

How to install Docs: http://docs.python-requests.org/en/latest/user/install/  

Take into account that you may need to excecute the instalation using admin permissions; otherwise you could receive the following error message:
```
[Errno 13] Permission denied: '/Library/Python/2.7/site-packages/test-easy-install-2478.write-test'
```
