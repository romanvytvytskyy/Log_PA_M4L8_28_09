from django.shortcuts import render
from django.views.generic import TemplateView
from announcements.models import Announcement 
from events.models import Events
from polls.models import Poll
from django.utils import timezone

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest-announcements'] = Announcement.objects.order_by('-created_at')[:3]
        context['latest-events'] = Events.objects.filter(
             event_date__gte=timezone.now()
             ).order_by('event_date')[:3]
        context['latest-poll'] = Poll.objects.order_by('-created_at').first()
                
        return context
    
    
        