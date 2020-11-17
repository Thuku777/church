from django.contrib import admin
from .models import *

# Register your models here.

class SlideAdmin(admin.ModelAdmin):
    list_display= ( 'image_preview', 'title', 'date_posted', 'is_published')
    list_filter =( 'title',)
    # prepopulated_fields = {"slug": ('title',)}
    list_editable = ('is_published',)
    list_per_page = 25

    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

admin.site.register(Slide, SlideAdmin)

admin.site.register(Contact)
