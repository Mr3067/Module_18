"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task5.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('class/', index),
    # # path('func/', index2.as_view()),
    # path('func/', TemplateView.as_view(template_name='func_view.html')),
    # path('', TemplateView.as_view(template_name='main_pg.html'))

    # path('', TemplateView.as_view(template_name=r'fourth_task\task4_main.html')),
    # # path('', TemplateView.as_view(template_name=r'fourth_task\menu.html')),
    # path('shop/', TemplateView.as_view(template_name=r'fourth_task\task4_depend1.html')),
    # path('recycle/', TemplateView.as_view(template_name=r'fourth_task\task4_depend2.html'))

    path('html_form/', sign_up_by_html),
    path('dj_form/', sign_up_by_django),
    path('', choose)

]
