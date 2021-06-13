from django import forms
from .models import Profile
import os

class UpdateProfileForm(forms.Form):
    bio=forms.CharField(
        label='Biography',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'biography',
            'placeholder': 'Enter your biography'
            }
        )
    )
    url = forms.URLField(
        required=False,
        label='Website',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'url',
            'placeholder': 'Website'
        })
    )

    image = forms.ImageField(
        required=False,
    )

    def save(self, user):
        profile = Profile.objects.get(user=user)
        profile.bio = self.cleaned_data.get('bio')
        profile.url = self.cleaned_data.get('url')
        if self.cleaned_data.get('image'):
            if profile.image:
                try:
                    os.remove(os.path.dirname(__file__) + '/..' + profile.image.url)
                except:
                    pass
            profile.image = self.cleaned_data.get('image')
        profile.save()


