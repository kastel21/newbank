# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('/add_patient',views.CreatePatientView.as_view(), name='add_patient'),
    path('/remove_patient',views.DeletePatientView.as_view(), name='remove_patient'),
    path('/view_patients',views.PatientIndexView.as_view(), name='view_patients'),




    path('/view_studies',views.StudyIndexView.as_view(), name='view_studies'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
