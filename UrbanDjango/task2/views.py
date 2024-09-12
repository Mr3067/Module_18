from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request,'class_view.html')


# class index2(TemplateView):
#     template_name = 'func_view.html'