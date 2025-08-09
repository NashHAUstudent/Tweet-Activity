from django.contrib import admin
from .models import Tweet


# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin panel for the Tweet model.
    This version includes fieldsets and filters for a more powerful admin view.
    """
    # This list controls which fields are displayed in the list view of the admin site.
    list_display = ('text', 'created_at', 'image')

    # This adds a search bar to the admin list view, allowing you to search by tweet text.
    search_fields = ('text',)

    # This adds a filter sidebar to the admin list view, allowing you to filter by date.
    list_filter = ('created_at',)

    # This uses a fieldset to group the input fields on the tweet's detail page.
    fieldsets = (
        (None, {
            'fields': ('text', 'image')
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',),  # This makes the section collapsible
        }),
    )

    # This makes the 'created_at' field read-only, as it's set automatically.
    readonly_fields = ('created_at',)
