# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy
from .forms import InputForm, inputfromuser

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
    print("bc")
    if req.method == 'POST':
        print ("coming in the post")
        form = inputfromuser(req.POST)
        if form.is_valid():
            print("form is valid")
            data = form.cleaned_data
            if data['user_input'] == "Homocide":
                form = inputfromuser()
                context = {'form': form}
                return render(req, "homicide.html", context)
            if data['user_input'] == "Caught Selling Drugs":
                form = inputfromuser()
                context = {'form': form}
                return render(req, "caughtsellingdrugs.html", context)
            if data['user_input'] == "Caught Selling Only Marijuana":
                form = inputfromuser()
                context = {'form': form}
                return render(req, "caughtsellingmarijuana.html", context)
    else:
        print("first time sex")
        form = inputfromuser()
        context = {'form': form}
        return render(req, "graphs.html", context)
