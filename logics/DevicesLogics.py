import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import DevicesResponses

DEVICE_LIST_URI = "/v2/devices/list"
DEVICE_LIST_REQ_TYPE = "POST"

def GET_LIST_BODY():
    b = json.dumps(
        {"sort":
            [
                {"field":"updatedOn",
                "direction":"desc"}
            ],
            "filter":{},
            "fields":[],
            "page":{"length":200,"offset":0}
        }
    )
    return b

def list(sessionname,CsvOutput):
    URL = urllib.parse.urljoin(DataUtils.GetUrl(sessionname), DEVICE_LIST_URI)

    payload = GET_LIST_BODY()
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'X-Authorization': DataUtils.GetAuthToken(sessionname)
    }

    response = requests.request(DEVICE_LIST_REQ_TYPE, URL, data=payload, headers=headers)
    isInError = DevicesResponses.Process_list_Response(response,CsvOutput)
