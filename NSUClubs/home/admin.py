from django.contrib import admin

from home.models import Club, User,Event,ClubMember

# Register your models here.

admin.site.register(Club)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(ClubMember)