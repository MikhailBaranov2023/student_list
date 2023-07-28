from django.urls import path
from main.views import contact, view_student, StudentListView, StudentsDetailView
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>', StudentsDetailView.as_view(), name='view_student')
]
