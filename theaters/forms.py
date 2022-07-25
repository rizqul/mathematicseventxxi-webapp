from django import forms

from .models import JawabanTheaterModel


class JawabanTheaterForm(forms.Form):
    jawaban = forms.CharField(widget=forms.Textarea)


# class JawabanTheaterForm(forms.ModelForm):
#     class Meta:
#         model = JawabanTheaterModel
#         exclude = ['exam_code', 'nama_peserta']

#         widgets = {
#             'jawaban0': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'jawaban1': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'jawaban2': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'jawaban3': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'jawaban4': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'jawaban5': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'jawaban6': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'jawaban7': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'jawaban8': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'jawaban9': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),

#         }
