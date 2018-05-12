from django import forms

class PersonCreateForm(forms.Form):
	FirstName = forms.CharField()
	LastName = forms.CharField()
	Suffix = forms.CharField()
	BadgeNumber = forms.CharField()
	EmailAddress = forms.EmailField()
	Phone = forms.CharField()
	Address = forms.CharField()
	City = forms.CharField()
	State = forms.CharField()
	Zip = forms.CharField()
	ReceiveNewsletter = forms.BooleanField()
	NewsletterFrequencyCode = forms.CharField()
	IsBusiness = forms.BooleanField()
