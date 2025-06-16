from django.db import models
from django.contrib.auth.models import User

MAX_LENGTH = 255
MAX_LENGTH_1 = 25


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    # buy = models.OneToOneField('Clothes', on_delete=models.CASCADE, related_name=by_clothes)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Collection(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование коллекции')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Clothes(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование позиции')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.PositiveIntegerField(default=36, verbose_name='Размер')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 verbose_name='Категория')  # protect не дает удалить

    collection = models.ManyToManyField(Collection, verbose_name='Коллекция')

    # buy = models.OneToOneField('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - ({self.price} рублей.)"

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'


class Brand(models.Model):
    BrandName = models.CharField(max_length=MAX_LENGTH_1, verbose_name='Название бренда')
    Img = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='изображение бренда')

    def __str__(self):
        return self.BrandName

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class PetType(models.Model):
    TypeName = models.CharField(max_length=25, verbose_name='Тип животного', unique=True)
    Description = models.TextField(max_length=500, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.TypeName

    class Meta:
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животных'


class CategoryProduct(models.Model):
    CategoryName = models.CharField(max_length=MAX_LENGTH_1, verbose_name='Название категории товара')
    PetType = models.ForeignKey(PetType, on_delete=models.CASCADE, verbose_name='Тип животного', null=True, blank=True)

    def __str__(self):
        return self.CategoryName

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class CatalogProduct(models.Model):
    ProductName = models.CharField(max_length=100, verbose_name='Название продукта')
    PriceOfProduct = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта')
    DescriptionProduct = models.CharField(max_length=300, verbose_name='Описание продукта')
    Img = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение продукта')
    Quantity = models.PositiveIntegerField(verbose_name='Количество')
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд')
    Category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.ProductName

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Promotion(models.Model):
    PromotionName = models.CharField(max_length=100, verbose_name='Название акции')
    DiscountPercentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Процент скидки')
    StartDate = models.DateTimeField(verbose_name='Дата начала')
    EndDate = models.DateTimeField(verbose_name='Дата окончания')
    CatalogProduct = models.ManyToManyField(CatalogProduct, verbose_name='Продукты', blank=True)

    def __str__(self):
        return self.PromotionName

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


# class Cart(models.Model):
#     User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
#     CatalogProduct = models.ForeignKey(CatalogProduct, on_delete=models.CASCADE, verbose_name='Продукт')
#     Quantity = models.PositiveIntegerField(verbose_name='Количество')
#     Price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
#
#     def __str__(self):
#         return f"{self.User.username} - {self.CatalogProduct.ProductName}"
#
#     class Meta:
#         verbose_name = 'Корзина'
#         verbose_name_plural = 'Корзины'


class Review(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    CatalogProduct = models.ForeignKey(CatalogProduct, on_delete=models.CASCADE, verbose_name='Продукт')
    Rating = models.PositiveIntegerField(verbose_name='Рейтинг')
    ReviewText = models.TextField(max_length=1000, verbose_name='Текст отзыва')
    CreatedAt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Отзыв {self.User.username} на {self.CatalogProduct.ProductName}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Favorite(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    CatalogProduct = models.ForeignKey(CatalogProduct, on_delete=models.CASCADE, verbose_name='Продукт')
    AddedAt = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f"{self.User.username} - {self.CatalogProduct.ProductName}"

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        unique_together = ('User', 'CatalogProduct')


class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"
    TYPE_DELIVERY=[
        (SHOP, 'Самовывоз'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Пункт выдачи заказов'),
    ]
    buyer_surname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия покупателя')
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя покупателя')
    buyer_middlename = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Отчество покупателя')
    comment = models.CharField(max_length=MAX_LENGTH, blank=True, null=True,verbose_name='Комментарий к заказу')
    delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ доставки')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения заказа')

    catalogproduct = models.ManyToManyField('CatalogProduct', through='Pos_order', verbose_name='Товар')


    def __str__(self):
        return f"#{self.pk} - {self.buyer_surname} {self.buyer_name} {self.date_create}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Pos_order(models.Model):
    catalogproduct = models.ForeignKey(CatalogProduct, on_delete=models.PROTECT, verbose_name='продукт')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количство продукта')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на позицию')

    def __str__(self):
        return f'{self.order.pk} {self.catalogproduct.name} ({self.order.buyer_surname} {self.order.buyer_name}'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'