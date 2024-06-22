from django.contrib import admin
from . import models


admin.site.register(models.Books_list)
admin.site.register(models.ReviewsBooks)
admin.site.register(models.Tag)
admin.site.register(models.Products)
admin.site.register(models.Quote)
