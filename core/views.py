from django.shortcuts import render
from django.views.generic import TemplateView
from announcements.models import Announcement 
# from events.models import Event
# from polls.model.Poll

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest-announcements'] = Announcement.objects.order_by('-created_at')
        
        return context
    
    
        