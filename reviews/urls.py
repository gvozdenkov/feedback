import imp
from django.urls import path


from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name="review-page"),
    path('thank-you', views.ThankYouView.as_view(), name="thank-you"),
    path('reviews', views.ReviewListView.as_view(), name="reviews"),
    path('reviews/<int:id>', views.ReviewDitailView.as_view(), name="review-ditail"),

]