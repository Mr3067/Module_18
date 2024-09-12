from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView


def task4_main(request):
    return render(request, template_name=r'fourth_task\task4_main.html')


def task4_depend1(request):
    list_doing = ['Настольные', 'Подстольные', 'На свежем воздухе']
    context = {
        'list_doing': list_doing
    }
    return render(request, template_name=r'fourth_task\task4_depend1.html', context=context)


def task4_depend2(request):
    return render(request, template_name=r'fourth_task\task4_depend2.html')

# class index2(TemplateView):
#     template_name = 'func_view.html'
