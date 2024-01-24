from django.contrib import admin

# Register your models here.
from users.models import Profile, Skill

# class ProfileAdmin(admin.ModelAdmin):
#     # list_display = ("project", "body", "value")
#     pass

admin.site.register(Profile)
admin.site.register(Skill)