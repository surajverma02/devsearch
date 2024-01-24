from django.contrib import admin

# Register your models here.
from project.models import Project, Review, Tag

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("project", "body", "value")

admin.site.register(Project)
admin.site.register(Review, ReviewAdmin )
admin.site.register(Tag)