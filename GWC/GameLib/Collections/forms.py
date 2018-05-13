from django import forms

from .models import Person, Boardgame, Collection

class PersonCreateForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = [
			'FirstName',
			'LastName',
			'Suffix',
			'BadgeNumber',
			'EmailAddress',
			'Phone',
			'Address',
			'City',
			'State',
			'Zip',
			'ReceiveNewsletter',
			'NewsletterFrequencyCode',
			'IsBusiness',
		]


	def clean_FirstName(self):
		FirstName = self.cleaned_data.get("FirstName")
		if FirstName == "Hello":
			raise forms.ValidationError("Not a valid name")
		return FirstName