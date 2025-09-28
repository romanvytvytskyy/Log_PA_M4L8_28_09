from django.shortcuts import render
from .models import Announcement
from django.views.generic import ListView

# Create your views here.
class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcement/announcement_list.html'
    context_object_name = 'announcement'
    queryset = Announcement.objects.order_by('-created_at')