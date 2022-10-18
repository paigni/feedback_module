from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from contact_form.forms import ContactForm


class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('success_page')
    form_class = ContactForm
    template_name = 'contact_form.html'

    def form_valid(self, form):
        """
        Проверка корректности выбора пользователя
        Args:
            form:форма приложения
        Returns:
            Перенаправление на success
        """
        data = form.data
        return super().form_valid(form)



def success(request):
   return HttpResponse('Письмо отправлено!')
   