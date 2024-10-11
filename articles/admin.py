from .models import Articles, Topics, Claps
from django.contrib import admin


admin.site.register([Articles, Topics, Claps])