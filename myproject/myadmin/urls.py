"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from myadmin import views
from .views import *

urlpatterns = [
    path('pdf/', GeneratePdf.as_view()),
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.login, name='login'),
    path('admin_login_check', views.admin_login_check, name='admin_login_check'),
    
    path('agency', views.agency, name='agency'),
    path('agency_viewmore/<int:id>', views.agency_viewmore, name='agency_viewmore'),


    path('inquiry', views.inquiry, name='inquiry'),
    path('feedback', views.feedback, name='feedback'),
    path('customer', views.customer, name='customer'),
    path('customer_viewmore/<int:id>', views.customer_viewmore, name='customer_viewmore'),
    path('order', views.order, name='order'),
    path('logout', views.logout, name='logout'),
    
    
    path('inquiry_read', views.inquiry_read, name='inquiry_read'),
    path('inquiry_delete/<int:id>', views.inquiry_delete, name='inquiry_delete'),
    path('order_viewmore/<int:id>', views.order_viewmore, name='order_viewmore'),
    path('feedback_delete/<int:id>', views.feedback_delete, name='feedback_delete'),

    path('admin_order', views.admin_order, name='admin_order'),
    path('approve/<int:id>', views.approve, name='approve'),
    path('reject/<int:id>', views.reject, name='reject'),

    path('ChangePassword', views.ChangePassword, name='ChangePassword'),
    path('ChangePassword_chk', views.ChangePassword_chk, name='ChangePassword_chk'),

    path('ForgetPassword', views.ForgetPassword, name='ForgetPassword'),
    path('ForgetPassword_chk', views.ForgetPassword_chk, name='ForgetPassword_chk'),
       


]
