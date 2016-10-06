from django.db import models
from django.contrib import admin

# Create your models here.
class BlogPost(models.Model):
    #bugId=models.CharField(primary_key=True,max_length=10)
    title=models.CharField(max_length=150)
    body =models.TextField()
    img = models.ImageField(null=True,blank=True,upload_to='upload')
    timestamp = models.DateTimeField()

'''class Meta:
    db_table = 'BlogPost'''''

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(BlogPost,BlogPostAdmin)