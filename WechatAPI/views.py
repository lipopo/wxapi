# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
import hashlib

# Create your views here.
def AccessServer(request):
    if request.method == 'GET':
        echoStr = request.GET.get('echostr')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        signature = request.GET.get('signature')
        token = 'tttLZPppap'
        access = [nonce, token, timestamp]
        access.sort()
        linkStr = reduce(lambda x, y: x + y, access, '')
        hashCode = hashlib.sha1(linkStr).hexdigest()
        if hashCode == signature:
            return HttpResponse(echoStr)