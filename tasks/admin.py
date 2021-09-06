from django.contrib import admin

from .models import Task, documents_links,video_links


class ChoiceInline(admin.TabularInline):
    # basically it says to Django : Choice Obj are edited on admin site, render 3 choices forms
    model = documents_links
    extra = 3

class VideoInline(admin.TabularInline):
    model=video_links
    extra=3

# allowing in admin panel to edit/add question
class TaskAdmin(admin.ModelAdmin):
    fieldssets = [
        (None, {'fields': ['task_text']}),
        ('Date information', {'fields': [
            'pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline,VideoInline]

    # This line add info about polls: timestamp and if it was created recelny => bool
    list_display = ('task_text', 'pub_date')

    # displaying deafult django filters for published date
    list_filter = ['pub_date']

    # added search form for better UX and faster and precise searching/filtering
    search_fields = ['task_text']


admin.site.register(Task, TaskAdmin)

