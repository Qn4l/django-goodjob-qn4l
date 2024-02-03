from django.urls import path

from . import views

urlpatterns = (path('', views.job_list_homepage_view, name='job_list_home'),
               path('<ids>/', views.job, name='jobs_detail'),
               # path('<str:ids>/', views.job, name='jobs_detail'),
               )
