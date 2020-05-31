from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import bedroom_choices, state_choices, price_choices


def index(request):
    if request.method == 'GET':
        listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

        context = {
            'listings': listings,
            'bedroom_choices': bedroom_choices,
            'state_choices': state_choices,
            'price_choices': price_choices
            }

        return render(request, 'pages/index.html', context)
        
def about(request):
    realtors = Realtor.objects.order_by('id')
    photos = {'realtors': realtors}
    return render(request, 'pages/about.html', photos)
