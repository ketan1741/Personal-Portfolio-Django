from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate,
		Experience
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True).order_by('id')
		portfolio = Portfolio.objects.filter(is_active=True)
		experiences = Experience.objects.filter(is_active = True)
		
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		context["experiences"] = experiences
  
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
		

	def form_valid(self, form):
		subj = form.cleaned_data['subject']
		sender_mail = form.cleaned_data['subject']
		
		nam = form.cleaned_data['name']
		emai = form.cleaned_data['email']
		messag = form.cleaned_data['message']
			
		final_message = "From Person Name:  "+nam
		final_message += "\n\nFrom Person Email:  "+emai
		final_message += "\n\nEmail Subject:  "+subj
		final_message += "\n\n\nEmail Message:\n\n"+messag

  
		try:
			send_mail("Django Resume App - "+subj, final_message, 'from_mail', ['to_mail'])
			form.save()
			messages.success(self.request, 'Thank you! I will be in touch soon.')
			return super().form_valid(form)
						
   
		except:
			form.save()
			messages.success(self.request, 'Thank you! I will be in touch soon.')
			return super().form_valid(form)



	def form_invalid(self, form):
		messages.error(self.request, 'Please try again. Invalid Email ID :(')
		return super().form_invalid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True).order_by('priority')


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True).order_by('id')


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"
