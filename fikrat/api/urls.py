from django.urls import path

from fikrat.api.views import (
    CategoryListAPIView,
    LanguageListAPIView,
    AuthorListAPIView,
    BookListAPIView,
    BookRetrieveAPIView,
    PhotoListAPIView,
    ProverbListAPIView,
    MediaListAPIView,
    ArticleAuthorListAPIView,
    ArticleListAPIView,
    AudioBookListAPIView,
)

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('language/', LanguageListAPIView.as_view(), name='language_list'),
    path('author/', AuthorListAPIView.as_view(), name='author_list'),
    path('book/', BookListAPIView.as_view(), name='book_list'),
    path('audio-book/', AudioBookListAPIView.as_view(), name='audio_book_list'),
    path('book/<int:pk>/', BookRetrieveAPIView.as_view(), name='book_retrieve'),
    path('photo/', PhotoListAPIView.as_view(), name='photo_list'),
    path('proverb/', ProverbListAPIView.as_view(), name='proverb_list'),
    path('media/', MediaListAPIView.as_view(), name='media_list'),
    path('article-author/', ArticleAuthorListAPIView.as_view(), name='article_author_list'),
    path('article/', ArticleListAPIView.as_view(), name='article_list'),
]
