from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Q
#from phonenumber_field.modelfields import PhoneNumberField

from comments.models import Comment
from django.contrib.contenttypes.models import ContentType


ITEM_CHOICES = (('leash','LEASH'),('chains','CHAINS'),('food','FOOD'),('CHEW','chew'))

User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published(self):
    	now = timezone.now()
    	return self.filter(published_date__lte=now)

    def search(self, query):
        lookup =( Q(product_name__icontains=query)|
        		Q(product_description__icontains=query)|
        		Q(catogory__icontains=query)
        		)
                    

        return self.filter(lookup)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
    	return self.get_queryset().published()

    def search(self,query=None):
    	if query is None:
    		return self.get_queryset().none()
    	return self.get_queryset().published().search(query)



class BlogPost(models.Model):
	shop_name = models.ForeignKey(User, default=User, null=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to='media/image/', blank=True, null=True) 
	image2 = models.ImageField(upload_to='media/image/', blank=True, null=True) 
	image3 = models.ImageField(upload_to='media/image/', blank=True, null=True) 

	product_name = models.CharField(max_length=120)
	catogory = models.CharField(max_length=120,choices=ITEM_CHOICES,default='')
	price = models.IntegerField(default=True)
	slug  = models.SlugField(unique=True) # hello world -> hello-world
	product_description = models.TextField(null=True, blank=True)
	published_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
	shop_adress = models.CharField(default=True,max_length=220)
	landmark = models.CharField(max_length=340,default=True)
	mobile_no = models.IntegerField(null=True,blank=False,unique=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	MinOffer = models.IntegerField(default=True)
	Active = models.BooleanField(default=True)


	objects = BlogPostManager()

	class Meta:
		ordering = ["-pk","image","-published_date","-updated","-timestamp"]

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/update"
	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete" 

	@property
	def comments(self):
		instance = self
		qs = Comment.objects.filter_by_instance(instance)
		return qs

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type
	
