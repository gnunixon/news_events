from django.contrib import admin
from .models import Event


class EventChildInline(admin.TabularInline):
    model = Event.childrens.through
    fk_name = 'from_event'


class EventAdmin(admin.ModelAdmin):
    inlines = (EventChildInline,)
    extra = 3

admin.site.register(Event, EventAdmin)
