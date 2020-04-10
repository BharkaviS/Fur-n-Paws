from django.db import models

# Create your models here.

class BuyerPost(models.Model):
	shop_name = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to='media/image/', blank=True, null=True)
	product_name = models.SlugField(unique=True,max_length=120)
	catogory = models.CharField(max_length=120,choices=ITEM_CHOICES,default='chains')
	price = models.IntegerField(default=True)
	item_description= models.TextField(null=True, blank=True)
	shop_adress = models.CharField(max_length=220)
	landmark = models.CharField(max_length=120)
	mobile_no = models.IntegerField(default=True)


	class Meta:
		ordering = ['shop_name','shop_adress','landmark','mobile_no','product_name','price','item_description','image']

		
