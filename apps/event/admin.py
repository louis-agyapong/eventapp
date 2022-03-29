from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    search_fields = ("title", "organizer", "type", "category", "location", "venue")
    list_display = ("title", "organizer", "type", "category", "location", "venue")
    ordering = ("title",)



admin.site.register(Event, EventAdmin)
