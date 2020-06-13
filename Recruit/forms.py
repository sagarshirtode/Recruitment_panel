from django import forms
from Recruit.models import requirement_statistics

class requirement_statisticsForm(forms.ModelForm):
    class Meta:
        model = requirement_statistics
        fields = "__all__"