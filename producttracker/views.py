from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
import string

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")









