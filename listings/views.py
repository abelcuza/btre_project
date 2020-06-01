from django.shortcuts import render, get_object_or_404
from .models import Listing
from realtors.models import Realtor
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .choices import price_choices, state_choices, bedroom_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    if request.method == 'GET':
        listing = get_object_or_404(Listing, pk=listing_id)
        realtor = Realtor.objects.get(name=listing.realtor)
        context = {'listing': listing, 'realtor': realtor}
        return render(request, 'listings/listing.html', context)

    elif request.method == 'POST':
        property = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')


def search(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET.get('state')
        if state:
            listings = listings.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)

    # Max Price
    if 'price' in request.GET:
        price = request.GET.get('price')
        if price:
            listings = listings.filter(price__lte=price)

    context = {'listings': listings,
               'state_choices': state_choices,
               'bedroom_choices': bedroom_choices,
               'price_choices': price_choices,
               'values': request.GET
               }

    print(context)

    return render(request, 'listings/search.html', context)
