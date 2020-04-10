from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea) 

	def clean_email(self,*args,**kwargs):
		email = self.cleaned_data.get('email')
		if email.endswith(".edu"):
			raise forms.ValidationError("This is not a valid email adress!")

class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['shop_name','shop_adress','landmark','mobile_no','product_name','price','MinOffer','catogory','product_description','image','image2','image3','slug'] 





class ContactForm(forms.Form):
	title = forms.CharField()
	email = forms.EmailField()
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea) 

	def clean_email(self,*args,**kwargs):
		email = self.cleaned_data.get('email')
		if email.endswith(".edu"):
			raise forms.ValidationError("This is not a valid email adress!")