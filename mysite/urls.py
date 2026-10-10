"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('home/', views.homepageview,name='home'),
#     # path('invoices/', views.invoiceslist,name='invoices'),
#     # path("", views.home),
#     # path("home/",views.show_invoices,name="customer_name"),
#     # path("invoices/",views.invoice,name="invoice"),
#     # path("invoices/",views.create_invoice,name= "create_invoice"),
#     # path("invoices/",views.show_one_invoice,name= "show_one_invoice"),
#     # path("invoices/",views.show_unpaid,name= "show_unpaid"),
#     # path("invoices/",views.mark_as_paid,name= "mark_as_paid"),
#     path('', views.home, name='home'),

#     path(
#         'home/',
#         views.show_invoices,
#         name='all_invoices'
#     ),

#     path(
#         'invoices/',
#         views.invoice,
#         name='invoice'
#     ),

#     path(
#         'invoices/create/',
#         views.create_invoice,
#         name='create_invoice'
#     ),

#     path(
#         'invoices/detail/',
#         views.show_one_invoice,
#         name='show_one_invoice'
#     ),

#     path(
#         'invoices/unpaid/',
#         views.show_unpaid,
#         name='show_unpaid'
#     ),

#     path(
#         'invoices/mark-paid/',
#         views.mark_as_paid,
#         name='mark_as_paid'
#     ),
#     path(
#         "invoice/add/",
#         views.add_invoice,
#         name="add_invoice",
#     ),
# ]






from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("home/", views.show_invoices, name="all_invoices"),
    path("invoices/", views.invoice, name="invoice"),
    path("invoices/create/", views.create_invoice,name="create_invoice"),
    path("invoices/detail/<int:pk>/",views.show_one_invoice, name="show_one_invoice"),
    path("invoices/unpaid/", views.show_unpaid,name="show_unpaid"),
    path("invoices/mark-paid/<int:pk>/",views.mark_as_paid, name="mark_as_paid"),
    path("invoice/add/", views.add_invoice,name="add_invoice"),
    path("invoices/delete/<int:pk>/",views.delete_invoice,name="delete_invoice"),
    path("login/",auth_views.LoginView.as_view(template_name="D:/django/accounts/templates/accounts/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("signup/",accounts_views.signup,name="signup"),
]
