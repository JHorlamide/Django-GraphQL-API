import strawberry
from typing import List

from .models import BlogPost
from .types import BlogPostType

# Query
@strawberry.type
class Query():
  
  @strawberry.field
  def get_posts(self, title: str=None) -> List[BlogPostType]:
    if title:
      posts = BlogPost.objects.filter(title=title)
      return posts
    
    return BlogPost.objects.all()


  @strawberry.field
  def get_post_by_id(self, id: int) -> BlogPostType:
    post = BlogPost.objects.get(id=id)
    return post
  
  
  @strawberry.field
  def get_post_by_limit(self, limit: int) -> List[BlogPostType]:
    posts = BlogPost.objects.all()[:limit]
    return posts
  

# Mutation
@strawberry.type
class Mutation():
  
  @strawberry.field
  def create_post(self, title: str, author: str, message: str) -> BlogPostType:
    post = BlogPost(title=title, author=author, message=message)
    post.save()
    return post
  
  
  @strawberry.field
  def update_post(self, id: int, title: str, author: str, message: str) -> BlogPostType:
    post = BlogPost.objects.get(id=id)
    
    if post is not None:
      post.title = title
      post.author = author
      post.message = message
      post.save()
      return post
    
    return { "message": "Post Not found" }
  
  
  @strawberry.field
  def delete_post(self, id: int) -> bool:
    post = BlogPost.objects.get(id=id)
    
    if post is not None:
      post.delete()
      return True
    
    return { "message": "Post Not found" }


# Schema
schema = strawberry.Schema(query=Query,  mutation=Mutation, subscription=None)
