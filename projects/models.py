from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class", blank=True)
    logo = models.ImageField(upload_to='technologies/', blank=True, null=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')
    technologies = models.ManyToManyField(Technology, related_name='projects')
    client_name = models.CharField(max_length=200)
    client_website = models.URLField(blank=True, null=True)
    featured_image = models.ImageField(upload_to='projects/featured/')
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    short_description = models.TextField()
    full_description = HTMLField()
    challenge = HTMLField(blank=True)
    solution = HTMLField(blank=True)
    results = HTMLField(blank=True)
    live_url = models.URLField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', 'order', '-completion_date']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')
    title = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"
        
    def __str__(self):
        return f"{self.project.title} - {self.title if self.title else f'Image {self.id}'}"

class ProjectTestimonial(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='testimonials')
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    
    class Meta:
        verbose_name = "Project Testimonial"
        verbose_name_plural = "Project Testimonials"
        
    def __str__(self):
        return f"{self.project.title} - {self.client_name}"
