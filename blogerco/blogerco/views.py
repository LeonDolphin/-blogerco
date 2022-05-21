from django.shortcuts import render

def index(request):
	context ={
		'judul':'Home',
		'subjudul':'BLOGERCO',
		'nav': [
			['/','Home'],
			['/blog','Blog'],
			['/tentang','Tentang'],
		]
	}
	
	return render(request,'index.html',context)