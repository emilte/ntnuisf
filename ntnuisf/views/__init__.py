from django.http import HttpRequest
from django.views import View
from django.shortcuts import render


class IndexView(View):
    template = 'ntnuisf/index.html'

    def get(self, request: HttpRequest):
        return render(request, self.template)


class ForbiddenView(View):
    template = 'ntnuisf/forbidden.html'

    def get(self, request):
        return render(request, self.template)
