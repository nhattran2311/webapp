from django.shortcuts import render
from blog.models import Post
from json import dumps

def pie_chart(request):
    labels = []
    data = []

    query_set = Post.objects.order_by('-date_posted')
    for post in query_set:
        labels.append(post.author)
        data.append(post.id)
    context = {
        'labels': labels,
        'data': data,
    }
    return render(request, 'dashboard/pie_chart.html',context)