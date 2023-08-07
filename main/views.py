from django.shortcuts import render, get_object_or_404, redirect
from main.models import Student, Subject
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from main.forms import StudentForm, SubjectForm
from django.forms import inlineformset_factory


class StudentListView(ListView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('main:home')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:home')


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


def view_student(requests, pk):
    student_item = get_object_or_404(Student, pk=pk)
    context = {
        'object': student_item
    }
    return render(requests, 'main/student_detail.html', context)


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:home'))
