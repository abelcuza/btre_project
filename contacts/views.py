from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if user_id != 0:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)

        new_contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                              message=message, user_id=user_id)
        new_contact.save()
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info'
            'admin@example.com'
            [realtor_email],
            fail_silently=False,)
        messages.success(request, 'Your request has been submited, a realtor will get back to you sonn')
        return redirect('/listings/' + listing_id)
