from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *


# Create your views here.
def index(request):
    template = loader.get_template('cv.html')
    context = {
        'person': Person.objects.first(),
        'experience': Experience.objects.all().order_by('-fromtime'),
        # 'keyskills': KeySkills.objects.all(),
        # 'education': Education.objects.all().order_by('-fromtime'),
    }
    return HttpResponse(template.render(context, request))
