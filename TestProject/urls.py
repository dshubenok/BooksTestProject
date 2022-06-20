from django.contrib import admin
from django.urls import path, include

api_views = [
    path('api/v1/books/', include('books.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += api_views
