from django.forms import ModelForm
from .models import PostModel


class PostModelForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ("title", "content", "slug")
