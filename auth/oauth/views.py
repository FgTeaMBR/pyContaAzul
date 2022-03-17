import base64
import requests
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .utils import create_json_file
from . import constants


def authorize(request):
    url = f"https://api.contaazul.com/auth/authorize?redirect_uri={constants.REDIRECT_URI}&client_id={constants.CLIENT_ID}&scope=sales&state={constants.STATE}"
    return HttpResponseRedirect(url)

def get_token(request):
    code = request.GET.get("code")
    state = request.GET.get("state")
    
    if state != constants.STATE:
        return HttpResponse(status=401)
    
    client_credentials = f"{constants.CLIENT_ID}:{constants.CLIENT_SECRET}"
    credentials_bytes = client_credentials.encode("ascii")
    base64_bytes = base64.b64encode(credentials_bytes)
    base64_credentials = base64_bytes.decode("ascii")
    headers = {
        "Authorization": f"Basic {base64_credentials}"
    }
    url = f"https://api.contaazul.com/oauth2/token?grant_type=authorization_code&redirect_uri={constants.REDIRECT_URI}&code={code}"
    response = requests.post(url, headers=headers)
    create_json_file(json.loads(response.content))
    return HttpResponse(200)