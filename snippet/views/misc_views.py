from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import activate
from django.views import View
from django.views.generic import TemplateView, FormView

from coderators import settings
from snippet.forms.feedback_forms import FeedbackForm
from snippet.forms.language_forms import ChooseLanguageForm


class AboutView(TemplateView):
    template_name = 'snippet/misc/about.html'


class ClientView(TemplateView):
    template_name = 'snippet/misc/clients.html'


class SendFeedback(FormView):
    template_name = 'snippet/misc/send_feedback.html'
    success_url = reverse_lazy('snippet:home')
    form_class = FeedbackForm

    def form_valid(self, form):
        if form.is_valid():
            content = form.cleaned_data['content']
            from_email = form.cleaned_data['email']

            mail = send_mail(
                subject=(form.cleaned_data['subject']),
                message=f'Message from {from_email}, content: {content}',
                from_email=from_email,
                recipient_list=['zavanton@yandex.ru'],
                fail_silently=False
            )

            if mail:
                messages.success(self.request, 'Your feedback is successfully sent!')
                return redirect('snippet:home')
            else:
                messages.error(self.request, 'Failed to send your feedback... Try again!')

        return super().form_valid(form)


class ChooseLanguage(View):
    def get(self, request, *args, **kwargs):
        form = ChooseLanguageForm()
        return render(request, 'snippet/misc/language_choice.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ChooseLanguageForm(request.POST)
        if form.is_valid():
            selected_language = form.cleaned_data['language']
            activate(selected_language)
            response = redirect('snippet:home')
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, selected_language)
            return response
        return render(request, 'snippet/misc/language_choice.html', {'form': form})
