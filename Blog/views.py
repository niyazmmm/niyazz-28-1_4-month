from django.shortcuts import render

# Create your views here.
def posts_view(request):
    if request.method == 'GET':
        hashtag_id = request.GET.get('hashtag_id')
        if hashtag_id:
            posts = Post.objects.filter(hashtag=Hashtag.objects.get(id=hashtag_id))
        else:
            posts = Post.objects.all()
        context = {
            'posts': Post.objects.all()
            'posts': posts
        }
        return render(request, 'posts/posts.html', context=context)


def hashtags_view(request):
def hashtags_view(request, **kwargs):
    if request.method == 'GET':
        context = {
            'hashtags': Hashtag.objects.all()
@@ -25,6 +30,6 @@ def detail_view(request, **kwargs):
        print(post.title)
        data = {
            'post': post,
            'comments': Comment.objects.filter(post_id=kwargs['id'])
            'comments': Comment.objects.filter(id=kwargs['id'])
        }
        return render(request, 'posts/detail.html', context=data)