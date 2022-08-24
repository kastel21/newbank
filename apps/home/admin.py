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
<<<<<<< HEAD
    list_display = ('id','study','type','date_of_archive', 'patient')
=======
    list_display = ('study','id','type','date_of_archive', 'patient')
>>>>>>> 2676a532b90341dc86777e32d7f9ed95f2c8c1fc
admin.site.register(Sample, Sample_Admin)

# class PatientAdmin(admin.ModelAdmin):
#     list_display = ('name','_id','study')

#     def get_form(self, request, obj=None, **kwargs):
#         form = super(PatientAdmin, self).get_form(request, obj, **kwargs)
#         form.base_fields['study'].label_from_instance = lambda inst: "{} {}".format(inst._id, inst.name)
#         return form
# admin.site.register(Patient,PatientAdmin)

# admin.site.register(Patient,AuthorAdmin)
<<<<<<< HEAD

=======
# @admin.register(Patient)
# class TaskAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
#         if db_field.name == "user":
#             formfield.label_from_instance = lambda obj: f'{obj.first_name} ({obj.last_name})'
#         return formfield
>>>>>>> 2676a532b90341dc86777e32d7f9ed95f2c8c1fc

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','id','study','age')
admin.site.register(Patient,PatientAdmin)


