from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe


# def validate_comma(value):
#     if "," in value:
#         raise forms.ValidationError("Check if comma is entered in the form")
#
#
# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=200, required=False)
#     last_name = forms.CharField(max_length=200, validators=[validate_comma])
#     your_email = forms.EmailField(max_length=200)
#     message = forms.CharField(max_length=300)
#
#     # def clean_first_name(self):
#     #     data = self.cleaned_data['first_name']
#     #     if "," in data:
#     #         raise forms.ValidationError("Invalid First Name")
#     #     return data

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        exclude = ('message',)
        # fields = '__all__'
        labels = {
            'first_name': _('Enter First Name'),
            'last_name': _('Enter Last Name'),
            'email': _('Enter Email')
        }
        # help_texts = {
        #     'first_name': _('Enter characters only')
        #
        # }
