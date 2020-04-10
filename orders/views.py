import time

from django.shortcuts import render,HttpResponseRedirect
from carts.models import Cart
from django.urls import reverse
# Create your views here.
from .models import Order


def Orders(request):
	context = {}
	template_name = "orders/user.html"

	return render(request,template_name,context)

def checkout(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		
		the_id = None
		return HttpResponseRedirect(reverse('cart'))

	new_order,created = Order.objects.get_or_create(cart=cart)

	if created:
		new_order.order_id = str(time.time())
		new_order.save()
	new_order.user = request.user
	new_order.save()

	if new_order.status == "Finished":
		del request.session['cart_id']
		del request.session['item_total']
		return HttpResponseRedirect(reverse('cart'))



	context = {}
	template_name = "blog/blog_post_list.html"
	return render(request,template_name,context)
