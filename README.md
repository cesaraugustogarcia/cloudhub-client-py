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
```
python cloudhubClient.py getApplicationInfo applicationDomain accountUser accountPassword
```

### Get All Applications <a name="getallapplications"/>

Doc: http://www.mulesoft.org/documentation/display/current/List+All+Applications

**Usage** 
```
python cloudhubClient.py getAllAplications accountUser accountPassword
```

### Update Application Metadata <a name="updateapplicationmetadata"/>

Doc: http://www.mulesoft.org/documentation/display/current/Update+Application+Metadata

**Usage** 
```
python cloudhubClient.py updateApplicationMetada accountUser accountPassword appDomain propertiesFilePath
```

This method expects a properties file like
```
#Endpoints configuration
propertyname.a=propertya
propertyname.b=propertyb
```


## Requirements <a name="requirements"/>

### Python requests module

How to install Docs: http://docs.python-requests.org/en/latest/user/install/
