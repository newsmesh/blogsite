from django.shortcuts import render
from blog.models import Blog
from . import scrap

# Create your views here.
def refresh_page(request):
	if request.method == 'POST':
		list_of_links =  scrap.get_links()
		for i in range(0, len(list_of_links)):
			scrap.pargraph(list_of_links[i])
	return render(request, 'refresh.html')

def home(request):
    # s = Blog.objects.filter(slug=slug)
    # context = {'s': s}
    return render(request, 'index.html')


def blog(request):
    blogs = Blog.objects.all()
    print('----------')
    print(blogs[6].category)
    context = {'blogs': blogs}
    return render(request, 'bloghome.html', context)


def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first
    context = {'blog': blog}
    # return HttpResponse(f"this is {slug}")
    return render(request, 'blogpost.html', context)


def contact(request):
    return render(request, 'contact.html')


def search(request):
    return render(request, 'search.html')
