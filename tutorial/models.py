from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True, blank=True)
    update_date = models.DateTimeField('Last Updated')
    about = RichTextField(blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    CATEGORIES = (
        ('',''),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('bootstrap', 'BOOTSTRAP'),
        ('sass', 'SASS'),
        ('flexbox', 'FLEXBOX'),
        ('javascript', 'JAVASCRIPT'),
        ('jquery', 'JQUERY'),
        ('ajax', 'AJAX'),
        ('json', 'JSON'),
        ('react', 'REACT'),
        ('angular', 'ANGULAR'),
        ('nodejs', 'NODEJS'),
        ('vuejs', 'VUEJS'),
        ('graphql', 'GRAPHQL'),
        ('php', 'PHP'),
        ('laravel', 'LARAVEL'),
        ('codeigniter', 'CODEIGNITER'),
        ('asp', 'ASP'),
        ('python', 'PYTHON'),
        ('django', 'DJANGO'),
        ('flask', 'FLASK'),
        ('numpy', 'NUMPY'),
        ('scipy', 'SCIPY'),
        ('pandas', 'PANDAS'),
        ('matplotlib', 'MATPLOTLIB'),
        ('tensorflow', 'TENSORFLOW'),
        ('pytorch', 'PYTORCH'),
        ('scikitlearn', 'SCIKITLEARN'),
        ('keras', 'KERAS'),
        ('opencv', 'OPENCV'),
        ('tkinter', 'TKINTER'),
        ('qt', 'QT'),
        ('pygame', 'PYGAME'),
        ('kivy', 'KIVY'),
        ('sql', 'SQL'),
        ('mysql', 'MYSQL'),
        ('postgresql', 'POSTGRESQL'),
        ('java', 'JAVA'),
        ('git', 'GIT'),
        ('android', 'ANDROID'),
        ('ios', 'IOS'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    body = RichTextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    category = models.CharField(max_length=20,
                              choices=CATEGORIES,
                              blank=True)
    
    nextpost = models.URLField(max_length=200, blank=True)
    previouspost = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
