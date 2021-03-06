import requests
import json
import sys
import os
import urllib.parse

sys.path.insert(1, './libs')
sys.path.insert(1, './responses')
import DataUtils
import ActivitiesResponses

AUTH_LIST_URI = "/v1/activity/history/list"
AUTH_LIST_REQ_TYPE = "POST"

def GET_LIST_BODY():
    b = json.dumps(
        {
        "sort":[
            {
            "field":"endDateTime",
            "direction":"desc"
            }
        ],
        "filter":{},
        "fields":[],
        "page":{
            "length":200,
            "offset":0
            }
        }
    )
    return b

def list(sessionname,CsvOutput):

    URL = urllib.parse.urljoin(DataUtils.GetUrl(sessionname), AUTH_LIST_URI)
    payload = GET_LIST_BODY()
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'X-Authorization': DataUtils.GetAuthToken(sessionname)
    }

    response = requests.request(AUTH_LIST_REQ_TYPE, URL, data=payload, headers=headers)
    isInError = ActivitiesResponses.Process_list_Response(response,CsvOutput)
