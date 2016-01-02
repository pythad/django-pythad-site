from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from personal_site.mixins import BackgroundMixin
from .models import Post, Subscriber


class Home(BackgroundMixin, ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = 'posts'


class PostDetailView(BackgroundMixin, DetailView):
    model = Post
    template_name = "blog/post.html"
    context_object_name = 'post'


class TaggedPostsListView(BackgroundMixin, ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])


@require_POST
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        if not Subscriber.objects.filter(email=email).exists():
            subscriber = Subscriber(email=email)
            subscriber.save()
            msg_txt = render_to_string('emails/sub_email.txt')
            msg_html = render_to_string('emails/sub_email.html')
            send_mail('Pythad Blog - Subscription confirmed', msg_txt,
                      settings.EMAIL_HOST_USER, [email], html_message=msg_html)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'exists'})
