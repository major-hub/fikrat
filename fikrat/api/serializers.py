from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers

from fikrat.api.mixins import TranslatedSerializerMixin
from fikrat.models import Category, Language, Author, Book, Photo, Proverb, Media, ArticleAuthor, Article


class BaseSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    pass


class CategoryModelSerializer(BaseSerializer):
    translations = TranslatedFieldsField(shared_model=Category)

    class Meta:
        model = Category
        fields = ('id', 'translations')


class LanguageModelSerializer(BaseSerializer):
    translations = TranslatedFieldsField(shared_model=Language)

    class Meta:
        model = Language
        fields = ('id', 'translations')


class AuthorModelSerializer(BaseSerializer):
    translations = TranslatedFieldsField(shared_model=Author)

    class Meta:
        model = Author
        fields = ('id', 'translations')


class BookListModelSerializer(BaseSerializer):
    author = AuthorModelSerializer()
    translations = TranslatedFieldsField(shared_model=Book)

    class Meta:
        model = Book
        fields = (
            'id',
            'translations',
            'author',
            'image',
        )


class BookDetailModelSerializer(BaseSerializer):
    category = CategoryModelSerializer()
    language = LanguageModelSerializer()
    author = AuthorModelSerializer()
    translations = TranslatedFieldsField(shared_model=Book)

    class Meta:
        model = Book
        fields = (
            'id',
            'translations',
            'category',
            'language',
            'author',
            'year',
            'number_of_pages',
            'image',
            'is_audio',
            'file',
            'file_size',  # property
            'file_extension',  # property
        )


class PhotoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image',)


class ProverbModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proverb
        fields = ('image',)


class MediaModelSerializer(BaseSerializer):
    translations = TranslatedFieldsField(shared_model=Media)

    class Meta:
        model = Media
        fields = ('id', 'translations', 'video', 'created_at')


class ArticleAuthorModelSerializer(BaseSerializer):
    translations = TranslatedFieldsField(shared_model=ArticleAuthor)

    class Meta:
        model = ArticleAuthor
        fields = ('id', 'translations')


class ArticleModelSerializer(BaseSerializer):
    category = CategoryModelSerializer()
    language = LanguageModelSerializer()
    author = AuthorModelSerializer()
    translations = TranslatedFieldsField(shared_model=Article)

    class Meta:
        model = Article
        fields = (
            'id',
            'translations',
            'category',
            'language',
            'author',
            'created_at',
        )
