from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import gettext_lazy as _


class MainIndex(View):
    def get(self, request):
        return render(request, 'main/index.html')