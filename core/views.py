from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView
from django.http import JsonResponse

from .models import Url
from .utils import shorten_url, update_url_clicks_count

class IndexView(View):
    def get(self, request):
        return render(request, 'core/index.html')
    
    def post(self, request):
        url = shorten_url(request.POST['redirect_url'], with_password=request.POST.get('with_password'))
        return render(request, 'core/url_created.html', {'url': url})

class UrlDetailView(DetailView):
    model = Url
    context_object_name = 'url'

class RedirectView(View):
    def get(self, request, url_pk):
        url = get_object_or_404(Url, url=url_pk)
        if url.has_password():
            return render(request, 'core/url_redirect.html', {'url': url})
        red_url = update_url_clicks_count(url)
        return redirect(red_url.redirect_url)
    
    def post(self, request, url_pk):
        url = get_object_or_404(Url, url=url_pk)
        if url.password == request.POST['password']:
            red_url = update_url_clicks_count(url)
            return JsonResponse({'red_url': red_url.redirect_url})
        return JsonResponse({'error_msg': 'Incorrect Password.'})