from django.urls import path
from note.views import MainPage

urlpatterns = [
    path('', MainPage.as_view()),
]
