from django.urls import path


from . import views

urlpatterns= [
	path('tentang/',views.tentang,name='tentang.html'),

]