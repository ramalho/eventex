from django.contrib import admin
from core.models import Speaker, Talk, Course, Contact, Media

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInline, ]
    prepopulated_fields = {'slug': ('name', )}


class MediaInline(admin.TabularInline):
    model = Media
    extra = 1

class TalkAdmin(admin.ModelAdmin):
    inlines = [MediaInline, ]


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Course)
admin.site.register(Media)
