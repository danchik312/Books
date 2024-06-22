from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
CONTENT = (
    ('Manga', 'Manga'),
    ('Anime', 'Anime'),
    ('Manha', 'Manha'),
    ('Ranobe', 'Ranobe')
)
PHONE = (
    ('Iphone','Iphone')
    ('Samsung', 'Samsung')
    ('Xiaomi', 'Xiaomi')
    ('Another', 'Another')
)


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone =  forms.ChoiceField(choices=PHONE, required=True)
    preferred_content = forms.ChoiceField(choices=CONTENT, required=True)
    phone_number = forms.CharField(required=True)
    years_of_exp = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = models.AnimeFan
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'years_of_exp',
            'gender',
            'phone_number',
            'preferred_content',
            'phone'
        )

    def save(self, commit=True):
        fan = super(CustomRegistrationForm, self).save(commit=True)
        fan.email = self.cleaned_data['email']
        if commit:
            fan.save()
        return fan


@receiver(post_save, sender=models.AnimeFan)
def set_club(sender, instance, created, **kwargs):
    if created:
        print('Ура пользовтель зарегался')
        years_of_exp = instance.years_of_exp
        if years_of_exp < 1:
            instance.rank = 'начинающий'
        elif years_of_exp >= 1 and years_of_exp <= 10:
            instance.rank = 'новичок'
        elif years_of_exp >= 11 and years_of_exp <= 18:
            instance.rank = 'профи'
        elif years_of_exp >= 18 and years_of_exp <= 80:
            instance.rank = 'олд'
        else:
            instance.rank = 'Ранг не определен'
        instance.save()