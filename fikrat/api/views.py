from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from fikrat.api.paginations import EightPagination, FourPagination
from fikrat.models import Category, Language, Author, Book, Photo, Proverb, Media, ArticleAuthor, Article
from fikrat.api.serializers import (
    CategoryModelSerializer,
    LanguageModelSerializer,
    AuthorModelSerializer,
    BookListModelSerializer,
    BookDetailModelSerializer,
    PhotoModelSerializer,
    ProverbModelSerializer,
    MediaModelSerializer,
    ArticleAuthorModelSerializer,
    ArticleModelSerializer,
)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class LanguageListAPIView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageModelSerializer


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.filter(is_audio=False)
    serializer_class = BookListModelSerializer
    pagination_class = EightPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('category', 'language', 'author')
    search_fields = ('translations__title', 'translations__publisher')


class AudioBookListAPIView(ListAPIView):
    queryset = Book.objects.filter(is_audio=True)
    serializer_class = BookListModelSerializer
    pagination_class = EightPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('category', 'language', 'author')
    search_fields = ('translations__title', 'translations__publisher')


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailModelSerializer


class PhotoListAPIView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoModelSerializer
    pagination_class = EightPagination


class ProverbListAPIView(ListAPIView):
    queryset = Proverb.objects.all()
    serializer_class = ProverbModelSerializer
    pagination_class = EightPagination


class MediaListAPIView(ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaModelSerializer
    pagination_class = FourPagination


class ArticleAuthorListAPIView(ListAPIView):
    queryset = ArticleAuthor.objects.all()
    serializer_class = ArticleAuthorModelSerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    pagination_class = FourPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('category', 'language', 'author')
