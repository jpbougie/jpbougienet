from blog.models import Entry
from django.shortcuts import render_to_response


def index(request):
    entry = Entry.published.latest()
    return render_to_response('index.html', {'entry': entry})