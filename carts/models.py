from django.db import models
from blog.models import BlogPost


PAYMENT_CHOICES = (("credit card","credit card"),("Cash On Delivery","Cash On Delivery"),("Online Transactions","Online Transactions"))



class CartItem(models.Model):
	cart = models.ForeignKey('Cart',null=True,blank=True,on_delete=models.CASCADE)
	product = models.ForeignKey(BlogPost,null=True,blank=True,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(default=10.99,max_digits=1000,decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	#checkout
	#Mobile_No = models.IntegerField(default=True)
	#Shipping_Adress = models.CharField(max_length=500,default=True)
	#Type_Of_Payment = models.CharField(max_length=200,choices = PAYMENT_CHOICES,default='')


	def __unicode__(self):
		try:
			return str(self.cart.id)
		except:
			self.product.title

class Cart(models.Model):
	total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	Active = models.BooleanField(default=True) 



#class CheckOut(models.Model):
	


	def __unicode__(self):
		return "Cart Id: %s"%(self.id)

	#def cart_get_edit_url(self):
		#return f"{self.get_absolute_url()}/update"
