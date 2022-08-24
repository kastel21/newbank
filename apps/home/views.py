# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .mixins import LoginRequired, AuthorshipRequired
from django.views.generic import CreateView, View, ListView, DetailView, UpdateView
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


from datetime import date
from datetime import datetime

def age(birthdate):

    date_str = birthdate.split("T")[0]

    dto = datetime.strptime(date_str, '%Y-%m-%d').date()

    today = date.today()
    age = today.year - dto.year - ((today.month, today.day) < (dto.month, dto.day))
    return age

class CreatePatientView(LoginRequired, CreateView):
    template_name = 'patients/create_patient.html'
    model = Patient
    fields = ['name', 'gender','study','dob']

    def form_valid(self, form):
        form.instance.age = age(form.instance.dob)
        # form.instance.createdby_email = self.request.user.email
        # form.instance.assignto_email = self.get_email(form.instance.assignto)

        return super(CreatePatientView, self).form_valid(form)



    def get_email(self,username):
        email = User.objects.get(username = username).email
        return email

    def get_success_url(self):
        return reverse('home')

class DeletePatientView(LoginRequired, AuthorshipRequired, DeleteView):
    template_name = 'patients/create_patient.html'
    model = Patient
    pk_url_kwarg = 'taskid'

    def get_success_url(self):
        return reverse_lazy('home')



class PatientIndexView(LoginRequired,ListView):
    model = Patient
    context_object_name = 'questions'
    template_name = 'home/patients.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PatientIndexView, self).get_context_data(*args, **kwargs)
        patient_list = Patient.objects.all().order_by('-_id')
        paginator = Paginator(patient_list, 6)

        page = self.request.GET.get('page')
        try:
            patients = paginator.page(page)
        except PageNotAnInteger:
            patients = paginator.page(1)
        except EmptyPage:
            patients = paginator.page(paginator.num_pages)

        context['allpatients'] = True
        context['patients'] = patients
        context['total'] = patient_list.count()

        return context




class PatientView(PatientIndexView,LoginRequired):

    def get_context_data(self, *args, **kwargs):
        context = super(PatientIndexView, self).get_context_data(*args, **kwargs)
        patient_list = Patient.objects.filter(Q( assignto = self.request.user) | Q(createdby=self.request.user) )
        paginator = Paginator(patient_list, 6)

        page = self.request.GET.get('page')
        try:
            tasks = paginator.page(page)
        except PageNotAnInteger:
            tasks = paginator.page(1)
        except EmptyPage:
            tasks = paginator.page(paginator.num_pages)

        context['patients'] = tasks
        context['patientTabActive'] = True
        context['total'] = patient_list.count()

        return context