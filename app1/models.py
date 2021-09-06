from django.db import models
from datetime import datetime
from django.conf import settings


class User(models.Model):
    user_first_name=models.CharField(max_length=50,null=False)
    user_last_name=models.CharField(max_length=50,null=False)
    user_email=models.EmailField(primary_key=True,null=False)
    user_DOB=models.DateField(null=False)
    user_password=models.CharField(max_length=100,null=False)
    user_phone=models.CharField(max_length=12,null=False)
    user_reg_no=models.CharField(max_length=10,null=False)
    is_admin=models.BooleanField(default=False)
    is_ffcs=models.BooleanField(default=False)
    user_join_date=models.DateTimeField(auto_now_add=True)
    user_post=models.CharField(max_length=50,default="user")
    user_github=models.CharField(max_length=5000,blank=True,null=True)
    user_linkedin=models.CharField(max_length=5000,blank=True,null=True)
    user_insta=models.CharField(max_length=5000,blank=True,null=True)
    user_profile_photo=models.ImageField(upload_to="profile/",blank=True,null=True)
    events_reg=models.ManyToManyField('Event',related_name="events_id",blank=True,null=True)
    user_Codechef_id=models.CharField(max_length=50,null=True,blank=True)
    user_Codeforces_id=models.CharField(max_length=50,null=True,blank=True)





class Notification(models.Model):
    notofication_topic=models.CharField(max_length=50)
    notofication_content=models.CharField(max_length=1000)
    notofication_datetime=models.DateTimeField(auto_now_add=True)
    notification_seen=models.ManyToManyField(User)

class Event(models.Model):
    event_name=models.CharField(max_length=50)
    event_start_date=models.DateTimeField(null=False)
    event_end_date=models.DateTimeField(null=False)
    event_details=models.CharField(max_length=5000)
    non_vitians=models.BooleanField(default=False)
    event_registation=models.CharField(max_length=1000,default="")
    event_image=models.ImageField(upload_to="event_photos/",null=True)
    registered_users=models.ManyToManyField('User',related_name='red_usr',blank=True)



class Event_Photos(models.Model):
    event_id=models.ForeignKey(Event,on_delete=models.CASCADE)
    event_photo=models.ImageField(upload_to="event_photos/",null=True)


class Resources(models.Model):
    resource_name=models.CharField(max_length=50)
    resource_content=models.CharField(max_length=500)
    resource_link=models.CharField(max_length=5000, default="")
    resource_date_time=models.DateTimeField(null=False,default=datetime.now())

class Insta(models.Model):
    insta_link=models.CharField(max_length=100000,default="")

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendants',unique=False)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attending',primary_key=True,unique=False)
    is_attending = models.BooleanField(default=False)


class recruitment(models.Model):
    full_name=models.CharField(max_length=50,null=False)
    regno=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=50,null=False)
    department=models.CharField(max_length=100,null=False)


class Non_vitians(models.Model):
    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=20,null=False)
    email_id=models.EmailField(max_length=50,null=False)
    phone=models.CharField(max_length=12,null=False)
    college=models.CharField(max_length=50,null=True)

class Idea(models.Model):
    idea=models.TextField(max_length=5000,null=False)
    framework=models.CharField(max_length=1000,null=True)
    user=models.OneToOneField('User',blank=True,on_delete=models.CASCADE,unique=False)