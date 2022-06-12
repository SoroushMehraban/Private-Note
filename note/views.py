from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class MainPage(View):
    def get(self, request):
        return render(request, 'note/home.html')

    def post(self, request):
        # TODO: Store note here
        return HttpResponseRedirect(request.path_info)
