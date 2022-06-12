from django.urls import path
from note.views import MainPage, ShowLink, OpenNote, ShowNote, NotExist404

urlpatterns = [
    path('', MainPage.as_view(), name='homepage'),
    path('show_link/<str:address>', ShowLink.as_view(), name='show_link'),
    path('open_note/<str:address>', OpenNote.as_view(), name='open_note'),
    path('note/<str:address>', ShowNote.as_view(), name='show_note'),
    path('404/', NotExist404.as_view(), name='NotExist404')
]
