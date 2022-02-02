from django import views
from django.shortcuts import render
from django.http import HttpResponseRedirect        # для переадресации формы после post на страницу thank-you.html
from django.views import View                       # для создания view на основе класса View
from django.views.generic.base import TemplateView
from django.views.generic import ListView



from . forms import ReviewForm
from . models import Review

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

class ThankYouView(TemplateView):
    # template_name спец свойство
    template_name = "reviews/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['massage'] = 'this work!'
        return context

class ReviewListView(TemplateView):
    template_name = "reviews/review-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context

class ReviewDitailView(TemplateView):
    template_name = "reviews/review-ditail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ищем в kwargs наш переменный параметр id, который передаём в urls.py <int:id>
        review_id = kwargs['id']
        review = Review.objects.get(id=review_id)
        context['review'] = review
        return context