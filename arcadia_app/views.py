from django.shortcuts import render, redirect

from django.views.generic import TemplateView, ListView, View
from arcadia_app.models import Post, Event

from arcadia_app.forms import  ContactForm
from django.contrib import messages

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
        