from django.contrib import admin
from media.models import Media


class MediaAdmin(admin.ModelAdmin):
    list_display = ("user", "mediatype", "path", "tags", "date_created")
    list_filter = ("tags", "date_created")


admin.site.register(Media, MediaAdmin)
