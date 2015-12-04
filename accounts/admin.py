from django.contrib import admin
from accounts.models import softlayer_api
from accounts.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(softlayer_api)
