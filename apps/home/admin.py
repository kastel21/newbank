# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from . models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','_id')

    def get_form(self, request, obj=None, **kwargs):
        form = super(AuthorAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['name'].label_from_instance = lambda inst: "{} {}".format(inst._id, inst.name)
        return form
admin.site.register(Study,AuthorAdmin)


# class PatientAdmin(admin.ModelAdmin):
#     list_display = ('name','_id','study')

#     def get_form(self, request, obj=None, **kwargs):
#         form = super(PatientAdmin, self).get_form(request, obj, **kwargs)
#         form.base_fields['study'].label_from_instance = lambda inst: "{} {}".format(inst._id, inst.name)
#         return form
# admin.site.register(Patient,PatientAdmin)

# admin.site.register(Patient,AuthorAdmin)
@admin.register(Patient)
class TaskAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "user":
            formfield.label_from_instance = lambda obj: f'{obj.first_name} ({obj.last_name})'
        return formfield