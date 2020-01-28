from django.db import models

class ProductCategories(models.Model):
	""" Модель категории товаров """

	name = models.CharField('Наименование', max_length=255)
	created = models.DateTimeField(verbose_name='Создано', auto_now_add = True)

	class ReportBuilder:
		fields = ('name', 'created')
		filters = ('name', 'created')

	class Meta:
		ordering = ['-id']

	def __str__(self):
		return str(self.name)

class Product(models.Model):
	""" Модель товаров """

	name = models.CharField('Наименование', max_length=255)
	vendorcode = models.CharField('Артикул', max_length=30)
	description = models.TextField('Описание', null = True, blank = True)
	prodcat = models.ManyToManyField(ProductCategories, verbose_name="Категории", related_name='prodcat')
	created = models.DateTimeField(verbose_name='Создано', auto_now_add = True)

	class ReportBuilder:
		fields = ('name', 'vendorcode', 'description', 'prodcat', 'created')
		filters = ('name', 'vendorcode', 'description', 'prodcat', 'created')

	class Meta:
		ordering = ['-id']

	def __str__(self):
		return str(self.name)