from django import forms
from django.forms import ModelForm, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import Field
from .models import *

class ProductCategoriesForm(forms.ModelForm):
	class Meta:
		model = ProductCategories
		fields = ('name',)

	def __init__(self, *args, **kwargs):
		super(ProductCategoriesForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-sm-2'
		self.helper.field_class = 'col-sm-6'
		self.helper.layout = Layout(
			Fieldset(
				'Добавление новой категории',
				Field('name'),
			),
		)

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		widgets = {
			'description': Textarea(attrs={'cols': 50, 'rows': 3}),
		}
		fields = ('name', 'vendorcode', 'description', 'prodcat',)

	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-sm-2'
		self.helper.field_class = 'col-sm-6'
		self.helper.layout = Layout(
			Fieldset(
				'Добавление нового товара',
				Field('name'),
				Field('vendorcode'),
				Field('description'),
				Field('prodcat'),
			),
		)