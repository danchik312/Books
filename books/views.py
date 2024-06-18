from django.http import HttpResponse
from datetime import datetime
import random
from django.views import generic
class SearchView(generic.ListView):
    template_name = 'books/Book_List.html'
    context_object_name = 'bk'
    paginate_by = 5

    def get_queryset(self):
        return models.Books_list.objects.filter(name__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

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


# def Book_Detail_view(request, id):
#     if request.method == "GET":
#         bk_id = get_object_or_404(models.Books_list, id=id)
#         return render(
#             request,
#             template_name="books/Book_Detail.html",
#             context={
#                 "bk_id": bk_id
#             }
#         )


# def Book_List_view(request):
#     if request.method == 'GET':
#         queryset = models.Books_list.objects.filter().order_by('-id')
#         return render(
#             request,
#             template_name='books/Book_List.html',
#             context={
#                 'bk': queryset
#             }
#         )

class BooksListView(generic.ListView):
    template_name = 'books/Book_List.html'
    context_object_name = 'bk'
    model = models.Books_list
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quote'] = models.Quote.objects.order_by('-id')
        return context

def books_tags_view(request):
    if request.method == 'GET':
        teen_tags = models.Products.objects.filter(tags__name='Подростковый').order_by('-id')
        return render(
            request,
            template_name='products/books_tags.html',
            context={'teen_tags': teen_tags}
        )


# all products

def all_books(request):
    if request.method == 'GET':
        products = models.Products.objects.filter().order_by('-id')
        return render(
            request,
            template_name='products/all_books.html',
            context={
                'products': products
            }
        )

# def edit_books_view(request, id):
#     bk_id = get_object_or_404(models.Books_list, id=id)
#     if request.method == 'POST':
#         form = forms.Books_list_Form(request.POST, instance=bk_id)
#         form.save()
#         return HttpResponse('<h3>Books updated successfully!</h3>'
#                             '<a href="/Books_list/">Список книг</a>')
#     else:
#         form = forms.Books_list_Form(instance=bk_id)
#     return render(
#         request,
#         template_name='products/edit_books.html',
#         context={
#             'form': form,
#             'bk_id': bk_id
#         }
#     )
class EditBooksView(generic.UpdateView):
    template_name = 'products/edit_books.html'
    form_class = forms.Books_list_Form
    success_url = '/Books_list/'

    def get_object(self, **kwargs):
        bk_id = self.kwargs.get('id')
        return get_object_or_404(models.Books_list, id=bk_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditBooksView, self).form_valid(form=form)



# def drop_books_view(request, id):
#     bk_id = get_object_or_404(models.Books_list, id=id)
#     bk_id.delete()
#     return HttpResponse('<h3>Book delete successfully!</h3>'
#                         '<a href="/Books_list/">Список книг</a>')
class DeleteBooksView(generic.DeleteView):
    template_name = 'books/confirm_delete.html'
    success_url = '/Books_list/'

    def get_object(self, **kwargs):
        bk_id = self.kwargs.get('id')
        return get_object_or_404(models.Books_list, id=bk_id)


# create employee

# def create_books_view(request):
#     if request.method == "POST":
#         form = forms.Books_list_Form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Book created successfully!</h3>'
#                                 '<a href="/Books_list/">Список книг</a>')
#     else:
#         form = forms.Books_list_Form()
#
#     return render(
#         request,
#         template_name='products/create_books.html',
#         context={'form': form}
#     )
class CreateBooksView(generic.CreateView):
    template_name = 'products/create_books.html',
    form_class = forms.Books_list_Form
    success_url = '/Books_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBooksView, self).form_valid(form=form)


class BooksDetailView(generic.DetailView):
    template_name = 'books/Book_Detail.html'
    context_object_name = 'bk_id'

    def get_object(self, **kwargs):
        bk_id = self.kwargs.get('id')
        return get_object_or_404(models.Books_list, id=bk_id)

