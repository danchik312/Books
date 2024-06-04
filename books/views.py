from django.http import HttpResponse
from datetime import datetime
import random

def personal_info(request):
    name = "Даниэль"
    surname = "Кемелов"
    age = 17
    return HttpResponse(f"Имя: {name}, Фамилия: {surname}, Возраст: {age}")

def hobbies(request):
    hobbies_list = "хобби: Чтение манг, Программирование, Спорт"
    return HttpResponse(hobbies_list)

def current_time(request):
    now = datetime.now().strftime("%H:%M:%S")
    return HttpResponse(f"Текущее время: {now}")

def random_numbers(request):
    numbers = [random.randint(1, 100) for _ in range(5)]
    return HttpResponse(f"Рандомные числа: {', '.join(map(str, numbers))}")

def home(request):
    return HttpResponse("Добро пожаловать на главную страницу!")

