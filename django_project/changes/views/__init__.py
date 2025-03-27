
from changes.views.category import *
from changes.views.entry import *
from changes.views.version import *
from changes.views.changelog_github import *
from django.shortcuts import redirect

def redirect_root(request):
    return redirect('version-list')