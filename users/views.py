import math
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.views.generic.detail import DetailView
# from django.views.generic import TemplateView
from django.contrib.auth.models import User

from .models import Profile
from recipes.models import Recipe

from .forms import UpdateProfileForm

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recipes = Recipe.objects.filter(author=context['profile']).order_by('-created_at')[:3]
        context['recipes'] = recipes

        return context


class EditProfileView(DetailView):
    model = Profile
    template_name = 'update_profile.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if request.user.username != context['profile'].user.username:
            return redirect('index')
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = UpdateProfileForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save(request.user)
            return redirect('users:profile', format(context['profile'].slug))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        initial = {
            'bio': context['profile'].bio,
            'url': context['profile'].url
        }
        context['update_profile_form'] = UpdateProfileForm(self.request.POST or None, initial=initial)
        return context
