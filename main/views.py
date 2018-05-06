import json
import requests
from django.shortcuts import render


# Create your views here.

def coin_ids(request):
    response = requests.get('http://127.0.0.1:8888/coin_ids')
    _coin_ids = json.loads(response.content)
    th_list = ['coin_id']
    tr_list = [[coin_id] for coin_id in _coin_ids]
    context = {
        'th_list': th_list,
        'tr_list': tr_list,
    }
    return render(request, "main/display_coin_ids.html", context=context)
