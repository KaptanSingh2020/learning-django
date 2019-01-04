from django.db import models
from django.core.urlresolvers import reverse

class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organizer_tag_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class Startup(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField()
    description = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()
    website = models.URLField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def get_absolute_url(self): # Here reverse() is used with args, not kwargs. 
        return reverse('organizer_startup_detail', args=(self.slug,))

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'


class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup) # many to one relationship (many news links to one startup)

    def __str__(self):
        return "{} : {}".format(self.startup, self.title)

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

