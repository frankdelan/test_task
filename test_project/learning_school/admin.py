from django.contrib import admin

from learning_school.models import Author, Access, Lesson, Product, UserGroup

# Register your models here.
admin.site.register(Author)
admin.site.register(Access)
admin.site.register(Lesson)
admin.site.register(Product)
admin.site.register(UserGroup)
