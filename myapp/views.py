from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timezone

from .models import Post

def index(request):
	posts = Post.objects.all()
	for i in posts:
		diff = int((datetime.now(timezone.utc) - (i.created)).days)
		if diff==1:
			i.latest = True
	context = Post.objects.order_by('-created')[:5]
	return render(request, 'myapp/index.html', {'context' : context, 'posts' : posts})