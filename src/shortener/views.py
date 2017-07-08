from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def kirr_redirect_view(request, *args, **kwargs): #function based view
  return HttpResponse("hello")

class KirrCBView(View):
  def get(self, reques, *args, **kwargs): #class based view
    return HttpResponse("hello again")