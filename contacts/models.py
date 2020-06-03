from django.db import models
from listings.models import Listing


class Contact(models.Model):
    user_id: models.IntegerField()
    listing: models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    listing_id: models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    message: models.TextField(blank=True)
    contact_date: models.DateTimeField(datetime.now, blank=True)
