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
    list_display = ('study','id','type','date_of_archive', 'patient')

admin.site.register(Sample, Sample_Admin)

# class PatientAdmin(admin.ModelAdmin):
#     list_display = ('name','_id','study')

#     def get_form(self, request, obj=None, **kwargs):
#         form = super(PatientAdmin, self).get_form(request, obj, **kwargs)
#         form.base_fields['study'].label_from_instance = lambda inst: "{} {}".format(inst._id, inst.name)
#         return form
# admin.site.register(Patient,PatientAdmin)

# admin.site.register(Patient,AuthorAdmin)

# @admin.register(Patient)
# class TaskAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
#         if db_field.name == "user":
#             formfield.label_from_instance = lambda obj: f'{obj.first_name} ({obj.last_name})'
#         return formfield

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','id','study','age')
admin.site.register(Patient,PatientAdmin)

class FreezerAdmin(admin.ModelAdmin):
    list_display = ('name','id','capacity')
admin.site.register(Freezer,FreezerAdmin)

class RackAdmin(admin.ModelAdmin):
    list_display = ('shelf','name','capacity')
admin.site.register(Rack,RackAdmin)

class ShelfAdmin(admin.ModelAdmin):
    list_display = ('freezer','name','capacity')
admin.site.register(Shelf,ShelfAdmin)

class CubeAdmin(admin.ModelAdmin):
    list_display = ('box','name')
    def get_form(self, request, obj=None, **kwargs):
        form = super(CubeAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['sample'].queryset = Sample.objects.filter(deleted=True)
        return form
    # def render_change_form(self, request, context, *args, **kwargs):
    #      context['adminform'].form.fields['theme'].queryset = Theme.objects.filter(name__iexact='company')
    #      return super(CompanyAdmin, self).render_change_form(request, context, *args, **kwargs)
admin.site.register(Cube,CubeAdmin)

class BoxAdmin(admin.ModelAdmin):
    list_display = ('rack','name','capacity')


admin.site.register(Box,BoxAdmin)