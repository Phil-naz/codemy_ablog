from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField(null=True, blank=True)
	profile_pic = models.ImageField(null=True, blank=True, upload_to="theblog_images/profile/")
	website_url = models.CharField(max_length=255, null=True, blank=True)
	vk_url = models.CharField(max_length=255, null=True, blank=True)
	facebook_url = models.CharField(max_length=255, null=True, blank=True)
	twitter_url = models.CharField(max_length=255, null=True, blank=True)
	instagram_url = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return str(self.user)   # name of 1 record in admin panel

	def get_absolute_url(self):   # for redirects after adding data to table
		# return reverse('article-detail', args=(str(self.id)))
		return reverse('theblog_home')


class Post(models.Model):
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to="theblog_images/")
	title_tag = models.CharField(max_length=255, default="Here write default")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	# body = models.TextField(blank=True, null=True)
	body = RichTextField(blank=True, null=True)
	post_date = models.DateField(auto_now_add=True)   # Auto date of adding data. You need import this
	category = models.CharField(max_length=255, default='coding')
	snippet = models.CharField(max_length=255)
	likes = models.ManyToManyField(User, related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + ' | ' + str(self.author)   # name of 1 record in admin panel

	def get_absolute_url(self):   # for redirects after adding data to table
		# return reverse('article-detail', args=(str(self.id)))
		return reverse('theblog_home')


	class Meta:
		ordering = ['-id', 'title']

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)
