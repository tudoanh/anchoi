from django import forms


class EmailForm(forms.Form):
    CITY_CHOICES = (
        ('HN', 'Hà Nội'),
        ('SG', 'Sài Gòn'),
        ('ALL', 'Toàn bộ')
    )
    email = forms.EmailField()
    city = forms.ChoiceField(choices=CITY_CHOICES, initial='ALL')

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()
