from django import forms
from news.models import Article


class NewsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "name", "description"
        ]
