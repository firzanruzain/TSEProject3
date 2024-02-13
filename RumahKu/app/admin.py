from django.contrib import admin
from app.models import Property, Owner, Searcher, ShortlistedProperty, PropertyPicture, Tenant, Tenancy

admin.site.register(Property)
admin.site.register(Owner)
admin.site.register(Searcher)
admin.site.register(ShortlistedProperty)
admin.site.register(PropertyPicture)
admin.site.register(Tenant)
admin.site.register(Tenancy)