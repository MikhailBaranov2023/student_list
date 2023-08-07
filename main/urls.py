from django.urls import path
from main.views import contact, view_student, StudentListView, StudentsDetailView, StudentCreateView, StudentUpdateView, \
    StudentDeleteView, toggle_activity
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>', StudentsDetailView.as_view(), name='view_student'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', StudentUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
