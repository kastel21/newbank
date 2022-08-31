from models import *
from django.forms import ModelForm



class ClientAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientAdminForm, self).__init__(*args, **kwargs)
        # access object through self.instance...
        self.fields['sample'].queryset = Sample.objects.filter(deleted=True)



        
