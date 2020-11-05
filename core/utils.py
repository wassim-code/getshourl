import random as r, string

from django.shortcuts import get_object_or_404

from .models import Url

def shorten_url(url, with_password=False):
    redirect_url = f"https://{url}"
    if url[:7] == 'http://' or url[:8] == 'https://':
        redirect_url = url
    try:
        url_obj = Url.objects.create(
            url=get_rand_str(5, 8),
            redirect_url=redirect_url,
            password=get_rand_str(14, 18) if with_password else None,
        )
    except:
        url_obj = shorten_url(url)
    return url_obj

def update_url_clicks_count(url):
    url.total_clicks += 1
    url.save()
    return url

def get_rand_str(r1, r2):
    letters = string.ascii_letters + string.digits
    rand_str = ''.join(r.choice(letters) for i in range(r.randint(r1, r2)))
    return rand_str
