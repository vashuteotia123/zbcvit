from django.contrib import admin
from import_export.admin import  ImportExportModelAdmin
from app1.models import User,Event,Notification,Resources,Insta,Attendance,Non_vitians
# Register your models here.
@admin.register(User)
class PersonAdmin(ImportExportModelAdmin):
    search_fields=['user_reg_no','user_email','user_phone','user_first_name','user_last_name','user_post']
    list_display=['user_first_name','user_last_name','user_reg_no','is_ffcs','user_email','user_phone','user_post']
    list_editable=['user_post','is_ffcs']

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display=['event_name','event_start_date','event_end_date']
    list_editable=[]
    search_fields=['event_name']


@admin.register(Resources)
class ResourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Non_vitians)
class Non_vitiansAdmin(ImportExportModelAdmin):
    search_fields = ['first_name', 'last_name', 'email_id', 'phone', 'college']
    list_display = ['first_name', 'last_name', 'email_id', 'phone', 'college']
