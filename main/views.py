from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.utils.translation import gettext_lazy as _
from main.models import Post


class MainIndex(View):
    def get(self, request):
        return render(request, 'main/index.html')


class UploadPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'comment', 'file']
    template_name = 'layouts/form.html'
    success_url = reverse_lazy('main:upload')

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        request.title = _("Yuklash")

    def form_valid(self, form):
        form.instance.user = self.request.user # me
        messages.success(self.request, _("Muvaffaqiyatli qo'shildi."))
        return super().form_valid(form)