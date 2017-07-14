from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL
# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
  
  obj = get_object_or_404(KirrURL, shortcode=shortcode)
  
  # NOTES
  
  # obj_url = obj.url
  # obj_url = None
  # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
  # if qs.exists() and qs.count() == 1:
  #   obj = qs.first()
  #   obj_url = obj.url

  return HttpResponse("hello {sc}".format(sc=obj.url))

class KirrCBView(View):
  def get(self, request ,shortcode=None, *args, **kwargs): #class based view
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponse("hello again {sc}".format(sc=shortcode))
    