# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    return render(request,'test.html', {'date': datetime.now()})


# Create your views here.
