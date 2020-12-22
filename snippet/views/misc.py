from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'snippet/misc/about.html'


class ClientView(TemplateView):
    template_name = 'snippet/misc/clients.html'


class ContactsView(TemplateView):
    template_name = 'snippet/misc/contact.html'