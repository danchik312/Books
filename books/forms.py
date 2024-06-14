from django import forms
from . import models


class Books_list_Form(forms.ModelForm):
    class Meta:
        model = models.Books_list
        fields = "__all__"
 18 changes: 18 additions & 0 deletions18