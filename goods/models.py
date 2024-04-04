from email.policy import default
from django.db import models
from django.urls import reverse

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True,  verbose_name='URL')
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        
    def __str__(self) -> str:
        return self.name
    
class Brands(models.Model):
    name = models.CharField(max_length=70, unique=True, verbose_name='Бренд')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True,  verbose_name='URL')
    
    class Meta:
        db_table = 'brand'
        verbose_name = 'Бренда'
        verbose_name_plural = 'Бренды'
        
    def __str__(self) -> str:
        return self.name
        
        
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True,  verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Картинка')
    price = models.PositiveIntegerField(verbose_name='Цена')
    quantity= models.PositiveIntegerField(default=0, verbose_name='Количество')
    category= models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')
    brand = models.ForeignKey(to=Brands, on_delete=models.PROTECT, verbose_name='Бренд', blank=True, null=True,)
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)
        
    def __str__(self) -> str:
        return f'{self.name} Количество - {self.quantity}'
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    
    
    def display_id(self):
        return f'{self.id:05}'