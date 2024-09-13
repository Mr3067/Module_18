from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm
from .db_task5 import five_member, list_member

CONTEXT = {}


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        print(f'Name: {username}')
        print(f'Password: {password}')
        print(f'repeat_password: {repeat_password}')
        print(f'age: {age}')
        if (not username in [list_member[i][0] for i in range(len(list_member))]
                and (password == repeat_password)
                and age >= 18):
            return HttpResponse(f'Приветствуем, {username}!')
        elif not password == repeat_password:
            return HttpResponse(f'Пароли не совпадают!')
        elif age < 18:
            return HttpResponse(f'Вы должны быть старше 18!')
        elif username in [list_member[i][0] for i in range(len(list_member))]:
            return HttpResponse(f'Пользователь уже существует!')

    return render(request, template_name=r'fifth_task\UserRegister.html', context={'list': list_member})


def sign_up_by_django(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            print(f'Name: {username}')
            print(f'Password: {password}')
            print(f'repeat_password: {repeat_password}')
            print(f'age: {age}')

            if (not username in [list_member[i][0] for i in range(len(list_member))]
                    and (password == repeat_password)
                    and age >= 18):
                return HttpResponse(f'Приветствуем, {username}!')
            elif not password == repeat_password:
                return HttpResponse(f'Пароли не совпадают!')
            elif age < 18:
                return HttpResponse(f'Вы должны быть старше 18!')
            elif username in [list_member[i][0] for i in range(len(list_member))]:
                return HttpResponse(f'Пользователь уже существует!')

    else:
        form = ContactForm()

    return render(request,
                  template_name=r'fifth_task\UserRegister.html',
                  context={'form': form, 'list': list_member})


def choose(request):
    if len(list_member) == 0:
        five_member()
    return render(request, template_name=r'fifth_task\Choose_form.html')
