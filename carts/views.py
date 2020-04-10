from django.shortcuts import render,HttpResponseRedirect 
from django.urls import reverse 
from .models import Cart,CartItem
from blog.models import BlogPost 
#from .forms import CheckOutForm
from django.shortcuts import render,get_object_or_404,redirect
#from .models import CheckOut

# Create your views here.

def View(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)

	except:
		the_id = None
	if the_id:
		the_id = request.session['cart_id']
		context = {"cart":cart}
	else:
		empty_message = "Your cart is empty!please keep shopping!"
		context = {"empty":True,"empty_message":empty_message}

	template_name = "carts/view.html"
	
	return render(request,template_name,context)


'''def remove_from_cart(request,id):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)

	except:
		return HttpResponseRedirect(reverse("cart"))
	cartitem = CartItem.objects.get(id=id)
	cartitem.cart = None
	cartitem.save()
	#cartitem.delete()	
	return HttpResponseRedirect(reverse("cart"))'''



'''def update_cart(request,slug):
	request.session.set_expiry(1200000)

	try:
		qty = request.GET.get('qty')
		update_qty = True
	except:
		qty = None
		update_qty = False

		
	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id 
		the_id = new_cart.id

	cart = Cart.objects.get(id=the_id)


	try:
		product = BlogPost.objects.get(slug=slug)
	except BlogPost.DoesNotExsist:
		pass
	except:
		pass

	cart_item,created = CartItem.objects.get_or_create(cart=cart,product=product)

	if  update_qty and qty:
		if int(qty) == 0:
			cart_item.delete()
		else:
			cart_item.quantity = qty 
			cart_item.save()
	else:
		pass

	#if not cart_item in cart.items.all():
		#cart.items.add(cart_item)
	#else:
		#cart.items.remove(cart_item)

	new_total = 0.00 
	line_total = 0.00
	for item in cart.cartitem_set.all():
		line_total += float(item.product.price)*item.quantity
		new_total += line_total

	request.session['items_count'] = cart.cartitem_set.count()

	cart.total = new_total 
	cart.save() 

	return HttpResponseRedirect(reverse("cart")) 


def CheckOut_View(request):
	template_name = "carts/order.html"
	form = CheckOutForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = CheckOutForm()
	context = {"form":form} 
	return render(request,template_name,context)


def OrderSummary(request):
	obj = get_object_or_404(CheckOut)
	template_name = "checkout.html"
	context = {"obj":obj} 


	return render(request,context,template_name)

def OrderSummary(request):
	try:
		the_id = request.session['cart_id']
	except:
		the_id = None
	if the_id:
		cart = Cart.objects.get(id=the_id)
		context = {"cart":cart}
	else:
		empty_message = "Your cart is empty!please keep shopping!"
		context = {"empty":True,"empty_message":empty_message}

	template_name = "carts/checkout.html"
	
	return render(request,template_name,context)'''


