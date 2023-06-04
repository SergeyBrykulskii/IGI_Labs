from django import forms
from .models import GymMembership

class GymMembershipForm(forms.ModelForm):
    class Meta:
        model = GymMembership
        fields = ['name', 'description', 'cost']