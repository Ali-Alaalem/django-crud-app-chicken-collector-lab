from django.contrib import admin
# Add Feeding to the import
from .models import Chicken, Eggs

admin.site.register(Chicken)
# Register the new Feeding model
admin.site.register(Eggs)