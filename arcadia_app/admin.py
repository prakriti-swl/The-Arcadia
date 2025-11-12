from django.contrib import admin
from .models import Post, Category, Tag, Comment, Event, Newsletter, Reservation, Contact
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Newsletter)
admin.site.register(Reservation)
admin.site.register(Contact)