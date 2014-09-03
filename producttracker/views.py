from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from main.models import *
from main.utils import *
import datetime
import string

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")









