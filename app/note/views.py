from django.shortcuts import render, redirect, reverse
from django.views import View
from note.models import Note

from note.utils import timeout_occurred


class MainPage(View):
    def get(self, request):
        return render(request, 'note/home.html')

    def post(self, request):
        note = Note.objects.create(content=request.POST.get('note'))
        return redirect(reverse('show_link', args=(note.address,)))


class ShowLink(View):
    def get(self, request, address):
        note = Note.objects.filter(address=address).first()
        if note:
            return render(request, 'note/showlink.html', context={'address': note.address})
        else:
            return redirect('NotExist404')


class OpenNote(View):
    def get(self, request, address):
        note = Note.objects.filter(address=address).first()
        if note:
            return render(request, 'note/open_note.html', context={'address': note.address})
        else:
            return redirect('NotExist404')


class ShowNote(View):
    def get(self, request, address):
        note = Note.objects.filter(address=address).first()
        if note and not timeout_occurred(note.date_added):
            note.delete()
            return render(request, 'note/note.html', context={'content': note.content})
        else:
            return redirect('NotExist404')


class NotExist404(View):
    def get(self, request):
        return render(request, 'note/404.html')
