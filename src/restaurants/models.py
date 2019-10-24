from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.conf import settings
# Create your models here.
User=settings.AUTH_USER_MODEL

class RestaurantLocation(models.Model):
	owner 			= models.ForeignKey(User)
	name      		= models.CharField(max_length=120)
	location  		= models.CharField(max_length=120, null=True, blank=True)
	category  		= models.CharField(max_length=120,null=True,blank=True)
	review  		= models.CharField(max_length=2000,null=True,blank=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated   		= models.DateTimeField(auto_now=True)
	slug 			= models.SlugField(null=True, blank=True)
	updated1   		= models.DateTimeField(auto_now=True)
	updated2   		= models.DateTimeField(auto_now=True)


	# my_date_feild 	= models.DataField(auto_now=False, auto_now_add=False)
	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name
def rl_pre_save(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug=unique_slug_generator(instance)

pre_save.connect(rl_pre_save,sender=RestaurantLocation)


