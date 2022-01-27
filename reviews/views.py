from django.shortcuts import render
from django.http import HttpResponseRedirect        #для переадресации формы после post на страницу thank-you.html

# Create your views here.

def review(request):
    if request.method == 'POST':
        # получаем данные, введённые в форму из dict (словарь) по ключу
        # который возвращает request.Post - ключь в html <input name='username'>
        entered_username = request.POST['username']
        print(f"user input: {entered_username}")

        # переадресация на домен /thank-you который описан в urls.py
        return HttpResponseRedirect("thank-you")
        
    return render(request, "reviews/review.html")


def thank_you(request):
    return render(request, "reviews/thank-you.html")