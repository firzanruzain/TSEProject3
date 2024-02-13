"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
#sharing entity


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    # Add any other fields relevant to owners

    def __str__(self):
        return self.user.username
    
class Searcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='searcher')

    def __str__(self):
        return self.user.username

class ShortlistedProperty(models.Model):
    searcher = models.ForeignKey(Searcher, on_delete=models.CASCADE, related_name='shortlisted_properties')
    property = models.ForeignKey('Property', on_delete=models.CASCADE)  # Assuming you have a Property model

class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100, default="Unknown")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bedrooms = models.PositiveIntegerField(default=1)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)  # ForeignKey to the Owner model, allowing null values

    def __str__(self):
        return self.title

class PropertyPicture(models.Model):
    property = models.ForeignKey(Property, related_name='pictures', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='property_pictures/')

    def __str__(self):
        return f"Picture of {self.property.title}"

class ApplicationRequest(models.Model):
    searcher = models.ForeignKey(Searcher, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    status_choices = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=status_choices, default='Pending')

class InAppMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


