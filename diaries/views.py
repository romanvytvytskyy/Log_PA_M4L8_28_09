from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Grade, Subject
from events.views import StaffRequiredMixin

# Create your views here.
class GradebookView(ListView):
    model = Grade
    template_name = 'diaries/gradebook.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = User.objects.all()
        subjects = Subject.objects.all()
        
        grade_data = {}
        #! { "student1": {"MAth": [10,5,12,7,9,8], "Atr": [8,9,7,8,9]} }
        
        for student in students:
            grade_data[student.username] = {}
            for subject in subjects:
                grade = Grade.objects.filter(student=student, subject=subject)
                grade_data[student.username][subject.name] = list(grade)
                
        context['subjects'] = subjects
        context['students'] = students
        context['grade_data'] = grade_data
        return context                

class GradeCreateView(StaffRequiredMixin, CreateView):
    model = Grade
    fields = ['student', 'subject', 'grade', 'comment']
    template_name = 'diaries/grade_form.html'
    success_url = reverse_lazy('gradebook')
    
class GradeUpdateView(StaffRequiredMixin, UpdateView):
    model = Grade
    fields = ['student', 'subject', 'grade', 'comment']
    template_name = 'diaries/grade_form.html'
    success_url = reverse_lazy('gradebook')
class GradeDeleteView(StaffRequiredMixin, DeleteView):
    model = Grade
    template_name = 'diaries/grade_confirm_delete.html'
    success_url = reverse_lazy('gradebook')
    