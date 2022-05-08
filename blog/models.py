from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from tax_management_system import settings
class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,verbose_name = "User ")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Posted On:")
    blog_image = models.FileField(upload_to='uploads/images/', blank = True,null = True,verbose_name="Featured Image")
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-created_date']