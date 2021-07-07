from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice

from django.template import loader

#-----------------------------------V1------------------------------------------#
#def index(request):
#    return render(request, 'djangroot/index.html')
# à éditer pour mettre des test BDD


#def index2(request):
#    dicos = [{'name': 'd1'}, {'name': 'd2'}, {'name': 'd3'}]
#    context = {'dicos': dicos}
#    print(context)
#    return render(request, 'djangroot/index2.html', context)

#-----------------------------------V2------------------------------------------#
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'djangroot/index.html', context)
#
#
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'djangroot/detail.html', {'question_id': question_id, 'question': question})
#
#
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'djangroot/results.html', {'question': question})
#
#
#def vote(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choice = question.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(request, 'djangroot/detail.html', {
#            'question': question,
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        return HttpResponseRedirect(reverse('djangroot_name:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'djangroot/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'djangroot/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'djangroot/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'djangroot/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('djangroot_name:results', args=(question.id,)))

