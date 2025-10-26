from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Events




# Create your views here.
class EventListView(ListView):
    model = Events
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    
class EventDetailView(DetailView):
    model = Events
    template_name = 'events/event_detail.html'
    
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        if hasattr(self.request.user, 'profile'):
            return self.request.user.profile.role in ['admin', 'moderator']
        return False
    
class EventCreateView(StaffRequiredMixin, CreateView):
    model = Events
    fields = ['name', 'description', 'event_date']
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event-list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class EventUpdateView(StaffRequiredMixin, UpdateView):
    model = Events
    fields = ['name', 'description', 'event_date']
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event-list')
class EventDeleteView(StaffRequiredMixin, DeleteView):
    model = Events
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')
    
    