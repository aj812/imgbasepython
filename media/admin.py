from django.contrib import admin
from media.models import Media


class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "filename", "mediatype", "uri", "tags", "user", "date_created")
    list_filter = ("user", "tags", "date_created")


admin.site.register(Media, MediaAdmin)
