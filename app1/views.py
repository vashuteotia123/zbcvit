from django.shortcuts import render
from django.shortcuts import redirect
from .models import Notification,User,Event,Event_Photos,Resources,Attendance,Non_vitians,recruitment,Idea
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.db.models import Q, F, Max,Count
from datetime import datetime
import json
import requests
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
import csv



def Home(request):
    return render(request,'index.html')

def Login(request):
    message=None

    if 'is_logedin' not in request.session and request.method!='POST':
        message="Please Enter your Email  and password "
        return render(request,'login.html',{'message':message})
    elif  request.method=='POST':

        user_email=request.POST.get('User_Email')
        user_email=user_email.lower()
        user_password=request.POST.get('User_Password')
        try:
            user_detauls=(User.objects.get(pk=user_email))
            if(user_detauls.user_password==user_password):
                request.session['is_logedin']=True
                request.session['logdin_time']=str(datetime.now())
                request.session['user_email']=user_detauls.user_email
                #request.session['first_name']=user_detauls.user_first_name
                #request.session['last_name']=user_detauls.user_last_name
                request.session['is_admin']=user_detauls.is_admin
                request.session['joindate']=str(user_detauls.user_join_date)
                return redirect('Home')
            else:
                message="Please check your credentials."
        except User.DoesNotExist:
            message="No user found...!!"

        return render(request,'login.html',{'message':message} )

    return redirect("Home")

def Logout(request):
    if 'is_logedin' in request.session:
        del request.session['is_logedin']
        request.session.clear()
        return redirect('Login')
    return redirect("Home")

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        regno=request.POST.get('regno')
        regno=regno.upper()
        dob=request.POST.get('date_of_birth')
        password=request.POST.get('password')
        email=request.POST.get('email')
        email=email.lower()
        phone=request.POST.get('phone')
        check_user=User.objects.filter(pk=email)
        u1=User(user_first_name=first_name,
                    user_last_name=last_name,
                    user_email=email,
                    user_DOB=dob,
                    user_phone=phone,
                    user_reg_no=regno,
                    user_password=password,
                    is_admin=False,
                    user_join_date=datetime.now())
        if not check_user.exists():
            print("innninini")
            u1.save()
            return redirect('Login')
        else :  return render(request,'register.html',{ 'message':"user alredy exists"})

    return render(request,'register.html')

def events_port(request):
    events=Event.objects.all()
    user_details=User.objects.all()
    up_coming=events.filter(event_start_date__gt=datetime.now()).order_by("-event_start_date")
    past=events.filter(event_end_date__lt=datetime.now()).order_by("-event_start_date")
    current=events.filter(event_start_date__lt=datetime.now()).filter(event_end_date__gt=datetime.now()).order_by("-event_start_date")
    context={
        "up_coming":up_coming,
        "past":past,
        "current":current,
        "user":user_details,
        "MEDIA_URL":settings.MEDIA_URL,


    }
    return render(request,"event.html",context=context)

def event_details(request,event_id=0):
    print(event_id)
    if request.method=='POST':
        event_title=request.POST.get('event_title')
        event_desc=request.POST.get('event_desc')
        event_start_dt=request.POST.get('event_start_date')
        event_end_dt=request.POST.get('event_end_date')



        event_start_dt=datetime.strptime(event_start_dt,'%Y-%m-%dT%H:%M')
        event_end_dt=datetime.strptime(event_end_dt,'%Y-%m-%dT%H:%M')

        if event_id==0:
            try:
                photo=request.FILES['event_photo']
            except MultiValueDictKeyError:
                photo=None
            if photo:
                event_photo=photo
            new_event=Event(event_name=event_title,
                            event_start_date=event_start_dt,
                            event_end_date=event_end_dt,
                            event_details=event_desc,

                            event_image=event_photo,
                            )
            new_event.save()
            ev_photo=new_event
        else:

            update_event=Event.objects.get(id=event_id)
            update_event.event_name=event_title
            update_event.event_start_date=event_start_dt
            update_event.event_end_date=event_end_dt
            update_event.event_details=event_desc

            try:
                photo=request.FILES['event_photo']
            except MultiValueDictKeyError:
                photo=None
            if photo:
                update_event.event_image=photo
            update_event.save()



        return redirect('Events_port')
    elif request.method=='GET'and event_id==0:
         return render(request,'event_details.html')
    else:
        event_det=Event.objects.get(pk=event_id)
        event_ph=Event_Photos.objects.filter(event_id=event_det)

        contex={
            "event_id":event_id,
            "title":event_det.event_name,
            "desc":event_det.event_details,
            "start_dt":event_det.event_start_date,
            "start_dt_formated":datetime.strftime(event_det.event_start_date,'%Y-%m-%dT%H:%M') ,
            "end_dt":event_det.event_end_date,
            "end_dt_formated":datetime.strftime(event_det.event_end_date,'%Y-%m-%dT%H:%M') ,
            "reg_usr":event_det.registered_users.all(),

            "MEDIA_URL":settings.MEDIA_URL
        }
    return render(request,'event_details.html',context=contex)

def delete_event(request,event_id):
    ev=Event.objects.filter(pk=event_id).get()
    Event_Photos.objects.get(ev).delete()
    ev.delete()
    return redirect("Events_port")



def profile(request,user_email="my_profile"):
    if 'is_logedin' in request.session:
        print(user_email)
        if request.method=='POST':
            user=User.objects.filter(pk=user_email).get()
            first_name=request.POST.get('fname')
            last_name=request.POST.get('lname')
            post=request.POST.get('post')
            dob=request.POST.get('dob')
            regno=request.POST.get('regno')
            regno=regno.upper()
            github=request.POST.get('github')

            linkedin=request.POST.get('linkedin')
            insta=request.POST.get('insta')
            phone=request.POST.get('phone')
            ccid=request.POST.get('ccid')
            cfid=request.POST.get('cfid')
            user.user_first_name=first_name
            user.user_last_name=last_name
            user.user_phone=phone
            user.user_reg_no=regno
            user.user_github=github
            user.user_linkedin=linkedin
            user.user_insta=insta
            user.user_Codechef_id=ccid
            user.user_Codeforces_id=cfid
            if(post):user.user_post=post
            if(post=="mentor"):
                user.is_admin=True
            user.user_DOB=datetime.strptime(dob,'%Y-%m-%d')
            try:
                photo=request.FILES['profile_photo']
            except MultiValueDictKeyError:
                photo=None
            if photo:
                user.user_profile_photo=photo
            user.save()

        is_user=None
        if('user_email' in request.session and user_email==request.session['user_email']):is_user=True
        if user_email=="my_profile":
            user_email= request.session['user_email']
            is_user=True
        user_details=User.objects.filter(pk=user_email).get()
        context={
            "fname":user_details.user_first_name,
            "lname":user_details.user_last_name,
            "email":user_details.user_email,
            "dob":user_details.user_DOB,
            "regno":user_details.user_reg_no,
            "dob_formated":datetime.strftime(user_details.user_DOB,'%Y-%m-%d'),
            "phone":user_details.user_phone,
            "profile_photo":user_details.user_profile_photo,
            "MEDIA_URL":settings.MEDIA_URL,
            "github":user_details.user_github,
            "linkedin":user_details.user_linkedin,
            "insta":user_details.user_insta,
            "is_user":is_user,
            "is_admin":user_details.is_admin,
            "is_ffc":user_details.is_ffcs,
            "post":user_details.user_post,
            "ccid":user_details.user_Codechef_id,
            "cfid":user_details.user_Codeforces_id,
        }
        print(datetime.strftime(user_details.user_DOB,'%Y-%m-%d'))
        return render(request,'profile.html',context=context)

def resources(request):
    all_resources=Resources.objects.all().order_by("-resource_date_time")
    context={
        "resources":all_resources
    }
    if request.method=='POST':
        all_resources=all_resources.filter( Q(resource_name__contains=request.POST['search'])| Q(resource_content__contains=request.POST['search']) ).order_by("-resource_date_time")
        context={
            "resources":all_resources,
        }
    return render(request,"resources.html",context=context)



def resource_detail(request,resource_id=0):
    if 'is_logedin' in request.session and request.session['is_admin']==True:
        if request.method=='POST':
            print(resource_id)
            resource_title=request.POST.get('rname')
            resource_desc=request.POST.get('rdesc')
            resource_link=request.POST.get('rlink')
            if resource_id==0:
                new_resource=Resources(resource_name=resource_title,resource_content=resource_desc,resource_link=resource_link,resource_date_time=datetime.now())
                new_resource.save();
                return redirect("Admin_port")
            else:
                update_resource=Resources.objects.filter(pk=resource_id).get()
                update_resource.resource_name=resource_title
                update_resource.resource_content=resource_desc
                update_resource.resource_link=resource_link
                update_resource.save()
                return redirect("Resources")
        context={}
        if resource_id!=0:
            rid=Resources.objects.filter(pk=resource_id).get()
            print(rid.id)
            context={"resource":rid}
        else :  context={"resource":{ "id":0}}
        return render(request,"resource_detail.html",context=context)
    return redirect("Resources")

def delete_resource(request,resource_id):
    Resources.objects.filter(pk=resource_id).delete()
    return redirect("Resources")

def contest_details(request):
    curr_time=datetime.strftime(datetime.now(),'%Y-%m-%dT%H:%M')
    #cc_users=User.objects.exclude(user_Codechef_id="")
    #cf_users=User.objects.exclude(user_Codeforces_id="")
    #cc_data=[]
    #cf_data=[]
    #for u in cc_users:
     #   x=requests.get("https://competitive-coding-api.herokuapp.com/api/codechef/"+u.user_Codechef_id)
      #  if(x.status_code==200):
       #     x=x.json()
        #    cc_data.append([x['rating'], u.user_email, u.user_first_name, u.user_last_name])
    #for u in cf_users:
        #x=requests.get("https://codeforces.com/api/user.info?handles="+u.user_Codeforces_id)
        #if(x.status_code==200):
            #x=x.json()
            #if 'rating' in x['result'][0]:
                #print(x['result']['rank'])
                #cf_data.append([x['result'][0]['rating'], u.user_email, u.user_first_name, u.user_last_name])
    #print(cf_data)
    #cc_data.sort(reverse=True)
    #cf_data.sort(reverse=True)
    try:
        response1=requests.get("https://clist.by/api/v1/json/contest/?username=vashuteotia123&api_key=a567132c02f52428ee0a946605a049d36d3ab7e8&resource__name=codechef.com&start__gte="+curr_time+"&filtered=true&order_by=start")
        response2 = requests.get("https://clist.by/api/v1/json/contest/?username=vashuteotia123&api_key=a567132c02f52428ee0a946605a049d36d3ab7e8&resource__name=codeforces.com&start__gte=" + curr_time + "&filtered=true&order_by=start")
        response4 = requests.get("https://clist.by/api/v1/json/contest/?username=vashuteotia123&api_key=a567132c02f52428ee0a946605a049d36d3ab7e8&resource__name=hackerearth.com&start__gte=" + curr_time + "&filtered=true&order_by=start")
        response5 = requests.get("https://clist.by/api/v1/json/contest/?username=vashuteotia123&api_key=a567132c02f52428ee0a946605a049d36d3ab7e8&resource__name=codingcompetitions.withgoogle.com&start__gte=" + curr_time + "&filtered=true&order_by=start")
        data1= json.loads(response1.text)
        data2 = json.loads(response2.text)

        data4 = json.loads(response4.text)
        data5 = json.loads(response5.text)
        context={
                "response1":data1['objects'][:10],
            "response2": data2['objects'][:10],

            "response4": data4['objects'][:10],
            "response5": data5['objects'][:10],
                 #"ccuser":cc_data,
                 #"cfuser":cf_data
                 }
    except:
        context={'message':"Server Busy!!Please try again in one minute"}
    return render(request,"contest_details.html",context=context)

def about(request):
    mentors=User.objects.filter(user_post="mentor")
    admins=User.objects.filter(is_admin=True).exclude(user_post="mentor")
    context={
        "mentors":mentors,
        "admins":admins,
        "MEDIA_URL":settings.MEDIA_URL,
    }
    print(context)
    return render(request,"about.html",context=context)

def admin_port(request):
    if 'is_logedin' in request.session and request.session['is_admin']==True:
        user_details=User.objects.filter(is_admin=False)
        admin_details=User.objects.filter(is_admin=True)
        registered_user=Attendance.objects.filter(is_attending=True)
        event_detail=Event.objects.all().order_by('-event_start_date')
        context={
            "users":user_details,
            "admins":admin_details,
            "registered": registered_user,
            "total_events":len(Event.objects.annotate(Count('events_id'))),
            "total_members":(User.objects.filter(is_ffcs=True).count()),
            "total_admins":(User.objects.filter(is_admin=True).count()),
            "total_resources":Resources.objects.all().count(),
            "total_registrations":(Attendance.objects.filter(is_attending=True).count()),
            "event_detail":event_detail,
            "total_ideas":(Idea.objects.all().count()),
        }
        if request.method=='POST':
            message_topic=request.POST.get('topic')
            message_cont=request.POST.get('notification')
            print(message_cont)
            if message_topic!="" and message_cont!="":
                new_noti=Notification(notofication_topic=message_topic,
                                    notofication_content=message_cont,
                                    notofication_datetime=datetime.now())
                new_noti.save()
                context['message']="Notification added successfully"
                return render(request,'admin_panal.html',context=context)
            else :
                return render(request,'admin_panal.html',context=context)
        else: return render(request,'admin_panal.html',context=context)
    else:
        return redirect("Home")

def add_as_admin(request,user_email):
    new_admin=User.objects.filter(user_email=user_email).get()
    new_admin.is_admin=True
    new_admin.save()
    return redirect("Admin_port")

def remove_admin(request,user_email):
    rem_admin=User.objects.filter(user_email=user_email).get()
    rem_admin.is_admin=False
    rem_admin.save()
    return redirect("Admin_port")

def remove_profile(request,user_email):
    User.objects.filter(user_email=user_email).delete()
    return redirect("Admin_port")

def navbar_restructure(request):
    message={}
    notifications_obj=[]
    if 'is_logedin' in request.session:
        message['messaage']='loged_in'
        message['is_admin']=request.session['is_admin']
        notifications_obj.append(message)
        noti_final=[]
        join_dt=request.session['joindate'].format(datetime.now())
        notifications=Notification.objects.filter(notofication_datetime__gt=join_dt)
        new_notifications=notifications.exclude(notification_seen=User.objects.get(user_email=request.session['user_email'])).order_by("-notofication_datetime")
        old_notifications=Notification.objects.filter(notification_seen=User.objects.get(user_email=request.session['user_email'])).order_by("-notofication_datetime")
        for notification in new_notifications:
            noti={
            'id':notification.id,
            'topic':notification.notofication_topic,
            'content':notification.notofication_content,
            'datetime':str((notification.notofication_datetime).strftime("%a,%d %B,%y %I:%M:%S %p"))
            }
            noti_final.append(noti)
        new_noti_final=noti_final
        noti_final=[]
        for notification in old_notifications:
            noti={
            'id':notification.id,
            'topic':notification.notofication_topic,
            'content':notification.notofication_content,
            'datetime':str((notification.notofication_datetime).strftime("%a,%d %B,%y %I:%M:%S %p"))
            }
            noti_final.append(noti)
        old_noti_final=noti_final
        notifications_obj.append({'New_notifications':new_noti_final,'Old_notifications':old_noti_final});
    else :
        message['messaage']='not_logedin'
        notifications_obj.append(message)

    notifications_obj=json.dumps(notifications_obj)
    return HttpResponse(notifications_obj)


def Close_notification(request):
    if request.is_ajax():
        message_id=request.POST.get('seen_message_id')
        print(message_id)
        message_seen=Notification.objects.get(pk=int(message_id))
        user=User.objects.get(pk=request.session['user_email'])
        message_seen.notification_seen.add(user)
        return render(request,'index.html')


def Delete_notification(request):
    if request.is_ajax():
        message_id=request.POST.get('delete_message_id')
        noti= Notification.objects.get(id=message_id)
        noti.notification_seen.clear()
        noti.delete()
        print("deleted")
        return render(request,'index.html')

def insta(request):
    return render(request,"insta.html")

def Insta_link(request,insta_id=0):
    if 'is_logedin' in request.session and request.session['is_admin']==True:
        if request.method=='POST':
            print(insta_id)
            insta_link=request.POST.get('ilink')
            if insta_id==0:
                new_link=Insta(insta_link=insta_link)
                new_link.save();
                return redirect("Admin_port")
            else:
                update_insta=Insta.objects.filter(pk=insta_id).get()
                update_insta.insta_link=insta_link
                update_insta.save()
                return redirect("Insta")
        context={}
        if insta_id!=0:
            rid=Insta.objects.filter(pk=insta_id).get()
            print(rid.id)
            context={"insta":rid}
        else :  context={"insta":{ "id":0}}
        return render(request,"insta_link.html",context=context)
    return redirect("Insta")

def team(request):
    return render(request,"team.html")

def is_attending(request, event_id):
    event = Event.objects.get(pk=event_id)
    events=Event.objects.all()
    user_details=User.objects.all()
    up_coming=events.filter(event_start_date__gt=datetime.now()).order_by("-event_start_date")
    past=events.filter(event_end_date__lt=datetime.now()).order_by("-event_start_date")
    current=events.filter(event_start_date__lt=datetime.now()).filter(event_end_date__gt=datetime.now()).order_by("-event_start_date")
    if 'is_logedin' not in request.session:
        message = "Please Login to Register"
        return render(request, 'login.html', {'message': message})
    elif event in past:
        message = "Registration closed"
        return render(request, 'index.html', {'message': message})
    else:
        user_email = request.session['user_email']
        user=User.objects.filter(pk=user_email).get()

        event.registered_users.add(user)
        message='Registered successfully!'


    context={
        "up_coming":up_coming,
        "past":past,
        "current":current,
        "user":user_details,
        "MEDIA_URL":settings.MEDIA_URL,
        "message":message,


    }
    return render(request, 'event.html', context=context)

def clear_list(request):
    clearlist=Attendance.objects.all()
    user_email = request.session['user_email']
    user_details = User.objects.filter(is_admin=False)
    admin_details = User.objects.filter(is_admin=True)
    registered_user = Attendance.objects.filter(is_attending=True)
    context = {
        "users": user_details,
        "admins": admin_details,
        "registered": registered_user,
        "total_events": len(Event.objects.annotate(Count('id'))),
        "total_users": (User.objects.filter(is_admin=False).count()),
        "total_admins": (User.objects.filter(is_admin=True).count()),
        "total_resources": Resources.objects.all().count(),
        "total_registrations": (Attendance.objects.filter(is_attending=True).count()),
    }
    if user_email=="vishal.teotia2019@vitstudent.ac.in":
        clearlist.delete()
        clear_email = request.session['user_email']
        current_user=User.objects.filter(user_email=clear_email).get()
        context['who_email'] = clear_email
        context['who_cleared'] = current_user.user_first_name
        context['who_cleared2'] = current_user.user_last_name
        context['date'] = str(datetime.now().date())
        context['time'] = str(datetime.now().time())
    else:
        context['message']='You are not permitted to clear the list'
    return render(request, 'admin_panal.html', context=context)

def user_registered(request,event_id=0):
    print(event_id)
    if 'is_logedin' in request.session and request.session['is_admin']==True:
        event_det=Event.objects.get(pk=event_id)
        event_ph=Event_Photos.objects.filter(event_id=event_det)
        non_vit=Non_vitians.objects.all()
        contex={
            "event_id":event_id,
            "title":event_det.event_name,
            "desc":event_det.event_details,
            "start_dt":event_det.event_start_date,
            "start_dt_formated":datetime.strftime(event_det.event_start_date,'%Y-%m-%dT%H:%M') ,
            "end_dt":event_det.event_end_date,
            "end_dt_formated":datetime.strftime(event_det.event_end_date,'%Y-%m-%dT%H:%M') ,
            "reg_usr":event_det.registered_users.all(),
            "count_reg_usr": event_det.registered_users.all().count(),
            "event_link":event_det.event_registation,
            "MEDIA_URL":settings.MEDIA_URL,
            "non_vit":non_vit,
        }
    return render(request,'user_registered.html',context=contex)


def reset_password(request):
    try:
        mail_subject='ZBC Login'
        to_email = request.POST.get('mail_id')
        to_email=to_email.lower()
        user_det=User.objects.filter(pk=to_email).get()
        ctx={
            "f1name":user_det.user_first_name,
            "l1name":user_det.user_last_name,
            "pass":user_det.user_password,
        }
        msg=get_template('mail.html').render(ctx)
        email = EmailMessage(
            mail_subject, msg, to=[to_email]
        )
        email.content_subtype = "html"
        email.send()
        message="Please check given mail id for password. Do check spam folder."
        return render(request, 'login.html', {'message': message})
    except:
        message="Please enter registered mail ID"
        return render(request, 'reset_pass.html', {'message': message})




def reset_pas(request):
    return render(request,'reset_pass.html')

def nonvit(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('dis_id')
        email=request.POST.get('email')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        if Non_vitians.objects.filter(email_id=email):
            message="Already registered"
            return render(request, 'index.html', {'message':message})
        new = Non_vitians(
            first_name=first_name,
            last_name = last_name,
            email_id=email,
            phone=phone,
            college=college,
            )
        new.save()
        message="Registered Successfully"
    return render(request, 'index.html', {'message':message})

def nonvit_reg(request):
    events=Event.objects.all()
    user_details=User.objects.all()
    up_coming=events.filter(event_start_date__gt=datetime.now()).order_by("-event_start_date")
    for eve in up_coming:
        if eve.non_vitians==True:
            return render(request,'nonvit_reg.html')
    return render(request, 'index.html', {'message':"Registrations closed"})

def certificate(request,event_id=0):
    print(event_id)
    event_det = Event.objects.get(pk=event_id)
    if 'is_logedin' in request.session:
        user_email = request.session['user_email']
        for usr in event_det.registered_users.all():
            if user_email == usr.user_email:
                user = User.objects.filter(pk=user_email).get()
                contex={
                    "event_id":event_id,
                    "title":event_det.event_name,
                    "end_dt":event_det.event_end_date,
                    "end_dt_formated":datetime.strftime(event_det.event_end_date,'%d-%m-%Y') ,
                    "reg_usr":event_det.registered_users.all(),
                    "fname":user.user_first_name,
                    "lname":user.user_last_name,
                }
                return render(request,'certificate.html', contex)

        else:

            events=Event.objects.all()
            user_details=User.objects.all()
            up_coming=events.filter(event_start_date__gt=datetime.now()).order_by("-event_start_date")
            past=events.filter(event_end_date__lt=datetime.now()).order_by("-event_start_date")
            current=events.filter(event_start_date__lt=datetime.now()).filter(event_end_date__gt=datetime.now()).order_by("-event_start_date")
            context={
                "up_coming":up_coming,
                "past":past,
                "current":current,
                "user":user_details,
                "MEDIA_URL":settings.MEDIA_URL,
                "message":"You didn't register for this event"
            }
            return render(request,"event.html",context=context)
    else:
        return redner(request,'login.html')

def reg_csv(request,event_id=0):
    print(event_id)
    output = []
    response = HttpResponse(content_type='text/csv')
    event_det = Event.objects.get(pk=event_id)
    reg_usr = event_det.registered_users.all(),
    filename = event_det.event_name+u".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(filename)
    writer = csv.writer(response)

    # Header
    writer.writerow(['Name', 'Email', 'Phone','Reg No.'])
    for us in reg_usr:
        for u in us:
            output.append([u.user_first_name+" "+u.user_last_name,u.user_email,u.user_phone,u.user_reg_no])
    # CSV Data
    writer.writerows(output)
    output1=[]
    writer.writerow(['NON-VITIANS'])
    writer.writerow(['Name', 'Email','Phone','College'])
    non_vit=Non_vitians.objects.all()
    for u in non_vit:
        output1.append([u.first_name + " " + u.last_name, u.email_id, u.phone,u.college])
    writer.writerows(output1)
    return response

def leaderboard(request):

    cc_users=User.objects.exclude(user_Codechef_id="")
    cf_users=User.objects.filter(user_Codeforces_id__isnull=False)
    cc_data=[]
    cf_data=[]
    for u in cc_users:


        url = ("https://competitive-programming-platform.p.rapidapi.com/codechef/"+str(u.user_Codechef_id))

        headers = {
            'x-rapidapi-key': "350629e7e8msh2a4005052689697p1d2ef5jsnac409665d078",
            'x-rapidapi-host': "competitive-programming-platform.p.rapidapi.com"
        }
        x=requests.request("GET", url, headers=headers)
        if(x.status_code==200):
            x=x.json()
            if 'rating' in x:
                cc_data.append([x['rating'], u.user_email, u.user_first_name, u.user_last_name, x['stars']])


    for u in cf_users:
        x = requests.get("https://codeforces.com/api/user.info?handles="+str(u.user_Codeforces_id))
        x=x.json()
        if(x['status']=="OK"):
            if 'rating' in x['result'][0]:

                cf_data.append([x['result'][0]['rating'], u.user_email, u.user_first_name, u.user_last_name,x['result'][0]['rank']])


    cc_data.sort(reverse=True)
    cf_data.sort(reverse=True)

    context={

            "ccuser":cc_data,
            "cfuser":cf_data
            }
    return render(request,"leaderborad.html",context=context)


def recruit_page(request):
    return render(request,"registration_form.html")

def recruit(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        email=request.POST.get('email')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        depatment=request.POST.get('checks')
        new = recruitment(
            full_name=first_name,
            email=email,
            phone=phone,
            regno=college,
            department=depatment,
            )
        new.save()
        message="Registered Successfully"
    return render(request, 'index.html', {'message':message})

def linktree(request):
    events=Event.objects.all()
    up_coming=events.filter(event_start_date__gt=datetime.now()).order_by("-event_start_date")
    context ={
        "upcoming" : up_coming,
        }
    return render(request, 'linktree.html', context = context)

def register_member(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        regno=request.POST.get('regno')
        regno=regno.upper()
        dob=request.POST.get('date_of_birth')
        password=request.POST.get('password')
        email=request.POST.get('email')
        email=email.lower()
        phone=request.POST.get('phone')
        check_user=User.objects.filter(pk=email)
        u1=User(user_first_name=first_name,
                    user_last_name=last_name,
                    user_email=email,
                    user_DOB=dob,
                    user_phone=phone,
                    user_reg_no=regno,
                    user_password=password,
                    is_admin=False,
                    is_ffcs=True,
                    user_join_date=datetime.now())
        if not check_user.exists():
            print("innninini")
            u1.save()
            return redirect('Login')
        else :  return render(request,'register_member.html',{ 'message':"user alredy exists"})

    return render(request,'register_member.html')

def idea_page(request):
    if 'is_logedin' not in request.session:
        message = "Please Login."
        return render(request, 'login.html', {'message': message})
    elif 'is_logedin' in request.session and User.objects.filter(pk=request.session['user_email']).get().is_ffcs==False:
        message = "Only available for club members."
        return render(request, 'index.html', {'message': message})
    else:
        return render(request, 'idea_sub.html')

def idea_sub(request):
    idea=request.POST.get('idea')
    framework=request.POST.get('framework')
    user_email = request.session['user_email']
    user=User.objects.filter(pk=user_email).get()

    try:
        ids=Idea(idea=idea,framework=framework,user=user)
        ids.save()
        message='Submitted successfully!'
        context={
            "message":message,
        }
        return render(request, 'index.html', context=context)


    except:
        Idea.objects.get(user=user)
        message='Only one submission is allowed.'
        context={
        "message":message,
        }
        return render(request, 'index.html', context=context)


def idea_show(request):
    if 'is_logedin' in request.session and request.session['is_admin']==True:
        context={
            "idea":Idea.objects.all,
            }
        return render(request,'idea_show.html',context=context)
    else:
        return render(request,'index.html')

