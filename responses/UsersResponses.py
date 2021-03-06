import requests
import json
import sys
import os

sys.path.insert(1, './libs')
sys.path.insert(1, './transformers')
import DataUtils
import UsersTransformers
import StdResponses

def Process_List_Response(res,CsvOutput):
    isError,isCsvOutput = StdResponses.ProcessStdResponse(res,CsvOutput)
    if(isError):
        exit(1)
    else:
        result = json.loads(res.text)
        if isCsvOutput:
            print(UsersTransformers.GetUserListAsCsv(result))
            exit(0)
        else:
            print(result)
            exit(0)

def Process_Set_Login_Response(res,CsvOutput):
    isError,isCsvOutput = StdResponses.ProcessStdResponse(res,CsvOutput)
    if(isError):
        exit(1)
    else:
        result = json.loads(res.text)
        if isCsvOutput:
            print(res.text)
            exit(0)
        else:
            print(result)
            exit(0)

def Process_Delete_Response(res,CsvOutput):
    isError,isCsvOutput = StdResponses.ProcessStdResponse(res,CsvOutput)
    if(isError):
        exit(1)
    else:
        result = json.loads(res.text)
        if isCsvOutput:
            print(res.text)
            exit(0)
        else:
            print(result)
            exit(0)

def Process_Create_Response(res,CsvOutput):
    isError,isCsvOutput = StdResponses.ProcessStdResponse(res,CsvOutput)
    if(isError):
        exit(1)
    else:
        result = json.loads(res.text)
        if isCsvOutput:
            print(print("user created with ID:"+str(result['id'])))
            exit(0)
        else:
            print(result)
            exit(0)
