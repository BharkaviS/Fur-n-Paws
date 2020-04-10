from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostModelForm,ContactForm
from .decorators import user_is_entry_author
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from urllib.parse import quote_plus

#imports for adding comments
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from comments.forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect, Http404


def BlogPostDetailPage(request,slug):
	#queryset = BlogPost.objects.filter(slug=slug)
	#if queryset.count() == 0:
		#raise Http404
	obj = get_object_or_404(BlogPost,slug=slug)
	template_name = "blog/blog_post_detail.html"
	title = ""
	context = {"object":obj}
	return render(request,template_name,context) 


def blog_post_list_view(request):
	qs_list = BlogPost.objects.all().published()
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(shop_name=request.user)
		qs_list = (my_qs | qs_list).distinct()
	template_name = "blog/blog_post_list.html"
	
	paginator = Paginator(qs_list,8)

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {"object_list":qs}
	return render(request,template_name,context)


def blog_post_list_user_view(request):
	qs_list = BlogPost.objects.filter(shop_name=request.user)
	template_name = "blog/user_posts.html"
	
	paginator = Paginator(qs_list,2)

	page = request.GET.get('page')
	try:
		qs = paginator.page(page)
	except PageNotAnInteger:
		qs = paginator.page(1)
	except EmptyPage:
		qs = paginator.page(paginator.num_pages)
	context = {"object_list":qs_list}
	return render(request,template_name,context)

@login_required
def blog_post_create_view(request):	
	template_name = "blog/blog_post_create.html"
	form = BlogPostModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = BlogPostModelForm()
	context = {"form":form}
	return render(request,template_name,context)



def blog_post_detail_view(request,slug):
	obj = get_object_or_404(BlogPost,slug=slug)
	template_name = "blog/blog_post_detail.html"
	share_string = quote_plus(obj.product_description)

	#comments
	initial_data = {
		"content_type":obj.get_content_type.model,
		"object_id":obj.id
	}
	comment_form = CommentForm(request.POST or None,initial=initial_data)
	if comment_form.is_valid() and request.user.is_authenticated:
		c_type = comment_form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = comment_form.cleaned_data.get('object_id')
		content_data = comment_form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()


		new_comment, created = Comment.objects.get_or_create(
							user = request.user,
							content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,
						)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


	content_type = ContentType.objects.get_for_model(BlogPost)
	obj_id = obj.id 
	comments = obj.comments
	context = {"object":obj,"share_string":share_string,"comments":comments,"comment_form":comment_form}
	return render(request,template_name,context)  



@user_is_entry_author
def blog_post_update_view(request,slug):
	obj = get_object_or_404(BlogPost,slug=slug)
	item = BlogPost.objects.get(slug=slug)
	template_name = "blog/form.html"
	form = BlogPostModelForm(request.POST or None,instance=obj)
	context = {"form":form,"title":f"update {obj.product_name}"}
	if form.is_valid(): 
		form.save()
	return render(request,template_name,context)


'''class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin):
	model = BlogPost
	fields = ['title','email','slug','content','published_date','image','price']

    def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True 
		return False'''

@staff_member_required
def blog_post_delete_view(request,slug):
	obj = get_object_or_404(BlogPost,slug=slug)
	template_name = "blog/blog_post_delete.html"
	context = {"object":obj}
	if request.method == "POST":
		obj.delete()
		return redirect("/about")
	return render(request,template_name,context)  

def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
	return render(request,"blog/form.html",{'form':form})

def FrontPage(request):
	return render(request,'blog/fp.html') 

def loginbuyer(request):
	return render(request,'blog/buyer.html')

def seller(request):
	return render(request,'blog/seller.html')
