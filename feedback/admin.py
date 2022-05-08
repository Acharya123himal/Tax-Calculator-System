from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["sender","email","message","tel","date_sent"]

    search_fields = ["email"]

    list_filter = ["date_sent"]

    class Meta:
        model = Feedback