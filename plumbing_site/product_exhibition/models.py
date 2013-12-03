from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Author(models.Model):
	"""
	Model for introducting and show in the contact part
	"""
	first_name 	= models.CharField(max_length = 20)
	second_name = models.CharField(max_length = 20)
	email 		= models.EmailField(max_length = 75)
	address		= models.CharField(max_length = 50)
	description = models.TextField()
	profile_img = models.ImageField(upload_to = "pic_folder/", default = "pic_folder/default_image.jpg")
	mobile_phone = models.CharField(max_length = 20)
	telephone	= models.CharField(max_length = 20)
	
	def __unicode__(self):
		"""
		"""
		return self.first_name + self.second_name

class Elementary(models.Model):
	"""
	"""
	name_en 	= models.CharField(max_length = 80, unique = True, default = "None")
	name_ch 	= models.CharField(max_length = 50, unique = True, default = "None")
	material_en 	= models.CharField(max_length = 80, default = "None")
	material_ch 	= models.CharField(max_length = 50, default = "None")
	characteristic_en = models.CharField(max_length = 150, default = "None")
	characteristic_ch = models.CharField(max_length = 150, default = "None")
	
	def __unicode__(self):
		return self.name_ch

class New(models.Model):
	"""
	"""
	title 		= models.CharField(max_length = 100)
	slug 		= models.SlugField(unique = True)
	text		= models.TextField()
	created_on 	= models.DateTimeField(auto_now_add = True)
	author		= models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		"""
		"""
		return ('blog_post_detail', (),
				{
					'slug':	self.slug,
				})

	def save(self, *args, **kwargs):
		"""
		"""
		if not self.slug:
			self.slug = slugify(self.title)
		super(New, self).save(*args, **kwargs)

class Category(models.Model):
	"""
	"""
	name_en = models.CharField(max_length = 50, default = "None")
	name_ch = models.CharField(max_length = 50, default = "None")

	def __unicode__(self):
		return self.name_ch + " " + (self.name_en)

class Production(models.Model):
	"""
	"""
	product_name_en	 	= models.CharField(max_length = 80, unique = True, default = "None")
	product_name_ch	 	= models.CharField(max_length = 50, unique = True, default = "None")
	product_brand_en 	= models.CharField(max_length = 80, default = "None")
	product_brand_ch 	= models.CharField(max_length = 50, default = "None")
	material_en 		= models.CharField(max_length = 80, default = "None")
	material_ch 		= models.CharField(max_length = 100, default = "None")
	product_performance_en	= models.CharField(max_length = 150, default = "None")
	product_performance_ch 	= models.CharField(max_length = 80, default = "None")
	product_size_en 		= models.CharField(max_length = 150, default = "None")
	product_size_ch			= models.CharField(max_length = 100, default = "None")
	work_environment_en		= models.CharField(max_length = 100, default = "None")
	work_environment_ch		= models.CharField(max_length = 150, default = "None")
	product_char_en		= models.CharField(max_length = 150, default = "None")
	product_char_ch 	= models.CharField(max_length = 150, default = "None")
	detail_en			= models.CharField(max_length = 150, default = "None")
	detail_ch			= models.CharField(max_length = 150, default = "None")
	product_price_en	= models.CharField(max_length = 100, default = "None")
	product_category_en = models.ForeignKey(Category)
	product_img			= models.ImageField(upload_to = "pic_folder/", default = "pic_folder/default_image.jpg") # this still need for modifying
	product_size_img	= None

	def __unicode__(self):
		"""
		"""
		return self.product_name_ch + " " + (self.product_name_en)