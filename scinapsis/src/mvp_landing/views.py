from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from blog.models import Post

class HomeBlogView(ListView):
    template_name = 'home.html'
    model = Post
    queryset=Post.objects.filter(pinned=False).order_by("-created")[:3]

    def get_context_data(self, **kwargs):
        context = super(HomeBlogView, self).get_context_data(**kwargs)
        context['pinned'] = Post.objects.filter(pinned=True)
        return context

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)