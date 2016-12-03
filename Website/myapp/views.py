# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy


def index(req):
    return HttpResponse("Hi there! You have reached the index page. Try to find our awesome website. Specify url with home, dataset, regression or graphs.")

def home(req):

  return render(req, "home.html")

def dataset(req):

   import pandas as pd
   from os.path import join
   from django.conf import settings

   filename = join(settings.STATIC_ROOT, 'myapp/table.csv')

   df = pd.read_csv(filename)

   table = df.to_html()

   return render(req, "dataset.html", {"html_table" : table})

def regressions(req):

   return render(req, "regressions.html")

def graphs(req):

  return render(req, "graphs.html")
