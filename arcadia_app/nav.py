from arcadia_app.models import Category, Post, Tag


def navigation(request):
    # tags = Tag.objects.all()[:12]
    # categories = Category.objects.all()[:6]
    # trending_posts = Post.objects.filter(
    #     published_at__isnull = False, status = "active"
    # ).order_by("-views_count")[:3]

    side_categories = Category.objects.all()[:6]
    
    popular_posts = Post.objects.filter(
            published_at__isnull = False, status = "active"
        ).order_by("-views_count","-published_at")[:7]

    return{
        # "tags" : tags,
        # "categories": categories,
        "side_categories": side_categories,
        # "trending_posts": trending_posts,
        "recent_posts": popular_posts,
            
    }