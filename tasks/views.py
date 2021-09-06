from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import requests

from tasks.models import Task, video_links,documents_links
from app1.models import User


def task(request):
    if 'is_logedin' in request.session:
        task=Task.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        context={
            'task_list':task,


        }
        return render(request,'tasks/index.html',context=context)
    else:
        message="Please login"
        context={
            'message':message
            }
        return render(request,'login.html',context=context)

def task_details(request, task_id=0):
    print(task_id)
    task_det=Task.objects.get(pk=task_id)
    context={
        'task_det':task_det,
        'image':task_det.task_img,
    }
    return render(request,'tasks/task_details.html',context=context)

