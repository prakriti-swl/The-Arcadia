from django import forms
from arcadia_app.models import  Contact



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


# class NewsletterForm(forms.ModelForm):
#     class Meta:
#         model = Newsletter
#         fields = "__all__"