from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    # basically it says to Django : Choice Obj are edited on admin site, render 3 choices forms
    model = Choice
    extra = 3


# allowing in admin panel to edit/add question
class QuestionAdmin(admin.ModelAdmin):
    fieldssets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]

    # This line add info about polls: timestamp and if it was created recelny => bool
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # displaying deafult django filters for published date
    list_filter = ['pub_date']
    
    # added search form for better UX and faster and precise searching/filtering
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
