from django.urls import path


from . import views

app_name = 'users'

urlpatterns = [
        path('edit/<slug:slug>', views.EditProfileView.as_view(), name='edit_profile'),
    path('<slug:slug>', views.ProfileView.as_view(), name='profile' ),
]


