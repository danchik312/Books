from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class FanRankMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            years_of_exp = int(request.POST.get("years_of_exp"))
            if years_of_exp < 1:
                return HttpResponseBadRequest(
                    "Ваш опыт слишком мал, вы нам не подходите"
                )
            elif 1 <= years_of_exp <= 10:
                request.rank = "Новичок"
            elif 11 <= years_of_exp <= 18:
                request.rank = "Профи"
            elif 18 <= years_of_exp <= 80:
                request.rank = "Олд"
            else:
                return HttpResponseBadRequest("Ого, к сожалению, вы очень стары")
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "rank", "Ранг не определен")
