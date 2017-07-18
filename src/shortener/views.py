from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import View

from analytics.models import ClickEvent
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
      new_url = form.cleaned_data.get("url")
      obj, created = KirrURL.objects.get_or_create(url=new_url)
      context = {
        "obj": obj,
        "created": created
      }
      if created:
        template = "shortener/success.html"
      else:
        template = "shortener/already-exists.html"

    return render(request, template, context)


class URLRedirectView(View):
  def get(self, request ,shortcode=None, *args, **kwargs): #class based view
    qs = KirrURL.objects.filter(shortcode=shortcode)
    if qs.count() != 1 and not qs.exists():
      raise Http404
    obj = qs.first()
    print(ClickEvent.objects.create_event(obj))
    return HttpResponseRedirect(obj.url)


