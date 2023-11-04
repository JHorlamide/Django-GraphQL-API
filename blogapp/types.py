import strawberry
from .models import BlogPost

@strawberry.django.type(BlogPost)
class BlogPostType():
  id: int
  title: str
  author: str
  message: str
  
