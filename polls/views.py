from django.shortcuts import render
from .models import Poll, Option
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from events.views import StaffRequiredMixin

from django.shortcuts import get_object_or_404, redirect

# Create your views here.
class PollListView(ListView):
    model = Poll
    template_name = 'polls/poll_list.html'
    content_object_name ='polls'

class PollDetailView(LoginRequiredMixin,DetailView):
    model= Poll
    template_name = 'polls/poll_detail.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.user in self.object.voted.user.all():
            context['user_voted'] = True
        else:
            context['user_voted'] = False
        return context
            
class PollResultsView(DetailView):
    model = Poll
    template_name = 'polls/poll_result.html'
    
class PollCreateView(StaffRequiredMixin, CreateView):
    model = Poll
    fields = ['question']
    template_name = 'polls/poll_from.html'
    success_url = reverse_lazy('poll-list')
    
class PollUpdateView(StaffRequiredMixin, UpdateView):
    model = Poll
    fields = ['question']
    template_name = 'polls/poll_from.html'
    success_url = reverse_lazy('poll-list')

class PollDeleteView(StaffRequiredMixin, DeleteView):
    model = Poll
    template_name = 'polls/poll_confirm_delete.html'
    success_url = reverse_lazy('poll-list')
    


def vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.user in poll.voted_users.all():
        return HttpResponseForbidden(
             "Ви вже залишили свій відгук"
             )
    try:
        selected_option_id = request.POST['option']
        selected_option = poll.options.get(pk=selected_option_id)
    except (KeyError, Option.DoesNotExist):
        return redirect('poll-detail', pk=pk)
    else:
        selected_option.votes += 1
        selected_option.save()
        poll.voted_users.add(request.user)
        
        return redirect('poll-results', pk=pk)
    