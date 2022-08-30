from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..      *Required',
			'class': 'form-control'
			}))
 
	subject = forms.CharField(max_length=300, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Subject..      *Required',
			'class': 'form-control'
			}))
 
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..      *Required',
			'class': 'form-control'
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..      *Required',
			'class': 'form-control',
			'rows': 6,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'subject', 'email', 'message',)