from django.shortcuts import render
from .models import Announcement
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/announcements_list.html'
    context_object_name = 'announcement'
    queryset = Announcement.objects.order_by('-created_at')
    
class AnnouncementCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Announcement
    fields = ['title', 'content']
    template_name = 'announcements/announcement_form.html'
    success_url = reverse_lazy('announcement-list')
    
    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form.valid(form)
    
    def test_func(self):
        if hasattr(self.request.user, 'profile'):
            return self.request.user.profile.role in ['admin', 'moderator']
        return False


class AnnouncementUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model =Announcement
    fields = ['title', 'content']
    template_name = 'announcements/announcement_form.html'
    success_url = reverse_lazy('announcement-list')
    def test_func(self):
        if hasattr(self.request.user, 'profile'):
            return self.request.user.profile.role in ['admin', 'moderator']
        return False

class AnnouncementDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model =Announcement
    template_name = 'announcements/announcement_form.html'
    success_url = reverse_lazy('announcement-list')
    def test_func(self):
        if hasattr(self.request.user, 'profile'):
            return self.request.user.profile.role in ['admin', 'moderator']
        return False