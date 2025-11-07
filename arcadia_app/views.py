from django.shortcuts import render, redirect

from django.views.generic import TemplateView, ListView, View, DetailView
from arcadia_app.models import Post, Event, Category 

from arcadia_app.forms import  ContactForm, NewsletterForm, CommentForm
from django.contrib import messages
from django.http import JsonResponse
class HomeView(TemplateView):
    template_name = "arcadia/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Static slider images
        context['slider_images'] = [
            "arcadia/images/slide1-01.jpg",
            "arcadia/images/master-slides-02.jpg",
            "arcadia/images/master-slides-01.jpg",
        ]

        # Intro Images / Items
        context['intro_items'] = [
            {
                "title": "Breath Taking Views",
                "description": "Phasellus lorem enim, luctus ut velit eget, con-vallis egestas eros.",
                "image": "arcadia/images/intro-01.jpg",
                "link": "#"
            },
            {
                "title": "Delicious Food",
                "description": "Aliquam eget aliquam magna, quis posuere risus ac justo ipsum nibh urna.",
                "image": "arcadia/images/intro-02.jpg",
                "link": "#"
            },
            {
                "title": "Red Wines You Love",
                "description": "Sed ornare ligula eget tortor tempor, quis porta tellus dictum.",
                "image": "arcadia/images/intro-04.jpg",
                "link": "#"
            },
        ]
        # To display blogs in the home page
        context["popular_posts"]= Post.objects.filter(
            published_at__isnull = False, status = "active"
        ).order_by("-published_at")[:7]

        # # Fetch Events from Database for Slider
        # context['events'] = Event.objects.all()

        return context


class EventSliderView(ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'


class IntroSectionView(TemplateView):
    template_name = 'booking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['intro_items'] = [
            {
                "title": "Breath Taking Views",
                "description": "Phasellus lorem enim, luctus ut velit eget, con-vallis egestas eros.",
                "image": "arcadia/images/intro-01.jpg",
                "link": "#"
            },
            {
                "title": "Delicious Food",
                "description": "Aliquam eget aliquam magna, quis posuere risus ac justo ipsum nibh urna.",
                "image": "arcadia/images/intro-02.jpg",
                "link": "#"
            },
            {
                "title": "Red Wines You Love",
                "description": "Sed ornare ligula eget tortor tempor, quis porta tellus dictum.",
                "image": "arcadia/images/intro-04.jpg",
                "link": "#"
            },
        ]

        return context

class AboutView(TemplateView):
    template_name = "arcadia/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Static slider images
        context['about_images'] = [
            "arcadia/images/slide1-01.jpg",
            "arcadia/images/master-slides-02.jpg",
            "arcadia/images/master-slides-01.jpg",
        ]

class MenuView(TemplateView):
    template_name = "arcadia/home/menu.html"


class DetailedMenuView(TemplateView):
    template_name = "arcadia/detailed_menu.html"

class BookingView(TemplateView):
    template_name = "arcadia/home/booking.html"

class GalleryView(TemplateView):
    template_name = "arcadia/gallery.html"


class ContactView(View):
    template_name = "arcadia/contact.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully submitted your query. We will contact you soon."
            )
            return redirect("contact")
        else:
            messages.error(
                request, "Cannot submit your query. Please make sure all fields are valid.",
            )
            return render(
                request,
                self.template_name,
                {"form": form},
            )
    
class PostListView(ListView):
    model = Post
    template_name = "arcadia/list/list.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(
            published_at__isnull = False, status = "active"
        ).order_by("-published_at")


class PostDetailView(DetailView):
    model = Post
    template_name = "arcadia/blog/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(published_at__isnull = False, status = "active")
        return query
    

# class NewsletterView(View):
#     def post(self, request):
#         is_ajax = request.headers.get("x-requested-with")
#         if is_ajax == "XMLHttpRequest":
#             form = NewsletterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return JsonResponse(
#                     {
#                         "success": True,
#                         "message": "Successfully subscribed to newsletter.",
#                     },
#                     status = 201,
#                 )
#             else:
#                 return JsonResponse(
#                     {
#                         "success": False,
#                         "message": " Cannot subscribe to the newsletter.",
#                     },
#                     status = 400,
#                 )
#         else:
#             return JsonResponse(
#                 {
#                     "success": False,
#                     "message": " Cannot process. Must be an AJAX XMLHttpRequest",
#                 },
#                 status = 400,
#             )
        


# class NewsletterView(View):
#     def post(self, request):
#         form = NewsletterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Successfully subscribed to newsletter.")
#         else:
#             messages.error(request, "Email already exists or invalid.")
#         return redirect("home")


class NewsletterView(View):
    def post(self, request):
        form = NewsletterForm(request.POST)
        is_ajax = request.headers.get("x-requested-with") == "XMLHttpRequest"

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Successfully subscribed to newsletter.")
            except:
                messages.error(request, "Email already subscribed.")
        else:
            messages.error(request, "Invalid email address.")

        return redirect("home")
    
class PostByCategoryView(ListView):
    model = Post
    template_name = "arcadia/list/list.html"
    context_object_name = "posts"
    # paginate_by = 1

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull =  False, status = "active", category__id = self.kwargs["category_id"],
        ).order_by("-published_at")

        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add all categories to the context
        context["categories"] = Category.objects.all()
        # optionally add current category
        context["current_category"] = Category.objects.get(id=self.kwargs["category_id"])
        return context
    

from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q

class PostSearchView(View):
    template_name = "arcadia/list/list.html"

    def get(self, request, *args, **kwargs):
        query = request.GET["query", ""]
        post_list = Post.objects.filter(
        (Q(title__icontains= query) | Q(content__icontains= query))
        & Q(status = "active")
        & Q(published_at__isnull = False)
        ).order_by("-published_at")

        page = request.GET.get("page", 1)
        paginate_by = 3
        paginator = Paginator(post_list, paginate_by)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        return render(
            request,
            self.template_name,
            {"page_obj":posts, "query": query},
        )
    
class CommentView(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        # post_id = request.POST["post"]
        if form.is_valid():
            post = Post.objects.get(id=request.POST.get("post"))
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post.get_absolute_url())
        else:
            post = Post.objects.get(id=request.POST.get("post"))
            return render(request, "arcadia/detail/comment.html", {"form": form, "post": post})
        

class VideoView(TemplateView):
    template_name = 'arcadia/video.html'