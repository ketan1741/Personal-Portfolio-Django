from os import major
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
        ordering = ['id']
    
    name = models.CharField(max_length=30, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    image_filename = models.CharField(max_length=100, blank=True, null=True)
    is_coding_skill = models.BooleanField(default=False)
    is_key_interest = models.BooleanField(default=False)
    is_framework = models.BooleanField(default=True)
    is_webtech = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    image_filename = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")
    cv_filename = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"].reverse()
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    subject = models.CharField(verbose_name="Subject",max_length=300)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'



class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["start_year"].reverse()

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    image_filename = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    program = models.CharField(max_length=200, blank=True, null=True)
    major = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    start_year = models.DateField(blank=True, null=True)
    end_year = models.DateField(blank=True, null=True)
    cgpa = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["priority"]
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    image_filename = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, max_length=500)
    is_active = models.BooleanField(default=True)
    show_git = models.BooleanField(default=True)
    git_link = models.CharField(max_length=500, blank=True, null=True)
    priority = models.IntegerField(("Priority"), blank=True, null= True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=False)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, max_length=500)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    image_filename = models.CharField(max_length=100, blank=True, null=True)
    to_display = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    doi_link = models.CharField(max_length=500, blank=True, null=True)
    research_gate_link = models.CharField(max_length=500, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    verification_link = models.CharField(max_length=500, blank = True, null=True)
    course_link = models.CharField(max_length=500, blank = True, null=True)


class Experience(models.Model):

    class Meta:
        verbose_name_plural = 'Experiences'
        verbose_name = 'Experience'
        ordering = ['id']

    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    certificate_link = models.CharField(max_length=500, blank = True, null=True)
    course_link = models.CharField(max_length=500, blank = True, null=True)

    def __str__(self):
        return self.name