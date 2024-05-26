from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    preview = models.ImageField(
        upload_to="catalog/photo", verbose_name="Превью продукта", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.FloatField(verbose_name="Цена продукта")
    created_at = models.DateField(verbose_name="Дата создания", blank=True, null=True)
    updated_at = models.DateField(verbose_name="Дата изменения", blank=True, null=True)
    # manufactured_at = models.DateField(verbose_name='Дата производства продукта', blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    # Наименование, Описание, Изображение (превью), Категория, Цена за покупку
    # Дата создания (записи в БД), Дата последнего изменения (записи в БД)

    # Наименование, Описание

# Поля «Дата создания» и «Дата последнего изменения» стали стандартом для моделей.
# Их общепринятые названия — created_at и updated_at соответственно.