from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(name=models.CharField(max_length=200), )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "bo'lim"
        verbose_name_plural = "bo'limlar"


class Language(TranslatableModel):
    translations = TranslatedFields(name=models.CharField(max_length=200), )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "til"
        verbose_name_plural = "tillar"


class Author(TranslatableModel):
    translations = TranslatedFields(full_name=models.CharField(max_length=200), )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "kitob avtor"
        verbose_name_plural = "kitob avtorlar"


class Book(TranslatableModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    translations = TranslatedFields(
        title=models.CharField(max_length=250),
        publisher=models.CharField(max_length=250),
        description=models.TextField()
    )
    year = models.PositiveSmallIntegerField()
    number_of_pages = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='book_images/')
    is_audio = models.BooleanField(default=False)
    file = models.FileField(upload_to='book_files/', validators=[FileExtensionValidator(
        allowed_extensions=['pdf', 'doc', 'docx', 'epub', 'mp3', 'ogg']
    )])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "kitob"
        verbose_name_plural = "kitoblar"


class Photo(models.Model):
    """
    Shunchaki galareya
    """
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = "rasm"
        verbose_name_plural = "rasmlar"


class Proverb(models.Model):
    """
    Rasmdagi hikmatlar
    """
    image = models.ImageField(upload_to='proverbs/')

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = "hikmat"
        verbose_name_plural = "hikmatlar"


class Media(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=250),
    )
    video = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "media"
        verbose_name_plural = "medialar"


class ArticleAuthor(TranslatableModel):
    translations = TranslatedFields(full_name=models.CharField(max_length=200), )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "maqola avtor"
        verbose_name_plural = "maqola avtorlar"


class Article(TranslatableModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    author = models.ForeignKey('ArticleAuthor', on_delete=models.CASCADE)

    translations = TranslatedFields(
        title=models.CharField(max_length=250),
        content=models.TextField()
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "maqola"
        verbose_name_plural = "maqolalar"
