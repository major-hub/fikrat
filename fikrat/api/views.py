from rest_framework.generics import ListAPIView, RetrieveAPIView

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
    queryset = Book.objects.all()
    serializer_class = BookListModelSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailModelSerializer


class PhotoListAPIView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoModelSerializer


class ProverbListAPIView(ListAPIView):
    queryset = Proverb.objects.all()
    serializer_class = ProverbModelSerializer


class MediaListAPIView(ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaModelSerializer


class ArticleAuthorListAPIView(ListAPIView):
    queryset = ArticleAuthor.objects.all()
    serializer_class = ArticleAuthorModelSerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
