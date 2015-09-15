from django.contrib import admin
from .models import Post

# register model created in models.py 
# so it is visible on the admin page
admin.site.register(Post)


