from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Post


from datetime import timedelta
from django.utils import timezone

def index(request):
	Previous_Date = timezone.now().date() - timedelta(days=1)
	posts = Post.objects.filter(created__gte = Previous_Date, created__lte = timezone.now().date())
	print(posts)
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
