from django import forms
from .models import BuyerPost 

class BuyerModelForm(forms.Modelform):
	model = BuyerPost 
	fields = ['shop_name','shop_adress','landmark','mobile_no','product_name','price','item_description','image']
