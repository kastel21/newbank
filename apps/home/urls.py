# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.CubeIndexView.as_view(), name='home'),

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
    path('/remove_sample',views.DeleteSampleView.as_view(), name='remove_sample'),
    path('/view_sample',views.SampleIndexView.as_view(), name='view_sample'),
    re_path(r'^(?P<sampleid>\d+)/detail_sample/$',views.sampleDetails, name='sampleDetails'),
    re_path(r'^(?P<sampleid>\d+)/edit_sample/$',views.UpdateSampleView.as_view(), name='edit_sample'),
    re_path(r'^(?P<sampleid>\d+)/delete_sample/$',views.DeleteSamplesView.as_view(), name='remove_sample'),
    re_path(r'^(?P<sampleid>\d+)/aliquote_sample/$',views.sample_aliquoteDetails, name='aliquote_sample'),


    


    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),






        #**********************stduy urls***********************************************

    re_path(r'^(?P<studyid>\d+)/details/$',views.studyDetails, name='studyDetails'),
    path('/add_study',views.CreateStudyView.as_view(), name='add_study'),
    re_path('view_studies',views.StudyIndexView.as_view(), name='view_studies'),
    re_path(r'^(?P<studyid>\d+)/edit_study/$',views.UpdateStudyView.as_view(), name='edit_study'),
    re_path(r'^(?P<stduyid>\d+)/delete_study/$',views.DeleteStudyView.as_view(), name='remove_study'),






        #**********************cube urls***********************************************

    re_path(r'^(?P<cubeid>\d+)/details_cube/$',views.cubeDetails, name='cubeDetails'),
    # path('/add_study',views.CreateStudyView.as_view(), name='add_study'),
    re_path('view_cubes',views.CubeIndexView.as_view(), name='view_cubes'),
    re_path(r'^(?P<cubeid>\d+)/edit_cube/$',views.UpdateCubeView.as_view(), name='edit_cube'),
    re_path(r'^(?P<cubeid>\d+)/reset_cube/$',views.DeleteStudyView.as_view(), name='reset_cube'),


]
