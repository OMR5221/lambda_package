import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    server_name = os.environ.get("SERVER_NAME")
    tag_name = os.environ.get("TAG_NAME")
    timestamp = os.environ.get("TIMESTAMP")

    # make sure what_to_print and how_many_times values exist
    if server_name and tag_name and timestamp:
        url="http://dummy-api.source.asmx"
        #headers = {'content-type': 'application/soap+xml'}
        headers = {'content-type': 'text/xml'}
        body = """<?xml version="1.0" encoding="utf-8"?>
                 <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:fpl="http://API.COM/">
                    <soapenv:Header/>
                       <soapenv:Body>
                         <fpl:GetArchiveValue>
                             <!--Optional:-->
                             <fpl:sServerName>{ServerName}</fpl:sServerName>
                             <!--Optional:-->
                             <fpl:sPointName>{TagName}</fpl:sPointName>
                             <!--Optional:YYYY-MM-DD-->
                             <fpl:sTimeStamp>{Timestamp}</fpl:sTimeStamp>
                          </fpl:GetArchiveValue>
                   </soapenv:Body>
                </soapenv:Envelope>""".format(ServerName=server_name, TagName=tag_name, Timestamp=timestamp)
        response = requests.post(url,data=body,headers=headers)
        xml = response.content
        soup = BeautifulSoup(xml, 'lxml')
        print(soup)
        return soup

    ## uLTIMATELY WANT SCRIPT TO USE BOTOT3 TO CREATE A NEW LAMABDA FOR EACH  PROCESS:

    return None
