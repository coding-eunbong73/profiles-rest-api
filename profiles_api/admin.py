from django.contrib import admin

#added 
from profiles_api import models

admin.site.register(models.UserProfile)
