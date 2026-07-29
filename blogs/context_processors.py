from . models import Category,SociaLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories = categories)

def get_social_link(request):
    social_links = SociaLink.objects.all()
    return dict(social_links = social_links)
