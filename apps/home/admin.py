# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from . models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','id')

    def get_form(self, request, obj=None, **kwargs):
        form = super(AuthorAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['name'].label_from_instance = lambda inst: "{} {}".format(inst._id, inst.name)
        return form
admin.site.register(Study,AuthorAdmin)

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('patient','study','_id')

#     def get_form(self, request, obj=None, **kwargs):
#         form = super(AuthorAdmin, self).get_form(request, obj, **kwargs)
#         form.base_fields['patient'].label_from_instance = lambda inst: "{} {}".format(inst._id, inst.patient)
#         return form
# admin.site.register(Sample,AuthorAdmin)

class Sample_Admin(admin.ModelAdmin):
    list_display = ('id','study','type','date_of_archive', 'patient')
admin.site.register(Sample, Sample_Admin)

# class PatientAdmin(admin.ModelAdmin):
#     list_display = ('name','_id','study')

#     def get_form(self, request, obj=None, **kwargs):
#         form = super(PatientAdmin, self).get_form(request, obj, **kwargs)
#         form.base_fields['study'].label_from_instance = lambda inst: "{} {}".format(inst._id, inst.name)
#         return form
# admin.site.register(Patient,PatientAdmin)

# admin.site.register(Patient,AuthorAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','id','study','age')


admin.site.register(Patient,PatientAdmin)


