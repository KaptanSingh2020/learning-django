from django.db import models
from organizer.models import Tag, Startup
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class MyModel(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class AnotherModel(models.Model):
    mymodel = GenericRelation(MyModel)

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63, 
        help_text='a label for URL config', 
        unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField(
        'date published',
        auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')
# When we set the related name attribute of a relationship field we are changing the name of 
# the variable Django creates (post_set) for the relation on the other model (the reverse relation).
    
    def __str__(self):
        return "{} on {}".format(
            self.title, 
            self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=(self.pub_date.year, self.pub_date.month, self.slug))

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'
        permissions = (
            ("view_future_post", "Can view unpublished Post"),
            ("view_post", "Can view Post")
            )
