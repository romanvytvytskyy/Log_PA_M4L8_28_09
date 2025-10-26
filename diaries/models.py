from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, 
                            unique=True,
                            verbose_name="Назва предмету" 
                            )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"
    
class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Студент")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    grade = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)],
                                        verbose_name="Оцінка")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата отримання")
    comment = models.CharField(max_length=255, blank=True, null=True, verbose_name="Коментар")
    
    def __str__(self):
        return f"{self.student.username} - {self.subject.name}: {self.grade}"

    class Meta:
        verbose_name= "Оцінка"
        verbose_name_plural= "Оцінки"
        ordering = ["-date"]