from django.urls import path, include
import apis.views as api_view
from django.contrib import admin
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('details/', api_view.DetailView.as_view()),
    path('attendance/', api_view.AttendanceView.as_view()),
    path('marks/', api_view.MarksView.as_view()),
    path('timetable/', api_view.TimetableView.as_view()),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
