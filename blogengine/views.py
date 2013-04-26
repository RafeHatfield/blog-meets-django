from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from blogengine.models import Post

def getPosts(request, selected_page=1):
    # Get all blog posts
    posts = Post.objects.all().order_by('-pub_date')

    # Add pagination
    pages = Paginator(posts, 5)
    returned_page = pages.page(selected_page)

    # Display all the posts
    return render_to_response('posts.html', {'posts':returned_page.object_list})

def getPost(request, postSlug):
    # Get specified post
    post = Post.objects.filter(slug=postSlug)

    # Display specified post
    return render_to_response('posts.html', { 'posts':post})