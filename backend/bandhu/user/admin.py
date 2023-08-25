from django.contrib import admin
from .models import Question, Sentiments  # Import your models

admin.site.register(Question)
admin.site.register(Sentiments)
# Register your models here.
