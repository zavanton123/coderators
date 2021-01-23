import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from authentication.user_forms import UpdateUserForm, SetAvatarForm

log = logging.getLogger(__name__)


class ViewUser(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('snippet:login')
    redirect_field_name = 'redirect_to'
    template_name = 'authentication/user/view_user.html'


class UpdateUser(View):
    def get(self, request, *args, **kwargs):
        current_user_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'experience': request.user.experience,
            'description': request.user.description,
        }
        form = UpdateUserForm(current_user_data)
        return render(request, 'authentication/user/update_user.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.experience = form.cleaned_data['experience']
            request.user.description = form.cleaned_data['description']
            request.user.save()
            return redirect('snippet:view_user')
        return render(request, 'authentication/user/update_user.html', {'form': form})


class SetAvatar(View):
    def get(self, request, *args, **kwargs):
        form = SetAvatarForm()
        return render(request, 'authentication/user/set_avatar.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SetAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['avatar']
            if image:
                request.user.avatar = image
                request.user.save()
            return redirect('snippet:view_user')
        return render(request, 'authentication/user/set_avatar.html', {'form': form})