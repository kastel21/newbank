# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    #**********************patient urls***********************************************

    re_path(r'^(?P<patientid>\d+)/detail/$',views.patientDetails, name='patientDetails'),
    path('/add_patient',views.CreatePatientView.as_view(), name='add_patient'),
    # path('/remove_patient',views.DeletePatientView.as_view(), name='remove_patient'),
    path('/view_patients',views.PatientIndexView.as_view(), name='view_patients'),
    # path('/edit_patient',views.UpdatePatientView.as_view(), name='edit_patient'),
    re_path(r'^(?P<patientid>\d+)/edit/$',views.UpdatePatientView.as_view(), name='edit_patient'),
    re_path(r'^(?P<patientid>\d+)/delete/$',views.DeletePatientView.as_view(), name='remove_patient'),

    #**********************sample urls***********************************************
    path('/add_sample',views.CreateSampleView.as_view(), name='add_sample'),




    #**********************stduy urls***********************************************

    path('/add_study',views.CreateStudyView.as_view(), name='add_study'),
    path('/view_studies',views.StudyIndexView.as_view(), name='view_studies'),


    #**********************sample urls***********************************************
    path('/add_sample',views.CreateSampleView.as_view(), name='add_sample'),
    path('/remove_sample',views.DeleteSampleView.as_view(), name='remove_sample'),
    path('/view_sample',views.SampleIndexView.as_view(), name='view_sample'),

    path('/remove_study',views.StudyIndexView.as_view(), name='remove_study'),



    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
