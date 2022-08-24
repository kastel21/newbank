
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
from django.db.models import Q
from django.shortcuts import render, get_object_or_404





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
        form.instance.age = self.age(form.instance.dob)
        # form.instance.createdby_email = self.request.user.email
        # form.instance.assignto_email = self.get_email(form.instance.assignto)

        return super(CreatePatientView, self).form_valid(form)



    def get_email(self,username):
        email = User.objects.get(username = username).email
        return email

    def get_success_url(self):
        return reverse('home')

    def age(self,birthDate ):
        from datetime import date
        from datetime import datetime

        dt_obj = datetime.strptime(birthDate.split("T")[0], '%Y-%m-%d').date()

        today = date.today()
        age = today.year - dt_obj.year -((today.month, today.day) < (dt_obj.month, dt_obj.day))
    
        return age
    

class DeletePatientView(LoginRequired, AuthorshipRequired, DeleteView):
    template_name = 'patients/create_patient.html'
    model = Patient
    pk_url_kwarg = 'taskid'

    def get_success_url(self):
        return reverse_lazy('home')

# **************************sample view******************************************
class CreateSampleView(LoginRequired, CreateView):
    template_name = 'samples/create_sample.html'
    model = Sample
    fields = ['patient', 'study', 'type','date_of_archive']

    def form_valid(self, form):
        # form.instance.createdby = self.request.user
        # form.instance.createdby_email = self.request.user.email
        # form.instance.assignto_email = self.get_email(form.instance.assignto)

        return super(CreateSampleView, self).form_valid(form)

    def get_form(self, obj=None, **kwargs):
        form = super(CreateSampleView, self).get_form( obj, **kwargs)
        form.base_fields['study'].label_from_instance = lambda inst: "{} {}".format(inst.date_of_archive, inst.study)
        return form

    # def get_email(self,username):
    #     email = User.objects.get(username = username).email
    #     return email

    def get_success_url(self):
        return reverse('home')

# class DeletePatientView(LoginRequired, AuthorshipRequired, DeleteView):
#     template_name = 'patients/create_patient.html'
#     model = Patient
#     pk_url_kwarg = 'taskid'

#     def get_success_url(self):
#         return reverse_lazy('home')



class PatientIndexView(LoginRequired,ListView):
    model = Patient
    context_object_name = 'questions'
    template_name = 'home/patients.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PatientIndexView, self).get_context_data(*args, **kwargs)
        patient_list = Patient.objects.all().order_by('-id')
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



#methods and classes for studies

class CreateStudyView(LoginRequired, CreateView):
    template_name = 'studies/create_study.html'
    model = Study
    fields = ['name', 'narrative_name','status']

    def form_valid(self, form):
        # form.instance.age = age(form.instance.dob)
        # form.instance.createdby_email = self.request.user.email
        # form.instance.assignto_email = self.get_email(form.instance.assignto)

        return super(CreateStudyView, self).form_valid(form)



    def get_email(self,username):
        email = User.objects.get(username = username).email
        return email

    def get_success_url(self):
        return reverse('home')

class DeleteStudyView(LoginRequired, AuthorshipRequired, DeleteView):
    template_name = 'patients/create_patient.html'
    model = Patient
    pk_url_kwarg = 'taskid'

    def get_success_url(self):
        return reverse_lazy('home')



class StudyIndexView(LoginRequired,ListView):
    model = Study
    context_object_name = 'questions'
    template_name = 'home/studies.html'

    def get_context_data(self, *args, **kwargs):
        context = super(StudyIndexView, self).get_context_data(*args, **kwargs)
        study_list = Study.objects.all().order_by('-_id')
        paginator = Paginator(study_list, 6)

        page = self.request.GET.get('page')
        try:
            studies = paginator.page(page)
        except PageNotAnInteger:
            studies = paginator.page(1)
        except EmptyPage:
            studies = paginator.page(paginator.num_pages)

        context['allstudies'] = True
        context['studies'] = studies
        context['total'] = study_list.count()

        return context




class StudyView(PatientIndexView,LoginRequired):

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








#*******************show Patient******************************************************************


def patientDetails(request,patientid):
    patient = get_object_or_404(Patient, id=patientid)
    context={'patient':patient}

    context['PatientTabActive'] = True
    



    return render(request, 'patients/view_patient.html', context)


#*******************Update Patient******************************************************************
class UpdatePatientView(LoginRequired, AuthorshipRequired, UpdateView):
    template_name = 'patients/edit_patient.html'
    model = Patient
    pk_url_kwarg = 'patientid'
    fields = ['name','phone','study','dob']

    def get_success_url(self):
        patient = self.get_object()
        return reverse('patientDetails', kwargs={'patientid': patient.pk})


#*******************delete Patient******************************************************************

class DeleteTaskView(LoginRequired, AuthorshipRequired, DeleteView):
    template_name = 'patients/delete_patient.html'
    model = Patient
    pk_url_kwarg = 'patientid'

    def get_success_url(self):
        return reverse_lazy('view_patients')
