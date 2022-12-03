from django.contrib import admin
from content.models import *

admin.site.register([
    Blog,
    Comment,
    Newsletter
])