
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns= [
	path('',views.index,name='index.hhtml'),
	path('',include ('blog.url')),
	path('',include ('tentang.urls')),
	path('admin/', admin.site.urls),
]
