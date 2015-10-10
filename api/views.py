from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse

from api.models import Product

from lxml import html
import requests
import json


# Create your views here.
@api_view(['GET'])
def get_product(request, ean_code):
    carritus_id = get_carritus_id(ean_code) # ean_code = 8480010055849
    prices_list = get_prices(carritus_id) #carritus_id = 53095890 

    return JsonResponse({'result': prices_list})
        

def get_carritus_id(ean_code):
    product = Product.objects.get(ean_code=ean_code)
    productX = Product.objects.filter(ean_code=ean_code)
    return product.carritus_id
       
        
def get_prices(product_id):
    
    page = requests.get('http://www.carritus.com/tienda/super/eroski/cp/08016/producto/%d' % int(product_id))
    tree = html.fromstring(page.text)

    empty = False
    index = 1
    prices_list = {}
    while empty == False:
        market = tree.xpath('//*[@id="tienda"]/div[1]/div[2]/div[3]/table/tbody/tr[%d]/td[1]/span/text()' % index)
        price = tree.xpath('//*[@id="tienda"]/div[1]/div[2]/div[3]/table/tbody/tr[%d]/td[2]/p/strong/text()' % index)
        if market:
            prices_list[market[0]] = price[0].split(' ')[0]
            index += 1
        else:
            empty = True
    return prices_list