from django.db import models

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
    about_emp = models.TextField()
    book_status = models.CharField(max_length=100, choices=BOOK_STATUS, null=True)
    rezume = models.FileField(upload_to='rezume/')
    date_of_issue = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.book_status}'

    class Meta:
        verbose_name = 'произведение'
        verbose_name_plural = 'произведения'
