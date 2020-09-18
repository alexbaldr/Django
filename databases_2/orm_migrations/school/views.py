from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    object_list = Student.objects.prefetch_related('teacher').order_by(ordering)
    # object_list = Student.objects.all().order_by(ordering)
    context = {
        'object_list':object_list,
    }
    
    return render(request, template, context)
