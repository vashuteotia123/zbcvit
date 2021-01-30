from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Question, Choice
from app1.models import User

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last 5 published questions not including
        those set to be published in the future
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplaying the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Please select atleast one option!'
        })
    else:
        try:
            user = request.session['user_email']
            user1 = User.objects.filter(pk=user).get()
            selected_choice.votes.add(user1)
        except:
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': 'Please login..!'
            })
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
