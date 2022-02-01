# файл для работы с формами и нстройки их вида

from django import forms

# from feedback.reviews.models import Review
from . models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Input your name", max_length=20, error_messages={
#         "required": "your name must not be empty"
#     })
#     review_text = forms.CharField(label="Your feedback", widget=forms.Textarea)
#     review_text.widget.attrs.update(size='40')
#     rating = forms.IntegerField(label="Your ratig", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # fields = ['user_name', 'review_text', 'rating']       выборочно поля
        labels = {
            "user name": "Enter your name",
            "review_text": "Your feedback",
            "rating": "Your rating",
        }

        error_messages = {
            "required": "your name must not be empty"
        }
 