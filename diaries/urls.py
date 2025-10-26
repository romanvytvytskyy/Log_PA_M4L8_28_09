from django.urls import path
from .views import GradebookView, GradeCreateView, GradeDeleteView, GradeUpdateView

urlpatterns = [
    path('', GradebookView.as_view(), name="gradebook"),
    path('grade/<int:pk>/edit/', GradeUpdateView.as_view(), name="grade-edit"),
    path('grade/add/', GradeCreateView.as_view(), name="grade-add"),
    path('grade/<int:pk>/delete', GradeDeleteView.as_view(), name="grade-delete"),
]
