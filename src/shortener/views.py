from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL
# Create your views here.

class HomeView(View):
  def get(self, request, *args, **kwargs):
    the_form = SubmitUrlForm()
    context = {
      "title": "Submit URL",
      "form": the_form
    }
    return render(request, "shortener/home.html", context)

  def post(self, request, *args, **kwargs):
    form = SubmitUrlForm(request.POST)
    context = {
      "title": "Submit URL",
      "form": form
    }
    template = "shortener/home.html"
    if form.is_valid():
      print(form.cleaned_data)
      new_url = form.cleaned_data.get("url")
      obj, created = KirrURL.objects.get_or_create(url=new_url)
      new_context = {
        "obj": obj,
        "created": created
      }
      if created:
        template = "shortener/success.html"
      else:
        template = "shortener/already-exists.html"

    return render(request, template, new_context)


class KirrCBView(View):
  def get(self, request ,shortcode=None, *args, **kwargs): #class based view
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return  HttpResponseRedirect(obj.url)