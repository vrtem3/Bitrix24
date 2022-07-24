from django_filters import FilterSet, ModelChoiceFilter
from .models import Post


class PostFilter(FilterSet):
    Post = ModelChoiceFilter(
        field_name='category_type',
        queryset=Post.objects.all(),
        label='Категория'
    )

    class Meta:
        model = Post
        fields = {
            'post_title': ['icontains'],
            'date_create': ['gte'],
        }
