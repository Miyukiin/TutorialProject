from django.contrib import admin
from .models import Question, Choice
from django.apps import apps

# Get all the models from your app
app = apps.get_app_config('polls')  # Replace 'polls' with your app name

# Register all models
for model in app.get_models():
    admin.site.register(model)
