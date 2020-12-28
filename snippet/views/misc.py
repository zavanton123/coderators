import logging

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView

from snippet.forms.feedback import FeedbackForm

log = logging.getLogger(__name__)


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


def choose_language(request):
    context = {
        'redirect_to': reverse('snippet:home')
    }
    return render(request, 'snippet/misc/language_choice.html', context=context)
