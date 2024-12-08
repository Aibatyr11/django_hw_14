from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import BbForm
from .models import *


class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index_html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rubrics"] = Rubric.objects.all()
        return context


def index(request):
    s = "Спсиок объявлений\r\n"
    bb = Bb.objects.order_by('-published')
    for b in bb:
        s += b.title + '\r\n' + b.content + '\r\n'
    return HttpResponse(s, content_type="text/plain; charset=utf-8")


def hello(request):
    return HttpResponse("Hello")


def index_html(request):
    bb = Bb.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    context = {'bb': bb, 'rubrics': rubrics}  # отправка в html
    return render(request, 'index.html', context)


def by_rubric(request, rubric_id):
    bb = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(id=rubric_id)
    context = {'bb': bb, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'by_rubric.html', context)


def get_by_slug(request, slug):
    crypto = Crypto.objects.get(slug=slug)
    return render(request, "crypto.html", {"crypto": crypto})


def comment(request, slug):
    comment = Comment.objects.get(slug=slug)
    return render(request, "comment.html", {"comment": comment})


def comment_delete(request, slug):
    comment_delete = Comment.objects.get(id=id)
    Comment.objects.filter(pk=id).delete()

    return render(request, "comment_delete.html", {"comment_delete": comment_delete})

