from django.db import models


class Subscribe(models.Model):

    NEWSLETTER_OPTION = [('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')]

    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    option = models.CharField(max_length=1, choices=NEWSLETTER_OPTION, default='M')
