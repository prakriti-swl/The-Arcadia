from django.shortcuts import render

from arcadia_app.models import Post

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "arcadia/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider_images'] = [
            "arcadia/images/slide1-01.jpg",
            "arcadia/images/master-slides-02.jpg",
            "arcadia/images/master-slides-01.jpg",
        ]

        context['intro_images'] = [
            "arcadia/images/intro-01.jpg",
            "arcadia/images/intro-02.jpg",
            "arcadia/images/intro-04.jpg",
        ]

        context['event_images'] = [
            "arcadia/images/bg-event-01.jpg",
            "arcadia/images/bg-event-02.jpg",
            "arcadia/images/bg-event-04.jpg",
        ]

        context['inner_event_images'] = [
            "arcadia/images/event-02.jpg",
            "arcadia/images/event-06.jpg",
            "arcadia/images/event-01.jpg",
        ]



        return context
    



















# def menu(request):
#     return render(request, "arcadia/menu.html")

# def review(request):
#     return render(request, "arcadia/review.html")

# def event(request):
#     return render(request, "arcadia/event.html")

# def gallery(request):
#     return render(request, "arcadia/gallery.html")

# def booking(request):
#     return render(request, "arcadia/booking.html")