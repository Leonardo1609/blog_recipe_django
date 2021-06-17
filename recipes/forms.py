from django import forms
from categories.models import Category
from .models import Recipe

def categories_in_tuple():
    return (('', '--Seleccionar--' ), *[ (category.pk, category.name) for category in Category.objects.all() ])

class RecipeForm(forms.Form):
    title = forms.CharField(
            required=True, 
            min_length=6, 
            max_length=50, 
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'title',
                'placeholder': 'Enter the title here'
            })
    )
    category = forms.ChoiceField(
            required=True,
            choices = categories_in_tuple(),
            widget = forms.Select(attrs={
                'class': 'form-select',
                'id': 'category',
            })
    )

    image = forms.ImageField(
            required=False,
    )

    ingredientes = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'ingredients',
            'placeholder': 'Enter the ingredients here'
        })
    )
    preparation = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'preparation',
            'placeholder': 'Enter the preparation here'
        })
    )
    
    def save(self, author):
        category = Category.objects.get(pk=self.cleaned_data.get('category'))
        
        Recipe.objects.create(
            title=self.cleaned_data.get('title'),
            category=category,
            author=author,
            image=self.cleaned_data.get('image'),
            preparation=self.cleaned_data.get('preparation'),
            ingredients=self.cleaned_data.get('ingredientes')
        )
