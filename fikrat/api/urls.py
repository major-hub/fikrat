from django.urls import path

from fikrat.api.views import (
    CategoryListAPIView,
)

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('language/', CategoryListAPIView.as_view(), name='language_list'),
    path('author/', CategoryListAPIView.as_view(), name='author_list'),
    path('book/', CategoryListAPIView.as_view(), name='book_list'),
    path('book/<int:pk>/', CategoryListAPIView.as_view(), name='book_retrieve'),
    path('photo/', CategoryListAPIView.as_view(), name='photo_list'),
    path('proverb/', CategoryListAPIView.as_view(), name='proverb_list'),
    path('media/', CategoryListAPIView.as_view(), name='media_list'),
    path('article-author/', CategoryListAPIView.as_view(), name='article_author_list'),
    path('article/', CategoryListAPIView.as_view(), name='article_list'),
]
