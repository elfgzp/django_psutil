# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from .psutil_get_server_info import get_server_info


# Create your views here.
def server_info_api(request):
    try:
        server_info = get_server_info()
    except Exception as e:
        print(e)
    else:
        return HttpResponse(json.dumps(server_info))


@staff_member_required
def server(request):
    try:
        context = {
            'title': u'服务器监控',
        }
    except Exception as e:
        print(e)
    else:
        return render_to_response('server.html', context)
