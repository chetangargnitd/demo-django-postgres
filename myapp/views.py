from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timezone
from django.db.models import Q

from .models import Post

def index(request):
	posts = Post.objects.all()
	for i in posts:
		diff = int((datetime.now(timezone.utc) - (i.created)).days)
		if diff==1:
			i.latest = True
	context = Post.objects.order_by('-created')[:5]

	return render(request, 'myapp/index.html', {'context' : context, 'posts' : posts})


def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'myapp/search.html', context)

        else:
            return render(request, 'myapp/search.html')

    else:
        return render(request, 'myapp/search.html')
