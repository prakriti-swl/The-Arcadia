from django.db import models
from django.utils.text import slugify

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True


class Category(TimeStampModel):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    

class Tag(TimeStampModel):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    

class Post(TimeStampModel):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("in_active", "Inactive"),
    ]
    title = models.CharField(max_length= 200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_image/%y/%m/%d", blank= False)
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default="active")
    views_count = models.PositiveBigIntegerField(default=0)
    published_at = models.DateTimeField(null = True, blank = True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(TimeStampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email} |  {self.comment[:70]}"
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post-detail', kwargs={'pk': self.pk})
    

# Event model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_time = models.DateTimeField()
    background_image = models.ImageField(upload_to='events/backgrounds/')
    event_image = models.ImageField(upload_to='events/images/')
    # slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         base_slug = slugify(self.title)
    #         slug = base_slug
    #         num = 1
    #         # Ensure uniqueness
    #         while Event.objects.filter(slug=slug).exists():
    #             slug = f"{base_slug}-{num}"
    #             num += 1
    #         self.slug = slug
    #     super().save(*args, **kwargs)

    # def short_description(self, length=100):
    #     """Return a truncated description for previews."""
    #     return self.description[:length] + "..." if len(self.description) > length else self.description
    

class Contact(TimeStampModel):
    message = models.TextField()
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    subject = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    
class Newsletter(TimeStampModel):
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.email



class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(max_length=20)
    people = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"