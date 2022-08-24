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


class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','id','study','age')


admin.site.register(Patient,PatientAdmin)

