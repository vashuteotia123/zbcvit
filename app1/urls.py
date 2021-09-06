"""Pc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Home, name='Home'),
    path('login',views.Login, name='Login'),
    path('logout',views.Logout, name='Logout'),
    path('login/register',views.register, name='Register'),
    path('events',views.events_port, name='Events_port'),
    path('profile<user_email>',views.profile,name='Profile'),
    path('add_as_admin<user_email>',views.add_as_admin,name='Add_as_admin'),
    path('remove_admin<user_email>',views.remove_admin,name='Remove_admin'),
    path('remove_profile<user_email>',views.remove_profile,name='Remove_profile'),
    path('events/event_details<int:event_id>',views.event_details, name='Event_details'),
    path('delete_event<int:event_id>',views.delete_event, name='Delet_event'),
    path('resources/', views.resources, name='Resources'),
    path('resource_detail<int:resource_id>',views.resource_detail, name='Resource_detail'),
    path('delete_resource<int:resource_id>',views.delete_resource, name='Delete_resource'),
    path('about',views.about, name='About'),
    path('admin_pirt',views.admin_port, name='Admin_port'),
    path('close_notification',views.Close_notification, name='Close_notification'),
    path('delete_notification',views.Delete_notification,name='Delete_notification'),
    path('navbar_restructure',views.navbar_restructure,name='Navbar_restructure'),
    path('insta',views.insta,name='Insta'),
    path('insta_link<int:insta_id>',views.Insta_link,name='Insta_link'),
    path('acd37e8ae184b8e8b12<int:event_id>3818117e35a0a',views.is_attending,name='attending'),
    path('clear_list',views.clear_list,name='Clear_list'),
    path('events/user_registered<int:event_id>',views.user_registered, name='User_registered'),
    path('reset_password',views.reset_password,name="Reset_password"),
    path('reset_pas',views.reset_pas,name="reset_pass"),
    path('nonvit',views.nonvit,name='Non_vit'),
    path('nonvit_reg',views.nonvit_reg,name='nonvit_reg'),
    path('acd37e8ae18968e8b12<int:event_id>38184527e35a0a',views.certificate,name='certificate'),
    path('contests/',views.contest_details,name='contests'),
    path('events/reg_csv<int:event_id>',views.reg_csv,name='reg_csv'),
    path('leaderboard',views.leaderboard,name='leaderboard'),
    path('recruitment',views.recruit,name="recruit"),
    path('summer_tech',views.recruit_page,name="recruitment"),
    path('linktree',views.linktree,name="linktree"),
    path('member_register',views.register_member,name="member_register"),
    path('idea_pitch',views.idea_page,name="idea_pitch"),
    path('idea_sub',views.idea_sub,name="idea_sub"),
    path('idea_show',views.idea_show,name="idea_show"),

]
