from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView
from django.utils.translation import gettext_lazy as _
from main.models import Post, Category


class MainIndex(View):
    def get(self, request, id=None):
        query = Post.objects.order_by('-id')
        if id is not None:
            query = query.filter(category_id=id)

        paginator = Paginator(query.all(), 2)
        page = paginator.get_page(request.GET.get('page'))

        return render(request, 'main/index.html', {
            'object_list': page.object_list,
            'page_obj': page,
            'categories': Category.objects.all()
        })


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