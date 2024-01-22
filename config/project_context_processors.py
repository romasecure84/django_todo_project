from todo.models import Category

def global_category_context(request):
    # global_categories=Category.objects.all() # bu butun kategoriyalari gostermek ucundur
    return dict(
        global_categories=Category.objects.filter(is_active=True)
    )
