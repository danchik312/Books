from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms, models, middlewares


# register
class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = 'fans/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        years_of_exp = form.cleaned_data['years_of_exp']
        if years_of_exp < 1:
            self.object.rank = 'начинающий'
        elif 5 <= years_of_exp <= 10:
            self.object.rank = 'новичок'
        elif 11 <= years_of_exp <= 18:
            self.object.rank = 'профи'
        elif 18 <= years_of_exp <= 80:
            self.object.rank = 'олд'
        else:
            self.object.rank = 'Ранг не определен'
        self.object.save()
        return response


# authorization
class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'fans/login.html'

    def get_success_url(self):
        return reverse('fans:fan_list')


# Logout
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('fans:login')


class FanListView(ListView):
    template_name = 'fans/fan_list.html'
    model = models.AnimeFan

    def get_queryset(self):
        return models.AnimeFan.objects.filter().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rank'] = getattr(self.request, 'rank', 'Ранг не определен')
        return context