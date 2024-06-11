from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator




class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=110)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Books_list(models.Model):

    BOOK_STATUS = (
        ('Онгоинг', 'Онгоинг'),
        ('Анонс', 'Анонс'),
        ('Завершен', 'Завершен'),
        ('Приостановлен', 'Приостановлен'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(default='@gmail.com')
    image = models.ImageField(upload_to='images/')
    about_bk = models.TextField()
    book_status = models.CharField(max_length=100, choices=BOOK_STATUS, null=True)
    description = models.FileField(upload_to='descriptions/')
    date_of_issue = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.book_status}'

    class Meta:
        verbose_name = 'произведение'
        verbose_name_plural = 'произведения'

class ReviewsBooks(models.Model):
    reviews_bk = models.ForeignKey(Books_list, on_delete=models.CASCADE,
                                    related_name='reviews_books')
    text = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.stars}-{self.reviews_bk}'