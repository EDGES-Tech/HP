from __future__ import unicode_literals
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect

def member(request):
    d = {
        'message': 'Sample message',
    }
    return render(request, 'member/index.html', d)
    