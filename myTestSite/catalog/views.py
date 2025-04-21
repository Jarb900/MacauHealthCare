#from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

#def homePageView(request):
#    return HttpResponse('Welcome to the catalog')

class HomePageView(TemplateView):
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html'