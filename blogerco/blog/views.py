from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
	context ={
		'judul':'Blog',
		'subjudul':'BLOG',
		'nav': [
			['/','Home'],
			['/blog','Blog'],
			['/tentang','Tentang'],
		]
	}
	
	return render(request,'blog.html',context)
def posttext(request):
	return render(request,'posttext.html')
def postimage(request):
	return render(request,'postimage.html')