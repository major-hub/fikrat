from django.contrib import admin

from parler.admin import TranslatableAdmin

from fikrat.models import Category, Language, Author, Book, Photo, Proverb, Media, ArticleAuthor, Article


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(TranslatableAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(TranslatableAdmin):
    pass


@admin.register(Book)
class BookAdmin(TranslatableAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Proverb)
class ProverbAdmin(admin.ModelAdmin):
    pass


@admin.register(Media)
class MediaAdmin(TranslatableAdmin):
    pass


@admin.register(ArticleAuthor)
class ArticleAuthorAdmin(TranslatableAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(TranslatableAdmin):
    pass
