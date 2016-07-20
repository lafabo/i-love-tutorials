from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blog.models import Post
from .models import *
from .forms import FeedbackForm


# Create your views here.
def index(request):
    template = loader.get_template('cv.html')
    # form = FeedbackForm()
    context = {
        'person': Person.objects.first(),
        'experience': Experience.objects.all().order_by('-fromtime'),
        'keyskills': KeySkills.objects.all(),
        'education': Education.objects.all().order_by('-fromtime'),
        'bloglast6':  Post.objects.all().order_by('-published_date')[:6],
        'feedback': FeedbackForm,
    }
    return HttpResponse(template.render(context, request))