from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.CharField(
        max_length=155,
        verbose_name='email'
    )
    number = models.CharField(
        max_length=255,
        verbose_name='номер'
    )
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name_plural = 'Контакты' 

class Animals(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='имя'
    )
    gender = models.CharField(
        max_length=255,
        verbose_name='пол'
    )
    image = models.ImageField(
        upload_to='base',
        verbose_name='Фото'
    )
    kastrasya = models.CharField(
        max_length=155,
        verbose_name='кастрация'
    )
    age = models.CharField(
        max_length=255,
        verbose_name='возраст'
    
    )
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'добавить животных' 
        
        
class Our_gallery(models.Model):
    all = models.ImageField(
        upload_to='base',
        verbose_name='все фотографии'
    )
    dogs_and = models.ImageField(
        upload_to='base',
        verbose_name='кошки и собаки'
    )
    other = models.ImageField(
        upload_to='base',
        verbose_name='наше'
    )
    def __str__(self) -> str:
        all_url = self.all.url if self.all else 'No Image'
        dogs_and_url = self.dogs_and.url if self.dogs_and else 'No Image'
        other_url = self.other.url if self.other else 'No Image'
        return f"Gallery Item: {self.id} - All: {all_url}, Dogs and Cats: {dogs_and_url}, Other: {other_url}"

    
    class Meta:
        verbose_name_plural = 'Настройки галлереи животных' 
        
        
class Our_prices(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='base',
        verbose_name='Фото'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка нашей цены' 

class Base(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='base',
        verbose_name='Фото'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка главной страницы'

class Our_service(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    photo = models.ImageField(
        upload_to='image/',
        verbose_name="фотография "
    )
    

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"
