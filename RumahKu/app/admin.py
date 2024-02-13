from django.contrib import admin
from app.models import Property, Owner, Searcher, ShortlistedProperty, PropertyPicture

admin.site.register(Property)
admin.site.register(Owner)
admin.site.register(Searcher)
admin.site.register(ShortlistedProperty)
admin.site.register(PropertyPicture)