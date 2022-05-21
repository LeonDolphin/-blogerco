from django.urls import path

from . import views


urlpatterns=[
		#path('',views.blog),
		path('blog/',views.blog,name='blog.html'),
		path('PostText/',views.posttext,name='posttext.html'),
		path('PostImage/',views.postimage),
	
		
]