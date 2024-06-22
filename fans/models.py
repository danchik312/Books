from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class AnimeFan(User):

    GENDER = (("Male", "Male"), ("Female", "Female"))

    CONTENT = (
        ("Manga", "Manga"),
        ("Anime", "Anime"),
        ("Manha", "Manha"),
        ("Ranobe", "Ranobe"),
    )
    PHONE = (
        ("Iphone", "Iphone"),
        ("Samsung", "Samsung"),
        ("Xiaomi", "Xiaomi"),
        ("Another", "Another"),
    )

    phone_number = models.CharField(max_length=14, default="+996")
    years_of_exp = models.PositiveIntegerField(
        default=18, validators=[MaxValueValidator(99), MinValueValidator(5)]
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    bio = models.FileField(
        upload_to="media/biography/",
        verbose_name="Загрузите свою биографию",
        null=True,
        blank=True,
    )
    birth_date = models.DateField(verbose_name="Укажите дату рождения", null=True)
    phone = models.CharField(max_length=100, choices=CONTENT)
    image = models.ImageField(
        upload_to="images/", verbose_name="Загрузите ваше фото", null=True
    )

    preferred_content = models.CharField(
        max_length=100,
        choices=CONTENT,
        verbose_name="Укажите предпочитаемый контент",
        null=True,
    )
    rank = models.CharField(max_length=50, default="Ранг не определен")


@receiver(post_save, sender=AnimeFan)
def set_rank(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан успешно пользователь зарегистрировался")
        years_of_exp = instance.years_of_exp
        if years_of_exp < 1:
            instance.rank = "новичок"
        elif years_of_exp >= 1 and years_of_exp <= 10:
            instance.rank = "любитель"
        elif years_of_exp >= 11 and years_of_exp <= 18:
            instance.rank = "профи"
        elif years_of_exp >= 18 and years_of_exp <= 80:
            instance.rank = "олд"
        else:
            instance.rank = "Ранг не определен"
        instance.save()
