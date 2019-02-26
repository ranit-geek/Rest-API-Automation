import requests
from ptest.plogger import preporter
import json


def get(url, headers={}):
    preporter.info("Getting url: " + url)
    return requests.get(url, headers=headers)


def post(url, request_json, headers={}):
    preporter.info("Post url : " + url)
    preporter.info("Request body : " + json.dumps(request_json))
    return requests.post(url, json=request_json, headers=headers)


def put(url, request_json, headers={}):
    preporter.info("Put url:" + url)
    preporter.info("Request body: " + json.dumps(request_json))
    return requests.put(url, json=request_json, headers=headers)


def delete(url, headers={}):
    preporter.info("Delete url :" + url)
    return requests.delete(url, headers=headers)
    1+4




