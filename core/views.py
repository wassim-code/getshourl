import random as r, string

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView
from django.http import JsonResponse

from .models import Url

class IndexView(View):
    def get(self, request):
        return render(request, 'core/index.html')
    
    def post(self, request):
        letters = string.ascii_letters + string.digits
        if request.POST['redirect_url'][:7] == 'http://' or request.POST['redirect_url'][:8] == 'https://':
            redirect_url = request.POST['redirect_url']
        else:
            redirect_url = f"https://{request.POST['redirect_url']}"
        try:
            url = Url.objects.create(
                url=''.join(r.choice(letters) for i in range(r.randint(5, 8))),
                redirect_url=redirect_url,
            )
        except:
            self.post(request)
        return JsonResponse({'url': url.url, 'original_url': url.redirect_url}, safe=False)

class UrlDetailView(DetailView):
    model = Url
    context_object_name = 'url'

def redirect_view(request, url):
    red_url = get_object_or_404(Url, url=url)
    red_url.total_clicks += 1
    red_url.save()
    return redirect(red_url.redirect_url)