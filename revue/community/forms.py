from django import forms
from .models import Review, Comment, ShortReview, Recomment, Report

from django_summernote.widgets import SummernoteWidget

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'placeholder': '제목 입력',
            }
            )
        )
    rating = forms.IntegerField(
        label="Rating",
        widget=forms.NumberInput(
        )
        )

    class Meta:
        model = Review
        fields = ['title','rating','content',]
        widgets = {
            'content' : SummernoteWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('content',)


class RecommentForm(forms.ModelForm):
    class Meta:
        model=Recomment
        fields=('content',)


class ShortReviewForm(forms.ModelForm):
    content = forms.CharField(
        label="한줄평",
        widget=forms.Textarea(
            attrs={
                'row':5,
                'col':50,
            }
        )
    )
    class Meta:
        model = ShortReview
        fields = ('content',)

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('simple_reason', 'detail_reason')