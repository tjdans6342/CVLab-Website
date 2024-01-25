# count_posts.py
 
def main():
    posts = Post.objects.all()
    print(f"There are {posts.count()} posts in the database")
 
 
if __name__ == "__main__":
    import os
 
    from django.core.wsgi import get_wsgi_application
 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvlab_project.settings")
    application = get_wsgi_application()
 
    from post.models import Post
 
    main()