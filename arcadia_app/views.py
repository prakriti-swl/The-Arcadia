from django.shortcuts import render, redirect

from django.views.generic import TemplateView, ListView, View, DetailView
from arcadia_app.models import Newsletter, Post, Event, Category , Reservation

from arcadia_app.forms import  ContactForm, NewsletterForm, CommentForm, ReservationForm
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime



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
        context["home_posts"]= Post.objects.filter(
            published_at__isnull = False, status = "active"
        ).order_by("-published_at","-views_count")[:3]

        # === Add Event Data for Slider ===
        # Events sorted by upcoming time
        # now = timezone.now()
        # context["events"] = Event.objects.filter(event_time__gte=now).order_by("event_time")

        context["events"] = Event.objects.filter(event_time__gte=timezone.now()).order_by("event_time")

        # print("Events in HomeView:", context["events"])

        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'arcadia_app/event_detail.html'
    context_object_name = 'event'


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

# class MenuView(TemplateView):
    # template_name = "arcadia/home/menu.html"


class DetailedMenuView(TemplateView):
    template_name = "arcadia/detailed_menu.html"



class ReservationView(TemplateView):
    template_name = "arcadia/reservation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReservationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)


       # accept either DD/MM/YYYY or MM/DD/YYYY automatically
        raw_date = request.POST.get("date")
        try:
            # Try parsing as DD/MM/YYYY first (your input)
            date = datetime.strptime(raw_date, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            # Fallback if calendar sends MM/DD/YYYY (in some browsers)
            date = datetime.strptime(raw_date, "%m/%d/%Y").strftime("%Y-%m-%d")

        # Update form data so Django saves correct date
        form.data = form.data.copy()
        form.data['date'] = date

        time = request.POST.get('time')
        email = request.POST.get('email')

        #  Check for existing reservation
        existing = Reservation.objects.filter(date=date, time=time, email=email).first()

        if existing:
            # redirect with query param instead of messages
            return redirect(f"{request.path}?error=exists&date={date}&time={time}")

        if form.is_valid():
            form.save()
            # redirect with query param instead of message framework
            return redirect(f"{request.path}?success=true")
        else:
            return redirect(f"{request.path}?error=invalid")

    


class ContactView(View):
    template_name = "arcadia/contact.html"

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Message sent successfully!"})
        else:
            # Collect missing fields
            missing_fields = [field for field in form.errors]
            message = "Message wasn't sent. Please fill: " + ", ".join(missing_fields)
            return JsonResponse({"status": "error", "message": message})
        
        
    
class PostListView(ListView):
    model = Post
    template_name = "arcadia/list/list.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(
            published_at__isnull = False, status = "active"
        ).order_by("-published_at")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add popular posts (e.g., top 5 by views)
        context["popular_posts"] = Post.objects.filter(
            published_at__isnull=False,
            status="active"
        ).order_by("-views_count")[:5]

        # All categories for sidebar
        context["categories"] = Category.objects.all()

        # No current_category on list page
        context["current_category"] = None

        return context

 
class PostDetailView(DetailView):
    model = Post
    template_name = "arcadia/blog/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        # Only fetch active posts that are published
        return super().get_queryset().filter(
            published_at__isnull=False, status="active"
        )
    
    # Increment view count when post is viewed
    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.views_count += 1           # increment view count
        post.save(update_fields=["views_count"])  # only update views field
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Sidebar
        context["categories"] = Category.objects.all()

        # Popular posts
        context["popular_posts"] = Post.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-views_count")[:5]

        # No current_category on detail page
        context["current_category"] = None

        return context  

class NewsletterView(View):
    def post(self, request):
        form = NewsletterForm(request.POST)
        is_ajax = request.headers.get("x-requested-with") == "XMLHttpRequest"

        email = request.POST.get('email')
        email_exists = Newsletter.objects.filter(email=email).exists()

        if is_ajax:  # Only handle AJAX results here
            if form.is_valid():
                form.save()
                return JsonResponse(
                    {"success": True, "message": "Successfully subscribed to newsletter!"}
                )

            if email_exists:
                return JsonResponse(
                    {"success": False, "message": "Email already subscribed."},
                    status=400
                )

            return JsonResponse(
                {"success": False, "message": "Invalid email address."},
                status=400
            )

        # Non-AJAX fallback
        if form.is_valid():
            form.save()
        return redirect("home")


    
class PostByCategoryView(ListView):
    model = Post
    template_name = "arcadia/list/list.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(
            published_at__isnull=False,
            status="active",
            category__id=self.kwargs["category_id"]
        ).order_by("-published_at")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Sidebar: all categories
        context["categories"] = Category.objects.all()
        
        # Current selected category
        context["current_category"] = Category.objects.get(id=self.kwargs["category_id"])
        
        # Popular posts
        context["popular_posts"] = Post.objects.filter(
            published_at__isnull=False,
            status="active"
        ).order_by("-views_count")[:5]

        return context

from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q

class PostSearchView(View):
    template_name = "arcadia/list/list.html"

    def get(self, request, *args, **kwargs):
        # Safely get query param
        query = request.GET.get("query", "").strip()

        # Only filter if query is not empty
        if query:
            post_list = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).order_by("-published_at")
        else:
            post_list = Post.objects.none()

        print("Search query:", query)
        print("Found posts:", post_list.count())

        # Pagination
        page = request.GET.get("page", 1)
        paginator = Paginator(post_list, 3)  # 3 posts per page

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except Exception:
            posts = paginator.page(paginator.num_pages)

        # Render
        return render(
            request,
            self.template_name,
            {
                "page_obj": posts,
                "posts": posts,
                "query": query,
            },
        )
    
# class CommentView(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post_id = request.POST["post"]

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return redirect('home')  # fallback

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            # REDIRECT WITHOUT ERROR
            return redirect(post.get_absolute_url())

        return render(
            request,
            "arcadia/blog/left/comment.html",
            {"form": form, "post": post}
        )


class CommentView(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post_id = request.POST.get("post")

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            # ✅ CHANGED: handle missing post safely
            return redirect("/?error=invalid_post")

        # ✅ CHANGED: form validation + success/error redirects
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            # ✅ Redirect with success parameter (no get_absolute_url)
            return redirect(f"/blog/{post.id}/?success=comment")
        else:
            # ✅ Collect which fields have errors
            missing_fields = [field.label for field in form if field.errors]
            missing_str = ",".join(missing_fields) if missing_fields else "fields"

            # ✅ Redirect back with error + missing field info
            return redirect(f"/blog/{post.id}/?error=invalid&missing={missing_str}")

class GalleryView(TemplateView):
    template_name = "arcadia/gallery.html"


class VideoView(TemplateView):
    template_name = 'arcadia/video.html'