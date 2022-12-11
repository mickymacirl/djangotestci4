from django.views import generic
from .models import Post

# "This view will return a list of Post objects, published, ordered by the created_on field."
# 
# The queryset attribute is used to specify the query set that will be used to retrieve objects for
# the view. In this case, we're using the Django ORM to filter the Post model by the status field, and
# then order the results by the created_on field
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# "The PostDetail view will display the details of a particular type of object, in this case, a blog
# post, and it will use a template called post_detail.html."
# 
# The DetailView generic view expects the primary key value captured from the URL to be called "pk",
# so we've changed question_id to pk for the generic views
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
