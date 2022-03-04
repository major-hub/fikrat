from django_filters.fields import CSVWidget
from django_filters import ModelMultipleChoiceFilter
from django_filters.rest_framework import FilterSet

from fikrat.models import Book, Category, Author, Language


class BookFilterSet(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name="category",
        queryset=Category.objects.all(),
        widget=CSVWidget
    )
    language = ModelMultipleChoiceFilter(
        field_name="language",
        queryset=Language.objects.all(),
        widget=CSVWidget
    )
    author = ModelMultipleChoiceFilter(
        field_name="author",
        queryset=Author.objects.all(),
        widget=CSVWidget
    )

    class Meta:
        model = Book
        fields = ['category', 'language', 'author']
