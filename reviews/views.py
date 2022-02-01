from pdb import post_mortem
from django.shortcuts import render
from django.http import HttpResponseRedirect        #для переадресации формы после post на страницу thank-you.html
from django.views import View

from . forms import ReviewForm
# from . models import Review

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "input_form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thank-you")
        
        return render(request, "reviews/review.html", {
            "input_form": form
        })

# def review(request):
#     if request.method == 'POST':
#         # получаем данные введённые в форму
#         form = ReviewForm(request.POST)

#         # проверка на корректность данных. Встроено в джанго
#         if form.is_valid():
#             print(f"user input: {form.cleaned_data}")
#             # это ручное сохранение данных из формы в базу
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating'])
#             # review.save()

#             # Но если используем формы на основе классов, то
#             # просто сохраняем форму в базу так
#             form.save()

#             # переадресация на домен /thank-you который описан в urls.py
#             return HttpResponseRedirect("thank-you")
#     else:
#         # если метод не POST, а GET - рендерим чистую форму (кнопка не нажималась)
#         form = ReviewForm()

#     # есил метод POST, но валидация не прошла, то на рендер идёт не чистая форма, а ReviewForm(request.POST)
#     # позволяет не терять введённые данные, если они неправильные
#     return render(request, "reviews/review.html", {
#             "input_form": form
#     })


def thank_you(request):
    return render(request, "reviews/thank-you.html")