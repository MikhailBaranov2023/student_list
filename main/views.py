from django.shortcuts import render, get_object_or_404
from main.models import Student
from django.views.generic import ListView, DetailView


class StudentListView(ListView):
    model = Student
    template_name = 'main/home.html'


def contact(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        message = requests.POST.get('massage')
        print(f'{name}({email}): {message}')

    context = {
        'title': 'Контакты'
    }

    return render(requests, 'main/contact.html', context)


class StudentsDetailView(DetailView):
    model = Student
    template_name = 'main/student_detail.html'


def view_student(requests, pk):
    student_item = get_object_or_404(Student, pk=pk)
    context = {
        'object': student_item
    }
    return render(requests, 'main/student_detail.html', context)
