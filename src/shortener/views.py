from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import KirrURL
# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
  obj_url = None
  qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
  if qs.exists() and qs.count() == 1:
    obj = qs.first()
    obj_url = obj.url

  return HttpResponse("hello {sc}".format(sc=obj_url))

class KirrCBView(View):
  def get(self, request ,shortcode=None, *args, **kwargs): #class based view
    return HttpResponse("hello again {sc}".format(sc=shortcode))
    