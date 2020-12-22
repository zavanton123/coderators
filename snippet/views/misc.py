import logging

from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from snippet.forms.contacts import ContactForm

log = logging.getLogger(__name__)


class AboutView(TemplateView):
    template_name = 'snippet/misc/about.html'


class ClientView(TemplateView):
    template_name = 'snippet/misc/clients.html'


class ContactsView(FormView):
    template_name = 'snippet/misc/contact.html'
    success_url = reverse_lazy('snippet:home')
    form_class = ContactForm

    def form_valid(self, form):
        if form.is_valid():
            log.debug("form is valid")
        return super().form_valid(form)
