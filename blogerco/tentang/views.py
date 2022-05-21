from django.shortcuts import render

def tentang(request):
	context ={
		'judul':'Tentang',
		'subjudul':'TENTANG',
		'contact':
			'phone  : +62882282268'

			'email  : leonyd915@gamil.com',

		'nav':[
			['/','Home'],
			['/blog','Blog'],
			['/tentang','Tentang'],
		]
	}
	return render(request,'tentang.html',context)
