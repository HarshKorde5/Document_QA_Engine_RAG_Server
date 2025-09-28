
from django.contrib import admin
from django.urls import path
# Import settings and static for serving uploaded media files
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Map all URLs starting with 'documents/' to the documents app
    path('', include('documents.urls')), 
]
