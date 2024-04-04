from django.urls import path
from .views import courseListView,courseDetailView

urlpatterns =[
    path('courses/',courseListView.as_view()),
    path('courses/<int:pk>',courseDetailView.as_view()),
]