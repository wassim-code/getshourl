import random as r, string

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import JsonResponse

from .models import Url

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        letters = string.ascii_letters + string.digits
        if request.POST['redirect_url'][:8] != 'https://':
            redirect_url = f"https://{request.POST['redirect_url']}"
        else:
            redirect_url = request.POST['redirect_url']
        try:
            url = Url.objects.create(
                url=''.join(r.choice(letters) for i in range(r.randint(5, 8))),
                redirect_url=redirect_url,
            )
        except:
            self.post(request)
        return JsonResponse({'url': url.url, 'original_url': url.redirect_url}, safe=False)

def redirect_view(request, url):
    redirect_url = get_object_or_404(Url, url=url)
    redirect_url.visits += 1
    redirect_url.save()
    return redirect(redirect_url.redirect_url)