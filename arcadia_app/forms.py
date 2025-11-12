from django import forms
from arcadia_app.models import  Contact, Newsletter, Comment, Reservation



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'phone': forms.TextInput(attrs={'required': True}),
            'message': forms.Textarea(attrs={'required': True}),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'email', 'date', 'time', 'people']
        widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'time': forms.TimeInput(attrs={'type': 'time'}),
        }













# TIME_CHOICES = [
#     ('9:00 AM','9:00 AM'), ('9:30 AM','9:30 AM'), ('10:00 AM','10:00 AM'),
#     ('10:30 AM','10:30 AM'), ('11:00 AM','11:00 AM'), ('11:30 AM','11:30 AM'),
#     ('12:00 PM','12:00 PM'), ('12:30 PM','12:30 PM'), ('1:00 PM','1:00 PM'),
#     ('1:30 PM','1:30 PM'), ('2:00 PM','2:00 PM'), ('2:30 PM','2:30 PM'),
#     ('3:00 PM','3:00 PM'), ('3:30 PM','3:30 PM'), ('4:00 PM','4:00 PM'),
#     ('4:30 PM','4:30 PM'), ('5:00 PM','5:00 PM'), ('5:30 PM','5:30 PM'),
#     ('6:00 PM','6:00 PM'), ('6:30 PM','6:30 PM'), ('7:00 PM','7:00 PM'),
#     ('7:30 PM','7:30 PM'), ('8:00 PM','8:00 PM'), ('8:30 PM','8:30 PM'),
#     ('9:00 PM','9:00 PM'), ('9:30 PM','9:30 PM'), ('10:00 PM','10:00 PM'),
#     ('10:30 PM','10:30 PM'), ('11:00 PM','11:00 PM'),
# ]

# PEOPLE_CHOICES = [(f"{i} person" if i==1 else f"{i} people", f"{i} person" if i==1 else f"{i} people") for i in range(1,13)]

# class ReservationForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ['date', 'time', 'people', 'name', 'phone', 'email']
#         widgets = {
#             'date': forms.DateInput(attrs={
#                 'type': 'date',
#                 'class': 'my-calendar bo-rad-10 sizefull txt10 p-l-20',
#                 'placeholder': 'mm/dd/yyyy'
#             }),
#             'time': forms.Select(choices=TIME_CHOICES, attrs={
#                 'class': 'selection-1 bo-rad-10 sizefull txt10 p-l-20'
#             }),
#             'people': forms.Select(choices=PEOPLE_CHOICES, attrs={
#                 'class': 'selection-1 bo-rad-10 sizefull txt10 p-l-20'
#             }),
#             'name': forms.TextInput(attrs={
#                 'class': 'bo-rad-10 sizefull txt10 p-l-20',
#                 'placeholder': 'Name'
#             }),
#             'phone': forms.TextInput(attrs={
#                 'class': 'bo-rad-10 sizefull txt10 p-l-20',
#                 'placeholder': 'Phone'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'bo-rad-10 sizefull txt10 p-l-20',
#                 'placeholder': 'Email'
#             }),
#         }