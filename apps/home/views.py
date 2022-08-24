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