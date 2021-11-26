from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect


class ContactView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'contact/contact.html'
    success_message = "Mesajınız başarıyla gönderildi.!"

    def form_invalid(self, form):
        messages.error(self.request, 'Gönderiminizle ilgili bir sorun oluştu. Lütfen tekrar deneyin.')
        return HttpResponseRedirect('/iletisim')