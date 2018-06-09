from models import AccessToken
from celery import shared_task
import requests

@shared_task
def refreshAccessToken():
    accessToken = requests.get('https://api.weixin.qq.com/cgi-bin/token',{'grant_type':'client_credential','appid':'wxf100e4f37dcc04b4','secret':'486bfdbf94451be7d98b24e9df12595a'}).json()
    if accessToken.has_key('access_token'):
        accessTokenToken = accessToken['access_token']
        access = AccessToken.objects.all()
        if len(access) == 0:
            AccessToken.objects.create(token=accessTokenToken)
        else:
            AccessToken.objects.first().update(token=accessTokenToken)