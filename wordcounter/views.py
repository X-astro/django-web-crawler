from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup

import requests
import operator

from collections import Counter
from string import punctuation
from .forms import *


def index(request):
    form = inputForm()
    if request.method == "POST":
        url = request.POST.get('url')
        if Mail.objects.filter(url=url):
            query = Mail.objects.get(url=url)
            most_common = query.words
            context = {'words': query.words, 'url': url}
            return render(request, 'send.html', context)
        else:
            r = requests.get(url)
            soup = BeautifulSoup(r.content)
            text = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
            c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
            most_common = c.most_common()
            Mail.objects.create(url=url, words=most_common)
            context = {'words': most_common, 'url': url}
            return render(request, 'send.html', context)
    context = {'form': form}
    return render(request, 'home.html', context)